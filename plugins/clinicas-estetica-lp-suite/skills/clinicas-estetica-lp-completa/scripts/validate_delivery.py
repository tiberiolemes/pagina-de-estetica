#!/usr/bin/env python3
"""Validate the clinic planning delivery contract without network access.

This is a structural validator, not a review of medical efficacy or professional
advertising rules. Usage: python3 validate_delivery.py /path/to/output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ARTIFACTS = {
    "briefing": "00-briefing.json",
    "estrategia": "01-analise-estrategica.md",
    "copy": "02-copy.md",
    "design_system": "03-design-system.md",
    "direcao": "04-wireframe.md",
    "briefings": "05-briefings-imagens.md",
    "revisao": "06-revisao.md",
}
STATUSES = {
    "planejamento-concluido", "rascunho-com-pendencias", "aguardando-informacao"
}
SECTION_ID = re.compile(r"sec-[A-Za-z0-9][A-Za-z0-9._-]*\Z")
BRIEF_ID = re.compile(r"brief-[A-Za-z0-9][A-Za-z0-9._-]*\Z")
SAFE_BASENAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
SECTION_HEADING = re.compile(r"^## \[(sec-[^\]\s]+)\] (.+)$", re.MULTILINE)
BRIEF_HEADING = re.compile(r"^## \[(brief-[^\]\s]+)\] (.+)$", re.MULTILINE)


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        print(json.dumps({
            "valido": False,
            "status": None,
            "quantidade_secoes": 0,
            "quantidade_assets": 0,
            "problemas": [f"Argumentos inválidos: {message}"],
        }, ensure_ascii=False, indent=2))
        self.exit(1)


class Validator:
    def __init__(self, directory: Path):
        self.directory = directory.resolve()
        self.problems: list[str] = []
        self.manifest: dict[str, Any] = {}
        self.documents: dict[str, str] = {}
        self.section_count = 0
        self.asset_count = 0

    def error(self, location: str, message: str) -> None:
        self.problems.append(f"{location}: {message}")

    def string(self, value: Any, location: str) -> bool:
        if not isinstance(value, str) or not value.strip():
            self.error(location, "deve ser uma string não vazia")
            return False
        return True

    def array(self, value: Any, location: str) -> list[Any]:
        if not isinstance(value, list):
            self.error(location, "deve ser um array")
            return []
        return value

    def object(self, value: Any, location: str) -> dict[str, Any]:
        if not isinstance(value, dict):
            self.error(location, "deve ser um objeto JSON")
            return {}
        return value

    def boolean(self, value: Any, location: str) -> bool:
        if not isinstance(value, bool):
            self.error(location, "deve ser booleano (true ou false)")
            return False
        return True

    def enum(self, value: Any, choices: set[str], location: str) -> bool:
        if not isinstance(value, str) or value not in choices:
            self.error(location, f"deve ser um de: {', '.join(sorted(choices))}")
            return False
        return True

    def record_id(
        self, record: dict[str, Any], location: str, seen: set[str], pattern=None
    ) -> str | None:
        value = record.get("id")
        if not self.string(value, f"{location}.id"):
            return None
        if pattern and not pattern.fullmatch(value):
            self.error(f"{location}.id", "identificador fora do formato exigido")
        if value in seen:
            self.error(f"{location}.id", f"identificador duplicado: {value}")
        seen.add(value)
        return value

    def read_local(self, name: Any, location: str) -> str | None:
        if not self.string(name, location):
            return None
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or "\\" in name:
            self.error(location, "o caminho deve ser relativo e confinado à saída")
            return None
        try:
            resolved = (self.directory / relative).resolve()
            resolved.relative_to(self.directory)
            if not resolved.is_file():
                self.error(location, f"arquivo ausente: {name}")
                return None
            content = resolved.read_text(encoding="utf-8")
        except ValueError:
            self.error(location, "o caminho sai do diretório de saída ou é inválido")
            return None
        except (OSError, UnicodeError) as exc:
            self.error(location, f"não foi possível ler {name}: {exc}")
            return None
        if not content.strip():
            self.error(location, f"arquivo vazio: {name}")
            return None
        return content

    def load_json(self, content: str | None, location: str) -> dict[str, Any]:
        if content is None:
            return {}
        try:
            value = json.loads(content)
        except (json.JSONDecodeError, RecursionError) as exc:
            self.error(location, f"JSON inválido: {exc}")
            return {}
        return self.object(value, location)

    def validate_manifest(self) -> None:
        m = self.manifest
        if type(m.get("schema_version")) is not int or m["schema_version"] != 1:
            self.error("manifest.schema_version", "deve ser o inteiro 1")
        if m.get("escopo") != "estrategia-copy-design-direcao":
            self.error("manifest.escopo", "deve ser estrategia-copy-design-direcao")
        self.enum(m.get("status"), STATUSES, "manifest.status")
        for key in ("clinica", "servico"):
            self.string(m.get(key), f"manifest.{key}")
        artifacts = self.object(m.get("artefatos"), "manifest.artefatos")
        for key, expected in ARTIFACTS.items():
            path = artifacts.get(key)
            if isinstance(path, str) and path != expected:
                self.error(f"manifest.artefatos.{key}", f"deve apontar para {expected}")
            content = self.read_local(path, f"manifest.artefatos.{key}")
            if content is not None:
                self.documents[key] = content

    def validate_sections(self) -> tuple[dict[str, dict[str, Any]], dict[str, set[str]]]:
        records: dict[str, dict[str, dict[str, Any]]] = {}
        sequences: dict[str, list[tuple[str, str]]] = {}
        slots: dict[str, set[str]] = {}
        primary_cta_count = 0
        main = self.object(self.manifest.get("cta_principal"), "manifest.cta_principal")
        for field in ("texto", "destino"):
            self.string(main.get(field), f"manifest.cta_principal.{field}")
        for key, document in (("secoes_copy", "copy"), ("secoes_wireframe", "direcao")):
            items = self.array(self.manifest.get(key), f"manifest.{key}")
            if not items:
                self.error(f"manifest.{key}", "deve conter ao menos uma seção")
            if key == "secoes_copy":
                self.section_count = len(items)
            seen: set[str] = set()
            records[key] = {}
            sequences[key] = []
            for index, item in enumerate(items):
                loc = f"manifest.{key}[{index}]"
                record = self.object(item, loc)
                sid = self.record_id(record, loc, seen, SECTION_ID)
                headline = record.get("headline")
                headline_valid = self.string(headline, f"{loc}.headline")
                if sid is not None:
                    records[key][sid] = record
                    if headline_valid:
                        sequences[key].append((sid, headline))
                if key != "secoes_wireframe":
                    continue
                asset_refs = self.array(record.get("assets"), f"{loc}.assets")
                for pos, ref in enumerate(asset_refs):
                    if not self.string(ref, f"{loc}.assets[{pos}]"):
                        continue
                    if sid is not None:
                        slots.setdefault(ref, set()).add(sid)
                for pos, cta in enumerate(self.array(record.get("ctas"), f"{loc}.ctas")):
                    cloc = f"{loc}.ctas[{pos}]"
                    cta = self.object(cta, cloc)
                    for field in ("texto", "destino"):
                        self.string(cta.get(field), f"{cloc}.{field}")
                    valid_type = self.enum(cta.get("tipo"), {"primario", "secundario"}, f"{cloc}.tipo")
                    if valid_type and cta["tipo"] == "primario":
                        primary_cta_count += 1
                        for field in ("texto", "destino"):
                            if cta.get(field) != main.get(field):
                                self.error(f"{cloc}.{field}", "CTA primário diverge de cta_principal")
            text = self.documents.get(document)
            if text is not None:
                headings = SECTION_HEADING.findall(text)
                if headings != sequences[key]:
                    self.error(
                        ARTIFACTS[document],
                        "headings devem corresponder, na mesma sequência, aos IDs e headlines "
                        f"de {key}, no formato exato '## [sec-ID] Headline'",
                    )
        if sequences["secoes_copy"] != sequences["secoes_wireframe"]:
            self.error("manifest.secoes_wireframe", "IDs, headlines e sequência divergem de secoes_copy")
        if primary_cta_count == 0:
            self.error("manifest.secoes_wireframe.ctas", "deve haver ao menos um CTA primário no wireframe")
        return records["secoes_wireframe"], slots

    def validate_assets(
        self, sections: dict[str, dict[str, Any]], slots: dict[str, set[str]]
    ) -> dict[str, dict[str, Any]]:
        items = self.array(self.manifest.get("assets"), "manifest.assets")
        self.asset_count = len(items)
        seen: set[str] = set()
        filenames: dict[str, str] = {}
        assets: dict[str, dict[str, Any]] = {}
        pending_usage = False
        for index, item in enumerate(items):
            loc = f"manifest.assets[{index}]"
            asset = self.object(item, loc)
            aid = self.record_id(asset, loc, seen)
            if aid is not None:
                assets[aid] = asset
            self.enum(asset.get("tipo"), {f"{n:02}" for n in range(1, 9)}, f"{loc}.tipo")
            self.enum(asset.get("metodo"), {"existente", "foto-real", "ilustracao", "vetor", "inline"}, f"{loc}.metodo")
            self.enum(asset.get("status"), {"disponivel", "a-produzir", "a-verificar"}, f"{loc}.status")
            if "nome_arquivo" not in asset:
                self.error(f"{loc}.nome_arquivo", "campo obrigatório, inclusive quando null")
            filename = asset.get("nome_arquivo")
            if asset.get("metodo") == "inline":
                if filename is not None:
                    self.error(f"{loc}.nome_arquivo", "asset inline deve usar null")
                self.string(asset.get("renderizacao"), f"{loc}.renderizacao")
            elif self.string(filename, f"{loc}.nome_arquivo"):
                if not SAFE_BASENAME.fullmatch(filename) or ".." in filename:
                    self.error(f"{loc}.nome_arquivo", "use basename seguro com letras ASCII, números, ponto, hífen ou underscore")
                # Case-insensitive filesystems must not collapse two different assets.
                folded = filename.casefold()
                if folded in filenames:
                    self.error(f"{loc}.nome_arquivo", f"arquivo já pertence ao asset {filenames[folded]}; reutilize o mesmo ID")
                elif aid is not None:
                    filenames[folded] = aid
            if asset.get("status") == "disponivel":
                self.string(asset.get("fonte"), f"{loc}.fonte")
            if asset.get("status") == "a-verificar":
                pending_usage = True
            if "briefing_id" not in asset:
                self.error(f"{loc}.briefing_id", "campo obrigatório, inclusive quando null")
            bid = asset.get("briefing_id")
            if bid is not None:
                self.string(bid, f"{loc}.briefing_id")
            if asset.get("status") == "a-produzir" and not (isinstance(bid, str) and bid.strip()):
                self.error(f"{loc}.briefing_id", "asset a-produzir precisa de briefing")
            refs: set[str] = set()
            for pos, sid in enumerate(self.array(asset.get("secoes"), f"{loc}.secoes")):
                if not self.string(sid, f"{loc}.secoes[{pos}]"):
                    continue
                if sid in refs:
                    self.error(f"{loc}.secoes[{pos}]", f"seção duplicada: {sid}")
                refs.add(sid)
                if sid not in sections:
                    self.error(f"{loc}.secoes[{pos}]", f"seção inexistente: {sid}")
            if not refs:
                self.error(f"{loc}.secoes", "asset do inventário final deve aparecer em ao menos uma seção")
            if aid is not None and refs != slots.get(aid, set()):
                self.error(f"{loc}.secoes", f"não coincide com os slots do wireframe para {aid}")
        for aid in slots:
            if aid not in assets:
                self.error("manifest.secoes_wireframe.assets", f"slot aponta para asset inexistente: {aid}")
        if pending_usage and self.manifest.get("status") != "rascunho-com-pendencias":
            self.error("manifest.status", "assets a-verificar exigem rascunho-com-pendencias")
        return assets

    def validate_briefings(self, assets: dict[str, dict[str, Any]]) -> None:
        seen: set[str] = set()
        by_id: dict[str, dict[str, Any]] = {}
        expected_headings: dict[str, str] = {}
        for index, item in enumerate(self.array(self.manifest.get("briefings"), "manifest.briefings")):
            loc = f"manifest.briefings[{index}]"
            brief = self.object(item, loc)
            bid = self.record_id(brief, loc, seen, BRIEF_ID)
            if bid is not None:
                by_id[bid] = brief
            aid = brief.get("asset_id")
            if not self.string(aid, f"{loc}.asset_id"):
                continue
            if aid not in assets:
                self.error(f"{loc}.asset_id", f"asset inexistente: {aid}")
                continue
            asset = assets[aid]
            if bid is not None and asset.get("briefing_id") != bid:
                self.error(loc, f"briefing_id do asset {aid} não aponta de volta para {bid}")
            title = asset.get("nome_arquivo") if asset.get("metodo") != "inline" else aid
            if bid is not None and isinstance(title, str):
                expected_headings[bid] = title
        for aid, asset in assets.items():
            bid = asset.get("briefing_id")
            if bid is None:
                continue
            if not isinstance(bid, str) or bid not in by_id:
                self.error(f"asset {aid}.briefing_id", f"briefing inexistente: {bid}")
            elif by_id[bid].get("asset_id") != aid:
                self.error(f"asset {aid}.briefing_id", f"{bid} está associado a outro asset")
        text = self.documents.get("briefings")
        if text is None:
            return
        headings = BRIEF_HEADING.findall(text)
        actual: dict[str, str] = {}
        for bid, title in headings:
            if bid in actual:
                self.error(ARTIFACTS["briefings"], f"heading de briefing duplicado: {bid}")
            actual[bid] = title
        for bid, title in expected_headings.items():
            if actual.get(bid) != title:
                self.error(ARTIFACTS["briefings"], f"heading ausente ou divergente; esperado '## [{bid}] {title}'")
        for bid in actual:
            if bid not in by_id:
                self.error(ARTIFACTS["briefings"], f"heading sem briefing no manifest: {bid}")

    def validate_facts(self) -> None:
        briefing = self.load_json(self.documents.get("briefing"), ARTIFACTS["briefing"])
        seen: set[str] = set()
        facts: dict[str, dict[str, Any]] = {}
        for index, item in enumerate(self.array(briefing.get("fatos"), "briefing.fatos")):
            loc = f"briefing.fatos[{index}]"
            fact = self.object(item, loc)
            fid = self.record_id(fact, loc, seen)
            if fid is not None:
                facts[fid] = fact
            for field in ("campo", "fonte"):
                self.string(fact.get(field), f"{loc}.{field}")
            if "valor" not in fact:
                self.error(f"{loc}.valor", "campo obrigatório")
            self.enum(fact.get("status"), {"confirmado", "pendente"}, f"{loc}.status")
            self.boolean(fact.get("publicavel"), f"{loc}.publicavel")
        used_seen: set[str] = set()
        for pos, fid in enumerate(self.array(self.manifest.get("fatos_utilizados"), "manifest.fatos_utilizados")):
            loc = f"manifest.fatos_utilizados[{pos}]"
            if not self.string(fid, loc):
                continue
            if fid in used_seen:
                self.error(loc, f"fato duplicado: {fid}")
            used_seen.add(fid)
            if fid not in facts:
                self.error(loc, f"fato inexistente no briefing: {fid}")
            elif facts[fid].get("status") != "confirmado" or facts[fid].get("publicavel") is not True:
                self.error(loc, f"{fid} deve estar confirmado e publicavel=true")

    def validate_pending_and_analysis(self) -> None:
        seen: set[str] = set()
        for index, item in enumerate(self.array(self.manifest.get("pendencias"), "manifest.pendencias")):
            loc = f"manifest.pendencias[{index}]"
            pending = self.object(item, loc)
            self.record_id(pending, loc, seen)
            self.string(pending.get("descricao"), f"{loc}.descricao")
            self.boolean(pending.get("bloqueia_publicacao"), f"{loc}.bloqueia_publicacao")
            if self.manifest.get("status") == "planejamento-concluido" and pending.get("bloqueia_publicacao") is True:
                self.error(loc, "pendência que bloqueia publicação impede planejamento-concluido")
        analysis = self.documents.get("estrategia")
        if analysis is not None:
            numbers = re.findall(r"^#{2,6}\s+SEÇÃO\s+([1-6])(?:\s|[—:.-]|$)", analysis, re.MULTILINE | re.IGNORECASE)
            for number in map(str, range(1, 7)):
                if numbers.count(number) != 1:
                    self.error(ARTIFACTS["estrategia"], f"deve haver uma subseção SEÇÃO {number}")

    def run(self) -> dict[str, Any]:
        if not self.directory.is_dir():
            self.error("diretorio", f"diretório de saída inexistente: {self.directory}")
        else:
            self.manifest = self.load_json(self.read_local("manifest.json", "manifest.json"), "manifest.json")
            if self.manifest:
                self.validate_manifest()
                sections, slots = self.validate_sections()
                assets = self.validate_assets(sections, slots)
                self.validate_briefings(assets)
                self.validate_facts()
                self.validate_pending_and_analysis()
            elif not self.problems:
                self.error("manifest.json", "manifest vazio")
        return {
            "valido": not self.problems,
            "diretorio": str(self.directory),
            "status": self.manifest.get("status"),
            "quantidade_secoes": self.section_count,
            "quantidade_assets": self.asset_count,
            "problemas": self.problems,
            "limite": "Validação estrutural e técnica; não certifica eficácia, conformidade profissional ou autorização para publicar.",
        }


def main() -> int:
    parser = JsonArgumentParser(description=__doc__)
    parser.add_argument("diretorio", help="Diretório que contém manifest.json e os sete artefatos")
    args = parser.parse_args()
    try:
        result = Validator(Path(args.diretorio)).run()
    except (OSError, ValueError, TypeError, RecursionError) as exc:
        result = {
            "valido": False,
            "status": None,
            "quantidade_secoes": 0,
            "quantidade_assets": 0,
            "problemas": [f"Não foi possível validar a entrega: {exc}"],
            "limite": "Validação técnica não certifica eficácia ou norma profissional.",
        }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valido"] else 1


if __name__ == "__main__":
    sys.exit(main())

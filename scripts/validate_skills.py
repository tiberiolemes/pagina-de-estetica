#!/usr/bin/env python3
"""Validate the public aesthetics skill package using only the standard library."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "clinicas-estetica-lp-suite"
SKILL = PLUGIN / "skills" / "clinicas-estetica-lp-completa"
ERRORS = []

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}

def frontmatter(path):
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        ERRORS.append(f"{path.relative_to(ROOT)}: {exc}")
        return ""
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        ERRORS.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return ""
    return match.group(1)

fm = frontmatter(SKILL / "SKILL.md")
if not re.search(r"(?m)^name:\s*clinicas-estetica-lp-completa\s*$", fm):
    ERRORS.append("SKILL.md name must match its directory")
if not re.search(r"(?m)^description:\s*", fm):
    ERRORS.append("SKILL.md description missing")

for md in SKILL.rglob("*.md"):
    for target in re.findall(r"\]\(([^\s)]+)\)", md.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("#"):
            continue
        rel = target.split("#", 1)[0]
        if rel and not (md.parent / rel).resolve().exists():
            ERRORS.append(f"broken reference in {md.relative_to(ROOT)}: {target}")

plugin = load_json(PLUGIN / ".claude-plugin/plugin.json")
marketplace = load_json(ROOT / ".claude-plugin/marketplace.json")
if plugin.get("name") != "clinicas-estetica-lp-suite":
    ERRORS.append("plugin name mismatch")
if plugin.get("version") != "1.0.0":
    ERRORS.append("plugin version must be 1.0.0")
if "MIT" not in (ROOT / "LICENSE").read_text(encoding="utf-8"):
    ERRORS.append("MIT license missing")
if not any(item.get("name") == plugin.get("name") for item in marketplace.get("plugins", [])):
    ERRORS.append("marketplace plugin entry mismatch")
if not (PLUGIN / "agents/clinicas-estetica-lp-completa-agent.md").is_file():
    ERRORS.append("Claude coordinator agent missing")
if not (SKILL / "agents/openai.yaml").is_file():
    ERRORS.append("Codex UI metadata missing")

secret_patterns = [
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bsk-ant-api03-[A-Za-z0-9_-]{30,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    if any(pattern.search(text) for pattern in secret_patterns):
        ERRORS.append(f"possible credential pattern in {path.relative_to(ROOT)}")

if ERRORS:
    print(json.dumps({"valid": False, "errors": ERRORS}, indent=2))
    raise SystemExit(1)
print(json.dumps({"valid": True, "skill": "clinicas-estetica-lp-completa", "plugin": plugin["name"], "version": plugin["version"], "errors": []}, indent=2))

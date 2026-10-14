<div align="center">

    ╔══════════════════════════════════════════════════════════════════╗
    ║  CLÍNICAS DE ESTÉTICA · PÁGINA COMPLETA                         ║
    ║  estratégia → copy → sistema visual → direção de criação         ║
    ║  Codex · Claude Code · MIT                                       ║
    ╚══════════════════════════════════════════════════════════════════╝

**Agente autônomo para planejar landing pages de clínicas de estética.**

[![Version](https://img.shields.io/badge/version-1.0.0-2563eb?style=for-the-badge)](plugins/clinicas-estetica-lp-suite/.claude-plugin/plugin.json)
[![License](https://img.shields.io/badge/license-MIT-16a34a?style=for-the-badge)](LICENSE)
![Codex](https://img.shields.io/badge/Codex-supported-111827?style=for-the-badge)
![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-111827?style=for-the-badge)

[English version below](#english)

</div>

## O que faz

Em uma solicitação, a skill coordena análise estratégica, copy, design system, direção de criação, inventário de assets, briefings e revisão. Usa agentes especialistas quando a plataforma permite delegação e informa quando trabalha em sequência.

O resultado padrão é um planejamento pronto para produção. Construir ou publicar o site depende de pedido separado. A skill não substitui avaliação profissional, não certifica conformidade e não promete eficácia de procedimentos.

## Instalação — Codex

Clone o repositório e copie a skill para sua pasta pessoal:

    git clone https://github.com/tiberiolemes/pagina-de-estetica.git
    mkdir -p ~/.agents/skills
    cp -R pagina-de-estetica/plugins/clinicas-estetica-lp-suite/skills/clinicas-estetica-lp-completa ~/.agents/skills/

Se necessário, reinicie o Codex. Invoque:

    $clinicas-estetica-lp-completa

Para usar apenas em um projeto, copie a pasta para .agents/skills/ na raiz do projeto.

## Instalação — Claude Code

Adicione o marketplace público e instale o plugin no escopo do usuário:

    /plugin marketplace add tiberiolemes/pagina-de-estetica
    /plugin install clinicas-estetica-lp-suite@tiberio-clinicas-estetica

A invocação será /clinicas-estetica-lp-suite:clinicas-estetica-lp-completa. Para testar uma cópia local por uma sessão, clone o repositório e inicie Claude Code com --plugin-dir ./plugins/clinicas-estetica-lp-suite.

## Uso

Forneça os materiais da clínica, delimite o serviço e informe o caminho de conversão:

    Use $clinicas-estetica-lp-completa com estes materiais. Conduza as quatro etapas até entregar o pacote final.

A skill diferencia cliente e paciente conforme o serviço, não presume incômodo corporal, não inventa resultados e registra lacunas de evidência, autorização, profissão ou oferta como pendências. Não envie prontuários, fotos sem autorização ou dados identificáveis.

## Retomada

A pasta de entrega inclui estado.json. Para continuar um pacote interrompido, reabra o projeto com os materiais e peça:

    Retome $clinicas-estetica-lp-completa a partir de estado.json. Confira as versões dos insumos, preserve minhas edições e continue da próxima etapa incompleta.

## Estrutura

    plugins/clinicas-estetica-lp-suite/
    ├── .claude-plugin/plugin.json
    ├── agents/clinicas-estetica-lp-completa-agent.md
    └── skills/clinicas-estetica-lp-completa/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── scripts/validate_delivery.py

## Licença e contribuição

Pacote público sob licença MIT: consulte LICENSE. Contribuições são bem-vindas conforme CONTRIBUTING.md. Regras de publicidade dependem do serviço e da profissão. Confirme exigências vigentes em fontes oficiais primárias com os responsáveis profissionais antes de publicar.

---

<a id="english"></a>

## English

**An autonomous agent for planning landing pages for aesthetics clinics.** In one request, the skill coordinates strategy, copy, design system, creative direction, asset inventory, production briefs, and final review. It uses specialist agents when the host supports delegation and reports when it must work sequentially.

The default output is a production-ready plan. Website implementation or publication requires a separate request. This skill does not replace professional assessment, certify compliance, or promise procedural efficacy.

### Install — Codex

    git clone https://github.com/tiberiolemes/pagina-de-estetica.git
    mkdir -p ~/.agents/skills
    cp -R pagina-de-estetica/plugins/clinicas-estetica-lp-suite/skills/clinicas-estetica-lp-completa ~/.agents/skills/

Restart Codex if needed, then invoke $clinicas-estetica-lp-completa. For project-only use, copy the folder to .agents/skills/ at your project root.

### Install — Claude Code

    /plugin marketplace add tiberiolemes/pagina-de-estetica
    /plugin install clinicas-estetica-lp-suite@tiberio-clinicas-estetica

Invoke /clinicas-estetica-lp-suite:clinicas-estetica-lp-completa. For one local session, clone the repository and start Claude Code with --plugin-dir ./plugins/clinicas-estetica-lp-suite.

### Use

Provide the clinic materials, the service in scope, and the conversion path. The skill distinguishes clients and patients according to the service, does not assume body dissatisfaction, does not invent outcomes, and records missing evidence, permissions, professional categories, or offer terms as pending. Do not provide identifiable health records, unauthorized photos, or personal data.

### Resume

Delivery folders include estado.json. To continue an interrupted package, reopen the project with its source materials and ask:

    Resume $clinicas-estetica-lp-completa from estado.json. Check input versions, preserve my edits, and continue from the next incomplete stage.

### License and contribution

This public package is licensed under MIT; see LICENSE. Contributions are welcome under CONTRIBUTING.md. Advertising rules depend on the service and profession. Verify current requirements with primary official sources and the responsible professionals before publication.

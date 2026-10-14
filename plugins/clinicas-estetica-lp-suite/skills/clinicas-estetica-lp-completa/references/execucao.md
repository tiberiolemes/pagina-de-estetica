# Protocolo de execução e entrega

Este protocolo mantém as quatro etapas coerentes. O coordenador distribui os módulos e só carrega o detalhe necessário para revisar cada saída.

## Pasta e artefatos

Use uma pasta de saída do projeto, separada dos insumos e desta skill:

```text
00-briefing.json
01-analise-estrategica.md
02-copy.md
03-design-system.md
04-wireframe.md
05-briefings-imagens.md
06-revisao.md
manifest.json
estado.json
```

A ausência de imagens produzidas é compatível com o escopo de planejamento. O inventário precisa distinguir arquivos disponíveis, produção futura e uso ainda não verificado.

## Briefing compartilhado

`00-briefing.json` contém clínica, serviço, público, participantes da decisão, caminho de conversão, CTA e destino conhecidos, profissionais e categorias, condições, identidade, referência visual, arquivos disponíveis e fontes.

Separe:

- `fatos`: itens com ID estável, campo, valor, fonte, status e condição de uso.
- `hipoteses`: interpretações estratégicas, com fundamentação e limites.
- `decisoes`: opções de estrutura ou estilo adotadas pelo coordenador e sua origem.
- `fontes_normativas`: categoria pertinente, URL oficial, data de consulta e o que a fonte sustenta, quando necessário.
- `pendencias`: fatos, materiais ou decisões ainda desconhecidos.

Formato de um fato:

```json
{
  "id": "F001",
  "campo": "servico",
  "valor": "Serviço informado pelo usuário",
  "fonte": "material.md#secao-identificavel",
  "status": "confirmado",
  "publicavel": true
}
```

`confirmado` significa sustentado por uma fonte identificada para este trabalho; não transforma uma declaração do cliente em comprovação científica. `publicavel` significa que há base para usar aquele fato na mensagem, respeitando contexto e finalidade conhecidos; nunca infira autorização de imagem ou depoimento só por receber um arquivo.

Use `pendente` para um fato não confirmado. Não promova hipótese a fato. Recomendações de cores e layout não são resultados clínicos nem evidências sobre o atendimento.

## Contrato entre especialistas

Na mensagem de delegação, indique:

```text
Papel e objetivo da etapa
Módulo que deve ler
Briefing e materiais compartilháveis
Saídas anteriores aceitas e sua versão
Arquivos que pode editar — somente os da etapa atribuída
Fatos e condições que deve preservar
Pendências que não pode preencher por invenção
Critérios de entrega e resumo esperado para o coordenador
```

O especialista de sistema visual pode trabalhar em duas passagens, preliminar e consolidada. O especialista de direção escreve o wireframe e propõe o inventário final; o coordenador concilia isso com os briefings e o sistema. O revisor independente não altera diretamente os documentos.

## Formato das saídas

### Análise

`01-analise-estrategica.md` mantém as seis seções do módulo, com subtítulos `### SEÇÃO 1 — ...` a `### SEÇÃO 6 — ...`. Cite a origem das conclusões e identifique lacunas.

### Copy e wireframe

Use IDs estáveis de seção e preserve a headline exata, incluindo suas marcações. Nos dois arquivos:

```text
## [sec-hero] Headline exata desta seção
```

As demais informações da seção vêm abaixo. O documento de copy contém o texto e as notas editoriais separadas; o wireframe contém a composição. O ID não faz parte do texto público nem determina a tag HTML final.

Os dois documentos mantêm a mesma sequência de IDs e headlines. Se uma ordem nova for aceita durante a revisão interna, sincronize copy, wireframe e manifest.

CTA tem texto, destino e tipo (`primario` ou `secundario`). Todos os CTAs primários devem executar a ação principal definida; ações diferentes precisam de hierarquia explícita. Um destino desconhecido fica pendente, sem número, URL ou integração inventados.

Inclua pelo menos um CTA primário no wireframe. O inventário final contém apenas assets associados a seções; materiais dispensados podem ser registrados na revisão, sem inflar a contagem de produção.

### Sistema visual

`03-design-system.md` registra o modo `extraido` ou `proposto`, as origens das decisões, especificações desktop/mobile, cores, tipografia, componentes, CSS vars, mapa estrutural, backgrounds e limites de imagens. Use CSS válido quando apresentar código implementável; se algo não estiver resolvido, descreva a pendência em texto.

Sem referência, use `proposto`. Isso é autorizado pela execução autônoma desta skill; não atribua medidas, fontes ou cores inventadas a uma referência que não existe.

### Briefings

`05-briefings-imagens.md` possui um bloco por asset a produzir:

```text
## [brief-hero-profissional] foto-profissional.webp
```

Para um componente inline, o título usa exatamente o ID do asset. Briefings descrevem função, origem, método, composição, proporção, recorte mobile e limites de tratamento. Foto real recebe orientação de fotografia; ilustração pode receber prompt; vetor recebe especificação. Não crie prompt para fabricar equipe ou prova real.

Materiais existentes podem ter somente instruções de uso e tratamento. Toda produção planejada precisa de um briefing. Não declare existência de foto ou autorização que não foi fornecida.

### Revisão

`06-revisao.md` registra verificações realizadas, achados corrigidos, limitações, decisões finais e pendências. Distingua revisão textual e estrutural de teste visual da página implementada.

## Manifest

`manifest.json` é mantido pelo coordenador e representa os documentos efetivamente entregues. Estrutura:

```json
{
  "schema_version": 1,
  "escopo": "estrategia-copy-design-direcao",
  "status": "planejamento-concluido",
  "clinica": "Nome fornecido",
  "servico": "Serviço da campanha",
  "artefatos": {
    "briefing": "00-briefing.json",
    "estrategia": "01-analise-estrategica.md",
    "copy": "02-copy.md",
    "design_system": "03-design-system.md",
    "direcao": "04-wireframe.md",
    "briefings": "05-briefings-imagens.md",
    "revisao": "06-revisao.md"
  },
  "cta_principal": {
    "texto": "Texto confirmado da ação",
    "destino": "Destino confirmado"
  },
  "secoes_copy": [
    {"id": "sec-hero", "headline": "Headline exata"}
  ],
  "secoes_wireframe": [
    {
      "id": "sec-hero",
      "headline": "Headline exata",
      "assets": ["asset-hero-profissional"],
      "ctas": [
        {"texto": "Texto confirmado da ação", "destino": "Destino confirmado", "tipo": "primario"}
      ]
    }
  ],
  "assets": [
    {
      "id": "asset-hero-profissional",
      "nome_arquivo": "foto-profissional.webp",
      "tipo": "01",
      "metodo": "foto-real",
      "status": "a-produzir",
      "secoes": ["sec-hero"],
      "briefing_id": "brief-hero-profissional"
    }
  ],
  "briefings": [
    {"id": "brief-hero-profissional", "asset_id": "asset-hero-profissional"}
  ],
  "fatos_utilizados": ["F001"],
  "pendencias": []
}
```

O exemplo é um contrato de formato; substitua os valores pelos materiais reais. Não o copie como entrega de uma clínica desconhecida.

Métodos de assets: `existente`, `foto-real`, `ilustracao`, `vetor`, `inline`. Status: `disponivel`, `a-produzir`, `a-verificar`. Tipo: string de `01` a `08`, conforme os módulos 02 e 03.

- Asset `disponivel` inclui `fonte` explícita. A fonte pode estar nos insumos, fora da pasta de saída; não invente um arquivo existente.
- Asset `a-produzir` exige `briefing_id` e bloco correspondente.
- Asset `inline` usa `nome_arquivo: null` e `renderizacao` descrevendo SVG, CSS ou HTML; se ainda for preciso produzi-lo, também precisa de briefing.
- Nome de arquivo é basename seguro, sem caminho externo ou dados identificáveis de pacientes.
- `secoes` de cada asset coincide com seus slots no wireframe. Reutilização usa o mesmo ID, sem multiplicar falsamente os arquivos.
- `fatos_utilizados` contém somente fatos confirmados e publicáveis do briefing. Ele registra a sustentação das alegações públicas, não transforma recomendações visuais em fatos clínicos.
- Pendência tem `id`, `descricao` e `bloqueia_publicacao` booleano. Preços, registros ou autorizações desconhecidos não devem aparecer como fatos confirmados em copy pública.

## Condição de conclusão

- **`planejamento-concluido`:** as quatro etapas e a revisão foram entregues e conciliadas; não há pendência marcada como bloqueadora de publicação no conteúdo. Pode haver produção de assets ainda planejada, claramente descrita. Isso não significa que o site exista ou esteja publicado.
- **`rascunho-com-pendencias`:** o pacote foi produzido até onde os materiais permitem, mas faltam fatos ou verificações necessários ao uso público. Assets com uso `a-verificar` mantidos no plano exigem essa condição; prefira omiti-los ou substituir a composição quando possível.
- **`aguardando-informacao`:** falta uma resposta indispensável para escolher a oferta ou o próximo passo. Faça a pergunta concreta e mantenha o trabalho independente em andamento; não marque o pacote como concluído.

Não execute o validador de entrega completa como se todos os arquivos existissem antes de uma pergunta indispensável ser respondida. Na retomada, finalize as saídas e valide o pacote consolidado.

## Correções e retomada

Falha estrutural retorna ao arquivo que a originou. Mudança de copy ou CTA atualiza wireframe, briefings afetados e manifest; mudança visual atualiza sistema e direção conforme a dependência. O coordenador controla essas edições para não haver escritores simultâneos no mesmo arquivo.

Registre em `estado.json` a etapa, a versão dos insumos, saídas aceitas, decisões e pendências após cada avanço. Na retomada, reutilize o que continua válido, preserve alterações do usuário e refaça apenas dependências afetadas.

A revisão final combina leitura crítica com `scripts/validate_delivery.py`. Um resultado técnico válido não certifica alegações de resultado, enquadramento profissional ou permissão publicitária. Relate o alcance real da verificação.

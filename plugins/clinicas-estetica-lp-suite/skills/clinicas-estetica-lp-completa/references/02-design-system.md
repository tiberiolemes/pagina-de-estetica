# Design System Extrator — Landing de Clínicas de Estética

Adaptação da metodologia original da coleção para páginas de clínicas de estética.

Você extrai, organiza e traduz uma referência visual em especificação técnica. A estrutura vem da referência; a identidade e os fatos vêm dos insumos da clínica. Qualquer adaptação deve ficar identificada como recomendação, sem parecer uma característica observada.

**Contexto do segmento:** a composição ajuda a compreender a oferta, conhecer os profissionais e entender o papel da avaliação. Imagens de equipe, ambiente e processo podem sustentar a escolha. Uma atmosfera aspiracional não comprova resultado estético e não deve fabricar insatisfação corporal.

**Imagem tem função:** diferencie prova, informação e atmosfera. Não use uma foto decorativa como resultado de um serviço.

**Background organiza a leitura:** documente o ritmo existente, inclusive quando a referência usa fundo contínuo. Não acrescente alternância, grain ou brilho apenas para parecer uma página de estética.

**Tratamento visual tem limites:** direção de luz e cor não autoriza modificar corpo, pele ou resultado em uma prova real.

## INSUMOS — LEIA O CONTEXTO ANTES DE PERGUNTAR

- **Referência visual:** URL, prints ou PDF da página modelo. É necessária para afirmar que houve extração. Se faltar, peça a referência; não apresente um sistema inventado como extraído.
- **Identidade da clínica:** logo, cores, fontes, manual de marca e escolhas aprovadas. A identidade fornecida prevalece sobre sugestões padrão desta skill.
- **Copy e análise estratégica:** use os resultados das [00](00-analise.md) e [01](01-copy.md), quando disponíveis. Preserve oferta, desejo expresso, público, profissionais, CTA, condições e limites confirmados.
- **Materiais reais:** equipe, clínica, estrutura, atendimento, equipamentos, relatos e imagens de resultados, quando existirem. Registre origem, contexto e condições de uso conhecidas.
- **Moodboard ou atmosfera desejada:** imagens ou palavras fornecidas pelo usuário. Calibra luz, temperatura, textura e linguagem visual; não determina eficácia ou indicação de um procedimento.
- **Contexto de implementação:** plataforma, assets existentes, restrições técnicas e dispositivos prioritários, quando conhecidos.

Não pergunte novamente o que já estiver nos materiais. Sem copy final, entregue o mapa estrutural da referência e sinalize que sua associação às seções da clínica ainda é provisória.

Uma referência de outro segmento pode fornecer estrutura. Não transporte seus personagens, promessas, provas ou condições comerciais para a clínica. Se um serviço tiver motivação de cuidado em saúde, use a versão correspondente do segmento.

## ORIGEM E CONFIANÇA DAS ESPECIFICAÇÕES

Identifique cada decisão relevante como:

- **OBSERVADO:** visível na referência ou confirmado por seus arquivos e estilos.
- **ESTIMADO:** medida aproximada obtida de print ou conteúdo sem acesso aos estilos; informe como estimou.
- **FORNECIDO:** identidade, asset ou escolha explicitamente enviada ou aprovada pelo usuário.
- **RECOMENDADO:** ajuste proposto para copy, responsividade, acessibilidade ou contexto da oferta estética.
- **NÃO IDENTIFICADO:** informação que a evidência não permite determinar.

Sem evidência, não invente nome de fonte, peso, HEX exato ou estado de hover. Um print desktop também não comprova o layout mobile. Identifique adaptações propostas e não trate uma tendência visual como propriedade da referência.

## FASE 1 — LEITURA E EXTRAÇÃO

### Estrutura macro

Registre grid, container, alinhamentos, proporção de texto e imagem, espaços verticais, número de seções, posição dos CTAs e sequência dos fundos. Use px para medidas observadas ou estimadas e identifique a origem. Na implementação, unidades fluidas podem ser usadas com correspondência documentada.

Se houver copy aprovada, mapeie suas funções na estrutura. Não acrescente um procedimento, pacote, desconto, resultado ou mecanismo exclusivo porque a referência possui uma seção para isso.

### Tipografia

Extraia ou registre: família quando identificável, estilo, pesos, tamanhos, altura de linha, tracking, escala H1 → corpo → legenda, caixa alta, itálico e grifos. Separe desktop e mobile.

Quando houver necessidade autorizada de escolher uma fonte, mantenha as opções da metodologia original: Sora, DM Sans, Outfit; Newsreader, Playfair Display, Crimson Text; IBM Plex Mono para usos pontuais adequados. Justifique a escolha pelos insumos e marque como recomendação.

Evite adotar Inter, Poppins, Roboto, Arial, Open Sans ou system-ui como escolha principal automática. Se a marca ou o usuário tiver aprovado uma delas, preserve essa escolha explícita. Fallback técnico não é identidade tipográfica.

Registre fonte, origem, pesos disponíveis, licença conhecida e carregamento; não fabrique URL de download. Para hero em duas colunas, especifique ajuste próprio de H1 compatível com a headline real. `clamp(24px, 2.8vw, 44px)` é um exemplo da metodologia, não uma medida obrigatória.

Legendas de provas, identificação profissional e condições da oferta devem permanecer legíveis. Sofisticação visual não exige texto fino, minúsculo ou de baixo contraste.

### Paleta e legibilidade

Documente cores centrais em HEX: fundo, texto, primária, CTA e superfície. Registre separadamente bordas, texto secundário e estados semânticos necessários. Não deduza paleta por gênero, procedimento ou segmento.

Mostre os pares texto/fundo e o contraste calculado quando houver valores confiáveis. Para texto comum, considere pelo menos 4,5:1; para texto grande, 3:1, conforme os critérios e exceções do [W3C — contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Não declare contraste medido por impressão visual.

Se a referência tiver baixa legibilidade, registre o problema e proponha ajuste separado. Verifique especialmente legenda, texto sobre foto, CTA, condições de preço e identificação profissional.

### Componentes

Especifique botões primário e secundário, cards de serviços, apresentação dos profissionais, FAQ, condições da oferta e formulário quando existirem: dimensões, padding, radius, borda, cor, sombra e estados conhecidos.

Descreva focus visível, labels, mensagens de erro e feedback de envio. Controles e estados que dependam de indicação visual devem considerar o [W3C — contraste não textual](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).

Como recomendação de conforto, prefira área de toque de pelo menos 44px nos CTAs principais; identifique como escolha de projeto, não requisito universal extraído. Preserve a finalidade e os campos mínimos do formulário definidos na copy.

Não transforme um slider de imagem, selo de “protocolo” ou card de equipamento em comprovação de resultado. Componentes de prova precisam carregar o contexto pertinente e cumprir as condições de uso.

**Ícones:** mantenha uma família coerente. Na ausência de escolha fornecida, as opções da metodologia são Iconify Solar Outline, Feather ou Phosphor. Evite Lucide como substituição automática; uma família explicitamente aprovada pelo usuário prevalece. Ícone não comprova habilitação, segurança ou aprovação de órgão público.

### Animações

Documente os comportamentos observados: entradas, hover, stagger ou outros efeitos. Sem evidência interativa, marque como desconhecido ou recomendação.

Nos ajustes, priorize leitura e acesso ao CTA e defina movimento reduzido. Não use animação para simular transformação corporal, amplificar defeito, modificar resultado ou esconder condições e contexto. Não acrescente contagem regressiva ou escassez visual sem conteúdo confirmado.

### Decisão de luz

Registre a atmosfera fornecida e a luz observada. Como direções possíveis, não como fatos universais:

| Atmosfera fornecida | Direção a avaliar |
|---|---|
| Proximidade e bem-estar | Luz natural ou difusa, preservando a aparência real |
| Precisão e clareza | Luz neutra e enquadramento informativo |
| Reserva e sofisticação | Luz controlada e contraste moderado, conforme a identidade |

Fotos reais podem manter condições originais diferentes da direção ilustrativa. Registre exceções em vez de retocar tudo para parecer uniforme.

Em provas de resultados, preserve os arquivos e o contexto. Não altere iluminação, textura, tom de pele, proporção corporal, cabelo ou expressão para favorecer uma comparação. Uma estética global de imagens decorativas não se aplica automaticamente a provas.

### Inventário de imagens — tipos 01–08

Conte todos os assets relevantes à composição, inclusive logos, ícones e fundos. Separe arquivos únicos de ocorrências; um sprite pode ter um arquivo e vários ícones utilizados.

| Tipo | Uso em clínicas de estética |
|---|---|
| 01 | Profissionais e equipe reais, com identidade e uso adequados |
| 02 | Clínica e estrutura reais |
| 03 | Experiência de atendimento ou serviço, sem simular caso real |
| 04 | Relato ou avaliação de experiência real com uso adequado |
| 05 | Informação ou resultado contextualizado, somente se pertinente e utilizável |
| 06 | Jornada de contato, avaliação, decisão e acompanhamento conforme a oferta |
| 07 | Atmosfera ou ilustração claramente identificada |
| 08 | Ícone, diagrama ou informação de acesso sem falso endosso |

Para cada asset, registre:

```text
ID / nome do arquivo / seção / tipo 01–08 / função
origem: real fornecido | a fotografar | ilustração | vetor | banco autorizado
status: disponível | pendente | uso público a verificar | dispensado
posição / proporção / enquadramento / resolução conhecida
tratamento permitido / contexto ou legenda necessários
categoria profissional pertinente quando for prova de atendimento ou resultado
mobile: mantém | reposiciona | reduz | substitui | decorativo removível
alt: texto útil | vazio quando puramente decorativo
```

Uma imagem de atmosfera não pode ser descrita como pessoa atendida pela clínica. Equipamento fotografado comprova sua presença no material, não superioridade de resultados. Não esconda no celular legenda ou contexto necessário para entender uma prova.

### Uso de imagens de resultados

Se a composição utilizar resultado ou antes e depois, identifique serviço, profissional, origem, contexto, autorização conhecida e regras aplicáveis. Não faça do tipo 05 uma exigência para toda página.

Para publicidade médica, verifique as condições do [Manual do CFM — Capítulo XII](https://publicidademedica.cfm.org.br/manual/aplicacao-pratica/capitulo-12). Um par de fotos isolado com “resultados variam” não deve ser presumido suficiente. Para biomédicos, consulte o [Código de Ética do CFBM](https://cfbm.gov.br/legislacao/codigo-de-etica/); para outras categorias, suas fontes oficiais.

Não aplique as regras de uma categoria automaticamente a outra. Material não verificado fica marcado como pendente ou é substituído por uma composição apoiada em fatos utilizáveis; não gere resultados fictícios para preencher o espaço.

### Mapa de backgrounds

Para cada seção, registre cor, efeito observado, grafismo, imagem de fundo, overlay e movimento. Informe opacidade ou intensidade quando conhecida e marque estimativas.

Registre o ritmo existente. Gradiente, textura, grain ou luz decorativa entram quando observados ou propostos com função clara. Não use o efeito de fundo para fazer uma pele, corpo ou resultado real parecer diferente.

## FASE 2 — SÍNTESE E VALIDAÇÃO DA DIREÇÃO

Apresente uma síntese concreta:

```text
DESIGN SYSTEM — CLÍNICA DE ESTÉTICA [NOME]
REFERÊNCIA / OFERTA / COPY UTILIZADA:
LAYOUT: grid / container / espaçamento / seções
TIPOGRAFIA: famílias / pesos / escala / origem e grau de confiança
PALETA: HEX e papéis / pares de contraste / origem
LUZ E IMAGENS: atmosfera / materiais reais / ilustrações / exceções para provas
COMPONENTES: CTA / serviços / FAQ / oferta / formulário / foco
ÍCONES E MOVIMENTO: família / comportamentos observados e propostos
INVENTÁRIO: arquivos únicos / ocorrências / distribuição 01–08
PROVAS: materiais utilizáveis / contexto / uso a verificar por categoria
BACKGROUNDS: sequência / efeitos / ajustes de legibilidade
CONFLITOS: referência × identidade × copy × integridade das provas
PENDÊNCIAS: somente o que afeta uma decisão relevante
```

Use um único checkpoint quando houver uma escolha de direção ainda dependente do usuário. Pergunte sobre o conflito concreto, sem pedir confirmação genérica de escolhas já aprovadas. Se a direção estiver autorizada ou o usuário tiver pedido execução completa com autonomia, siga para a entrega técnica; não acrescente uma parada automática.

Enquanto uma decisão necessária estiver pendente, avance nas especificações independentes. Não apresente uma autorização ou permissão desconhecida como fato confirmado.

## FASE 3 — ENTREGA COMPLETA

### A — DESIGN SYSTEM TÉCNICO

Entregue valores concretos e sua origem; mantenha desconhecidos identificados. O esquema abaixo orienta o conteúdo, não é CSS pronto para execução:

```text
# DESIGN SYSTEM — [CLÍNICA / SERVIÇO]

CORES: primária / CTA / BG / superfície / texto / muted / borda / estados
       HEX / origem / contraste dos pares utilizados
TIPOGRAFIA: família / arquivo ou URL verificada / licença conhecida / pesos
            mobile e desktop: H1 / H2 / H3 / corpo / legenda / CTA
            line-height / tracking / grifos / ajuste de H1 para hero split
ESPAÇOS: container / padding horizontal / section py / gaps / breakpoints
BORDAS: width / cor / radius de botão, card, input, imagem e badge
SOMBRAS: valores CSS / contexto de uso
BOTÕES: dimensões / padding / cores / hover / focus / ativo / desabilitado
CARDS: grid / padding / border / shadow / responsive
OFERTA: hierarquia de valores e condições confirmadas / CTA
FORMULÁRIO: labels / campos confirmados / foco / erro / envio / sucesso
FAQ: estado aberto / foco / texto legível
ÍCONES: família / tamanho / peso / cor / labels necessários
IMAGENS: proporções / recortes / tratamento por categoria / alt / resolução
PROVAS: contexto visível / integridade / condições de uso conhecidas
MOVIMENTO: gatilho / duração / easing / redução de movimento
```

Forneça um bloco real de CSS vars com nomes consistentes e valores válidos quando os insumos permitirem, incluindo cores, fontes, espaços, raios e sombras. Não entregue `#___` como se fosse cor implementável.

Mantenha um contrato de tokens para a etapa seguinte:

```text
--color-primary / --color-accent / --color-bg / --color-surface
--color-text / --color-muted / --color-border / --color-focus
--font-heading / --font-body
--container-max / --padding-x-m / --padding-x-d
--section-py-m / --section-py-d / --card-gap
--radius-btn / --radius-card / --radius-input
--shadow-sm / --shadow-md / --shadow-lg
```

Esse bloco lista nomes, não valores. Preencha o CSS final com a especificação verificada ou recomendada e identifique a origem das escolhas no documento.

Para overlays decorativos, especifique gradientes e cores válidas; em cores dinâmicas, defina os canais RGB ou RGBA necessários. Não use a expressão inválida `rgba(bg, ...)`. Não aplique opacidade global à imagem e ao texto juntos.

Filter e overlay não são obrigatórios para toda imagem. Em provas reais, documente os limites: não modificar resultado, esconder contexto, apagar uma condição relevante ou favorecer a comparação.

### B — WIREFRAME DOBRA A DOBRA

“Dobra” identifica a seção narrativa, não uma promessa de caber em uma altura fixa de tela. Preserve a copy aprovada e o caminho de conversão.

```text
SEÇÃO [N] — [NOME]
ORIGEM: seção observada / adaptação para copy / proposta ainda pendente
FUNÇÃO: dúvida ou expectativa que esclarece / fato que demonstra
COMPOSIÇÃO: entrada visual / percurso de leitura / chegada ao CTA
DESKTOP: colunas e proporções / container / padding / alinhamentos
MOBILE: ordem / empilhamento / tamanhos / recorte / contexto preservado
BG: HEX / efeito / overlay / grafismo / origem
ASSETS: nome exato / tipo / função / proporção / tratamento / alt
PROVA: material / contexto / categoria profissional / uso verificado ou pendente
IDENTIFICAÇÃO: dados profissionais necessários e localização prevista
OFERTA: condições confirmadas que precisam permanecer visíveis
CTA: texto aprovado / primário ou secundário / destino e próximo passo
ÍCONES E MOVIMENTO: família / interação / comportamento reduzido
DEPENDÊNCIAS: asset ausente / dado desconhecido / peso ou script a avaliar
```

Se houver comparação de resultados utilizável, o layout deve preservar contexto, imagens e legendas no desktop e no celular. Não esconda informação em um slider ou recorte que favoreça a leitura de resultado garantido.

Se a referência tiver uma barra fixa, documente como funciona. Só recomende uma para o projeto quando ajudar na ação e não cobrir conteúdo ou foco. Não acrescente barra de escassez, selo de promoção ou contagem regressiva por padrão.

O wireframe desta etapa especifica a adaptação estrutural. A etapa 03 de direção de criação poderá detalhar a composição usando este sistema e a copy, sem reextrair a identidade.

### C — BRIEFINGS DE IMAGEM

Para cada asset a criar ou obter, escolha a produção adequada:

- **Foto real:** profissionais, equipe, clínica ou experiência de atendimento documentada. Entregue briefing de fotografia e condições de uso a verificar.
- **Asset existente:** registre fonte, resolução, licença ou autorização conhecida e limites de tratamento. Material de resultado mantém sua integridade e contexto.
- **Ilustração:** pode receber prompt de geração quando sua função for explicativa ou de atmosfera, com identificação clara. Não pode simular paciente, procedimento ocorrido ou resultado real.
- **Vetor, ícone ou diagrama:** especifique conteúdo, labels e sistema gráfico. Não force geração raster quando a solução adequada for SVG ou código.

```text
BRIEFING — [nome-exato.ext]
Seção / tipo / função / origem / método de produção
Sujeito ou conteúdo confirmado / composição / proporção / enquadramento
Luz / cor / fundo / espaço para texto / recorte mobile
Tratamento permitido / elementos a evitar / alt e legenda
Dependências: fato, contexto, material ou autorização a verificar
Foto real: o que fotografar / como / identificação necessária
Resultado existente: preservação / contexto / limites de recorte e tratamento
Ilustração: prompt, preferencialmente em inglês se a ferramenta exigir
Vetor: estrutura, labels e família gráfica
```

Não crie prompt para antes e depois fictício, corpo “corrigido”, profissional inexistente ou cliente supostamente atendido. Não peça remoção artificial de marcas ou mudanças de proporção para tornar uma prova mais persuasiva.

Não envie imagens identificáveis ou informações clínicas a um gerador externo apenas porque estão nos insumos. Uma alternativa ilustrativa deve continuar identificada como ilustração. Briefing não autoriza publicação nem uso público de asset pendente.

### D — RESUMO DE PRODUÇÃO E HANDOFF

Entregue total de seções, assets únicos e ocorrências; seções com CTA; comportamento mobile; lista de arquivos exatos; fontes e origem; mapa de backgrounds; decisões observadas, fornecidas e propostas; materiais de prova e condições de uso conhecidas; pendências que afetam implementação.

Use nomes descritivos e estáveis, como `foto-profissional-nome.webp`, `foto-clinica-ambiente.webp`, `diagrama-jornada-avaliacao.svg` e `ilustracao-atmosfera-estetica.webp`. Os exemplos não pressupõem a existência desses materiais. Se um nome precisar mudar, atualize todas as referências.

Passe copy, design system e mapa estrutural à etapa 03 de direção de criação. Fotografia ou geração de ilustrações seguirá os briefings no escopo solicitado. Não declare revisão visual mobile concluída sem ter inspecionado a implementação.

## REGRAS DO SEGMENTO

1. Preserve a identidade e as escolhas explicitamente aprovadas pelo usuário.
2. Distingua observação, estimativa, recomendação e informação desconhecida.
3. Não invente medidas exatas, fontes, cores ou interações que a referência não permite verificar.
4. Tipografia, paleta e ícones sugeridos precisam de origem clara; não substitua escolhas fornecidas automaticamente.
5. Legibilidade, foco, identificação e condições da oferta devem permanecer claros no celular.
6. Conte todos os assets e ocorrências; cada asset recebe um tipo 01–08 e uma função.
7. Diferencie prova de experiência, prova de resultado e imagem de atmosfera.
8. Não fabrique pacientes, clientes, profissionais, relatos, credenciais ou resultados por fotografia encenada, edição ou IA.
9. Não use atmosfera visual para explorar vergonha corporal ou sugerir transformação social garantida.
10. Preserve fotos reais e o contexto das provas. A direção de luz global não se sobrepõe à integridade de um resultado.
11. Identifique serviço e categoria profissional antes de recomendar uso de imagens, relatos, selos ou dados de registro. Estética médica segue suas regras; outras categorias exigem suas fontes oficiais.
12. Registre fonte e data quando uma recomendação depender de norma. Não presuma autorização, permissão ou ausência de restrições.
13. Não use logos de conselhos, fabricantes ou órgãos públicos como endosso da clínica.
14. Não oculte contexto de resultados, identificação ou condições em legendas ilegíveis, overlays ou recortes mobile.
15. Não acrescente promoções, sessões, manutenção ou escassez ausentes da copy aprovada.
16. Cada asset a produzir tem briefing adequado ao método; nem todo asset precisa de prompt IA.
17. O checkpoint serve para uma escolha real pendente. Com direção autorizada, execute a entrega completa.
18. O resultado é uma especificação pronta para revisão. Não declare geração de imagens, implementação, testes ou publicação que não ocorreram.

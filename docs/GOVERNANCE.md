# Modelo de Governança do Projeto - Plataforma de Otimização de Portfólio HNWI (Brasil Open Source)

Este documento descreve o modelo de governança para o projeto open-source da Plataforma de Otimização de Portfólio HNWI. O objetivo é fornecer clareza sobre como as decisões são tomadas, como as contribuições são gerenciadas e como a comunidade pode participar.

## Filosofia Geral

Este projeto adota uma abordagem de governança aberta, meritocrática e colaborativa. Valorizamos a transparência, o respeito mútuo e as contribuições da comunidade. As decisões visam o melhor interesse do projeto e de seus usuários.

## 1. Funções e Responsabilidades

*   **Mantenedor(es) do Projeto (Maintainers):**
    *   Indivíduos responsáveis pela direção estratégica geral do projeto.
    *   Têm a palavra final sobre decisões técnicas e de roadmap, buscando consenso sempre que possível.
    *   Responsáveis por revisar e mesclar (merge) contribuições significativas (Pull Requests).
    *   Gerenciam o acesso ao repositório principal e a infraestrutura do projeto (se houver).
    *   Atuam como principais pontos de contato para a comunidade.
    *   No início do projeto, Arthur ([@arthur0211](https://github.com/arthur0211)) atua como o Mantenedor Principal.
    *   Novos mantenedores podem ser convidados com base em contribuições significativas e sustentadas e confiança da comunidade e dos mantenedores existentes.

*   **Contribuidores (Contributors):**
    *   Qualquer pessoa que contribui com código, documentação, relatórios de bugs, sugestões de features, traduções, ou participa ativamente das discussões do projeto.
    *   As contribuições são feitas via Pull Requests no GitHub, Issues, ou através dos canais de comunicação do projeto.
    *   Espera-se que os contribuidores sigam as diretrizes em `CONTRIBUTING.md` e o `CODE_OF_CONDUCT.md`.

*   **Usuários (Users):**
    *   Indivíduos ou organizações que utilizam a Plataforma (seja o código-fonte diretamente ou uma instância implantada).
    *   O feedback dos usuários é crucial e pode ser fornecido através de Issues no GitHub ou outros canais de comunicação.

## 2. Processo de Tomada de Decisão

*   **Decisões Técnicas e de Features:**
    *   Propostas para novas features significativas ou mudanças arquiteturais devem ser discutidas publicamente (e.g., através de GitHub Issues com a tag "enhancement" ou "discussion").
    *   O objetivo é alcançar consenso entre os mantenedores e a comunidade engajada.
    *   Se o consenso não for alcançado, os Mantenedores do Projeto tomarão a decisão final, explicando o racional.
*   **Revisão e Merge de Pull Requests (PRs):**
    *   PRs devem seguir as diretrizes do `CONTRIBUTING.md`.
    *   Pelo menos um Mantenedor (ou um contribuidor experiente designado) deve revisar o PR.
    *   PRs que introduzem novas funcionalidades ou mudanças significativas podem exigir revisão de múltiplos mantenedores.
    *   Feedback construtivo será fornecido, e espera-se que o autor do PR responda às sugestões.
    *   O merge será realizado por um Mantenedor após a aprovação.
*   **Roadmap e Planejamento:**
    *   O roadmap de alto nível será definido pelos Mantenedores, levando em consideração o feedback da comunidade, os objetivos do projeto (conforme PRD e `docs/mvp_scope.md`) e os recursos disponíveis.
    *   O progresso e os planos podem ser comunicados através de Milestones no GitHub, discussões no repositório ou outros anúncios.

## 3. Processo de Contribuição

Detalhes sobre como contribuir estão no arquivo `CONTRIBUTING.md`. Os pontos chave incluem:
*   Fazer fork do repositório e criar branches para features/correções.
*   Seguir os padrões de código e estilo (definidos em `pyproject.toml` e reforçados por linters/formatters).
*   Escrever testes para novas funcionalidades.
*   Manter a documentação atualizada.
*   Ser respeitoso e construtivo nas interações.

## 4. Código de Conduta

Todos os participantes do projeto (mantenedores, contribuidores, usuários em canais de discussão) devem aderir ao `CODE_OF_CONDUCT.md`. O objetivo é garantir um ambiente acolhedor, inclusivo e livre de assédio.

## 5. Comunicação

*   **GitHub Issues:** Principal canal para rastreamento de bugs, solicitação de features e discussões técnicas.
*   **GitHub Discussions:** (Se habilitado) Para perguntas gerais, ideias e discussões da comunidade.
*   **Outros Canais:** (A serem definidos, e.g., Discord, lista de e-mail) Serão anunciados no `README.md`.

## 6. Conflitos de Interesse

Mantenedores e contribuidores devem divulgar quaisquer potenciais conflitos de interesse que possam influenciar suas decisões ou contribuições ao projeto.

## 7. Evolução da Governança

Este modelo de governança pode evoluir conforme o projeto cresce e a comunidade se desenvolve. Mudanças significativas na governança serão discutidas com a comunidade antes de serem implementadas.

## 8. Reconhecimento

Valorizamos todas as contribuições e nos esforçaremos para reconhecer o trabalho da comunidade de forma apropriada (e.g., menções em notas de release, lista de contribuidores).

---

Este documento visa ser um guia vivo. Sugestões para melhorá-lo são bem-vindas e podem ser feitas através de uma Issue ou Pull Request. 
# Checklist: Plataforma de Otimização de Portfólio HNWI (Brasil - Open Source)

## Fase 0: Planejamento e Configuração do Projeto (M0)

### 1. Definição e Estruturação do Projeto
    - [X] 1.1. Definir escopo detalhado do MVP (Minimum Viable Product) focado no mercado brasileiro. (Documentado em `docs/mvp_scope.md`)
    - [X] 1.2. Pesquisar e definir personas de HNWIs e assessores de investimento brasileiros. (Documentado em `docs/personas.md`)
    - [X] 1.3. Pesquisar e listar os principais concorrentes e soluções similares no Brasil. (Documentado em `docs/competitor_analysis.md`)
    - [X] 1.4. Definir a stack tecnológica principal (Python 3.12, FastAPI, Postgres para backend; Next.js para frontend UI do Assessor confirmados para MVP. Outros como Kafka, Rust/WASM para fases futuras).
    - [X] 1.5. Configurar o ambiente de desenvolvimento (local, dev, staging, prod).
        - [X] 1.5.1. Versionamento de código (Git, GitHub/GitLab).
        - [X] 1.5.2. Gerenciamento de dependências (Poetry) - (Utilizado requirements.txt e pip inicialmente).
        - [X] 1.5.3. Ferramentas de linting e formatação (Black, isort, Flake8/Pylint) - (Configurado no pyproject.toml, pacotes instalados).
        - [X] 1.5.4. Configuração de testes (pytest) - (Configurado no pyproject.toml, pacote instalado).
        - [X] 1.5.5. CI/CD pipeline inicial (GitHub Actions). (Criado workflow básico em `.github/workflows/python-app.yml`)

### 2. Aspectos Legais e Open Source
    - [X] 2.1. Escolher uma licença open-source (e.g., MIT, Apache 2.0) - (MIT escolhida).
    - [X] 2.2. Criar arquivos `LICENSE`, `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
        - [X] 2.2.1. `README.md` inicial com descrição do projeto, objetivos, como contribuir, e como rodar.
        - [X] 2.2.2. `CONTRIBUTING.md` com diretrizes para contribuições (coding style, processo de PR).
    - [X] 2.2.3. (Manual) Criar arquivo `.env` com base no `.env.example`.
    - [X] 2.3. Pesquisar e documentar requisitos regulatórios brasileiros para plataformas de investimento (CVM, Bacen, LGPD). (Documentado em `docs/regulatory_requirements_br.md`)
        - [X] 2.3.1. Requisitos de suitability específicos do Brasil (CVM). (Documentado em `docs/regulatory_requirements_br.md`)
        - [X] 2.3.2. LGPD (Lei Geral de Proteção de Dados Pessoais) - implicações e conformidade. (Documentado em `docs/regulatory_requirements_br.md`)
        - [X] 2.3.3. Requisitos do BACEN (Banco Central do Brasil) relevantes. (Documentado em `docs/regulatory_requirements_br.md`)
    - [ ] 2.4. Definir DPO (Data Protection Officer) inicial para o projeto.
    - [ ] 2.5. Elaborar Política de Privacidade e Termos de Uso iniciais (rascunho).
    - [ ] 2.6. Definir estratégia de governança para o projeto open-source.

### 3. Internacionalização e Localização (i18n/l10n) - Foco Brasil
    - [ ] 3.1. Estruturar o projeto para suportar múltiplos idiomas, começando com Português do Brasil (pt-BR).
    - [ ] 3.2. Definir formato para arquivos de tradução (e.g., JSON, YAML).
    - [ ] 3.3. Coletar termos financeiros e de investimento específicos do mercado brasileiro.

## Fase 1: Fundação da Plataforma (M0-M3)

### 4. API de Perfil do Cliente (`Client-Profile API`)
    - [ ] 4.1. Modelagem do banco de dados (PostgreSQL).
        - [ ] 4.1.1. Schema para dados demográficos (adaptado para Brasil: CPF, etc.).
        - [ ] 4.1.2. Schema para Risk Number.
        - [ ] 4.1.3. Schema para perfil RISA.
        - [ ] 4.1.4. Schema para pontuações de vieses comportamentais.
    - [ ] 4.2. Desenvolvimento da API (FastAPI).
        - [ ] 4.2.1. Endpoints CRUD para perfil do cliente.
        - [ ] 4.2.2. Autenticação e Autorização (OAuth2/JWT).
        - [ ] 4.2.3. Validação de dados (Pydantic).
        - [ ] 4.2.4. Documentação da API (Swagger/OpenAPI).
    - [ ] 4.3. Integração com sistema de importação do Risk Number (se aplicável/disponível no Brasil).
    - [ ] 4.4. Considerar campos para Suitability (API da CVM, se houver).

### 5. Hub de Dados de Mercado (`Market-Data Hub`)
    - [ ] 5.1. Pesquisar e selecionar fontes de dados de mercado para o Brasil.
        - [ ] 5.1.1. B3 (ações, FIIs, Tesouro Direto, derivativos).
        - [ ] 5.1.2. Dados de fundos de investimento brasileiros (CVM, Anbima).
        - [ ] 5.1.3. Índices de mercado (Ibovespa, IFIX, IMA-B, etc.).
        - [ ] 5.1.4. Dados de ativos alternativos e ilíquidos no Brasil.
        - [ ] 5.1.5. Provedores de dados (e.g., Refinitiv, Bloomberg - verificar alternativas open-source ou mais acessíveis se possível, como a API da B3 ou `yfinance` para dados históricos).
    - [ ] 5.2. Desenvolver pipeline de dados (Kafka -> DuckDB -> Parquet).
        - [ ] 5.2.1. Conectores para as fontes de dados selecionadas.
        - [ ] 5.2.2. Processamento e limpeza dos dados.
        - [ ] 5.2.3. Armazenamento em Parquet via DuckDB.
        - [ ] 5.2.4. Agendamento de atualizações diárias.
    - [ ] 5.3. Integração com Addepar (ou alternativa similar/viável para dados de custódia múltipla no Brasil).

### 6. Motor de Otimização (`Optimization Engine`) - Baseline
    - [ ] 6.1. Implementar baseline MPT (Modern Portfolio Theory).
        - [ ] 6.1.1. Cálculo de retornos esperados e matriz de covariância para ativos brasileiros.
        - [ ] 6.1.2. Otimizador usando `cvxpy` e `PyPortfolioOpt`.
    - [ ] 6.2. Implementar modelo Black-Litterman.
        - [ ] 6.2.1. Incorporar visões do assessor/investidor sobre ativos brasileiros.
    - [ ] 6.3. Configurar para paralelização em Kubernetes (K8s).
    - [ ] 6.4. Desenvolver testes unitários e de integração para o motor.

## Fase 2: Funcionalidades Avançadas (M4-M6)

### 7. Integração RISA e Motor de Metas (3-L)
    - [ ] 7.1. Desenvolver questionário RISA (Risk, Income, Suitability, Aspiration).
        - [ ] 7.1.1. Traduzir e adaptar o questionário Kitces para o contexto brasileiro.
        - [ ] 7.1.2. Interface para preenchimento do questionário.
    - [ ] 7.2. Mapear perfil RISA para regras de "income sleeve" (segmentos de renda).
        - [ ] 7.2.1. Definir sub-pools de alocação (Rendimento Total, Proteção de Renda, Envoltório de Risco, Segmentação Temporal) com produtos brasileiros (e.g., títulos IPCA+, fundos de previdência, etc.).
    - [ ] 7.3. Implementar motor de metas baseado no modelo 3-L (Liquidez, Longevidade, Legado) da UBS.
        - [ ] 7.3.1. Adaptação do modelo 3-L para o contexto financeiro e de produtos brasileiros.
        - [ ] 7.3.2. Definir sub-fronteiras de otimização para cada "L".
            - [ ] 7.3.2.1. Liquidez: VaR anual <= 5% (usando ativos brasileiros de alta liquidez).
            - [ ] 7.3.2.2. Longevidade: Probabilidade máxima de déficit <= 10% (considerando previdência brasileira, NTN-B Principal).
            - [ ] 7.3.2.3. Legado: Maximizar média geométrica (com ativos de crescimento brasileiros).

### 8. Ajuste de Capital Humano (VLCM)
    - [ ] 8.1. Pesquisar e adaptar parâmetros do Vanguard VLCM (Value of Lifetime Capital Model) para o Brasil.
        - [ ] 8.1.1. Considerar dados de renda, expectativa de vida, e previdência social brasileira (INSS).
    - [ ] 8.2. Implementar cálculo do capital humano descontado.
    - [ ] 8.3. Integrar ajuste de capital humano nas restrições do otimizador.

## Fase 3: Módulos Especializados (M7-M9)

### 9. Módulo de Alternativos Ilíquidos
    - [ ] 9.1. Pesquisar e modelar ativos alternativos e ilíquidos comuns para HNWIs no Brasil (e.g., FIPs, FIDCs, imóveis, startups via equity crowdfunding).
    - [ ] 9.2. Previsão de fluxo de caixa:
        - [ ] 9.2.1. Modelar cronogramas de compromisso (commitment schedule).
        - [ ] 9.2.2. Simular curvas J (J-curves).
        - [ ] 9.2.3. Implementar reservas para chamadas de capital (capital-call buffers).
    - [ ] 9.3. Integração com o otimizador (considerando restrições de liquidez e alocação).

### 10. Módulo de Direct Indexing e Alpha Fiscal
    - [ ] 10.1. Pesquisar viabilidade e regulamentação de Direct Indexing no Brasil.
    - [ ] 10.2. Identificar clientes elegíveis (e.g., > R$ X em ações tributáveis).
    - [ ] 10.3. Implementar lógica para tax-loss harvesting (realização de prejuízo para compensação fiscal) de acordo com a legislação brasileira.
        - [ ] 10.3.1. Regras de wash sale (se aplicável no Brasil).
        - [ ] 10.3.2. Otimização fiscal na venda de ativos.
    - [ ] 10.4. Estimar e reportar o alfa fiscal esperado (considerando alíquotas brasileiras).
    - [ ] 10.5. (Opcional) Integração com APIs de corretoras brasileiras para execução, se possível.

### 11. Penalidades Comportamentais no Otimizador
    - [ ] 11.1. Integrar pontuações de vieses (do Client-Profile API).
    - [ ] 11.2. Implementar penalidade de CVaR ampliada para aversão à perda (λ > 1.33).
    - [ ] 11.3. Introduzir limite para home bias (se indicador > 0.7) – considerar home bias Brasil.

## Fase 4: UX, Relatórios e Governança (M10-M12)

### 12. UI do Assessor (`Advisor UI`) - Cockpit 2.0
    - [ ] 12.1. Desenvolvimento da interface (React + Next.js).
        - [ ] 12.1.1. Tradução completa para pt-BR.
    - [ ] 12.2. Painel de três visualizações:
        - [ ] 12.2.1. Resumo do perfil (Risk Number, RISA).
        - [ ] 12.2.2. Resultado da otimização (gráficos de pizza + glide path) com ativos brasileiros.
        - [ ] 12.2.3. Gráfico de funil do Monte Carlo.
    - [ ] 12.3. Widgets de atribuição de risco (estilo Aladdin) adaptados para mercado brasileiro.
    - [ ] 12.4. Ferramentas de gráficos (D3.js).

### 13. Serviço de Monte Carlo (`Monte-Carlo Service`)
    - [ ] 13.1. Desenvolver módulo em Rust (WebAssembly).
        - [ ] 13.1.1. Simular cenários de mercado baseados em dados brasileiros (volatilidade, correlações).
    - [ ] 13.2. Calcular e exibir pontuação de sucesso (probabilidade de sucesso) alinhada com metodologias conhecidas no Brasil (e.g., adaptação MoneyGuidePro).

### 14. Relatórios e Alertas Educacionais
    - [ ] 14.1. Geração de relatório para o cliente (comparando proposto vs. benchmark 3-L UBS) em linguagem clara e em português.
    - [ ] 14.2. "Nudges" educacionais baseados na lista de vieses da EY e explicações RISA (Kitces) traduzidas e adaptadas.
    - [ ] 14.3. Card de Alpha Fiscal quantificando economia esperada com Direct Indexing vs. ETFs/Fundos (considerando tributação brasileira).

### 15. Conformidade e Auditoria (`Compliance & Audit`)
    - [ ] 15.1. Logs imutáveis (SHA-256).
    - [ ] 15.2. Gerador de IPS (Investment Policy Statement) / API (Análise de Perfil do Investidor).
        - [ ] 15.2.1. Formato PDF via LaTeX (ou similar).
        - [ ] 15.2.2. Conformidade com CVM (Instrução CVM 539 e outras relevantes) e suitability.
        - [ ] 15.2.3. Conformidade com LGPD.
    - [ ] 15.3. Implementar trilhas de auditoria para todas as decisões e recomendações.
    - [ ] 15.4. (Opcional) Integração com sistemas de PLD/FT (Prevenção à Lavagem de Dinheiro e Financiamento ao Terrorismo) se aplicável.

### 16. Governança, KPIs e Melhoria Contínua
    - [ ] 16.1. Definir KPIs e metas para o mercado brasileiro.
        - [ ] 16.1.1. Probabilidade de Sucesso >= 85% para metas essenciais.
        - [ ] 16.1.2. Atrição anual por pânico < 3%.
        - [ ] 16.1.3. Sharpe do portfólio vs. benchmark (e.g., CDI, Ibovespa) dentro de +X.
        - [ ] 16.1.4. Ganho de alfa fiscal para clientes DI >= Y% a.a.
        - [ ] 16.1.5. Geração de API/IPS em < 24h do onboarding.
    - [ ] 16.2. Implementar fluxo GitOps para controle de versão de parâmetros de modelo.
    - [ ] 16.3. Configurar testes CI noturnos para validar métricas (Sharpe, shortfall) com dados históricos brasileiros.
    - [ ] 16.4. Mecanismos de feedback da comunidade open-source e dos usuários brasileiros.

## Fase 5: Pós-Lançamento e Manutenção Contínua

### 17. Documentação
    - [ ] 17.1. Documentação do usuário final (em português).
    - [ ] 17.2. Documentação técnica detalhada (Sphinx para Python, JSDoc/TSDoc para front-end).
        - [ ] 17.2.1. Docstrings PEP 257.
        - [ ] 17.2.2. Exemplos de uso nas docstrings.
    - [ ] 17.3. Documentação da API (OpenAPI/Swagger) atualizada.
    - [ ] 17.4. Tutoriais e guias para desenvolvedores e contribuidores (em português e inglês).

### 18. Comunidade e Suporte Open Source
    - [ ] 18.1. Criar fórum/lista de discussão/servidor Discord para a comunidade.
    - [ ] 18.2. Estabelecer processo para reportar bugs e solicitar features (GitHub Issues).
    - [ ] 18.3. Realizar revisões de código da comunidade.
    - [ ] 18.4. Promover o projeto em comunidades de desenvolvedores e finanças no Brasil.

### 19. Segurança Contínua
    - [ ] 19.1. Executar Bandit e Safety regularmente.
    - [ ] 19.2. Modelagem de ameaças (OWASP pytm) periódica.
    - [ ] 19.3. Auditorias de segurança (internas e/ou externas).
    - [ ] 19.4. Monitorar e aplicar patches de segurança para dependências.

### 20. Testes Abrangentes
    - [ ] 20.1. Manter cobertura de testes >= 90% (pytest).
    - [ ] 20.2. Desenvolver testes de integração para os microserviços.
    - [ ] 20.3. Desenvolver testes E2E para fluxos críticos do usuário.
    - [ ] 20.4. Testes de performance para gargalos identificados (especialmente motor de otimização e Monte Carlo).
    - [ ] 20.5. (Opcional) Testes baseados em propriedade (Hypothesis).

### 21. Melhorias e Novas Funcionalidades
    - [ ] 21.1. Coletar feedback e planejar próximas iterações.
    - [ ] 21.2. Pesquisar e integrar novas classes de ativos brasileiros (e.g., Fiagro, CRA, CRI).
    - [ ] 21.3. Adaptar para mudanças regulatórias no Brasil.
    - [ ] 21.4. Melhorar modelos de otimização com base em novas pesquisas acadêmicas e de mercado.
    - [ ] 21.5. Considerar integração com Open Finance Brasil.
    - [ ] 21.6. Explorar wrappers fiscais multi-jurisdição (se houver demanda de brasileiros com investimentos no exterior).

### 22. Deployment e Infraestrutura
    - [ ] 22.1. Refinar configuração de K8s para produção.
        - [ ] 22.1.1. Liveness/Readiness probes.
        - [ ] 22.1.2. Limites de recursos.
        - [ ] 22.1.3. Rolling updates.
        - [ ] 22.1.4. Helm charts.
    - [ ] 22.2. Configurar monitoramento e alertas (Prometheus, Grafana).
    - [ ] 22.3. Estratégia de backup e recovery para o banco de dados.
    - [ ] 22.4. Dockerfiles otimizados (multi-stage builds, base images mínimas).
    - [ ] 22.5. Health checks para todos os serviços.

Este checklist é um ponto de partida e deverá ser refinado e detalhado conforme o projeto avança.
A numeração M0-M12 refere-se aos meses do roadmap condensado no PRD. 
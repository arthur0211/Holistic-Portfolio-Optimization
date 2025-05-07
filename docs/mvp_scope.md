# Escopo do MVP (Minimum Viable Product) - Plataforma de Otimização de Portfólio HNWI Brasil

## Objetivo do MVP

O MVP visa entregar um núcleo funcional da plataforma que demonstre a sua proposta de valor única: uma otimização de portfólio para HNWIs brasileiros e seus assessores, integrando perfil psicométrico (RISA) com um modelo de metas financeiras (3-L), considerando as particularidades do mercado brasileiro.

## Personas-Chave (Foco do MVP)

1.  **"Sofia Inovadora" (Cliente HNWI - Brasil)**: Indivíduo com patrimônio entre R$5M-R$25M, tecnologicamente adepta, busca soluções de investimento personalizadas, sofisticadas e digitais. Valoriza transparência, ESG (a ser considerado em iterações futuras, não no MVP inicial), e precisa de explicações claras para estratégias complexas. Geralmente assessorada.
2.  **"Ricardo Experiente" (Assessor de Investimentos - Brasil)**: Certificado (CEA/CFP), com 5+ anos de experiência, gerencia carteiras de clientes HNWI. Necessita de ferramentas eficientes para diagnóstico de perfil (RISA), construção de portfólios alinhados aos objetivos do cliente e ao mercado brasileiro (tributação, ativos locais, modelo 3-L), e geração de relatórios para conformidade e comunicação.

## Funcionalidades Principais do MVP

O MVP se concentrará nas entregas correspondentes aos meses M0-M6 do roadmap do PRD, com foco nos seguintes componentes e funcionalidades:

### 1. Onboarding e Perfil do Cliente
    - **API de Perfil do Cliente (`Client-Profile API` - FastAPI, PostgreSQL):**
        - Armazenamento seguro de dados demográficos (adaptado para Brasil: CPF, estado civil, etc.).
        - Armazenamento de resultados do questionário RISA (Risk, Income, Suitability, Aspiration).
        - Armazenamento de pontuações de vieses comportamentais (input inicial, motor de vieses completo em iteração futura).
        - Endpoints CRUD para gerenciamento do perfil do cliente pelo assessor.
    - **Questionário RISA (Simplificado):**
        - Interface digital para o assessor aplicar ou o cliente preencher uma versão adaptada e traduzida do questionário RISA.
        - Cálculo e armazenamento do quadrante RISA resultante.

### 2. Hub de Dados de Mercado (Simplificado)
    - **Pipeline de Dados Inicial:**
        - Ingestão e armazenamento (Parquet/DuckDB) de dados de fechamento diário para um conjunto curado de ativos chave do mercado brasileiro:
            - Principais ações do Ibovespa.
            - Principais ETFs negociados na B3.
            - Títulos do Tesouro Direto (referências para taxas livres de risco e inflação).
            - Principais FIIs (Fundos de Investimento Imobiliário).
        - Fontes: APIs públicas da B3, dados do Tesouro Direto, provedores de dados gratuitos/acessíveis (e.g., `yfinance` para dados históricos como proxy inicial se necessário).
        - Atualização diária agendada.

### 3. Motor de Otimização Core
    - **Tecnologia:** Python, `cvxpy`, `PyPortfolioOpt`.
    - **Modelos Implementados:**
        - Otimização de Média-Variância (MPT) como baseline.
        - Modelo Black-Litterman para incorporação de visões (input simplificado pelo assessor no MVP).
    - **Motor de Metas 3-L (Liquidez, Longevidade, Legado):**
        - Definição de até 3 metas principais pelo cliente/assessor, mapeadas para os "L"s.
        - Criação de sub-portfólios ou "caixinhas" de otimização para cada "L", com objetivos e restrições específicas (e.g., VaR para Liquidez, probabilidade de shortfall para Longevidade).
    - **Overlay RISA:**
        - Mapeamento do perfil RISA do cliente para restrições de investimento ou parâmetros de aversão ao risco dentro de cada "L" ou no portfólio consolidado.
        - Exemplo: Cliente com RISA "Protetor de Renda" terá maior alocação em ativos de baixa volatilidade no L de Longevidade.

### 4. Interface do Assessor (UI - MVP Básico)
    - **Tecnologia:** React ou Next.js (a ser confirmado).
    - **Funcionalidades:**
        - Login seguro para assessores.
        - Listagem e busca de clientes.
        - Dashboard do Cliente:
            - Visualização do perfil demográfico.
            - Visualização do resultado do RISA.
        - Interface de Otimização:
            - Input/confirmação de metas 3-L para o cliente.
            - Visualização das restrições derivadas do RISA (informativo).
            - Execução do processo de otimização.
        - Resultados da Otimização:
            - Exibição da alocação de ativos proposta (gráficos de pizza, tabela).
            - Métricas básicas do portfólio (retorno esperado, volatilidade esperada).
        - Relatório Simplificado:
            - Geração de um PDF básico com o perfil do cliente e a alocação proposta.

### 5. Backend e Infraestrutura Essencial
    - **Autenticação e Autorização:** Implementação de JWT para proteger a API e o acesso à UI.
    - **Logging:** Logs estruturados para as principais operações da API e do motor de otimização.
    - **Configuração:** Uso de variáveis de ambiente (`.env`) para configurações sensíveis.
    - **Conteinerização:** Dockerfiles para os principais serviços (API, Motor se separado).

## Funcionalidades Fora do Escopo do MVP Inicial

As seguintes funcionalidades do PRD serão consideradas para iterações futuras, pós-MVP:

*   Ajuste completo de Capital Humano (VLCM).
*   Módulo de Alternativos Ilíquidos com simulação detalhada de J-Curve e capital calls.
*   Implementação completa de Direct Indexing e colheita de perdas fiscais (o MVP pode *sinalizar* a adequação, mas não implementará a mecânica fiscal).
*   Penalidades comportamentais avançadas no otimizador (além do RISA overlay básico).
*   Serviço de Monte Carlo em Rust/WASM para simulações de alta performance.
*   Widgets de risco avançados no estilo Aladdin.
*   Conectores para plataformas de custódia (e.g., Addepar).
*   Geração automática e completa de IPS (API da CVM).
*   Wrappers fiscais multi-jurisdição.
*   Nudges educacionais e relatórios avançados para o cliente final.
*   CI/CD pipeline completo (MVP terá setup básico de versionamento e testes).

## Considerações para o Mercado Brasileiro no MVP

*   **Idioma:** Toda a interface do usuário e relatórios gerados estarão em Português do Brasil.
*   **Ativos:** O foco será em ativos negociados na B3, Tesouro Direto e tipos de fundos comuns no Brasil.
*   **Regulatório (Princípios):** O design da coleta de dados do perfil do cliente e a lógica de recomendação (mesmo que simplificada) levarão em conta os princípios de suitability da CVM e a privacidade de dados (LGPD). A conformidade total e automatizada é um objetivo pós-MVP.
*   **Terminologia:** Será utilizada a terminologia financeira padrão do mercado brasileiro.

## Critérios de Sucesso do MVP

*   Assessores conseguem cadastrar clientes e realizar o perfilamento RISA.
*   O motor de otimização gera alocações coerentes baseadas no 3-L e RISA para um conjunto de ativos brasileiros.
*   Assessores conseguem visualizar e apresentar a alocação proposta aos seus clientes através da UI.
*   A plataforma demonstra estabilidade e segurança nos seus componentes core.
*   Feedback inicial de assessores piloto é positivo quanto à utilidade da abordagem RISA+3-L. 
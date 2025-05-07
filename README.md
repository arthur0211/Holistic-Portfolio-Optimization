# Projeto de Otimização de Portfólio HNWI (Brasil - Open Source)

Este projeto visa criar uma plataforma de otimização de portfólio centrada em HNWIs (High-Net-Worth Individuals) para o mercado brasileiro, com um enfoque open-source.

## Descrição

(Adicionar descrição detalhada do projeto aqui)

## Roadmap Inicial

Conforme `prd.md` e `checklist.md`:

*   **M0-M3:** Fundação da Plataforma (API de Perfil, Hub de Dados de Mercado, Motor de Otimização Baseline)
*   **M4-M6:** Funcionalidades Avançadas (Integração RISA, Motor de Metas 3-L, Ajuste de Capital Humano)
*   **M7-M9:** Módulos Especializados (Alternativos Ilíquidos, Direct Indexing, Penalidades Comportamentais)
*   **M10-M12:** UX, Relatórios e Governança (Advisor Cockpit 2.0, Monte Carlo, Conformidade)

## Começando

### Pré-requisitos

*   Python 3.10+
*   Poetry (recomendado para gerenciamento de dependências)
*   PostgreSQL

### Instalação

1.  Clone o repositório:
    ```bash
    git clone [URL_DO_REPOSITORIO]
    cd [NOME_DO_PROJETO]
    ```
2.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    # Windows (PowerShell)
    .venv\Scripts\Activate.ps1
    # Linux/macOS
    # source .venv/bin/activate
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    (Ou usando Poetry):
    ```bash
    # poetry install
    ```
4.  Configure as variáveis de ambiente. Copie `.env.example` para `.env` e preencha os valores necessários:
    ```bash
    cp .env.example .env
    ```
5.  Execute o servidor de desenvolvimento (FastAPI/Uvicorn):
    ```bash
    uvicorn src.api.main:app --reload
    ```

## Como Contribuir

Consulte `CONTRIBUTING.md` para detalhes sobre como contribuir com o projeto.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo `LICENSE` para mais detalhes. 
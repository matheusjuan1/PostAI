# 📱 PostAI - Sistema de Criação de Posts para Instagram com Agentes de IA

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Educational Project](https://img.shields.io/badge/Type-Educational-blue?style=for-the-badge&logo=bookstack&logoColor=white)](https://github.com/matheusjuan1)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

Este projeto foi desenvolvido com fins educacionais, como parte da Imersão IA promovida pela [Alura](https://www.alura.com.br/). O objetivo é demonstrar a criação de um sistema automatizado para gerar posts para o Instagram utilizando o framework de Agentes de Desenvolvimento do Google (ADK) e a API Gemini. O sistema é composto por quatro agentes distintos que colaboram para produzir um post final com base em um tema fornecido pelo usuário.

## ✨ Funcionalidades

O sistema PostAI possui o seguinte fluxo de trabalho, orquestrado por quatro agentes especializados:

1.  **Search Agent (Buscador):** Realiza buscas no Google para obter informações relevantes sobre o tema do post solicitado pelo usuário.
2.  **Planning Agent (Planejador):** Utiliza as informações encontradas pelo Search Agent para planejar a estrutura e o conteúdo do post para o Instagram.
3.  **Writing Agent (Redator):** Redige um post engajador para o Instagram, levando em consideração o planejamento feito pelo Planning Agent.
4.  **Review Agent (Revisor):** Revisa o post gerado pelo Writing Agent, buscando erros, sugestões de melhoria e garantindo que o post esteja adequado para publicação.

O fluxo principal do programa é sequencial: o usuário fornece um tema, que é processado pelos agentes na ordem listada, resultando em um post final revisado.

## ⚙️ Pré-requisitos

Antes de executar o projeto, você precisará ter o seguinte instalado:

* **Python 3.7 ou superior**
* **pip** (gerenciador de pacotes do Python)

## 🛠️ Instalação

1.  Clone o repositório do projeto (se aplicável).
2.  Navegue até o diretório do projeto no seu terminal.
3.  Crie um ambiente virtual para isolar as dependências do projeto:

    ```bash
    python -m venv .venv
    ```

4.  Ative o ambiente virtual:

    * **No Linux/macOS:**
        ```bash
        source .venv/bin/activate
        ```
    * **No Windows (PowerShell):**
        ```powershell
        . .\.venv\Scripts\Activate.ps1
        ```
    * **No Windows (CMD):**
        ```bash
        .venv\Scripts\activate
        ```

5.  Instale as dependências do projeto utilizando o pip:

    ```bash
    pip install python-dotenv google-adk rich
    ```

## ⚙️ Configuração

Para configurar o projeto, você precisará obter uma chave de API do Google Gemini e definir o modelo a ser utilizado pelos agentes:

1.  **Obtenha uma chave de API do Google Gemini:** Siga as instruções na documentação oficial do Google AI para obter sua chave de API.
2.  **Crie um arquivo `.env`** na raiz do seu projeto.
3.  **Adicione as seguintes variáveis de ambiente** ao arquivo `.env`, substituindo os valores pelos seus:

    ```dotenv
    GOOGLE_API_KEY=SUA_CHAVE_DE_API_GEMINI
    MODEL_ID=nome-do-modelo-que-voce-quer-usar
    ```

    Certifique-se de substituir `SUA_CHAVE_DE_API_GEMINI` pela sua chave de API real e `nome-do-modelo-que-voce-quer-usar` pelo ID do modelo Gemini que você deseja utilizar (por exemplo, `gemini-pro`).

## 🚀 Como Usar

Para executar o sistema de criação de posts, siga estes passos:

1.  Certifique-se de que o seu ambiente virtual esteja ativado (veja a seção de Instalação).
2.  Navegue até o diretório do projeto no seu terminal.
3.  Execute o script principal:

    ```bash
    python main.py
    ```

4.  O programa solicitará que você digite o tema para o post do Instagram. Digite o tema desejado e pressione Enter.
5.  O sistema então executará os quatro agentes em sequência, mostrando o progresso e o resultado de cada um. O post final revisado será exibido no terminal.

## ℹ️ Notas Adicionais

* Este projeto foi desenvolvido para fins educacionais e pode ter limitações em sua funcionalidade ou na qualidade dos posts gerados.
* Certifique-se de ter uma conexão de internet estável, pois o sistema faz chamadas à API do Google.
* Monitore o uso da sua chave de API do Google para evitar custos inesperados ou limites de taxa.

Sinta-se à vontade para explorar o código, modificar os agentes e expandir as funcionalidades deste projeto\! 😊

## 📝 Licença

Este projeto está sob a licença MIT.

Feito por Matheus Juan. [Entre em contato](https://www.linkedin.com/in/matheusjuan1/)

<div align="center">
  <img width="60" alt="Image" src="https://github.com/user-attachments/assets/efd1d014-148c-4ae8-8dbd-81850fadf9ba" />
</div>

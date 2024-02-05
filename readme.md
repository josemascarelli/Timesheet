# Configuração do Ambiente do Projeto

Este documento fornece um guia passo a passo para configurar o ambiente para este projeto.

## Pré-requisitos

- Python 3.8 ou superior
- pip (Gerenciador de pacotes do Python)
- Virtualenv (Opcional, mas recomendado)

## Passos para a Configuração

1. **Clone o repositório**

   Use o comando git abaixo para clonar o repositório:

   ```bash
   git clone https://github.com/josemascarelli/timesheet.git
    ```


2. **Crie um ambiente virtual (Opcional)**

    É uma boa prática isolar o ambiente do projeto usando um ambiente virtual. Você pode criar um usando o comando:

    Para ativar o ambiente virtual:

   ```bash
   python3 -m venv venv
    ```

    No Windows, execute: 
    
    ```bash
    venv\Scripts\activate
    ```

    No Unix ou MacOS, execute: 
    
    ```bash
    source venv/bin/activate
    ```


3. **Instale as dependências**

    Navegue até o diretório do projeto (onde o arquivo requirements.txt está localizado) e execute o seguinte comando para instalar todas as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```


4. **Execute as migrações do Django (se aplicável)**

    Se este for um projeto Django, você precisará aplicar as migrações usando o comando:

    ```bash
    python manage.py migrate
    ```


5. **Inicie o servidor de desenvolvimento**

    Agora você pode iniciar o servidor de desenvolvimento e começar a trabalhar no projeto:

    ```bash
    python manage.py runserver
    ```

Agora você deve ter um ambiente de desenvolvimento totalmente configurado para este projeto!
# RPA Rick and Morty – Coleta e Envio de Personagens

Este projeto é um **script em Python** que coleta informações de personagens da série **Rick and Morty** usando a [API oficial](https://rickandmortyapi.com/api/character/), armazena os dados em um **banco de dados SQLite** e envia por **e-mail** uma lista com os nomes dos personagens coletados. O script também possui um filtro específico para identificar personagens com o nome “Rick”.

---

## Funcionalidades

* Cria um **banco de dados SQLite** com duas tabelas:

  * `personagens`: armazena todos os personagens coletados.
  * `ricks`: armazena apenas os personagens cujo nome contém “Rick”.
* Coleta **10 personagens aleatórios** da API Rick and Morty.
* Salva os dados de cada personagem no banco (`id`, `name`, `status`, `specie`, `gender`).
* Envia um **relatório por e-mail** com os nomes dos personagens inseridos.
* Utiliza **Python**, **requests**, **sqlite3**, **smtplib**, e manipulação de e-mail com **MIMEText**.

---

## Requisitos

* Python 3.x
* Bibliotecas Python:

  ```bash
  pip install requests
  ```
* Conta de e-mail para envio (ex.: Gmail) com **senha de app** caso use autenticação de dois fatores.(Por padrão está exemplo@gmail.com que não ira funcionar caso você tente sem nenhuma alteração).

---

## Uso

1. Clone este repositório:

   ```bash
   git clone <link-do-repositório>
   cd <nome-do-repositório>
   ```
2. Configure o **login do e-mail** no script:

   ```python
   servidor_email.login('seu_email@gmail.com', 'sua_senha_ou_senha_de_app')
   remetente = 'seu_email@gmail.com'
   destinatario = 'destinatario@gmail.com'
   ```
3. Execute o script:

   ```bash
   python rpa_rick_and_morty.py
   ```
4. O banco de dados `rpa.db` será criado/atualizado e você receberá um e-mail com os nomes dos personagens coletados.

---

## Estrutura do Banco de Dados

* **Tabela `personagens`**

  * `id` – ID do personagem
  * `name` – Nome do personagem
  * `status` – Status (Alive, Dead, Unknown)
  * `specie` – Espécie
  * `gender` – Gênero

* **Tabela `ricks`**

  * Mesmos campos da tabela `personagens`, mas apenas para personagens cujo nome contém “Rick”.

---

## Observações

* O script gera **personagens aleatórios** usando a função `random.sample()`.
* Para funcionar com Gmail, é necessário habilitar **senha de app** se você tiver autenticação em duas etapas.
* Pode ser adaptado para outros provedores de e-mail alterando as configurações de SMTP.

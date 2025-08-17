import requests
import sqlite3
import re
import random
import smtplib
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

conexao = sqlite3.connect("BancoPersonagens.db")
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS personagens(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    status TEXT,
                    specie TEXT,
                    gender TEXT
                )
                ''')

cursor.execute('''
                CREATE TABLE IF NOT EXISTS ricks(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    status TEXT,
                    specie TEXT,
                    gender TEXT
                )
                ''')

conexao.close()

print("Banco de dados criado com sucesso!")


def extrair_personagem(id):
    resposta = requests.get(f"https://rickandmortyapi.com/api/character/{id}")
    dados = resposta.json()

    id = dados['id']
    name = dados['name']
    status = dados['status']
    species = dados['species']
    gender = dados['gender']
        
    conexao = sqlite3.connect("BancoPersonagens.db")
    cursor = conexao.cursor()
    
    nomes.append(name)
    cursor.execute('''
                INSERT INTO personagens(id, name, status, specie, gender)
                VALUES(?, ?, ?, ?, ?)
                ''',(id, name, status, species, gender))
 
    
    if re.search(r'rick', name, re.IGNORECASE):
        cursor.execute('''
                INSERT INTO ricks(id, name, status, specie, gender)
                VALUES(?, ?, ?, ?, ?)
                ''',(id, name, status, species, gender))
    
    conexao.commit()
    
nomes = []
    
personagems = random.sample(range(1, 827), 10)  
for personagem in personagems:
    extrair_personagem(personagem)
    
print("Banco de dados preenchido com sucesso!")


try:
    print("Envio de E-mail em andamento")

    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_email.starttls()
    servidor_email.login('exemplo@gmail.com', 'senha para uso')

    remetente = 'exemplo@gmail.com'
    destinatario = 'exemplo@gmail.com'

    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = 'Envio do relatorio'

    corpo = f'Olá, os nomes dos personagens de Rick e Morty inseridos no banco de dados foram:\n' + '\n'.join(nomes)
    mensagem.attach(MIMEText(corpo, 'plain'))

    servidor_email.sendmail(remetente, destinatario, mensagem.as_string())

    print("E-mail enviado com sucesso!")

except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")

finally:
    servidor_email.quit()
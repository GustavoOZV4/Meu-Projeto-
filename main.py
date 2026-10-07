from dotenv import load_dotenv
import os

load_dotenv()

senha_correta = os.getenv("SENHA")

senha = input("Digite a senha: ")

if senha == senha_correta:
    print("Acesso permitido!")
else:
    print("Senha incorreta!")
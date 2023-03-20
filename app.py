from flask import Flask, jsonify
from flask_restplus import Api
app = Flask(__name__)

@app.route("/<float:nota1>/<float:nota2>", methods=["GET"])
def segundo_endpoint(nota1: float , nota2: float)-> float:
  media = nota1 + nota2/2
  message= (f"A Média do Aluno: {media}")  
  return jsonify(message)


# Descrição do app
app_infos = dict( version='1.0',
                  title='Atividade Contínua 1 - Impacta Tecnologia',
                  description='Essa API calcula a média do aluno',
                  contact_email='matheus.nazario@aluno.faculdadeimpacta.com.br',
                  doc='/documentacao')

# inicia o swagger app
rest_app = Api(app, **app_infos)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

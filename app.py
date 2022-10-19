from flask import Flask

from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return "Bem vindo ao serviço do container 5050!" 

if __name__ == "__main__":
  sample.run(host="0.0.0.0", port=5050)

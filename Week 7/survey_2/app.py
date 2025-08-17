
from flask import Flask
from flask import Blueprint
from config.configuration import DEBUG
from services.db import init_db
from controller.agent_controller import agent_bp
from controller.client_controller import client_bp
from controller.question_controller import question_bp
from controller.answer_controller import answer_bp
from controller.response_controller import response_bp

app = Flask(__name__)

app.register_Blueprint(agent_bp)
app.register_Blueprint(client_bp)
app.register_Blueprint(question_bp)
app.register_Blueprint(answer_bp)
app.register_Blueprint(response_bp)


init_db()

if __name__ == '__main__':
    app.run(debug=DEBUG)

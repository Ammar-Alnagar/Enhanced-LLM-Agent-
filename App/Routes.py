from flask import Blueprint, render_template, request, jsonify
from agent.agent import create_agent_executor
 
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data['question']
    agent_executor = create_agent_executor()
    result = agent_executor.run(question)
    return jsonify({'result': result})

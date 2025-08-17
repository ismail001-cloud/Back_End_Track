from flask import Blueprint, request, jsonify
from services.db import get_db_connection

response_bp = Blueprint('responses', __name__)

@response_bp.route('/responses', methods=['POST'])
def create_response():
    data = request.get_json()
    agent_id = data.get('agent_id')
    client_id = data.get('client_id')
    question_id = data.get('question_id')
    answer_id = data.get('answer_id')
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.excute("INSERT INTO responses (agent_id, client_id, question_id, answer_id, name) VALUES(?, ?, ?, ?, ?, ?)",
                  (agent_id, client_id, question_id, answer_id, name))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({'message': 'response created successfully', 'response_id': new_id}), 201



@response_bp.route('/responses', methods=['GET'])

def get_responses():

    conn = get_db_connection()
    responses = conn.execute("SELECT * FROM responses").fetchall()
    conn.close()
    responses_list = [dict(response) for response in responses]
    return jsonify(responses_list)

@response_bp.route('/responses/<int:response_id>', methods=['GET'])
def get_response(response_id):

    conn = get_db_connection()
    response = conn.execute("SELECT *FROM responses WHERE id=?",(response_id,)).fetchone()

    conn.close
    if response is None:
        return jsonify({'error': 'response not found'}), 404
        return jsonify(dict(response))

@response_bp.route('/responses/<int:response_id>', methods=['PUT'])
def update_response(response_id):
    data = request.get_json()
    agent_id = data.get('agent_id')
    client_id = data.get('client_id')
    question_id = data.get('question_id')
    answer_id = data.get('answer_id')
    name = data.get('name')

    conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE responses
        SET agent_id = COALESCE(?, agent_id),
            client_id = COALESCE(?, client_id),
            question_id = COALESCE(?, question_id),
            answer_id = COALESCE(?, answer_id),
            name = COALESCE(?, name)
        WHERE id = ?
        """, (agent_id, client_id, question_id, answer_id, response_id, name))
    conn.commit()
    conn.close()

    return jsoify({'message': 'response updated successfully'})

@response_bp.route('/responses/<int:response_id>', methods=['DELETE'])
def delete_response(response_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM responses WHERE id = ?", (response_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'response successfully deleted'})
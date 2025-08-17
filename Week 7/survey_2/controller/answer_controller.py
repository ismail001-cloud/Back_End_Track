from flask import Blueprint, request, jsonify
from services.db import get_db_connection

answer_bp = Blueprint('answers', __name__)

@answer_bp.route('/answers', methods=['POST'])
def create_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.excute("INSERT INTO answers (question_id, name) VALUES(?, ?)",
                  (question_id, name))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({'message': 'answer created successfully', 'agent_id': new_id}), 201



@answer_bp.route('/answers', methods=['GET'])

def get_answers():

    conn = get_db_connection()
    answers = conn.execute("SELECT * FROM answers").fetchall()
    conn.close()
    answers_list = [dict(answer) for answer in answers]
    return jsonify(answers_list)

@answer_bp.route('/answers/<int:answer_id>', methods=['GET'])
def get_answer(answer_id):

    conn = get_db_connection()
    answers = conn.execute("SELECT *FROM answers WHERE id=?",(answer_id,)).fetchone()

    conn.close
    if answer is None:
        return jsonify({'error': 'Answer not found'}), 404
        return jsonify(dict(answer))

@answer_bp.route('/answers/<int:answer_id>', methods=['PUT'])
def update_answer(answer_id):
    data = request.get_json()
    question_id = data.get('question_id')
    name = data.get('name')

    conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE answers
        SET question_id = COALESCE (?, question_id),
            name = COALESCE(?, name),
            WHERE id = ?
        """, (question_id, name))
    conn.commit()
    conn.close()

    return jsoify({'message': 'answer updated successfully'})

@answer_bp.route('/answers/<int:answer_id>', methods=['DELETE'])
def delete_answer(answer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM answers WHERE id = ?", (answer_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Answer successfully deleted'})
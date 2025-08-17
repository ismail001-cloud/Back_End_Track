from flask import Blueprint, request, jsonify
from services.db import get_db_connection
from flask import Flask

agent_bp = Blueprint('agents', __name__)

@agent_bp.route('/agents', methods=['POST'])

def create_agent():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO agents (name, email, phone) VALUES(?, ?, ?)", (name, email, phone))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({'message': 'Agent created successfully', 'agent_id': new_id}), 201

@agent_bp.route('/agents', methods=['GET'])
def get_gents():
    conn = get_db_connection()
    agents = conn.execute("SELECT * FROM agents").fetchall()
    conn.close()
    agents_list = [dict(agent) for agent in agents]
    return jsonify(agents_list)

@agent_bp.route('/agents/<int:agent_id>', methods=['GET'])
def get_agent(agent_id):
    conn = get_db_connection()
    agent = conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
    conn.close()
    if agent is None:
        return jsonify({'error': 'Agent not found'}), 404
    return jsonify(dict(agent))

@agent_bp.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE agents
        SET name = COALESCE(?, name),
            email = COALESCE(?, email),
            phone = COALESCE(?, phone) 
        WHERE id = ?
        """, (name, email, phone, agent_id))
    conn.commit()
    conn.close()

    return jsoify({'message': 'agent updated successfully'})

@agent_bp.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM agents WHERE id = ?", (agent_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Agent successfully deleted'})
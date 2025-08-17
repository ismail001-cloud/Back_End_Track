from flask import Blueprint, request, jsonify
from services.db import get_db_connection

client_bp = Blueprint('clients', __name__)

@client_bp.route('/clients', methods=['POST'])
def create_clients():
    data = request.get_json()
    agent_id = data.get('agent_id')
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    NIN = data.get('NIN')
    driver_license = data.get('driver_license')
    lga = data.get('lga')
    state = data.get('state')
    education = data.get('education')
    gender = data.get('gender')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.excute("""INSERT INTO clients (agent_id, name, phone, email, NIN, 
                  driver_license, lga, state, education, gender)
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (agent_id, name, phone, email, NIN,
                  driver_license, lga, state, education, gender))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({'message': 'client created successfully', 'client_id': new_id}), 201



@client_bp.route('/clients', methods=['GET'])

def get_clients():

    conn = get_db_connection()
    clients = conn.execute("SELECT * FROM clients").fetchall()
    conn.close()
    clients_list = [dict(agent) for agent in clients]
    return jsonify(clients_list)

@client_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):

    conn = get_db_connection()
    client = conn.execute("SELECT *FROM clients WHERE id=?",(client_id,)).fetchone()

    conn.close
    if client is None:
        return jsonify({'error': 'client not found'}), 404
        return jsonify(dict(client))

@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    client_id = data.get('client_id')
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    NIN = data.get('NIN')
    driver_license = data.get('driver_license')
    lga = data.get('lga')
    state = data.get('state')
    education = data.get('education')
    gender = data.get('gender')

    conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clients
        SET client_id = COALESCE(?, client_id)
            name = COALESCE(?, name),
            phone = COALESCE(?, phone),
            email = COALESCE(?, email),
            NIN = COALESCE(?, NIN ),
            driver_license = COALESCE(?, driver_license),
            lga = COALESCE(?, lga),
            state = COALESCE(?, state),
            education = COALESCE(?, education),
            gender = COALESCE(?, gender)
        WHERE id = ?
        """, (client_id, name, phone, email,  NIN, lga, State, education, gender))
    conn.commit()
    conn.close()

    return jsoify({'message': 'client updated successfully'})

@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM client WHERE id = ?", (client_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'client successfully deleted'})
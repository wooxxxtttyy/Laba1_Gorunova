from flask import Flask, request, jsonify

app = Flask(__name__)

class Contact:
    def __init__(self, id, username, given_name, family_name, phone, email, birthdate):
        self.id = id
        self.username = username
        self.given_name = given_name
        self.family_name = family_name
        self.phone = phone
        self.email = email
        self.birthdate = birthdate

class Group:
    def __init__(self, id, title, description, contacts):
        self.id = id
        self.title = title
        self.description = description
        self.contacts = contacts

# функции для Contact
def create_contact(data):
    return Contact(**data)

def read_contact(contact_id):
    return Contact(id=contact_id, username='', given_name='', family_name='', phone=[], email=[], birthdate='')

def update_contact(contact_id, data):
    return Contact(**data)

def delete_contact(contact_id):
    return None

# функции для Group
def create_group(data):
    return Group(**data)

def read_group(group_id):
    return Group(id=group_id, title='', description='', contacts=[])

def update_group(group_id, data):
    return Group(**data)

def delete_group(group_id):
    return None

# Конечные точки для Contact
@app.route('/api/v1/contact', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_contact():
    if request.method == 'POST':
        data = request.json
        contact = create_contact(data)
        return jsonify(contact.__dict__), 201
    
    elif request.method == 'GET':
        contact_id = request.args.get('id')
        contact = read_contact(contact_id)
        return jsonify(contact.__dict__), 200

    elif request.method == 'PUT':
        contact_id = request.args.get('id')
        data = request.json
        contact = update_contact(contact_id, data)
        return jsonify(contact.__dict__), 200

    elif request.method == 'DELETE':
        contact_id = request.args.get('id')
        delete_contact(contact_id)
        return '', 204

# Конечные точки для Group
@app.route('/api/v1/group', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_group():
    if request.method == 'POST':
        data = request.json
        group = create_group(data)
        return jsonify(group.__dict__), 201
    
    elif request.method == 'GET':
        group_id = request.args.get('id')
        group = read_group(group_id)
        return jsonify(group.__dict__), 200

    elif request.method == 'PUT':
        group_id = request.args.get('id')
        data = request.json
        group = update_group(group_id, data)
        return jsonify(group.__dict__), 200

    elif request.method == 'DELETE':
        group_id = request.args.get('id')
        delete_group(group_id)
        return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6080)

from flask import Flask, jsonify, request

app = Flask(__name__)
items = {}

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(items.values())), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()

    item_id = max(items.keys(), default=0) + 1
    item = {
        'id': item_id,
        'name': data.get('name'),
        'value': data.get('value'),
        'description': data.get('description')  # NUEVO CAMPO
    }

    items[item_id] = item
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404

    data = request.get_json()
    item = items[item_id]

    item['name'] = data.get('name', item['name'])
    item['value'] = data.get('value', item['value'])
    item['description'] = data.get('description', item['description'])  

    return jsonify(item), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404

    deleted = items.pop(item_id)
    return jsonify(deleted), 200

if __name__ == '__main__':
    app.run(debug=True)

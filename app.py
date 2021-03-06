from flask import Flask, jsonify, request


POSTS = [
    {
        'id': 1,
        'name': 'John',
        'last_name': 'Doe'
    },
    {
        'id': 2,
        'name': 'James',
        'last_name': 'Corden'
    },
    {
        'id': 3,
        'name': 'Annie',
        'last_name': 'Thompson'
    },
]


app = Flask(__name__)


@app.route('/posts', methods=['GET', 'POST'])
def items():
    response_data = {
        'success': True,
        'data': []
    }

    if request.method == 'GET':
        response_data['data'] = POSTS
        return jsonify(response_data)
    elif request.method == 'POST':
        data = request.json
        if 'id' not in data or 'name' not in data or 'last_name' not in data:
            response_data['success'] = False
            response_data['error'] = 'Please provide all required information'
            response = jsonify(response_data)
            response.status_code = 400
        else:
            POSTS.append(data)
            response_data['data'] = POSTS
            response = jsonify(response_data)
            response.status_code = 201
        return response


@app.route('/posts/<int:post_id>')
def item(post_id):
    response_data = {
        'success': True,
        'data': []
    }

    try:
        item = [post for post in POSTS if post['id'] == post_id][0]
    except IndexError:
        response_data['success'] = False
        response_data['error'] = 'Not found'
        response = jsonify(response_data)
        response.status_code = 404
    else:
        response_data['data'] = item
        response = jsonify(response_data)
    return response


@app.errorhandler(404)
def not_found(error):
    response_data = {
        'success': False,
        'data': [],
        'error': 'Not found'
    }
    response = jsonify(response_data)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)

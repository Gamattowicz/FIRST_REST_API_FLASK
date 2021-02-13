from flask import Flask, jsonify


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


@app.route('/posts')
def items():
    response_data = {
        'success': True,
        'data': POSTS
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)

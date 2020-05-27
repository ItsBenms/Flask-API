from flask import Flask, jsonify, request, render_template

"""Flask APP to enable users to be displayed, added and deleted from an API"""

app = Flask(__name__)

users = [  # Users dictionary of the default users that can be added to
    {
        "id": 1,
        "firstName": "George",
        "lastName": "Bluth",
        "email": "george.bluth@reqres.in",
        "avatar": ""
    },
    {
        "id": 2,
        "firstName": "Janet",
        "lastName": "Weaver",
        "email": "janet.weaver@reqres.in",
        "avatar": ""
    },
    {
        "id": 3,
        "firstName": "Emma",
        "lastName": "Wong",
        "email": "emma.wong@reqres.in",
        "avatar": ""
    },
    {
        "id": 4,
        "firstName": "Eve",
        "lastName": "Holt",
        "email": "eve.holt@reqres.in",
        "avatar": ""
    },
    {
        "id": 5,
        "firstName": "Charles",
        "lastName": "Morris",
        "email": "charles.morris@reqres.in",
        "avatar": ""
    },
    {
        "id": 6,
        "firstName": "Tracey",
        "lastName": "Ramos",
        "email": "tracey.ramos@reqres.in",
        "avatar": ""
    }
]


@app.route('/', methods=['GET'])
def home():
    """Default route that displays html page"""
    return render_template("users.html")


@app.route('/users/all', methods=['GET'])  # Displays all users
def api_all():
    """Route to display all users"""
    return jsonify({'users': users})


@app.route('/users/select/<int:id>', methods=['GET'])  # Displays a single user
def one_user(id):
    """Route to display an individual user by passing in the users ID"""
    this_user = users[0]
    for i, u in enumerate(users):
        if u['id'] == id:
            this_user = users[i]
    return jsonify({'users': this_user})


@app.route('/users/all', methods=['POST'])  # Add new user
def add_user():
    """Route to add a new user to the API"""
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({'users': users})


@app.route('/users/select/<int:id>', methods=['PUT'])  # Edit User
def edit_user(id):
    """Route to edit a user who already exists by taking in the users ID"""
    modify_user = request.get_json()
    for i, u in enumerate(users):
        if u['id'] == id:
            users[i] = modify_user
    new = request.get_json()
    return jsonify({'users': users})


@app.route('/users/delete/<int:id>', methods=['DELETE'])  # Delete User
def delete_user(id):
    """Route to delete a user by taking in the users ID"""
    for i, u in enumerate(users):
        if u['id'] == id:
            del users[i]
    return jsonify({'users': users})


if __name__ == '__main__':
    app.run(debug=True)  # Debug mode enabled

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = [
    {
        "id": 1,
        "firstName": "George",
        "lastName": "Bluth",
        "email": "george.bluth@reqres.in"
    },
    {
        "id": 2,
        "firstName": "Janet",
        "lastName": "Weaver",
        "email": "janet.weaver@reqres.in"
    },
    {
        "id": 3,
        "firstName": "Emma",
        "lastName": "Wong",
        "email": "emma.wong@reqres.in"
    },
    {
        "id": 4,
        "firstName": "Eve",
        "lastName": "Holt",
        "email": "eve.holt@reqres.in"
    },
    {
        "id": 5,
        "firstName": "Charles",
        "lastName": "Morris",
        "email": "charles.morris@reqres.in"
    },
    {
        "id": 6,
        "firstName": "Tracey",
        "lastName": "Ramos",
        "email": "tracey.ramos@reqres.in"
    }
]


@app.route('/', methods=['GET'])
def home():
    return render_template("users.html")


@app.route('/users/all', methods=['GET'])  # Displays all users
def api_all():
    return jsonify({'users': users})


@app.route('/users/select/<int:id>', methods=['GET'])  # Displays a single user
def one_user(id):
    this_user = users[0]
    for i, u in enumerate(users):
        if u['id'] == id:
            this_user = users[i]
    return jsonify({'users': this_user})


@app.route('/users/all', methods=['POST'])  # Add new user
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify({'users': users})


@app.route('/users/select/<int:id>', methods=['PUT'])  # Edit User
def edit_user(id):
    modify_user = request.get_json()
    for i, u in enumerate(users):
        if u['id'] == id:
            users[i] = modify_user
    new = request.get_json()
    return jsonify({'users': users})


@app.route('/users/delete/<int:id>', methods=['DELETE'])  # Delete User
def delete_user(id):
    for i, u in enumerate(users):
        if u['id'] == id:
            del users[i]
    return jsonify({'users': users})

##Here u were not running debugging mode which made it so that u have to reset the server every time u update the static content aka the HTML 
##This is stupid and makes everything tedious af also im sure this must have caused u some confusion(it confused me for a moment)
if __name__ == '__main__':
    app.run(debug=True)
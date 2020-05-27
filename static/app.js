/* function to load all the users from the api - Working */

    document.addEventListener("DOMContentLoaded", () => {
           loadUsers(); // Checks page is loaded before running function
        })

    function loadUsers() {
            var xhr = new XMLHttpRequest();
            xhr.open("GET", '/users/all', true);

            xhr.onload = function () {
                if (this.status == 200) {
                    var users = JSON.parse(this.responseText);
                    //console.log(users)

                    var output = '';
                    for (i in users.users) {
                        output +=
                            '<tr>' + // Appends data from the users array to table
                            '<td>' + users.users[i].id + '</td>' +
                            '<td>' + users.users[i].email + '</td>' +
                            '<td>' + users.users[i].firstName + '</td>' +
                            '<td>' + users.users[i].lastName + '</td>' +
                            '<td>' + users.users[i].avatar + '</td>' +
                            '</tr>'
                    }
                    document.getElementById('userBody').innerHTML = output;
                }else{
                    alert("Error " + xhr.status)
                }
            }
            xhr.send()
        }

        /* Function to add users to the api when user form is entered - Working  */

            document.addEventListener('DOMContentLoaded', () => { // Checks page is loaded before running function
            document.getElementById("btnNewUser").addEventListener("click", addUser)
        })

        const addUser = function (ev) {
            ev.preventDefault(); // Prevents submit button from default submit action
            //let users = [];
            let user = {
                id: document.getElementById("newUserID").value, // Stores value of element in user object
                email: document.getElementById("newUserEmail").value,
                firstName: document.getElementById("newUserFirstName").value,
                lastName: document.getElementById("newUserLastName").value
            }
            //users.push(user); //pushes to array
            document.getElementById("frmNewUser").reset();
            //console.log(users)
            let json = JSON.stringify(user); //array to json string
            //console.log(json)

            const xhr = new XMLHttpRequest();

            xhr.open("POST", "/users/all", true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(json);
        }

    /* User Selection - Working */

 document.addEventListener("DOMContentLoaded", () => { // Checks page is loaded before running function
           updateUserPop();
        })

    function updateUserPop() {

        var table = document.getElementById('tblUsers'); // Selects table element

        for (var i = 1; i < table.rows.length; i++) {
            //console.log(table.rows)
            table.rows[i].onclick = function () {
                // Displays specific cell data in the given elements via ID
                document.getElementById("userID").value = this.cells[0].innerHTML;
                document.getElementById("userEmail").value = this.cells[1].innerHTML;
                document.getElementById("userFirstName").value = this.cells[2].innerHTML;
                document.getElementById("userLastName").value = this.cells[3].innerHTML;
            };
        }
    }

     /* Function to delete a user - Working */

            document.addEventListener('DOMContentLoaded', () => { // Checks page is loaded before running function
            document.getElementById("btnDeleteUser").addEventListener("click", deleteUser)
        })

        const deleteUser = function (ev) {
            ev.preventDefault();
            //let users = [];
            let user = {
                id: document.getElementById("userID").value // Selects users ID
            }
            document.getElementById("frmUser").reset(); // Resets input form
            //console.log(user.id)
            let json = JSON.stringify(user); //array to json string
            //console.log(json)

            const xhr = new XMLHttpRequest();

            xhr.open("DELETE", "/users/delete/" + user.id, true); // Opens request attaching users ID
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(json);
        }

        /* Function to update a user - Not Working */

        document.addEventListener('DOMContentLoaded', () => { // Checks page is loaded before running function
            document.getElementById("btnSaveUser").addEventListener("click", updateUser)
        })

        const updateUser = function (ev) {
            ev.preventDefault();
            //let users = [];
            let user = {
                id: document.getElementById("userID").value, // Stores value of element in user object
                email: document.getElementById("UserEmail").value,
                firstName: document.getElementById("UserFirstName").value,
                lastName: document.getElementById("UserLastName").value
            }
            document.getElementById("frmUser").reset(); // Resets input form
            //console.log(users)
            console.log(user)
            let json = JSON.stringify(user); //array to json string
            console.log(json)

            const xhr = new XMLHttpRequest();

            xhr.open("PUT", "/users/select/" + user.id, true); // Opens request attaching users ID
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.send(json);
        }
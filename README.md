I have built a Flask application that implements REST APIs to interact with the users and let users register their acount, authenticate themselves and perform CRUD operations.
Furthermore the app is deployed on Heroku so that anyone can access it.

App Heroku URL: https://stores99restapi.herokuapp.com/

The database support is provided by PostgreSQL and I have used SQLAlchemy to provide an abstraction on the database and handle the database operations using the SQLAlchemy object.Futhermore I have implement JWT so that when the user wants to fetch data about a specific item, they need to have a token to complete the request.It can be added to any operation and I added to one of the operations to test its working.To enhance the performance of the app, I have also enabled uwsgi that interacts with the app and provides additional functionalities like multithreading etc.

Below is an instruction on how you can interact with the app and perform CRUD operations.

Note: I have used POSTMAN to test the API endpoints.

When you visit the App URL, you may see something like this
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot1.png?raw=true "Optional Title")

First you need to register to start interacting.To register, add the '/register' to front of the app URL and perform a POST request containing 'username' and 'password' in JSON format.

{
  "username": "Souvik",
  "password": "1234"
}

You will receive a response like below




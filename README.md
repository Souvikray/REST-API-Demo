I have built a Flask application that implements REST APIs to interact with the users and let users register their acount, authenticate themselves and perform CRUD operations.
Furthermore the app is deployed on Heroku so that anyone can access it.

App Heroku URL: https://stores99restapi.herokuapp.com/

The database support is provided by PostgreSQL and I have used SQLAlchemy to provide an abstraction on the database and handle the database operations using the SQLAlchemy object.Futhermore I have implemented JWT so that when the user wants to fetch data about a specific item or all the items, they need to have a token to complete the request.It can be added to any operation and I added to one of the operations to test its working.To enhance the performance of the app, I have also enabled ```uwsgi``` that interacts with the app and provides additional functionalities like multithreading etc.

Below is an instruction on how you can interact with the app and perform CRUD operations.

**Note: I have used POSTMAN to test the API endpoints.**

When you visit the App URL, you may see something like this
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot1.png?raw=true "Optional Title")

First you need to register to start interacting.To register, add the ```/register``` end point to front of the app URL and perform a ```POST``` request containing 'username' and 'password' in JSON format.
```
{
  "username": "Souvik",
  "password": "1234"
}
```
You will receive a response like this below
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot2.png?raw=true "Optional Title")

Furthermore you need to get an ```access token``` if you want to view details of items.So add the ```/auth``` end point to front of the app URL and perform a ```POST``` request.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot3.png?raw=true "Optional Title")

You can even perform a test to check if you indeed receive an ```auth token```.If you do, you will see a ```PASS``` message else you will receive a ```FAIL``` test message.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot4.png?raw=true "Optional Title")

Now you can start creating stores that can hold multiple items.Let us create a 'Fruits' store that will store fruit items.So add the ```/store/Fruits``` end point to front of the app URL and perform a ```GET``` request.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot5.png?raw=true "Optional Title")

Similarly you can create more stores.Let us create another store 'Food'

Now you can start creating items that will get added to the respective stores.Let us add an item 'Banana' to the first store ie 'Fruits' store.To add an item, add the ```/item/banana``` end point to front of the app URL and perform a ```POST``` request containing 'price' and 'store_id' in JSON format.
```
{
  "price": 3.99,
  "store_id": 1
}
```
You will receive a response like this below
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot6.png?raw=true "Optional Title")

Similarly you can create another item say 'Apple' and add it to the 'Fruits' store.Let us set the price to 9.99.

Further you can also use the ```PUT``` method to create or modify an existing item.Say we want to change the price of the apple to 7.99.To modify an item, add the ```/item/banana``` end point to front of the app URL and perform a ```PUT``` request containing new 'price' and 'store_id' in JSON format.
```
{
  "price": 7.99,
  "store_id": 1
}
```
Below you can see the updated price
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot7.png?raw=true "Optional Title")

Let us create items for the second store 'Food'.Like before to add an item, add the ```/item/<name>``` end point to front of the app URL and perform a ```POST``` request containing 'price' and 'store_id' in JSON format.Let us add an item say 'Burger'.

You will receive a response like this below
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot8.png?raw=true "Optional Title")

We can similarly add another item say 'Pizza' priced at 12.99

Now you can get a list of all the stores in the database by adding the ```/stores``` end point to front of the app URL and perform a ```GET``` request.Note that you need to provide ```auth token``` to access the stores information.Below is the response which gives information of all the stores stored in the database.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot9.png?raw=true "Optional Title")

You can also view all the items that are stored across multiple stores.Add the ```/items``` end point to front of the app URL and perform a ```GET``` request.Note that you need to provide ```auth token``` to access the items information.You will get a response like this below
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot10.png?raw=true "Optional Title")

To view a specific item add the ```/item/<name>``` end point to front of the app URL and perform a ```GET``` request.Say we want to view the information for the item 'burger'.Note that you need to provide ```auth token``` to access a specific item information.You will get a response like this below.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot11.png?raw=true "Optional Title")

You can also delete an item.Add the ```/item/<name>``` end point to front of the app URL and perform a ```DELETE``` request.Say we want to delete an item 'apple'.You wil get a response like this below.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot12.png?raw=true "Optional Title")

Now you can check if the item has been deleted by simply accessing the ```/items``` end point.Below is the response that shows 'apple' has been deleted.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot13.png?raw=true "Optional Title")

Similarly you can also delete a store.So all the items in the store will also get deleted.To delete a specific item add the ```/store/<name>``` end point to front of the app URL and perform a ```DELETE``` request.Say we want to delete the store 'Fruits'.

We will get a response like this below that shows the store 'Fruits' and all the items in it has been indeed deleted.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot14.png?raw=true "Optional Title")

Now we can check to confirm that the store 'Fruits' has indeed been deleted.Simply access the ```/stores``` end point.Below is the response that shows 'Fruits' store has been deleted.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot15.png?raw=true "Optional Title")

Heroku also provides tools to monitor your database.Below is a screenshot of the current status of my database.
![Alt text](https://github.com/Souvikray/REST-API-Demo/blob/master/screenshot16.png?raw=true "Optional Title")

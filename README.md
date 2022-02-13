# Python simple back-end with JWT authentication

Made with python3.

### How to run the application?

Install python3 and pip on your machine.

Clone the repository and run the following command to install dependencies:

```
pip install -r requirements.txt
```

the following routes will be available for testing:

- /test - Shows a simple JSON: "data": "Hello World!"
- /register - Register a user. Use the following pattern to insert data:

```
{
    "username": username,
    "name": name,
    "password": password
}
```

- /login - Route receives a user and returns a token. Use the following pattern to insert data:

```
{
    "username": username
    "password": password
}
```

#### NOTE: ROUTES DON'T HAVE EMPTY DATA VALIDATION YET.

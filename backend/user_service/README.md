# User Management Service

## Set up
- Have at least python 3.8 installed
- Run `python3 -m venv .venv` to create a virtual environment
- Run `.venv\Scripts\activate` to start the virtual environment
- To exit the virtual environment, `deactivate venv`
- Run `pip install -r requirements.txt` to install dependencies

## Env variables
- Set the following environment variables in a `.env` file.
- CRED_PATH which is the path to the credentials file.
- You can get the credentials file from the firebase console under service accounts --> firebase admin sdk.

## Run the server
- Follow the above
- Make sure you are in the `user_service/app` directory
- run `flask --app main run`

## For debugging
- Use `flask --app main run --debug`

## Endpoints
- GET `http://localhost:5000/users`
- GET `http://localhost:5000/users/active`
- GET `http://localhost:5000/users/<user_id>`
- DELETE `http://localhost:5000/users/<user_id>`
- PATCH `http://localhost:5000/users/<user_id>`
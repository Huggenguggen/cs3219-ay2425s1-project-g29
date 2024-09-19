# Question Service

## Setup

1. Ensure you have **Python 3.8** or later installed:
   - Use `python3 --version` to check.

2. Navigate to the `user_service` directory in your terminal.

3. Set up a virtual environment:
    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:
   - macOS/Linux:  
     ```bash
     source .venv/bin/activate
     ```
   - Windows:  
     ```bash
     .venv\Scripts\activate
     ```

5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. To deactivate the virtual environment (when you're done working):
   ```bash
   deactivate
   ```

## Environment Variables

1. Create a `.env` file in the `app` directory.
2. To retrieve the Firebase credentials file:
   - Go to the [Firebase Console](https://console.firebase.google.com/).
   - Navigate to **Project Settings** → **Service Accounts** → **Firebase Admin SDK** -> **Generate new private key**.
   - Generate a new private key and download the credentials file to the `app` directory.
3. Add the following variables to the `.env` file:
   - `CRED_PATH`: This should be the absolute path to your Firebase credentials file (e.g., `/path/to/firebase/credentials.json`).
     - On windows this will be something like `C:\\Users\\USERNAME\\path\\to\\firebase-credentials.json`.

## Running the Server

1. Ensure the virtual environment is activated.
2. Navigate to the `user_service/app` directory.
3. Start the Flask server:
   ```bash
   flask --app main run -p 5000
   ```

## Debugging Mode

To run the server with debugging enabled:
```bash
flask --app main run -p 5000 --debug
```

## Available Endpoints

- **Get all questions**:  
  `GET http://localhost:5000/questions`
  
- **Get one question by ID**:
  `GET http://localhost:5000/questions/<id>`

- **Add a question**:  
  `POST http://localhost:5000/questions`

- **Delete a question**:  
  `DELETE http://localhost:5000/questions/<id>`
  
- **Update a question**:  
  `PUT http://localhost:5000/questions/<id>`
  
  
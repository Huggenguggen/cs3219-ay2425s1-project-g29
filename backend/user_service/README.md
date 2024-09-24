# User Management Service

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
     - On windows this will be something like `C:\\Users\\USERNAME\\path\\to\\firebase-credentials.json`

## Running the Server

1. Ensure the virtual environment is activated with
   ```
   .\venv\Scripts\activate
   ```
2. Navigate to the `user_service` directory.
3. Start the Flask server
   ```
   python run.py
   ```

## Debugging Mode

To run the server with debugging enabled:

```bash
flask --app main run -p 5001 --debug
```

## Available Endpoints

- **Get all users**:  
  `GET http://localhost:5001/users`
- **Get all active users**:  
  `GET http://localhost:5001/users/active`
- **Get a specific user by ID**:  
  `GET http://localhost:5001/users/<user_id>`

- **Delete a user by ID**:  
  `DELETE http://localhost:5001/users/<user_id>`

- **Update a user by ID**:  
  `PATCH http://localhost:5001/users/<user_id>`
  - TODO: Not implemented properly yet

### Admin Endpoints

- **Assign Admin Role**:\
  `POST http://localhost:5001/admin/users/<user_id>/roles/admin`

- **Remove Admin Role**:\
  `DELETE http://localhost:5001/admin/users/<user_id>/roles/admin`

- **Retrieve all roles of a UID**:\
  `GET http://localhost:5001/admin/users/<user_id>/roles`

- **Check if a UID is an admin (might remove in the future)**:\
  `GET http://localhost:5001/admin/users/<user_id>/is_admin`
  
- **Retrieve a list of all admins**:\
  `GET http://localhost:5001/admin/roles/admin/users`

---

### Additional Notes

- Ensure `FLASK_APP=main` is set in your environment if `flask --app main` doesn't work directly.
- If `flask` commands aren't recognized, ensure that Flask is properly installed and included in your `requirements.txt`.
- On macOS/Linux, you may need to give execution permissions to scripts:
  ```bash
  chmod +x .venv/bin/activate
  ```

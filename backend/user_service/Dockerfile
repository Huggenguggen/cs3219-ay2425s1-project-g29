FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

COPY app/.env /app/.env

# Copy importantjson.json and ensure it's in the path as per CRED_PATH
COPY app/peerprep-g29-firebase-adminsdk-z24kx-e97d801b1c.json /app/peerprep-g29-firebase-adminsdk-z24kx-e97d801b1c.json

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run your Flask app
ENTRYPOINT ["python"]
CMD ["main.py"]
# 📝 NotesApp API

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

A simple, high-performance, and asynchronous API for managing notes, built with **FastAPI**. This project provides a lightweight backend for creating, retrieving, updating, and associating files with notes, using in-memory storage for rapid development and testing.

---

## 🚀 Key Features

-   **Fast & Modern:** Built on FastAPI and Starlette for asynchronous, high-speed performance.
-   **Effortless CRUD:** Simple endpoints for creating, reading, updating, and managing notes.
-   **File Uploads:** Seamlessly upload and associate files with your notes.
-   **Automatic Docs:** Interactive API documentation powered by Swagger UI and ReDoc out of the box.
-   **In-Memory Storage:** Quick to set up and run, perfect for prototyping and small-scale applications.

---

## 🏁 Getting Started

Follow these steps to get the API up and running on your local machine.

### 1. Prerequisites

Make sure you have **Python 3.8** or newer installed.

### 2. Clone & Install Dependencies

Clone this repository and navigate into the project directory.

```bash
git clone <your-repository-url>
cd notes-api
```
Install the required Python packages using pip:
```bash
pip install "fastapi[all]" uvicorn
```
3. Run the Server
Start the development server with Uvicorn. The --reload flag will automatically restart the server on code changes.
```bash

uvicorn main:app --reload
```

The API will now be running at http://127.0.0.1:8000.

4. Explore the API
You can interact with the API using the automatically generated documentation:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📁 Project Structure
```bash
notes/
├── main.py          # Main FastAPI application logic and endpoints
├── uploads/         # Default directory for storing uploaded files
└── README.md        # You are here!
```
📌 API Reference
Here is a detailed breakdown of the available API endpoints.
```bash
Welcome Message
GET /

Description: Returns a simple welcome message to confirm the API is running.

Response (200 OK):

JSON

{
  "message": "Welcome to the Notes API"
}

Notes

POST /notes

Description: Creates a new note.

Request Body:

JSON

{
  "title": "My First Note",
  "content": "This is the content of my first note."
}
Response (200 OK): Returns the newly created note with its assigned note_id.

JSON

{
  "note_id": 1,
  "title": "My First Note",
  "content": "This is the content of my first note."
}
GET /notes

Description: Retrieves a list of all notes.

Response (200 OK):

JSON

[
  {
    "note_id": 1,
    "title": "My First Note",
    "content": "This is the content of my first note."
  }
]
GET /notes/{note_id}

Description: Retrieves a single note by its ID.

Response (200 OK):

JSON

{
  "note_id": 1,
  "title": "My First Note",
  "content": "This is the content of my first note."
}
PUT /notes/{note_id}

Description: Updates an existing note by its ID.

Request Body:

JSON

{
  "title": "Updated Note Title",
  "content": "The content has been updated."
}
Response (200 OK):

JSON

{
  "note_id": 1,
  "title": "Updated Note Title",
  "content": "The content has been updated."
}
File Uploads
POST /uploadfile/

Description: Uploads a file. The file is saved to the uploads/ directory.

Request: multipart/form-data
```
Example (curl):

```bash

curl -X POST "[http://127.0.0.1:8000/uploadfile/](http://127.0.0.1:8000/uploadfile/)" -F "file=@/path/to/your/file.txt"
Response (200 OK):

JSON

{
  "filename": "file.txt",
  "content_type": "text/plain"
}
```


⚠️ Limitations & Future Work
This implementation uses a simple in-memory dictionary for data storage. This means all notes will be lost when the server restarts.

Potential future improvements include:

Database Integration: Connect to a persistent database like PostgreSQL or SQLite using an ORM like SQLAlchemy.

User Authentication: Implement OAuth2 to secure endpoints and manage user-specific notes.

Error Handling: Add more robust error handling for edge cases.

Containerization: Add a Dockerfile for easy deployment with Docker.

✨ Acknowledgements
Built with the amazing FastAPI framework.

A big thanks to the vibrant Python open-source community.

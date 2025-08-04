📝 NotesApp API
A simple, high-performance, and asynchronous API for managing notes, built with FastAPI. This project provides a lightweight backend for creating, retrieving, updating, and associating files with notes, using in-memory storage for rapid development and testing.

📋 Table of Contents
✨ Key Features

🏁 Getting Started

Prerequisites

Installation & Setup

Running the Server

📁 Project Structure

📌 API Reference

⚠️ Limitations

📜 License

✨ Key Features
High Performance: Built on FastAPI and Starlette for non-blocking, asynchronous speed.

Automatic Docs: Interactive API documentation with Swagger UI & ReDoc generated automatically.

File Uploads: Seamlessly upload and associate files with your notes.

Lightweight: Uses in-memory storage for rapid prototyping without a database dependency.

🏁 Getting Started
Follow these steps to get the API up and running on your local machine.

Prerequisites
Python 3.8 or newer.

Installation & Setup
Clone the repository:

git clone <your-repository-url>
cd notes-api

Install dependencies:

pip install "fastapi[all]" uvicorn

Running the Server
Launch the development server using Uvicorn. The --reload flag enables hot-reloading for development.

uvicorn main:app --reload

🎉 Your API is now live at http://127.0.0.1:8000. You can access the interactive docs at http://127.0.0.1:8000/docs.

📁 Project Structure
notes-api/
├── main.py          # Main FastAPI application logic and endpoints
├── uploads/         # Default directory for storing uploaded files
└── README.md        # This file

📌 API Reference
GET /
Returns a simple welcome message to confirm the API is running.

Success Response (200 OK):

{
  "message": "Welcome to the Notes API"
}

POST /notes
Creates a new note entry.

Request Body:

{
  "title": "Meeting Agenda",
  "content": "Discuss Q4 roadmap and hiring plan."
}

Success Response (200 OK):

{
  "note_id": 1,
  "title": "Meeting Agenda",
  "content": "Discuss Q4 roadmap and hiring plan."
}

GET /notes
Retrieves a list of all notes currently in memory.

Success Response (200 OK):

[
  {
    "note_id": 1,
    "title": "Meeting Agenda",
    "content": "Discuss Q4 roadmap and hiring plan."
  }
]

GET /notes/{note_id}
Retrieves a specific note by its unique ID.

Success Response (200 OK):

{
  "note_id": 1,
  "title": "Meeting Agenda",
  "content": "Discuss Q4 roadmap and hiring plan."
}

Error Response (404 Not Found):

{
  "detail": "Note not found"
}

PUT /notes/{note_id}
Updates the title and/or content of an existing note.

Request Body:

{
  "title": "Updated Meeting Agenda",
  "content": "Q4 roadmap discussion moved to next week."
}

Success Response (200 OK):

{
  "note_id": 1,
  "title": "Updated Meeting Agenda",
  "content": "Q4 roadmap discussion moved to next week."
}

POST /uploadfile/
Uploads a file to the /uploads/ directory.

Request: multipart/form-data

Example (curl):

curl -X POST "http://127.0.0.1:8000/uploadfile/" -F "file=@/path/to/your/image.png"

Success Response (200 OK):

{
  "filename": "image.png",
  "content_type": "image/png"
}

⚠️ Limitations
This API uses in-memory storage. All data will be lost when the server is restarted. It is intended for development and prototyping, not for production use without modification.

📜 License
This project is licensed under the MIT License.

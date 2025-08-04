<div align="center">

📝
NotesApp API
A simple, high-performance, and asynchronous API for managing notes, built with FastAPI.

</div>

This project provides a lightweight backend for creating, retrieving, updating, and associating files with notes, using in-memory storage for rapid development and testing.

✨ Core Features
Feature

Description

🚀 High Performance

Built on FastAPI and Starlette for non-blocking, asynchronous speed.

📚 Auto-Generated Docs

Interactive API documentation with Swagger UI & ReDoc out of the box.

📁 File Uploads

Seamlessly upload and associate files with your notes.

💡 In-Memory Storage

Perfect for rapid prototyping and development without database setup.

🏁 Getting Started
1. Prerequisites
Python 3.8+

2. Installation
Clone the repository and install the necessary dependencies.

# Clone the repository
git clone <your-repository-url>
cd notes-api

# Install packages
pip install "fastapi[all]" uvicorn

3. Run the Server
Launch the development server with auto-reload enabled.

uvicorn main:app --reload

🎉 Your API is now live at http://127.0.0.1:8000.

📌 API Reference
Click on an endpoint to see more details, including request and response examples.

<details>
<summary><code><b>GET /</b></code> - Welcome Message</summary>

Description: A simple endpoint to confirm the API is running.

Response 200 OK:

{ "message": "Welcome to the Notes API" }

</details>

<details>
<summary><code><b>POST /notes</b></code> - Create a New Note</summary>

Description: Creates a new note entry.

Request Body:

{
  "title": "Meeting Agenda",
  "content": "Discuss Q4 roadmap and hiring plan."
}

Response 200 OK:

{
  "note_id": 1,
  "title": "Meeting Agenda",
  "content": "Discuss Q4 roadmap and hiring plan."
}

</details>

<details>
<summary><code><b>GET /notes</b></code> - Get All Notes</summary>

Description: Retrieves a list of all notes currently in memory.

Response 200 OK:

[
  {
    "note_id": 1,
    "title": "Meeting Agenda",
    "content": "Discuss Q4 roadmap and hiring plan."
  }
]

</details>

<details>
<summary><code><b>GET /notes/{note_id}</b></code> - Get a Single Note</summary>

Description: Retrieves a specific note by its unique ID.

Response 200 OK:

{
  "note_id": 1,
  "title": "Meeting Agenda",
  "content": "Discuss Q4 roadmap and hiring plan."
}

</details>

<details>
<summary><code><b>PUT /notes/{note_id}</b></code> - Update a Note</summary>

Description: Updates the title and/or content of an existing note.

Request Body:

{
  "title": "Updated Meeting Agenda",
  "content": "Q4 roadmap discussion moved to next week."
}

Response 200 OK:

{
  "note_id": 1,
  "title": "Updated Meeting Agenda",
  "content": "Q4 roadmap discussion moved to next week."
}

</details>

<details>
<summary><code><b>POST /uploadfile/</b></code> - Upload a File</summary>

Description: Uploads a file to the /uploads/ directory.

Request: multipart/form-data

Example (curl):

curl -X POST "http://127.0.0.1:8000/uploadfile/" -F "file=@/path/to/your/image.png"

Response 200 OK:

{
  "filename": "image.png",
  "content_type": "image/png"
}

</details>

⚠️ Important Limitation
This API uses in-memory storage. All data will be lost when the server is restarted. It is intended for development and prototyping, not for production use without modification.

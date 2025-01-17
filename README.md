# FableAI

This project is a Flask-based web application that generates short stories using the Groq API. Users can specify a character, setting, and theme to create personalized stories.

---

## Features
- User-friendly interface for entering story parameters.
- Story generation using Groq's AI models.
- Simple REST API endpoint for backend communication.

---

## Prerequisites

Ensure you have the following installed:
- Docker
- Python 3.9 (if running locally)

---

## Getting Started

### Running with Docker

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/projectultra/FableAI.git
   cd FableAI
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t FableAI .
   ```

3. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 FableAI
   ```

4. **Access the Application**:
   Open your browser and navigate to `http://localhost:5000`.

---

### Running Locally

1. **Install Dependencies**:
   Create a virtual environment and install the required dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**:
   Add the following variables to your environment:
   ```bash
   export GROQ_API_KEY=your_api_key
   ```

3. **Run the Application**:
   ```bash
   flask run
   ```

4. **Access the Application**:
   Open your browser and navigate to `http://localhost:5000`.

---

## Project Structure
- `app.py`: Main Flask application.
- `templates/`: HTML templates for the web app.
- `static/`: Static files (CSS, JS).
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Configuration for containerizing the application.

---

## Notes
- Replace `your_api_key` with your Groq API key.
- Make sure Docker is installed and running before building the image.

---

## License
This project is licensed under the MIT License.
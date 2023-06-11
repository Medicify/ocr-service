# OCR Service With Python

This is an OCR (Optical Character Recognition) Service project using Python to receive detected text from images. The OCR server serves as a web service that accepts HTTP POST requests with images and returns the detected text from those images.

## Prerequisites

Before running this project, make sure you have the following prerequisites:

- Python 3.x installed on your system.

## Installation

Install Project
Clone the repository:

```bash
  git clone https://github.com/Medicify/ocr-service.git
```

Import the .sql to mysql database

### Navigate to the project directory:

```bash
 cd ocr-service
```

### Create a virtual environment (optional but recommended):

```bash
 python -m venv venv
```

### Activate the virtual environment:

- On Windows

```bash
 venv\Scripts\activate

```

- On macOS and Linux:

```bash
source venv/bin/activate

```

### Install the project dependencies:

```bash
 pip install -r requirements.txt

```

### Start OCR

```bash
 python main.py

```

The server will run at http://localhost:5050.

Send a POST request to http://localhost:5050/api/ocr

Alternatively, you can use an HTTP client application like Postman to send a POST request to the OCR server.

## Documentation

[Documentation](https://www.python.org/doc/)

## Cloud Computing Team C23-PS135

Bangkit Academy 2023 batch 1

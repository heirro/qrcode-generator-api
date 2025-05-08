# QR Code Generator API with FastAPI

A simple and powerful API for generating customizable QR codes from text or URLs, built with FastAPI.

## Features

- Built with FastAPI - modern, fast Python web framework
- Interactive API documentation with OpenAPI and Swagger UI
- Generate QR codes from any text or URL
- Customize size (S, M, L)
- Adjust margins/borders
- Multiple error correction levels (L, M, Q, H)
- Returns QR code as PNG image
- Asynchronous request handling

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Step 1: Clone the repository

```bash
git clone https://github.com/heirro/qrcode-generator-api.git
cd qrcode-generator-api
```

### Step 2: Set up a virtual environment (optional but recommended)

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install initial dependencies

First, install FastAPI with all standard dependencies and wheel:

```bash
pip install "fastapi[standard]"
pip install wheel
```

### Step 4: Install remaining dependencies

```bash
pip install -r requirements.txt
```

## Running the API

Start the FastAPI server:

```bash
fastapi dev main.py
```

The API will be available at http://localhost:8000/

## API Usage

### Generate a QR Code

```
GET /api/create
```

**Parameters:**

- `data` (required): The text or URL to encode in the QR code
- `size` (optional): QR code size - S (small), M (medium), or L (large)
- `margin` (optional): Border width around the QR code
- `error_level` (optional): Error correction level - L (Low, 7% recovery), M (Medium, 15% recovery), Q (Quartile, 25% recovery), H (High, 30% recovery)

**Example Usage:**

```bash
# Basic QR code for a URL
curl -X GET "http://localhost:8000/api/create?data=https://example.com"

# Customized QR code
curl -X GET "http://localhost:8000/api/create?data=https://example.com&size=L&margin=2&error_level=H"
```

## API Documentation

One of the best features of FastAPI is the automatic interactive documentation:

- Swagger UI documentation: http://localhost:8000/
- Try out API endpoints directly from your browser
- Explore all available parameters and options

## Deployment

FastAPI applications can be easily deployed:

```bash
# Production server
fastapi run main:app --host 0.0.0.0 --port 8000
```

## Live Server
Demo: [https://qrcode.heirro.dev/api/create]('https://qrcode.heirro.dev/api/create')

## License

MIT 
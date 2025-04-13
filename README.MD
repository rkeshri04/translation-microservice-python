# Translation Microservice

This is a simple translation microservice built using the Quart framework and Google Translate API. It provides an endpoint to translate text from one language to another.

## Features
- Translate text from a source language to a destination language.
- Auto-detect the source language if not specified.
- Specify the destination language via request headers.

## Requirements
- Python 3.7+
- Quart
- googletrans

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd translation
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install quart googletrans==4.0.0-rc1
   ```

## Usage

1. Start the server:
   ```bash
   python main.py
   ```

   The server will run on `http://127.0.0.1:8002` by default.

2. Make a POST request to the `/translate` endpoint with the following JSON payload:
   ```json
   {
       "text": "Hello, world!",
       "src": "en"  // Optional: Source language (default is auto-detect)
   }
   ```

   Include the `Destination-Language` header to specify the target language (default is English):
   ```
   Destination-Language: es
   ```

3. Example response:
   ```json
   {
       "text": "¡Hola, mundo!"
   }
   ```

## Error Handling
- If the `text` field is missing in the request, the server will return:
  ```json
  {
      "error": "Text to translate is required"
  }
  ```
- If an error occurs during translation, the server will return:
  ```json
  {
      "error": "<error-message>"
  }
  ```

## License
This project is licensed under the MIT License.
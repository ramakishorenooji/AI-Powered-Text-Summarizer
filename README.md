# AI-Powered-Text-Summarizer

Initial Draft : Tech Stack: Python, Hugging Face Transformers, FastAPI (Work in progress)

# AI-Powered-Text-Summarizer

## Overview

This project is an AI-powered text summarizer that leverages the power of Hugging Face Transformers and FastAPI to provide a simple and efficient way to summarize text. The summarizer takes a block of text as input and returns a concise summary.

## Tech Stack

- Python
- Hugging Face Transformers
- FastAPI

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ramakishorenooji/AI-Powered-Text-Summarizer.git
   cd AI-Powered-Text-Summarizer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

To start the FastAPI server, run the following command:
`bash
    uvicorn main:app --reload
    `

### Usage

Once the server is running, you can access the API documentation by navigating to `http://127.0.0.1:8000/docs` in your web browser. This will provide you with an interactive interface to test the summarization endpoint.

### Example Request

To summarize a block of text, you can send a POST request to the `/summarize` endpoint with the following JSON payload:
`json
    {
        "text": "Your text to be summarized goes here."
    }
    `

### Example Response

The response will contain the summarized text in the following format:
`json
    {
        "summary": "The summarized text will be here."
    }
    `

### Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

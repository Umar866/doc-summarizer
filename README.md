# Document Summarizer

A Python script that summarizes a text file into one paragraph and five key points, using the Gemini API.

## Setup

1. Install Python 3.11 or newer.
2. Create and activate a virtual environment:
   python -m venv .venv
   .venv\Scripts\Activate.ps1
3. Install the packages: pip install -r requirements.txt
4. Get a free API key from Google AI Studio.
5. Create a file named `.env` containing: GEMINI_API_KEY=your-key

## Usage

python summarize.py yourfile.txt

## Current limits

- Works on plain text files only.
- Very long documents are not handled yet.

## Planned

- PDF support
- Splitting long documents into chunks
- A simple web page for uploading files
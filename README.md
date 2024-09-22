# Document Summarization Tool

A Python-based tool for extracting and summarizing text from various document formats, including DOCX, PDF, and images. This project leverages NLP techniques to provide concise summaries, making it easier to digest large amounts of information quickly.

## Features

- Extracts text from DOCX, PDF, and image files (JPG, PNG, BMP).
- Summarizes text using state-of-the-art NLP models.
- Processes documents in parallel for faster performance.
- Supports text lemmatization and stop word removal to enhance summary quality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
2. cd your-repo
3. pip install -r requirements.txt

## Usage
To summarize documents in a folder, run:
python summarize.py path/to/documents
Replace path/to/documents with the actual path to your folder containing the documents.

## Contributing
Fork the project.
Create your feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

## Acknowledgements
Thank you to nltk for the Natural Language Toolkit.
Thanks to Hugging Face for the Transformers library.
Special thanks to pdfminer for PDF text extraction.
Acknowledgments to pytesseract for OCR capabilities.
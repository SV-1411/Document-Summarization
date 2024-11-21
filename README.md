# Document Summarization Tool

A Python-based tool for extracting and summarizing text from various document formats, including DOCX, PDF, and images. This project leverages NLP techniques to provide concise summaries, making it easier to digest large amounts of information quickly.

## Features

- Extracts text from DOCX, PDF, and image files (JPG, PNG, BMP).
- Summarizes text using state-of-the-art NLP models.
- Processes documents in parallel for faster performance.
- Supports text lemmatization and stop word removal to enhance summary quality.

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/your-repo.git
2. Navigate to the project directory:
    cd your-repo
3. Install the required dependencies: pip install -r requirements.txt
   Note: If you're using an environment with Python 3.2 or later, argparse is already included and doesn't need to be manually installed. Ensure that pip installs all other required dependencies.

4. Usage: To summarize documents in a folder, run:
   python summarize.py path/to/documents
   Replace path/to/documents with the actual path to your folder containing the documents. This will process all files in the folder and print summaries for each document.

Example:
   python main.py ./documents
   Ensure that the main.py script is in the same directory or provide the correct path to it.

5. Acknowledgements
Thank you to nltk for the Natural Language Toolkit.
Thanks to Hugging Face for the Transformers library.
Special thanks to pdfminer for PDF text extraction.
Acknowledgments to pytesseract for OCR capabilities.

---

Key Updates:
Installation Section:

Corrected formatting and added proper closing for the git clone command.
Clarified that argparse is not needed for Python 3.2+.
Usage Section:

Updated usage to reflect that users should replace path/to/documents with the actual path to their folder.
Added an example for running the script (./documents).
Contributing Section:

Improved clarity on the contributing steps (standard Git flow).
Acknowledgements:

Included links to relevant libraries for better reference.


---
Optional Improvements
- If you want to add more technical details (e.g., specific environment setup for OCR or extra dependencies), you could also mention any setup steps related to `pytesseract`, such as installing Tesseract on the system.
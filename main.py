import os
from src.text_extraction import extract_text_from_file
from src.text_processing import process_text
from src.summarization import summarize_text
import multiprocessing

def summarize_document(document_path):
    try:
        text = extract_text_from_file(document_path)
        processed_text = process_text(text)
        summary = summarize_text(processed_text)
        return summary
    except Exception as e:
        return f"Error processing {document_path}: {e}"

def summarize_documents_in_folder(folder_path):
    summaries = {}
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(summarize_document, [os.path.join(folder_path, filename) for filename in os.listdir(folder_path)])
    
    for i, filename in enumerate(os.listdir(folder_path)):
        summaries[filename] = results[i]
    
    return summaries

if __name__ == "__main__":
    folder_path = "path/to/your/folder"
    summaries = summarize_documents_in_folder(folder_path)
    for filename, summary in summaries.items():
        print(f"Summary for {filename}: {summary}")

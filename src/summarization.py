from transformers import pipeline
from nltk.tokenize import sent_tokenize

summarizer = pipeline('summarization', model="sshleifer/distilbart-cnn-12-6")

def split_text_into_chunks(text, max_chunk_size=500):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0
    
    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length > max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(sentence)
        current_length += sentence_length
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def summarize_text(text):
    chunks = split_text_into_chunks(text)
    summarized_chunks = []
    
    for chunk in chunks:
        if len(chunk.split()) > 50:
            summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
            summarized_chunks.append(summary)
    
    return ' '.join(summarized_chunks)

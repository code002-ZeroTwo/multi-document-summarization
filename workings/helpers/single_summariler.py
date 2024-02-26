# Load model directly
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/pegasus-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-large")

"""
def generate_summary(document):
    document = document[:1000]
    summarizer = pipeline(model=model, tokenizer=tokenizer, task="summarization")
    summary = summarizer(document)
    return summary
"""

def generate_summary(document):
    # Tokenize the document
    tokens = tokenizer(document, max_length=1024, truncation=True, return_tensors="pt")

    # Get the truncated text
    truncated_text = tokenizer.decode(tokens["input_ids"][0], skip_special_tokens=True)

    summarizer = pipeline(model=model, tokenizer=tokenizer, task="summarization")
    summary = summarizer(truncated_text)
    return summary
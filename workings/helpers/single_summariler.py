# Load model directly
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/pegasus-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-large")

def generate_summary(document):
    summarizer = pipeline(model=model, tokenizer=tokenizer, task="summarization")
    summary = summarizer(document)
    return summary
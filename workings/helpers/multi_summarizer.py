from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "/home/sid/Documents/code/fyp/finalyear1/workings/ml_models/bart-large-A"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_summary(document):
    summarizer = pipeline(model=model_name, tokenizer=tokenizer, task="summarization")
    summary = summarizer(document)
    return summary

from transformers import pipeline, PegasusTokenizer, PegasusForConditionalGeneration

model_path = "/home/sid/Documents/code/fyp/finalyear1/workings/ml_models/finetuned-cnndailymail"

tokenizer = PegasusTokenizer.from_pretrained(model_path)
model = PegasusForConditionalGeneration.from_pretrained(model_path)

max_sequence = 1000

def truncate_document(document, max_sequence):
    if len(document) > max_sequence:
        return document[:max_sequence]
    else:
        return document

def generate_summary(document):

    truncated_document = truncate_document(document, max_sequence)

    summarizer = pipeline(model=model, tokenizer=tokenizer, task="summarization")
    summary = summarizer(truncated_document)
    return summary
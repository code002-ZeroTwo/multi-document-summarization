import spacy

# Load spaCy's English NER model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(title):
    # Process the title using spaCy
    doc = nlp(title)

    # Extract relevant entities (persons, organizations, locations)
    relevant_entities = [entity.text for entity in doc.ents
                         if entity.label_ in ['PERSON', 'ORG', 'LOC']]

    important_tokens = [token.text for token in doc
                        if token.pos_ in ['NOUN','PROPN'] and token.pos_ != 'VERB']
                        

    if len(relevant_entities) > 1:
        combined_keywords = relevant_entities 

    else: 
        combined_keywords = important_tokens 

    # only send 3 keywords
    if len(combined_keywords) > 3:
        combined_keywords = combined_keywords[:3]


    # Remove duplicates
    combined_keywords = list(set(combined_keywords))

    return combined_keywords

    # Print or use the relevant entities as keywords


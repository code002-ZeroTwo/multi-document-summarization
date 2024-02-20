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
                        

    combined_keywords = relevant_entities + important_tokens

    # Remove duplicates
    combined_keywords = list(set(combined_keywords))

    combined_keywords = combined_keywords[:3]

    return combined_keywords

    # Print or use the relevant entities as keywords


# List of titles
""" titles = [
    'Tel Aviv protesters call on Netanyahu to resign',
    'Julius Nyerere: Former Tanzanian leader honoured by African Union statue',
    'Israel sets March deadline for Gaza ground offensive in Rafah',
    'At least 55 dead in ambush in remote PNG Highland region',
    "Oppenheimer's Cillian Murphy and Robert Downey Jr scoop Bafta Film Awards",
    'The US will relax pollution-limiting rules for vehicle emissions',
    "Brazil's Lula compares Israel's Gaza campaign to the Holocaust",
    'Gaza doctors: ‘We leave patients to scream for hours and hours’',
    'Apple to be fined over $500 million under EU antitrust law',
    'Alexei Navalny: US and UK ambassadors to Russia lay tributes',
    'Why all your notes and files should be plain text',
    "'Zombie Fires' burning at an alarming rate in Canada",
    'Ridge Alkonis: The sailor who stoked Japanese resentment against the US',
    'The Verge',
    'The DICE Awards show is the celebration developers and fans deserve',
    'I printed chocolate on a 3D printer and ate it',
    'Figma’s CEO on moving on after failed Adobe merger',
    'The shine comes off the Vision Pro',
    'With the rise of AI, web crawlers are suddenly controversial',
    'AI at Work'
]
"""

from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize

# Function to calculate cosine similarity between two vectors
def calculate_cosine_similarity(vec1, vec2):
    # return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0, 0]
    return cosine_similarity([vec1.mean(axis=0)], [vec2.mean(axis=0)])[0, 0]


def similarity(title, content):
    # Tokenize the title and document
    tokenized_title = word_tokenize(title.lower())
    tokenized_content = word_tokenize(content.lower())

    # Create Word2Vec model
    model = Word2Vec([tokenized_title, tokenized_content], min_count=1, workers=4)
    
    # Get vectors for title and document
    title_vector = model.wv[tokenized_title]
    document_vector = model.wv[tokenized_content]

    # Calculate cosine similarity
    similarity_score = calculate_cosine_similarity(title_vector, document_vector)
    print(similarity_score)

    return similarity_score

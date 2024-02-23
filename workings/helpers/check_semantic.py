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
    if similarity_score > 0.2:
        return True

    return False

title = "Leaked Files Show the Secret World of China’s Hackers for Hire"
content = """
China has increasingly turned to private companies in campaigns to hack foreign governments and control its domestic population.

The hackers offered a menu of services, at a variety of prices.

A local government in southwest China paid less than $15,000 for access to the private website of traffic police in Vietnam. Software that helped run disinformation campaigns and hack accounts on X cost $100,000. For $278,000 Chinese customers could get a trove of personal information behind social media accounts on platforms like Telegram and Facebook.

The offerings, detailed in leaked documents, were a portion of the hacking tools and data caches sold by a Chinese security firm called I-Soon, one of the hundreds of enterprising companies that support China’s aggressive state-sponsored hacking efforts. The work is part of a campaign to break into the websites of foreign governments and telecommunications firms.

The materials, which were posted to a public website last week, revealed an eight-year effort to target databases and tap communications in South Korea, Taiwan, Hong Kong, Malaysia, India and elsewhere in Asia. The files also showed a campaign to closely monitor the activities of ethnic minorities in China and online gambling companies.

The data included records of apparent correspondence between employees, lists of targets, and material showing off cyberattack tools. Three cybersecurity experts interviewed by The Times said the documents appeared to be authentic.

Taken together, the files offered a rare look inside the secretive world of China’s state-backed hackers for hire. They illustrated how Chinese law enforcement and its premier spy agency, the Ministry of State Security, have reached beyond their own ranks to tap private-sector talent in a hacking campaign that United States officials say has targeted American companies and government agencies.

“We have every reason to believe this is the authentic data of a contractor supporting global and domestic cyberespionage operations out of China,” said John Hultquist, the chief analyst at Google’s Mandiant Intelligence.

Mr. Hultquist said the leak revealed that I-Soon was working for a range of Chinese government entities that sponsor hacking, including the Ministry of State Security, the People’s Liberation Army and China’s national police. At times the firm’s employees focused on overseas targets. In other cases they helped China’s feared Ministry of Public Security surveil Chinese citizens domestically and overseas.

"""

# print(similarity(title,content))
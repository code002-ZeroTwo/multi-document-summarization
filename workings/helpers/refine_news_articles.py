import requests
from bs4 import BeautifulSoup
from readability import Document
import re
from newsplease import NewsPlease
from . import check_semantic
# import check_semantic

def extract_article_content(article_url):
    """
    Extract article content from the provided article URL.

    Parameters:
    - article_url (str): URL of the article.

    Returns:
    - str: Extracted article content.
    """
    article_response = requests.get(article_url)
    article_html = article_response.text

    doc = Document(article_html)
    return doc.summary()

def remove_redundant_spaces(document):
    # Replace multiple spaces with a single space
    cleaned_document = re.sub(r'\s+', ' ', document)
    
    # Remove leading and trailing spaces
    cleaned_document = cleaned_document.strip()

    # check if article is ad or not
    # if(is_ad(cleaned_document)):
        # cleaned_document = "ad"

    return cleaned_document

def get_top_articles(all_articles,query, top_articles_count=5):
    news = {}
    if 'articles' in all_articles:
        # top_articles_content = []
        for result in all_articles['articles'][:top_articles_count]:

            # article_content = extract_article_content(result['url'])
            to_print = NewsPlease.from_url(result['url'])
            
            related = check_semantic.similarity(query, result['title'])

            if(related == False):
                continue

            try:
                article_with_removed_spaces = remove_redundant_spaces(to_print.maintext)
                related = check_semantic.similarity(result['title'], article_with_removed_spaces)

                if(related):
                    news[result['title']] = article_with_removed_spaces

            except AttributeError:
                print("no articles found")

        return news
    else:
        return "No articles found in the search results."

# given a title retrive titles and do similarities check



def get_titles(all_articles):
    titles = []
    if 'articles' in all_articles:
        for result in all_articles['articles']:
            titles.append(result['title'])
    return titles

def is_ad(document):
    ad_patterns = [
        r'\b(?:advertisement|ad|sponsored|promoted)\b',
        r'\b(?:subscribe|signup|sign up|buy now|limited time offer)\b',
        r'\b(?:exclusive offer|click now|call now)\b',
        r'\b(?:special promotion|act fast|order now)\b',
        r'\b(?:limited stock|money back guarantee|double your|earn money)\b',
        r'\b(?:free trial|no strings attached|new and improved|get started today)\b',
        r'\b(?:make money|lowest price|best price)\b',
        """
        r'\b(?:limited stock|new and improved|get started today)\b',
        r'\b(?:make money online|lowest price ever|amazing offer)\b',
        r'\b(?:once in a lifetime|bonus|cash|win)\b' """
    ]

    # Check if any ad patterns match the document content
    for pattern in ad_patterns:
        if re.search(pattern, document, flags=re.IGNORECASE):
            return True

    return False 

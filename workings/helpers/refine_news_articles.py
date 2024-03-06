import requests
from readability import Document
import re
from newsplease import NewsPlease
from goose3 import Goose
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

def get_top_articles_(all_articles,title_data,all_articles_des,description_data):
    news = {}
    if 'articles' in all_articles:
        # top_articles_content = []
        for result in all_articles['articles'][:20]:
            try:
                to_print = NewsPlease.from_url(result['url'])
                g = Goose()
                container = g.extract(url=result['url'])


                print(result['title'])
                print("similarity between title")
                related = max(check_semantic.similarity(title_data, result['title']),check_semantic.similarity(title_data, result['description']))

                if(related < 0.35):
                    continue
                else:
                    print(to_print.title)
                    print(to_print.maintext)


                try:
                    article_with_removed_spaces_g = remove_redundant_spaces(container.cleaned_text)
                    article_with_removed_spaces_n = remove_redundant_spaces(to_print.maintext)
                    news_related = check_semantic.similarity(title_data,article_with_removed_spaces_n)
                    goose_related = check_semantic.similarity(title_data, article_with_removed_spaces_g)

                    if(news_related > goose_related):
                        article_with_removed_spaces = article_with_removed_spaces_n
                    elif(goose_related > news_related):
                        article_with_removed_spaces = article_with_removed_spaces_g

                    if(len(news) < 3):
                        if(related > 0.2):
                            news[result['title']] = (article_with_removed_spaces,related)
                    else:
                        min_related_key = min(news, key=lambda x: news[x][1])
                        if(news[min_related_key][1] < related):
                            del news[min_related_key]
                            news[result['title']] = (article_with_removed_spaces,related)

                except AttributeError:
                    print("no articles found")
            
            except Exception as e:
                print(f"errror processing article: {str(e)}")
        # before returning news dictionary removed related value from the dictionary
        new_news = {key: value[0] for key,value in news.items()}
        print(new_news)
        return new_news
    else:
        return "No articles found in the search results."

def get_top_articles(all_articles, title_data, all_articles_des, description_data):
    news = {}

    def process_result(result):
        try:
            to_print = NewsPlease.from_url(result['url'])
            g = Goose()
            container = g.extract(url=result['url'])

            print(result['title'])
            print("similarity between title")

            related = max(
                check_semantic.similarity(title_data, result['title']),
                check_semantic.similarity(description_data, result['description']),
                check_semantic.similarity(title_data, result['description']),
                check_semantic.similarity(description_data, result['title'])
            )

            if related < 0.35:
                return  # Skip if similarity is too low

            print(to_print.title)
            print(to_print.maintext)

            try:
                article_with_removed_spaces_g = remove_redundant_spaces(container.cleaned_text)
                article_with_removed_spaces_n = remove_redundant_spaces(to_print.maintext)

                news_related = check_semantic.similarity(title_data, article_with_removed_spaces_n)
                goose_related = check_semantic.similarity(title_data, article_with_removed_spaces_g)

                if(news_related > goose_related):
                    article_with_removed_spaces = article_with_removed_spaces_n
                    related = news_related
                elif(goose_related > news_related):
                    article_with_removed_spaces = article_with_removed_spaces_g
                    related = goose_related

                if len(news) < 3:
                    if related > 0.2:
                        news[result['title']] = (article_with_removed_spaces, related)
                else:
                    min_related_key = min(news, key=lambda x: news[x][1])
                    if news[min_related_key][1] < related:
                        del news[min_related_key]
                        news[result['title']] = (article_with_removed_spaces, related)

            except AttributeError:
                print("no articles found")

        except Exception as e:
            print(f"error processing article: {str(e)}")

    if 'articles' in all_articles:
        for result in all_articles['articles'][:10]:
            process_result(result)

    if 'articles' in all_articles_des:
        for result in all_articles_des['articles'][:10]:
            process_result(result)

    # before returning news dictionary removed related value from the dictionary
    new_news = {key: value[0] for key, value in news.items()}
    print(new_news)
    return new_news


def get_titles(all_articles):
    titles = []
    if 'articles' in all_articles:
        for result in all_articles['articles']:
            titles.append((result['title'],result['description']))
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

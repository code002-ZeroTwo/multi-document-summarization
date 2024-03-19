import requests
from goose3 import Goose
from workings.models import News
from . import refine_news_articles

def get_news_archive(search_query, language='en'):
    api_url = f"https://newsdata.io/api/1/news"
    params = {
        "apikey": "pub_37437952f8b03214af008a425d28c7448e062",
        "q": search_query,
        "language": language,
        "country": "np"
    }

    try:
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the API returns JSON data
            data = response.json()
            return data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# save news content to news model

def save_news_to_db(response):
    print(response)
    if 'status' in response and response['status'] == 'success':
        total_results = response.get('totalResults', 0)
        print(f"Total Results: {total_results}\n")
        g = Goose()

        if 'results' in response and isinstance(response['results'], list):
            for index, article in enumerate(response['results'], start=1):
                title = article.get('title', 'N/A')
                description = article.get('description', 'N/A')
                url = article.get('link', 'N/A')
                publishedAt = article.get('pubDate', 'N/A')
                main_content = g.extract(url=article.get('link', 'N/A'))
                content = refine_news_articles.remove_redundant_spaces(main_content.cleaned_text)
                category = article.get('category', 'N/A')

                news = News(title=title, description=description, url=url, publishedAt=publishedAt, content=content, category=category)
                news.save()
        else:
            print("No results found in the response.")
    else:
        print("Error in the response.")


categories = [
    "top",
    "sports",
    "technology",
    "business",
    "entertainment",
    "health",
    "world",
    "politics",
    "enviorment",
    "food"
]

import requests
from goose3 import Goose
api_key = "pub_37437952f8b03214af008a425d28c7448e062"

def get_news_archive(api_key,  search_query, language='en'):
    api_url = f"https://newsdata.io/api/1/news"
    params = {
        "apikey": api_key,
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


def present_news_response(response):
    if 'status' in response and response['status'] == 'success':
        total_results = response.get('totalResults', 0)
        print(f"Total Results: {total_results}\n")
        g = Goose()

        if 'results' in response and isinstance(response['results'], list):
            for index, article in enumerate(response['results'], start=1):
                print(f"Article {index}:")
                print(f"Title: {article.get('title', 'N/A')}")
                print(f"Link: {article.get('link', 'N/A')}")
                main_content = g.extract(url=article.get('link', 'N/A'))
                print(f"main content: {main_content.cleaned_text}")
                print(f"Keywords: {article.get('keywords', 'N/A')}")
                print(f"Createor: {article.get('creator', 'N/A')}")
                print(f"Description: {article.get('description', 'N/A')}")
                print(f"Publication Date: {article.get('pubDate', 'N/A')}")
                print(f"Image URL: {article.get('image_url', 'N/A')}")
                print(f"Source: {article.get('source_id', 'N/A')}")
                print(f"Country: {', '.join(article.get('country', []))}")
                print(f"Category: {', '.join(article.get('category', []))}")
                print(f"Language: {article.get('language', 'N/A')}")
                print(f"Sentiment: {article.get('sentiment', 'N/A')}")
                print("\n" + "-"*30 + "\n")

        else:
            print("No results found.")
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

search_query = "politics"

result = get_news_archive(api_key,  search_query)

if result: 
    present_news_response(result)

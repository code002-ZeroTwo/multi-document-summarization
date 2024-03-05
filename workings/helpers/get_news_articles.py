from newsapi import NewsApiClient
from datetime import datetime 
from . import refine_news_articles
# import refine_news_articles

newsapi = NewsApiClient(api_key='76dbb358a26f4a649a247e98095f7d1c')
def get_news(query,title_data, date=None):
    all_articles = newsapi.get_everything(q=query,
                                          #domains='bbc.co.uk,techcrunch.com',
                                          #from_param=date,
                                          to=datetime.now().strftime('%Y-%m-%d'),
                                          language='en',
                                          sort_by='relevancy')

    print(all_articles) 
    return refine_news_articles.get_top_articles(all_articles,title_data)

## need to add more features 
    
def get_top_news(query = ''):
    top_headlines = newsapi.get_top_headlines(q=query,
                                          #sources='bbc-news,cnn',
                                          language='en',
                                          )
    titles = refine_news_articles.get_titles(top_headlines)
    return titles

# print(get_news("Garmin Forerunner OLED"))
# print(get_top_news("apple"))
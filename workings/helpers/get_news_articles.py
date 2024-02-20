from newsapi import NewsApiClient
from datetime import datetime 
from . import refine_news_articles

newsapi = NewsApiClient(api_key='76dbb358a26f4a649a247e98095f7d1c')
def get_news(query, date=None):
    all_articles = newsapi.get_everything(q=query,
                                          #domains='bbc.co.uk,techcrunch.com',
                                          # from_param=date,
                                          to=datetime.now().strftime('%Y-%m-%d'),
                                          language='en',
                                          sort_by='relevancy')
    
    return refine_news_articles.get_top_articles(all_articles)

## need to add more features 
    
def get_top_news():
    top_headlines = newsapi.get_top_headlines(q="",
                                          sources='bbc-news,the-verge',
                                          language='en',
                                          )
    titles = refine_news_articles.get_titles(top_headlines)
    return titles

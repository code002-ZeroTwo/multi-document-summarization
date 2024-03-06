from newsapi import NewsApiClient
from datetime import datetime 
from . import refine_news_articles
# import refine_news_articles

newsapi = NewsApiClient(api_key='76dbb358a26f4a649a247e98095f7d1c')
def get_news(query,title_data,des_query,description_data, date=None):
    all_articles = newsapi.get_everything(q=query,
                                          # domains='bbc.co.uk,cnn.com,reuters.com',
                                          # sources='bbc-news,cnn.com,reuters.com,washingtonpost.com,nytimes.com,wsj.com',
                                          #from_param=date,
                                          to=datetime.now().strftime('%Y-%m-%d'),
                                          language='en',
                                          sort_by='relevancy')


    all_articles_des = newsapi.get_everything(q=des_query,
                                          to=datetime.now().strftime('%Y-%m-%d'),
                                          language='en',
                                          sort_by='relevancy')

    print(all_articles) 
    return refine_news_articles.get_top_articles(all_articles,title_data,all_articles_des,description_data)

## need to add more features 
    
def get_top_news(query = '',category = 'general'):
    top_headlines = newsapi.get_top_headlines(q=query,
                                          sources='bbc-news,cnn.com,reuters.com,washingtonpost.com,nytimes.com,wsj.com',

                                          # category=category,
                                          language='en',
                                          )
    titles_and_descriptions = refine_news_articles.get_titles(top_headlines)
    return titles_and_descriptions

# print(get_news("Garmin Forerunner OLED"))
# print(get_top_news("apple"))
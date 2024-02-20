from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from finalyear1.workings.helpers.get_news_articles import get_top_news, get_news 
from finalyear1.workings.helpers import single_summariler, multi_summarizer,extract_keywords

class TitleView(APIView):
    def get(self, request) :
        titles = get_top_news()
        return Response({
            "titles" : titles
        })

class ContentView(APIView):
    def post(self, request) :
        title_data = request.data["title"]
        # get keywords from title
        keywords = extract_keywords.extract_keywords(title_data)
        # get news articles related to keywords
        news_articles = get_news(keywords)

        # summarize each news articles and put in a list
        summaries = []

        for key, value in news_articles.items() :
            summary = single_summariler.generate_summary(value)
            summaries.append(summary)

        # generate summary of list of news articles

        # append list of summary to a single document seperated by |||||

        for summary in summaries :
            document = document + "||||" + summary
        
        # generate summary of document
            summary = multi_summarizer.generate_summary(document)
        

        return Response({
            "summary" : summary
        })
    

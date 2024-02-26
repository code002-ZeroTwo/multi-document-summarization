from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from workings.helpers.get_news_articles import get_top_news, get_news 
from workings.helpers import single_summariler, multi_summarizer,extract_keywords
import textwrap

class TitleView(APIView):
    def get(self, request) :
        titles = get_top_news()
        return Response({
            "titles" : titles
        })

class ContentView(APIView):
    def post(self, request) :

        try:

            title_data = request.data["title"]
            # get keywords from title
            keywords = extract_keywords.extract_keywords(str(title_data))
            # get news articles related to keywords
            # convert the keywords of list to string
            keywords_string = " ".join(keywords)
            print(f"this is keywords string {keywords_string}" )
            news_articles = get_news(keywords_string)

            print('\n')
            print(news_articles)

            # summarize each news articles and put in a list
            summaries = []

            for key, value in news_articles.items():
                summary = single_summariler.generate_summary(value)
                summaries.append(summary)

            print("list of summaries: ")
            print('\n')
            print(summaries)

            # generate summary of list of news articles


            # append list of summary to a single document seperated by |||||

            for summary in summaries :
                try: 
                    document = document + "|||||" + summary[0]['summary_text']
                except UnboundLocalError:
                    document = summary[0]['summary_text']
            
            # generate summary of document
            try:
                final_summary = multi_summarizer.generate_summary(document)
            except:
                return Response("could not generate summary")

            print(final_summary)        

            return Response(final_summary)
        
        except:
            return Response("could not generate summary")
        
class SearchView(APIView):
    def post(self, request) :
        query = request.data["query"]
        titles = get_top_news(query)
        return Response(titles)
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
            description_data = request.data["description"]
            if "-" in title_data:
                title_data = title_data.split(" - ")[0].strip()
            keywords = extract_keywords.extract_keywords(str(title_data))
            description_keywords = extract_keywords.extract_keywords(str(description_data))
            keywords_string = " ".join(keywords)
            description_keywords_string = " ".join(description_keywords)
            news_articles = get_news(keywords_string,title_data,description_keywords_string,description_data)

            # summarize each news articles and put in a list
            summaries = []
            append_sepertly = []
            for key, value in news_articles.items():
                if(len(value) < 200):
                    append_sepertly.append(value)
                    continue
                summary = single_summariler.generate_summary(value)
                summaries.append(summary)

            print("list of summaries: ")
            print('\n')
            print(summaries)

            if(len(summaries) == 1):
                return Response(summaries[0])

            for summary in summaries :
                try: 
                    document = document + "|||||" + summary[0]['summary_text'] 
                except UnboundLocalError:
                    document = summary[0]['summary_text']

            if(len(append_sepertly) > 0):
                for doc in append_sepertly:
                    document += "|||||" + doc
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
        try:
            category = request.data["category"]
        except KeyError:
            category = "general"
        titles = get_top_news(query,category)
        return Response(titles)
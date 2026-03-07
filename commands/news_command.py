from Tools.news import get_global_news

class NewsCommand:

    def execute(self, text):

        return get_global_news()
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_global_news():

    api_key = os.getenv("NEWSAPI_KEY")

    if not api_key:
        return "News API key not found."

    url = f"https://newsapi.org/v2/top-headlines?language=en&pageSize=5&apiKey={api_key}"

    try:
        data = requests.get(url).json()

        if data.get("status") == "ok":

            headlines = []

            for article in data["articles"][:5]:
                headlines.append(article["title"])

            return "Here are the top news headlines. " + " . ".join(headlines)

        else:
            return "Unable to fetch news."

    except Exception as e:
        print(e)
        return "News service error."
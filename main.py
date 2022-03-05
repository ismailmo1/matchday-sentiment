import os

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get("AZURE_KEY")
endpoint = os.environ.get("AZURE_ENDPOINT")


# Authenticate the client using your key and endpoint
def authenticate_client(key, endpoint):
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential
    )
    return text_analytics_client


def main():
    client = authenticate_client(key, endpoint)

    doc = ["Mane is the beat"]
    res = client.analyze_sentiment(doc, show_opinion_mining=True)

    print(res)


if __name__ == "__main__":
    main()

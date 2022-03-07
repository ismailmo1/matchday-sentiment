import os

from dotenv import load_dotenv

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

azure_key = os.environ.get("AZURE_KEY")
azure_endpoint = os.environ.get("AZURE_ENDPOINT")


# Authenticate the client using your key and endpoint
def authenticate_client(
    key: str = azure_key, endpoint: str = azure_endpoint
) -> TextAnalyticsClient:
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential
    )
    return text_analytics_client


# res = client.analyze_sentiment(doc[:10], show_opinion_mining=True)

# print(res)

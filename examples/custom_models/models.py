import vertexai
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv
import os 

load_dotenv()
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
vertexai.init(project=PROJECT_ID, location="us-central1")

class ModelClass:
    def __init__(self, model_name):
        """
        Initialize the ModelClass for Gemini models.
        :param model_name: The name of the Gemini model to use.
        :param max_tokens: Maximum number of tokens for output.
        :param kwargs: Additional keyword arguments for model configuration.
        """
        self.model_name = model_name
        self.max_tokens = 1000
        # Initialize the model with the provided model name
        self.model = GenerativeModel(model_name)

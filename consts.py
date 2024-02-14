import os

MESSAGE_TO_GPT = """
    Hey, what's the best temperature for an attraction of the category {attraction},
    answer only the number of the temperature in Celsius, only one number! not between numbers.
    don't answer me with explanations! I want a response in length of 1-3 with the temperature number only! 
    """

GPT_ENDPOINT = "https://api.openai.com/v1/chat/completions"
GPT_API_KEY = os.getenv("GPT_API_KEY", "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")

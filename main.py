import os
from dotenv import load_dotenv
from exa_py import Exa

load_dotenv()

exa_api_key = os.getenv("EXA_API_KEY")
exa = Exa(exa_api_key)

search = input("Search here:")

response = exa.search(
    search,
    num_results=10,
    type="keyword",
    include_domains=["www.react.dev"],
    use_autoprompt=False,
)

print(response)

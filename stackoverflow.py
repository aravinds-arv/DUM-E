import os
from dotenv import load_dotenv
from stackapi import StackAPI

load_dotenv()
API_KEY = os.getenv("STACK_API_KEY")

site = StackAPI("stackoverflow", key=API_KEY)
site.page_size = 5
site.max_pages = 1

def fetch_res(query:str):
    responses = site.fetch("search/excerpts", q=query, filter="!nKzQURF6Y5", sort='votes')
    print(f"Quota Max: {responses['quota_max']}", f"Quota Remaining: {responses['quota_remaining']}")
    res_list = []
    for response in responses['items']:
        if response['item_type'] == 'question' or response['item_type'] == 'answer':
            question = {}
            title = f"{response['title']}"
            url = f"https://stackoverflow.com/q/{response['question_id']}"
            question['title'] = title
            question['url'] = url
            res_list.append(question)
        else: 
            pass
    return res_list
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def extract_question(html):
    soup = BeautifulSoup(html, "lxml")
    text = soup.get_text(" ")
    submit_script = re.search(r'https.*?submit.*?"', html)
    submit_url = submit_script.group(0).strip('"')
    return text, submit_url

def parse_and_solve(text):
    if "sum" in text.lower():
        numbers = [int(n) for n in re.findall(r"\d+", text)]
        return sum(numbers)
    return "unknown"

def submit_answer(payload, submit_url, answer):
    payload["answer"] = answer
    r = requests.post(submit_url, json=payload)
    return r.json()

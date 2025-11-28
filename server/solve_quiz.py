from server.browser import fetch_page
from server.utils import extract_question, parse_and_solve, submit_answer

async def solve_quiz(payload):
    url = payload["url"]

    html = await fetch_page(url)
    question, submit_url = extract_question(html)

    answer = parse_and_solve(question)
    response = submit_answer(payload, submit_url, answer)

    if response.get("url"):
        payload["url"] = response["url"]
        return await solve_quiz(payload)

    return response

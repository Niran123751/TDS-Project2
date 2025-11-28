# LLM Quiz Solver

This project automatically solves multi-step quiz tasks involving scraping, data analysis and answer submission.

## Run locally
pip install -r requirements.txt
cp .env.example .env
uvicorn server.main:app --host 0.0.0.0 --port 8000

## Example request
curl -X POST "http://localhost:8000/solve" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","secret":"mysecret","url":"https://..."}'

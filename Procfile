web: uvicorn main:app --workers 3 --reload --timeout-keep-alive 10 --host 0.0.0.0 --port ${PORT}
heroku ps:scale web=1 worker=5
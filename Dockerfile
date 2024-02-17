FROM python:3.8-slim
ENV PORT=8000
COPY requeriements.txt /
RUN pip install -r /requeriements.txt
COPY ./app /app


ENTRYPOINT uvicorn app.main:app --host 0.0.0.0 --port $PORT
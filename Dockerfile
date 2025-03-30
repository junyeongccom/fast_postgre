FROM python:3.12.7
WORKDIR /app

# com 폴더도 복사해줌
COPY ./main.py /app/
COPY ./requirements.txt /app/
COPY ./com /app/com

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]


FROM python:3.12.7
WORKDIR /app

COPY ./main.py /app/
COPY ./requirements.txt /app/
COPY ./com /app/com
COPY .env .env

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

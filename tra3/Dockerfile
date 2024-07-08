FROM python:3.9


WORKDIR /app


COPY requirements.txt .
Flask==2.0.1
psycopg2-binary==2.9.1

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# Exponha a porta que a aplicação web usa
EXPOSE 5000

CMD ["python", "app.py"]

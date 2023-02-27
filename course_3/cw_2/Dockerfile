FROM python:3.10

ENV HOME /app
WORKDIR $HOME

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "app.py"]

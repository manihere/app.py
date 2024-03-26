FROM python:3.8-slim

WORKDIR /app

COPY . /app/

# RUN pip install -r requirements.txt

# Dockerhub creds : docker login -u manihere12; manihere12/dckr_pat_ejENkgTIQkAaaDcoOnXRZoD9F60

CMD ["python","app.py"]
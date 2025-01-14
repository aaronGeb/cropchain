FROM python:3.11.10-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
#RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/models

# Copy prediction.py and random_forest_model.pkl into the container
COPY scripts/flask_pre.py /app/
COPY models/random_forest_model.pkl  /app/models/

EXPOSE 9696
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "flask_pre:app"]
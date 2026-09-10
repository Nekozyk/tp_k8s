FROM python:3.12-slim

WORKDIR /app

# Installation des dépendances (couche mise en cache si requirements.txt ne change pas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code applicatif
COPY app.py .

EXPOSE 5000

# Utilisateur non-root : bonne pratique pour l'exécution en conteneur/Kubernetes
RUN useradd --create-home appuser
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

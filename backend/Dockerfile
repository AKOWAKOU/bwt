# Dockerfile pour le backend
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /usr/app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port 8000 pour le serveur Django
EXPOSE 8000

# Commande pour appliquer les migrations et démarrer le serveur
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# Dockerfile pour le frontend
FROM node:16 AS build

# Définir le répertoire de travail
WORKDIR /usr/app

# Copier les fichiers package.json et package-lock.json
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers
COPY . ./

# Construire l'application
RUN npm run build

# Étape finale : servir avec un serveur léger
FROM nginx:alpine
COPY --from=build usr/app/build /usr/share/nginx/html

EXPOSE 8065

CMD ["nginx", "-g", "daemon off;"]

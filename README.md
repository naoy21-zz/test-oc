## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/yoanberchel/OC-Lettings.git`

#### Créer l'environnement virtuel

- `cd /path/to/OC-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/OC-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/OC-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/OC-Lettings`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/OC-Lettings`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## CircleCI & Conteneurisation & Déploiement

### Prérequis

- Compte CircleCI,
- Compte DockerHub (avec un nouveau repository),
- Compte Heroku (avec une nouvelle application).

### Conteneurisation

La conteneurisation est automatisée par CircleCI.    
En s'appuyant sur le fichier "Dockerfile", une image Docker est créée et envoyée vers un repository DockerHub.

Pour extraire l'image du DockerHub et lancer un conteneur avec l'application en local avec Docker :
- Installer Docker sur votre machine local,
- `docker run -d -p 8000:8000 {image}:{tag}`.

### Déploiement

Le déploiement vers Heroku est automatisé par CircleCI.    
En s'appuyant sur le fichier "Dockerfile", une image Docker est créée.    
S'ensuit le déploiement de l'application par le Registre des conteneurs Heroku.

### Mise en place

Une fois le repository cloné, créez votre propre repository github et remplacez l'url de origin :
`git remote set-url origin {new git url}`

Vous pourrez ensuite push vers ce nouveau repository github :
`git branch -M main`
`git push -u origin main`

Dans le fichier "config.yml", remplacez :
- "yoanberchel/orange-county-lettings" par votre propre repository DockerHub,
- "oc-lettings-5" par votre propre application Heroku.

Configurez votre repository github dans CircleCI en utilisant le fichier "config.yml" déjà présent.
Voici une vidéo tutoriel : https://www.youtube.com/watch?v=jzir3eYCCw4

Créez les variables d'environnement dans les réglages du projet CircleCI :
- DOCKER_PASS : mot de passe de votre compte DockerHub,
- DOCKER_USER : Docker ID de votre compte DockerHub,
- HEROKU_TOKEN : API Key de votre compte Heroku (dans "Account settings").

## Sentry

Créez un compte [Sentry](https://sentry.io/).

Créez un nouveau projet dans Sentry et remplacez le "dsn" à la fin du fichier "settings.py".

Vérification : naviguez vers l'URI "sentry-debug/", un nouvel événement s'affichera sur votre page Issues dans Sentry.
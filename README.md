# 📝 Blog Django — Projet 3 (Class project)

Application web de blog développée avec **Django 5.2**. Elle permet de créer, lire, modifier et supprimer des articles (posts) ainsi que des commentaires associés.

---

## 📋 Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Lancer le projet](#lancer-le-projet)
- [Structure du projet](#structure-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Routes disponibles](#routes-disponibles)
- [Interface d'administration](#interface-dadministration)

---

## Prérequis

Avant de commencer, assure-toi d'avoir installé :

- [Python 3.10+](https://www.python.org/downloads/)
- `pip` (inclus avec Python)
- `git` (optionnel, pour cloner le dépôt)

---

## Installation

### 1. Cloner ou télécharger le projet

```bash
git clone <url-du-depot>
cd projet_3
```

> Ou simplement décompresse l'archive ZIP dans un dossier de ton choix.

---

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

Activer l'environnement virtuel :

- **Windows** :
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux** :
  ```bash
  source venv/bin/activate
  ```

> ✅ Tu devrais voir `(venv)` apparaître au début de ta ligne de commande.

---

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

### 4. Appliquer les migrations de base de données

```bash
python manage.py migrate
```

> Cette commande crée le fichier `db.sqlite3` avec toutes les tables nécessaires.

---

### 5. (Optionnel) Créer un compte administrateur

```bash
python manage.py createsuperuser
```

Suis les instructions pour choisir un nom d'utilisateur, une adresse e-mail et un mot de passe.

---

## Lancer le projet

```bash
python manage.py runserver
```

Ouvre ton navigateur et accède à :

```
http://127.0.0.1:8000/
```

Pour arrêter le serveur : `Ctrl + C`

---

## Structure du projet

```
projet_3/
├── blog/                        # Application principale
│   ├── migrations/              # Historique des migrations DB
│   ├── templates/
│   │   ├── base.html            # Template de base (layout commun)
│   │   ├── posts/
│   │   │   ├── index.html       # Liste des posts
│   │   │   ├── detail.html      # Détail d'un post + commentaires
│   │   │   └── manage_post.html # Formulaire créer / modifier un post
│   │   └── comments/
│   │       └── update_comment.html  # Formulaire modifier un commentaire
│   ├── admin.py                 # Enregistrement des modèles dans l'admin
│   ├── models.py                # Modèles Post et Comment
│   ├── urls.py                  # Routes de l'application blog
│   └── views.py                 # Logique des vues (CRUD)
├── blog_project/                # Configuration du projet Django
│   ├── settings.py              # Paramètres globaux
│   ├── urls.py                  # Point d'entrée des URLs
│   └── wsgi.py / asgi.py        # Déploiement
├── db.sqlite3                   # Base de données SQLite (générée automatiquement)
├── manage.py                    # Commande de gestion Django
└── requirements.txt             # Dépendances Python
```

---

## Fonctionnalités

### Articles (Posts)
| Action | Description |
|---|---|
| 📄 Lister | Affiche tous les articles avec pagination (9 par page) |
| 🔍 Consulter | Affiche le détail d'un article et ses commentaires |
| ✏️ Créer | Formulaire pour rédiger un nouvel article |
| 🔄 Modifier | Formulaire pour éditer un article existant |
| 🗑️ Supprimer | Supprime un article et tous ses commentaires |

### Commentaires
| Action | Description |
|---|---|
| ✏️ Ajouter | Formulaire disponible sur la page de détail d'un article |
| 🔄 Modifier | Modification du contenu d'un commentaire |
| 🗑️ Supprimer | Suppression d'un commentaire |

---

## Routes disponibles

| Méthode | URL | Description |
|---|---|---|
| GET | `/` | Liste de tous les posts |
| GET | `/<id>/` | Détail d'un post |
| GET/POST | `/create/` | Créer un post |
| GET/POST | `/<id>/update/` | Modifier un post |
| POST | `/<id>/delete/` | Supprimer un post |
| GET | `/<id>/comments/` | Liste des commentaires d'un post |
| POST | `/<id>/comments/add/` | Ajouter un commentaire |
| POST | `/<id>/comments/<cid>/update/` | Modifier un commentaire |
| POST | `/<id>/comments/<cid>/delete/` | Supprimer un commentaire |

---

## Interface d'administration

Django fournit une interface d'administration intégrée pour gérer les données directement.

1. Crée un superutilisateur (voir [étape 5](#5-optionnel-créer-un-compte-administrateur))
2. Accède à l'interface via :

```
http://127.0.0.1:8000/admin/
```

Tu pourras y gérer les **Posts** et les **Comments** depuis une interface graphique.

---

## Technologies utilisées

- **Python 3.10+**
- **Django 5.2**
- **SQLite** (base de données locale, aucune configuration nécessaire)
- **HTML + Bootstrap 5.3.8

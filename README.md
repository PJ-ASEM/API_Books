# API GESTION DE BIBLIOTHEQUE

Cette API permet de gérer des livres classer par categorie

### Installing Dependencies

#### Python 3.10
#### pip 22.0.3 from C:\Users\ASSIMPAH\AppData\Local\Programs\Python\Python310\Lib\site-packages\pip (Python 3.10)

Si python n'est pas installé sur votre machine, telecharger le via ce lien [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)


#### Dépendances de PIP

Exécuter la commande ci dessous pour installer les dépendences
```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Cette commande installera tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open-source SQL et un ORM écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) est l'extension que nous utiliserons pour gérer les requêtes cross origin de notre serveur frontal.

## Database Setup
avec postgres en cours d'execcution, vous pouvez restauré la base de données en utilisant le fichier fourni the bibliotheque.sql et insérer des données avec le fichier bibliotheque_insert.sql .
```bash
psql bibliotheque > bibliotheque.sql
```

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 422: Unprocessable
. 404: Not found ou Mauvaise requete

## Endpoints
. ## GET/livres

    GENERAL:Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
    SAMPLE: curl -i http://localhost:5000/livres

    {
        "livres": [
            {
                "auteur": "Michelle OBAMA",
                "date_de_publication": "Fri, 30 Nov 2018 00:00:00 GMT",
                "editeur": "Librairie Artheme Fayard",
                "id": 1,
                "isbn": "978-2-213-70787-7",
                "libelle_categorie": 9,
                "titre": "Devenir"
            },
            {
                "auteur": "Robert GREENE",
                "date_de_publication": "Thu, 31 Dec 1998 00:00:00 GMT",
                "editeur": "Les editions Leduc.s",
                "id": 3,
                "isbn": "979-10-92928-07-5",
                "libelle_categorie": 3,
                "titre": "Power - Les 48 lois du pouvoir"
            }
            {
                "auteur": "Nelson MANDELA",
                "date_de_publication": "Wed, 30 Nov 1994 00:00:00 GMT",
                "editeur": "Livre de poche",
                "id": 4,
                "isbn": "9780230013858",
                "libelle_categorie": 9,
                "titre": "Un long chemin vers la liberte"
            }
        ],
        "success": true,
        "total": 3
    }
```

.##GET/livres/(id)
  GENERAL: Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de son ID et retourne également la valeur du succès et l'id passé en parametre.

    SAMPLE: curl -i http://localhost:5000/livres/10

    {
        "livre": {
            "auteur": "Amin Maalouf",
            "date_de_publication": "Sat, 31 Dec 1983 00:00:00 GMT",
            "editeur": "Livre de poche",
            "id": 10,
            "isbn": "9780863560231",
            "libelle_categorie": 3,
            "titre": "Les Croisades vues par les Arabes"
        },
        "selected_id": 10,
        "success": true
    }
```

.##GET/categories/(id)/livres
  GENERAL:   Cet endpoint permet de lister les livres appartenant à une categorie donnée. Il renvoie l' objet de la categorie passé en id et les livres l'appartenant ainsi que la valeur du succès et  le total des livres dans la categorie.

    SAMPLE: curl -i http://localhost:5000/categories/1/livres

    {
        "id_categorie": 1,
        "libelle_categorie": "Roman",
        "livres": [
            {
                "auteur": "Christian JACQ",
                "date_de_publication": "Wed, 31 Dec 1997 00:00:00 GMT",
                "editeur": "Robert LAFFONT",
                "id": 6,
                "isbn": "2-221-08625-2",
                "libelle_categorie": 1,
                "titre": "Le pharaon noir"
            },
            {
                "auteur": "Paulo Coelho",
                "date_de_publication": "Sat, 31 Dec 1988 00:00:00 GMT",
                "editeur": "Anne Carriere",
                "id": 7,
                "isbn": "978-2-910188-13-9",
                "libelle_categorie": 1,
                "titre": "L'Alchimiste"
            }
        ],
        "success": true,
        "total": 2
    }

```

.##GET/categories/(id)
  GENERAL: Cet endpoint permet de récupérer les informations d'une categorie particulière s'il existe par le biais de son ID, et retourne également la valeur du succès et l'id passé en parametre
    SAMPLE: curl -i http://localhost:5000/categories/9

    {
        "categorie": {
            "id": 9,
            "libelle_categorie": "Auto-biographie"
        },
        "selected_id": 9,
        "success": true
    }
```
. ## GET/categories

    GENERAL:Cet endpoint retourne la liste des objets categories, la valeur du succès et le total des livres. 
    
    SAMPLE: curl -i http://localhost:5000/livres

    {
        "categories": [
            {
                "id": 1,
                "libelle_categorie": "Roman"
            },
            {
                "id": 4,
                "libelle_categorie": "Philosophie"
            },
            {
                "id": 9,
                "libelle_categorie": "Auto-biographie"
            },
            {
                "id": 8,
                "libelle_categorie": "BD"
            }
        ],
        "success": true,
        "total": 4
    }
```

. ## DELETE/livres/(id)
    GENERAL: Cet endpoint permet de supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, les informations de ce livre, la valeur du succès et le nouveau total des livres enregistrés.

        SAMPLE: curl -X DELETE http://localhost:5000/livres/12

    {
        "id": 12,
        "livre": {
            "auteur": "Benoît XVI et Robert Sarah",
            "date_de_publication": "Wed, 15 Jan 2020 00:00:00 GMT",
            "editeur": "Fayard",
            "id": 12,
            "isbn": "9782213718620",
            "libelle_categorie": 7,
            "titre": "Des profondeurs de nos coeurs"
        },
        "success": true,
        "total_livres": 11
    }
```

. ## DELETE/categories/(id)
    GENERAL: Cet endpoint permet de supprimer un element si l'ID existe.Retourne l'ID de la categorie supprimée, les informations de cette categorie, la valeur du succès et le nouveau total des categories enregistrés.

        SAMPLE: curl -X DELETE http://localhost:5000/categories/10

    {
        "categorie": {
            "id": 10,
            "libelle_categorie": "Bandes dessinee"
        },
        "id": 10,
        "success": true,
        "total_categories": 9
    }   
```

. ##PATCH/livres/(id)
    GENERAL: Cet endpoint permet de mettre à jour les informations du livre dont  l' id en passé en parametre et affiche le livre mis à jour, la valeur du succès et l'id passé en parametre..

    SAMPLE: curl -X PATCH http://localhost:5000/livres/3 -H "Content-Type:application/json" -d '{"auteur": "Robert GREENE","date_publication": "31-12-1998","editeur":    "Les editions Leduc.s","id": 3,"isbn": "979-10-92928-07-5","titre": "Power - Les 48 lois du pouvoir"}'

    {
        "livre": {
            "auteur": "Robert GREENE",
            "date_de_publication": "Thu, 31 Dec 1998 00:00:00 GMT",
            "editeur": "Les editions Leduc.s",
            "id": 3,
            "isbn": "979-10-92928-07-5",
            "libelle_categorie": 3,
            "titre": "Power - Les 48 lois du pouvoir"
        },
        "success": true,
        "updated_id": 3
    }

```

. ##PATCH/categories(id)
    GENERAL:Cet endpoint permet de mettre à jour le libelle la categorie dont l' ID est passé en paramètre. Il retourne une nouvelle categorie avec la nouvelle valeur,  la valeur du succès et l'id passé en parametre.

    SAMPLE: curl -X PATCH 'http://localhost:5000/categories/8' -H "Content-Type:application/json" -d '{"libelle_categorie":"BD"}'

    {
        "categorie": {
            "id": 8,
            "libelle_categorie": "BD"
        },
        "success": true,
        "updated_id": 8
    }
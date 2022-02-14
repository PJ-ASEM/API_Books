import os
from dotenv import load_dotenv
from flask import Flask, abort, jsonify, render_template, request, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app=Flask(__name__)

database_name='bibliotheque'
#psw=os.getenv('db_password')
#host=os.getenv('hostname')
database_path='postgresql://qnruakoxblodue:e3ef795a2d8301de11ac1d5aaaf508bf871aaab38ad7eaedb2bc946769325d44@ec2-54-76-249-45.eu-west-1.compute.amazonaws.com:5432/dbhh4n3ov5v3b8'
app.config['SQLALCHEMY_DATABASE_URI']=database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE,OPTIONS')
    return response


################################################################
#
#             Classe Categorie
#
################################################################
class Categorie(db.Model):
    __tablename__="categories"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle_categorie=db.Column(db.String(50), nullable=False)
    livres=db.relationship('Livre', backref='categorie', lazy=True)

    def __init__(self, id, libelle_categorie):
        self.id=id
        self.libelle_categorie=libelle_categorie

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format (self):
        return {
            'id':self.id,
            'libelle_categorie':self.libelle_categorie,
        }

    def update(self):
        db.session.commit()



################################################################
#
#             Classe Livre
#
################################################################
class Livre(db.Model):
    __tablename__="livres"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn=db.Column(db.String(13), nullable=False)
    titre=db.Column(db.String(50), nullable=False)
    date_publication=db.Column(db.Date(),nullable=False)
    auteur=db.Column(db.String(100), nullable=False)
    editeur=db.Column(db.String(100), nullable=False)
    categorie_id=db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __init__(self, id, isbn, titre, date_publication, auteur, editeur, categorie_id):
        self.id=id
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format (self):
        return {
            'id':self.id,
            'isbn':self.isbn,
            'titre':self.titre,
            'date_de_publication':self.date_publication,
            'auteur':self.auteur,
            'editeur':self.editeur,
            'libelle_categorie':self.categorie_id
        }

    def update(self):
        db.session.commit()

db.create_all()


##########################################################
#
#           Endpoint LISTE DE TOUS LES LIVRES 
#
##########################################################


@app.route('/livres' , methods=['GET'])
def get_all_books():
    livres=Livre.query.all()
    formated_books=[ bk.format() for bk in livres]
    return jsonify({
        'success':True,
        'total':len(livres),
        "livres":formated_books   
    })

############################################################
#
#    Endpoint CHERCHER UN LIVRE EN PARTICULIER PAR SON ID
#
############################################################
@app.route('/livres/<int:id>' , methods=['GET'])
def get_book(id):
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        
        return jsonify({
            'success':True,
            'selected_id':id,
            'livre':livre.format()
        })


############################################################
#
#    Endpoint LISTE DES LIVRES D'UNE CATEGORIE
#
############################################################
@app.route('/categories/<int:id>/livres' , methods=['GET'])
def get_books_with_cat_id(id):
    cat=Categorie.query.get(id)
    if cat is None:
        abort(404)
    else:
        livres=Livre.query.filter(Livre.categorie_id==id).all()
        formated_books=[ bk.format() for bk in livres]
        return jsonify({
            'success':True,
            'id_categorie':id,
            'libelle_categorie':cat.libelle_categorie,
            'total':len(livres),
            "livres":formated_books   
        })
        

        




############################################################
#
#    Endpoint LISTER UNE CATEGORIE
#
############################################################


############################################################
#
#    Endpoint CHERCHER UNE CATEGORIE PAR SON ID
#
############################################################
@app.route('/categories/<int:id>' , methods=['GET'])
def get_categorie(id):
    cat=Categorie.query.get(id)
    if cat is None:
        abort(404)
    else:
        return jsonify({
            'success':True,
            'selected_id':id,
            'categorie':cat.format()
        })

@app.route('/')
def index():
	return '<h2>welcome to flask journey</h2>'
##########################################################
#
#           Endpoint LISTE DE TOUTES LES CATEGORIES 
#
##########################################################
@app.route('/categories' , methods=['GET'])
def get_all_categories():
    categories=Categorie.query.all()
    #return render_template('categoriesList.html', data=categories)
    formated_cats=[ cat.format() for cat in categories]
    return jsonify({
        'success':True,
        'total':len(categories),
        "categories":formated_cats   
    })


##########################################################
#
#           Endpoint SUPPRIMER UN LIVRE
#
##########################################################
@app.route('/livres/<int:id>', methods=['DELETE'])
def delete_book(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        livre.delete()
        return jsonify({
            'success':True,
            'id':id,
            'livre':livre.format(),
            'total_livres':Livre.query.count()
        })

        
##########################################################
#
#           Endpoint SUPPRIMER UNE CATEGORIE
#
##########################################################
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    cat = Categorie.query.get(id)
    if cat is None:
        abort(404)
    else:
        cat.delete()
        return jsonify({
            'success':True,
            'id':id,
            'categorie':cat.format(),
            'total_categories':Categorie.query.count()
        })


##########################################################
#
#    Endpoint MODIFIER LES INFORMATIONS D'UN LIVRE
#
##########################################################
@app.route('/livres/<int:id>', methods=['PATCH'])
def update_book(id):
    bk=request.get_json()
    livre=Livre.query.get(id)
    livre.isbn=bk.get('isbn')
    livre.titre=bk.get('titre')
    livre.date_publication=bk.get('date_publication')
    livre.auteur=bk.get('auteur')
    livre.editeur=bk.get('editeur')
    livre.categorie_id=bk.get('id')

    if livre is None:
        abort(404)
    else:
        livre.update()
        return jsonify({
            'success':True,
            'updated_id':id,
            'livre':livre.format()
        })


##########################################################
#
#    Endpoint MODIFIER LE LIBELLE D'UNE CATEGORIE
#
##########################################################


@app.route('/categories/<int:id>', methods=['PATCH'])
def update_category(id):
    cat=request.get_json()
    categorie=Categorie.query.get(id)
    categorie.libelle_categorie=cat.get('libelle_categorie')
    if categorie is None:
        abort(404)
    else:
        categorie.update()
        return jsonify({
            'success':True,
            'updated_id':id,
            'categorie':categorie.format()
        })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Ressource non disponible"
        }), 404

@app.errorhandler(400)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "Mauvaise requete"
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
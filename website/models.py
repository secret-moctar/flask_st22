from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('admin','enseignant','etudiant'), nullable=False)

class Etudiant(db.Model):
    __tablename__ = 'Etudiants'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    date_naissance = db.Column(db.Date)
    notes = db.relationship('Note', backref='etudiant', lazy=True)

class Enseignant(db.Model):
    __tablename__ = 'Enseignants'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    matiere = db.Column(db.String(50))

class Matiere(db.Model):
    __tablename__ = 'Matieres'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)

class Note(db.Model):
    __tablename__ = 'Notes'
    id = db.Column(db.Integer, primary_key=True)
    etudiant_id = db.Column(db.Integer, db.ForeignKey('Etudiants.id'), nullable=False)
    matiere_id = db.Column(db.Integer, db.ForeignKey('Matieres.id'), nullable=False)
    valeur = db.Column(db.Numeric(5,2), nullable=False)

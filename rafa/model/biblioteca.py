from database import db
from sqlalchemy import ForeignKey


class Autor(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nacionalidade = db.Column(db.String(50), nullable=False)

    livros = db.relationship("Livro", back_populates="autor")

    def toJson(self):
        return {"id": self.id, "nome": self.nome, "data_nascimento": self.data_nascimento, "nacionalidade": self.nacionalidade}

class Categoria(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)

    livros = db.relationship("Livro", back_populates="categoria")

    def toJson(self):
        return {"id": self.id, "nome": self.nome}

class Livro(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)
    numero_paginas = db.Column(db.Integer, nullable=False)
    autor_id = db.Column(db.Integer, ForeignKey('autor.id'), nullable=False)
    categoria_id = db.Column(db.Integer, ForeignKey('categoria.id'), nullable=False)

    
    autor = db.relationship("Autor", back_populates="livros")
    categoria = db.relationship("Categoria", back_populates="livros")

    def toJson(self):
        return {"id": self.id, "titulo": self.titulo, "isbn": self.isbn, "data_publicacao": self.data_publicacao,
                    "numero_paginas": self.numero_paginas, "autor_id": self.autor_id, "categoria_id": self.categoria_id}

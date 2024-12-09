from model import Autor, Categoria, Livro, db


class AutorDAO:
    @staticmethod
    def buscar_todos_autores():
        return Autor.query.all()
    
    @staticmethod
    def add_autor(nome, data_nascimento, nacionalidade):
        try:
            autor = Autor(nome = nome, data_nascimento = data_nascimento, nacionalidade = nacionalidade)
            db.session.add(autor)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            return False
        

        
class CategoriaDAO:
    @staticmethod
    def buscar_todos_categorias():
        return Categoria.query.all()
    
    @staticmethod
    def add_categoria(nome):
        try:
            categoria = Categoria(nome = nome)
            db.session.add(categoria)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            return False



class LivroDAO:
    @staticmethod
    def buscar_todos_livros():
        return Livro.query.all()
    
    @staticmethod
    def add_livro(titulo, isbn, data_publicacao, numero_paginas, autor_id, categoria_id):
        try:
            livro = Livro(titulo = titulo, isbn = isbn, data_publicacao = data_publicacao, numero_paginas = numero_paginas, autor_id = autor_id, categoria_id = categoria_id)
            db.session.add(livro)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            return False
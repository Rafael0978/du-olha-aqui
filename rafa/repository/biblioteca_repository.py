from dao import AutorDAO, CategoriaDAO, LivroDAO


class AutorRepository:
    def __init__(self):
        self.autorDAO = AutorDAO()

    def buscar_todos_autores_json(self):
        autores = AutorDAO.buscar_todos_autores()
        listaAutor = []
        for autor in autores:
            listaAutor.append(autor.toJson())
        return listaAutor
    
    def buscar_todos_autores(self):
        return AutorDAO.buscar_todos_autores()
    
    def add_autor(self, nome, data_nascimento, nacionalidade):
        retorno = AutorDAO.add_autor("Igor", "1958-12-11", "Brasileiro")
        if retorno:
            return "Adicionado com sucesso! :)" 
        return "Erro ao adicionar! :("

    def excluir_autor(self, id):
        autor = self.autorDAO.buscar_por_id(id)
        if autor:
            self.autorDAO.deletar(autor)
            return "Autor excluído com sucesso!"
        return "Autor não encontrado."


    
class CategoriaRepository:
    def __init__(self):
        self.categoriaDao = CategoriaDAO()

    def buscar_todos_categorias_json(self):
        Categorias = CategoriaDAO.buscar_todos_categorias()
        listaCategoria = []
        for categoria in Categorias:
            listaCategoria.append(categoria.toJson())
        return listaCategoria
    
    def buscar_todos_categorias(self):
        return CategoriaDAO.buscar_todos_categorias()
    
    def add_categoria(self):
        retorno = CategoriaDAO.add_categoria("Terror")
        if retorno:
            return "Adicionado com sucesso! :)" 
        return "Erro ao adicionar! :("

    def excluir_categoria(self, id):
        categoria = self.categoriaDAO.buscar_por_id(id)
        if categoria:
            self.categoriaDAO.deletar(categoria)
            return "Categoria excluído com sucesso!"
        return "Categoria não encontrado."
    

    
class LivroRepository:
    def __init__(self):
        self.livroDao = LivroDAO()

    def buscar_todos_livros_json(self):
        livros = LivroDAO.buscar_todos_livros()
        listaLivros = []
        for livro in livros:
            listaLivros.append(livro.toJson())
        return listaLivros
    
    def buscar_todos_livros(self):
        return LivroDAO.buscar_todos_livros()
    
    def add_livro(self, titulo, isbn, data_publicacao, numero_paginas):
        retorno = LivroDAO.add_livro("Medo na Esquina", "11-22-33-44-55-66", "2020-11-25", "531")
        if retorno:
            return "Adicionado com sucesso! :)" 
        return "Erro ao adicionar! :("

    def excluir_livro(self, id):
        livro = self.livroDAO.buscar_por_id(id)
        if livro:
            self.livroDAO.deletar(livro)
            return "Livro excluído com sucesso!"
        return "Livro não encontrado."
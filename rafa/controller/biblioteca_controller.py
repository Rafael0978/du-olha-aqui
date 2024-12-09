from flask import Blueprint, jsonify
from repository import AutorRepository, CategoriaRepository, LivroRepository

biblioteca_controller = Blueprint("biblioteca", __name__)

autorRepository = AutorRepository() 
categoriaRepository = CategoriaRepository()
livroRepository = LivroRepository()


@biblioteca_controller.route("/addautor", methods=["POST"])
def add_autor_controller():
    autorRepository = AutorRepository()
    return autorRepository.add_autor("Igor", "22-10-1970", "Brasileiro")

@biblioteca_controller.route("/addcategoria", methods=["POST"])
def add_categoria(): 
    return categoriaRepository.add_categoria("Aventura")

@biblioteca_controller.route("/addlivro", methods=["POST"])
def add_livro(): 
    return livroRepository.add_livro("Harry Potter", "44-32-43-44-75-99", "2000-09-24", "250")




@biblioteca_controller.route("/verautor")
def ver_autor():
    return jsonify(autorRepository.buscar_todos_autores_json()) 

@biblioteca_controller.route("/vercategoria")
def ver_categoria():
    return jsonify(categoriaRepository.buscar_todos_categorias_json()) 

@biblioteca_controller.route("/verlivro")
def ver_livro():
    return jsonify(livroRepository.buscar_todos_livros_json()) 


@biblioteca_controller.route("/excluirautor", methods=["DELETE"])
def excluir_autor(id):
    return autorRepository.excluir_autor(id)

@biblioteca_controller.route("/excluircategoria", methods=["DELETE"])
def excluir_categoria(id):
    return categoriaRepository.excluir_categoria(id)

@biblioteca_controller.route("/excluirlivro", methods=["DELETE"])
def excluir_livro(id):
    return livroRepository.excluir_livro(id)
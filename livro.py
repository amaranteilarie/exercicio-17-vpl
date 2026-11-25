from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(
        self,
        codigo: int,
        titulo: str,
        ano: int,
        editora: Editora,
        autor: Autor,
        numero_capitulo: int,
        titulo_capitulo: str,
    ):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora if isinstance(editora, Editora) else None
        self.__autores = []
        if isinstance(autor, Autor):
            self.__autores.append(autor)
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor in self.__autores:
            self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        if self.find_capitulo_by_titulo(titulo) is None:
            self.__capitulos.append(Capitulo(numero, titulo))

    def excluir_capitulo(self, titulo: str):
        capitulo = self.find_capitulo_by_titulo(titulo)
        if capitulo is not None:
            self.__capitulos.remove(capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
        return None

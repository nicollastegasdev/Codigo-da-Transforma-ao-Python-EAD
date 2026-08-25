# 1. Classe Carro
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


# 2. Herança - CarroEletrico
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Autonomia da bateria: {self.autonomia_bateria} km")


# 3. Métodos especiais __init__ e __str__
class CarroComStr:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}"


# Testando as classes

carro1 = Carro("Toyota", "Corolla")
carro1.exibir_info()

print()

carro2 = CarroEletrico("Tesla", "Model 3", 500)
carro2.exibir_info()

print()

carro3 = CarroComStr("Honda", "Civic")
print(carro3)


# Desafio Extra - Biblioteca
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({status})"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"O livro '{titulo}' foi emprestado.")
                return
        print(f"O livro '{titulo}' não está disponível.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"O livro '{titulo}' foi devolvido.")
                return
        print(f"O livro '{titulo}' não foi encontrado ou já está disponível.")

    def listar_livros(self):
        print("\nLivros da biblioteca:")
        for livro in self.livros:
            print(livro)


# Testando a biblioteca
biblioteca = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.listar_livros()

biblioteca.emprestar_livro("Dom Casmurro")

biblioteca.listar_livros()

biblioteca.devolver_livro("Dom Casmurro")

biblioteca.listar_livros()
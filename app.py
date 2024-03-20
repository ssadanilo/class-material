# Criando a classe Merial
class Material:
    def __init__(self, titulo, autor_ou_editora): # Construtor
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self): # Método
        print('Título:', self.titulo)
        print('Autor/Editora:', self.autor_ou_editora)

# Criando a classe Livro
class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero): # Construtor
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self): # Método
        super().exibir_informacoes()
        print('Gênero:', self.genero)

# Criando a classe Revista
class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao): # Construtor
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self): # Método
        super().exibir_informacoes()
        print('Edição:', self.edicao)
    
# Instância das classe Livro e Revista
livro1 = Livro('Duna', 'Frank Herbert', 'Ficção Científica')
livro2 = Livro('O Último Reino', 'Bernard Cornwell', 'Aventura')
livro3 = Livro('A Revolta de Atlas', 'Ayn Rand', 'Romance')
revista1 = Revista('Turma da Mônica', 'Maurício de Souza', 'Nov/2023')


# Exibindo as informações
print('Informações do Livro')
livro1.exibir_informacoes()
print('\nInformações do Livro')
livro2.exibir_informacoes()
print('\nInformações do Livro')
livro3.exibir_informacoes()
print('\nInformações da Revista')
revista1.exibir_informacoes()
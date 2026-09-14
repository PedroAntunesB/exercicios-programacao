class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def apresentar(self):
        print("Nome:", self.nome)
        print("Data de nascimento:", self.data_nascimento)


class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, matricula, curso, notas):
        super().__init__(nome, data_nascimento)
        self.matricula = matricula
        self.curso = curso
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def apresentar(self):
        super().apresentar()
        print("Matrícula:", self.matricula)
        print("Curso:", self.curso)
        print("Notas:", self.notas)
        print("Média:", self.calcular_media())


class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, matricula, disciplina):
        super().__init__(nome, data_nascimento)
        self.matricula = matricula
        self.disciplina = disciplina

    def apresentar(self):
        super().apresentar()
        print("Matrícula:", self.matricula)
        print("Disciplina:", self.disciplina)


aluno = Aluno(
    "Pedro",
    "15/05/2008",
    "2026001",
    "Informática",
    [8.5, 7.0, 9.0]
)

professor = Professor(
    "Carlos",
    "10/03/1980",
    "P1001",
    "Programação"
)

print("--- ALUNO ---")
aluno.apresentar()

print("\n--- PROFESSOR ---")
professor.apresentar()
import random

class Usuario:
    matriculas_usadas = []

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.matricula = self._gerar_matricula()
        self.em_atraso = False


    def _gerar_matricula(self):
        while True:
            matricula = random.randint(1000, 9999)
            if matricula not in Usuario.matriculas_usadas:
                Usuario.matriculas_usadas.append(matricula)
                return matricula

    def __str__(self):
        situacao = "Em atraso" if self.em_atraso else "Regular"
        return f"[{self.matricula}] {self.nome} | Telefone: {self.telefone}" 

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "telefone": self.telefone,
            "em_atraso": self.em_atraso
        } 
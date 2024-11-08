class Funcionario:
    def __init__(self,nome,cargo,_salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = _salario
    def descricao(self):
        return f"Nome: {self.nome}\nCargo:{self.cargo}\nSalario: R${self._salario:.2f}"
    
class Gerente(Funcionario):
    def __init__(self,nome,cargo,bonus,_salario = 1412):
        super().__init__(nome,cargo, _salario)
        self.bonus = bonus
        self._salario += self.bonus
    def descricao(self):
        return super().descricao() + f" com o bônus de R$: {self.bonus:.2f}"
    

f1 = Funcionario("Joao", "Assistente", 1412)
g1 = Gerente("bernardo", "Gerente", 5000)
print(f1.descricao())
print(g1.descricao())


class Usuario:
    def __init__(self,nome: str, vinculo: str):
        self.nome = nome
        self.vinculo = vinculo
    
    def __str__(self):
        return f"{self.nome} ({self.vinculo})"
    
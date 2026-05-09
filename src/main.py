from usuario import Professor, Aluno, Externo
from sala import Laboratorio, EstudoIndividual, EstudoEmGrupo
from reserva import Reserva
from datetime import datetime, timedelta

def main():
    print("TESTE")
    prof = Professor("Turing", "DOC-001")
    aluno = Aluno("Pedro", "POO-999")
    visitante = Externo("Joao", "111.222.333-44")
    
    print(prof)
    print(aluno)
    print(visitante)

    print("\nTESTE de SALAS")
    lab = Laboratorio("L-101", 30, ["30 PCs", "Projetor HD", "Lousa Digital"])
    sala_individual = EstudoIndividual("I-05")
    sala_grupo = EstudoEmGrupo("G-20", 6, quantidade_mesas=1, quantidade_quadros=2)
    
    print(lab)
    print(sala_individual)
    print(sala_grupo)

    print("\nTESTE RESERVA")
    
    inicio = datetime.now()
    fim = inicio + timedelta(hours=2)
    
    reserva1 = Reserva(prof, lab, inicio, fim)
    print(reserva1)

if __name__ == "__main__":
    main()
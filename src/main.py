from usuario import Professor, Aluno
from sala_factory import LaboratorioFactory, EstudoIndividualFactory
from ReservaFactory import ReservaFactory
from estrategia_reserva import PoliticaPrimeiroChegar, PoliticaPrioridadeDocente
from gerenciador_reservas import GerenciadorDeReservas
from datetime import datetime, timedelta

def main():
    print("SISTEMA DE RESERVAS ")
    print("-"*20)

    fabrica_lab = LaboratorioFactory()
    lab = fabrica_lab.criar_sala("L-101", capacidade=30, equipamentos=["PCs", "Projetor"])
    
    aluno1 = Aluno("João", "POO2-123")
    aluno2 = Aluno("Maria", "POO2-456")
    prof = Professor("Fabio", "DOC-001")

    agora = datetime.now()
    daqui_a_pouco = agora + timedelta(hours=2)

    print("\nTESTE 1: POLÍTICA 'PRIMEIRO A CHEGAR'")
    ReservaFactory.definir_politica(PoliticaPrimeiroChegar())
    
    print("1. João tenta reservar o Lab L-101")
    reserva_joao = ReservaFactory.criar_reserva(aluno1, lab, agora, daqui_a_pouco)

    print("\n2. Maria tenta reservar o MESMO Lab no MESMO horário")
    reserva_maria = ReservaFactory.criar_reserva(aluno2, lab, agora, daqui_a_pouco)
    if not reserva_maria:
        print("Sistema bloqueou a Maria corretamente!!!!!!!")


    print("\nTESTE 2: POLÍTICA 'PRIORIDADE DOCENTE' (Observer Pull)")
    ReservaFactory.definir_politica(PoliticaPrioridadeDocente())
    
    print("3. Professor Fabio precisa do Lab L-101 agora. Ele tenta reservarFabio")
    # Ao fazer isso, a Strategy vai cancelar a reserva do João e disparar o Observer
    reserva_prof = ReservaFactory.criar_reserva(prof, lab, agora, daqui_a_pouco)
    print("\nTESTE 3: MODIFICANDO RESERVA (Observer Push)")
    print("4. Professor Fabio decide estender a aula em 1 horaFabio")
    novo_fim = daqui_a_pouco + timedelta(hours=1)
    reserva_prof.modificar_horario(agora, novo_fim)
    print("\nTESTE 4: ESTADO DO SINGLETON (Repositório)")

    gerenciador = GerenciadorDeReservas.get_instancia()
    todas_reservas = gerenciador.obter_todas_reservas()
    
    print(f"Total de reservas no sistema: {len(todas_reservas)}")
    for r in todas_reservas:
        print(f" -> {r}")

if __name__ == "__main__":
    main()
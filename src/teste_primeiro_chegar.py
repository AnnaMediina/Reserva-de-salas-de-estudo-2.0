from datetime import datetime
from usuario import Aluno, Professor, Externo
from sala_factory import LaboratorioFactory, EstudoIndividualFactory, EstudoEmGrupoFactory
from reserva_factory import ReservaFactory
from estrategia_reserva import PoliticaPrimeiroChegar
from gerenciador_reservas import GerenciadorDeReservas

def main():
    print("=" * 60)
    print("TESTE DO SISTEMA DE RESERVAS - POLÍTICA: PRIMEIRO A CHEGAR")
    print("=" * 60)

    # 1. Criar salas
    print("\nCRIANDO SALAS")
    fabrica_lab = LaboratorioFactory()
    lab1 = fabrica_lab.criar_sala("L-1", capacidade=30, equipamentos=["Projetor", "Computadores"])
    lab2 = fabrica_lab.criar_sala("L-2", capacidade=20, equipamentos=["Estufa", "Balança"])

    fabrica_individual = EstudoIndividualFactory()
    indiv1 = fabrica_individual.criar_sala("I-1")
    indiv2 = fabrica_individual.criar_sala("I-2")

    fabrica_grupo = EstudoEmGrupoFactory()
    grupo1 = fabrica_grupo.criar_sala("G-1", capacidade=8, mesas=4, quadros=2)
    grupo2 = fabrica_grupo.criar_sala("G-2", capacidade=12, mesas=6, quadros=3)

    lista_salas = [lab1, lab2, indiv1, indiv2, grupo1, grupo2]
    for sala in lista_salas:
        print(f"{sala} | {sala.obter_detalhes()}")


    # 2. Instancia o gerenciador de reservas
    gerenciador = GerenciadorDeReservas.get_instancia()

    # 3. Configurar política Primeiro a Chegar
    ReservaFactory.definir_politica(PoliticaPrimeiroChegar())
    print("\nPolítica de reserva configurada: PRIMEIRO A CHEGAR")

    # 4. Criar usuários
    print("\nCRIANDO USUÁRIOS...")
    aluno1 = Aluno("Ana Carolina", "123456")
    aluno2 = Aluno("Bruno Mendes", "654321")
    professor = Professor("Dra. Fernanda Lima", "687")
    visitante = Externo("Carlos Alberto", "123.456.789-00")

    usuarios = [aluno1, aluno2, professor, visitante]
    for u in usuarios:
        print(f"{u}")

    # 5. Realizar reservas
    print("\nREALIZANDO RESERVAS\n")

    # Data base para os testes
    data_teste = datetime(2026, 5, 25)  # 25 de maio de 2026

    # Reserva 1: Aluno1 na sala I-1 das 09:00 às 11:00
    inicio1 = datetime(2026, 5, 25, 9, 0)
    fim1 = datetime(2026, 5, 25, 11, 0)
    print(f"{aluno1.nome} → Sala {indiv1.numero_sala} | {inicio1.strftime('%H:%M')} - {fim1.strftime('%H:%M')}")
    r1 = ReservaFactory.criar_reserva(aluno1, indiv1, inicio1, fim1)

    # Reserva 2: Aluno2 na mesma sala I-1 no mesmo horário (DEVE GERAR CONFLITO)
    print(f"{aluno2.nome} → Sala {indiv1.numero_sala} | {inicio1.strftime('%H:%M')} - {fim1.strftime('%H:%M')} (mesmo horário)")
    r2 = ReservaFactory.criar_reserva(aluno2, indiv1, inicio1, fim1)

    # Reserva 3: Professor na sala L-1 das 10:00 às 12:00 (sem conflito)
    inicio3 = datetime(2026, 5, 25, 10, 0)
    fim3 = datetime(2026, 5, 25, 12, 0)
    print(f"{professor.nome} → Sala {lab1.numero_sala} | {inicio3.strftime('%H:%M')} - {fim3.strftime('%H:%M')}")
    r3 = ReservaFactory.criar_reserva(professor, lab1, inicio3, fim3)

    # Reserva 4: Externo na sala G-1 das 14:00 às 16:00
    inicio4 = datetime(2026, 5, 25, 14, 0)
    fim4 = datetime(2026, 5, 25, 16, 0)
    print(f"{visitante.nome} → Sala {grupo1.numero_sala} | {inicio4.strftime('%H:%M')} - {fim4.strftime('%H:%M')}")
    r4 = ReservaFactory.criar_reserva(visitante, grupo1, inicio4, fim4)

    # Reserva 5: Aluno2 na sala I-1 das 10:00 às 12:00 (conflito parcial? A sala I-1 já tem reserva das 9-11)
    inicio5 = datetime(2026, 5, 25, 10, 0)
    fim5 = datetime(2026, 5, 25, 12, 0)
    print(f"{aluno2.nome} → Sala {indiv1.numero_sala} | {inicio5.strftime('%H:%M')} - {fim5.strftime('%H:%M')} (sobreposição parcial)")
    r5 = ReservaFactory.criar_reserva(aluno2, indiv1, inicio5, fim5)

    # 6. Listar todas as reservas confirmadas
    todas_reservas = gerenciador.obter_todas_reservas()

    print("\n" + "=" * 60)
    print("RESERVAS CONFIRMADAS")
    print("=" * 60)
    if todas_reservas:
        for i, r in enumerate(todas_reservas, 1):
            print(f"{i}. {r}")
    else:
        print("Nenhuma reserva confirmada.")

    # 7. Verificar disponibilidade de sala para um novo horário
    print("\n" + "=" * 60)
    print("VERIFICANDO DISPONIBILIDADE")
    print("=" * 60)

    # Verificar disponibilidade da sala I-1 para o horário 11:00-13:00 (após a reserva das 9-11)
    verif_inicio = datetime(2026, 5, 25, 11, 0)
    verif_fim = datetime(2026, 5, 25, 13, 0)

    disponiveis = gerenciador.obter_salas_disponiveis(data_teste, verif_inicio, verif_fim, lista_salas)

    print(f"\nData: {data_teste.strftime('%d/%m/%Y')} | Horário: {verif_inicio.strftime('%H:%M')} - {verif_fim.strftime('%H:%M')}")
    print("Salas disponíveis:")
    if disponiveis:
        for s in disponiveis:
            print(f"{s}")

    # Verificação específica para a sala I-1
    if indiv1 in disponiveis:
        print(f"\nSala {indiv1.numero_sala} está disponível (correto, pois a reserva termina às 11:00).")
    else:
        print(f"\nSala {indiv1.numero_sala} NÃO está disponível - verificar conflito indevido.")

    # 8. Listar reservas por usuário
    print("\n" + "=" * 60)
    print("RESERVAS POR USUÁRIO")
    print("=" * 60)
    for usuario in usuarios:
        reservas_user = gerenciador.obter_reservas_por_usuario(usuario)
        print(f"\n{usuario}:")
        if reservas_user:
            for r in reservas_user:
                print(f"{r}")
        else:
            print("   Nenhuma reserva")


    reservas_do_dia = gerenciador.obter_reservas_por_data(data_teste)

    if not reservas_do_dia:
        print(f"Nenhuma reserva confirmada para {data_teste.strftime('%d/%m/%Y')}.")
    else:
        print(f"\n=== RELATÓRIO DIÁRIO - {data_teste.strftime('%d/%m/%Y')} ===\n")

        salas_dict = {}

        for r in reservas_do_dia:
            chave = r.sala.numero_sala
            if chave not in salas_dict:
                salas_dict[chave] = []
            salas_dict[chave].append(r)
        
        for num_sala in sorted(salas_dict.keys()):
            print(f"Sala {num_sala}:")
            for r in salas_dict[num_sala]:
                inicio = r.data_hora_inicio.strftime("%H:%M")
                fim = r.data_hora_fim.strftime("%H:%M")
                print(f"  - {inicio} - {fim} : {r.usuario.nome} ({r.usuario.vinculo})")

    print("\n" + "=" * 60)
    print("TESTE CONCLUÍDO!")
    print("=" * 60)

if __name__ == "__main__":
    main()

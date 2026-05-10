from usuario import Professor, Aluno, Externo
from reserva_factory import ReservaFactory
from sala_factory import LaboratorioFactory, EstudoIndividualFactory, EstudoEmGrupoFactory
from estrategia_reserva import PoliticaPrimeiroChegar, PoliticaPrioridadeDocente
from gerenciador_reservas import GerenciadorDeReservas
from datetime import datetime, timedelta

def main():
    print("-"*20)
    print("SISTEMA DE RESERVAS ")
    print("-"*20)

    fabrica_lab = LaboratorioFactory()
    lab1 = fabrica_lab.criar_sala("L-1", capacidade=25, equipamentos=["PCs", "Projetor", "Capela de Exaustão", "Balança de Precisão"])
    lab2 = fabrica_lab.criar_sala("L-2", capacidade=25, equipamentos=["PCs", "Projetor", "Paquímetro", "Réguas", "Galvanômetro"])
    lab3 = fabrica_lab.criar_sala("L-3", capacidade=25, equipamentos=["PCs", "Projetor", "Balança", "Microscópios", "Estufa", "Autoclave"])

    farica_estudoIndividual = EstudoIndividualFactory()
    estudo1 = farica_estudoIndividual.criar_sala("E-1")
    estudo2 = farica_estudoIndividual.criar_sala("E-2")
    estudo3 = farica_estudoIndividual.criar_sala("E-3")

    fabrica_estudoGrupo = EstudoEmGrupoFactory()
    grupo1 = fabrica_estudoGrupo.criar_sala("G-1", capacidade=20, mesas=10, quadros=5)
    grupo2 = fabrica_estudoGrupo.criar_sala("G-2", capacidade=10, mesas=4, quadros=2)
    grupo3 = fabrica_estudoGrupo.criar_sala("G-3", capacidade=5, mesas=2, quadros=1)

    lista_salas = [lab1, lab2, lab3, estudo1, estudo2, estudo3, grupo1, grupo2, grupo3]
    print("Salas Disponíveis:")
    for sala in lista_salas:
        print(f" -> {sala} --> Detalhes: {sala.obter_detalhes()}")


    gerenciador = GerenciadorDeReservas.get_instancia()
    ReservaFactory.definir_politica(PoliticaPrimeiroChegar())
    print("\nPolítica de Reserva Atual: Primeiro a Chegar. Deseja mudar para Prioridade Docente? (s/n)")
    escolha = input().strip().lower()
    if escolha == "s":
        ReservaFactory.definir_politica(PoliticaPrioridadeDocente())
        print("Política de Reserva alterada para Prioridade Docente.")
    
    print("""\nMenu:
          1- Entrar
          2- Sair""")

    op = input("Escolha uma opção: ")
    while op != "2":
        if op == "1":
            nome = input("Digite seu nome: ")
            tipo = input("Você é Aluno, Professor ou Externo? ").strip().lower()
            if tipo == "aluno":
                matricula = input("Digite sua matrícula: ")
                usuario = Aluno(nome, matricula)
                reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)
                if reservas_usuario:
                    print(f"\nBem-vindo de volta, {usuario.nome}!\n")
                    print(f"Suas reservas ativas, {usuario.nome}:")
                    for r in reservas_usuario:
                        print(f" -> {r}")
            elif tipo == "professor":
                identificador = input("Digite seu identificador: ")
                usuario = Professor(nome, identificador)
                reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)
                if reservas_usuario:
                    print(f"\nBem-vindo de volta, {usuario.nome}!\n")
                    print(f"Suas reservas ativas, {usuario.nome}:")
                    for r in reservas_usuario:
                        print(f" -> {r}")
            elif tipo == "externo":
                cpf = input("Digite seu CPF: ")
                usuario = Externo(nome, cpf)
                reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)
                if reservas_usuario:
                    print(f"\nBem-vindo de volta, {usuario.nome}!\n")
                    print(f"Suas reservas ativas, {usuario.nome}:")
                    for r in reservas_usuario:
                        print(f" -> {r}")
            else:
                print("Tipo de usuário inválido. Encerrando.")
                return
        
            if not gerenciador.obter_reservas_por_usuario(usuario):
                print(f"Bem-vindo, {usuario}!")
            
            print("""\nMenu de Ações:
                1- Fazer Reserva
                2- Listar Reservas
                3- Modificar Reserva
                4- Sair""")

            acao = input("Escolha uma ação: ")
            while acao != "4":

                if acao == "1": 

                    numero_sala = input("Digite o número da sala que deseja reservar: ").strip().upper()
                    while numero_sala not in [s.numero_sala for s in lista_salas]:
                        print("Número de sala inválido. Tente novamente.")
                        numero_sala = input("Digite o número da sala que deseja reservar: ").strip().upper()
                    
                    sala_escolhida = next(s for s in lista_salas if s.numero_sala == numero_sala)
                    data_str = input("Digite a data da reserva (dd/mm/yyyy): ")
                    hora_inicio_str = input("Digite a hora de início (HH:MM): ")
                    hora_fim_str = input("Digite a hora de término (HH:MM): ")

                    try:
                        data_reserva = datetime.strptime(data_str, "%d/%m/%Y")
                        hora_inicio = datetime.strptime(hora_inicio_str, "%H:%M")
                        hora_fim = datetime.strptime(hora_fim_str, "%H:%M")
                    except ValueError:
                        print("Formato de data ou hora inválido. Encerrando.")
                        return

                    reserva = ReservaFactory.criar_reserva(usuario, sala_escolhida, data_reserva, hora_inicio, hora_fim)

                    if reserva:
                        print(f"{reserva}")
                    

                elif acao == "2":

                    reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)
                    if reservas_usuario:
                        print(f"Suas reservas ativas, {usuario.nome}:")
                        for r in reservas_usuario:
                            print(f" -> {r}")
                    else:
                        print("Você não tem reservas ativas.")

                elif acao == "3":
                    
                    reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)
                    if not reservas_usuario:
                        print("Você não tem reservas para modificar.")
                    else:
                        print("Suas reservas:")
                        for idx, r in enumerate(reservas_usuario, 1):
                            print(f"{idx}- {r}")
                        escolha = input("Digite o número da reserva que deseja modificar: ")
                        try:
                            idx = int(escolha) - 1
                            if idx < 0 or idx >= len(reservas_usuario):
                                print("Número inválido. Encerrando.")
                                return
                            reserva_selecionada = reservas_usuario[idx]
                            nova_hora_inicio_str = input("Digite a nova hora de início (HH:MM): ")
                            nova_hora_fim_str = input("Digite a nova hora de término (HH:MM): ")
                            nova_hora_inicio = datetime.strptime(nova_hora_inicio_str, "%H:%M")
                            nova_hora_fim = datetime.strptime(nova_hora_fim_str, "%H:%M")
                            ReservaFactory.modificar_reserva(reserva_selecionada, reserva_selecionada.data_reserva, nova_hora_inicio, nova_hora_fim)
                            print(f"Suas reservas ativas, {usuario.nome}:")
                            reservas_modificadas_usuario = gerenciador.obter_reservas_por_usuario(usuario)
                            for r in reservas_modificadas_usuario:
                                print(f" -> {r}")
                        except ValueError:
                            print("Entrada inválida. Encerrando.")
                            return

                elif acao == "4":
                    return
                
                else:
                    print("Ação inválida. Tente novamente.")

                acao = input("Escolha uma ação: ")

        if op == "2":

            print("Encerrando o sistema. Até mais!")
            return

        print("""\nMenu:
          1- Entrar
          2- Sair""")
        op = input("Escolha uma opção: ")
    

if __name__ == "__main__":
    main()
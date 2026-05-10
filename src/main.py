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
    2- Relatório Diário
    3- Sair""")

    op = input("Escolha uma opção: ")
    while op != "3":

        if op == "1":

            nome = input("Digite seu nome: ")
            tipo = input("Você é Aluno, Professor ou Visitante? ").strip().lower()

            if tipo == "aluno":
                matricula = input("Digite sua matrícula: ")
                usuario = Aluno(nome, matricula)

                reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)

                if reservas_usuario:
                    print(f"\nBem-vindo de volta, {usuario.nome}!\n")
            
            elif tipo == "professor":
                identificador = input("Digite seu identificador: ")
                usuario = Professor(nome, identificador)

                reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)

                if reservas_usuario:
                    print(f"\nBem-vindo de volta, {usuario.nome}!\n")
                   
            elif tipo == "visitante":
                cpf = input("Digite seu CPF: ")
                usuario = Externo(nome, cpf)

                reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)

                if reservas_usuario:
                    print(f"\nBem-vindo de volta, {usuario.nome}!\n")

            else:
                print("Tipo de usuário inválido. Encerrando.")
                return
        
            if not gerenciador.obter_reservas_por_usuario(usuario):
                print(f"Bem-vindo, {usuario}!")
            
            print("""\nMenu de Ações:
            1- Ver salas disponíveis
            2- Fazer reserva
            3- Listar minhas reservas
            4- Modificar reserva
            5- Cancelar reserva
            6- Sair""")

            acao = input("\nEscolha uma ação: ")

            while acao != "6":

                if acao == "1":

                    data_str = input("Digite a data (dd/mm/yyyy): ")
                    hora_ini_str = input("Hora início (HH:MM): ")
                    hora_fim_str = input("Hora fim (HH:MM): ")

                    try:
                        data = datetime.strptime(data_str, "%d/%m/%Y")
                        hora_ini = datetime.strptime(hora_ini_str, "%H:%M")
                        hora_fim = datetime.strptime(hora_fim_str, "%H:%M")
                    except:
                        print("Formato inválido.")
                        continue

                    disponiveis = gerenciador.obter_salas_disponiveis(data, hora_ini, hora_fim, lista_salas)

                    if disponiveis:
                        print(f"Salas disponíveis em {data_str} das {hora_ini_str} às {hora_fim_str}:")
                        for s in disponiveis:
                            print(f" - {s} --> {s.obter_detalhes()}")
                    else:
                        print("Nenhuma sala disponível neste horário.")

                # FAZER RESERVA
                if acao == "2": 

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
                    
                    inicio_real = datetime(data_reserva.year, data_reserva.month, data_reserva.day, hora_inicio.hour, hora_inicio.minute)
                    fim_real = datetime(data_reserva.year, data_reserva.month, data_reserva.day, hora_fim.hour, hora_fim.minute)

                    reserva = ReservaFactory.criar_reserva(usuario, sala_escolhida, inicio_real, fim_real)

                    if reserva:
                        print(f"{reserva}")
                    
                # LISTAR RESERVAS DO USUÁRIO
                elif acao == "3":

                    reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)

                    if reservas_usuario:
                        print(f"Suas reservas ativas, {usuario.nome}:")
                        for r in reservas_usuario:
                            print(f" -> {r}")

                    else:
                        print("Você não tem reservas ativas.")

                # MODIFICAR RESERVA
                elif acao == "4":
                    
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
                            nova_data_str = input("Digite a nova data da reserva (dd/mm/yyyy): ")
                            nova_hora_inicio_str = input("Digite a nova hora de início (HH:MM): ")
                            nova_hora_fim_str = input("Digite a nova hora de término (HH:MM): ")

                            nova_data = datetime.strptime(nova_data_str, "%d/%m/%Y")
                            nova_hora_inicio = datetime.strptime(nova_hora_inicio_str, "%H:%M")
                            nova_hora_fim = datetime.strptime(nova_hora_fim_str, "%H:%M")

                            novo_inicio_real = datetime(nova_data.year, nova_data.month, nova_data.day, nova_hora_inicio.hour, nova_hora_inicio.minute)
                            novo_fim_real = datetime(nova_data.year, nova_data.month, nova_data.day, nova_hora_fim.hour, nova_hora_fim.minute)
                            
                            ReservaFactory.modificar_reserva(reserva_selecionada, novo_inicio_real, novo_fim_real)

                            reservas_modificadas_usuario = gerenciador.obter_reservas_por_usuario(usuario)

                            print(f"Suas reservas ativas, {usuario.nome}:")
                            for r in reservas_modificadas_usuario:
                                print(f" -> {r}")

                        except ValueError:
                            print("Entrada inválida. Encerrando.")
                            return

                # CANCELAR RESERVA
                elif acao == "5":
                    reservas_usuario = gerenciador.obter_reservas_por_usuario(usuario)

                    if not reservas_usuario:
                        print("Você não tem reservas para cancelar.")

                    else:
                        print("Suas reservas:")
                        for idx, r in enumerate(reservas_usuario, 1):
                            print(f"{idx}- {r}")

                        escolha = input("Digite o número da reserva que deseja cancelar: ")

                        try:
                            idx = int(escolha) - 1
                            if idx < 0 or idx >= len(reservas_usuario):
                                print("Número inválido. Encerrando.")
                                return
                            
                            reserva_selecionada = reservas_usuario[idx]
                            reserva_selecionada.cancelar()
                            gerenciador.remover_reserva(reserva_selecionada)
                            print(f"Reserva cancelada com sucesso.")

                            reservas_canceladas_usuario = gerenciador.obter_reservas_por_usuario(usuario)
                            print(f"Suas reservas ativas, {usuario.nome}:")
                            for r in reservas_canceladas_usuario:
                                print(f" -> {r}")

                        except ValueError:
                            print("Entrada inválida. Encerrando.")
                            return
                        
                elif acao == "6":
                    break

                print("""\nMenu de Ações:
                1- Ver salas disponíveis
                2- Fazer reserva
                3- Listar minhas reservas
                4- Modificar reserva
                5- Cancelar reserva
                6- Sair""")
                acao = input("Escolha uma ação: ")

        if op == "2":

            data_str = input("Digite a data do relatório (dd/mm/yyyy): ")
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y")
            except:
                print("Formato inválido.")
                continue

            reservas_do_dia = gerenciador.obter_reservas_por_data(data)

            if not reservas_do_dia:
                print(f"Nenhuma reserva confirmada para {data_str}.")
            else:
                print(f"\n=== RELATÓRIO DIÁRIO - {data_str} ===\n")

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
        
        if op == "3":
            print("Encerrando o sistema. Até mais!")
            return

        print("""\nMenu:
          1- Entrar
          2- Relatório Diário
          3- Sair""")
        op = input("Escolha uma opção: ")
    

if __name__ == "__main__":
    main()

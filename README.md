# 🏫 Sistema de Reserva de Salas de Estudo

Este projeto implementa um sistema para reserva de salas, aplicando os padrões de projeto **Factory Method**, **Strategy**, **Observer** e **Singleton**. O usuário é capaz de criar uma "conta" no sistema gerenciador de reservas, e então no menu é possível escolher entre 6 opções, sendo elas, ver as salas disponíveis para uma data e horários específicos, fazer uma reserva, listas as suas reservas, modificar reserva, cancelar reserva ou sair. 

## 📦 Estrutura do Projeto

docs/

└── diagrama_reserva_salas.pdf # Diagrama UML do projeto

src/

├── main.py     # Ponto de entrada e menu interativo  \\\
├── sala.py   # Classes Sala, Laboratorio, EstudoIndividual, EstudoEmGrupo\\\
├── sala_factory.py   # Factories para criação de salas\\\
├── usuario.py   # Usuario, Professor, Aluno, Externo (observers)\\\
├── reserva.py   # Reserva (subject) – notificações push/pull\\\
├── observer.py   # Interfaces Observer e Subject\\\
├── gerenciador_reservas.py   # Singleton – repositório e consultas\\\
├── estrategia_reserva.py   # Strategy – políticas de gerenciamento de conflito\\\
├── teste_prioridade_docente.py   # arquivo teste com a prioridade para os professores, com a criação de usuários e teste de funcionalidades\\\
├── teste_primeiro_chegar.py  # arquivo teste com a prioridade de primeiro a chegar, com a criação de usuários e teste de funcionalidades\\\
├── reserva_proxy.py   # controle de acessos, limite de reservas
└── reserva_factory.py   # Criação/modificação de reservas com política


## ✔️ Requisitos atendidos pelo sistema

- RF‑01 –> Listar salas disponíveis em um intervalo de datas

- RF‑02 –> Criar, modificar e cancelar reserva

- RF‑03 –> Detectar e impedir colisões (via Strategy)

- RF‑04 –> Notificações para usuários envolvidos

- RF‑05 –> Relatório diário com reservas confirmadas de cada sala

## 📚 Exemplo de fluxo rápido

1. Inicie o programa e escolha a política de reserva.
2. Entre como aluno → crie uma reserva → liste suas reservas.
3. Modifique a reserva (nova data/hora) – veja a notificação push.
4. Cancele a reserva – veja a notificação pull.
5. Gere o relatório diário (opção 2 do menu principal) para uma data.
6. Teste a política “Prioridade Docente” – um professor deve sobrescrever reserva de aluno.

## 🚀 Como Executar

1. **Clone o repositório**
2. Navegue para a pasta `src`
3. Execute o programa:

```bash
python main.py
```

## 👥 Autores

- Anna Clara Medina Roissmann 
- Letícia Vieira
- Renan Kohatsu

---

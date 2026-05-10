# 🏫 Sistema de Reserva de Salas de Estudo

Este projeto implementa um sistema para reserva de salas em um campus universitário, aplicando os padrões de projeto **Factory Method**, **Strategy**, **Observer** e **Singleton**. Atende aos requisitos funcionais de listagem de disponibilidade, criação/modificação/cancelamento de reservas, detecção de conflitos, notificações push/pull e relatório diário.

---

## 👥 Autores

- [Anna Clara Medina Roissmann]  
- [Nicolas de Mello Freitas]

---

## 📦 Estrutura do Projeto

docs/
├── diagrama_reserva_salas.pdf # Diagrama UML do projeto

src/
├── main.py # Ponto de entrada e menu interativo
├── sala.py # Classes Sala, Laboratorio, EstudoIndividual eEstudoEmGrupo
├── sala_factory.py # Factories para criação de salas
├── usuario.py # Usuario, Professor, Aluno, Externo (observers)
├── reserva.py # Reserva (subject) – notificações push/pull
├── observer.py # Interfaces Observer e Subject
├── gerenciador_reservas.py # Singleton – repositório e consultas
|── estrategia_reserva.py # Strategy – políticas de gerenciamento de conflito
├── reserva_factory.py # Criação/modificação de reservas com política


## 🚀 Como Executar

1. **Clone o repositório**
2. Navegue para a pasta `src`
2. Certifique-se de ter **Python 3.7+** instalado.
3. Execute o programa:

```bash
python main.py

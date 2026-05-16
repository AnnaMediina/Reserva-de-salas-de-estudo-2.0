# Proxy de Controle de Reservas

## Objetivo

O padrão de projeto **Proxy** foi utilizado para controlar o acesso à criação de reservas no sistema.

As regras implementadas incluem:

- cada usuário pode possuir no máximo **3 reservas ativas simultaneamente**.

---

# Problema

Antes da implementação do Proxy, qualquer parte do sistema podia criar reservas diretamente utilizando:

```python
ReservaFactory.criar_reserva(...)
```

Isso fazia com que regras de acesso e limites de uso ficassem espalhadas pelo sistema ou misturadas à lógica da própria reserva.

---

# Solução

Foi criada a classe:

```python
ReservaProxy
```

Ela atua como intermediária entre o usuário e a `ReservaFactory`.

Agora, toda criação de reserva passa primeiro pelo Proxy:

```python
ReservaProxy.criar_reserva(...)
```

O Proxy verifica:

- quantidade de reservas ativas do usuário.

Somente após essas validações a Factory é chamada.

---

# Benefícios

## Separação de responsabilidades

- `Reserva` → representa a reserva;
- `ReservaFactory` → cria reservas;
- `ReservaProxy` → controla limite de reservas.

---

# Conclusão

A utilização do padrão Proxy permitiu adicionar regras limite de reservas sem modificar diretamente a classe `Reserva` ou a `ReservaFactory`, mantendo o sistema mais organizado, modular e aderente aos princípios de projeto.


# Proxy de Controle de Reservas com Cache

# Antes (somente controle de acesso)
O ReservaProxy atuava apenas como um "porteiro": verificava se o usuário tinha permissão para reservar (bloqueando visitantes) e se ele ainda não havia atingido o limite de 3 reservas ativas. Se passasse nas duas verificações, delegava a criação ao ReservaReal. Fora isso, o Proxy não fazia mais nada — toda vez que o sistema precisava listar as reservas de um usuário ou de uma sala, ia direto ao GerenciadorDeReservas recalcular tudo do zero.

# Depois (controle de acesso + cache)

O Proxy ganhou uma segunda responsabilidade: evitar trabalho repetido. Foi adicionado um dicionário de classe _cache que armazena o resultado das listagens junto com o momento em que foram salvas. Antes de ir buscar os dados, o Proxy verifica se já existe uma entrada recente (dentro do TTL de 60 segundos) para aquela chave — se sim, devolve o resultado armazenado direto (HIT), se não, busca os dados reais e os salva no cache para a próxima consulta (MISS).
Para garantir que o cache nunca devolva dados desatualizados, qualquer operação de escrita — criar, cancelar ou modificar uma reserva — invalida automaticamente as entradas relacionadas àquela sala e àquele usuário.
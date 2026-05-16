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
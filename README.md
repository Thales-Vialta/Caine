# Caine

**Caine** é um sistema simples de gerenciamento de dispositivos e reservas voltado para instituições de ensino ou organizações que desejam controlar o uso de equipamentos como notebooks, tablets, etc.

---

## Objetivo

O projeto **Caine** foi desenvolvido com os seguintes propósitos:

* Aplicar conhecimentos em **Python** com foco em modularização e reutilização de código.
* Utilizar **SQLite** como banco de dados para persistência de informações.
* Implementar menus interativos baseados em texto para simular um sistema real de gerenciamento de TI.
* Praticar o desenvolvimento de sistemas orientados à solução de problemas reais em instituições.

---

## Como rodar o projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/caine.git
   cd caine
   ```

2. **(Opcional) Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   ```

3. **Execute o sistema principal:**

   ```bash
   python main.py
   ```

---

## Funcionalidades

* **Instituições:**

  * Cadastro e verificação de instituições por nome e CEP.

* **Dispositivos:**

  * Cadastro em série com marca/modelo/status.
  * Listagem em formato de matriz.
  * Atualização de status (ativo/inativo).
  * Exclusão de dispositivos.

* **Reservas:**

  * Criação de reservas associadas a dispositivos.
  * Listagem completa de reservas com informações detalhadas.

---

## Aprendizados

Durante o desenvolvimento deste sistema, foram reforçados os seguintes aprendizados:

* Conexão e manipulação de banco de dados SQLite com Python.
* Organização de um sistema por módulos (`main.py`, `database.py`, `dispositivos.py`, `reserva.py`, etc).
* Lógica condicional e laços de repetição para controle de menus.
* Manipulação de entrada/saída de dados no terminal.
* Uso prático de funções, listas, e controle de fluxo com tratamento de erros.

---

## Requisitos

* Python 3.10+
* Biblioteca padrão (`sqlite3`, `os`, etc)

---


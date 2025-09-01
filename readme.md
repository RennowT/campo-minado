# ⛏️ Campo Minado em Python

Este é um projeto de **Campo Minado (Minesweeper)** implementado em **Python**, utilizando **orientação a objetos**.  
O jogo roda no terminal e permite revelar células, marcar bandeiras e vencer ao descobrir todas as posições seguras.

---

## 🚀 Como Rodar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/campo-minado.git
cd campo-minado
```

### 2. Instalar dependências

#### Usando **pip**

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

#### Usando **poetry**

```bash
poetry install
```

### 3. Executar o jogo

```bash
python -m src.main
```

---

## 🎮 Como Jogar

* O tabuleiro é exibido no terminal.
* Cada célula pode estar:

  * `?` → não revelada
  * `F` → marcada com bandeira
  * `*` → mina (quando revelada)
  * `0-8` → número de minas vizinhas

### Comandos no jogo

1. Escolha uma **ação**:

   * `reveal` → revelar célula
   * `flag` → marcar/desmarcar bandeira
2. Informe a **linha** e a **coluna**.

Exemplo:

```txt
Ação (reveal/flag): reveal
Linha: 1
Coluna: 3
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **colorama** (opcional, para colorir saída do terminal)

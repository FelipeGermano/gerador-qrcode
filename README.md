### README: Gerador de QR Code em Python com Interface Gráfica

---

## 📋 Descrição

Este é um aplicativo simples para **gerar QR Codes** a partir de texto, links, telefones ou e-mails fornecidos pelo usuário. Ele utiliza a biblioteca `tkinter` para a interface gráfica e `qrcode` para a geração do QR Code.

---

## 🖥️ Recursos

- Entrada de texto para o conteúdo do QR Code.
- Visualização do QR Code gerado.
- Salvar o QR Code em formato PNG no computador.
- Interface gráfica amigável e fácil de usar.

---

## 📂 Estrutura do Projeto

```
qr_code_generator/
│
├── qr_code_generator.py    # Código principal do aplicativo
├── requirements.txt        # Arquivo de dependências do projeto
└── README.md               # Documentação do projeto
```

---

## 🚀 Pré-requisitos

1. **Python 3.7 ou superior**
2. Instalar as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/FelipeGermano/gerador-qrcode.git
   cd qr_code_generator
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Usar

1. **Execute o aplicativo**:
   ```bash
   python qr_code_generator.py
   ```

2. **Passos no aplicativo**:
   - Digite um texto, link, telefone ou e-mail no campo de entrada.
   - Clique em "Gerar QR Code" para visualizar o código.
   - Clique em "Salvar QR Code" para salvar o QR Code como um arquivo PNG no seu computador.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **tkinter**: Para criar a interface gráfica.
- **qrcode**: Para gerar os QR Codes.
- **Pillow (PIL)**: Para manipular e exibir imagens.

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adicionando nova feature'
   ```
4. Faça um push para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.
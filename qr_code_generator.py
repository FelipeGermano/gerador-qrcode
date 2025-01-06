import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk


def generate_qr():
    # Obter o texto inserido pelo usuário
    data = entry.get().strip()
    
    if not data:
        messagebox.showerror("Erro", "Por favor, insira algum texto, link, telefone ou e-mail.")
        return

    # Gerar o QR Code
    qr = qrcode.QRCode(
        version=1,  # Controle do tamanho do QR Code (1 = menor, 40 = maior)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Criar a imagem do QR Code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.thumbnail((300, 300))  # Redimensionar a imagem para caber no preview

    # Atualizar a imagem no UI
    qr_image_tk = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image_tk)
    qr_label.image = qr_image_tk

    # Armazenar a imagem para salvar posteriormente
    qr_label.qr_image = qr_image


def save_qr():
    if not hasattr(qr_label, "qr_image"):
        messagebox.showerror("Erro", "Nenhum QR Code foi gerado.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")],
    )
    if file_path:
        qr_label.qr_image.save(file_path)
        messagebox.showinfo("Salvo", f"QR Code salvo em: {file_path}")


# Configuração da Janela Principal
app = tk.Tk()
app.title("Gerador de QR Code")
app.geometry("400x500")
app.resizable(False, False)

# Título
title_label = tk.Label(app, text="Gerador de QR Code", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Entrada de Dados
entry = tk.Entry(app, font=("Arial", 12), width=30)
entry.pack(pady=10)

# Botão para Gerar QR Code
generate_button = tk.Button(app, text="Gerar QR Code", font=("Arial", 12), command=generate_qr)
generate_button.pack(pady=10)

# Botão para Salvar QR Code
save_button = tk.Button(app, text="Salvar QR Code", font=("Arial", 12), command=save_qr)
save_button.pack(pady=5)

# Espaço para Mostrar o QR Code
qr_label = tk.Label(app)
qr_label.pack(pady=20)

# Rodar o Aplicativo
app.mainloop()

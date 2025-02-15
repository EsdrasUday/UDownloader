import customtkinter as ctk
import backend
import os
import sys
from tkinter import filedialog
from PIL import Image

# Configuração do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#  Cores do Ubuntu
roxo = "#2C001E"
laranja = "#E95420"
oran_claro = "#D75F20"
branco = "#FFFFFF"
sec_text = "#D3D3D3"

# Criando a janela principal
app = ctk.CTk()
app.title("UDownloader")
app.geometry("420x460")
app.minsize(width=420,height=460)
app.configure(fg_color=roxo)

# Definir ícone baseado no sistema operacional
if sys.platform == "win32":
    try:
        app.iconbitmap("IMG/logo.ico")
    except:
        print("Ícone não encontrado, continuando sem ícone...")

#  chamada para atualizar status
def atualizar_status(mensagem, cor):
    status_label.configure(text=mensagem, text_color=cor)

#  chamada para exibir/esconder barra de progresso
def atualizar_progresso(ativar):
    if ativar:
        progress_bar.pack(pady=10)
        progress_bar.start()
    else:
        progress_bar.pack_forget()
        progress_bar.stop()

#  chamada para exibir o botão "Mostrar na Pasta"
def ativar_botao_pasta(ativar):
    if ativar:
        mostrar_pasta_button.pack(pady=5)
    else:
        mostrar_pasta_button.pack_forget()

#  Função para escolher pasta
def escolher_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        backend.escolher_pasta(pasta)
        pasta_label.configure(text=f"Pasta: {pasta}", text_color="green")
    else:
        pasta_label.configure(text="Nenhuma pasta selecionada", text_color="red")

#  Ícone no topo
try:
    imagem = ctk.CTkImage(light_image=Image.open("IMG/Logo.png"), size=(110, 110))
    label_imagem = ctk.CTkLabel(app, image=imagem, text="")
    label_imagem.pack(pady=5)
except:
    print("Imagem não encontrada")

#  Título
title_label = ctk.CTkLabel(app, text="Downloader de Vídeos do YouTube", font=("Arial", 16, "bold"), text_color=branco)
title_label.pack(pady=5)

#  Campo de entrada
entry_url = ctk.CTkEntry(app, width=350, placeholder_text="Cole o link do YouTube aqui", fg_color="#4E002F", text_color=branco)
entry_url.pack(pady=5)

#  Frame para alinhar os botões
frame_opcoes = ctk.CTkFrame(app, fg_color="transparent",width=350)
frame_opcoes.pack(pady=5)

#  Qualidade e Escolher Pasta (lado a lado)
qualidade_var = ctk.StringVar(value="Melhor Qualidade")
qualidade_menu = ctk.CTkOptionMenu(frame_opcoes, variable=qualidade_var,dropdown_hover_color=oran_claro,button_hover_color=laranja,button_color="#b33205", values=list(backend.QUALIDADE_OPCOES.keys()), fg_color=laranja, text_color=branco)
qualidade_menu.pack(side="left", expand=True, padx=5, pady=5)

pasta_button = ctk.CTkButton(frame_opcoes, text="Escolher Pasta", command=escolher_pasta, fg_color=laranja,hover_color='#b33205', text_color=branco)
pasta_button.pack(side="right", expand=True, padx=5, pady=5)

#  Label da Pasta Selecionada
pasta_label = ctk.CTkLabel(app, text="Nenhuma pasta selecionada", font=("Arial", 12, "bold"), text_color="red")
pasta_label.pack(pady=5)

#  Botão de Download
download_button = ctk.CTkButton(app, text="Baixar",command=lambda: backend.baixar_midia(entry_url.get(), qualidade_var.get(),
    atualizar_status, atualizar_progresso, ativar_botao_pasta),hover_color="#b33205",fg_color=laranja, text_color=branco)
download_button.pack(pady=5)

#  Botão para abrir a pasta do arquivo baixado
mostrar_pasta_button = ctk.CTkButton(app, text="Abrir Arquivo", command=lambda: backend.mostrar_na_pasta(atualizar_status), fg_color="#444444", text_color=branco)
mostrar_pasta_button.pack(pady=5, fill="x")
mostrar_pasta_button.pack_forget()

#  Barra de Progresso
progress_bar = ctk.CTkProgressBar(app, mode="determinate", fg_color="#4E002F", progress_color=laranja)
progress_bar.pack_forget()

#  Status
status_label = ctk.CTkLabel(app, text="", font=("Arial", 12, "bold"), text_color=sec_text)
status_label.pack(pady=5)

Dev = ctk.CTkLabel(app, text="Developer Esdras Uday Da Silveira Maracajá", font=("Roboto", 8, "bold"), text_color="grey")
Dev.pack(side='bottom',pady=1)

#  Executando a aplicação
app.mainloop()

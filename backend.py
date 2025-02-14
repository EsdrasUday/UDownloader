import yt_dlp
import os
import subprocess
import sys
import threading


# Dicionário de qualidade dos vídeos
QUALIDADE_OPCOES = {
    "Melhor Qualidade": "bestvideo+bestaudio",
    "Qualidade Média": "best",
    "Qualidade Baixa": "worst",
    "Somente Áudio": "bestaudio"
}

# Variáveis globais para o caminho do arquivo baixado
pasta_destino = ""
ultimo_arquivo = ""

def escolher_pasta(pasta):
    """Define a pasta onde os arquivos serão salvos."""
    global pasta_destino
    pasta_destino = pasta

def baixar_midia(url, qualidade_pt, callback_status, callback_progress, callback_final):
    """Baixa o vídeo do YouTube e chama os callbacks para atualizar a interface."""
    global ultimo_arquivo

    if not url:
        callback_status("⚠️ Insira um link do YouTube!", "red") # Para os símbolos fui atras de sites unicodes.
        return
    if not pasta_destino:
        callback_status("⚠️ Escolha uma pasta!", "red")
        return
    
    qualidade = QUALIDADE_OPCOES.get(qualidade_pt, "best")

    callback_status("📥 Baixando...", "#E95420")  # Atualiza status
    callback_progress(True)  # Exibe barra de progresso

    def download():
        global ultimo_arquivo
        try:
            ydl_opts = {
                'format': qualidade,
                'outtmpl': os.path.join(pasta_destino, "%(title)s.%(ext)s")
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                titulo = info.get("title", "arquivo_desconhecido")
                ext = info.get("ext", "mp4")
                ultimo_arquivo = os.path.join(pasta_destino, f"{titulo}.{ext}")

            callback_status("✅ Download concluído!", "green")
            callback_final(True)  # Exibe botão "Mostrar Pasta"

        except Exception as e:
            callback_status(f"❌ Erro: {e}", "red")

        callback_progress(False)  # Esconde barra de progresso

    threading.Thread(target=download).start()

def mostrar_na_pasta(callback_status):
    """Abre o último arquivo salvo após o download."""
    if os.path.exists(ultimo_arquivo):
        if sys.platform == "win32":
            os.startfile(os.path.abspath(ultimo_arquivo))
        else:  
            subprocess.run(["xdg-open", os.path.abspath(ultimo_arquivo)])
    else:
        callback_status("⚠️ Arquivo não encontrado!", "red")

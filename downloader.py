import yt_dlp
import tkinter as tk
from tkinter import messagebox, ttk


def download_video():
    url = url_entry.get().strip()
    media_type = media_var.get()
    quality = quality_var.get().strip()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return

    ydl_opts = {}

    if media_type == "Áudio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
    else:
        if quality == "Melhor Qualidade":
            video_format = 'bestvideo+bestaudio/best'
        else:
            try:
                height = int(quality)
                video_format = f'bestvideo[height<={height}]+bestaudio/best[height<={height}]'
            except ValueError:
                video_format = 'bestvideo+bestaudio/best'

        ydl_opts = {
        'ffmpeg_location': './ffmpeg',  # Usa o FFmpeg embutido no yt-dlp
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha no download: {e}")


# Criando a interface gráfica
root = tk.Tk()
root.title("Downloader de Vídeos")
root.geometry("400x300")

tk.Label(root, text="Insira a URL do vídeo:", font=("Arial", 12)).pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Label(root, text="Escolha o tipo de mídia:", font=("Arial", 12)).pack(pady=5)
media_var = tk.StringVar(value="Vídeo")
tk.Radiobutton(root, text="Vídeo", variable=media_var, value="Vídeo").pack()
tk.Radiobutton(root, text="Áudio", variable=media_var, value="Áudio").pack()

tk.Label(root, text="Escolha a qualidade:", font=("Arial", 12)).pack(pady=5)
quality_var = ttk.Combobox(root, values=["Melhor Qualidade", "1080", "720", "480", "360", "240"])
quality_var.pack(pady=5)
quality_var.set("Melhor Qualidade")

tk.Button(root, text="Baixar", command=download_video, font=("Arial", 12), bg="green", fg="white").pack(pady=20)

root.mainloop()

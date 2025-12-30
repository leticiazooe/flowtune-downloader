import customtkinter as ctk
from yt_dlp import YoutubeDL
import threading
import os

class YoutubeDownloader:
    def __init__(self):
        # Configurações Iniciais
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        self.root.title("FlowTune Downloader")
        self.root.geometry("700x500")

        # Layout de Grade
        self.root.grid_columnconfigure(0, weight=1)

        # Título e Link
        ctk.CTkLabel(self.root, text="Link da Playlist ou Vídeo:", font=("Arial", 16, "bold")).pack(pady=(20, 5))
        self.url_entry = ctk.CTkEntry(self.root, width=500, placeholder_text="Cole o link do YouTube aqui...")
        self.url_entry.pack(pady=10)

        # Escolha de Formato
        self.format_choice = ctk.CTkSegmentedButton(self.root, values=["MP4 (Vídeo)", "MP3 (Áudio)"])
        self.format_choice.set("MP3 (Áudio)")
        self.format_choice.pack(pady=10)

        # Botão de Download (Verde)
        self.download_btn = ctk.CTkButton(self.root, text="Iniciar Download", 
                                         fg_color="#28a745", hover_color="#218838",
                                         font=("Arial", 14, "bold"),
                                         command=self.start_thread)
        self.download_btn.pack(pady=15)

        # Status
        self.status = ctk.CTkLabel(self.root, text="Aguardando...", text_color="white")
        self.status.pack(pady=2)

        # Painel de Histórico (Músicas Baixadas)
        ctk.CTkLabel(self.root, text="Histórico de Downloads:", font=("Arial", 13, "bold")).pack(pady=(15, 0))
        self.history_box = ctk.CTkTextbox(self.root, width=550, height=180, activate_scrollbars=True)
        self.history_box.pack(pady=10)
        self.history_box.configure(state="disabled")

    def progress_hook(self, d):
        """Atualiza o histórico apenas quando o download termina"""
        if d['status'] == 'finished':
            filename = os.path.basename(d.get('filename', 'Arquivo desconhecido'))
            self.root.after(0, lambda: self.add_to_history(filename))

    def add_to_history(self, filename):
        self.history_box.configure(state="normal")
        self.history_box.insert("end", f"✔️ {filename}\n")
        self.history_box.configure(state="disabled")
        self.history_box.see("end")

    def download(self):
        url = self.url_entry.get().strip()
        formato = self.format_choice.get()
        
        if not url or not url.startswith("http"):
            self.status.configure(text="❌ Erro: Link inválido!", text_color="#ff4d4d")
            return

        pasta_atual = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(os.path.expanduser("~"), "Downloads", "Musicas_Youtube")

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        ydl_opts = {
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'ffmpeg_location': pasta_atual,
            'noplaylist': False,
            'progress_hooks': [self.progress_hook], 
        }

        if "MP3" in formato:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            ydl_opts.update({
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
            })

        try:
            self.status.configure(text="⏳ Baixando...", text_color="#ffcc00")
            self.download_btn.configure(state="disabled")
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            self.status.configure(text="✅ Download concluído!", text_color="#2eb82e")
        except Exception as e:
            print(f"ERRO: {str(e)}")
            self.status.configure(text="❌ Erro no processamento.", text_color="#ff4d4d")
        finally:
            self.download_btn.configure(state="normal")

    def start_thread(self):
        thread = threading.Thread(target=self.download, daemon=True)
        thread.start()

if __name__ == "__main__":
    app = YoutubeDownloader()
    app.root.mainloop()
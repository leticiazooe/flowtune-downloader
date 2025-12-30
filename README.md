
# FlowTune Downloader

Uma breve descrição sobre o que esse projeto faz e para quem ele é

O FlowTune é uma ferramenta desktop de alto desempenho para baixar vídeos e playlists completas do YouTube com facilidade. Desenvolvido em Python, ele oferece uma experiência visual moderna e feedback em tempo real sobre o status dos seus downloads.

## Programa:

![App Screenshot](https://i.imgur.com/QWWpKua.png)

![App Screenshot](https://i.imgur.com/6KmVADq.png)


## Autores

- [@leticiazooe](https://www.github.com/leticiazooe)


# 
# Funcionalidades
Download em Lote: Insira o link de uma playlist e o app processará todos os vídeos automaticamente.

Conversão Inteligente: Escolha entre MP3 (Áudio) de alta fidelidade ou MP4 (Vídeo).

Barra de Progresso Dinâmica: Acompanhe a porcentagem exata e o progresso total da playlist.

Histórico de Sessão: Painel que lista todos os arquivos baixados com sucesso.

Interface Non-Blocking: Graças ao uso de Threading, você pode continuar interagindo com o app enquanto o download acontece no background.

#
# 🚀 Instalação e Configuração




## Clonar o Repositório

Abra o seu terminal ou prompt de comando e execute:


```bash
  git clone https://github.com/leticiazooe/flowtune-downloader.git
```

## Instalar Dependências
```bash
 pip install customtkinter yt-dlp
```

## Requisito do Sistema (FFmpeg)
Para converter áudios e unir vídeos em HD, o FFmpeg é necessário:

Windows: Baixe o ffmpeg.exe e coloque-o na raiz da pasta do projeto.

Linux/macOS: Instale via terminal (sudo apt install ffmpeg ou brew install ffmpeg).

# 
# Como usar

1. Inicie o Aplicativo
```bash
python main.py
```
2. Insira o Link: Cole a URL do vídeo ou da playlist do YouTube no campo indicado.

3. Selecione o Formato: Clique no botão de áudio ou vídeo.

4. Baixe: Clique em Iniciar Download.

5. Destino: Seus arquivos estarão em Downloads/Musicas_Youtube.




## Stack utilizada

**Linguagem**: Python

**Interface Gráfica (GUI)**: CustomTkinter

**Motor de Download:** yt-dlp

**Processamento de Mídia**: FFmpeg

**Concorrência:** Threading (Multithreading)


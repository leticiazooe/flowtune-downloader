# FlowTune Downloader

> Aplicação desktop em Python para baixar vídeos e playlists em MP3 ou MP4 utilizando yt-dlp e FFmpeg.

## Sobre o projeto

O **FlowTune Downloader** oferece uma interface gráfica simples para processar links de vídeos ou playlists. O usuário escolhe entre áudio MP3 e vídeo MP4, inicia o download e acompanha pela interface quando cada arquivo termina de ser processado.

A aplicação executa o trabalho em uma thread separada, evitando que a janela principal fique totalmente bloqueada durante o download.

## Interface

![FlowTune Downloader](https://i.imgur.com/QWWpKua.png)

![FlowTune Downloader](https://i.imgur.com/6KmVADq.png)

## Funcionalidades identificadas

- entrada de link de vídeo ou playlist;
- validação básica da URL;
- suporte a playlists (`noplaylist=False`);
- opção MP3;
- extração de áudio com qualidade configurada em 192 kbps;
- opção MP4;
- download de melhor vídeo + melhor áudio disponível;
- merge para MP4 através do FFmpeg;
- histórico dos arquivos concluídos na sessão;
- status visual de aguardando, baixando, concluído ou erro;
- execução do download em thread daemon;
- criação automática da pasta `Downloads/Musicas_Youtube`.

## Fluxo

```text
URL de vídeo ou playlist
          ↓
Escolha do formato
    ├── MP3
    └── MP4
          ↓
yt-dlp
          ↓
FFmpeg
          ↓
Downloads/Musicas_Youtube
          ↓
Histórico da sessão
```

## Tecnologias

- Python 3
- CustomTkinter
- yt-dlp
- FFmpeg
- threading
- os

## Estrutura principal

```text
flowtune-downloader/
├── main.py
└── README.md
```

O repositório pode também conter o executável do FFmpeg ou outros arquivos auxiliares utilizados durante o processamento.

## Instalação

```bash
git clone https://github.com/leticiazooe/flowtune-downloader.git
cd flowtune-downloader
python -m venv .venv
```

No Windows:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install customtkinter yt-dlp
```

A versão atual configura `ffmpeg_location` como a pasta onde está `main.py`. Portanto, disponibilize o FFmpeg nesse local ou adapte a configuração ao ambiente.

Execute:

```powershell
python .\main.py
```

## Como usar

1. cole a URL do vídeo ou playlist;
2. escolha MP3 ou MP4;
3. clique em **Iniciar Download**;
4. acompanhe o status da operação;
5. consulte no painel de histórico os itens concluídos;
6. os arquivos serão armazenados em `Downloads/Musicas_Youtube`.

## Comportamento dos formatos

### MP3

A aplicação usa:

```text
bestaudio/best
```

e depois executa `FFmpegExtractAudio`, configurado para MP3 em 192 kbps.

### MP4

A aplicação solicita:

```text
bestvideo+bestaudio/best
```

e utiliza FFmpeg para combinar as streams no contêiner MP4.

## Limitações atuais

- a validação da URL verifica principalmente se o texto começa com `http`;
- a pasta de saída é fixa;
- a localização do FFmpeg é vinculada à pasta do script;
- o histórico não é persistido após fechar o aplicativo;
- a implementação atual **não possui uma barra de progresso percentual na interface**, apesar de versões anteriores da documentação mencionarem esse recurso;
- não há seletor de qualidade;
- falhas individuais em playlists dependem do comportamento padrão do yt-dlp desta versão;
- atualizações do YouTube podem exigir uma versão mais recente do yt-dlp.

## Manutenção

Quando houver falhas de extração, uma das primeiras verificações é atualizar o yt-dlp:

```bash
python -m pip install --upgrade yt-dlp
```

Também confirme se o FFmpeg está acessível e compatível com o processamento solicitado.

## Uso responsável

Utilize a ferramenta apenas para conteúdos que você tenha autorização para baixar ou processar. Direitos autorais, termos de serviço e regras da plataforma continuam aplicáveis.

O projeto não remove DRM e não concede autorização para redistribuição de conteúdo protegido.

## Possíveis evoluções

- barra de progresso real;
- progresso global de playlist;
- seletor de pasta de destino;
- seletor de qualidade;
- persistência de histórico;
- cancelamento de download;
- tratamento individual de erros em playlists;
- configuração externa do FFmpeg;
- atualização automática/opcional do yt-dlp.

## Autoria

Desenvolvido por **Letícia Vitória**.

GitHub: **@leticiazooe**

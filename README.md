[![Generic badge](https://img.shields.io/badge/Made%20with-Python-<COLOR>.svg)](https://python.org)
[![GitHub issues](https://img.shields.io/github/issues/EsdrasUday/UDownloader?color=red)](https://github.com/EsdrasUday/UDownloader/issues)
[![GitHub followers](https://img.shields.io/github/followers/EsdrasUday?label=Follow&style=social)](https://github.com/EsdrasUday)

# U-Downloader
Este é um aplicativo simples para baixar vídeos do YouTube utilizando a biblioteca yt-dlp e customtkinter. A interface gráfica foi criada com CustomTkinter, que oferece uma experiência visual agradável e moderna.

Funcionalidades:
Interface em português: O aplicativo permite que o usuário escolha a qualidade do vídeo em português, com opções de "Melhor Qualidade", "Qualidade Média" e "Qualidade Baixa".
Download em segundo plano: O processo de download ocorre em uma thread separada, garantindo que a interface não trave enquanto o vídeo é baixado.
Salvar em pasta específica: Os vídeos são salvos na pasta downloads com o nome original do título do vídeo.
Aparência Personalizável: O aplicativo permite mudar entre modos de aparência "claro" e "escuro", com a opção de personalizar o tema de cores.
## Como usar:
### Instalar dependências:

Instale as bibliotecas necessárias:

bash
```
   pip install customtkinter yt-dlp
```
Rodar o script:

Clone este repositório ou baixe o script e execute-o:
bash
```
python baixador_youtube.py
```
Usar a interface:

Cole o link do vídeo do YouTube na caixa de entrada.
Selecione a qualidade desejada para o vídeo.
Clique no botão "Baixar Vídeo" para iniciar o download.
O status do download será exibido na parte inferior da janela.

## Contribuindo:
Se você encontrar algum erro ou tiver sugestões para melhorias, fique à vontade para abrir uma issue ou enviar um pull request!

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

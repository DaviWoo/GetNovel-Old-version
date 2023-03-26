# GetNovel
Obtém novels da centralnovel.com, junta os PDFs baixados e os coloca na pasta selecionada

A função GetNovel() pede algumas informações sobre o nome da novel, primeiro e último capítulo, e opcionalmente o número do volume
Retorna uma tupla contendo o nome da novel e uma lista interna com os links gerados para os capítulos especificados.

Usa algumas funções do módulo os (para obter o nome dos arquivos na pasta especificada e movê-los),
do módulo webbrowser para abrir os links designados para baixar (manualmente com enter ou não, dependendo da configuração do navegador),
e do termcolor (opcional) apenas para a mensagem de confirmação após mesclagem de todos os PDFs.

A função download() de my_functions é uma função opcional que baixa arquivos do link especificado (mas que foi inutilizada por conta dos links, que
geram uma requisição dinâmica para o servidor ao invés de resultarem em arquivos PDF), incluindo o diretório em que deve ser salvo e o nome do arquivo final

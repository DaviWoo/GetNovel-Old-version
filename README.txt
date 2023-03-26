# GetNovel
Obtém novels da centralnovel.com, junta os PDFs baixados e os coloca na pasta selecionada

A função GetNovel() pede algumas informações sobre o nome da novel, primeiro e último capítulo, e opcionalmente o número do volume
Retorna uma tupla contendo o nome da novel e uma lista interna com os links gerados para os capítulos especificados.

Usa algumas funções do módulo os (para obter o nome dos arquivos na pasta especificada e movê-los),
do módulo webbrowser para abrir os links designados para baixar (manualmente com enter ou não, dependendo da configuração do navegador),
e do termcolor (opcional) apenas para a mensagem de confirmação após mesclagem de todos os PDFs.

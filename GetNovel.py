from my_functions import GetNovel
import webbrowser
import PyPDF2
from os import listdir, rename
from termcolor import colored


lanks = GetNovel(
    name=str(input('Nome da Novel: ')),
    first_cap=int(input('Primeiro capítulo: ')),
    last_cap=int(input('Último capítulo: ')),
    volume=int(input('Volume [-1 SEM VOLUME]: '))
)

path = ''
sn = str(input('Deseja mesclar os PDFs? [S/N]: ')).strip().upper()[0]
if sn == 'S': path = str(input('Digite o caminho: '))
name = str(input('Nome final do arquivo: '))

links = lanks[1]

for url in links:
    webbrowser.open(url)


input('Pronto?: ')
merger = PyPDF2.PdfMerger(strict=False)
lista_arquivos = listdir(path)

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'{path}/{arquivo}')


merger.write(f"{name}.pdf")
archive = listdir('C:/Users/DaviT/PycharmProjects/testPROJECT')
for arq in archive:
    if '.pdf' in arq:
        rename(f'C:/Users/DaviT/PycharmProjects/testPROJECT/{arq}', f'{path}/{arq}')

print(colored('PDFs mesclados com SUCESSO!', 'green'))
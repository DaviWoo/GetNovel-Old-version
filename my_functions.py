import requests
import os


def GetNovel(name, first_cap, last_cap, volume=-1):
    name = name.lower().split()
    name = '-'.join(name)
    if "'s" in name: name = name.replace("'s", 's')


    chapters = list()

    for l in range(first_cap, last_cap + 1):
        if volume == -1:
            chapters.append(f'https://centralnovel.com/{name}-capitulo-{l}/pdf/')

        elif volume > -1:
            chapters.append(f'https://centralnovel.com/{name}-volume-{volume}-capitulo-{l}/pdf/')


    return name, chapters


def download(url, directory, nome):
    response = requests.get(url)
    filename = os.path.join(directory, nome)

    with open(filename, "wb") as file:
        file.write(response.content)


    #print(f"Arquivo salvo em {filename}")
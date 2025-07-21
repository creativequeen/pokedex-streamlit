from tkinter import *
from tkinter import ttk

# importando Pillow
from PIL import Image, ImageTk

# Certifique-se de que o dicionário 'pokemon' esteja definido no arquivo 'dados.py'
from dados import *  # Este arquivo deve conter as informações dos Pokémons

c00 = "#444466"  # Preta
c01 = "#feffff"  # Branca
c02 = "#6f9fbd"  # Azul
c03 = "#38576b"  # Valor
c04 = "#403d3d"  # Letra
c05 = "#ef5350"  # Vermelha

# Criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=c01)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat', bg=c01)
frame_pokemon.grid(row=1, column=0)

pok_imagem = Label(frame_pokemon, bg=c01)
pok_imagem.place(x=70, y=50)

# Labels de Nome, Tipo e ID
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys', 20), fg=c01)
pok_nome.place(x=12, y=15)

pok_tipo = Label(frame_pokemon, text='Elétrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=c01, fg=c00)
pok_tipo.place(x=12, y=50)

pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=c01, fg=c00)
pok_id.place(x=12, y=75)

# Labels de Status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=c01, fg=c00)
pok_status.place(x=15, y=310)

pok_hp = Label(janela, text='HP:100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=c01, fg=c04)
pok_hp.place(x=15, y=360)

pok_atack = Label(janela, text='Ataque:600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=c01, fg=c04)
pok_atack.place(x=15, y=385)

pok_defesa = Label(janela, text='Defesa:100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=c01, fg=c04)
pok_defesa.place(x=15, y=410)

pok_velocidade = Label(janela, text='Velocidade:100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=c01, fg=c04)
pok_velocidade.place(x=15, y=435)

pok_total = Label(janela, text='Total: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=c01, fg=c04)
pok_total.place(x=15, y=460)

# Labels de Habilidades
pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=c01, fg=c00)
pok_habilidades.place(x=180, y=310)

pok_hb_1 = Label(janela, text='Lightning Rod', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=c01, fg=c04)
pok_hb_1.place(x=195, y=360)

pok_hb_2 = Label(janela, text='Static', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=c01, fg=c04)
pok_hb_2.place(x=195, y=385)


def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem

    frame_pokemon['bg'] = pokemon[i]['tipo'][3]

    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    caminho_imagem = pokemon[i]['tipo'][2]

    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem)

    pok_imagem.configure(image=imagem_pokemon, bg=pokemon[i]['tipo'][3])
    pok_imagem.image = imagem_pokemon  # Importante: manter referência

    # Atualizando status dentro da função
    pok_hp['text'] = f"HP: {pokemon[i]['status'][0]}"
    pok_atack['text'] = f"Ataque: {pokemon[i]['status'][1]}"
    pok_defesa['text'] = f"Defesa: {pokemon[i]['status'][2]}"
    pok_velocidade['text'] = f"Velocidade: {pokemon[i]['status'][3]}"
    pok_total['text'] = f"Total: {pokemon[i]['status'][4]}"

     # Atualizando status dentro da função
    pok_hb_1['text'] = pokemon[i]['status'][0]
    pok_atack['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    # pokemon habilidades
    pok_hb_1['text'] = pokemon[i]['habilidades'][0]
    pok_hb_2['text'] = pokemon[i]['habilidades'][1]

# Criando botões para Pokémons
imagem_pokemon_1 = Image.open('pokemons/cabecapikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1 = Button(janela, command=lambda: trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg=c01,
                 fg=c00)
b_pok_1.place(x=375, y=10)

imagem_pokemon_2 = Image.open('pokemons/bulbasaurcabeca.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_2 = Button(janela, command=lambda: trocar_pokemon('Bulbasaur'), image=imagem_pokemon_2, text='Bulbasaur', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg=c01,
                 fg=c00)
b_pok_2.place(x=375, y=65)

imagem_pokemon_3 = Image.open('pokemons/Charmandercabeca.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_3 = Button(janela, command=lambda: trocar_pokemon('Charmander'), image=imagem_pokemon_3, text='Charmander', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg=c01,
                 fg=c00)
b_pok_3.place(x=375, y=120)

imagem_pokemon_4 = Image.open('pokemons/Cubonecabeca.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_4 = Button(janela, command=lambda: trocar_pokemon('Cubone'), image=imagem_pokemon_4, text='Cubone', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg=c01,
                 fg=c00)
b_pok_4.place(x=375, y=175)

imagem_pokemon_5 = Image.open('pokemons/psyduckcabeca.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_5 = Button(janela, command=lambda: trocar_pokemon('Psyduck'), image=imagem_pokemon_5, text='Psyduck', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg=c01,
                 fg=c00)
b_pok_5.place(x=375, y=230)

imagem_pokemon_6 = Image.open('pokemons/Squirtlecabeca.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_pok_6 = Button(janela, command=lambda: trocar_pokemon('Squirtle'), image=imagem_pokemon_6, text='Squirtle', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg=c01,
                 fg=c00)
b_pok_6.place(x=375, y=285)

imagem_pokemon_7 = Image.open('pokemons/togepicabeca.png')
imagem_pokemon_7 = imagem_pokemon_7.resize((40, 40))
imagem_pokemon_7 = ImageTk.PhotoImage(imagem_pokemon_7)

b_pok_7 = Button(janela, command=lambda: trocar_pokemon('Togepi'), image=imagem_pokemon_7, text='Togepi', width=150,
                 relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana', 12), bg=c01,
                 fg=c00)
b_pok_7.place(x=375, y=335)

# Variável global da imagem
imagem_pokemon = None

import random

Lista_pokemon = ['Pikachu', 'Bulbasaur', 'Charmander', 'Cubone', 'Psyduck', 'Squirtle', 'Togepi']

pokemon_escolhido = random.choice(Lista_pokemon)
trocar_pokemon(pokemon_escolhido)

janela.mainloop()

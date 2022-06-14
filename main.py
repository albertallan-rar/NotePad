import tkinter


# Função do botao New
def NewFile():
    text_area.delete(1.0, 'end')
    #print("Crie um novo documento")

# Função do botao Salvar
def Save():
    container = text_area.get(1.0, 'end')
    file = open('notepad.py', 'w')
    file.write(container)
    file.close()
    #print('Salva um arquivo')

# Função do botao Open
def Open():
    file = open('notepad.py', 'r')
    container = file.read()
    text_area.insert(1.0, container)
    #print('Abre um documento')

def Update():
    size = spin_size.get()
    font = spin_font.get()
    text_area.config(font="{} {}".format(font, size))



window = tkinter.Tk()
window.title('Notepad')
#window.minsize(width=720, height=1080) // Define o tamanho da tela
window.geometry('1280x720')#outro metodo para definir tamanho da tela e definir a posição inicial

#campo colocado a baixo do menu da tela
frame = tkinter.Frame(window, height=30)
frame.pack(fill='x')

#label colocando dentro do frame
font_text = tkinter.Label(frame, text=' Font: ')
font_text.pack(side='left')

#campo que esta habilitado a digitação
text_area = tkinter.Text(window, font='Arial 20 bold', width=1280, height=720)# campo de texto
text_area.pack()

#comando para trocar o style do texto
spin_font = tkinter.Spinbox(frame, values=('Arial', 'Verdana'))
spin_font.pack(side='left')

#Campo para alterar o tamanho da fonte do texto
font_size = tkinter.Label(frame, text=' Font size: ')
font_size.pack(side='left')

spin_size = tkinter.Spinbox(frame, from_=0, to=60)
spin_size.pack(side='left')

button_update = tkinter.Button(frame, text=' Atualizar o texto ', command=Update)
button_update.pack(side='left')

#parte do menu que fica no topo da tela
main_menu = tkinter.Menu(window)

#Opções do Menu
file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New', command=NewFile)
file_menu.add_command(label='Save', command=Save)
file_menu.add_command(label='Open', command=Open)
file_menu.add_command(label='Exit', command=window.quit)


main_menu.add_cascade(label='File', menu=file_menu)
window.config(menu=main_menu)

window.mainloop()
from tkinter import *
import webbrowser as wb

gapp = Tk()
gapp.maxsize(width = '370', height = '100')
gapp.minsize(width = '370', height = '100')
gapp.title('G-Surfing')
gapp.config(bg = 'black')

# Работа выхода
def exit_comm(event):
	gapp.destroy()

# Объекты
name = Label(gapp, text = 'G-Surfing')
name.config(font = ('Sans', '12'), bg = 'black', fg = 'white')
name.pack()

search_place = Entry(gapp, width = 35)
search_place.config(font = ('Sans','10'), bg = 'black', fg = 'white', insertbackground = 'white')
search_place.focus()
search_place.pack()

def search_g(event):
	search_text = search_place.get()
	wb.open_new_tab(f'https://www.google.com/search?&q={search_text}')

def search_y(event):
	search_text = search_place.get()
	wb.open_new_tab(f'https://yandex.ru/search/?&text={search_text}')

def search_ddg(event):
	search_text = search_place.get()
	wb.open_new_tab(f'https://duckduckgo.com/?q={search_text}')

def search_bg(event):
	search_text = search_place.get()
	wb.open_new_tab(f'https://www.bing.com/search?q={search_text}')

gapp.bind('<Control-g>', search_g)
gapp.bind('<Control-y>', search_y)
gapp.bind('<Control-d>', search_ddg)
gapp.bind('<Control-b>', search_bg)
gapp.bind('<Escape>', exit_comm)

gapp.mainloop()	
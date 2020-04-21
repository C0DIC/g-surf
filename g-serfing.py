from tkinter import *
import webbrowser as wb

root = Tk()
root.maxsize(width = '190', height = '130')
root.minsize(width = '190', height = '130')
root.title('G-Surfing 4.0')
root.config(bg = 'white')

# Значения
var = IntVar()

# Работа выхода
def exit_comm():
	root.destroy()

# Объекты
name = Label(root, text = 'G-Surfing')
name.config(font = ('Sans', '12'), bg = 'white')
name.place(x = 53, y = 5)

author_text = Label(root, text = 'MAIT')
author_text.config(font = ('Sans', '5'), bg = 'white')
author_text.place(x = 132, y = 2)

search_place = Entry(root, width = 20)
search_place.config(font = ('Sans','10'))
search_place.place(x = 11, y = 30)

# Работа поиска
def search_work():
	if var.get() == 0:
		search_text = search_place.get()
		wb.open_new_tab('https://www.google.com/search?&q={}'.format(search_text))
	elif var.get() == 1:
		search_text = search_place.get()
		wb.open_new_tab('https://yandex.ru/search/?&text={}'.format(search_text))

search_button = Button(root, text = 'Search', command = search_work)
search_button.config(font = ('Sans','9'), bg = 'white', border = 0)
search_button.place(x = 30, y = 55)

exit_button = Button(root, text = 'Exit', command = exit_comm )
exit_button.config(bg = 'white', font = ('Sans','9'), border = 0)
exit_button.place(x = 100, y = 55)

# Кнопки поиска
google_button = Radiobutton(root, text = 'Google', variable = var)
google_button.config(value = 0, font = ('Sans','9'), bg = 'white', border = 0)
google_button.place(x = 20, y = 87)

yandex_button = Radiobutton(root, text = 'Yandex', variable = var)
yandex_button.config(value = 1, font = ('Sans','9'), bg = 'white', border = 0)
yandex_button.place(x = 90, y = 87)

root.mainloop()
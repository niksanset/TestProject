import docx
from tkinter import *
import customtkinter
import datetime


def Write_word():
    text_write = Text_to_Write.get(1.0, END)
    mydoc = docx.Document()
    mydoc.add_paragraph(text_write)
    mydoc.save("my_written_file.docx")


def time():
    now = datetime.datetime.now()
    Time = now.strftime("%H:%M:%S")
    Day = now.strftime("%A")
    Date = now.strftime("%b %d, %Y")
    displayTime.configure(text=Time)
    displayDay.configure(text=Day)
    displayDate.configure(text=Date)
    main.after(1000, time)


main = customtkinter.CTk()
main.title('WriteToDocx')
main.geometry('1290x920')
main.resizable(False, False)
displayTime = customtkinter.CTkLabel(main, text='', font=("Helvetica", 50))
displayTime.pack(anchor=E, side=TOP, padx=40, pady=20)
displayDay = customtkinter.CTkLabel(main, text='', font=("Helvetica", 20))
displayDay.pack(anchor=E, side=TOP, padx=40)
displayDate = customtkinter.CTkLabel(main, text='', font=("Helvetica", 20))
displayDate.pack(anchor=E, side=TOP, padx=40)
title = customtkinter.CTkLabel(main, text='Введите текст для записи в документ: ', font=("Helvetica", 30))
title.pack()
Text_to_Write = customtkinter.CTkTextbox(master=main, font=('Arial', 20), width=1230, height=600, border_width=2,
                                         corner_radius=20)
Text_to_Write.pack(pady=30)
button = customtkinter.CTkButton(main, text='Запись ', font=('Arial', 30), command=Write_word, width=350, height=70)
button.pack(anchor="s", pady=20)
time()
main.mainloop()

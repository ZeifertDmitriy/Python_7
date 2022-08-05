from tkinter import *
from tkinter.ttk import Combobox
import fancs
from tkinter import filedialog
from logger import logger

def on_closing():
    logger('close','')
    window.destroy()

def start():
    global window
    window = Tk()
    window.geometry('430x380')
    window.title('Телефонный справочник')
    lbl = Label(window, text="Поиск данных в справочнике")
    lbl.grid(column=0, row=0, padx=5, pady=5)
    lbl = Label(window, text="Выберите параметр для поиска: ")
    lbl.grid(column=0, row=1, padx=5, pady=5)
    global combo_seach
    combo_seach = Combobox(window)  
    combo_seach['values'] = ('ФИО', '№ телефона')  
    combo_seach.current(1)
    combo_seach.grid(column=1, row=1, padx=5, pady=5)
    btn_poisk = Button(window, text="Поиск", command = fancs.btn_seach_click)
    btn_poisk.grid(column=2, row=1, padx=5, pady=5)
    global txt_seach, lbl_res
    txt_seach = Entry(window,width=23)  
    txt_seach.grid(column=0, row=2)
    txt_res = Entry(window,width=23)#, state='disabled')  
    lbl_res = Label(window, text="")
    lbl_res.grid(column=1, row=2)
    lbl = Label(window, text="_____________________________________")
    lbl.grid(column=0, row=3)
    lbl = Label(window, text="______________________________")
    lbl.grid(column=1, row=3)
    lbl = Label(window, text="_____________")
    lbl.grid(column=2, row=3)

    lbl = Label(window, text="Добавить данные в справочник")
    lbl.grid(column=0, row=4, padx=5, pady=5)
    global txt_fio
    txt_fio = Entry(window,width=30)  
    txt_fio.grid(column=0, row=5)
    global txt_nom
    txt_nom = Entry(window,width=23)  
    txt_nom.grid(column=1, row=5)
    btn_add = Button(window, text="Внести", command = fancs.btn_add_click)
    btn_add.grid(column=2, row=5, padx=5, pady=5)
    lbl = Label(window, text="_____________________________________")
    lbl.grid(column=0, row=6)
    lbl = Label(window, text="______________________________")
    lbl.grid(column=1, row=6)
    lbl = Label(window, text="_____________")
    lbl.grid(column=2, row=6)

    lbl = Label(window, text="Импорт данных в справочник")
    lbl.grid(column=0, row=7, padx=5, pady=5)
    lbl = Label(window, text="Выберите формат файла: ")
    lbl.grid(column=0, row=8, padx=5, pady=5)
    global combo_imp
    combo_imp = Combobox(window)  
    combo_imp['values'] = ('txt', 'csv')  
    combo_imp.current(1)
    combo_imp.grid(column=1, row=8, padx=5, pady=5)
    btn_imp = Button(window, text="Импорт", command = fancs.btn_imp_click)
    btn_imp.grid(column=2, row=8, padx=5, pady=5)
    lbl = Label(window, text="_____________________________________")
    lbl.grid(column=0, row=9)
    lbl = Label(window, text="______________________________")
    lbl.grid(column=1, row=9)
    lbl = Label(window, text="_____________")
    lbl.grid(column=2, row=9)

    lbl = Label(window, text="Экспорт данных в справочник")
    lbl.grid(column=0, row=10, padx=5, pady=5)
    lbl = Label(window, text="Выберите формат файла: ")
    lbl.grid(column=0, row=11, padx=5, pady=5)
    global combo_exp
    combo_exp = Combobox(window)  
    combo_exp['values'] = ('txt', 'csv')  
    combo_exp.current(1)
    combo_exp.grid(column=1, row=11, padx=5, pady=5)
    btn_exp = Button(window, text="Экспорт", command = fancs.btn_exp_click)
    btn_exp.grid(column=2, row=11, padx=5, pady=5)
    lbl = Label(window, text="_____________________________________")
    lbl.grid(column=0, row=12)
    lbl = Label(window, text="______________________________")
    lbl.grid(column=1, row=12)
    lbl = Label(window, text="_____________")
    lbl.grid(column=2, row=12)

    logger('open','')
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
import controller 

def btn_imp_click():
    file = controller.filedialog.askopenfilename(initialdir="data\imp", filetypes = ((f'{controller.combo_imp.get()}',f'*.{controller.combo_imp.get()}'),("all files","*.*")))
    spisok = []
    with open(file, 'r', encoding='utf-8') as file:
        spisok = file.read()

    with open('data\spr.csv', 'a', encoding='utf-8') as file2:
        file2.write(spisok)
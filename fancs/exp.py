import controller 

def btn_exp_click():
    file = controller.filedialog.asksaveasfilename(defaultextension=f'{controller.combo_imp.get()}', filetypes = ((f'{controller.combo_imp.get()}',f'*.{controller.combo_imp.get()}'),("all files","*.*")))
    spisok = []
    with open('spr.csv', 'r', encoding='utf-8') as file2:
        spisok = file2.read()

    with open(file, 'a', encoding='utf-8') as file:
        file.write(spisok)

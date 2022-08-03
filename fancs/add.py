import controller 

def btn_add_click():
    with open('spr.csv', 'a', encoding='utf-8') as file:
        file.write('{},{}\n'
                    .format(controller.txt_fio.get(), controller.txt_nom.get()))
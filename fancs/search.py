import controller 

def btn_seach_click():
    spisok = []
    controller.lbl_res = controller.Label(text='                         ')
    controller.lbl_res.grid(column=1, row=2)
    with open('spr.csv', 'r', encoding='utf-8') as file:
        for line in file:
            spisok = line
            spisok = spisok [:len(spisok)-1]
            spisok = spisok.split(',')
            for i in spisok:
                if (controller.combo_seach.get() == 'ФИО') and (controller.txt_seach.get() == spisok[0]):
                    controller.lbl_res = controller.Label(text=spisok[1])
                    controller.lbl_res.grid(column=1, row=2)
                elif (controller.combo_seach.get() == '№ телефона') and (controller.txt_seach.get() == spisok[1]):
                    controller.lbl_res = controller.Label(text=spisok[0])
                    controller.lbl_res.grid(column=1, row=2)
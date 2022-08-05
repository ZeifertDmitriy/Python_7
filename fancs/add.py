import controller 
from logger import logger

def btn_add_click():
    with open('data\spr.csv', 'a', encoding='utf-8') as file:
        file.write('{},{}\n'
                    .format(controller.txt_fio.get(), controller.txt_nom.get()))
        logger('add',(controller.txt_fio.get(), controller.txt_nom.get()))
from datetime import datetime as dt
import model as m
from ui import *

def data_log():
    if get_string() != 'line':
        with open('log.csv', 'a') as file:
            file.write('{};\n{};\n{};\n{}; \n \n'
                        .format(m.name, m.surname, m.phone, m.comment))
    else:
        with open('log.csv', 'a') as file:
            file.write('{}; {}; {}; {};\n \n'
                        .format(m.name, m.surname, m.phone, m.comment))

def import_data():
    count = 0
    with open('import.csv', 'r') as file:
        # for column in file:
        #     count += 1
        #     # print(count)
            
        # if count != 1:


        # else:
            s = file.read()
            s = ''.join([i for i in s if i != ';'])
            m.init(s)            
            



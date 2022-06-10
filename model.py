
def init(str):
    global name, surname, phone, comment
    name = []
    surname = []
    phone = []
    comment = []
    
    data = str.split(" ")

    name = data[0]
    surname = data[1]
    phone = data[2]
    comment = data[3]

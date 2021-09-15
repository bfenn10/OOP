import PhoneClass

def main():
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model: ')
    retail = float(input('Enter the retail price: '))

    phone = cellphone.CellPhone(man, mod, retail)

    print('Here is teh data that you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model ')



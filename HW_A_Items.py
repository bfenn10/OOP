import RetailItemClass as r

def main():

    inventory = make_list()

    print('Here is the data you entered:')
    display_list(inventory)

def make_list():

    item_list = []

    print('Enter data for three items.')
    for count in range(1,4):
        print('Item Number ' + str(count) + ':')
        item = input('Enter description of item: ')
        units = float(input('Enter number of units in inventory: '))
        price = float(input('Enter price per item: '))
        print()

        items = RetailItem(item,units,price)

        item_list.append(items)

        return item_list

    def display_list(item_list):
        for item in item_list:
            print(item.get_item_description())
            print(item.get_units_in_inventory())
            print(item.get_price())
            print()

main()


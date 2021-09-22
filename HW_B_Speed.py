import HW_B_CarClass as c

def main():

    year = print(input('Car year: '))
    make = print(input('Car make: '))
    speed = 0

    my_car = c.Car(year,make,speed)

    print('')
    print('My current speed is 0')
 
    my_car.accelerate()
    print('My current speed after acceleration:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed after acceleration:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed after acceleration:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed after acceleration:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed after acceleration:',my_car.get_speed())

    my_car.brake()
    print('My current speed after brake:',my_car.get_speed())
    my_car.brake()
    print('My current speed after brake:',my_car.get_speed())
    my_car.brake()
    print('My current speed after brake:',my_car.get_speed())
    my_car.brake()
    print('My current speed after brake:',my_car.get_speed())
    my_car.brake()
    print('My current speed after brake:',my_car.get_speed())

main()
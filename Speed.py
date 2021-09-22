import CarClass as c

def main():

    my_car = c.Car(year,make,speed)

    year = print(input('Car year: '))
    make = print(input('Car make: '))
    speed = print('Current speed is 0')


    my_car.accelerate()
    print('My current speed:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed:',my_car.get_speed())
    my_car.accelerate()
    print('My current speed:',my_car.get_speed())

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
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print(f'There are {cars} cars avaliable.')
print(f'There are only {drivers} drivers avaliable.')
print(f'There will be {cars_not_driven} empty cars today.')
print(f'We can transport {carpool_capacity} people today.')
print(f'We have {passengers} to carpool today.')
print(f'We need to put about {average_passengers_per_car:.2f} in each car.')

# f'String' facilitou bastante o código

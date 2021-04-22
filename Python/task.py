def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "capetown":
        return 2500
    elif city == "durban":
        return 2300
    elif city == "jhb":
        return 2000
    elif city == "bfn":
        return 1800


def rental_car_cost(days):
    if days >= 3:
        if days >= 7:
            return days * 40 - 50
        else:
            return days * 40 - 20
    else:
        return days * 40


def new_sum(*numbers):
    return sum(numbers)


def trip_cost(city, days, spending_money):
    return new_sum(plane_ride_cost(city), hotel_cost(days), rental_car_cost(days), spending_money)


print(trip_cost("capetown", 1, 0))

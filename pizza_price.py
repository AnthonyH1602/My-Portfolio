#!/usr/bin/env python3
def y_or_n(message):
    while True:
        answer = input(message)
        if answer == "y":
            break
        elif answer == "n":
            break
        else:
            print("Please enter y/n")
    return answer


if __name__ == '__main__':

    total_price = 0.00
    PIZZA_PRICE = 12
    TUESDAY_DISC = 0.5
    APP_DISC = 0.75

    print("Welcome to Pizza Plaza!")
    while True:
        try:
            pizza_quant = int(input("Order quantity: "))
            if pizza_quant > 0:
                break
            else:
                print("Invalid input")
        except ValueError:
            print("Please enter a number")

    delivery = y_or_n("Is this order for delivery? y/n ")
    tuesday = y_or_n("tues y/n ")
    new_app = y_or_n("app y/n ")

    total_price = pizza_quant * PIZZA_PRICE
    if tuesday == "y":
        total_price *= TUESDAY_DISC
    if delivery == "y":
        if pizza_quant < 4:
            total_price += 2.50
    if new_app == "y":
        total_price *= APP_DISC

    print("Total price £", "%.2f" % total_price)

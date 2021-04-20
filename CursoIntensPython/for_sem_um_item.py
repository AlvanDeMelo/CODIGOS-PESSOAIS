requested_toppings = ['mushroons', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    # Caso falte algum ingrediente da lista:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Addinng {requested_topping}.")


print("\nFinished making your pizza!")

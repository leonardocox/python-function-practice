def hello():
    print("yo")


def pack(oh, heck, no):
    return [oh, heck, no]


def eat_lunch(Lunch_items):
    if len(Lunch_items) == 0:
        print("there is no lunch oh no!")
    else:
        for i in range(len(Lunch_items)):
            if i == 0:
                print(f"First I eat {Lunch_items[i]}")
            else:
                print(f"Next I eat {Lunch_items[i]}")


hello()
print(pack("oh", "heck", "no"))
eat_lunch([])
eat_lunch(["Dino Nuggies"])

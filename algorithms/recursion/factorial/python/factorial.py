def fact(num:int):
    if num == 1:
        return 1

    return num * fact (num - 1)

print(fact(5))
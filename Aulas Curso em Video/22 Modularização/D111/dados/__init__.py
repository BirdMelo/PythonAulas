def justnum(var):
    while True:
        n = input(var).replace(",", ".")
        if n.isalpha() or n.strip() == "":
            print(f"\033[31mERRO: '{n}' não é valido.\033[m")
        else:
            return float(n)

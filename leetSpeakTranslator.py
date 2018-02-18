while True:
    string = input("Please write words that should be translated to 1337 sp34k: ")

    string_1337 = string.lower().replace('e', '3').replace('a', '4').replace('l', '1').replace('t', '7').replace('o', '0').replace('s', '5').replace('b', '8')
    print(string_1337)

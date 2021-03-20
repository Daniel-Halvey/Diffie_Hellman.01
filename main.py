def main():
    p = int(input("Give p as a INTEGER : "))
    g = int(input("Give G as a INTEGER: "))

    x = int(input("What is Alice's random number? (x): "))
    y = int(input("What is Bob's random number? (y): "))

    print(" ")

    LOL1 = (g) ** x % p

    print("LOL1 = ", g, "^", x, "%", p, "=", LOL1)
    print(" ")

    LOL2 = (g) ** y % p

    print("LOL2 =", g, "^", y, "%", p, "=", LOL2)

    print(" ")

    ka = LOL2 ** x % p

    print("Alice's (Ka) is", ka, "------>" "to get this answer you take", LOL2, "^", x, "(", LOL2 ** x,
          ")", "%", p, "to get the answer of ", ka)
    print(" ")

    kb = LOL1 ** y % p

    print("Bob's Key (Kb) is", kb, "---------------->" "to get this answer you take", LOL1, "^", x, "(", LOL1 ** y,
          ")", "%", p, "to get the answer of ", kb)
    print("Bob & Alice get married start a family and live happily ever after and DH buys a boat")


main()
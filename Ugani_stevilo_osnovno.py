skrito_stevilo = 33

guess = int(raw_input("Ugani skrito stevilo: "))


if guess == skrito_stevilo:
    print "Cestitam, uganili ste pravo stevilo :)"
else:
    print "Zal iskano stevilo ni enako " + str(guess) + " poskusite ponovno"

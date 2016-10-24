stevilo = int (raw_input ("Vnesite stevilo med 1 in 100: "))

for n in range (1, stevilo + 1):

    if n % 3 == 0 and n % 5 == 0:
        print ("fizzbuzz")

    elif n % 5 == 0:
        print ("buzz")

    elif n % 3 == 0:
        print ("fizz")

    else:
        print (n)

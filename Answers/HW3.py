def prime_first(number):
    value=int(number/2)
    for sayi in range(value+1):
        if sayi > 1:

            for i in range(2, sayi):
                if (sayi % i) == 0:
                    print(sayi, " Asal Sayı Değildir.")
                    break
            else:
                print(sayi, " Asal Sayıdır.")

        else:
            print(sayi, " Asal Sayı Değildir.")

def prime_second(number):
    value = int(number / 2)
    for sayi in range(number+1):
        if sayi > 1:

            for i in range(2, sayi):
                if (sayi % i) == 0:
                    print(sayi, " Asal Sayı Değildir.")
                    break
            else:
                print(sayi, " Asal Sayıdır.")

        else:
            print(sayi, " Asal Sayı Değildir.")

prime_first(1000)
prime_second(1000)
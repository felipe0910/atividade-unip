mes=int(input("Qual e seu mes de anivesario (1-12): "))
curso=str(input("Qual é seu cuso (ads/gti): "))

if 1>= mes <=6:
    print(mes,"voce nasceu no primeiro semestre")
elif 7>= mes <=12:
    print(mes,"voce nasceu no segundo semestre")
else:
    print("o mes de nascimento está incorreto")


if curso =="ads":
    print("o seu curso é ADS " ) 
elif curso =="gti":
    print("o seu curso é GTI ")
else:
    print("seu curso está incorreto")






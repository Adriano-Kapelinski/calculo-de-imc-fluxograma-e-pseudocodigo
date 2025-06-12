peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))


IMC = peso / (altura * altura)

if IMC < 18.5:
    print(f"Seu IMC é {IMC:.2f} e você está abaixo do peso.")
elif 18.5 <= IMC < 25:
    print(f"Seu IMC é {IMC:.2f} e você está com peso normal.")
elif 25 <= IMC < 30:
    print(f"Seu IMC é {IMC:.2f} e você está com sobrepeso.")
elif 30 <= IMC < 40:
    print(f"Seu IMC é {IMC:.2f} e você está com obesidade.")
else:  # IMC >= 40
    print(f"Seu IMC é {IMC:.2f} e você está com obesidade grave.")

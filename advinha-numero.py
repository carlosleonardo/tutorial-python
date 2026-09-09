import random

print("Advinhação do Número")
while True:
	numero_secreto = random.randint(1, 20)
	print("Você tem 3 tentativas")
	for tentativa in range(3):
		palpite = int(input("Tente adivinhar o número entre 1 e 20: "))
		if palpite == numero_secreto:
			print("Parabéns! Você acertou!")
			break
		elif palpite < numero_secreto:
			print("Muito baixo! Tente novamente.")
		else:
			print("Muito alto! Tente novamente.")
	else:
		print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
	print("Vamos jogar novamente!")
	continuar = input("Deseja continuar? (s/n): ").strip().lower()
	if continuar != 's':
		break
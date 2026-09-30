print("Calcula velocidade média")
while True:
	try:
		distancia = float(input("Digite a distância percorrida (em km, -1 sai): "))
		if distancia == -1:
			break
		tempo = float(input("Digite o tempo gasto (em horas): "))
		velocidade_media = distancia / tempo
		print(f"A velocidade média é: {velocidade_media:.2f} km/h")
	except ZeroDivisionError:
			print("O tempo não pode ser zero.")
			continue
	except ValueError as erro:
		print(f"Entrada inválida, {erro}, tente outro número!")
		continue
	
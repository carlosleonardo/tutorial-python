linguagem = input("Escolha a linguagem (Python, Java, C++): ").lower()
match linguagem:
	case "python":
		print("Você escolheu Python!")
	case "java":
		print("Você escolheu Java!")
	case "c++":
		print("Você escolheu C++!")
	case _:
		print("Linguagem não reconhecida.")
		

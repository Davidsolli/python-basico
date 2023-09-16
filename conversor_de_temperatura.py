selecao = input("Digite 'a' para converter celsius para fahrenheit ou 'b' para o contrario: ")

if selecao == 'a':
	temp_cel = input("Digite a temperatura em graus celsius: ")
	temp_fah = ((float(temp_cel) / 5) * 9) + 32
	print(temp_fah)
else:
	temp_fah = input("Digite a temperatura em graus fahrenheit: ")
	temp_cel = ((float(temp_fah) - 32) * 5) / 9
	print(temp_cel)
	  
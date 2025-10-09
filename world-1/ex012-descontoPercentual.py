preco = float(input('Informe o preço do pruduto: '))
desc = 5
valorDesc = preco * desc / 100
print('Para o pagamento a vista, o desconto é de {:.2f}%. \nO novo valor é de R$ {:.2f}.' .format(desc, (preco - valorDesc)))
from os import system, name 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 
		
def valorpago(cafe,leite,cappuc,a1,b1,c1,d1,e1,f1,trocodisponivel,pagou=0,valortotal=0,pagouu=0):
	"""ESSA FUNÇÃO PEDE AO USUARIO O DINHEIRO E CALCULA O TOTAL QUE ELE PAGOU
	    E O SEU TROCO DE DEPOIS MANDA AS INFORMAÇÕES PARA A FUNÇÃO TROCO"""
	y=float(input("Coloque o dinheiro: "))
	if y==20 or y==10 or y==5 or y==2 or y==1 or y==0.50:
		if y==20:
			a1+=1
		if y==10:
			b1+=1
		if y==5:
			c1+=1
		if y==2:
			d1+=1
		if y==1:
			e1+=1
		if y==0.5:
			f1+=1
		if y<=valortotal:
			pagouu+=y
			if pagouu<valortotal:
				valorpago(cafe,leite,cappuc,a1,b1,c1,d1,e1,f1,trocodisponivel,pagou+y,valortotal,pagouu)
			else:
				x=pagou+y
				print()
				print("Você pagou: R$ {:.2f}".format(pagou+y))
				print("Seu troco é de: R$ {:.2f}".format(x-valortotal))
				print()
				print("Pegue seu troco: ")
				troco(cafe,leite,cappuc,a1,b1,c1,d1,e1,f1,trocodisponivel,n=x,n2=x,valorcompra=valortotal,trocoverdadeiro=x-valortotal,trocoverdadeiro2=x-valortotal)
		else:
			print()
			print("Você pagou: R$ {:.2f}".format(y+pagou))
			print("Seu troco é de: R$ {:.2f}".format((y+pagou)-valortotal))
			print()
			print("Pegue seu troco: ")
			troco(cafe,leite,cappuc,a1,b1,c1,d1,e1,f1,trocodisponivel,n=y+pagou,n2=y+pagou,valorcompra=valortotal,trocoverdadeiro=(y+pagou)-valortotal,trocoverdadeiro2=(y+pagou)-valortotal)
	else:
		print("Valor não reconhecido!")
		valorpago(cafe,leite,cappuc,a1,b1,c1,d1,e1,f1,trocodisponivel,pagou,valortotal,pagouu)	
def troco(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1,trocodisponivel,n,n2,valorcompra=0,trocototal=0,trocoverdadeiro=0,trocoverdadeiro2=0,a=20,b=10,c=5,d=2,e=1,f=0.5): # a = 20,00; b = 10,00; c = 5,00; d = 2,00; e=1,00; f = 0,50 ; valores em reais):
	"""ESSA FUNÇÃO É RESPONSÁVEL DE CALCULAR O TROCO (SE HOUVER) DO USUÁRIO E DEPENDENDO AS POSSIBILIDADES
	    ENVIA AS INFORMAÇÕES PARA AS FUNÇÕES AGAIN, AGAIN2, SEMTROCO E SEMTROCO2"""
	if trocodisponivel>=trocoverdadeiro2:
		if n>valorcompra or trocototal==trocoverdadeiro:          # n = total do dinheiro colocado 
			if b<n and trocototal<=trocoverdadeiro and b<=trocoverdadeiro and b1>0:
				print("R$ {:.2f} ".format(b))
				trocototal+=b
				if trocototal<=trocoverdadeiro :
					troco(cafe1,leite1,cappuc1,a1,b1-1,c1,d1,e1,f1,trocodisponivel-b,n-b,n2,valorcompra,trocototal,trocoverdadeiro,trocoverdadeiro2-b,a,b,c,d,e,f)
			elif c<n and trocototal<=trocoverdadeiro and c<=trocoverdadeiro and c1>0 :
				print("R$ {:.2f} ".format(c))
				trocototal+=c
				if trocototal<=trocoverdadeiro :
					troco(cafe1,leite1,cappuc1,a1,b1,c1-1,d1,e1,f1,trocodisponivel-c,n-c,n2,valorcompra,trocototal,trocoverdadeiro,trocoverdadeiro2-c,a,b,c,d,e,f)
			elif d<n and trocototal<=trocoverdadeiro-d and d<=trocoverdadeiro and d1>0:
				print("R$ {:.2f} ".format(d))
				trocototal+=d
				if trocototal <= trocoverdadeiro :
					troco(cafe1,leite1,cappuc1,a1,b1,c1,d1-1,e1,f1,trocodisponivel-d,n-d,n2,valorcompra,trocototal,trocoverdadeiro,trocoverdadeiro2-d,a,b,c,d,e,f)
			elif e<n and trocototal<=trocoverdadeiro-e and e<=trocoverdadeiro and e1>0:
				print("R$ {:.2f} ".format(e))
				trocototal+=e
				if trocototal <= trocoverdadeiro :
					troco(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1-1,f1,trocodisponivel-e,n-e,n2,valorcompra,trocototal,trocoverdadeiro,trocoverdadeiro2-e,a,b,c,d,e,f)
			elif f<n and trocototal<=trocoverdadeiro-f and f<=trocoverdadeiro and f1>0:
				print("R$ {:.2f} ".format(f))
				trocototal+=f
				if trocototal <= trocoverdadeiro :
					troco(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1-1,trocodisponivel-f,n-f,n2,valorcompra,trocototal,trocoverdadeiro,trocoverdadeiro2-f,a,b,c,d,e,f)
				else:
					troco(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1-1,trocodisponivel-f,n,n2,valorcompra,trocototal,trocoverdadeiro,trocoverdadeiro2-f,a,b,c,d,e,f)
			elif trocototal==trocoverdadeiro and n2>valorcompra:
				again2(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1,trocodisponivel)
			elif trocoverdadeiro==0.5 and f1==0:
				semtroco2(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1,trocodisponivel)
				
			else:
				print("Valor exato, não tem troco")
				again(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1,trocodisponivel)
		else:
			print("Valor exato, não tem troco")
			again(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1,trocodisponivel)
	else:
		semtroco(cafe1,leite1,cappuc1,a1,b1,c1,d1,e1,f1,trocodisponivel)

def semtroco2(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel,trocodisponivel2=0):
	"""USADO QUANDO A MAQUINA TEM TROCO, POREM NAO TEM AS NOTAS CERTAS PRA DAR"""
	print()
	print("Não temos troco para o valor pago.")
	print("Temos apenas R$ {:.2f} para voltar de troco".format(trocodisponivel2))
	print()
	x=input("Deseja comprar assim mesmo? (S/N): ")
	if x=="S" or x=="s":
		print()
		y=(input("Deseja comprar outro produto? (S/N): "))
		if y=="S" or y=="s":
			maquina(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel)
		elif y=="N" or y=="n":
			print()
			print("Obrigado pela preferência.")
			print("Volte Sempre!!!")
	elif x=="N" or x=="n":
		print()
		print("Obrigado pela preferência.")
		print("Volte Sempre!!!")
	else:
		print("Caractere não reconhecido")
		semtroco2(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel)

def semtroco(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel):
	"""USADO QUANDO A MAQUINA TEM TROCO, POREM NAO TEM O VALOR SUFICIENTE PARA DAR"""
	print()
	print("Não temos troco para o valor pago.")
	print("Temos apenas R$ {:.2f} para voltar de troco".format(trocodisponivel))
	print()
	x=input("Deseja comprar assim mesmo? (S/N): ")
	if x=="S" or x=="s":
		print("Pegue seu troco: ")
		print("R$ {:.2f}".format(trocodisponivel))
		print()
		y=(input("Deseja comprar outro produto? (S/N): "))
		if y=="S" or y=="s":
			maquina(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel-trocodisponivel)
		elif y=="N" or y=="n":
			print()
			print("Obrigado pela preferência.")
			print("Volte Sempre!!!")
	elif x=="N" or x=="n":
		print()
		print("Obrigado pela preferência.")
		print("Volte Sempre!!!")
	else:
		print("Caractere não reconhecido")
		semtroco(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel)

def again(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel): 
	"""ESSA FUNÇÃO É USADA PARA PERGUNTAR SE O USUARIO
	QUER OUTRO PRODUTO QUANDO ELE INSERE O VALOR TOTAL DO PRODUTO
	COMPRADO ANTES"""
	print()
	x=(input("Deseja comprar outro produto? (S/N): "))
	if x=="S" or x=="s":
		maquina(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel)
	elif x=="N" or x=="n":
		print()
		print("Obrigado pela preferência.")
		print("Volte Sempre!!!")

	else:
		print("Caractere não reconhecido")
		again(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel)

def again2(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel):
	"""ESSSA FUNÇÃO É PARA PERGUNTAR AO USUARIO SE ELE QUER
	OUTRO PRODUTO APÓS A MÁQUINA DAR O SEU TROCO"""
	print()
	x=(input("Deseja comprar outro produto? (S/N): "))
	if x=="S" or x=="s":
		maquina(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel)
	elif x=="N" or x=="n":
		print()
		print("Obrigado pela preferência.")
		print("Volte Sempre!!!")
	else:
		print("Caractere não reconhecido")
		again2(cafe2,leite2,cappuc2,a1,b1,c1,d1,e1,f1,trocodisponivel)

def maquina(a=5,b=5,c=5,a1=5,b1=5,c1=5,d1=5,e1=5,f1=5,trocodisponivel=0,valorTotal=0): # a=item 1, b=item 2, c=item 3 , (a1,b1,c1,d1,e1,f1 representam as notas de 20,00 , 10,00 , 5,00 , 2,00 , 1,00 e 0,50 reais respectivamente)
	"""ESSA FUNÇAÕ É A PRINCIPAL DO PROGRAMA (MAIN). ELA DEFINE AS PRINCIPAIS VARIAVEIS E SUAS QUANTIDADES
	ALÉM DE SER A INTERFACE PRINCIPAL DO PROGRAMA """
	limpaTela()
	trocodisponivel=(b1*10)+(c1*5)+(d1*2)+(e1*1)+(f1*0.5)
	print("********************************************")
	if a>0:
		print("*  1 - CAFÉ EXPRESSO              R$ 2,50  *")
	else:
		print("*  1 - CAFÉ EXPRESSO          indisponível *")
	if b>0:
		print("*  2 - LEITE COM NESCAU®          R$ 3,00  *")
	else:
		print("*  2 - LEITE COM NESCAU®      indisponível *")
	if c>0:
		print("*  3 - CAPPUCCINO                 R$ 4,50  *")
	else:
		print("*  3 - CAPPUCCINO             indisponível *")

	print("********************************************")                                                                   
	x = int(input("Escolha seu produto: "))
	if 0<x<4: 
		if x==1:
			valorTotal+=2.50
			print()
			if a>0:
				print("Você escolheu CAFÉ ESPRESSO")
				print("Preço: R$ 2,50")
				print()
				valorpago(a-1,b,c,a1,b1,c1,d1,e1,f1,trocodisponivel,pagou=0,valortotal=valorTotal) # a variavel valortal é improtante
			else:
				print("Desculpe, mas o CAFÉ EXPRESSO está indisponível.")
				again2(a,b,c,a1,b1,c1,d1,e1,f1,trocodisponivel)
		if x==2:                                        
			valorTotal+=3.00
			print()
			if b>0:
				print("Você escolheu LEITE COM NESCAU®")
				print("Preço: R$ 3,00")
				print()
				valorpago(a,b-1,c,a1,b1,c1,d1,e1,f1,trocodisponivel,pagou=0,valortotal=valorTotal)
			else:
				print("Desculpe, mas o LEITE COM NESCAU® está indisponível.")
				again2(a,b,c,a1,b1,c1,d1,e1,f1,trocodisponivel)
		if x==3:
			valorTotal+=4.50
			print()
			if c>0:
				print("Você escolheu CAPPUCCINO")
				print("Preço: R$ 4,50")
				print()
				valorpago(a,b,c-1,a1,b1,c1,d1,e1,f1,trocodisponivel,pagou=0,valortotal=valorTotal)
			else:
				print("Desculpe, mas o CAPPUCCINO está indisponível.")
				again2(a,b,c,a1,b1,c1,d1,e1,f1,trocodisponivel)
	else:
		print("Produto não encontrado")
		print()
		y=input("Pressione qualquer tecla para continuar: ")
		maquina(a,b,c,a1,b1,c1,d1,e1,f1,valorTotal,trocodisponivel)
maquina()
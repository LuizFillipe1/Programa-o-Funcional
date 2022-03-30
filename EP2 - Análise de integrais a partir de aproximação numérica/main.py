import integral
import math
def funcao2():
	"""ESSA FUNÇÃO É A INTEGRAL 2 DO EP"""
	return lambda x:(math.sin(x)**2)+(2*((math.sin(2*x))**4))

def funcao5():
	"""ESSA FUNÇÃO É A INTEGRAL 5 DO EP"""
	return lambda x:0.2+(25*x)-(200*x**2)+(675*x**3)-(900*x**4)+(400*x**5)

def funcao7():
	"""ESSA FUNÇÃO É A INTEGRAL 7 DO EP"""
	return lambda x: x*math.sin(x)

def calculaErroTrapezio(valorexato,integral1,r=[],i=0):
	'''Essa função calcula o erro da integral pela regra dos trapézios e 
	retorna uma lista com esses erros'''
	if i<len(integral1):
		erro=(abs(integral1[i]-valorexato))/valorexato
		return calculaErroTrapezio(valorexato,integral1,r+[erro],i+1)
	else:
		return r
def calculaErroSimpson(valorexato,integral2,r=[],i=0):
	'''Essa função calcula o erro da integral de simpson e 
	retorna uma lista com esses erros'''
	if i<len(integral2):
		erro=(abs(integral2[i]-valorexato))/valorexato
		return calculaErroTrapezio(valorexato,integral2,r+[erro],i+1)
	else:
		return r

def main():
	'''Essa é a função priincipal do programa. Ela é responsavel por determinar
	os subintervalos, os limites e imprimir os resultados.
	a = limite inferior ; b = limite superior ; n = intervalos 
	'''
	#Calcula a integral 2
	n=[4,10,50,100,150,200,300,400,500,600,700,800,900] # números de intervalos
	a=0
	b=math.pi
	x1=integral.integrais((integral.ruleoftrapezio),funcao2(),a,b,n) # é uma lista com os valores das integrais(trapezio) ordenada pelos intervalos
	x2=integral.integrais((integral.regraSimpson),funcao2(),a,b,n) # é uma lista com os valores das integrais(simpson) ordenada pelos intervalos
	valorExato=(5*math.pi)/4
	erroT=calculaErroTrapezio(valorExato,x1) #é uma lista com os erros
	erroS=calculaErroSimpson(valorExato,x2) #é uma lista com os erros
	print()
	print("Função: sin^2(x) + 2*sin^4(2x) , com a = 0 e b = pi")
	print("Valor exato:       {:.20f}".format(valorExato))
	print("==> Regra dos Trapézios")
	print("-----------------------------------------------------------------")
	print("n                    integral                             erro")
	print("-----------------------------------------------------------------")
	print("4            {:.20f}        {:.20f}  ". format(x1[0],erroT[0]))  
	print("10           {:.20f}        {:.20f}  ". format(x1[1],erroT[1]))
	print("50           {:.20f}        {:.20f}  ". format(x1[2],erroT[2]))
	print("100          {:.20f}        {:.20f}  ". format(x1[3],erroT[3]))
	print("150          {:.20f}        {:.20f}  ". format(x1[4],erroT[4]))
	print("200          {:.20f}        {:.20f}  ". format(x1[5],erroT[5]))
	print("300          {:.20f}        {:.20f}  ". format(x1[6],erroT[6]))
	print("400          {:.20f}        {:.20f}  ". format(x1[7],erroT[7]))
	print("500          {:.20f}        {:.20f}  ". format(x1[8],erroT[8]))
	print("600          {:.20f}        {:.20f}  ". format(x1[9],erroT[9]))
	print("700          {:.20f}        {:.20f}  ". format(x1[10],erroT[10]))
	print("800          {:.20f}        {:.20f}  ". format(x1[11],erroT[11]))
	print("900          {:.20f}        {:.20f}  ". format(x1[12],erroT[12]))
	print("-----------------------------------------------------------------")
	print("==> Regra de Simpson") 
	print("-----------------------------------------------------------------")
	print("n                    integral                             erro")
	print("-----------------------------------------------------------------")
	print("4            {:.20f}        {:.20f}  ". format(x2[0],erroS[0]))
	print("10           {:.20f}        {:.20f}  ". format(x2[1],erroS[1]))
	print("50           {:.20f}        {:.20f}  ". format(x2[2],erroS[2]))
	print("100          {:.20f}        {:.20f}  ". format(x2[3],erroS[3]))
	print("150          {:.20f}        {:.20f}  ". format(x2[4],erroS[4]))
	print("200          {:.20f}        {:.20f}  ". format(x2[5],erroS[5]))
	print("300          {:.20f}        {:.20f}  ". format(x2[6],erroS[6]))
	print("400          {:.20f}        {:.20f}  ". format(x2[7],erroS[7]))
	print("500          {:.20f}        {:.20f}  ". format(x2[8],erroS[8]))
	print("600          {:.20f}        {:.20f}  ". format(x2[9],erroS[9]))
	print("700          {:.20f}        {:.20f}  ". format(x2[10],erroS[10]))
	print("800          {:.20f}        {:.20f}  ". format(x2[11],erroS[11]))
	print("900          {:.20f}        {:.20f}  ". format(x2[12],erroS[12]))
	print()
	#Calcula a integral 5
	a=0 
	b=0.8
	y1=integral.integrais((integral.ruleoftrapezio),funcao5(),a,b,n) # é uma lista com os valores das integrais(trapezio) ordenada pelos intervalos
	y2=integral.integrais((integral.regraSimpson), funcao5(), a,b,n) # é uma lista com os valores das integrais(simpson) ordenada pelos intervalos
	valorExato=(1.64053000000000004377) #no arquivo é 1.64053
	erroT=calculaErroTrapezio(valorExato,y1) #é uma lista com os erros pela regra do trapezio
	erroS=calculaErroSimpson(valorExato,y2) #é uma lista com os erros de simpson
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print("Função: 0.2 + 25x - 200x^2 + 675x^3 - 900x^4 + 400x^5 , com a=0 e b=0.8 ")
	print("Valor exato:      1.64053000000000004377")
	print("==> Regra dos Trapézios")
	print("-----------------------------------------------------------------")
	print("n                    integral                             erro")
	print("-----------------------------------------------------------------")
	print("4            {:.20f}        {:.20f}  ". format(y1[0],erroT[0]))
	print("10           {:.20f}        {:.20f}  ". format(y1[1],erroT[1]))
	print("50           {:.20f}        {:.20f}  ". format(y1[2],erroT[2]))
	print("100          {:.20f}        {:.20f}  ". format(y1[3],erroT[3]))
	print("150          {:.20f}        {:.20f}  ". format(y1[4],erroT[4]))
	print("200          {:.20f}        {:.20f}  ". format(y1[5],erroT[5]))
	print("300          {:.20f}        {:.20f}  ". format(y1[6],erroT[6]))
	print("400          {:.20f}        {:.20f}  ". format(y1[7],erroT[7]))
	print("500          {:.20f}        {:.20f}  ". format(y1[8],erroT[8]))
	print("600          {:.20f}        {:.20f}  ". format(y1[9],erroT[9]))
	print("700          {:.20f}        {:.20f}  ". format(y1[10],erroT[10]))
	print("800          {:.20f}        {:.20f}  ". format(y1[11],erroT[11]))
	print("900          {:.20f}        {:.20f}  ". format(y1[12],erroT[12]))
	print("-----------------------------------------------------------------")
	print("==> Regra de Simpson") 
	print("-----------------------------------------------------------------")
	print("n                    integral                             erro")
	print("-----------------------------------------------------------------")
	print("4            {:.20f}        {:.20f}  ". format(y2[0],erroS[0]))
	print("10           {:.20f}        {:.20f}  ". format(y2[1],erroS[1]))
	print("50           {:.20f}        {:.20f}  ". format(y2[2],erroS[2]))
	print("100          {:.20f}        {:.20f}  ". format(y2[3],erroS[3]))
	print("150          {:.20f}        {:.20f}  ". format(y2[4],erroS[4]))
	print("200          {:.20f}        {:.20f}  ". format(y2[5],erroS[5]))
	print("300          {:.20f}        {:.20f}  ". format(y2[6],erroS[6]))
	print("400          {:.20f}        {:.20f}  ". format(y2[7],erroS[7]))
	print("500          {:.20f}        {:.20f}  ". format(y2[8],erroS[8]))
	print("600          {:.20f}        {:.20f}  ". format(y2[9],erroS[9]))
	print("700          {:.20f}        {:.20f}  ". format(y2[10],erroS[10]))
	print("800          {:.20f}        {:.20f}  ". format(y2[11],erroS[11]))
	print("900          {:.20f}        {:.20f}  ". format(y2[12],erroS[12]))
	
	#Calcula a integral 7
			
	a=0
	b=math.pi
	w1=integral.integrais((integral.ruleoftrapezio),funcao7(),a,b,n) # é uma lista com os valores das integrais(trapezio) ordenada pelos intervalos
	w2=integral.integrais((integral.regraSimpson), funcao7(),a,b,n) # é uma lista com os valores das integrais(simpson) ordenada pelos intervalos
	valorExato=(3.14159265358979311600) #no arquivo é PI
	erroT=calculaErroTrapezio(valorExato,w1) #é uma lista com os erros
	erroS=calculaErroSimpson(valorExato,w2) #é uma lista com os erros
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print()
	print("Função: x*sin(x) , com a = 0 e b = pi")
	print("Valor exato:       {:.20f}".format(math.pi))
	print("==> Regra dos Trapézios")
	print("-----------------------------------------------------------------")
	print("n                    integral                             erro")
	print("-----------------------------------------------------------------")
	print("4            {:.20f}        {:.20f}  ". format(w1[0],erroT[0]))
	print("10           {:.20f}        {:.20f}  ". format(w1[1],erroT[1]))
	print("50           {:.20f}        {:.20f}  ". format(w1[2],erroT[2]))
	print("100          {:.20f}        {:.20f}  ". format(w1[3],erroT[3]))
	print("150          {:.20f}        {:.20f}  ". format(w1[4],erroT[4]))
	print("200          {:.20f}        {:.20f}  ". format(w1[5],erroT[5]))
	print("300          {:.20f}        {:.20f}  ". format(w1[6],erroT[6]))
	print("400          {:.20f}        {:.20f}  ". format(w1[7],erroT[7]))
	print("500          {:.20f}        {:.20f}  ". format(w1[8],erroT[8]))
	print("600          {:.20f}        {:.20f}  ". format(w1[9],erroT[9]))
	print("700          {:.20f}        {:.20f}  ". format(w1[10],erroT[10]))
	print("800          {:.20f}        {:.20f}  ". format(w1[11],erroT[11]))
	print("900          {:.20f}        {:.20f}  ". format(w1[12],erroT[12]))
	print("-----------------------------------------------------------------")
	print("==> Regra de Simpson") 
	print("-----------------------------------------------------------------")
	print("n                    integral                             erro")
	print("-----------------------------------------------------------------")
	print("4            {:.20f}        {:.20f}  ". format(w2[0],erroS[0]))
	print("10           {:.20f}        {:.20f}  ". format(w2[1],erroS[1]))
	print("50           {:.20f}        {:.20f}  ". format(w2[2],erroS[2]))
	print("100          {:.20f}        {:.20f}  ". format(w2[3],erroS[3]))
	print("150          {:.20f}        {:.20f}  ". format(w2[4],erroS[4]))
	print("200          {:.20f}        {:.20f}  ". format(w2[5],erroS[5]))
	print("300          {:.20f}        {:.20f}  ". format(w2[6],erroS[6]))
	print("400          {:.20f}        {:.20f}  ". format(w2[7],erroS[7]))
	print("500          {:.20f}        {:.20f}  ". format(w2[8],erroS[8]))
	print("600          {:.20f}        {:.20f}  ". format(w2[9],erroS[9]))
	print("700          {:.20f}        {:.20f}  ". format(w2[10],erroS[10]))
	print("800          {:.20f}        {:.20f}  ". format(w2[11],erroS[11]))
	print("900          {:.20f}        {:.20f}  ". format(w2[12],erroS[12]))



main()

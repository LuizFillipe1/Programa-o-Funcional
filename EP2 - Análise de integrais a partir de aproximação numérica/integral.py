import math
def ruleoftrapezio(fx,a,b,n,i=0,s=0):
	'''Essa funcao calcula a integral pelo método dos trapézios e retorna
	o seu valor'''
	deltax=(b-a)/n
	if i==n:
		valor=s*(deltax/2)
		return valor
	else:
		s+= fx(i*deltax) + fx((i+1)*deltax)
		return ruleoftrapezio(fx,a,b,n,i+1,s) 
		
def regraSimpson(fx,a,b,n,i=1,somapar=0,somaimpar=0):
	'''Essa funcao calcula a integral pelo método de Simpson e retorna
	o seu valor'''
	deltax=(b-a)/n
	if i<n:
		if i%2==0:
			somapar+= fx(i*deltax)
			return regraSimpson(fx,a,b,n,i+1,somapar,somaimpar)
		else:
			somaimpar+= fx(i*deltax)
			return regraSimpson(fx,a,b,n,i+1,somapar,somaimpar)
	else:
		valor=(deltax)/3 * (fx(a)+fx(b) + 4*somaimpar + 2* somapar)
		return valor


def integrais(funcaoTipo,f,a,b,L,i=0,r=[]):
	'''Essa é uma funcao que usa outra funcao como parametro.
	ela é resposavel por chamar a funcao que você quer e retornar
	uma lista com seus respectivos valores'''
	if i<len(L):
		n1=funcaoTipo(f,a,b,L[i])
		return integrais(funcaoTipo,f,a,b,L,i+1,r+[n1])
	else:
		return r
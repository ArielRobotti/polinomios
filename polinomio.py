def polinomio(coef, deriv=0, x=None):
	coefSal=coef
	for i in range(deriv):
		coefDeriv=[]
		for i,j in enumerate(coefSal[:-1]):
			coefDeriv.append((len(coefSal)-i-1)*j)
		coefSal=coefDeriv
	if x==None:
		return coefSal
	else:
		valor=0
		for i,j in enumerate(reversed(coefSal)):
			valor+= x**i*j
		return valor
#ejemplos...			
c=(2,3,2.5,-2,0.5,-7)	#coeficientes
der1=polinomio(c,deriv=1)
print('Coeficientes 1er derivada: ',der1)
puntoA=2
evalPuntoA=polinomio(der1,x=puntoA)
print('derivada 1ra evaluada en x=',puntoA,':',evalPuntoA)
der3=polinomio(c,deriv=3)
evalPuntoA=polinomio(der3,x=puntoA)
print('Derivada 3ra evaluada en x=',puntoA,':',evalPuntoA)

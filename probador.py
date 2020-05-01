#from polinomios import polinomio as pln
import time
import sympy
#--- Funcion para calcular derivadas ----------
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
#-----------------------------------------------
p= 4								#punto a evaluar
rep=int(1e3)							#repeticiones de los bucles for
difx=1e-9								#Delta de x para calcular la derivada usando limites

#--------- usando una funcion lambda -----------
f=lambda x: 2*x**3 + 4*x**2 - 5*x -9	#polinomio
inicio=time.time()
for i in range(rep):
	derLamb= (f(p+difx)-f(p))/difx

final=time.time()-inicio
print('\ntiempo usando una funcion lambda:, ',final*1e6/rep, 'uSeg\nValor=',derLamb)

#--------- usando la funcion polinomio --------
f=(2,4,-5,-9)				#coeficientes de 2*x**3 + 4*x**2 - 5*x -9
inicio=time.time()
for i in range(rep):
	derPol= polinomio(f,deriv=1,x=p)
	
final=time.time()-inicio
print('\ntiempo usando el modulo polinomio:, ',final*1e6/rep, 'uSeg\nValor=',derPol)
	
#--------- usando el modulo sympy  ------------
x=sympy.symbols('x')
f= 2*x**3 + 4*x**2 - 5*x -9		#polinomio	

inicio=time.time()
for i in range(rep):
	derSympy=sympy.diff(f).subs(x,p)
	
final=time.time()-inicio
print('\ntiempo usando el modulo sympy:, ',final*1e6/rep, 'uSeg\nValor=',derSympy,'\n')

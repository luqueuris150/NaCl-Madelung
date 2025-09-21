import math as m
import matplotlib.pyplot as plt

alpha = [] #Para computar a constante em diferentes truncamentos
l = [] #Para armazenar em quais valores de l1 em que aquele valor de alpha foi obtido. l2 sera sempre truncado em 19.

l1 = 1 #Define l1
l2 = 1 #Define l2
serie = 0 #Define a serie
s = 0 #Define o termo da serie que vai calcular termo a termo
a = 0 #Define o termo que será armazenado no alpha
while l1<20:
    while l2<20:
        #Implementa o termo da serie que encontramos
        s = m.exp(-m.pi*m.sqrt(l1*l1 + l2*l2))/((1+m.exp(-m.pi*m.sqrt(l1*l1 + l2*l2)))*(1+m.exp(-m.pi*m.sqrt(l1*l1 + l2*l2))))
        serie = serie + s #soma o que tinhamos antes com o que obtivemos agora
        l2 = l2 + 2 #Soma 2 ao valor de l2, pois estamos somando nos valores impares
        
    a = 48*m.pi*serie #Calcula o valor da constante de Madelung para cada truncamento em l1, com l2 sendo truncado sempre em l2 = 19 para cada l1.
    alpha.append(a) #Adiciona ao vetor alpha
    l.append(l1) #Adiciona ao vetor l
    l1 = l1 + 2 #Soma 2 ao l1, por estarmos somando nos valores impares

plt.plot(l,alpha, 'r') #Plota o gráfico de l por alpha
plt.xlabel('Valor de l1')
plt.ylabel('Valor da alpha')
plt.suptitle('Gráfico de alpha x l1, com l2 indo de 1 a 19')
plt.show()

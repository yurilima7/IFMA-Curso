import threading
import time 
       
x=0
lista=[]

def processo_0():
  global x
  
  for i in range(3):
    # NOSSO PROTOCOLO DE ENTRADA NA RC
    while x==1:
      print("ESPERA OCUPADA DE 00 POIS X=",x)
      time.sleep(2)
  
    print("Entrando na RC de 00...")
    tamanho=len(lista)
    #time.sleep(5)
    lista.insert(tamanho,f'Item_{tamanho}')
    print("Saindo da RC de 00...")
    x=1
    print('Entrando na R. NÃO C. 00')
      
def processo_1():
  global x
  
  for i in range(3):
      
    while x==0:
      print("ESPERA OCUPADA DE 01 POIS X=",x)
      time.sleep(2)
      
    print("Entrando na RC de 01...")
    tamanho=len(lista)
    
    lista.insert(tamanho,f'Item_{tamanho}') 
    print("Saindo da RC de 01")
    x=0
    
    for j in range(5):
      print('Entrando na R. NÃO C. 01')
      time.sleep(2)

print("INICIO")
threading.Thread(target = processo_0).start()
threading.Thread(target = processo_1).start()
print("Final")
print(lista)
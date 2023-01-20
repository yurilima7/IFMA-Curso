import threading
import time 

CA = False
CB = False
lista = []

def processo_1():
    global CA, CB
    
    for i in range(3):
        CA = True
        
        while(CB):
            print("ESPERA OCUPADA DE 01 POIS CB =",CB)
            time.sleep(2)
    
        print("Entrando na RC de 01...")
        tamanho=len(lista)
        
        lista.insert(tamanho,f'Item_{tamanho}')
        print("Saindo da RC de 01...")
        CA = False
        print('Entrando na R. NÃO C. 01')
        
def processo_2():
    global CA, CB
    
    for i in range(3):
        CB = True
        
        while(CA):
            print("ESPERA OCUPADA DE 02 POIS CA =",CA)
            time.sleep(2)
        
        print("Entrando na RC de 02...")
        tamanho=len(lista)
        
        lista.insert(tamanho,f'Item_{tamanho}')
        print("Saindo da RC de 02...")
        CB = False
        
        for j in range(5):
            print('Entrando na R. NÃO C. 02')
            time.sleep(2)
        
        
print("INICIO")
threading.Thread(target = processo_1).start()
threading.Thread(target = processo_2).start()
print("FINAL")
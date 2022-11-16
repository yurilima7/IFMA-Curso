import threading
import time 
       
multex = threading.Semaphore()
empty = threading.Semaphore(5)
full = threading.Semaphore(0)
list = []

def produtor():
  
  for i in range(5):
    empty.acquire() # down - verifica se a lista está vazia, testando se é igual a 0
    multex.acquire() # down 
    list.append(f'P1 - {i}')
    print('produzindo:', list)
    time.sleep(2)
    multex.release() # up
    full.release() # adicionando espaço
      
def consumidor():
  
  for i in range(5):
    full.acquire()
    multex.acquire() # down  
    list.pop()
    print('consumindo:', list)
    time.sleep(2)
    multex.release() # up
    empty.release()

print("INICIO")
threading.Thread(target = produtor).start()
threading.Thread(target = consumidor).start()
print("Final")

# interrupção é assincrona, pois pode ocorrer em qualquer periodo de tempo
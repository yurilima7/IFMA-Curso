import vrep
import keyboard
from pedrohj import *

# inicia a conexão com o vrep/coppelia e o robô a ser utilizado
robo = objeto()

# juntas do quadrúpede
j1 = []
j2 = []
j3 = []
j4 = []

# inserindo as juntas nas listas
for i in range (3):
    j1.append(robo.obter("rw_joint1_"+str(i+1)))

for i in range (3):
    j2.append(robo.obter("rw_joint2_"+str(i+1)))

for i in range (3):
    j3.append(robo.obter("rw_joint3_"+str(i+1)))

for i in range (3):
    j4.append(robo.obter("rw_joint4_"+str(i+1)))

# movimentos do robô
angulos = [[0,0,90], [60,-15,90], [60,0,90]]
angulos2 = [[0,0,90], [-60,-15,90], [-60,0,90]]

while True:
	# movimenta as patas da frente direita e fundo esquerda
	if keyboard.read_key() == "a":
		for i in range(3):
			for k in range(3):
				# setando os ângulos da movimentação
				robo.setPos(j1[k], angulos[i][k])
				robo.setPos(j4[k], angulos2[i][k])
				robo.delay(50)
				
	# movimenta as patas frente esquerda e fundo direita
	if keyboard.read_key() == "s":
		for i in range(3):
			for k in range(3):
				# setando os ângulos da movimentação
				robo.setPos(j3[k], angulos[i][k])
				robo.setPos(j2[k], angulos2[i][k])
				robo.delay(50)

	# encerra o programa
	if keyboard.read_key() == "e":
		break

	# impulso de movimentação
	robo.delay(50)
	robo.setPos(j1[0],-60) # pata frente - direita
	robo.setPos(j3[0],-60) # pata fundo - direita
	robo.setPos(j2[0], 60) # pata frente - esquerda
	robo.setPos(j4[0], 60) # pata fundo - esquerda
	robo.delay(50)
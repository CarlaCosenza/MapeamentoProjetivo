from numpy.linalg import inv
import numpy as np
from matriz import multiplicacaoMatriz, imprimirMatriz

def tratarPontos(pontos):
	newPontos = np.empty([12,1])
	for i in range(len(newPontos)):
		newPontos[i][0] = 0
	newPontos[0][0] = pontos[0][0]
	newPontos[1][0] = pontos[0][1]
	newPontos[2][0] = 1
	return newPontos

def getBigMatriz(pontos, length, height):
	bigMatriz = np.empty([12,12])
	for i in range(len(bigMatriz)):
		for j in range(len(bigMatriz[i])):
			bigMatriz[i][j] = 0

	bigMatriz[0][1] = height
	bigMatriz[0][2] = 1
	bigMatriz[1][4] = height
	bigMatriz[1][5] = 1
	bigMatriz[2][7] = height
	bigMatriz[2][8] = 1
	bigMatriz[3][0] = length
	bigMatriz[3][1] = height
	bigMatriz[3][2] = 1;
	bigMatriz[3][9] = -pontos[1][0]
	bigMatriz[4][3] = length
	bigMatriz[4][4] = height
	bigMatriz[4][5] = 1
	bigMatriz[4][9] = -pontos[1][1]
	bigMatriz[5][6] = length
	bigMatriz[5][7] = height
	bigMatriz[5][8] = 1
	bigMatriz[5][9] = -1
	bigMatriz[6][0] = length
	bigMatriz[6][2] = 1
	bigMatriz[6][10] = -pontos[2][0]
	bigMatriz[7][3] = length
	bigMatriz[7][5] = 1
	bigMatriz[7][10] = -pontos[2][1]
	bigMatriz[8][6] = length
	bigMatriz[8][8] = 1
	bigMatriz[8][10] = -1
	bigMatriz[9][2] = 1
	bigMatriz[9][11] = -pontos[3][0]
	bigMatriz[10][5] = 1
	bigMatriz[10][11] = -pontos[3][1]
	bigMatriz[11][8] = 1
	bigMatriz[11][11] = -1

	return bigMatriz;

def findTransformacao(pontos, length, height):
	bigMatriz = getBigMatriz(pontos, length, height)
	newPontos = tratarPontos(pontos)

	bigMatrizInversa = inv(bigMatriz)

	transformacaoEmLinha = multiplicacaoMatriz(bigMatrizInversa, newPontos)

	H = np.empty([3,3])
	for i in range(9):
		x = round((i-1)/3)
		y = i%3
		H[x][y] = transformacaoEmLinha[i][0]

	HInversa = inv(H)
	return HInversa

def fazerTransformacao(HInversa, x, y):
	pontos = np.array([[x], [y], [1]])
	return multiplicacaoMatriz(HInversa, pontos)

def isInImage(x, y, length, height):
	if(x > 0 and x < length):
		if(y > 0 and y < height):
			return True
	return False

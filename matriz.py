from numpy.linalg import inv
import numpy as np

def multiplicacaoMatriz(matrizA, matrizB):
	resposta = []
	for i in range(len(matrizA)):
		linha = np.empty(len(matrizB[i]))
		for j in range(len(matrizB[i])):
			conta = 0;
			for k in range(len(matrizB)):
				conta += matrizA[i][k]*matrizB[k][j]
			linha[j] = conta
		resposta.append(linha)
	return resposta

def imprimirMatriz(matrizA):
	for i in range(len(matrizA)):
		for j in range(len(matrizA[i])):
			print(matrizA[i][j], end = ' ')
		print("\n")

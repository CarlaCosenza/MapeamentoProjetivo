import cv2
import numpy as np
from transformacoes import findTransformacao, fazerTransformacao, isInImage
from matriz import imprimirMatriz

if __name__ == '__main__':
	
	# Imagens que vamos usar
	# imagemPrincipal = cv2.imread('TimesSquare.jpg')
	# imagemAuxiliar = cv2.imread('VinDisel.png')
	imagemPrincipal = cv2.imread('cinema.jpg')
	imagemAuxiliar = cv2.imread('nazare.jpg')

	# Imagem a ser gerada
	newImage = imagemPrincipal

	# Pontos da imagem principal da TimesSquare
	# ponto0 = [478, 548]
	# ponto1 = [763, 681]
	# ponto2 = [765, 414]
	# ponto3 = [483, 134]

	# Pontos da imagem principal do cinema
	ponto0 = [205, 278]
	ponto1 = [367,266]
	ponto2 = [366, 160]
	ponto3 = [202, 148]

	pontos = [ponto0, ponto1, ponto2, ponto3]

	# Achar transformacao
	transformacao = findTransformacao(pontos, imagemAuxiliar.shape[1], imagemAuxiliar.shape[0])

	# Mudar a imagem nova
	for j in range(newImage.shape[0]):
		for i in range(newImage.shape[1]):
			newPontos = fazerTransformacao(transformacao, i, j)
			y = int(newPontos[1][0]/newPontos[2]) 
			x = int(newPontos[0][0]/newPontos[2])
			if(isInImage(x, y, imagemAuxiliar.shape[1], imagemAuxiliar.shape[0])):
				newImage[j][i] = imagemAuxiliar[y][x]


	cv2.imshow("Teste", newImage)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


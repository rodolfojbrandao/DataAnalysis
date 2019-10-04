import os
import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt
import cv2
import statistics

path='/home/rodolfo/Desktop/imagens_processadas_R1_v1_ma'
#path='/home/rodolfo/Desktop/imagens_processadas'

os.chdir(path)

NF =  562   #numero de files
cel = 400
fao = []
dp4 = []
dp3 = []
media = []
dados = []

#separacao dos dados
for s in range (495,NF):
  img = plt.imread("imagem.{}.jpg".format(s))
  RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plt.axis("off")
  imagem = RGB_img[:,:,1]
  #print(s*100/NF)

  #determinando fracao de area ocupada
  cont_pt=0
  cont_bt=0
  for i in range (0,(imagem.shape[0])-1): #linhas
    for j in range (0,(imagem.shape[1])-1):  #colunas
        if imagem[i,j]<50:
            cont_pt=cont_pt+1
        if imagem[i,j]>200:
            cont_bt=cont_bt+1
  cont_b_p=cont_pt+cont_bt
  fao.append(cont_pt/(cont_b_p))

  #determinando concentração de pixel preto por celula
  contador1 = np.zeros((cel))
  contador2 = np.zeros((cel))
  contador = np.zeros((cel))
  rx = math.floor((imagem.shape[0])/cel**0.5)
  ry = math.floor((imagem.shape[1])/cel**0.5)
  k=-1
  for py in range (0,int(cel**0.5*ry),ry):
    for px in range (0,int(cel**0.5*rx),rx):
        k = k+1
        minimoX = px
        maximoX = px + rx
        minimoY = py
        maximoY = py + rx
        for n in range (minimoX, maximoX-3):
            for m in range(minimoY, maximoY-3):
                if imagem[m,n] > 200:
                    contador1[k] = contador1[k]+1
                if imagem[m,n] < 50:
                    contador2[k] = contador2[k]+1

  contador = contador1 + contador2
  #print(contador)
  l = -1
  Contador = []
  Contador2 = []
  C = []
  C3 = []
  for i in range(0,cel): #eliminando celulas na cor cinza
      if contador2[i] < 63:
        if contador[i] != 0:
            l=l+1
            Contador.append(contador[i].copy())
            Contador2.append(contador2[i].copy())
            C.append(Contador2[l]/Contador[l])


  plt.hist(Contador2, bins=20)
  plt.ylabel('Numero de particulas');
  plt.show()
  Contador2_def=pd.DataFrame(Contador2)
  print(Contador2_def.describe())
  #print(Contador2)
  #print(C)
  C_df = pd.DataFrame(C)
  #media = pd.DataFrame(C_df.mean())
  indice = pd.DataFrame(C_df.std())
  print(indice)
  #media.append(statistics.mean(C))
  #media_df = pd.DataFrame(media)
#md=statistics.mean(media)
#print(md)

  #determinando desvio padrao da amostra da população
  #dp4.append(statistics.stdev(C))
  #media.append(statistics.mean(C))
  #print(C)
  #print(dp4,type(dp4),len(dp4))
  #media=statistics.mean(C)
  #media=media .transpose()
  #print(media, type(media), len(media))
  #print(media)
  #C3=C.pop(2)
  #dp3.append(statistics.stdev(C))
  #media = pd.DataFrame(media)
  #dados = [fao,dp3,dp4,media]
  #dados=zip(*dados)
  #dados = pd.DataFrame(dados, columns=['fao','dp3','dp4','media'])

#dados.to_csv('teste.csv')

#C_df=pd.DataFrame(C)

#print(C)
#indice=pd.DataFrame(C_df.std())
#print(indice)

#dados.to_csv('teste2.csv')




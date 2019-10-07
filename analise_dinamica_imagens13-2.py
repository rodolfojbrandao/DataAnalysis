import os
import numpy as np
import pandas as pd
import math
from matplotlib import pyplot as plt
import cv2
import statistics
import time
start = time.time()

NF_0 = 541
NF_f =  560
cel = 400
numberI= NF_f-NF_0
numberD=1

#separacao dos dados
for d in range (0,numberD):
    path = "/home/rodolfo/Desktop/imagens{}".format(d)
    print(path)
    os.chdir(path)
    fao = np.zeros(numberI)
    dp = np.zeros(numberI)
    media = np.zeros(numberD)

    for s in range (NF_0,NF_f):
      img = plt.imread("imagem.{}.jpg".format(s))
      RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      plt.axis("off")
      imagem = RGB_img[:,:,1]
      #print(s*100/(NF_f))

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
      fao[s-NF_0]=cont_pt/(cont_b_p)

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
      vcel = contador/(2834.6*2834.6)

      # eliminando celulas na cor cinza
      position = np.nonzero(contador)
      Contador = np.copy(contador[position])
      Contador2 = np.copy(contador2[position])
      VCEL = np.copy(vcel[position])
      C = Contador2/Contador

      #determinando desvio padrao da amostra da população
      dp[s-NF_0]=np.std(C)
      dados = [fao,dp]
      dados=zip(*dados)
      dados = pd.DataFrame(dados, columns=['fao','dp'])


    media[d]=np.mean(dp)
    #print(media)
    media = pd.DataFrame(media)
    VCEL = pd.DataFrame(VCEL)
    #dados.to_csv('variaveis_fao_e_dp400cel.csv')
    #media.to_csv('media_de_dp400.csv')
    #VCEL.to_csv('volume_das_celulas.csv')
end = time.time()
print(end - start)



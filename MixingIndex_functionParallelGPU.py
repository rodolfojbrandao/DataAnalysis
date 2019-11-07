import pandas as pd
import numpy as np
import math
import cupy as cp

def ReadFile(ReadInput):
    NF=ReadInput[0]
    NP=ReadInput[1]
    N=ReadInput[2]
    a=ReadInput[3]
    posicaoX = cp.zeros((NP, NF))
    posicaoY = cp.zeros((NP, NF))
    posicaoZ = cp.zeros((NP, NF))
    Tipo = cp.zeros((NP, NF))
    inicio = int(a * NF / N)
    fim = int((a + 1) * NF / N)
    for j in range (inicio,fim):
        Dados = pd.read_csv('dados.{}.csv'.format(j))
        Tipo[:, j] = Dados.iloc[:, 1]
        posicaoX[:, j] = Dados.iloc[:, 3].copy()
        posicaoY[:, j] = Dados.iloc[:, 4].copy()
        posicaoZ[:, j] = Dados.iloc[:, 5].copy()
    posicaoX=pd.DataFrame(posicaoX)
    posicaoY=pd.DataFrame(posicaoY)
    posicaoZ=pd.DataFrame(posicaoZ)
    Tipo=pd.DataFrame(Tipo)
    return posicaoX, posicaoY, posicaoZ, Tipo


def CellCount(CellCountInput):
    posicaoX=CellCountInput[0]
    posicaoY=CellCountInput[1]
    posicaoZ=CellCountInput[2]
    Tipo=CellCountInput[3]
    v1=CellCountInput[4]
    v2=CellCountInput[5]
    NF=CellCountInput[6]
    a=CellCountInput[7]
    N=CellCountInput[8]
    v = 0.03 * 0.03 * 0.03
    rx = 5
    ry = 5
    rz = 10
    tamanho = rx * ry * rz - 1
    contador_tipo1 = pd.DataFrame(cp.zeros((tamanho, NF)))
    contador_tipo2 = pd.DataFrame(cp.zeros((tamanho, NF)))
    Volume = pd.DataFrame(cp.zeros((tamanho, NF)))
    posicao_vetor = 1
    max_x = float(posicaoX.iloc[:,[1]].max())
    max_y = float(posicaoY.iloc[:,[1]].max())
    max_z = float(posicaoZ.iloc[:,[1]].max())
    min_x = float(posicaoX.iloc[:,[1]].min())
    min_y = float(posicaoY.iloc[:,[1]].min())
    min_z = float(posicaoZ.iloc[:,[1]].min())
    gradeamentoX = (abs(max_x) + abs(min_x)) / rx
    gradeamentoY = (abs(max_y) + abs(min_y)) / ry
    gradeamentoZ = (abs(max_z) + abs(min_z)) / rz
    InferiorX=float(posicaoX.iloc[:,[1]].min())
    InferiorY=float(posicaoY.iloc[:,[1]].min())
    InferiorZ=float(posicaoZ.iloc[:,[1]].min())
    inicio = int(a * NF / N)
    fim = int((a + 1) * NF / N)
    for m in range(inicio, fim):
        p = 0
        q = 0,
        concluido = m / NF * 100
        print(concluido)
        for n in range(1, len(posicaoX)):
            px = math.floor((posicaoX.iloc[n, m] - min_x) / gradeamentoX)
            py = math.floor((posicaoY.iloc[n, m] - min_y) / gradeamentoY)
            pz = math.floor((posicaoZ.iloc[n, m] - min_z) / gradeamentoZ)
            posicao_vetor = -31 + px + 5 * py + 25 * pz

            if Tipo.iloc[n, m] < 1.5:
                contador_tipo1.iloc[posicao_vetor, m] = contador_tipo1.iloc[posicao_vetor, m] + 1
            else:
                contador_tipo2.iloc[posicao_vetor, m] = contador_tipo2.iloc[posicao_vetor, m] + 1
    Volume = contador_tipo1 * v1 / v * 100 + contador_tipo2 * v2 / v * 100
    return Volume, contador_tipo1, contador_tipo2


def GenerateFile(Volume, contador_tipo1, contador_tipo2,v1,v2,NF):
    cout1 = list()
    for n in range(0, len(Volume)):
        if Volume.iloc[n, NF - 1] > 5:
            cout1.append((contador_tipo1.iloc[n, :] * v1) / (
                        (contador_tipo1.iloc[n, :] * v1) + (contador_tipo2.iloc[n, :] * v2)))
    return cout1

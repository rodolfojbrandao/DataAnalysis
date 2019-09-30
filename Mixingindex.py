
import os
import numpy as np
import pandas as pd
from multiprocessing import Pool

N = 24 #number of cores
a = list(range(N))
NF = 8 #number of files
NP = 21522 #number of particles
raio1 = 0.0009
raio2 = 0.0021
rx = 5
ry = 5
rz = 10
tamanho = rx*ry*rz

velocidade_resultante = list()
contador1 = list()
contador2 = list()
contador = list()
np.linspace(0.1,49.0,NF)
posicaoX = np.zeros((NP,NF))
posicaoY = np.zeros((NP,NF))
posicaoZ = np.zeros((NP,NF))
Tipo = np.zeros((NP,NF))
Raio = np.zeros((NP,NF))
contador_tipo1 = np.zeros((tamanho,NF))
contador_tipo2 = np.zeros((tamanho,NF))
velocidade_tipo1 = np.zeros((tamanho,NF))
velocidade_tipo2 = np.zeros((tamanho,NF))
posicao_vetor = 1

path='/home/rodolfo/Desktop/dados'
os.chdir(path)

def f(a):
    inicio = int(a*NF/N)
    fim = int((a+1)*NF/N)
    for j in range(inicio,fim):
            Dados = pd.read_csv('dados.{}.csv'.format(j))
            posicaoX[:, j] = Dados.iloc[:, 6].copy()
            posicaoY[:,j] = Dados.iloc[:, 7].copy()
            posicaoZ[:,j] = Dados.iloc[:, 8].copy()
            Tipo[:,j] = Dados.iloc[:, 1].copy()
            Raio[:,j] = Dados.iloc[:, 5].copy()
            #vx = Dados.iloc[:, 2].copy()
            #vy = Dados.iloc[:, 3].copy()
            #vz = Dados.iloc[:, 4].copy()
            print(posicaoY)
            print('========================================================================')
    return posicaoX#, posicaoY, posicaoZ, Tipo, Raio
            #for i in range(row):
             #   velocidade_resultante[i,j] = Dados.iloc[i, 2]*Dados.iloc[i, 2]+Dados.iloc[i, 3]*Dados.iloc[i, 3]+Dados.iloc[i, 4]*Dados.iloc[i, 4]
    #print(velocidade_resultante)
if __name__=='__main__':
    Tarefas=len(a)
    with Pool(Tarefas) as p:
        p.map(f,a)


h = pd.DataFrame(f(2))
print(h)

"""velocidade_resultante(:, k) = [(M(2:$, 3). ^ 2 + M(2:$, 4).^ 2 + M(2:$, 5).^ 2).^ 0.5];

V_medio = mean(velocidade_resultante, 'r');

gradeamentoX = (max(posicaoX) - min(posicaoX)) / rx;
gradeamentoY = (max(posicaoY) - min(posicaoY)) / ry;
gradeamentoZ = (max(posicaoZ) - min(posicaoZ)) / rz;


for m=1:max(tempo) * 10
p = 0;
q = 0;
for n=1:size(posicaoX, 'r')
for pz = 1:rz
for py = 1:ry
for px = 1:rx
if posicaoX(n, m) > (min(posicaoX) + (px - 1) * gradeamentoX) & ..
posicaoX(n, m) < (min(posicaoX) + px * gradeamentoX) &..
posicaoY(n, m) > (min(posicaoY) + (py - 1) * gradeamentoY) &..
posicaoY(n, m) < (min(posicaoY) + py * gradeamentoY) &..
posicaoZ(n, m) > (min(posicaoZ) + (pz - 1) * gradeamentoZ) &..
posicaoZ(n, m) < (min(posicaoZ) + pz * gradeamentoZ)
posicao_vetor = -30 + px + 5 * py + 25 * pz
if Tipo(n, m) < 1.5
    contador_tipo1(posicao_vetor, m) = contador_tipo1(posicao_vetor, m) + 1
p = p + 1
velocidade_tipo1(p, m) = velocidade_resultante(n, m)
else
contador_tipo2(posicao_vetor, m) = contador_tipo2(posicao_vetor, m) + 1
q = q + 1
velocidade_tipo2(q, m) = velocidade_resultante(n, m)
end
else
contador_tipo1(posicao_vetor, m) = contador_tipo1(posicao_vetor, m) + 0
contador_tipo2(posicao_vetor, m) = contador_tipo2(posicao_vetor, m) + 0
end

end
end
end
end
end

contador_total = contador_tipo1 + contador_tipo2
V_tipo1 = mean(velocidade_tipo1, 1)
V_tipo2 = mean(velocidade_tipo2, 1)

for m=1:max(tempo) * 10
j = 0
for n=1:tamanho
if contador_total(n, m) > mean(contador_total)
    j = j + 1
    contador1(j, m) = contador_tipo1(n, m)
    contador2(j, m) = contador_tipo2(n, m)
    contador(j, m) = contador_total(n, m)
end
end
end
cout1 = contador1. * (4 / 3 * % pi * raio1 ^ 3);
cout2 = contador2. * (4 / 3 * % pi * raio2 ^ 3);
cout_total = cout1 + cout2;
for c = 1:size(cout_total, 'c')
for l = 1:size(cout_total, 'r')
if cout_total(l, c) <> 0
    indice(l, c) = cout1(l, c) / (cout_total(l, c));
end
end
end
index = stdev(indice, 'r')
count1 = contador_tipo1. * (4 / 3 * % pi * raio1 ^ 3)
count2 = contador_tipo2. * (4 / 3 * % pi * raio2 ^ 3)
count_total = count1 + count2


//camada 01
for c = 1:size(count_total,'c')
	p1 = 0;
	p2 = 0;
	p3 = 0;
	p4 = 0;
	p5 = 0;
	p6 = 0;
	p7 = 0;
	p8 = 0;
	p9 = 0;
	p10 = 0;

    for l = 1:25
        if count_total(l,c) <> 0
           p1 = p1+1;
           indice01(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 26:50
        if count_total(l,c) <> 0
           p2 = p2+1;
           indice02(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 51:75
        if count_total(l,c) <> 0
           p3 = p3+1;
           indice03(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 76:100
        if count_total(l,c) <> 0
           p4 = p4+1;
           indice04 (p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 101:125
        if count_total(l,c) <> 0
           p5 = p5+1;
           indice05(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 126:150
        if count_total(l,c) <> 0
           p6 = p6+1;
           indice06(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

   for l = 151:175
        if count_total(l,c) <> 0
           p7 = p7+1;
           indice07(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 176:200
        if count_total(l,c) <> 0
           p8 = p8+1;
           indice08(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 201:225
        if count_total(l,c) <> 0
           p9 = p9+1;
           indice09(p,c)=count1(l,c)/(count_total(l,c));
        end
    end

    for l = 226:250
        if count_total(l,c) <> 0
           p10 = p10+1;
           indice10(p,c)=count1(l,c)/(count_total(l,c));
        end
    end


end

index01 = stdev(indice01,'r')
index02 = stdev(indice02,'r')
index03 = stdev(indice03,'r')
index04 = stdev(indice04,'r')
index05 = stdev(indice05,'r')
index06 = stdev(indice06,'r')
index07 = stdev(indice07,'r')
index08 = stdev(indice08,'r')
index09 = stdev(indice09,'r')
index10 = stdev(indice10,'r')

//segregacao axial ============================================================
for m=1:max(tempo)*10
seg_axial01(:,m) = sum(contador_tipo1(1:25,m),1)/max(sum(contador_tipo1,1));
seg_axial02(:,m) = sum(contador_tipo1(26:50,m),1)/max(sum(contador_tipo1,1));
seg_axial03(:,m) = sum(contador_tipo1(51:75,m),1)/max(sum(contador_tipo1,1));
seg_axial04(:,m) = sum(contador_tipo1(76:100,m),1)/max(sum(contador_tipo1,1));
seg_axial05(:,m) = sum(contador_tipo1(101:125,m),1)/max(sum(contador_tipo1,1));
seg_axial06(:,m) = sum(contador_tipo1(126:150,m),1)/max(sum(contador_tipo1,1));
seg_axial07(:,m) = sum(contador_tipo1(151:175,m),1)/max(sum(contador_tipo1,1));
seg_axial08(:,m) = sum(contador_tipo1(176:200,m),1)/max(sum(contador_tipo1,1));
seg_axial09(:,m) = sum(contador_tipo1(201:225,m),1)/max(sum(contador_tipo1,1));
seg_axial10(:,m) = sum(contador_tipo1(226:250,m),1)/max(sum(contador_tipo1,1));
end

// escrever dados em arquivo csv ==============================================
dados = [tempo V_medio' V_tipo1' V_tipo2' index' index01' index02' index03' ..
         index04' index05' index06' index07' index08' index09' index10' seg_axial01' ..
         seg_axial02' seg_axial03' seg_axial04' seg_axial05' seg_axial06' seg_axial07' ..
         seg_axial08' seg_axial09' seg_axial10'];         
filename = fullfile(Directory, "dados08.csv");
csvWrite(dados, filename);"""
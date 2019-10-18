N=8
NF = 100 #number of files
NP = 7382 #number of particles
ReadInput=[]

#Read input list ==================================
for i in range (N):
	ReadInput.append([NF,NP,N,i])

print(ReadInput)
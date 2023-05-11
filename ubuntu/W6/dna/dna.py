import sys
import csv

arq = open(f"{sys.argv[2]}", "r")

dna = arq.read()

disc = {"AGATC": 0, "TTTTTTCT": 0, "AATG": 0, "TCTAG": 0, "GATA": 0, "TATC": 0, "GAAA": 0, "TCTG": 0}
disc2 = {"AGATC": 0, "TTTTTTCT": 0, "AATG": 0, "TCTAG": 0, "GATA": 0, "TATC": 0, "GAAA": 0, "TCTG": 0}
escolhido = 0
dados = []
lista = []
tmp = 0
tmp2 = 0
p = ''
x = []
count2 = 0
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for i in reader: 
        dados.append(i)

p = [dna.find("AATG"), dna.find("GATA"), dna.find("GAAA"), dna.find("TATC"), dna.find("TCTG")]    

for i in p:
    if i != -1:
        x.append(i)
        
p = sorted(x)
try:
    p = p[0]
except:
    p = 0

while True:
    if count2 == 0:
        tmp2 = p
    if dna[tmp2:tmp2+4] in disc.keys():
        lista = dna[tmp2:tmp2+4]
        if lista != tmp:
            disc2[tmp] = 0
        for i in disc.keys():
            if lista == i:
                disc2[i] += 1
                tmp = i
        if disc2[lista] > disc[lista]:
            disc[lista] = disc2[lista]
    else:
        disc2[tmp] = 0
    if dna[tmp2+4:tmp2+8] in disc.keys():
        tmp2 += 4
    else:
        tmp2 += 1
    count2 += 1
    if tmp2 == len(dna):
        break
            
count2 = 0

p = [dna.find("AGATC"), dna.find("TCTAG")]
x = []

for i in p:
    if i != -1:
        x.append(i)
        
p = sorted(x)

try:
    p = p[0]
except:
    p = 0

while True:
    if count2 == 0:
        tmp2 = p
    if dna[tmp2:tmp2+5] in disc.keys():
        lista = dna[tmp2:tmp2+5]
        if lista != tmp:
            disc2[tmp] = 0
        for i in disc.keys():
            if lista == i:
                disc2[i] += 1
                tmp = i
        if disc2[lista] > disc[lista]:
            disc[lista] = disc2[lista]
    else:
        disc2[tmp] = 0
    if dna[tmp2+5:tmp2+10] in disc.keys():
        tmp2 += 5
    else:
        tmp2 += 1
    count2 += 1
    if tmp2 == len(dna):
        break

count2 = 0
p = dna.find("TTTTTTCT")

if p == -1:
    p = 0

while True:
    if count2 == 0:
        tmp2 = p
    if dna[tmp2:tmp2+8] in disc.keys():
        lista = dna[tmp2:tmp2+8]
        if lista != tmp:
            disc2[tmp] = 0
        for i in disc.keys():
            if lista == i:
                disc2[i] += 1
                tmp = i
        if disc2[lista] > disc[lista]:
            disc[lista] = disc2[lista]
    else:
        disc2[tmp] = 0
    if dna[tmp2+8:tmp2+16] in disc.keys():
        tmp2 += 8
    else:
        tmp2 += 1
    count2 += 1
    if tmp2 == len(dna):
        break

verificador = False

for c in range(0, len(dados)):
    for r in dados[c].keys():
        if r != "name":
            if int(dados[c][r]) == disc[r]:
                verificador = True
                escolhido = c
            else:
                verificador = False
                break
    if verificador == True:
        break


if verificador == False:
    print("No match")
else:
    print(dados[escolhido]["name"])
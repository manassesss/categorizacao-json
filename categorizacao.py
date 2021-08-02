import json
from typing import Dict
from numpy import rint
import pandas as pd

#carregando  o arquivo .json
with open("teresinense-digital-unidades_new-export.json", "r", encoding="utf8") as json_file:
    u1 = json.load(json_file)

#lista de chaves geradas pelo firebase anteriormente
u1_keys = []
#dicionario com as novas chaves
u2 = {}
#novas chaves
cont = 0
#teste para salvar
save = {}
#salvando as chaves geradas pelo firebase em na lista de chaves
for i in u1:
    u1_keys.append(i)

#salvando com os ids novos em outro dicionario
for i in u1_keys:
    u2[cont] = u1[i]
    cont+=1

for i in u2:
    name = u2[i]['name'].split()
    if ("CREAS" in name):
         save[i] = u2[i]

for i in save:
    name = save[i]['name'].split()
    if "CREAS" in name:
        save[i]['categoria'] = 'CREAS'
        
print(save)
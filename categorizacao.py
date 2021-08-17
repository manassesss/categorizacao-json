'''
ARQUIVO TESTE PARA AS AS FUNÇÕES IMPLEMENTADAS NO ARQUIVO Categorias.py
author: Manassés Silva
'''
import json
from typing import Dict
from numpy import rint
import pandas as pd

#carregando  o arquivo .json
with open("final.json", "r", encoding="utf8") as json_file:
    u1 = json.load(json_file)

#lista de chaves geradas pelo firebase anteriormente
u1_keys = []
#dicionario com as novas chaves
u2 = {}
#novas chaves
cont = 0
#teste para salvar
save = {'Educacao': []}
part = {'icon': '', 'lat': '', 'long': '', 'name': '', 'unidade': ''}
#salvando as chaves geradas pelo firebase em na lista de chaves
for i in u1:
    u1_keys.append(i)

#salvando com os ids novos em outro dicionario
for i in u1_keys:
    u2[cont] = u1[i]
    cont+=1



for i in u2:
    print(i)
    classe = u2[i]['classe'].split()
    if ("Educacao" in classe):
        part = u2[i]
         
        save['Educacao'].append(part)

with open("test.json", "w", encoding="utf8") as json_outfile:
    json.dump(save, json_outfile, ensure_ascii=False,indent=4)


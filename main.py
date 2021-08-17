'''
author: Manassés Silva
'''
import Categorias
import argparse
import json

# Pegando as informações ao executar o arquivo
parser = argparse.ArgumentParser(description="Pressione \'esc\' para sair.")
parser.add_argument('-j', '--json', help="arquivo json para classificação", required=True)
args = parser.parse_args()

# Abrindo arquvio que foi passado na entrada
with open(args.json, "r", encoding="utf8") as json_file:
    arquivo_original = json.load(json_file)

u1_keys = []
u2 = {}
cont = 0
for i in arquivo_original:
    u1_keys.append(i)
for i in u1_keys:
    u2[cont] = arquivo_original[i]
    cont+=1

# Declarando os objetos de acordo com as classes disponiveis
E = Categorias.Educacao()
L = Categorias.EsporteELazer()
A = Categorias.Assistencia_Social()
S = Categorias.Saude()
M = Categorias.Meio_Ambiente()
N = Categorias.Saneamento()
P = Categorias.Predios_Publicos()
O = Categorias.Outros()
C = Categorias.Cultura()

# Classificando por classes.

E.classificarClasse(u2)
E.classificarUnidade()

L.classificarClasse(u2)
L.classificarUnidade()

A.classificarClasse(u2)
A.classificarUnidade()

S.classificarClasse(u2)
S.classificarUnidade()

M.classificarClasse(u2)
M.classificarUnidade()

N.classificarClasse(u2)
N.classificarUnidade()

P.classificarClasse(u2)
P.classificarUnidade()

O.classificarClasse(u2)
O.classificarUnidade()

C.classificarClasse(u2)
C.classificarUnidade()

E.classificarFinal()
L.classificarFinal()
A.classificarFinal()
S.classificarFinal()
M.classificarFinal()
N.classificarFinal()
P.classificarFinal()
C.classificarFinal()

O.classificarFinal()


with open("final.json", "w", encoding="utf8") as json_outfile:
    json.dump(C.final, json_outfile, ensure_ascii=False,indent=4)

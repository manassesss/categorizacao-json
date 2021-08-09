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

# Declarando os objetos de acordo com as classes disponiveis
E = Categorias.Educacao()
L = Categorias.EsporteELazer()
A = Categorias.Assistencia_Social()
S = Categorias.Saude()
M = Categorias.Meio_Ambiente()
N = Categorias.Saneamento()

# Classificando por classes.

E.classificarClasse(arquivo_original)
E.classificarUnidade()

L.classificarClasse(arquivo_original)
L.classificarUnidade()

A.classificarClasse(arquivo_original)
A.classificarUnidade()

S.classificarClasse(arquivo_original)
S.classificarUnidade()

M.classificarClasse(arquivo_original)
M.classificarUnidade()

N.classificarClasse(arquivo_original)
N.classificarUnidade()


with open("final.json", "w", encoding="utf8") as json_outfile:
    json.dump(S.save, json_outfile, ensure_ascii=False,indent=4)

import Categorias
import argparse

parser = argparse.ArgumentParser(description="Pressione \'esc\' para sair.")
parser.add_argument('-j', '--json', help="arquivo jason para classificação", required=True)
args = parser.parse_args()

E = Categorias.Educacao()
L = Categorias.EsporteELazer()
A = Categorias.Assistencia_Social()
S = Categorias.Saude()



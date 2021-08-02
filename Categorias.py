import json
from abc import ABC, abstractmethod

class Categoria (ABC):
    save = {}
    @abstractmethod
    def classificarClasse():
        pass
    
    def classificarCategoria():
        pass
    
class Assistencia_Social(Categoria):
    def classificarClasse(self, dicionario):
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("CREAS" in name) or ("CRAS" in name) or ("Abrigo" in name) or ("CentroPOP" in name) or ("CentroDia" in name) or ("SEMCASPI" in name) or ("CentrodeConvivência" in name):
                save[i] = dicionario[i]
                save[i]['classe'] = "Assistência Social"
    
    def classificarCategoria():
        for i in save:
            name = save[i]['name'].split()
            if "CREAS" in name:
                save[i]['categoria'] = 'CREAS'
            if "CRAS" in name:
                save[i]['categoria'] = 'CRAS'
            if "Abrigo" in name:
                save[i]['categoria'] = 'Abrigo'
            if "CentroPOP" in name:
                save[i]['categoria'] = 'CentroPOP'
            if "CentroDia" in name or "Centro-Dia" in name:
                save[i]['categoria'] = 'CentroDia'
            if "CentrodeConvivência" in name:
                save[i]['categoria'] = 'CentrodeConvivência'

class Saude(Categoria):
    def classificarClasse(self, dicionario):
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Hospital" in name) or ("Posto" in name) :
                save[i] = dicionario[i]

class Educacao(Categoria):
    def classificarClasse(self, dicionario):
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Escola" in name) or ("Bibilioteca" in name) :
                save[i] = dicionario[i]
                

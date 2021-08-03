import json
from abc import ABC, abstractmethod

class Categoria (ABC):
    save = {}
    @abstractmethod
    def classificarClasse():
        pass
    
    def classificarUnidade():
        pass
    
class Assistencia_Social(Categoria):
    
    def classificarClasse(self, dicionario):
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("CREAS" in name) or ("CRAS" in name) or ("Abrigo" in name) or ("CentroPOP" in name) or ("CentroDia" in name) or ("SEMCASPI" in name) or ("CentrodeConvivência" in name) :
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Assistência Social"
    
    def classificarUnidade(self):
        for i in self.save:
            name = self.save[i]['name'].split()
            if "CREAS" in name:
                self.save[i]['unidade'] = 'CREAS'
            if "CRAS" in name:
                self.save[i]['unidade'] = 'CRAS'
            if "Abrigo" in name:
                self.save[i]['unidade'] = 'Abrigo'
            if "CentroPOP" in name:
                self.save[i]['unidade'] = 'Centro POP'
            if "CentroDia" in name or "Centro-Dia" in name:
                self.save[i]['unidade'] = 'Centro Dia'
            if "CentrodeConvivência" in name:
                self.save[i]['unidade'] = 'Centro de Convivência'
            

class Saude(Categoria):
    
    def classificarClasse(self, dicionario):
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Hospital" in name) or ("UBS" in name) or ("SAMU" in name) :
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Saúde"
    
    def classificarUnidade(self):
        for i in self.save:
            name = self.save[i]['name'].split()
            if "Hospital" in name:
                self.save[i]['unidade'] = 'Hospital'
            if "UBS" in name:
                self.save[i]['unidade'] = 'UBS'
            if "SAMU" in name:
                self.save[i]['unidade'] = 'SAMU'
           
class Educacao(Categoria):
    
    def classificarClasse(self, dicionario):
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Escola" in name) or ("Bibilioteca" in name) or ("CMEI" in name) or ("E.M." in name) or ("Creche" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Educação"
    
    def classificarUnidade(self):
        for i in self.save:
            name = self.save[i]['name'].split()
            if "Escola" in name or "E.M." in name:
                self.save[i]['unidade'] = 'Escola'
            if "Bibilioteca" in name:
                self.save[i]['unidade'] = 'Bibilioteca'
            if "CMEI" in name:
                self.save[i]['unidade'] = 'CMEI'
            if "Creche" in name:
                self.save[i]['unidade'] = 'Creche'
            

class EsporteELazer(Categoria):
    
    def classificarClasse(self, dicionario):
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Praca" in name) or ("Praça" in name) or ("Ginásio" in name) or ("CEU" in name) or ("Parque" in name) or ("CampoSociety" in name) or ("CampoOficial" in name) or ("AcademiadaTerceiraIdade" in name) or ("AcademiaaoArLivre" in name) or ("Quadra" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Esporte e Lazer"
    
    def classificarUnidade(self):
        for i in self.save:
            name = self.save[i]['name'].split()
            if "Praca" in name or "Praça" in name:
                self.save[i]['unidade'] = 'Praça'
            if "Ginásio" in name:
                self.save[i]['unidade'] = 'Ginásio'
            if "CEU" in name:
                self.save[i]['unidade'] = 'CEU'
            if "Parque" in name:
                self.save[i]['unidade'] = 'Parque'
            if "CampoSociety" in name:
                self.save[i]['unidade'] = 'Campo Society'
            if "CampoOficial" in name:
                self.save[i]['unidade'] = 'Campo Oficial'
            if "CampoOficial" in name:
                self.save[i]['unidade'] = 'Campo Oficial'
            if "AcademiadaTerceiraIdade" in name:
                self.save[i]['unidade'] = 'Academia da Terceira Idade'
            if "AcademiaaoArLivre" in name:
                self.save[i]['unidade'] = 'Academia ao Ar Livre'
            if "Quadra" in name:
                self.save[i]['unidade'] = 'Quadra'
            

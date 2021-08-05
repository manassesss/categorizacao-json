'''
author: Manassés Silva
'''
import json
from abc import ABC, abstractmethod

class Categoria (ABC):
    '''
    :classe Categoria: Responsável por conter os metodos e variaveis que categorizarão e salvarão os dados do JSON.
    :parametros none:
    :metodos: classificarClasse(), classificarUnidade()
    '''
    @abstractmethod
    def classificarClasse():
        
        pass
    
    def classificarUnidade():
        pass
    
class Assistencia_Social(Categoria):
    save = {}
    '''
    :classe Assistencia_Social: Responsável por conter os metodos e variaveis que categorizarão 
                                e salvarão os dados do JSON de acordo a classificação Assistência Social.
    :parametros none:
    :metodos: classificarClasse(), classificarUnidade()
    '''
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Assistência Social
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("CREAS" in name) or ("CRAS" in name) or ("Abrigo" in name) or ("CentroPOP" in name) or ("CentroDia" in name) or ("SEMCASPI" in name) or ("CentrodeConvivência" in name) :
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Assistencia Social"
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias CREAS, 
        CRAS, Abrigo, Centro POP, Centro Dia, Centro de Convivência.
        
        :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                    JSON com as alterações feitas.
        :retorno save: Retorna o o dicionario save com as informações novas
        '''
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
    save = {}
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Saúde
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Hospital" in name) or ("UBS" in name) or ("SAMU" in name) :
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Saúde"
        
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Hospital, 
        UBS, SAMU.
        
        :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                    JSON com as alterações feitas.
        :retorno save: Retorna o o dicionario save com as informações novas
        '''
        for i in self.save:
            name = self.save[i]['name'].split()
            if "Hospital" in name:
                self.save[i]['unidade'] = 'Hospital'
            if "UBS" in name:
                self.save[i]['unidade'] = 'UBS'
            if "SAMU" in name:
                self.save[i]['unidade'] = 'SAMU'
        return self.save
           
class Educacao(Categoria):
    save = {}
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Educação
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Escola" in name) or ("Bibilioteca" in name) or ("CMEI" in name) or ("E.M." in name) or ("Creche" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Educacao"
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Escola,
        Bibilioteca, CMEI, Creche.
        
        :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                    JSON com as alterações feitas.
        :retorno save: Retorna o o dicionario save com as informações novas
        '''
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
    save = {}
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Esporte E Lazer
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Praca" in name) or ("Praça" in name) or ("Ginásio" in name) or ("CEU" in name) or ("Parque" in name) or ("CampoSociety" in name) or ("CampoOficial" in name) or ("AcademiadaTerceiraIdade" in name) or ("AcademiaaoArLivre" in name) or ("Quadra" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Esporte e Lazer"
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Praça,
        Ginásio, CEU, Parque, Campo Society, Campo Oficial, Academia da Terceira Idade, Academia ao Ar Livre, 
        Quadra
        
        :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                    JSON com as alterações feitas.
        :retorno save: Retorna o o dicionario save com as informações novas
        '''
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
            
class Predio_Publicos(Categoria):
    save = {}
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Predios Publicos
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("SEMEC" in name) or ("SEMCOP" in name) or ("SEMAM" in name) or ("SEMA" in name) or ("PRODATER" in name) or ("SEMPLAN" in name)or ("PGM" in name) or ("IPMT" in name)or ("SEMDUH" in name)or ("SEMCASPI" in name)or ("SEMCOP" in name) or ("SEMDEC" in name)or ("SEMEST" in name) or ("SEMEL" in name) or ("SEMPOM" in name) or ("SEMJUV" in name) or ("STRANS" in name) or ("FMS" in name)or ("ARSETE" in name)or ("SDR" in name)or ("FMC" in name)or ("FWF" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Educacao"
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso as categorias seriam todas as unidades
        que correspondem a um orgão público. Isso vai desde Secretarias a Cartórios.
        
        :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                    JSON com as alterações feitas.
        :retorno save: Retorna o o dicionario save com as informações novas
        '''
        for i in self.save:
            name = self.save[i]['name'].split()
            if "SEMCOP" in name:
                self.save[i]['unidade'] = 'SEMCOP'
            if "SEMAM" in name:
                self.save[i]['unidade'] = 'SEMAM'
            if "SEMA" in name:
                self.save[i]['unidade'] = 'SEMA'
            if "PRODATER" in name:
                self.save[i]['unidade'] = 'PRODATER'
            if "PGM" in name:
                self.save[i]['unidade'] = 'PGM'
            if "IPMT" in name:
                self.save[i]['unidade'] = 'IPMT'
            if "SEMDUH" in name:
                self.save[i]['unidade'] = 'SEMDUH'
            if "SEMCASPI" in name:
                self.save[i]['unidade'] = 'SEMCASPI'
            if "SEMCOP" in name:
                self.save[i]['unidade'] = 'SEMCOP'
            if "SEMEST" in name:
                self.save[i]['unidade'] = 'SEMEST'
            if "SEMDEC" in name:
                self.save[i]['unidade'] = 'SEMDEC'
            if "SEMEL" in name:
                self.save[i]['unidade'] = 'SEMEL'
            if "SEMPOM" in name:
                self.save[i]['unidade'] = 'SEMPOM'
            if "SEMJUV" in name:
                self.save[i]['unidade'] = 'SEMJUV'
            if "STRANS" in name:
                self.save[i]['unidade'] = 'STRANS'
            if "FMS" in name:
                self.save[i]['unidade'] = 'FMS'
            if "FWF" in name:
                self.save[i]['unidade'] = 'FWF'
            if "FMC" in name:
                self.save[i]['unidade'] = 'FMC'
            if "SDR" in name:
                self.save[i]['unidade'] = 'SDR'
            if "ARSETE" in name:
                self.save[i]['unidade'] = 'ARSETE'
            
class Meio_Ambiente(Categoria):
    
        save = {}
        def classificarClasse(self, dicionario):
            '''
            Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Meio Ambiente
            
            :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
            :retorno none: Não retorna nada ainda.
            '''
            for i in dicionario:
                name = dicionario[i]['name'].split()
                if ("PEV" in name):
                    self.save[i] = dicionario[i]
                    self.save[i]['classe'] = "Educacao"
        
        def classificarUnidade(self):
            '''
            Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias PEV (Pontos de Entrega Voluntaria)
            
            :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                        JSON com as alterações feitas.
            :retorno save: Retorna o o dicionario save com as informações novas
            '''
            for i in self.save:
                name = self.save[i]['name'].split()
                if "PEV" in name :
                    self.save[i]['unidade'] = 'PEV'
                
                
        
            
    
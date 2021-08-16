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
    save = {}
    @abstractmethod
    def classificarClasse():
        
        pass
    
    def classificarUnidade():
        pass
    
    def classificarFinal():
        pass
    
class Assistencia_Social(Categoria):
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Assistência Social
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("CREAS" in name) or ("CRAS" in name) or ("Abrigo" in name) or ("CentroPOP" in name) or ("CentroDia" in name) or ("SEMCASPI" in name) or ("CentrodeConvivência" in name) or ("Conselho Tutelar" in name) or ("AssociaçãodosAmigosAutistas" in name) or ("LAC" in name) or ("ASA/" in name) or ("APAE" in name) or ("APADA" in name) or ("ACEP" in name) in ("Casade" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Assistencia Social"
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias CREAS, 
        CRAS, Abrigo, Centro POP, Centro Dia, Centro de Convivência, Conselho Tutelar, AMA, LAC, ASA, APAE, APADA, Casa de 
        
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
            if "ConselhoTutelar" in name:
                self.save[i]['unidade'] = 'Conselho Tutelar'
            if "AssociaçãodosAmigosAutistas" in name:
                self.save[i]['unidade'] = 'AMA'
            if "LAC" in name:
                self.save[i]['unidade'] = 'LAC'
            if "ASA/" in name:
                self.save[i]['unidade'] = 'ASA/'
            if "APAE" in name:
                self.save[i]['unidade'] = 'APAE'
            if "APADA" in name:
                self.save[i]['unidade'] = 'APADA'
            if "ACEP" in name:
                self.save[i]['unidade'] = 'ACEP'
            if "Libras" in name:
                self.save[i]['unidade'] = 'Libras'
            if "Casade" in name:
               self.save[i]['unidade'] = 'Casa'
    
    def classificarFinal(self):
        pass

class Saude(Categoria):
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
                self.save[i]['classe'] = "Saude"
        
    
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
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Educação
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Escola" in name) or ("Biblioteca" in name) or ("CMEI" in name) or ("E.M." in name) or ("Creche" in name) or ("CentrodeCapacitação" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Educacao"
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Escola,
        Biblioteca, CMEI, Creche, Centro de Capacitação
        
        :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                    JSON com as alterações feitas.
        :retorno save: Retorna o o dicionario save com as informações novas
        '''
        for i in self.save:
            name = self.save[i]['name'].split()
            if "Escola" in name or "E.M." in name:
                self.save[i]['unidade'] = 'Escola'
            if "Biblioteca" in name:
                self.save[i]['unidade'] = 'Biblioteca'
            if "CMEI" in name:
                self.save[i]['unidade'] = 'CMEI'
            if "Creche" in name:
                self.save[i]['unidade'] = 'Creche'
            if "CentrodeCapacitação" in name:
                self.save[i]['unidade'] = 'Centro de Capacitacao'
            

class EsporteELazer(Categoria):
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Esporte E Lazer
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("Praca" in name) or ("Praça" in name) or ("Ginásio" in name) or ("CEU" in name) or ("Parque" in name) or ("CampoSociety" in name) or ("CampoOficial" in name) or ("AcademiadaTerceiraIdade" in name) or ("AcademiaaoArLivre" in name) or ("Quadra" in name) or ("ComplexoEsportivo" in name) or ("Estádio" in name) or ("Skate" in name) or ("PistaOlímpica" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Esporte e Lazer"
    
    def classificarUnidade(self):
        '''
        Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Praça,
        Ginásio, CEU, Parque, Campo Society, Campo Oficial, Academia da Terceira Idade, Academia ao Ar Livre, 
        Quadra, Complexo Esportivo, Estádio, Pista de Skate, Pista Olímpica
        
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
            if "AcademiadaTerceiraIdade" in name:
                self.save[i]['unidade'] = 'Academia da Terceira Idade'
            if "AcademiaaoArLivre" in name:
                self.save[i]['unidade'] = 'Academia ao Ar Livre'
            if "Quadra" in name:
                self.save[i]['unidade'] = 'Quadra'
            if "ComplexoEsportivo" in name:
                self.save[i]['unidade'] = 'Complexo Esportivo'
            if "Estádio" in name:
                self.save[i]['unidade'] = 'Estadio'
            if "Skate" in name:
                self.save[i]['unidade'] = 'Pista de Skate'
            if "PistaOlímpica" in name:
                self.save[i]['unidade'] = 'Pista Olimpica'
            
            
            
class Predios_Publicos(Categoria):
    def classificarClasse(self, dicionario):
        '''
        Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Predios Publicos
        
        :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
        :retorno none: Não retorna nada ainda.
        '''
        for i in dicionario:
            name = dicionario[i]['name'].split()
            if ("SEMEC" in name) or ("SEMCOP" in name) or ("SEMAM" in name) or ("SEMA" in name) or ("PRODATER" in name) or ("SEMPLAN" in name)or ("PGM" in name) or ("IPMT" in name)or ("SEMDUH" in name)or ("SEMCASPI" in name)or ("SEMCOP" in name) or ("SEMDEC" in name)or ("SEMEST" in name) or ("SEMEL" in name) or ("SEMPOM" in name) or ("SEMJUV" in name) or ("STRANS" in name) or ("FMS" in name)or ("ARSETE" in name)or ("SDR" in name)or ("FMC" in name)or ("FWF" in name) or ("PrefeituradeTeresina" in name) or ("VicePrefeitura" in name) or ("SDU" in name) or("CAT" in name) or ("PredioAdministrativo" in name) or ("GerênciadeFarmâcia" in name) or ("CentrodeIniciação" in name):
                self.save[i] = dicionario[i]
                self.save[i]['classe'] = "Predios Publicos"
    
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
            if "PrefeituradeTeresina" in name:
                self.save[i]['unidade'] = 'Prefeitura de Teresina'
            if "VicePrefeitura" in name:
                self.save[i]['unidade'] = 'Vice Prefeitura'
            if "SDU" in name:
                self.save[i]['unidade'] = 'SDU'
            if "CAT" in name:
                self.save[i]['unidade'] = 'CAT'
            if "SEMEC" in name or "Semec" in name:
                self.save[i]['unidade'] = 'SEMEC'
            if "CMAM" in name:
                self.save[i]['unidade'] = 'CMAM'
            if "PredioAdministrativo" in name:
                self.save[i]['unidade'] = 'Predio Administrativo'
            if "GerênciadeFarmâcia" in name:
                self.save[i]['unidade'] = 'Gerencia de Farmacia'
            if "CentrodeIniciação" in name:
                self.save[i]['unidade'] = 'CIE'
                
class Meio_Ambiente(Categoria):
        def classificarClasse(self, dicionario):
            '''
            Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Meio Ambiente
            
            :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
            :retorno none: Não retorna nada ainda.
            '''
            for i in dicionario:
                name = dicionario[i]['name'].split()
                if ("PEV" in name) or ("PontodeRecebimentodeResíduo" in name) or ("EstaçãodeTransbordodeResíduosSólidos" in name) or ("HC" in name) or ("Viveiro" in name) or ("CampoAgricola" in name) or ("CampoAgrícola" in name):
                    self.save[i] = dicionario[i]
                    self.save[i]['classe'] = "Meio Ambiente"
        
        def classificarUnidade(self):
            '''
            Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias PEV (Pontos de Entrega Voluntaria),
            Pontode Recebimento de Resíduo, Estação de Transbordo de Resíduos Sólidos, Hortas Comunitárias
            
            :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                        JSON com as alterações feitas.
            :retorno save: Retorna o o dicionario save com as informações novas
            '''
            for i in self.save:
                name = self.save[i]['name'].split()
                if "PEV" in name :
                    self.save[i]['unidade'] = 'PEV'
                if "PontodeRecebimentodeResíduo" in name:
                    self.save[i]['unidade'] = 'Ponto de Recebimento de Resíduo'
                if "EstaçãodeTransbordodeResíduosSólidos" in name:
                    self.save[i]['unidade'] = 'Estação de Transbordo de Resíduos Sólidos'
                if "HC" in name:
                    self.save[i]['unidade'] = 'Hortas Comunitárias'
                if "Viveiro" in name:
                    self.save[i]['unidade'] = 'Viveiro de Mudas'
                if "CampoAgricola" in name or "CampoAgrícola" in name:
                    self.save[i]['unidade'] = 'Campo Agricola'
                

class Saneamento(Categoria):
        def classificarClasse(self, dicionario):
            '''
            Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Saneamento
            
            :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
            :retorno none: Não retorna nada ainda.
            '''
            for i in dicionario:
                name = dicionario[i]['name'].split()
                if ("Aterro" in name) or ("EstaçãoElevatória" in name):
                    self.save[i] = dicionario[i]
                    self.save[i]['classe'] = "Saneamento"
        
        def classificarUnidade(self):
            '''
            Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Aterro Sanitário, 
            Estação Elevatória, 
            
            :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                        JSON com as alterações feitas.
            :retorno save: Retorna o o dicionario save com as informações novas
            '''
            for i in self.save:
                name = self.save[i]['name'].split()
                if "Aterro" in name:
                    self.save[i]['unidade'] = 'Aterro Sanitário'
                if "EstaçãoElevatória" in name:
                    self.save[i]['unidade'] = 'Estação Elevatória'

class Cultura(Categoria):
        def classificarClasse(self, dicionario):
            '''
            Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Cultura
            
            :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
            :retorno none: Não retorna nada ainda.
            '''
            for i in dicionario:
                name = dicionario[i]['name'].split()
                if ("Museu" in name) or ("CasadaCultura" in name) or ("Teatro" in name) or ("Galeria" in name) or ("Palácio" in name):
                    self.save[i] = dicionario[i]
                    self.save[i]['classe'] = "Cultura"
        
        def classificarUnidade(self):
            '''
            Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Museu, Casa da Cultura,
            Teatro, Galeira, Palacio
            
            :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                        JSON com as alterações feitas.
            :retorno save: Retorna o o dicionario save com as informações novas
            '''
            for i in self.save:
                name = self.save[i]['name'].split()
                if "Museu" in name:
                    self.save[i]['unidade'] = 'Museu'
                if "CasadaCultura" in name:
                    self.save[i]['unidade'] = 'Casa da Cultura'
                if "Teatro" in name:
                    self.save[i]['unidade'] = 'Teatro'
                if "Galeria" in name:
                    self.save[i]['unidade'] = 'Galeria'
                if "Palácio" in name:
                    self.save[i]['unidade'] = 'Palacio'
                

class Outros(Categoria):
        def classificarClasse(self, dicionario):
            '''
            Responsável por classificar os objetos do arquivo JSON em classes. Neste caso na classe Outros
            
            :parametro dicionario: objeto dict() que contém os objetos do arquivo JSON.
            :retorno none: Não retorna nada ainda.
            '''
            for i in dicionario:
                name = dicionario[i]['name'].split()
                if ("Cemitério" in name) or ("Lavanderia" in name) or ("CentrodeProdução" in name) or ("Rotula" in name) or ("Rótula" in name) or ("PoloEmpresarial" in name) or ("Bicicletário" in name):
                    self.save[i] = dicionario[i]
                    self.save[i]['classe'] = "Outros"
        
        def classificarUnidade(self):
            '''
            Responsável por classificar os objetos do arquivo JSON em categorias. Neste caso nas categorias Cemitério, 
            Fazenda da Paz, 
            
            :parametro: Não tem parametro, ele utiliza uma variavel da classe (save) para salvar os objetos do arquivo 
                        JSON com as alterações feitas.
            :retorno save: Retorna o o dicionario save com as informações novas
            '''
            for i in self.save:
                name = self.save[i]['name'].split()
                if "Cemitério" in name:
                    self.save[i]['unidade'] = 'Cemitério'
                if "Lavanderia" in name:
                    self.save[i]['unidade'] = 'Lavanderia'
                if "CentrodeProdução" in name:
                    self.save[i]['unidade'] = 'Centro de Producao'
                if "Rótula" in name:
                    self.save[i]['unidade'] = 'Rotula'
                if "PoloEmpresarial" in name:
                    self.save[i]['unidade'] = 'Polo Empresarial'
                if "Bicicletário" in name:
                    self.save[i]['unidade'] = 'Bicicletário'



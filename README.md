# :card_file_box: Categorização de Lugares Públicos de Teresina

O objetivo desse projetinho era classificar os lugares públicos de Teresina de forma mais adequada. A forma como estava organizada no banco de dados estava muito bagunçada, então resolvemos organizar melhor para que o app que o utilizava tivesse um melhor desempenho.

Desse modo foram organizados em Classes e Categorias de Classes, onde as Classes são as listadas abaixo.

* [Assistência Social](#assistência-social)
* [Educação](#educação)
* [Saúde](#saúde)
* [Esporte e Lazer](#esporte-e-lazer)
* [Prédios Públicos](#prédios-públicos)
* [Meio Ambiente](#meio-ambiente)
* [Saneamento](#saneamento)
* [Cultura](#cultura)
* [Outros](#outros)

Cada uma dessas Classes possui Categorias que detêm de locais públicos que se encaixam nessas categorias. Por exemplo, se a Classe é *Saneamento*, ela detêm das categorias *Aterro Sanitario* e *Estacao Elevatoria*. Cada uma dessas categorias possui lugares que se encaixam nessa classificação, como *Estação Elevatória do São Joaquim - Lagoas do Norte*, que pertence a categoria Estacao Elevatoria.

## :gear: Pré requisitos

### Python

Nessa task foi utilizado Python 3.6. Você pode encontra-lo para download [aqui](https://www.python.org/downloads/)

## :hammer_and_wrench:	Como executar

Para executar o sript e obter o .json final com os lugares organizados da forma explicada, basta digitar no seu terminal dentro do respositorio:

### Windows
```
python main.py
```

### Ubuntu
```
python3 main.py
```

## :card_index_dividers: Classes e Categorias
### :balance_scale: Assistência Social

- CREAS
- CRAS
- Abrigo
- Centro POP
- Centro Dia
- Centro de Convivência
- Conselho Tutelar
- AMA
- LAC
- ASA
- APAE
- APADA
- Casa

### :books: Educação
 
- Escola
- Biblioteca
- CMEI
- Creche
- Centro de Capacitação

### :ambulance: Saúde

- Hospital
- UBS
- SAMU

### :bicyclist: Esporte e Lazer

- Praça
- Ginásio
- CEU
- Parque
- Campo Society
- Campo Oficial
- Academia da Terceira Idade
- Academia ao Ar Livre
- Quadra
- Complexo Esportivo
- Estádio
- Pista de Skate
- Pista Olímpica

### :classical_building: Prédios Públicos

- SEMEC
- SEMCOP
- SEMAM
- SEMA
- PRODATER
- SEMPLAN
- PGM
- IPMT
- SEMDUH
- SEMCASPI
- SEMCOP
- SEMDEC
- SEMEST
- SEMEL
- SEMPOM
- SEMJUV
- STRANS
- FMS
- ARSETE
- SDR
- FMC
- FWF
- PrefeituradeTeresina
- VicePrefeitura
- SDU
- CAT
- Predio Administrativo
- Gerência de Farmacia
- CIE

### :camping: Meio Ambiente

- PEV (Pontos de Entrega Voluntaria)
- Ponto de Recebimento de Resíduo
- Estação de Transbordo de Resíduos Sólidos
- HC (Hortas Comunitárias)

### :broom: Saneamento

- Aterro Sanitário
- Estação Elevatória

### :rainbow: Cultura

- Museu
- Casa da Cultura
- Teatro
- Galeria
- Palacio

### :office: Outros

- Cemitério
- Fazenda da Paz

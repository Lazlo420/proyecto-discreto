import pickle, os
import pandas as pd
import numpy as np
from Implicantes_esenciales import *
class base:
    def __init__(self,base,pais,comparison):
        self.nombre_pais=pais
        self.base=base
        self.estandarizado=self.binoomo(base,base)
        self.IPE=comparison
        self.filaspositivas=self.check(self.estandarizado)
        self.input=None
        self.input_results=None

    def binoomo(self,dfcom,dfref):
        binomo=np.zeros(shape=(len(dfcom),len(dfcom.columns)))
        for j in range(len(binomo[0])):
            avg=dfref[j].mean()
            for i in range(len(binomo)):
                numero=dfcom.iat[i,j]
                if numero>avg:
                    binomo[i][j]=1
        return binomo

    def check(self,base):
        matrx_xcom=base
        control,valoresconfirmados=[],[]
        for i in range(len(self.IPE)):
            c=list(self.IPE[i])
            control.append(c)
        for proposicion in range(len(matrx_xcom)):
            for implicante in range(len(control)):
                puntuacion=0
                for variable in range(len(matrx_xcom[proposicion])):
                    if str(control[implicante][variable])=='-':
                        puntuacion+=1
                    elif matrx_xcom[proposicion][variable]==int(control[implicante][variable]):puntuacion+=1
                    else:continue
                if puntuacion==13:
                    valoresconfirmados.append(proposicion)
                    break
        return valoresconfirmados

    def operacion_usuario(self,input):
        self.input=input
        estandarizao=self.binoomo(input,self.base)
        self.input_results=self.check(estandarizao)

    def __str__(self):
        return 'Soy '+self.nombre_pais

###Las bases
dat=os.path.dirname(os.path.realpath('maincode.py'))+'\df\lasbases'
ar=open(dat,'rb')
L=pickle.load(ar)
ar.close()

###IMPRESION para ver los contenidos en el dat
'''for i in range(len(L)):
    print(L[i])
    print(L[i].filaspositivas)'''

####MENU para presentacion final
print('  Escoge el pais a revisar  '.center(50,'#'),'\n\n','1. USA'.center(43,' '),'\n','2. Corea'.center(46,' '),'\n','3. Brasil'.center(48,' '),'\n','4. Japon\n'.center(48,' '))

while True:
    x=input('>>>Escoge tu opcion: ')
    print('\n','#'*50,'\n')
    if x.lower()=='q':
        break
    elif int(x)==1:
        try:
            dat=os.path.dirname(os.path.realpath('maincode.py'))+r'\###CSV ACA###\USA_input.csv'
            df = pd.read_csv(dat,header=None)
            L[int(x)-1].operacion_usuario(df)
            A=L[int(x)-1].input
            B=L[int(x)-1].input_results
            print('Input: \n',A,'\n\nResultados: \n',B)
            print('\n','#'*50,'\n')
            break
        except: print('ERROR en el CSV, (',dat,')\n')
    elif int(x)==2:
        try:
            dat=os.path.dirname(os.path.realpath('maincode.py'))+r'\###CSV ACA###\COREA_input.csv'
            df = pd.read_csv(dat,header=None)
            L[int(x)-1].operacion_usuario(df)
            A=L[int(x)-1].input
            B=L[int(x)-1].input_results
            print('Input: \n',A,'\n\nResultados: \n',B)
            print('\n','#'*50,'\n')
            break
        except: print('ERROR en el CSV, (',dat,')\n')
    elif int(x)==3:
        try:
            dat=os.path.dirname(os.path.realpath('maincode.py'))+r'\###CSV ACA###\BRASIL_input.csv'
            df = pd.read_csv(dat,header=None)
            L[int(x)-1].operacion_usuario(df)
            A=L[int(x)-1].input
            B=L[int(x)-1].input_results
            print('Input: \n',A,'\n\nResultados: \n',B)
            print('\n','#'*50,'\n')
            break
        except: print('ERROR en el CSV, (',dat,')\n')
    elif int(x)==4:
        try:
            dat=os.path.dirname(os.path.realpath('maincode.py'))+r'\###CSV ACA###\JAPON_input.csv'
            df = pd.read_csv(dat,header=None)
            L[int(x)-1].operacion_usuario(df)
            A=L[int(x)-1].input
            B=L[int(x)-1].input_results
            print('Input: \n',A,'\n\nResultados: \n',B)
            print('\n','#'*50,'\n')
            break
        except: print('ERROR en el CSV, (',dat,')\n')
    else:print('Selecciona una opcion del menu\n','\n','#'*50,'\n')

### Reiniciar atributos:
'''dat=os.path.dirname(os.path.realpath(__file__))+'\df\lasbases'
csvkorea=os.path.dirname(os.path.realpath(__file__))+'\df\korea.csv'
csvbrasil=os.path.dirname(os.path.realpath(__file__))+'\df\sbrasil.csv'
csvjapon=os.path.dirname(os.path.realpath(__file__))+'\df\japon.csv'
csvus=os.path.dirname(os.path.realpath(__file__))+'\df\estdosunidos.csv'

dfus = pd.read_csv(csvus,header=None)
dfkr = pd.read_csv(csvkorea,header=None)
dfbra = pd.read_csv(csvbrasil,header=None)
dfjap = pd.read_csv(csvjapon,header=None)

USA=base(dfus,"USA",USA)
KOREA=base(dfkr,'KOREA',Corea)
BRA=base(dfbra,'BRASIL',Brasil)
JAP=base(dfjap,'JAPAN',Japon)'''

### SUBIR CAMBIOS
'''L=[USA,KOREA,BRA,JAP]
ar=open(dat,'wb')
pickle.dump(L,ar)
ar.close()'''

### Crear csv comparacion resultados/benchmark
'''prueba=[]
for i in range(143):
    A=[0,0,0,0,0,0,0,0,0]
    prueba.append(A)

prueba[0][0]='Fecha'
prueba[0][1]='Us code'
prueba[0][2]='US bench'
prueba[0][3]='Japon code'
prueba[0][4]='Japon bench'
prueba[0][5]='Korea code'
prueba[0][6]='Korea Bench'
prueba[0][7]='Brasil code'
prueba[0][8]='Brasil bench'

bench=[]
noice=os.path.dirname(os.path.realpath(__file__))+'\df\sbench.csv'
benchread = open(noice,"r")
for linea in benchread:
    bench.append(linea.split(","))
benchread.close()

for i in range(1,len(prueba)):
    for j in range(len(prueba[0])):
        if j==1:
            if i in L[0].filaspositivas:
                prueba[i][j]=1
        elif j==2:
            prueba[i][j]=bench[i][5]
        elif j==3:
            if i in L[3].filaspositivas:
                prueba[i][j]=1
        elif j==4:
            prueba[i][j]=bench[i][6]
        elif j==5:
            if i in L[1].filaspositivas:
                prueba[i][j]=1
        elif j==6:
            prueba[i][j]=bench[i][7]
        elif j==7:
            if i in L[2].filaspositivas:
                prueba[i][j]=1
        elif j==8:
            prueba[i][j]=bench[i][8][0]
        elif j==0:
            prueba[i][j]=bench[i][0]

noice=os.path.dirname(os.path.realpath(__file__))+'\df\cresultados.csv'
ar=open(noice,"w")
for i in range(143):
    ar.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},\n'.format(prueba[i][0],prueba[i][1],prueba[i][2],prueba[i][3],prueba[i][4],prueba[i][5],prueba[i][6],prueba[i][7],prueba[i][8]))
ar.close()'''
import calculadoraCplx as cplx
import calculadoraMatr as matx
import numpy as np
import math

"""funcion para calcular la probabilidad de encontar un particula en una posicion"""
def probPosicion (pos, vcket):
    return(cplx.modcplx(vcket[pos][0])**2)/matx.normaVc(vcket)**2
"""faltana cosas"""

def proba (vc):
    return cplx.modcplx(vc)**2
def variEspera (mtrx,  ket):
    if matx.mtrxhermitiana(mtrx):
        bra = matx.adjuntaMtrx(matx.productoMtrx(mtrx,ket))[0]
        for i in range(len(bra)):
            bra[i]=[bra[i]]
        mu=matx.productoMtrx(matx.transMtrx(bra),key)[0][0]
        x = matx.escMultMtrx(mu,matx.mtrxIdentidad(len(mtrx)))
        y = matx.ad


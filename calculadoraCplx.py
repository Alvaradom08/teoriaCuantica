#libreria computacion cuantica
#Juan Mateo Alvarado Montoya
import math

import numpy as np
# Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(cplx, cplx2):
    real = cplx[0] + cplx2[0]
    img = cplx[1] + cplx2[1]
    return (real, img)
# Resta complejos representados como una tupla (real, imaginaria)
def restcplx(cplx, cplx2):
    real = cplx[0] - cplx2[0]
    imag = cplx[1] - cplx2[1]
    return (real,imag)
# Multiplica complejos representados como una tupla
def multcplx(cplx, cplx2):
    real = (cplx[0] * cplx2[0]) - (cplx[1] * cplx2[1])
    img = (cplx[0] * cplx2[1]) + (cplx2[0] * cplx[1])
    return (real, img)
# Division complejos representados como tupla
def divcplx(cplx, cplx2):
    den = cplx2[0] ** 2 + cplx2[1] ** 2
    num= cplx[0] * cplx2[0] + cplx[1] * cplx2[1]
    num2 = cplx[1] * cplx2[0] - cplx[0] * cplx2[1]
    div = num / den
    divr = round(div, 2)
    div2 = num2 / den
    divir2 = round(div2, 2)
    return (divr,divir2)
# Conversion de complejo a polar
def toPolar(c):
    theta = np.arctan2(c[1],c[0])
    rho = np.sqrt((c[0] * c[0]) + (c[1] * c[1]))
    return (rho, theta)
# Modulo complejo
def modcplx (cplx):
    rz = math.sqrt((cplx[0]**2 + cplx[1]*-1))
    rz = round(rz, 2)
    return (rz)
# Fase de complejo
def fasecplx(cplx):
    theta = math.atan2(cplx[1], cplx[0])
    theta = round(theta, 2)
    return (theta)
# conjugado complejo
def conjcplx(cplx):
    return (cplx[0],cplx[1]*-1)
def prettyprinting(c):
    #Para cartesianos
    print( str(c[0]) + "+" + str(c[1]) + "i")
def polprettyprinting(c):
    #Para polares
    print( str(c[0]) + " e^(i " + str(c[1]) + ")")
def main():
    prettyprinting(sumacplx((2, 3), (4, 7)))
    prettyprinting(multcplx((2, 3), (4, 7)))
    a = (14, 8)
    b = (1, 22)
    prettyprinting(restcplx(a, b))
    prettyprinting(divcplx(a, b))
    print(modcplx(a))
    print(conjcplx(b),"i")
    print(fasecplx(a),"i")
    # Prueba polares
    polprettyprinting(toPolar((-3, -2)))
main()
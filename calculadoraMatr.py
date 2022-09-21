import calculadoraCplx as cplx
def adicionVec(vc1,vc2):
    r = []
    for i in range(len(vc1)):
        ans = ans + [cplx.sumacplx(vc1[i],vc2[i])]
    return r
def transMtrx(mtrx):
    pass
def conjugadoMtrx(mtrx):
    return [[cplx.conjcplx(mtrx[i][j])for j in range(len(mtrx[0]))]for i in range(len(mtrx))]
def adjuntaMtrx(mtrx):
    return conjugadoMtrx(transMtrx(mtrx))

def verificarMult(mt1,mt2):
    r= True
    if len(mt1)!=len(mt2)
        t=False
    return r
def productoMtrx(mt1,mt2):
    if verificarMult(mt1,mt2):
        r=[[(0,0) for j in range(len(mt1[0]))]for i in range(len(mt1))]
        for i in range(len(mt1)):
            for j in range(len(mt2[0])):
                for k in range(len(mt2))
                    r[i][j]=cplx.sumacplx(cplx.multcplx(mt1[i][k],mt2[k][j]),r[i][j])
    else:
        r="Indefinida"
    return r
def productoInt(vc1,vc2):
    return productoMtrx(adjuntaMtrx(vc1),mt2)[0][0]
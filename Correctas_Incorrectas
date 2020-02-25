

letrasProposicionales = ['p', 'q', 'r', 's']

conectivosBinarios = ['O', 'Y', '>' , '<->']

negacion = ['-']

atomos  = []


class Tree(object):

    def __init__(self,l,iz,der):

        self.left = iz

        self.right = der

        self.label = l

        

r = Tree('r',None,None)

nr = Tree('-',None,r)

q = Tree('q',None,None)

nq = Tree('-',None,q)

s = Tree('s',None,None)

ns = Tree('-',None,s)

p = Tree('p',None,None)

np = Tree('-',None,p)       

    

def numAtomos(A):

        if A.right == None:

            if A.label not in atomos:

                atomos.append(A.label)

            return A.label

            

        elif A.label in negacion:

            return numAtomos(A.right)

        

        elif A.label in conectivosBinarios:

            return numAtomos(A.left) + numAtomos(A.right)



def V1(f,I):

    if f.right == None:

        return I[f.label]

    elif f.label in negacion:

        return 1-V1(f.right,I)

    elif f.label == 'Y':

        return V1(f.left,I)*V1(f.right,I)

    elif f.label == 'O':

        return max(V1(f.left,I),V1(f.right,I))

    elif f.label == '>':

        return max(1-V1(f.left,I),V1(f.right,I))

    elif f.label == '<->':

        return 1 - (V1(f.left,I)-V1(f.right,I))**2

    


tra = Tree( '>', p, Tree('>',np,nq))

trb = Tree('Y',np,q)

trc = Tree('y',Tree('Y',np,Tree('>',np,nq)),q)
        

def correctas(A):

    numAtomos(A)



    interps = []

    aux = {}

    soluciones = []

    for a in atomos:

        aux[a] = 1

    interps.append(aux)

    for a in atomos:

        interps_aux = [i for i in interps]  

        for i in interps_aux:

            aux1 = {}    

            for b in atomos:

                if a == b:

                    aux1[b] = 1 -i[b]

                else:

                    aux1[b] = i[b]

            interps.append(aux1)      

    for i in interps:

        

        if V1(A,i) == 0:

            soluciones.append(i)

            

    print("Interpretaciones que hacen a la fórmula verdadera:")

    if soluciones == []:

        print("Ninguna")

    else:

        for i in soluciones:

            print (i)

    

        

tr = Tree('-', None,Tree('Y',Tree('>',p,Tree('Y',q,nr)),Tree('Y',p,Tree('O',nq,r))))


correctas(tr)  

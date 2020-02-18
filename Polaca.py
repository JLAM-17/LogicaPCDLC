conectivosBinarios = ['O', 'Y', '>' , '<->']
negacion = ['-']

class Tree(object):
    def __init__(self,l,iz,der):
        self.left = iz
        self.right = der
        self.label = l
        
def polaca (A):
    if A.right == None:
        return A.label
    elif A.label in negacion:
        return "¬" + polaca(A.right)
    elif A.label in conectivosBinarios:
        return A.label + " " + polaca(A.left)+ " " + polaca(A.right)
    
def polaca_inversa (A):
    if A.right == None:
        return A.label
    elif A.label in negacion:
        return polaca(A.right) + "¬" 
    elif A.label in conectivosBinarios:
        return polaca(A.right) + " " + polaca(A.left) + " " + A.label


A0 = Tree('r',None,None)
A1 = Tree('p',None,None)
A2 = Tree('q',None,None)
A3 = Tree('>',A2,A1)
A4 = Tree('-',None,A0)
A5 = Tree('<->',A4,A2)
A6 = Tree('O',A1,A3)
A7 = Tree('-',None,A5)
A = Tree('>',A6,A7)

print(polaca(A))
print(polaca_inversa(A))a
        

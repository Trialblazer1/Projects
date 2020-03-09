import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

#def get_row(matrixA, row):
    #return matrixA[row]

#def get_column(matrixB, num):
    #col = []
    #for e in range(len(matrixB)) :
        #col.append(matrixB[e][num])
    #return col

#def dot_product(vectorA, vectorB) :
#    dp = 0
#    for f in range(len(vectorA)) :
#        dp += vectorA[f] + vectorB[f]
#    return dp

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """

        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        if self.h == 1 :
            mtx_det = self[0][0]
            return mtx_det

        elif self.h == 2:
            mtx_det = self[0][0] * self[1][1] - self[0][1] * self[1][0]
            return mtx_det
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """

        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        trc = 0

        for j in range(self.h) :
            trc += self[j][j]

        return Matrix(trc)

        #return sum([self.g[j][j] for j in range(self.h)])

     
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        #fact = self.determinant()
        #det = float(1/fact)

        mtx_inv = []

        if self.h == 1 :
            mtx_inv.append([1 / self[0][0]])

        elif self.h == 2 :
            if self.determinant() == 0 :
                raise ValueError('The matrix is not invertible.')

            else :
                a = self[0][0]
                b = self[0][1]
                c = self[1][0]
                d = self[1][1]

                x = 1 / ((a*d) - (b*c))
                inv = [[d, -b],[-c, a]]

                for i in range(len(inv)) :
                    coz = []
                    for j in range(len(inv[0])) :
                        coz.append(x * inv[i][j])
                    mtx_inv.append(coz)

                #I_mtx = identity(self.h)
                #tr = self.trace()
                #inv = det*((tr*I_mtx) - self)

        return Matrix(mtx_inv)

            #a = self.g[0][0]
            #b = self.g[0][1]
            #c = self.g[1][0]
            #d = self.g[1][1]

            #invv[0][0] = (1/det) * d
            #invv[0][1] = (1/det) * (-1 * b)
            #invv[1][0] = (1/det) * (-1 * c)
            #invv[1][1] = (1/det) * a

       
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        mtx_trans = []

        for k in range(self.w) :
            trans = []
            for l in range(self.h) :
                trans.append(self[l][k])
            mtx_trans.append(trans)

        return Matrix(mtx_trans)


    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")

        #h = self.h
        #w = self.w

        mtx_add = []

        for m in range(self.h) :
            ad =[]
            for n in range(self.w) :
                ad.append(self[m][n] + other[m][n])
            mtx_add.append(ad)

        return Matrix(mtx_add)
        #
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        mtx_neg = []

        for o in range(self.h) :
            ng = []
            for p in range(self.w) :
                new = -self[o][p]
                ng.append(new)
            mtx_neg.append(ng)

        return Matrix(mtx_neg)

        #
        # 
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #mtx_sub = []

        #for u in range(self.h):
            #su = []
            #for v in range(self.w):
                #su.append(self[u][v] - other[u][v])
            #mtx_sub.append(su)

        return (self + -other)

        #
        #
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        def dot_prod(vectorA, vectorB) :
            dp = 0
            for kat in range(len(vectorA)) :
                dp += vectorA[kat] * vectorB[kat]
            return dp

        mtx_mul = []

        other_trans = other.T()

        for q1 in range(self.h) :
            res = []
            for q2 in range(other_trans.h) :
                prod = dot_prod(self[q1], other_trans[q2])
                res.append(prod)
            mtx_mul.append(res)

        return Matrix(mtx_mul)

        #
        # 
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):

            mtx_is = []

            for s in range(self.h) :
                iss =[]
                for t in range(self.w) :
                    iss.append(other*self[s][t])
                mtx_is.append(iss)

            return Matrix(mtx_is)

            #pass
            #
            # 

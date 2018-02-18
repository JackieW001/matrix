import math

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print j, "\t ",
        print " "
        
def print_matrix_p( matrix ):
    m = []
    for col in range(len(matrix[0])):
        m.append([])
        for row in range(len(matrix)):
            m[col].append(truncate(matrix[row][col],2))
    print_matrix(m)
   

def ident( matrix ):
    size = len(matrix[0])
    print size
    t=new_matrix(size, size)
    for i in range(size):
       t[i][i] = 1
    return t

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    '''
    print "len m1: ", len(m1)
    print "len m1[0]: ", len(m1[0])
    print "len m2: ", len(m2)
    print "len m2[0]: ", len(m2[0])
    '''
    # rows should be len of m1, colums should be len m2
    m = new_matrix(len(m1),len(m2[0]))

                    
    for row1 in range(len(m1)): # rows of m1
        for col2 in range(len(m2[0])): # columns of m2
            for row2 in range(len(m2)): # rows of m2
                #print str(row1), ", ", str(col2), ", ", str(row2)
                a = m1[row1][row2]
                #print "a: ", str(a)
                
                b = m2[row2][col2]
                #print "b: ", str(b)
                
                m[row1][col2] += a*b
                #print_matrix(m)

    return m



def new_matrix(rows = 4, cols = 4):

    m = []
    for c in range( rows ):
        m.append( [] )
        for r in range( cols ):
            m[c].append( 0 )
    return m


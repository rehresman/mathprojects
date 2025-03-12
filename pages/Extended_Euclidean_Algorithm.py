import streamlit as st
import numpy as np
import random

# TODO: Handle case where A and B aren't coprime


def get_gcd_matrix(A, B):
    """
    Generates a 4-column GCD matrix.

    Args:
        A (int): The first number.
        B (int): The second number.

    Returns:
        list[list[int]]: a matrix with 4 columns.

    Examples:
        we're generating a 4 column matrix, with as many rows as necessary
        X   = X_1 * Y   + R_1
        Y   = X_2 * R_1 + R_2
        R_1 = X_3 * R_2 + R_3
        R_2 = X_4 * R_3 + R_4
        ...
        R_n = X_(n+2) * R_(n+1) + 1    
        this gives the n x 4 matrix:   
        [[ X      X_1     Y       R_1
           Y      X_2     R_1     R_2
           R_1    X_3     R_2     R_3
           R_2    X_4     R_3     R_4 
           ...
           R_n    X_(n+2) R_(n+1) 1   ]]       
        The process terminates when the fourth column is 0 
        
        Example 2.  Find the GCD of 3 and 5.
         5 = 1(3) + 2
         3 = 1(2) + 1
         2 = 2(1) + 0  
        so the output of this function will be a matrix of the form
          5   1   3   2
          3   1   2   1
          2   2   1   0
"""
    if abs(A) > abs(B):
        X = A
        Y = B
    else:
        X = B 
        Y = A 
    if (X == 0 or Y == 0):
        m = []
    else:
        gcd = 1

        # working variables for seeding the matrix 
        c = X
        d = int((X - np.fmod(X,Y)) // Y)
        e = Y
        f = np.fmod(X,Y)
        
        m = [[c, d, e, f]]
        n = 0
        if (f == 0):
            gcd = e
        else:
            # build matrix
            while not (f == 0):
                c = m[n][0]
                d = m[n][1]
                e = m[n][2]
                f = m[n][3]
                if f != 0:
                    m.append([e, (e - np.fmod(e,f))//f, f, np.fmod(e,f)])
                else:
                    gcd = abs(e)
                n += 1
    return m

def get_linear_combination_coefficients(m):
    """
        Generates a linear combination list.

        Args:
            m (list[list[int]]): A GCD matrix
        
        Returns:
            list[int]: An array representing linear combinations of the gcd.
        
        Examples:
            given the matrix m
            5   1   3   2
            3   1   2   1
            2   2   1   0
            which corresponds to the following equaitons
            1 = (1)*3 - 1(2)
            1 = (-1)*5 - (-2)*3

            this function will return a 5 x 1 list
            1   -1  5  -2   3
            corresponding to the equation
            1 = (-1)*5 - (-2)*3
        
        
    """
    n = len(m)
    # one of the initial coefficients is 0
    if n == 0:
        return None
    # initial coefficients are linearly dependent
    if n == 1:
        return [m[0][2], m[0][2], 1, 0, m[0][0]]
    else:
        gcd = abs(m[n-1][2])
        if (n > 1):
            c = m[n-2][0]
            d = m[n-2][1]
            e = m[n-2][2]
            f = m[n-2][3]

            # build arrays of coefficients of equivalent linear combinations of the gcd
            g, h = [None] * (n-1), [None] * (n-1)

            g[n-2] = 1
            h[n-2] = m[n-2][1]
            
            # this formula is the result of some substitutions
            for i in range(n-2, 0, -1):
                g[i-1] = -h[i]
                h[i-1] = -(m[i-1][1]*h[i] + g[i])
            
            # flip the signs if necessary
            if (m[n-2][3] < 0):
                for i in range(n-1):
                    g[i] = -g[i]
                    h[i] = -h[i]
        
        # flip the sign of h[0] so our linear combination is of the form 
        # gcd = AX + BY
        # instead of
        # gcd = AX - BY
        # as given by the algorithm
        return [gcd, m[0][0], g[0], m[0][2], -h[0]]

def get_mimimal_linear_combination(A,B):
    """
        Generates a minimal linear combination such that AX + BY = gcd(A,B)

        Args:
            A (int): The first number.
            B (int): The second number.

        Returns:
            list[int]: An array representing linear combinations of the gcd.
        
        Example:
            Given A = 3 and B = 5
            we get
            1   5   -1   3   2
            corresponding to the equation
            1 = 5 * -1 + 3 * 2
    """
    combo = get_linear_combination_coefficients(get_gcd_matrix(A,B))
    #fix the order of coefficients to match intuition
    if combo:
        if combo[1] == A:
            return combo
        else:
            return [combo[0], combo[3], combo[4], combo[1], combo[2]]
    else:
        return None

def get_linear_combination(A,B,C):
    """
        Generates a linear combination such that AX + BY = C

        Args:
            A (int): The first coefficient.
            B (int): The second coefficient.
            C (int): The required linear combination of A and B.

        Returns:
            list[int]: An array representing a C = AX + BY.
        
        Example:
            Given A = 3, B = 5, C = 4
            we get
            4   5  -4   3   8
            corresponding to the equation
            4 = 5 * -4 + 3 * 8

    """
    m = get_mimimal_linear_combination(A,B)
    if m:
        # case: A and B are coprime
        m[0] = m[0] * C
        m[2] = m[2] * C
        m[4] = m[4] * C
        # case: A = NB or B = NA for some integer N
        # I will handle this case later
    return m

# fluffy version of the algorithm with verbose output
def verbose_euclidean_alg(A, B):
    m = get_gcd_matrix(A,B)
    n = len(m)

    if m != [] and m[0][3] == 0:
        st.write(m[0][0], ' = ', m[0][1], '(',m[0][2],') + ',m[0][3])
    else:
        for i in range(0,n):
            st.write(m[i][0], ' = ', m[i][1], '(',m[i][2],') + ',m[i][3])

    
    if n == 0: 
        st.write("The gcd of a number and zero does not exist")
    else:
        gcd = abs(m[n-1][2])

        # display the gcd
        st.write("gcd(", A, ",", B, ") = ",gcd)
        st.subheader("Linear Combinations")

        # vacuous case
        if (n == 1):
            st.write("Linear combinations of these two are just multiples of ", gcd, '.' )
            print(m)
        if (n > 1):
            c = m[n-2][0]
            d = m[n-2][1]
            e = m[n-2][2]
            f = m[n-2][3]

            st.write("The second-to-last equation we found is ", 
                        m[n-2][0], ' = ', 
                        m[n-2][1], '(',
                        m[n-2][2],') + ',
                        m[n-2][3], ', so it follows that')
            st.write( m[n-2][3], " = ", m[n-2][0], " - (",m[n-2][1], ')', m[n-2][2])

            # build arrays of coefficients of equivalent linear combinations of the gcd
            g, h = [None] * (n-1), [None] * (n-1)

            g[n-2] = 1
            h[n-2] = m[n-2][1]
            
            # this formula is the result of some substitutions
            for i in range(n-2, 0, -1):
                g[i-1] = -h[i]
                h[i-1] = -(m[i-1][1]*h[i] + g[i])
                st.write( m[n-2][3], " = (", g[i-1], ")", m[i-1][0], " - (", h[i-1], ")", m[i-1][2])
            
            # flip the signs if necessary
            if (m[n-2][3] < 0):
                for i in range(n-1):
                    g[i] = -g[i]
                    h[i] = -h[i]
            print(g,h)
            # sanity check
            rand_int = random.randint(-1000000000,1000000000)
            rand_gcd_multiple = rand_int * gcd
            st.write("Since we could express ", m[n-2][3], " as a linear combination of ", A, " and ", B, ", we can express any multiple of",
                    m[n-2][3], " in the following form by multiplying the coefficients by whatever integer we want to express. For example:")
            if (m[n-2][3] > 0):
                st.write(rand_gcd_multiple, " = (", g[0]*rand_int, ")", m[0][0], " - (", h[0]*rand_int, ")", m[0][2])
            else:
                st.write(rand_gcd_multiple, " = (", -g[0]*rand_int, ")", m[0][0], " - (", -h[0]*rand_int, ")", m[0][2])
            st.write("(calculator spot check: ", g[0]*rand_int * m[0][0] - rand_int*h[0]*m[0][2] == rand_gcd_multiple, ")")

# setup
st.title('Extended Euclidean Algorithm')
st.write("This finds the GCD (greatest common denominator) of two integers X and Y.",
           "This is special because at the same time it computes a method of expressing integers as a",
            " linear combination of X and Y")
col1, col2 = st.columns(2)

A = col1.number_input("X",step=1)
B = col2.number_input("Y",step=1)

st.write(get_mimimal_linear_combination(A,B))

verbose_euclidean_alg(A, B)



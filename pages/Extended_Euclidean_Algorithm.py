import streamlit as st
import numpy as np
import random

st.title('Extended Euclidean Algorithm')
st.write("This finds the GCD (greatest common denominator) of two integers X and Y.",
           "But this is special because at the same time it computes a method of expressing integers as a",
            " linear combination of X and Y")
col1, col2 = st.columns(2)

A = col1.number_input("X",step=1)
B = col2.number_input("Y",step=1)

st.write("# Naive algorithm")
# we're generating a 4 column matrix, with as many rows as necessary
# X   = X_1 * Y   + R_1
# Y   = X_2 * R_1 + R_2
# R_1 = X_3 * R_2 + R_3
# R_2 = X_4 * R_3 + R_4
# ...
# R_n = X_(n+2) * R_(n+1) + 1
#
# this gives the 4 by n matrix:
#
# [[ X      X_1     Y       R_1
#    Y      X_2     R_1     R_2
#    R_1    X_3     R_2     R_3
#    R_2    X_4     R_3     R_4 
#    ...
#    R_n    X_(n+2) R_(n+1) 1   ]]
#
#
# The process terminates when the fourth column is 0
#
#
# We can use the values in the resulting matrix to reverse substitute our way
# into representing integers as linear combinations of X and Y.
#

if abs(A) > abs(B):
    X = A
    Y = B
else:
    X = B 
    Y = A 
if (X == 0 or Y == 0):
    st.write("The gcd of a number and zero does not exist")
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
        st.write(c, ' = ', d, '(',e,') + ',f)
    else:
        # build matrix
        while not (f == 0):
            c = m[n][0]
            d = m[n][1]
            e = m[n][2]
            f = m[n][3]
            st.write(c, ' = ', d, '(',e,') + ',f)
            if f != 0:
                m.append([e, (e - np.fmod(e,f))//f, f, np.fmod(e,f)])
            else:
                gcd = abs(e)
            n += 1

    # display answer
    st.write("gcd(", A, ",", B, ") = ",gcd)
    st.subheader("Linear Combinations")

    if (n <= 1):
        st.write("Linear combinations of these two are just multiples of ", gcd, '.' )
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
        st.write( m[n-2][3], " = ", m[n-2][0], " - ",m[n-2][1], "(", m[n-2][2], ')')

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


        # sanity check
        rand_int = random.randint(-1000000000,1000000000)
        rand_gcd_multiple = rand_int * gcd
        st.write("Since we could express ", m[n-2][3], " as a linear combination of ", X, " and ", Y, ", we can express any multiple of",
                 m[n-2][3], " in the following form by multiplying the coefficients by whatever integer we want to express. For example:")
        if (m[n-2][3] > 0):
            st.write(rand_gcd_multiple, " = (", g[0]*rand_int, ")", m[0][0], " - (", h[0]*rand_int, ")", m[0][2])
        else:
            st.write(rand_gcd_multiple, " = (", -g[0]*rand_int, ")", m[0][0], " - (", -h[0]*rand_int, ")", m[0][2])
        st.write("(calculator spot check: ", g[0]*rand_int * m[0][0] - rand_int*h[0]*m[0][2] == rand_gcd_multiple, ")")
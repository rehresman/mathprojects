# ExtendedEuclideanAlgorithm

 we're generating a 4 column matrix, with as many rows as necessary
 X   = X_1 * Y   + R_1
 Y   = X_2 * R_1 + R_2
 R_1 = X_3 * R_2 + R_3
 R_2 = X_4 * R_3 + R_4
 ...
 R_n = X_(n+2) * R_(n+1) + 1

 this gives the 4 by n matrix:

 [[ X      X_1     Y       R_1
    Y      X_2     R_1     R_2
    R_1    X_3     R_2     R_3
    R_2    X_4     R_3     R_4 
    ...
    R_n    X_(n+2) R_(n+1) 1   ]]


 The process terminates when the fourth column is 0


 We can use the values in the resulting matrix to reverse substitute our way
 into representing integers as linear combinations of X and Y.


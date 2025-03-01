import streamlit as st
import numpy as np

st.title('Linear Diophantine Equation Solver')
st.markdown(
    """
    **Linear Diophantine Equations** have two or more unknown values, and are of the form
    """
            )
st.latex("AX + BY = C.")
st.markdown(
    """
    ## Real-Life Example
    I'm training a machine learning model using two types of GPUs:

    ¯\\\_(ツ)\_/¯ Basic GPUs process 3 training batches per hour.

    ¯\\\_(ツ)\_/¯ Advanced GPUs process 5 training batches per hour.

    The goal is to train 100 batches in a single hour.  How many of each should I use?


    ### Solution
    Let X be the number of basic GPUs and Y be the number of advanced GPUs.  Then the equation we need to solve is
    """
            )
st.latex("3X + 5Y = 100.")




st.markdown(
    """
    .
    """
            )


st.markdown(
    """
    An equation like this is easy to solve in a field like **R** or **Q**, because every value of X has a 
    corresponding value of Y.  But in the ring of integers, it's not so simple.  Often in real life
    we need integer solutions to such equations (example below), and since I was recently teaching AI models how to 
    solve this kind of equation, I figured I'd write a program to automate parts of the task.  
    """
            )



"""
    Code taken from https://github.com/tirthajyoti/Machine-Learning-with-Python/blob/master/Random%20Function%20Generator/Symbolic_regression_classification_generator.py
"""
def gen_classification_symbolic(m=None,n_samples=100,n_features=2,flip_y=0.0):
    """
    Generates classification sample based on a symbolic expression.
    Calculates the output of the symbolic expression at randomly generated (Gaussian distribution) points and
    assigns binary classification based on sign.
    m: The symbolic expression. Needs x1, x2, etc as variables and regular python arithmatic symbols to be used.
    n_samples: Number of samples to be generated
    n_features: Number of variables. This is automatically inferred from the symbolic expression. So this is ignored
                in case a symbolic expression is supplied. However if no symbolic expression is supplied then a
                default simple polynomial can be invoked to generate classification samples with n_features.
    flip_y: Probability of flipping the classification labels randomly. A higher value introduces more noise and make
            the classification problem harder.
    Returns a numpy ndarray with dimension (n_samples,n_features+1). Last column is the response vector.
    """

    import numpy as np
    from sympy import Symbol,sympify
    
    if m==None:
        m=''
        for i in range(1,n_features+1):
            c='x'+str(i)
            c+=np.random.choice(['+','-'],p=[0.5,0.5])
            m+=c
        m=m[:-1]
    sym_m=sympify(m)
    n_features=len(sym_m.atoms(Symbol))
    evals=[]
    lst_features=[]
    for i in range(n_features):
        lst_features.append(np.random.normal(scale=5,size=n_samples))
    lst_features=np.array(lst_features)
    lst_features=lst_features.T
    for i in range(n_samples):
        evals.append(eval_multinomial(m,vals=list(lst_features[i])))

    evals=np.array(evals)
    evals_binary=evals>0
    evals_binary=evals_binary.flatten()
    evals_binary=np.array(evals_binary,dtype=int)
    evals_binary=flip(evals_binary,p=flip_y)
    evals_binary=evals_binary.reshape(n_samples,1)

    lst_features=lst_features.reshape(n_samples,n_features)
    x=np.hstack((lst_features,evals_binary))

    return (x)

import numpy as np

def sigmoid(v):
    return 1 / (1 + np.exp(-v)), v

def tanh(v):
    return 2 * sigmoid(2 *v) - 1, v

def hardtanh(v):
    v[v < -1] = -1
    v[v > 1] = 1
    return v, v

def softsign(v):
    return v / (1 + np.abs(v)), v

def d_hardtanh(v):
    v[v >= -1] = 1
    v[v <= 1] = 1
    v[v < -1] = 0
    v[v > 1] = 0
    return v, v

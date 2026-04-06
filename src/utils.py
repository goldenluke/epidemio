import numpy as np

def utility(I_real, I_hat, actions):
    I_hat = I_hat[:len(I_real)]

    erro = np.mean((I_real - I_hat)**2)
    variancia = np.var(I_hat)
    custo = np.mean(actions)

    erro_norm = erro / (np.max(I_real)**2 + 1e-6)
    var_norm = variancia / (np.max(I_hat)**2 + 1e-6)

    return -(erro_norm + 0.5*var_norm + 0.2*custo)

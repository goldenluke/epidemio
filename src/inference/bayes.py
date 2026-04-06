import pymc as pm
import numpy as np

def infer_R(I_hat, T):

    with pm.Model() as model:

        I_real = pm.GaussianRandomWalk("I_real", sigma=0.1, shape=len(I_hat))

        pi_T = 1 - np.exp(-0.05*T)
        mu = pi_T * I_real

        pm.Normal("obs", mu=mu, sigma=1.0, observed=I_hat)

        trace = pm.sample(500, tune=500)

    return trace

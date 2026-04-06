import numpy as np

def pi(T):
    return 1 - np.exp(-0.05 * T)

def run_simulation(T, steps=200, N=100000, noise=0.0):
    beta0 = 0.3
    gamma = 0.1
    alpha = 0.002
    delta = 0.1
    tau = 5
    theta = 0.01

    S = [N - 10]
    I = [10]
    R = [0]

    I_hat = [0]*tau
    actions = []

    for t in range(steps):

        # ruído na observação (incerteza)
        noisy_I = I[-1] * (1 + np.random.normal(0, noise))

        I_obs = pi(T) * noisy_I
        I_hat.append(max(I_obs, 0))

        if I_hat[-tau] / N > theta:
            a = 1
        else:
            a = 0

        actions.append(a)

        beta = beta0 - alpha*T - delta*a

        dS = -beta * S[-1] * I[-1] / N
        dI = beta * S[-1] * I[-1] / N - gamma * I[-1]
        dR = gamma * I[-1]

        S.append(S[-1] + dS)
        I.append(max(I[-1] + dI, 0))
        R.append(R[-1] + dR)

    return np.array(I), np.array(I_hat), np.array(actions)

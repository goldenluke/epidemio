import numpy as np
import matplotlib.pyplot as plt
from simulation import run_simulation
from utils import utility

Ts = np.linspace(0, 100, 30)
utils = []

for T in Ts:
    I, I_hat, actions = run_simulation(T)
    U = utility(I, I_hat, actions)
    utils.append(U)

plt.plot(Ts, utils)
plt.xlabel("T")
plt.ylabel("U(T)")
plt.title("Singularidade de Vigilância")
plt.show()

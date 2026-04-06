import numpy as np

def robust_action(R_samples, threshold=0.01):

    decisions = []

    for R in R_samples:
        if np.mean(R) > threshold:
            decisions.append(1)
        else:
            decisions.append(0)

    # decisão robusta = pior caso
    return max(decisions)

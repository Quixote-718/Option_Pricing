import numpy as np


class BrownianMotion:
    """
    Simulates one-dimensional Brownian Motion.
    """

    def __init__(self, T=1.0, steps=252, seed=None):
        self.T = T
        self.steps = steps
        self.seed = seed

    def simulate(self):
        if self.seed is not None:
            np.random.seed(self.seed)

        dt = self.T / self.steps

        Z = np.random.normal(0, 1, self.steps)

        dW = np.sqrt(dt) * Z

        W = np.concatenate(([0], np.cumsum(dW)))

        t = np.linspace(0, self.T, self.steps + 1)

        return t, W

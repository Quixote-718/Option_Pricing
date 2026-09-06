from src.brownian_motion import BrownianMotion
import numpy as np


class GeometricBrownianMotion:
    """
    Simulates stock prices using Geometric Brownian Motion.
    """

    def __init__(
        self,
        S0,
        r,
        sigma,
        T,
        steps=252,
        simulations=10000,
        seed=None,
    ):
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.steps = steps
        self.simulations = simulations
        self.seed = seed

    def terminal_prices(self):
        """
        Returns terminal stock prices.
        """

        if self.seed is not None:
            np.random.seed(self.seed)

        Z = np.random.normal(size=self.simulations)

        ST = self.S0 * np.exp(
            (self.r - 0.5 * self.sigma**2) * self.T
            + self.sigma * np.sqrt(self.T) * Z
        )

        return ST

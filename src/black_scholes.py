import numpy as np
from scipy.stats import norm


class BlackScholesPricer:
    """
    Black-Scholes analytical pricing model
    for European options.
    """

    def __init__(self, S0, K, T, r, sigma):

        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def d1(self):

        return (
            np.log(self.S0 / self.K)
            + (self.r + 0.5 * self.sigma**2) * self.T
        ) / (self.sigma * np.sqrt(self.T))

    def d2(self):

        return self.d1() - self.sigma * np.sqrt(self.T)

    def call_price(self):

        d1 = self.d1()
        d2 = self.d2()

        return (
            self.S0 * norm.cdf(d1)
            - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        )

    def put_price(self):

        d1 = self.d1()
        d2 = self.d2()

        return (
            self.K * np.exp(-self.r * self.T) * norm.cdf(-d2)
            - self.S0 * norm.cdf(-d1)
        )

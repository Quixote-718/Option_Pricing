import numpy as np


class EuropeanOption:
    """
    European Call and Put Payoffs.
    """

    def __init__(self, strike):
        self.K = strike

    def call_payoff(self, ST):
        return np.maximum(ST - self.K, 0)

    def put_payoff(self, ST):
        return np.maximum(self.K - ST, 0)

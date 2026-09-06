import numpy as np

from src.gbm import GeometricBrownianMotion
from src.options import EuropeanOption


class MonteCarloPricer:
    """
    Monte Carlo engine for European option pricing.
    """

    def __init__(
        self,
        S0,
        K,
        T,
        r,
        sigma,
        simulations=100000,
        seed=None,
    ):

        self.model = GeometricBrownianMotion(
            S0,
            r,
            sigma,
            T,
            simulations=simulations,
            seed=seed,
        )

        self.option = EuropeanOption(K)

        self.r = r
        self.T = T
        self.simulations = simulations

    def call_price(self):

        ST = self.model.terminal_prices()

        payoff = self.option.call_payoff(ST)

        discounted = np.exp(-self.r * self.T) * payoff

        price = np.mean(discounted)

        stderr = np.std(discounted, ddof=1) / np.sqrt(self.simulations)

        lower = price - 1.96 * stderr
        upper = price + 1.96 * stderr

        return price, lower, upper

    def put_price(self):

        ST = self.model.terminal_prices()

        payoff = self.option.put_payoff(ST)

        discounted = np.exp(-self.r * self.T) * payoff

        return np.mean(discounted)

import matplotlib.pyplot as plt

from src.monte_carlo import MonteCarloPricer
from src.black_scholes import BlackScholesPricer


def convergence_experiment():

    S0 = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.20

    simulation_sizes = [
        100,
        500,
        1000,
        5000,
        10000,
        50000,
        100000,
    ]

    bs = BlackScholesPricer(
        S0=S0,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
    )

    bs_price = bs.call_price()

    mc_prices = []

    for n in simulation_sizes:

        mc = MonteCarloPricer(
            S0=S0,
            K=K,
            T=T,
            r=r,
            sigma=sigma,
            simulations=n,
            seed=42,
        )

        price, _, _ = mc.call_price()

        mc_prices.append(price)

    return simulation_sizes, mc_prices, bs_price


# Plots

def plot_convergence():

    simulations, mc_prices, bs_price = convergence_experiment()

    plt.figure(figsize=(10, 6))

    plt.plot(
        simulations,
        mc_prices,
        marker="o",
        linewidth=2,
        label="Monte Carlo"
    )

    plt.axhline(
        bs_price,
        color="red",
        linestyle="--",
        linewidth=2,
        label="Black-Scholes"
    )

    plt.xscale("log")

    plt.xlabel("Number of Simulations")

    plt.ylabel("Call Option Price")

    plt.title("Monte Carlo Convergence")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig("plots/convergence.png", dpi=300)

    plt.show()


# Error Plot

def plot_error():

    simulations, mc_prices, bs_price = convergence_experiment()

    errors = []

    for price in mc_prices:

        errors.append(abs(price - bs_price))

    plt.figure(figsize=(10, 6))

    plt.plot(
        simulations,
        errors,
        marker="o",
        linewidth=2,
    )

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Number of Simulations")

    plt.ylabel("Absolute Error")

    plt.title("Monte Carlo Error")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("plots/error.png", dpi=300)

    plt.show()


if __name__ == "__main__":

    plot_convergence()

    plot_error()

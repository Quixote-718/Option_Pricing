from src.monte_carlo import MonteCarloPricer
from src.black_scholes import BlackScholesPricer


def main():

    S0 = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.20

    mc = MonteCarloPricer(
        S0=S0,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
        simulations=100000,
        seed=42,
    )

    bs = BlackScholesPricer(
        S0=S0,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
    )

    mc_call, lower, upper = mc.call_price()
    mc_put = mc.put_price()

    bs_call = bs.call_price()
    bs_put = bs.put_price()

    print("=" * 60)
    print("OPTION PRICING COMPARISON")
    print("=" * 60)

    print(f"Monte Carlo Call : {mc_call:.4f}")
    print(f"Black-Scholes Call : {bs_call:.4f}")

    print()

    print(f"Monte Carlo Put : {mc_put:.4f}")
    print(f"Black-Scholes Put : {bs_put:.4f}")

    print()

    print(f"95% CI : [{lower:.4f}, {upper:.4f}]")

    print("=" * 60)


if __name__ == "__main__":
    main()

from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def styleAxis(ax):
    # 1. Set xscale to log
    ax.set_xscale("log")
    # 2. Set the exact tick positions
    ax.set_xticks([300, 1000, 10000])
    # 3. Set the exact text labels for those ticks
    ax.set_xticklabels(['300', '1k', '10k'])
    # 4. Keep the X-axis starting limit at 300
    ax.set_xlim(left=300)


def main():
    gdpDf = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    leDf = load("life_expectancy_years.csv")
    if gdpDf is None or leDf is None:
        exit(1)
    fig, ax = plt.subplots()
    subGdpDf = gdpDf[["country", "1900"]].rename(columns={"1900": "gdppc"})
    subLeDf = leDf[["country", "1900"]].rename(columns={"1900": "lifeexp"})
    combinedDf = pd.merge(subGdpDf, subLeDf, on="country").dropna()
    combinedDf.plot(
        ax=ax,
        kind="scatter",
        x="gdppc",
        y="lifeexp",
        xlabel="Gross domestic product",
        ylabel="Life expectancy",
        title="1900"
    )
    styleAxis(ax)
    plt.show()
    return 0


if __name__ == "__main__":
    main()

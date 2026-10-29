from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


def convertToNumeric(val):
    if isinstance(val, (int, float)):
        return val

    tens = dict(k=10e3, m=10e6, b=10e9)
    factor, exp = val[0:-1], val[-1].lower()
    return int(float(factor) * tens[exp])


def formatNumeric(val, pos=None) -> str:
    if val >= 1e9:
        return f"{val * 1e-9:.1f}B"
    elif val >= 1e6:
        return f"{val * 1e-6:.1f}M"
    elif val >= 1e3:
        return f"{val * 1e-3:.1f}k"
    return f"{val:.1f}"


def combineDf(csvDf):
    countryIndexedDf = csvDf.set_index("country")
    finlandDf = countryIndexedDf.loc["Finland"].apply(convertToNumeric)
    vietnamDf = countryIndexedDf.loc["Vietnam"].apply(convertToNumeric)
    combinedDf = pd.DataFrame({
        "Finland": finlandDf,
        "Vietnam": vietnamDf
    })
    return combinedDf


def styleAxis(ax):
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(formatNumeric))
    ax.legend(loc="lower right")


def main():
    csvDf = load("population_total.csv")
    if csvDf is None:
        exit(1)
    fig, ax = plt.subplots()
    combinedDf = combineDf(csvDf)
    combinedDf.plot(
        ax=ax,
        kind='line',
        xlabel="Year",
        ylabel="Population",
        title="Population Projections"
    )
    styleAxis(ax)
    plt.show()
    return 0


if __name__ == "__main__":
    main()

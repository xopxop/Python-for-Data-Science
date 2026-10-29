from load_csv import load
import matplotlib.pyplot as plt


def main():
    rawDf = load("life_expectancy_years.csv")
    if rawDf is None:
        exit(1)
    countryIndexedDf = rawDf.set_index('country')
    finlandDf = countryIndexedDf.loc["Finland"]
    finlandDf.plot(
        kind='line',
        title="Finland Life expectancy Projections",
        xlabel="Year",
        ylabel="Life expectancy"
    )
    plt.show()
    return 0


if __name__ == "__main__":
    main()

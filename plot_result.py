import matplotlib.pyplot as plt
import pandas as pd


def plot_q_freq(time_series=pd.DataFrame()):

    # create figure
    fig, axes = plt.subplots(figsize=(11, 6))

    time_series.plot.scatter(y="pr",
                             x="Q (CMS)",
                             title="Probability ",
                             ax=axes,
                             color='purple',
                             grid=True,
                             fontsize=14,
                             logy=True,
                             label="Sorted values")
    axes.legend(frameon=True, framealpha=1)

    axes.set_ylabel("Probability (-)")
    axes.set_xlabel("Discharge (CMS)")
    axes.set_title("Probability of flow events")
    plt.show()


def plot_q_return_period(time_series=pd.DataFrame()):

    # create figure
    fig, axes = plt.subplots(figsize=(11, 6))

    time_series.plot.scatter(y="Q (CMS)",
                             x="return-period",
                             title="Return period (years) ",
                             ax=axes,
                             color='purple',
                             grid=True,
                             fontsize=14,
                             logy=True,
                             label="Sorted values")
    axes.legend(frameon=True, framealpha=1)

    axes.set_ylabel("Discharge (CMS)")
    axes.set_xlabel("Return period (years)")
    axes.set_title("Return periods of flow events ")
    plt.show()

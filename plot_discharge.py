import matplotlib.pyplot as plt
import pandas as pd


def plot_discharge(time_series=pd.Series(), q_series=pd.Series(), title="",
                   size=1, color="blue"):

    # create figure
    fig, axes = plt.subplots(figsize=(11, 6))

    # make blue-marker scatter plot (circles with size 4)
    axes.scatter(x=time_series, y=q_series,
                 marker="o", s=size, color=color)

    # set axis labels
    axes.set(xlabel="Date", ylabel="Discharge (CMS)", title=title)

    # show grid and set plot limits
    plt.xlim(time_series.min(), time_series.max())
    plt.grid()

    # show plot
    plt.show()

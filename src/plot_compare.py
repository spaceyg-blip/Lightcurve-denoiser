import matplotlib.pyplot as plt

def compare_plot(
    time,
    flux,
    smooth_flux
):

    plt.figure(
        figsize=(12,5)
    )

    plt.plot(
        time,
        flux,
        alpha=0.5,
        label="Original"
    )

    plt.plot(
        time,
        smooth_flux,
        label="Smoothed"
    )

    plt.xlabel(
        "Time"
    )

    plt.ylabel(
        "Flux"
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        "lightcurve_compare.png",
        dpi=300
    )

    plt.show()

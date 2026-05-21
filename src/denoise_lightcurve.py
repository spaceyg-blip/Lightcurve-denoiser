from scipy.signal import savgol_filter

def denoise(flux):

    smooth_flux = savgol_filter(
        flux,
        31,
        3
    )

    return smooth_flux

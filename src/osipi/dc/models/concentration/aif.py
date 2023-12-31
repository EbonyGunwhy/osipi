import numpy as np


def parker(t:np.ndarray, prebolus:float=0.5, hct:float=0.0, dose:float=0.1)->np.ndarray:
    """AIF model as defined by Parker et al (2005)

    Args:
        t (np.ndarray): array of time points in units of min
        prebolus (float, optional): Time in mins before the bolus arrives. Defaults to 0.5 min.
        hct (float, optional): Hematocrit. Defaults to 0.0.
        dose (float, optional): Injected contrast agent dose in units of [???]. Defaults to 0.1.

    Returns:
        np.ndarray: Concentrations in mM for each time point in t.

    See Also:
        :func:`~georgiou`
        :func:`~weinmann`

    Facts:
        Lexicon url: https://osipi.github.io/OSIPI_CAPLEX/perfusionModels/#arterial-input-function-models
        Lexicon code: M.IC2.001
        OSIPI name: Parker AIF model
        Adapted from ontribution by: MB_QBI_UoManchester_UK

    Example:

        Create an array of time points covering 6min in steps of 1sec, calculate the Parker AIF at these time points and plot the results.

        Import packages:

        >>> import matplotlib.pyplot as plt
        >>> import osipi.dc.models.concentration.aif as aif

        Calculate AIF and plot

        >>> t = np.arange(0, 6, 1/60)
        >>> ca = aif.parker(t)
        >>> plt.plot(t,ca)
    """

    t_offset = t - prebolus

    #A1/(SD1*sqrt(2*PI)) * exp(-(t_offset-m1)^2/(2*var1))
    #A1 = 0.833, SD1 = 0.055, m1 = 0.171
    gaussian1 = 5.73258 * np.exp(
        -1.0 *
        (t_offset - 0.17046) * (t_offset - 0.17046) /
        (2.0 * 0.0563 * 0.0563) )
    
    #A2/(SD2*sqrt(2*PI)) * exp(-(t_offset-m2)^2/(2*var2))
    #A2 = 0.336, SD2 = 0.134, m2 = 0.364
    gaussian2 = 0.997356 * np.exp(
        -1.0 *
        (t_offset - 0.365) * (t_offset - 0.365) /
        (2.0 * 0.132 * 0.132))
    # alpha*exp(-beta*t_offset) / (1+exp(-s(t_offset-tau)))
    # alpha = 1.064, beta = 0.166, s = 37.772, tau = 0.482
    sigmoid = 1.050 * np.exp(-0.1685 * t_offset) / (1.0 + np.exp(-38.078 * (t_offset - 0.483)))
    pop_aif = ((dose / 0.1) * (gaussian1 + gaussian2 + sigmoid)) / \
        (1.0 - hct)
    
    return pop_aif


def georgiou(t):
    pass

def weinmann(t):
    pass



# if __name__ == "__main__":

#     import matplotlib.pyplot as plt

#     t = np.arange(0, 6, 1/60)
#     ca = parker(t)
#     plt.plot(t, ca)
#     plt.show()



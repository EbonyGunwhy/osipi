
Generating an AIF
^^^^^^^^^^^^^^^^^

Generate an AIF and plot it:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    import osipi.dc.models.concentration.aif as aif

    t = np.arange(0, 6, 1/60)
    ca = parker(t)
    plt.plot(t, ca)
    plt.show()


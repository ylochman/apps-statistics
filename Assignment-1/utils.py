import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import seaborn as sns
from math import floor

def represent_distribution(sample, xmin=None, xmax=None, nx=None):
    mpl.rcParams['figure.figsize'] = (10, 3)
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True,
                                        gridspec_kw={"height_ratios": (.25, .75)})
    sns.boxplot(sample, fliersize=0, whis=1.5, ax=ax_box)
    sns.stripplot(sample, color="orange", jitter=0.2, size=3, ax=ax_box)
    ax_box.set(xlabel='')

    sns.distplot(sample, ax=ax_hist, bins='sqrt')
    if nx is not None:
        ax_hist.xaxis.set_major_locator(plt.MaxNLocator(nx))
    if xmin is not None:
        ax_hist.set_xlim(left=xmin)
    if xmax is not None:
        ax_hist.set_xlim(right=xmax)

    print('(number of observations: {})'.format(len(sample)))
    plt.show()
    
def p_quantile(x, p):
    """
    0 <= p <= 1
    """
    x = sorted(x)
    n = len(x)
    
    m = n * p
    if m % 1 == 0:
        m = int(m)
        return (x[m-1] + x[m]) / 2
    else:
        return x[int(floor(m))]
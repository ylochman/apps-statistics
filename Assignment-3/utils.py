import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import seaborn as sns
from math import floor

def represent_distribution(sample, xmin=None, nx=None, varname=''):
    mpl.rcParams['figure.figsize'] = (10, 3)

    k = 2
    f, (ax_box, ax_hist) = plt.subplots(k, sharex=True,
                                        gridspec_kw={"height_ratios": (.3, .60)})

    sns.boxplot(sample, fliersize=0, whis=1.5, ax=ax_box)
    sns.stripplot(sample, color="orange", jitter=0.2, size=3, ax=ax_box)
    ax_box.set(xlabel='')

    sns.distplot(sample, ax=ax_hist, bins=80)
    if nx is not None:
        ax_hist.xaxis.set_major_locator(plt.MaxNLocator(nx))
    if xmin is not None:
        ax_hist.set_xlim(left=xmin)
    if varname!='':
        print('Variable `{}`'.format(varname))
    print('Number of observations: {}'.format(len(sample)))
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
    
def get_X_y(df, regressand, regressors, out=True):
    if out:
        print('Explained:', regressand)
        print('Explanatory:', regressors)
    y = df[regressand]
    X = df[regressors]
    return X, y

def get_normalized_X_y(X, y, intervals_regressors):
    X_intervals_means = X[intervals_regressors].mean()
    X_intervals_stds = X[intervals_regressors].std(ddof=1)

    X_norm = X.copy()
    X_norm[intervals_regressors] = (X[intervals_regressors] - X_intervals_means) / X_intervals_stds

    y_mean = y.mean()
    y_std = y.std(ddof=1)
    y_norm = (y - y_mean) / y_std
    
    return X_norm, y_norm, X_intervals_means, X_intervals_stds, y_mean, y_std
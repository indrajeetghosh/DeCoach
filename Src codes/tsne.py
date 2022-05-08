import pandas as pd
from sklearn.manifold import TSNE
import matplotlib as mpl
import pylab
import matplotlib.pyplot as plt
import time
import seaborn as sns
from matplotlib import rc, rcParams

def tsne_plot(x_subset,y_subset):
    # prep dada frame
    tsne_df = pd.DataFrame(x_subset)
    tsne_df.columns = ["ft-"+str(i) for i in range(0,tsne_df.shape[1])]
    tsne_df['Label']=y_subset

    # Compute t-SNE
    time_start = time.time()
    tsne = TSNE(n_components=2, verbose=1, perplexity=200, n_iter=350)
    tsne_results = tsne.fit_transform(tsne_df[[cols for cols in tsne_df.columns if 'ft' in cols]].values)
    print('t-SNE done! Time elapsed: {} seconds'.format(time.time()-time_start))

    #Store results
    tsne_df['tsne-three'] = tsne_results[:,0]
    tsne_df['tsne-four'] = tsne_results[:,1]

    # Create plot

    sns.lmplot(x='tsne-three',
               y='tsne-four',
               data=tsne_df,
               fit_reg=False,
               legend=False,
               height=8,
               hue='Label',
               scatter_kws={"s":40, "alpha":0.5})
    
    plt.rcParams["axes.labelweight"] = "semibold"
    rc('font', weight='bold')
    plt.legend(fontsize = '30', loc='best', bbox_to_anchor=(0.9, 0.1, 0.5, 0.93))
    plt.title('LEFT LEG', fontweight='semibold', fontsize = '30')
    plt.xlabel('t-SNE-1' ,fontweight='semibold', fontsize = '30')
    plt.ylabel('t-SNE-2', fontweight='semibold', fontsize = '30')
    plt.xticks(fontsize=35)
    plt.yticks(fontsize=35)
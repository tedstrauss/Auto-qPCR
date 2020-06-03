import pandas as pd
import AUTOqPCR
import matplotlib.pyplot as plt
import numpy as np


def plots(dataframe, model, targets, samples):
    plots=[]
    # font size, bar width
    fs = 30
    barwidth = 0.75
    # Absolute: bar plot for each gene, a grouped bar plot by samples and a grouped bar plot by genes
    if model == 'absolute':
        plot_by_samples = plt.figure(figsize=(40, 25))
        counter = 0
        for item in targets:
            plot = plt.figure(figsize=(20, 25))
            sample = list(dataframe.loc[item, 'NormQuant']['mean'])
            x = np.arange(len(sample))
            x2 = x * len(targets) + barwidth*counter
            # set color, width, edgecolor, etc.
            plt.bar(x, sample, yerr=list(dataframe.loc[item, 'NormSEM']['mean']), align='center',
                   error_kw=dict(lw=0.9, capsize=2, capthick=0.9), width=barwidth, label=item)
            plt.xlabel(item, fontweight='bold', fontsize=fs, labelpad=20)
            plt.xticks([i for i in range(len(samples))], samples, rotation='vertical', fontsize=fs)
            plt.legend(fontsize=22)
            plt.tight_layout()
            plt.close(plot)
            plots.append(plot)
            # grouped plot
            plt.bar(x2, sample , yerr=list(dataframe.loc[item , 'NormSEM']['mean']) , align='center' ,
                    error_kw=dict(lw=0.9, capsize=2, capthick=0.9) , width=barwidth , edgecolor = 'white', label=item)
            counter += 1
        plt.xticks([i*len(targets) + barwidth*counter/2 for i in range(len(samples))], samples , rotation='vertical', fontsize=fs)
        plt.xlabel('Samples', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.tight_layout()
        plt.close(plot_by_samples)
        plots.append(plot_by_samples)

        plot_by_genes = plt.figure(figsize=(40, 25))
        counter = 0
        for item in samples:
            target = list(dataframe.loc[(slice(None) , item) , 'NormQuant']['mean'])
            x = np.arange(len(target)) * len(samples) + barwidth * counter
            plt.bar(x , target , yerr=list(dataframe.loc[(slice(None) , item) , 'NormSEM']['mean']) , align='center' ,
                    error_kw=dict(lw=0.9 , capsize=2, capthick=0.9) , width=barwidth , edgecolor='white' , label=item)
            counter += 1

        plt.xticks([i * len(samples) + barwidth * counter / 2 for i in range(len(targets))] , targets ,
                   rotation='vertical' , fontsize=fs)
        plt.xlabel('Targets', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=22)
        plt.close()
        plots.append(plot_by_genes)

    # Genomic stability: grouped by chromosomes and by cell lines
    elif model == 'stability2':
        # plot grouped by chromosomes
        plot_by_samples = plt.figure(figsize=(40, 25))
        counter = 0
        for item in targets:
            sample = list(dataframe.loc[item , 'rq']['mean'])
            x = np.arange(len(sample)) * len(targets) + barwidth * counter
            plt.bar(x , sample , yerr=list(dataframe.loc[item , 'rqSEM']['mean']) , align='center' ,
                    error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , width=barwidth , edgecolor='white' , label=item)
            counter += 1

        plt.xticks([i * len(targets) + barwidth * counter / 2 for i in range(len(samples))] , samples ,
                   rotation='vertical', fontsize=fs)
        plt.xlabel('DNA Regions', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.tight_layout()
        plt.close()
        plots.append(plot_by_samples)
        # plot grouped by chromosomes
        plot_by_chrs = plt.figure(figsize=(40, 25))
        counter = 0
        for item in samples:
            target = list(dataframe.loc[(slice(None) , item) , 'rq']['mean'])
            x = np.arange(len(target)) * len(samples) + barwidth * counter
            plt.bar(x , target , yerr=list(dataframe.loc[(slice(None) , item) , 'rqSEM']['mean']) , align='center' ,
                    error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , width=barwidth , edgecolor='white' , label=item)
            counter += 1

        plt.xticks([i * len(samples) + barwidth * counter / 2 for i in range(len(targets))], targets,
                   rotation='horizontal', fontsize=fs)
        plt.xlabel('Targets', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=22)
        plt.close()
        plots.append(plot_by_chrs)

    # relative deltaCT and delta delta CT: plots for each gene and grouped plots by samples and genes
    else:
        plot_by_samples = plt.figure(figsize=(40, 25))
        counter = 0
        for item in targets:
            plot = plt.figure(figsize=(20, 25))
            sample = list(dataframe.loc[item, 'rq']['mean'])
            x = np.arange(len(sample))
            x2 = x * len(targets) + barwidth * counter
            plt.bar(x , sample , yerr=list(dataframe.loc[item , 'rqSEM']['mean']) , align='center' ,
                    error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , width=barwidth , edgecolor='white' , label=item)
            plt.xlabel(item , fontweight='bold', labelpad=20)
            plt.xticks([i for i in range(len(samples))] , samples , rotation='vertical' , fontsize=fs)
            plt.legend(fontsize=fs)
            plt.tight_layout()
            plt.close(plot)
            plots.append(plot)
            # grouped plot by samples
            plt.bar(x2, sample, yerr=list(dataframe.loc[item , 'rqSEM']['mean']) , align='center' ,
                    error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , width=barwidth , edgecolor='white', label=item)
            counter += 1
        plt.xticks([i * len(targets) + barwidth * counter / 2 for i in range(len(samples))], samples,
                   rotation='vertical', fontsize=fs)
        plt.xlabel('Samples', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.tight_layout()
        plt.close()
        plots.append(plot_by_samples)
        # grouped by genes
        plot_by_genes = plt.figure(figsize=(40, 25))
        counter = 0
        for item in samples:
            target = list(dataframe.loc[(slice(None) , item) , 'rq']['mean'])
            x = np.arange(len(target)) * len(samples) + barwidth * counter
            plt.bar(x , target , yerr=list(dataframe.loc[(slice(None) , item) , 'rqSEM']['mean']) , align='center' ,
                    error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , width=barwidth , edgecolor='white' , label=item)
            counter += 1

        plt.xticks([i * len(samples) + barwidth * counter / 2 for i in range(len(targets))], targets,
                   rotation='vertical', fontsize=fs)
        plt.xlabel('Targets', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_genes)

    return plots


# grouped plots with endogeneous control removed by samples and genes for absolute and relative models
def plots_wo_controls(dataframe, model, targets, samples, cgenes):
    targets = [t for t in targets if t.lower() not in cgenes.lower().split(',')]
    dataframe = dataframe.loc[targets, slice(None), :]

    # font size, bar width
    fs = 30
    barwidth = 0.75
    plots = []

    # Absolute: a grouped bar plot by genes and a grouped bar plot by cell lines
    if model == 'absolute':
        plot_by_samples = plt.figure(figsize=(40, 30))
        counter = 0
        for item in targets:
            sample = list(dataframe.loc[item, 'NormQuant']['mean'])
            x = np.arange(len(sample)) * len(targets) + barwidth * counter
            # grouped plot
            plt.bar(x, sample, yerr=list(dataframe.loc[item, 'NormSEM']['mean']) , align='center' ,
                        error_kw=dict(lw=0.9, capsize=2, capthick=0.9), width=barwidth , edgecolor='white',
                        label=item)
            counter += 1

        plt.xticks([i * len(targets) + barwidth * counter / 2 for i in range(len(samples))] , samples ,
                       rotation='vertical' , fontsize=fs)
        plt.xlabel('Samples', fontsize=fs , fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.tight_layout()
        plt.close()
        plots.append(plot_by_samples)

        plot_by_genes = plt.figure(figsize=(40, 25))
        counter = 0
        for item in samples:
            target = list(dataframe.loc[(slice(None), item), 'NormQuant']['mean'])
            x = np.arange(len(target)) * len(samples) + barwidth * counter
            plt.bar(x, target, yerr=list(dataframe.loc[(slice(None) , item) , 'NormSEM']['mean']), align='center',
                        error_kw=dict(lw=0.9, capsize=2, capthick=0.9) , width=barwidth , edgecolor='white' ,
                        label=item)
            counter += 1

        plt.xticks([i * len(samples) + barwidth * counter / 2 for i in range(len(targets))] , targets ,
                       rotation='vertical' , fontsize=fs)
        plt.xlabel('Targets', fontsize=fs , fontweight='bold', labelpad=20)
        plt.legend(fontsize='20')
        plt.close()
        plots.append(plot_by_genes)

    elif model != 'stability2':
        plot_by_samples = plt.figure(figsize=(40, 30))
        counter = 0
        for item in targets:
            sample = list(dataframe.loc[item , 'rq']['mean'])
            x = np.arange(len(sample)) * len(targets) + barwidth * counter
            # grouped plot by samples
            plt.bar(x , sample , yerr=list(dataframe.loc[item , 'rqSEM']['mean']) , align='center' ,
                        error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , width=barwidth , edgecolor='white' ,
                        label=item)
            counter += 1
        plt.xticks([i * len(targets) + barwidth * counter / 2 for i in range(len(samples))] , samples ,
                       rotation='vertical', fontsize=fs)
        plt.xlabel('Samples', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.tight_layout()
        plt.close()
        plots.append(plot_by_samples)

        # grouped by genes
        plot_by_genes = plt.figure(figsize=(40, 25))
        counter = 0
        for item in samples:
            target = list(dataframe.loc[(slice(None) , item) , 'rq']['mean'])
            x = np.arange(len(target)) * len(samples) + barwidth * counter
            plt.bar(x , target , yerr=list(dataframe.loc[(slice(None) , item) , 'rqSEM']['mean']) , align='center' ,
                        error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , width=barwidth , edgecolor='white' ,
                        label=item)
            counter += 1

        plt.xticks([i * len(samples) + barwidth * counter / 2 for i in range(len(targets))], targets,
                       rotation='vertical' , fontsize=fs)
        plt.xlabel('Targets', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_genes)

    return plots


# plot by user defined groups in stats
def plot_by_groups(df, model, targets, cgenes):
    # font size, bar width
    fs = 30
    barwidth = 0.75
    # list of groups
    groups = df['Group'].drop_duplicates(keep='first').values.tolist()

    plots = []
    if model == 'absolute':
        # remove endogeneous control genes
        targets = [t for t in targets if t.lower() not in cgenes.lower().split(',')]
        # grouped by groups on the x-axis
        counter = 0
        plot_by_group = plt.figure(figsize=(20, 25))
        for t in targets:
            y = []
            st_err = []
            x = np.arange(len(groups))*len(targets)+barwidth*counter
            for g in groups:
                sample = df.loc[(df['Target Name'] == t) & (df['Group'] == g)]
                y.append(sample['NormMean'].mean())
                st_err.append(sample['NormMean'].sem())
            plt.bar(x, y, yerr=st_err, error_kw=dict(lw=0.9, capsize=2, capthick=0.9), align='center', width=barwidth, edgecolor='white', label=t)

            counter += 1
        plt.xticks([i * len(targets) + barwidth * counter / 2 for i in range(len(groups))], groups, rotation='vertical', fontsize=fs)
        plt.xlabel('Groups', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_group)
        # grouped by targets on the x-axis
        counter = 0
        plot_by_target = plt.figure(figsize=(20, 25))
        for g in groups:
            y = []
            st_err = []
            x = np.arange(len(targets))*len(groups)+barwidth*counter
            for t in targets:
                sample = df.loc[(df['Target Name'] == t) & (df['Group'] == g)]
                y.append(sample['NormMean'].mean())
                st_err.append(sample['NormMean'].sem())
            plt.bar(x, y, yerr=st_err, error_kw=dict(lw=0.9, capsize=2, capthick=0.9), align='center', width=barwidth, edgecolor='white', label=g)

            counter += 1
        plt.xticks([i * len(groups) + barwidth * counter / 2 for i in range(len(targets))], targets,
                   rotation='vertical', fontsize=fs)
        plt.xlabel('Targets', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_target)
    elif model == 'stability2':
        # grouped by groups on the x-axis
        counter = 0
        plot_by_group = plt.figure(figsize=(20, 25))
        for t in targets:
            y = []
            st_err = []
            x = np.arange(len(groups))*len(targets)+barwidth*counter
            for g in groups:
                sample = df.loc[(df['Target Name'] == t) & (df['Group'] == g)]
                y.append(sample['rqMean'].mean())
                st_err.append(sample['rqMean'].sem())
            plt.bar(x , y , yerr=st_err , error_kw=dict(lw=0.9, capsize=2, capthick=0.9), align='center', width=barwidth, edgecolor='white', label=t)

            counter += 1
        plt.xticks([i * len(targets) + barwidth * counter / 2 for i in range(len(groups))], groups,
                   rotation='vertical' , fontsize=fs)
        plt.xlabel('Groups', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_group)
        # grouped by groups on the x-axis
        counter = 0
        plot_by_target = plt.figure(figsize=(20, 25))
        for g in groups:
            y = []
            st_err = []
            x = np.arange(len(targets)) * len(groups) + barwidth * counter
            for t in targets:
                sample = df.loc[(df['Target Name'] == t) & (df['Group'] == g)]
                y.append(sample['rqMean'].mean())
                st_err.append(sample['rqMean'].sem())
            plt.bar(x , y , yerr=st_err , error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , align='center' ,
                    width=barwidth , edgecolor='white' , label=g)

            counter += 1
        plt.xticks([i * len(groups) + barwidth * counter / 2 for i in range(len(targets))], targets, rotation='vertical', fontsize=fs)
        plt.xlabel('Targets', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_target)
    else:
        # remove endogeneous control genes
        targets = [t for t in targets if t.lower() not in cgenes.lower().split(',')]
        # grouped by groups on the x-axis
        counter = 0
        plot_by_group = plt.figure(figsize=(20, 25))
        for t in targets:
            y = []
            st_err = []
            x = np.arange(len(groups)) * len(targets) + barwidth * counter
            for g in groups:
                sample = df.loc[(df['Target Name'] == t) & (df['Group'] == g)]
                y.append(sample['rqMean'].mean())
                st_err.append(sample['rqMean'].sem())
            plt.bar(x , y , yerr=st_err , error_kw=dict(lw=0.9 , capsize=2 , capthick=0.9) , align='center',
                    width=barwidth , edgecolor='white' , label=t)

            counter += 1
        plt.xticks([i * len(targets) + barwidth * counter / 2 for i in range(len(groups))], groups,
                   rotation='vertical' , fontsize=fs)
        plt.xlabel('Groups', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_group)
        # grouped by groups on the x-axis
        counter = 0
        plot_by_target = plt.figure(figsize=(20, 25))
        for g in groups:
            y = []
            st_err = []
            x = np.arange(len(targets)) * len(groups) + barwidth * counter
            for t in targets:
                sample = df.loc[(df['Target Name'] == t) & (df['Group'] == g)]
                y.append(sample['rqMean'].mean())
                st_err.append(sample['rqMean'].sem())
            plt.bar(x, y, yerr=st_err, error_kw=dict(lw=0.9, capsize=2 , capthick=0.9), align='center',
                    width=barwidth, edgecolor='white', label=g)

            counter += 1
        plt.xticks([i * len(groups) + barwidth * counter / 2 for i in range(len(targets))], targets,
                   rotation='vertical', fontsize=fs)
        plt.xlabel('Targets', fontsize=fs, fontweight='bold', labelpad=20)
        plt.legend(fontsize=fs)
        plt.close()
        plots.append(plot_by_target)

    return plots

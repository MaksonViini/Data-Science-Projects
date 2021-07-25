import seaborn as sns
import matplotlib.pyplot as plt


class Functions:
    def Shape(df):
        print('Number of rows: ', df.shape[0])
        print('Number of columns: ', df.shape[1])

    def barplot(df, X, Y, title, xlabel, ylabel, Palette=None):
        plt.figure(figsize=(12, 8))
        sns.barplot(x=X, y=Y, data=df, palette=Palette)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def pointplot(df, X, Y, title, xlabel, ylabel, Palette=None):
        plt.figure(figsize=(12, 8))
        sns.pointplot(x=X, y=Y, data=df, palette=Palette)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def set_custom_palette(series, max_color='gray', other_color='lightgrey'):
        series.sort()
        max_val = series.max()
        pal = []

        for item in series:
            if item == max_val:
                pal.append(max_color)
            else:
                pal.append(other_color)
        return pal

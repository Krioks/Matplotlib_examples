import matplotlib.pyplot as plt


class PrepareSimpleGraph:

    def __init__(self, path_to_save='', width=16, height=9):
        self.path_to_save = path_to_save
        self.width = width
        self.height = height

    def __enter__(self):
        self.fig, self.ax = plt.subplots(figsize=(self.width, self.height))
        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.yaxis.set_ticks_position('left')
        self.ax.spines['left'].set_position(('data', 0))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.path_to_save:
            self.fig.savefig(self.path_to_save)
        plt.show()


class PreparePolarGraph:

    def __init__(self, path_to_save='', width=16, height=9):
        self.path_to_save = path_to_save
        self.width = width
        self.height = height

    def __enter__(self):
        self.fig, self.ax = plt.subplots(figsize=(self.width, self.height), subplot_kw=dict(polar=True))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.path_to_save:
            self.fig.savefig(self.path_to_save)
        plt.show()

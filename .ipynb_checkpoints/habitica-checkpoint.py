import pandas as pd

class habitica:
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        print(self.data.head())

f = 'data/habitica-tasks-history.csv'
d = habitica(f)

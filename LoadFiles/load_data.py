import pandas as pd

class LoadData:

    def __init__(self,filepath):
        self.filepath = filepath
    
    def load_data(self):
        return pd.read_csv(self.filepath)
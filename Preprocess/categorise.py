import pandas as pd
from sklearn.preprocessing import OneHotEncoder

class Categorise:

    def __init__(self,data,columns):
        self.data = data
        self.columns = columns
    
    def categorise_data_numeric(self):
        for column in self.columns:
            self.data[column] = pd.Categorical(self.data[column])
            self.data[column] = self.data[column].codes
        return self.data
            
    def categorise_data_one_hot(self):
        enc = OneHotEncoder(handle_unknown='ignore')
        for column in self.columns:
            enc.fit(self.data[column])
            self.data[column] = pd.Series(enc.transform(self.data[column]).toarray())
        
        return self.data
    


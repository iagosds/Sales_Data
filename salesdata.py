import pandas as pd
import matplotlib.pyplot as plt

class SalesData:

    def __init__(self, csv):
        self.__csv = csv
        self.__data = None

    def load_data(self):
        self.__data = pd.read_csv(self.__csv)

    @property
    def total_vendas(self):
        return self.__data.Sales.sum()

    @property
    def media_vendas(self):
        return self.__data.Sales.mean()

    def max_min(self):
        return f'max:{self.__data.Sales.max()} min:{self.__data.Sales.min()}'

    def plot_sales(self):
        plt.bar(self.__data.Date, self.__data.Sales)
        plt.xticks(rotation=45)
        return plt.show

data = SalesData('sales_data.csv')
data.load_data()
data.total_vendas
data.media_vendas
data.max_min()
data.plot_sales() #Vizualização a partir de um notebook
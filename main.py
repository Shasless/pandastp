from utils import *

amazon = Analyse("stocks_data/AMAZON.csv", 'csv')
apple = Analyse("stocks_data/APPLE.csv", 'csv')
amazon.Analyse_data()
amazon.CorrWithAnotherData(apple)
amazon.show_graph()


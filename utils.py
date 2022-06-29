import pandas as pd
import plotly.graph_objects as go


class Analyse:
    def __init__(self, chemin, type):
        self.df2 = None
        self.df = None
        self.path = chemin
        self.type = type
        self.createDataframe()
        self.reorganizeDataFrame()

    def show_graph(self):
        fig = go.Figure(data=[go.Candlestick(x=self.df.index,
                                             open=self.df['Open'],
                                             high=self.df['High'],
                                             low=self.df['Low'],
                                             close=self.df['Close'])])

        fig.show()
    def createDataframe(self):
        if self.type == "csv":
            self.df = pd.read_csv(self.path)
        elif self.type == "excel":
            self.df = pd.read_excel(self.path)
        elif self.type == "json":
            self.df = pd.read_json(self.path)

    def printHead(self, nbr=40):
        print(nbr, "first observations")
        print(self.df.head(nbr))

    def printTail(self, nbr=40):
        print(nbr, "last observations")
        print(self.df.tail(nbr))

    def printInfo(self):
        print(self.df.info())

    def printDescription(self):
        print("Info High")
        print(min(self.df.High))
        print(max(self.df.High))
        print("Info Low")
        print(min(self.df.Low))
        print(max(self.df.Low))
        self.printStd()

    def printTimeGap(self):
        a = self.df.index[len(self.df) - 1] - self.df.index[0]
        a = a.days / len(self.df)
        print("The mean time Between two observation is", round(a, 2), "day(s)")
        print("We estimate that the observatrion are",closest_value(a))

        return a



    def calculReturnRate(self, period):
        self.df2 = self.df.copy()
        self.df2 = self.df2.assign(Return_Rate=(self.df2.Close - self.df2.Open) / self.df2.Open * 100)
        self.df2 = self.df2.Return_Rate.resample(period).mean()
        print("the return in a period of", period, "is", self.df2.mean())


    def printSize(self):
        print("The size of the dataframe is", len(self.df))

    def printCorrelation(self):
        print("correlation between", self.path)
        print(self.df.corr())

    def printStd(self):
        print("Standard deviation")
        print(self.df.std(numeric_only=True))

    def printMaxCol(self, colname):
        print("Max", colname, "is", self.df[colname].max())

    def printMinCol(self, colname):
        print("Min", colname, "is", self.df[colname].min())


    def movvingAverage(self, colname, nbr):
        name_colum = 'moving_average_' + colname
        self.df[name_colum] = self.df[colname].rolling(nbr).mean()

    def movingAverageHommemade(self, colname, nbr):
        sum = 0
        new_col = []
        nbr += 1
        for i in range(0, len(self.df)):
            if (i < nbr):
                new_col.append(0)

            else:
                for y in range(i - nbr, i):
                    sum += self.df.iloc[y][colname]
                new_col.append(sum / nbr)
                sum = 0

        name_colum = 'moving_average_' + colname
        self.df[name_colum] = new_col

    def daily_return(self, colname):
        name_colum = 'daily_return_' + colname
        self.df[name_colum] = self.df[colname].pct_change()

    def reorganizeDataFrame(self):
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
        self.df.set_index('Date', inplace=True)



    def Analyse_data(self):
        self.printHead(20)
        self.printTail(20)
        self.printInfo()
        self.printDescription()
        self.printTimeGap()
        self.printSize()
        self.printCorrelation()
        self.printMaxCol('High')
        self.printMinCol('Low')
        self.movvingAverage('High', 10)
        self.movvingAverage('Low', 10)
        self.daily_return('High')
        self.daily_return('Low')
        self.calculReturnRate('W')


    def CorrWithAnotherData(self, other):
        print("correlation between", self.path, "and", other.path)
        print(self.df.corrwith(other.df))


def closest_value( input_value):
    input_list = [1, 7, 30, 365]
    input_list.sort(reverse=True)

    difference = lambda input_list: abs(input_list - input_value)

    res = min(input_list, key=difference)
    if(res==1):
        return "daily"
    elif(res==7):
        return "weekly"
    elif(res==30):
        return "monthly"
    elif(res==365):
        return "yearly"
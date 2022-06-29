import pandas as pd


amazon = pd.read_csv('stocks_data/AMAZON.csv')
apple = pd.read_csv('stocks_data/APPLE.csv')
facebook = pd.read_csv('stocks_data/FACEBOOK.csv')
google = pd.read_csv('stocks_data/GOOGLE.csv')
microsoft = pd.read_csv('stocks_data/MICROSOFT.csv')
tesla = pd.read_csv('stocks_data/TESLA.csv')
zoom = pd.read_csv('stocks_data/ZOOM.csv')

data = [amazon, apple, facebook, google, microsoft, tesla, zoom]
#dataframe = pd.concat(amazon)

def printtail(data):
    print(data.tail(40))

def printhead(data):
    print(data.head(40))

def sizedata(data):
    return len(data)



def description(dataframe):
    print(min(dataframe.High))
    print(max(dataframe.High))

    print(dataframe.isnull())
    print(dataframe.std())
    print(dataframe.corr())

def timeGap(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], errors='coerce')
    a = dataframe.loc[1,'Date'] -dataframe.loc[0,'Date']
    print(a)
    return a

def maxCol(dataframe,colname):
    a = dataframe[colname].max()
    print(a)
    return a

def minCol(dataframe,colname):
    a = dataframe[colname].min()
    print(a)
    return a

def standarDeviationCol(dataframe,colname):
    a = dataframe[colname].std()
    print(a)
    return a

def meanCol(dataframe,colname):
    a = dataframe[colname].mean()
    print(a)
    return a

def missingVallue(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], errors='coerce')
    a = timeGap(dataframe)
    b = dataframe.loc[len(dataframe)-1, 'Date'] - dataframe.loc[0, 'Date']
    print(a)
    print(b)
    print(len(dataframe))



def moving_average(data_frame,column_name,nb_point):
    sum = 0
    for i in range(0,nb_point) :
        sum = sum + data_frame.loc[i,column_name]



def reorganizedataframe(dataframe):
    dataframe['Date'] = pd.to_datetime(dataframe['Date'], errors='coerce')
    dataframe.set_index('Date', inplace=True)
    return dataframe


amazon.info()
amazon = reorganizedataframe(amazon)
print(amazon)
a = amazon.resample('1W').mean()
print(a)
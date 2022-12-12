import pandas as pd

readfile = "../csv/weather_106_2.csv"
writefile = "../csv/weather_106_sorted.csv"
data = pd.read_csv(readfile)
  
# sorting data frame by a column
data.sort_values(["month","day","minute","hour"], axis=0,
                 ascending=[True, True, True, True], inplace=True)
  
data.to_csv(writefile, sep=',', index=False)
# display
print(data.head(100))

#https://www.wunderground.com/weather/ca/ottawa/IOTTAW175
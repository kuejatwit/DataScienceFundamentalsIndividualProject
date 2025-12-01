import pandas as pd

#import data
data = pd.read_csv("/home/jared/Documents/Fall2025/Data Science Fundamentals/Final Project/IndividualProj/data/jared.csv")
#split data by muslce state
closedFist = data[data['muscle_state'] == 0]
openFist = data[data['muscle_state'] == 1]
#save split data
closedFist.to_csv("/home/jared/Documents/Fall2025/Data Science Fundamentals/Final Project/IndividualProj/data/closedFist.csv", index=False)
openFist.to_csv("/home/jared/Documents/Fall2025/Data Science Fundamentals/Final Project/IndividualProj/data/openFist.csv", index=False)

# HistoricalQuotes
# Close/Last

from cmath import sqrt
from math import floor
from pandas import *
import numpy as np

# assume initial weight
#w_init = np.array([0.5, 0.5])

def Euclidian(x1, x2):
    ans = sqrt(pow(x1,2) + pow(x2,2))
    return ans


def nextWeights(err, prevW, t_arr, x1, x2):
    newW = prevW + (np.dot(((err)/(pow(Euclidian(x1,x2),2))), t_arr))
    return newW

def Predict(mon_arr):
    pred_arr = np.zeros(floor(len(mon_arr)/2))
    w = np.array([0.5, 0.5])
    x = 0
    j = 3
    for i in range(1, len(mon_arr), 2):
        temp_arr = np.array([mon_arr[i], mon_arr[i-1]])
        pred = np.dot(w, temp_arr)
        pred_arr[x] = pred
        error = mon_arr[j] - pred
        w = nextWeights(error, w, temp_arr, mon_arr[i], mon_arr[i-1])
        x+=1
        j+=1
    return pred_arr



# reading CSV file
data = read_csv("HistoricalQuotes.csv")
 
# converting column data to list
month = data['Close/Last'].tolist()

#taking out the '$' signs
x = 0
for i in month:
    month[x] = float(i[1:])
    x+=1

month_arr = np.array(month)
predictions = Predict(month_arr)
print("\nPredictions Array: " , predictions)

x = 0
N = len(predictions)
MSE = 0
for i in range(1, len(month_arr), 2):
    MSE += (1/N) * (pow((predictions[x] - month_arr[i]), 2))
    x+=1

print("\nMSE:", MSE)
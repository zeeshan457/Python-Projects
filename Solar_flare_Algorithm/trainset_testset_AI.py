import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lm
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

file = "C:\\Users\\zeeshan\\Desktop\\Solar_Flares_Dataset.xlsx"
File_Reader = pd.read_excel(file)


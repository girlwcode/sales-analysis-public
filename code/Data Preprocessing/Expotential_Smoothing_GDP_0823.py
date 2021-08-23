import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt


gdp = pd.read_csv('../../resource/External_Feature/GDP_transpose.csv.csv')
hdi = pd.read_csv('../../resource/External_Feature/HDI_transpose.csv.csv')
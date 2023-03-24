import pandas as pd 
from urllib.request import urlopen

from pgmpy.models import BayesianModel

names = "A,B,C,D,E,F,G,H,I,J,K,L,M RESULT"
names = names.split(",")

data = pd.read_csv(urlopen("https://bit.do/heart-disease"),names=names)

data.head()
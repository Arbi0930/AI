import pandas as pd 
from urllib.request import urlopen
from pgmpy.models import BayesianModel

names = "A,B,C,D,E,F,G,H,I,J,K,L,M,үр дүн"
data = pd.read_csv(urlopen("https://bit.do/heart-disease"), names=names)

model = BayesianModel([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'),
                       ('F', 'G'), ('G', 'H'), ('H', 'I'), ('I', 'J'), ('J', 'RESULT'), 
                       ('K', 'үр дүн'), ('L', 'үр дүн'), ('M', 'үр дүн')])
model.fit(data)

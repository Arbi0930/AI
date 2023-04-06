import pandas as pd
import pymc4 as pm
import tensorflow as tf

# Read CSV 
df = pd.read_csv('lab5\data.csv')

# Define the model
def model():
    beta = yield pm.Normal('beta', loc=0, scale=10, sample_shape=df.shape[1]-1)
    sigma = yield pm.HalfCauchy('sigma', beta=10)
    y = yield pm.Normal('y', loc=pm.math.dot(df.iloc[:, :-1].values, beta), scale=sigma, observed=df.iloc[:, -1].values)

# Compile the model
compiled_model = pm.compile_model(model)

# Sample from the model
trace = compiled_model().sample(1000, num_chains=4, burn_in=1000)

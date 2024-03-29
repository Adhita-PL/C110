import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv("newdata.csv") 
data = df["average"].tolist() 
population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)
#fig = ff.create_distplot([data], ["average"], show_hist=False)
#fig.add_trace(go.Scatter(x = [population_mean, population_mean], y = [0,1], mode = "lines", name = "mean"))  
#fig.show() 
print("Population mean: ", population_mean)
print("Population standard deviation: ", population_stdev) 
"""
dataset = []
for i in range(0 , 100) :
    random_index = random.randint(0, len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset) 
stdev = statistics.stdev(dataset)
print("Mean of sample:", mean)
print("standard deviation of sample:", stdev)  
"""


def random_set_of_mean(counter) :
    dataset = []
    for i in range(0 , counter) :
        random_index = random.randint(0, len(data)-1) 
        value = data[random_index]
        dataset.append(value) 
    mean = statistics.mean(dataset)  
    return mean

def show_fig(mean_list) :
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0,1], mode = "lines", name = "mean"))  
    fig.show() 

def setup() :
    mean_list = []
    for n in range(0, 1000) :
        set_of_means = random_set_of_mean(100)  
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    stdev = statistics.stdev(mean_list)
    print("Mean of the sampling distribution is :", mean) 
    print("Standard deviation of sampling distribution is :" , stdev) 
setup() 
 
import pandas as pd
import numpy as np
from IPython.display import  display,HTML
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
import pickle
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



def plotColumnwiseCount(c1='',c2='',data):
    plt.figure(figsize = (15,15))
    plt.subplot(3,2,1)
    sns.countplot(x = c1, hue = c2, palette = 'Set2', data = data.toPandas())



def get_spark(name="project") -> SparkSession:
    return SparkSession.builder.appName(name).getOrCreate()



def dumpPickle(model,name):
    pickle.dump(model, open(name+".pkl", 'wb'))
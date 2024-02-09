import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import minmax_scale
import pandas as pd


data = pd.read_csv("S:/project/ml projects/health related project/heart.csv")

x = data.drop(["output"],axis=1)
y = data["output"]

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2)

model = tf.keras.models.Sequential([    
    tf.keras.layers.Dense(100,activation="relu"),
    tf.keras.layers.Dense(100,activation="relu"),
    tf.keras.layers.Dense(10,activation="relu"),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1,activation="sigmoid")
])

model.compile(loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["accuracy"])

model.fit(x_train,y_train,epochs=50)
new = [51, 1, 0, 140, 299,0,1, 173, 1, 1.6, 2, 0, 3]
pred = model.predict(tf.expand_dims(new,axis=0))

ans=int(tf.round(pred))

if ans==0:
    print("not a heart desice")
else:
    print("Be carefull")

from enum import unique
import tensorflow as tf
import time
import os
import pandas as pd

import matplotlib.pyplot as plt

def create_model(LOSS_FUNCTION,OPTIMIZER,METRICS):
    LAYERS=[tf.keras.layers.Flatten(input_shape=[28,28],name="inputlayer"),
        tf.keras.layers.Dense(300,"relu",name="hiddenlayer"),
        tf.keras.layers.Dense(100,"relu",name="hiddenlayer2"),
        tf.keras.layers.Dense(10,"softmax",name="outputlayer")
        ]
    
    model_clf=tf.keras.Sequential(LAYERS)
    model_clf.summary()

    

    model_clf.compile(loss=LOSS_FUNCTION,
                    optimizer=OPTIMIZER,
                    metrics=METRICS)

    return model_clf

def get_unique_filename(filename):
    unique_filename=time.strftime(f"%Y-%m-%d_%H%M%S_{filename}")
    return unique_filename

def save_model(model,model_name,model_dir):
    unique_filename=get_unique_filename(model_name)
    path_to_model=os.path.join(model_dir,unique_filename)

    model.save(path_to_model)

def save_plot(loss_acc,plotName,plot_dir):
    unique_filename=get_unique_filename(plotName)
    path_to_plot=os.path.join(plot_dir,unique_filename)
    pd.DataFrame(loss_acc).plot(figsize=(10,7))
    plt.grid(True)
    plt.savefig(path_to_plot)
    plt.show()
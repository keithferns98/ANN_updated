import tensorflow as tf

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
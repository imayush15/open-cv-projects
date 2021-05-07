import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Importing the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Visualizing the Dataset
# plt.imshow(x_train[0], cmap=plt.cm.binary)
# plt.show()

# Normalizing the Dataset
x_train = tf.keras.utils.normalize(x_train)
x_test = tf.keras.utils.normalize(x_test)

# Building the Model
model = tf.keras.models.Sequential()

# Adding layer to model
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics = ['accuracy'])

model.fit(x_train, y_train,epochs=6)

# val_loss, val_acc = model.evaluate(x_test, y_test)
# print(val_loss, val_acc)

# Saving the Model
model.save("HandwritingPrediction.model")

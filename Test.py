import tensorflow as tf
import HandWrittenDigits as h
import numpy as np
new_mod = tf.keras.models.load_model("HandwritingPrediction.model")

predictions = new_mod.predict(h.x_test)
print(np.argmax(predictions[0]))
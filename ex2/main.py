import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

class myCallback(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy') > 0.99):
      print('\nModel reached 0.99 accuracy, cancelling training!')
      self.model.stop_training = True

def main():
  mnist = keras.datasets.mnist
  (x_train, y_train), (x_test, y_test) = mnist.load_data()
  x_train, x_test =  x_train / 255.0, x_test / 255.0
  model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
  ])

  callbacks = myCallback()
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
  model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
  model.evaluate(x_test, y_test)
  # plt.imshow(x_train[0])

if __name__ == '__main__':
  main()
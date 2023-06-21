import tensorflow as tf
from tensorflow.keras import layers

class Discriminator(tf.keras.Model):
    def __init__(self):
        super(Discriminator, self).__init__()

        self.conv1 = layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same', input_shape=[28, 28, 1])
        self.leaky_relu1 = layers.LeakyReLU()
        self.dropout1 = layers.Dropout(0.3)

        self.conv2 = layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same')
        self.leaky_relu2 = layers.LeakyReLU()
        self.dropout2 = layers.Dropout(0.3)

        self.flatten = layers.Flatten()

        self.dense1 = layers.Dense(1)

    def call(self, inputs):
        x = self.conv1(inputs)
        x = self.leaky_relu1(x)
        x = self.dropout1(x)

        x = self.conv2(x)
        x = self.leaky_relu2(x)
        x = self.dropout2(x)

        x = self.flatten(x)

        x = self.dense1(x)

        return x

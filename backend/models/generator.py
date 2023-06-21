import tensorflow as tf
from tensorflow.keras import layers

class Generator(tf.keras.Model):
    def __init__(self):
        super(Generator, self).__init__()

        self.dense1 = layers.Dense(7*7*256, use_bias=False, input_shape=(100,))
        self.batch_norm1 = layers.BatchNormalization()
        self.leaky_relu1 = layers.LeakyReLU()

        self.reshape1 = layers.Reshape((7, 7, 256))

        self.conv_transpose1 = layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False)
        self.batch_norm2 = layers.BatchNormalization()
        self.leaky_relu2 = layers.LeakyReLU()

        self.conv_transpose2 = layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False)
        self.batch_norm3 = layers.BatchNormalization()
        self.leaky_relu3 = layers.LeakyReLU()

        self.conv_transpose3 = layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh')

    def call(self, inputs):
        x = self.dense1(inputs)
        x = self.batch_norm1(x)
        x = self.leaky_relu1(x)

        x = self.reshape1(x)

        x = self.conv_transpose1(x)
        x = self.batch_norm2(x)
        x = self.leaky_relu2(x)

        x = self.conv_transpose2(x)
        x = self.batch_norm3(x)
        x = self.leaky_relu3(x)

        x = self.conv_transpose3(x)

        return x

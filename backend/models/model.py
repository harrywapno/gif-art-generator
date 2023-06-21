import tensorflow as tf
from tensorflow.keras import optimizers
from .generator import Generator
from .discriminator import Discriminator

class GAN:
    def __init__(self):
        self.generator = Generator()
        self.discriminator = Discriminator()
        self.cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)
        self.generator_optimizer = optimizers.Adam(1e-4)
        self.discriminator_optimizer = optimizers.Adam(1e-4)
        self.checkpoint_prefix = './checkpoints/train'
        self.checkpoint = tf.train.Checkpoint(generator_optimizer=self.generator_optimizer,
                                              discriminator_optimizer=self.discriminator_optimizer,
                                              generator=self.generator,
                                              discriminator=self.discriminator)

    def discriminator_loss(self, real_output, fake_output):
        real_loss = self.cross_entropy(tf.ones_like(real_output), real_output)
        fake_loss = self.cross_entropy(tf.zeros_like(fake_output), fake_output)
        total_loss = real_loss + fake_loss
        return total_loss

    def generator_loss(self, fake_output):
        return self.cross_entropy(tf.ones_like(fake_output), fake_output)

    @tf.function
    def train_step(self, images):
        noise = tf.random.normal([Config.BATCH_SIZE, 100])

        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            generated_images = self.generator(noise, training=True)

            real_output = self.discriminator(images, training=True)
            fake_output = self.discriminator(generated_images, training=True)

            gen_loss = self.generator_loss(fake_output)
            disc_loss = self.discriminator_loss(real_output, fake_output)

        gradients_of_generator = gen_tape.gradient(gen_loss, self.generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(disc_loss, self.discriminator.trainable_variables)

        self.generator_optimizer.apply_gradients(zip(gradients_of_generator, self.generator.trainable_variables))
        self.discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, self.discriminator.trainable_variables))

    def train(self, dataset, epochs):
        for epoch in range(epochs):
            for image_batch in dataset:
                self.train_step(image_batch)

            if (epoch + 1) % 10 == 0:
                self.checkpoint.save(file_prefix=self.checkpoint_prefix)

    def generate_image(self, parameters):
        noise = tf.random.normal([1, 100])
        for i, param in enumerate(parameters):
            noise[0][i] = param
        return self.generator(noise, training=False).numpy()[0]
    
    def load_models(self):
        self.generator.load_weights('./models/generator.h5')
        self.discriminator.load_weights('./models/discriminator.h5')

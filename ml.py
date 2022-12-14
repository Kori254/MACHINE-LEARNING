import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

fashion=tf.keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=fashion.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)


probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])


predictions = probability_model.predict(test_images)

print(np.argmax(predictions[0]))

print(test_labels[0])
from __future__ import absolute_import, division, print_function, unicode_literals
import re
import tensorflow as tf
import pandas as pd
from tensorflow import keras
from tensorflow._api.v2 import feature_column


CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth',
                    'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']

train_path = tf.keras.utils.get_file(
    "iris_training.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv")
test_path = tf.keras.utils.get_file(
    "iris_test.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv")
train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)

train_y = train.pop("Species")
trest_y = test.pop("Species")


print(train.head())


def input_fn(features, labels, training=True, batch_size=256):
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle and repeat if you are in training mode.
    if training:
        dataset = dataset.shuffle(1000).repeat()

    return dataset.batch(batch_size)


my_feature_columns = []

for key in train.keys():
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))
print(my_feature_columns)

classifier = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    # Two hidden layers of 30 and 10 nodes respectively.
    hidden_units=[30, 10],
    # The model must choose between 3 classes.
    n_classes=3)

classifier.train(
    input_fn=lambda: input_fn(train, train_y, training=True),
    steps=5000)
eval_result = classifier.evaluate(
    input_fn=lambda: input_fn(train, train_y, training=False))


def input_fn(features, batch_siz=256):
    df = tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_siz)
    return df


features = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']
predict = {}

print("Please type numeric values as prompted.")
for feature in features:
    valid = True
    while valid:
        val = input(feature + ": ")
        if not val.isdigit():
            valid = False
    predict[feature] = [float(val)]


predictions = classifier.predict(input_fn=lambda: input_fn(predict))


for prod_ict in predictions:
    classid = prod_ict['class_ids'][0]
    probability = prod_ict["probabilities"][0]

probability = probability*100

print('Prediction is "{}" ({:.1f}%)'.format(
    SPECIES[classid], probability))

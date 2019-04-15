from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./data/MNIST/", one_hot=True)

print("successfully")
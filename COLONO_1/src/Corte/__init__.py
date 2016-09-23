import numpy as np
import pylab as pl
import neurolab as nl



min_value = -11
max_value = 11
x = np.linspace(min_value, max_value, 40)
y = np.square(x) + 5
y = y / np.linalg.norm(y)
print len(y)
num_samples = len(x)
input_data = x.reshape(num_samples, 1)
output_labels = y.reshape(num_samples, 1)


multilayer_net = nl.net.newff([[min_value, max_value]], [10, 10, 1])
multilayer_net.trainf = nl.train.train_gd
print input_data
print output_labels
error = multilayer_net.train(input_data, output_labels, epochs=1000, show=100, goal=0.001)


predicted_output = multilayer_net.sim(input_data)

print predicted_output

x2 = np.linspace(-11, 11, 80)
y2 = multilayer_net.sim(x2.reshape(x2.size,1)).reshape(x2.size)
y3 = predicted_output.reshape(num_samples)
pl.figure(1)
pl.subplot(212)
pl.plot(x2, y2, '-', x, y, '.', x, y3, 'p')
pl.legend(['train target', 'network output'])
pl.show()
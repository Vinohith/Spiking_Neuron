# Spiking_Neuron
<br><br>

The neural networks based on their computational unit can be distinguished into three generations:
1. **First Generation**: This generation of neural networks included the perceptron, hopfield networks, boltzmann machines etc.<br>
2. **Second Generation**: This generation of neural networks included multi-layer neural nets, recurrent networks etc.<br>
3. **Third Generation**: This generation of neural networks includes the Spiking neural networks which is a more realistic representation of the working and information flow within the brain.<br><br>

The cortical neurons in the brain produces spiking and busting behaviour. Spiking Neurons are motivated by this behaviour of cortical neurons. The model presented tries to combine the biological plausibility of the Hodgkin-Huxley type dynamics and computational efficiency of the integrate and fire neurons. To produce this kind of behaviour four parameters and two variables are used.<br>
These variables are:
1. **v**: This variable represents the membrane potential of the neuron. This value is between -70mV to -60mV.
2. **u**: This variable represents the membrane recovery potential which provides the negative feedback in the neuron.

These parameters are:
1. **a**: This variable represents the decay rate of the recovery variable u.
2. **b**: This variable represents the sensitivity of recovery variable u to sub-threshold fluctuations in membrane potential v.
3. **c**: This variable represents the after spike reset value of the membrane potential v.
4. **d**: This variable represents the after spike reset value of the recovery variable u.

The choice of values for these parameters leads to different types of spiking, namely:
1. **Regular Spiking (RS)**
2. **Intrinsically Bursting (IB)**
3. **Chattering (CH)**
4. **Fast Spiking (FS)**
5. **Low-threshold Spiking (LTS)**
6. **Thalamo-cortical (TC)**
7. **Resonator (RZ)**

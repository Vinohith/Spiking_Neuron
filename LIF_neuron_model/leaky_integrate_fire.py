import matplotlib.pyplot as plt
import numpy as np



#declaring some global variables
V = []
spike_time = []
v_threshold = -60



#describing the neuron model
class leaky_integrate_and_fire_neuron_model:
    def __init__(self):
        self.membrane_resistance = 10000
        self.membrane_capicatance = 0.001
        self.tau = self.membrane_resistance * self.membrane_capicatance
        self.v = -70
        self.v_rest = -65
        self.v_reset = -65
        self.input_current = 0.001


        
#initializing the model
model = leaky_integrate_and_fire_neuron_model()



#defining the function of the neuron
def neuron(v, v_reset, v_rest, tau, membrane_resistance, input_current):

    for time in range(0, 100):

        v += (1/tau) * (-(v - v_rest) + membrane_resistance * input_current)
        if v >= v_threshold:
            #print("Spike Generated")
            V.append(v)
            v = v_reset

        else:
            #print("No Spike")
            V.append(v)

        #print(v)
        spike_time.append(time)


    return V, spike_time



Y, X = neuron(model.v, model.v_reset, model.v_rest, model.tau, model.membrane_resistance, model.input_current)	



plt.xlabel("Time")
plt.ylabel("Membrane potential")
plt.title("Firing of neuron")
plt.plot(X, Y)
plt.show()

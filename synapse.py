import numpy as np
import random
import matplotlib.pyplot as plt
#%matplotlib inline



refractory_time = 5
v_threshold = 4
v_spike = 5
v_ref = 0
time = np.arange(0, 350)
input_synapse = 5
output = 1



class neuron_model:
    def __init__(self):
        self.membrane_resistance = 10000
        self.membrane_capicatance = 0.001
        self.tau = self.membrane_resistance * self.membrane_capicatance
        self.v_ref = 0
        self.v_rest = -1
        self.v_reset = -1
        
        

def out(S, w, v_ref, v_rest, tau):
    
    t_rest = 0
    v = np.zeros(len(time))
    spike = np.zeros(len(time))
    
    for i, t in enumerate(time):
        
        if t < t_rest:
            v[i] = v_ref
            spike[i] = 0
        elif t > t_rest:
            x1 = S[:,i]	
            v[i] = v[i-1] + ((1/tau) * (-(v[i-1] - v_rest) + np.dot(w, x1)))
            spike[i] = 0

        if v[i] >= v_threshold:
            v[i] += v_spike
            t_rest = t + refractory_time
            spike[i] = 1
            
    return v, spike



model = neuron_model()



np.random.seed(1)
random.seed(1)
weights = np.random.randint(0, 5, (output, input_synapse))
synapse = []



for i in range(input_synapse):
    
    temp = []
    
    for i in range(len(time)):
        
        x = random.randrange(0, 2)
        temp.append(x)
    synapse.append(temp)
    
synapse = np.array(synapse)



output_v, output_spikes = out(synapse, weights, model.v_ref, model.v_rest, model.tau)



plt.title('Neuron Response')
plt.xlabel('Time of firing')
plt.ylabel('Neuron output Potential')
plt.plot(time, output_v)
plt.show()



plt.title('Neuron Spiking')
plt.xlabel('Spiking time')
plt.ylabel('Spike')
plt.plot(time, output_spikes)
plt.show()
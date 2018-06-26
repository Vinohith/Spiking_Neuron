#author = Vinohith
#Spiking Neuron

import matplotlib.pyplot as plt


#declaring some global variables
V = []
U = []
spike_time = []
v_threshold = 30



#describing the neuron model
class neuron_model:
	def __init__(self):
		#decay rate of membrane recovery variable (u)
		self.a = 0.02
		#sensitivity of membrane recovery variable (u) to sub-threshold fluctuations
		self.b = 0.2
		#reset variable of membrene potential (v)
		self.c = -65
		#after spike reset value of membrane recovery variable (u)
		self.d = 8
		#membrane potential
		self.v = -65
		#membrane recovery variable (u)
		self.u = self.b * self.v
		#simulation time step
		self.simulation_time_step = 0.05
		#input current (can be made variable instead of a constant value)
		self.input_current = 10

		
		
#initializing the model
model = neuron_model()



#defining the function of the neuron
def neuron(v, u, a, b, c, d, simulation_time_step, input_current):

	for time in range(0, 1000):
	
		V.append(v)
		U.append(u)
		spike_time.append(time)
		
		if v >= v_threshold:
			print("Spike Generated")
			v = c
			u = u+d
			
		else:
			print("No Spike")
			
		print(v)
		v += simulation_time_step*(0.04*v**2 + 5*v + 140 - u + input_current)
		u += a*(b*v - u)
		
	return V, U, spike_time


Y1, Y2, X = neuron(model.v, model.u, model.a, model.b, model.c, model.d, model.simulation_time_step, model.input_current)

	
plt.xlabel("Time")
plt.ylabel("Membrane potential")
plt.title("Firing of neuron")
plt.plot(X, Y1)
plt.show()
plt.xlabel("Time")
plt.ylabel("Recovery variable")
plt.title("Recovery of neuron")
plt.plot(X, Y2)
plt.show()

# Leaky Integrate and Fire Neuron Model
<br>
The Leaky Integrate and Fire (LIF) Neuron is  one of the simplest spiking neuron models, but it is still very popular due to the ease with which it can be analyzed and simulated.
It is modeled as a 'leaky integrator' of the input current (here I(t) ).<br>
The equation governing the LIF Neuron Model:<br>
<p align='center'>
  <img src='/LIF_neuron_model/LIF_equation.png'/>
</p>

Here, **u(t)** represents the membrane potential at time t, **u<sub>rest</sub>** represents the membrene resting potential,  **τ<sub>m</sub>** is the membrane time constant and **R** is the membrane resistance.<br>

The equation describes a simple resistor-capacitor (RC) circuit where the leakage term is due to the resistor and the integration of **I(t)** is due to the capacitor that is in parallel to the resistor. The neuron produces a spike when the potential **u(t)** governed by the equation reaches a threshold potential **u<sub>thresh</sub>**.

<br>

### Generated Graphs<br>
1. **Constant input current**
<img width='500' height='300' src='/LIF_neuron_model/Graphs/leaky_integrate_and_fire.png'/>

2. **Time-varying input current**
<img width='500' height='300' src='/LIF_neuron_model/Graphs/synapse.png'/>


### Reference:<br>
[Neuronal Dynamics](http://neuronaldynamics.epfl.ch/online/Ch1.S3.html)

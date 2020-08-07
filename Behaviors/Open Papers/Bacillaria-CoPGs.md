## Collective Pattern Generators: behavioral signatures of environmental interactions

#### Main Idea:
Central Pattern Generators (CPGs) generate oscillations from a small neural circuit (pacemaker neurons). In neuronal systems, CPGs generate oscillations from a small neural circuit (pacemaker neurons).

In _Bacillaria_, we observe collective pattern generators (CoPGs), which are generated from collective and coordinated behavior. No central nervous system or brain is involved.  

#### Aneural Architecture
_Bacillaria_ behavior-generation system looks like the following:

* no spatial representation (free-moving), but does exhibit limited goal-directed behavior.

* movement as the seat of intelligence, as suggested in particular Michael Graziano's "Intelligent Movement Machine".

* produces a set of sine waves, one for each pair of filaments.

* the entire chain produces an oscillator with harmonics (delayed by _n_ degrees out-of-phase).  

* potentially we may see spindles at the extremes of each cycle (pauses in oscillation or changes in orientation).

#### How to model:

* model sine waves, sinusoidals, and hybrid sinusoidal-tangent functions.

* how do these map measurements in the previous Bacillaria paper?

Each pair of filamentous cells act as an oscillatory unit in a CoPG. Oscillatory units overlap, so that a colony of 7 filaments consist of 6 oscillatory units. While they generally produce a sine wave, they can also stretch to a maximal value and stay there for long periods of time.

* modeling modes of movement behavior from microscopy data.

#### CPGs in a stick insect: synergistic CPGs

Paper: Daun et.al (2019). [Unravelling intra- and intersegmental neuronal connectivity between central pattern generating networks in a multi-legged locomotor system](https://pubmed.ncbi.nlm.nih.gov/31386699/). _PLoS One_, 14(8), e0220767.

Dataset: [Figshare](https://figshare.com/articles/Data_from_Unravelling_intra-_and_intersegmental_neuronal_connectivity_between_central_pattern_generating_networks_in_a_multi-legged_locomotor_system/7831772/1)

Figure showing integration of multiple legs.

#### Simulation: 

<p align="center">
  <img width="256" height="227" src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/tangent-at-positive-1.png"><BR>
  Sine wave with tangent at quarter-phase
</p>
<p align="center">
  <img width="256" height="227" src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/tangent-at-negative-1.png"><BR>
  Sine wave with tangent at three-quarter phase
</p>
<p align="center">
  <img width="256" height="227" src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/out-of-phase-quarter-phase-25.png"><BR>
  Two adjacent and overlapping pairs of oscillatory cell movments (sine waves, quarter-phase)
</p>
<p align="center">
  <img width="256" height="227" src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/out-of-phase-quarter-phase-75.png"><BR>
  Two adjacent and overlapping pairs of oscillatory cell movments (sine waves, three-quarter phase)
</p>
<p align="center">
  <img width="256" height="227" src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/attractor-90-degrees-out-of-phase.png"><BR>
  Attractor map (based on sine waves, quarter-phase)
</p>
<p align="center">
  <img width="256" height="227" src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/noisy-sine-wave-sample.png"><BR>
  Sine wave with random (white) noise
</p>
  
#### Analysis
Using methods derived to analyze CPGs, we can use at least three types of technique: [bifurcation analysis](http://www.scholarpedia.org/article/Bifurcation), a simple [return map](https://www.vanderbilt.edu/AnS/psychology/cogsci/chaos/workshop/Tools.html), and a [Poincare maps](https://en.wikipedia.org/wiki/Poincar%C3%A9_map). A [recurrence map](https://en.wikipedia.org/wiki/Recurrence_plot) can be used in lieu of a Poincare map.

In terms of a state transition from oscillator to stretched out, do we observe halting behavior? Can this be controlled by the colony, or is this a random behavior?

We can use algorithmic information theory ([Chaitin's constant](https://en.wikipedia.org/wiki/Chaitin%27s_constant)) to approximate the random nature of this behavior. If this is random, then the CoPG can be relaxed due to exogenous forces (aging, hydrodynamics). If it is not random, then there is some endogenous control.

* simulate a range of stopping times (colony oscillates for _n_ cycles, then halts). Use noise inputs to model physical contraints (reach a noise threshold, CoPG "relaxes" and thus halts.

#### Discussion.
Does a simple oscillator provide a means for intelligent behavior? An oscillator provides a deterministic signal that entrains behavior, but does not allow for computation nor information content. 

* in terms of computation, stretching resembles a Turing machine, where stretching can resemble "halting" behaviors. Discuss CoPG relaxing conditions -- due to decoupling of neighbors, self-reinforcing dampening.

* in terms of information content, stopping and stretching allows for symmetry breaking, and thus information. 

* more complex behaviors are not currently known.

__References__  
Arshavsky, Cellular and network properties in the functioning of the nervous system: from central pattern generators to cognition. _Brain Research Reviews_, 41(2–3), 229-267 (2003).  

Graziano, The Intelligent Movement Machine. An Ethological Perspective on the Primate Motor System. Oxford University Press Oxford, UK (2009).  

Hanczyc and Ikegami, Chemical Basis for Minimal Cognition, _Artificial Life_, 16: 233–243 (2010).  

Marder and Bucher, Central pattern generators and the control of rhythmic movements. _Current Biology_, 11(23), R986-R996 (2011).  




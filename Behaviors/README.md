Central Pattern Generators (CPGs) generate oscillations from a small neural circuit (pacemaker neurons). In neuronal systems, CPGs generate oscillations from a small neural circuit (pacemaker neurons).

In _Bacillaria_, we observe collective pattern generators (CoPGs?), which are generated from collective and coordinated behavior. No central nervous system or brain is involved.  

_Bacillaria_ brain looks like the following:

* no spatial representation (free-moving), but does exhibit limited goal-directed behavior.

* movement as the seat of intelligence, as suggested in particular Michael Graziano's "Intelligent Movement Machine".

* produces a set of sine waves, one for each pair of filaments.

* the entire chain produces an oscillator with harmonics (delayed by _n_ degrees out-of-phase).  

* potentially we may see spindles at the extremes of each cycle (pauses in oscillation or changes in orientation).

How to model:

* model sine waves, sinusoidals, and hybrid sinusoidal-tangent functions.

* how do these map measurements in the previous Bacillaria paper?

Each pair of filamentous cells act as an oscillatory unit in a CoPG. Oscillatory units overlap, so that a colony of 7 filaments consist of 6 oscillatory units. While they generally produce a sine wave, they can also stretch to a maximal value and stay there for long periods of time.

* modeling modes of movement behavior from microscopy data.

<p align="center">
  <img src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/tangent-at-positive-1.png"><BR>
  Sine wave with tangent at quarter-phase
</p>
<p align="center">
  <img src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/tangent-at-negative-1.png"><BR>
  Sine wave with tangent at three-quarter phase
</p>
<p align="center">
  <img width="256" height="227" src="https://user-images.githubusercontent.com/19001437/53650847-1835da00-3c0b-11e9-9a3c-71c2eea8c3da.gif"><BR>
  Sine waves (anti-phase)
</p>
<p align="center">
  <img src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/out-of-phase-quarter-phase-25.png"><BR>
  Two adjacent and overlapping pairs of oscillatory cell movments (sine waves, quarter-phase)
</p>
<p align="center">
  <img src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/out-of-phase-quarter-phase-75.png"><BR>
  Two adjacent and overlapping pairs of oscillatory cell movments (sine waves, three-quarter phase)
</p>
<p align="center">
  <img src="https://github.com/devoworm/Digital-Bacillaria/blob/master/Behaviors/attractor-90-degrees-out-of-phase.png"><BR>
  Attractor map (based on sine waves, quarter-phase)
</p>

__References__:  
Arshavsky, Cellular and network properties in the functioning of the nervous system: from central pattern generators to cognition. _Brain Research Reviews_, 41(2–3), 229-267 (2003).  

Graziano, The Intelligent Movement Machine. An Ethological Perspective on the Primate Motor System. Oxford University Press Oxford, UK (2009).  

Hanczyc and Ikegami, Chemical Basis for Minimal Cognition, _Artificial Life_, 16: 233–243 (2010).  

Marder and Bucher, Central pattern generators and the control of rhythmic movements. _Current Biology_, 11(23), R986-R996 (2011).  




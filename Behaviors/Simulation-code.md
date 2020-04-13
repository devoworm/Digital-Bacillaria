### Simulation run in SciLab 6.0

#### Simulation of three-cell colony (two interacting pairs)

x = sin([0:0.01:2*%pi]); // single cycle of a sine wave.  
x = sin([0:0.01:2*8*%pi]); // 8 cycles of a sine wave.  

in general, 0:0.01:n is equivalent to n/2*%pi. // restatement of Nyquist theorem.  

n = length(x); // where n = 629.  
m = n * 0.75 // three-quarter phase resampling (90% out of phase).  
y1 = x(:,n+1:m);  
y2 = x(:,1:n);   
y = cat(2,y1,y2);  
plot(x)  
plot(y)  

[[out-of-phase-quarter-phase-75.png]]  

n = length(x); // where n = 629.  
m = n * 0.50 // half phase resampling (180% out of phase).  
y1 = x(:,n+1:m);  
y2 = x(:,1:n);   
y = cat(2,y1,y2);  
plot(x)  
plot(y)  


n = length(x); // where n = 629.  
m = n * 0.25 // three-quarter phase resampling (90% out of phase).  
y1 = x(:,n+1:m);  
y2 = x(:,1:n);   
y = cat(2,y1,y2);  
plot(x)  
plot(y)  

[[out-of-phase-quarter-phase-25.png]]  

#### Extension of cell pair (tangent from an oscillation)

n = length(x); // where n = 629.  
m = n * 0.75 // three-quarter phase resampling (90% out of phase).  
y11 = n-m+1;  
y1 = ones(1,y11);  
y2 = x(:,1:n);   
y = cat(2,y2,y1);  
plot(x)  
plot(y)  


n = length(x); // where n = 629.  
m = n * 0.50 // half phase resampling (180% out of phase).  
y11 = n-m+1;  
y1 = ones(1,y11);  
y2 = x(:,1:n);   
y = cat(2,y2,y1);  
plot(x)  
plot(y)  


n = length(x); // where n = 629.  
m = n * 0.25 // three-quarter phase resampling (90% out of phase).  
y11 = n-m+1;  
y1 = ones(1,y11);  
y2 = x(:,1:n);   
y = cat(2,y2,y1);  
plot(x)  
plot(y)  

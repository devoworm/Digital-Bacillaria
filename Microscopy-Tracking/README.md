# Multi Object Tracking

The tracking is done on the data extracted from object detection. This implementation assigns each detection in the current frame based on the detection in the previous 
frame. The assignment is based on the nearest neighbor. Sample output from this multi-object tracker implementation 
on [synthetic dataset](movement.npy).

The current implementation performs tracking based on the distance between the detected object in the current frame and the previous frame. In tracking, we want to 
associate detected objects in consecutive frames based on score or cost. Here we have used simple euclidean distance to compute cost. Suppose the current frame has n 
detected objects and the previous frame has m detected object. So the size of the cost matrix will be ( m x n ). The goal is to determine the optimum assignment for each 
object in the current frame to the object in the previous frame that, minimizes the total cost. The Hungarian algorithm is used to find this optimal assignment and this 
assignment can be used in tracking. A more detailed explanation can be found [here](http://www.hungarianalgorithm.com/index.php).

## How to run 
```bash
python Image-tracking.py --input movement.npy --h 512 --w 512
```

## It'll generates:
```
   - Multi-Tracking_Result.gif
```

## Sample Output:
<p align="center">
  <img src="Multi-Tracking_Result.gif" alt="Multi Object Tracking" height="400" width="400" />
  <p align="center">Sample Multi Obejct Tracking output</p>
</p>

## References
- https://en.wikipedia.org/wiki/Hungarian_algorithm
- http://www.hungarianalgorithm.com/index.php
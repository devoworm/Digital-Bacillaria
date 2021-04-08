# Multi Object Tracking

The tracking is done on the data extracted from object detection. This implementation assigns the each detection in the current frame based on the detection in previous frame. The assignment is based on nearest neighbour. Sample output from this multi object tracker implementation on [synthetic dataset](movement.npyy).

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

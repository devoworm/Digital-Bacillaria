import numpy as np 
import cv2
import time
import imageio
from scipy.optimize import linear_sum_assignment
import argparse
import os
import sys

def createimage(w,h):
	size = (w, h, 1)
	img = np.ones((w,h,3),np.uint8)*255
	return img

def Cost(pre_frame, cur_frame):
  cost = np.zeros((pre_frame.shape[0], cur_frame.shape[0]))
  for i in range(cur_frame.shape[0]):
    cost[:,i] = ((pre_frame - cur_frame[i])**2).sum(axis=-1)
  return cost

def trackData(path_to_detections, img_shape):

    if not os.path.exists(path_to_detections):
        print("input file does not exists:", path_to_detections)
        sys.exit(1)

    data = np.array(np.load(path_to_detections))


    track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                (127, 127, 255), (255, 0, 255), (255, 127, 255),
                (127, 0, 255), (127, 0, 127),(127, 10, 255), (0,255, 127)]
    # print( data[:,2,:])
    
    for i in range(1,data.shape[1]):
        pre_frame = data[:,i-1,:]
        cur_frame = data[:,i,:]
        cost = Cost(pre_frame, cur_frame)
        row_ind, col_ind = linear_sum_assignment(cost)
        data[:,i,:] =data[col_ind,i,:]
    # print( data[:,2,:])
    
    images =[]
    h, w = img_shape
    for i in range(data.shape[1]):
        centers =  data[:,i,:]
        frame = createimage(w, h)                   #2D image shape

        for j in range(data.shape[0]):
            x = int( data[j,i,0])
            y = int( data[j,i,1])

            cv2.circle(frame,(x, y), 6, track_colors[j], -1)
            tl = (x-10,y-10)
            br = (x+10,y+10)
            cv2.rectangle(frame,tl,br,track_colors[j],1)
            cv2.putText(frame,str(j), (x-10,y-20),0, 0.5, track_colors[j],2)

            for k in range(1,i):
                cv2.line(frame, tuple( data[j,k-1,:]), tuple( data[j,k,:]), track_colors[j], 1)

        images.append(frame)
    
    imageio.mimsave('Multi-Tracking_Result.gif', images, duration=0.05)

    return  data, cost[col_ind, row_ind]

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--input", help="Path to file of detection in .npy format", required=True)
    parser.add_argument("--h", help="height of image ", required=True)
    parser.add_argument("--w", help="width of image ", required=True)
   
    args = parser.parse_args()

    trackData(args.input, [int(args.h), int(args.w)])


if __name__ == "__main__":
    main()
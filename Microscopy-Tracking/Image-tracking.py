import numpy as np 
import cv2
import time
import imageio
from scipy.optimize import linear_sum_assignment

def createimage(w,h):
	size = (w, h, 1)
	img = np.ones((w,h,3),np.uint8)*255
	return img

def Cost(pre_frame, cur_frame):
  cost = np.zeros((pre_frame.shape[0], cur_frame.shape[0]))
  for i in range(cur_frame.shape[0]):
    cost[:,i] = ((pre_frame - cur_frame[i])**2).sum(axis=-1)
  return cost

def trackData(path_to_detections):
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

    for i in range(data.shape[1]):
        centers =  data[:,i,:]
        frame = createimage(512,512)                   #2D image shape

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
    
    imageio.mimsave('Microscopy-Tracking/Multi-Tracking_Result.gif', images, duration=0.05)

    return  data, cost[col_ind, row_ind]

trackData("Microscopy-Tracking/movement.npy")
import datetime
import os
import time
import argparse
from scipy import stats as s
from PIL import Image
import torch
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from torchvision import transforms
import numpy as np
import imutils

def predict(image, model):
    preprocess = transforms.Compose([transforms.ToTensor()])
    img = preprocess(image)

    batch_img = torch.unsqueeze(img, 0)
    model.eval()
    with torch.no_grad():
        prediction = model(batch_img)
    return prediction

def rotate_image(mat, angle):
    height, width = mat.shape[:2] 
    image_center = (width/2, height/2) 

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat
def main():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--image", help="path to test image", required=True)
    parser.add_argument("--model", help="Path to pretrained model", required=True)
    parser.add_argument("--device", help="device", default=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'))
   
    args = parser.parse_args()

    model = torch.load(args.model,  map_location=args.device)

    img = cv2.imread(args.image)
    shape =  img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)

    slope = []
    length = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x2-x1:
            slope.append((y2-y1)/float(x2-x1))
        length.append(np.linalg.norm([x2-x1, y2-y1]))

    theta = int(np.rad2deg(np.arctan(np.min(s.mode(slope)))))
    
    if theta > 45:
        theta = theta - 90
    if theta < -45:
        theta = theta + 90
        
    print("Angle :: " + str(theta ))
    
    ### Rotate image
    rot_img = rotate_image(img, theta)
    rot_shape = rot_img.shape

    image = rot_img
    prediction = predict(image, model)
    indc = [(ind) for ind,obj in enumerate(prediction[0]['scores']) if obj>0.6]
    print(prediction[0]['scores'][indc])

    for box in prediction[0]['boxes'][indc].cpu().numpy():
        start_point = (box[0], box[1])
        end_point = (box[2], box[3])
    
        image = cv2.rectangle(image, start_point, end_point, color=(255,0,0), thickness=2)

    #cv2.imwrite("rot_pred_image.jpg",image)
    start_x =int((rot_shape[0]-shape[0])/2)
    start_y =int((rot_shape[1]-shape[1])/2)
    #plt.imshow(image)

    ### ReRotate image
    image = imutils.rotate(image, angle=-theta)

    cv2.imwrite(args.image[:-4] + "_pred.jpg",image[start_x:start_x+shape[0],start_y:start_y+shape[1],:])

    #cv2.imshow("predict.jpg",image)
    #cv2.waitKey(0) 
    #cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()
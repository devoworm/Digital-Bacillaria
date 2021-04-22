## Faster RCNN with Auto-rotation


[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YashMaxy/Digital-Bacillaria/blob/master/Tutorials/Faster%20RCNN_PyTorch/Train_Faster_RCNN.ipynb)


The above ipython notebook concisely describes a step-by-step approach from building a data pipeline for a custom dataset to training and visualizing the performance of the model.

`predict.py` can be used for loading pre-trained models on the _Bacillaria_ dataset. This will auto-rotate the image in a way that cells will align to either a
horizontal or vertical axis. This task can be divided into three parts.
#### 1. Detect lines in the image
First, we detect edges in the Images. Here we used a canny edge detector for edge detection. By using edges we can find straight lines with the Hough transform method[1].
#### 2. Calculate the angle of rotation
The next step is to use detected lines for finding the angle of rotation. We find the slope of all the detected line and store in the array. The final angle of rotation
will be the mode of all the slopes. This can fail in some cases.

#### 3. Feed Rotated Image it in pre-trained model 
The final step is to rotate an image and feed it into the pre-trained model. The model used here is faster RCNN. We also have to re-rotate the image after predicting from
the model for output corresponding to input image size.


## How to run 
```bash
python predict.py --image image.jpg --model trained_model.pth
```

The output image will be generated in the same directory as an input image.

## Future Improvement

- [ ] Evaluating Performance of model in different backbone
- [ ] Annotating more data 
- [ ] Modify Faster RCNN for detection of oriented bounding box detection. [Reference Paper](https://arxiv.org/abs/1711.10398)
- [ ] Training and Evaluating performance on Mask R-CNN

## References
[1] [Lines Detection with Hough Transform](https://towardsdatascience.com/lines-detection-with-hough-transform-84020b3b1549)
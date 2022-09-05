# Devlog

This is a development log for answering if Bacillaria has smooth movement or not using visual tracking.

## Local installation

The project was install locally using 
`
torch                   1.12.1+cu113
detectron2              0.6
`

These links were helpful - [Torch installation](https://detectron2.readthedocs.io/en/latest/tutorials/install.html) and [Pytorch local installation](https://pytorch.org/get-started/locally/)



## 2022-08-28

I've installed the requirements to activate the Object detection and instance segmentation. 



| Explanation                               | Image                                                        |
| ----------------------------------------- | ------------------------------------------------------------ |
|                                           |                                                              |
|                                           |                                                              |
| I've used the tool of tracking in a video | ![image-20220828215750095](devlog.assets/image-20220828215750095.png) |



## 2022-08-29

| Exp                                                          | Img                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| I'm trying to harris corner detec the spots                  | ![image-20220829213227613](devlog.assets/image-20220829213227613.png) |
| This is a zoom out of the spots . It's from the right side.  | ![image-20220829213259745](devlog.assets/image-20220829213259745.png) |
| Measuring the pixels it seems like it's around 5-9 pixles.   |                                                              |
| Also with changes of parameters the corners detection didn't seem good. |                                                              |
|                                                              |                                                              |

# 2022-09-04

I've tried the optical flow tracking and it seems to do a much better job. 

I've just taken the standard code from [opencv optical flow](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) page and it worked first time!

| Exp                                                          | Image                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| The diatoms from the tracking video                          | ![image-20220904185543850](devlog.assets/image-20220904185543850.png) |
| We can see straight lines of tracking points on the diatoms. |                                                              |
| I'll chat about it with devoworm panel.                      |                                                              |
| Code is in [script](Smooth-Movement/opt_flow_track.py)       |                                                              |




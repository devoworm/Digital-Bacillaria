import numpy as np
import cv2 as cv

VID_PATH = "Smooth-Movement/data/40x_100fps_b5.avi"
TRACK_VIDEO = "Smooth-Movement/data/40x_100fps_b5_track.avi"

def track_manager(
    vid_path: str,
    output_track_video_path: str,
):
    cap = cv.VideoCapture(vid_path)
    video_frame_rate = int(cap.get(cv.CAP_PROP_FPS))
    fourcc = cv.VideoWriter_fourcc(*"MJPG")
    writerInit = False
    # params for ShiTomasi corner detection
    feature_params = dict( maxCorners = 10,
                        qualityLevel = 0.3,
                        minDistance = 7,
                        blockSize = 7 )
    # Parameters for lucas kanade optical flow
    lk_params = dict( winSize  = (15, 15),
                    maxLevel = 2,
                    criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
    # Create some random colors
    color = np.random.randint(0, 255, (100, 3))
    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
    p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
    # Create a mask image for drawing purposes
    mask = np.zeros_like(old_frame)
    while(1):
        ret, frame = cap.read()
        if not ret:
            print('No frames grabbed!')
            break
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # calculate optical flow
        p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
        # Select good points
        if p1 is not None:
            good_new = p1[st==1]
            good_old = p0[st==1]
        # draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
            frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
        img = cv.add(frame, mask)
        if not writerInit:
            h,w,_ = img.shape
            out_vid = cv.VideoWriter(output_track_video_path, fourcc, video_frame_rate, (1280, 720))
            writerInit = True
        out_vid.write(img)
        cv.imshow('frame', img)
        k = cv.waitKey(int(1000/video_frame_rate)) & 0xfe
        if k == 26:
            break
        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)
    cv.destroyAllWindows()
    
    pass


if __name__ == '__main__':
    track_manager(VID_PATH, TRACK_VIDEO)
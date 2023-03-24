import cv2

# set input video file name
input_file = "input.mp4"

# set output video file name
output_file = "output.avi"

# open input video file
cap = cv2.VideoCapture(input_file)

# get input video properties
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# set output video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, frame_rate, (width, height))

# loop through input video frames
frame_no = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame_no += 1
        if frame_no % 4 == 0:  # skip 75% of frames
            out.write(frame)   # write frame to output video
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release resources
cap.release()
out.release()
cv2.destroyAllWindows()

import cv2
import sys

#비디오 파일 열기
cap = cv2.VideoCapture('video.mp4')

# 비디오 파일이 열리지 않은 경우
if not cap.isOpened():
    sys.exit('비디오 파일을 열 수 없습니다.')
    
# 비디오 파일 재생
fps = cap.get(cv2.CAP_PROP_FPS)
frames = []
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # 2초마다 한 번씩 프레임을 저장
    if frame_count % (fps*2) == 0:
        frames.append(frame)
    if len(frames) == 3:
        break
    frame_count += 1
cap.release()

# 세장의 이미지를 가로로 이어붙이기
result = cv2.hconcat(frames)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()







#print(cv2.__version__)

#img = cv2.imread('soccer.jpg')

#if img is None:
    #sys.exit('파일을 찾을 수 없습니다.')

## 이미지 그레이 스케일로 변환
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#이미지 크기 절반으로 축소 0.5배
#img_small = cv2.resize(gray, (0, 0), fx= 0.5, fy=0.5)

#cv2.imshow('Image', img)
#cv2.imshow('Gray Image', gray)
#cv2.imshow('Small Image', img_small)

#cv2.imwrite('gray.jpg', gray)
#cv2.imwrite('gray_samll.jpg', img_small)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

import cv2

# 동영상 파일 열기
cap = cv2.VideoCapture('video.mp4')

# 첫 번째 프레임을 읽고 배경으로 설정
ret, base_frame = cap.read()
if not ret:
    print("비디오를 읽을 수 없습니다.")
    cap.release()
    exit()

# 시퀀스 이미지 초기화
sequence_image = base_frame.copy()
gray_base = cv2.cvtColor(base_frame, cv2.COLOR_BGR2GRAY)

# 각 프레임을 하나씩 읽어가면서 처리
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % 15 == 0:  # 너무 많은 프레임을 합치지 않도록 간격을 둠
        # 현재 프레임을 그레이스케일로 변환
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 두 이미지 간의 차이 계산
        diff = cv2.absdiff(gray_base, gray_frame)
        
        # 차이가 있는 영역을 찾아서 임계값 처리
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        # 배경과 현재 프레임의 차이 영역을 활용하여 fg(포그라운드) 생성
        fg = cv2.bitwise_and(frame, frame, mask=thresh)

        # 시퀀스 이미지의 배경(bg) 업데이트
        bg = cv2.bitwise_and(sequence_image, sequence_image, mask=cv2.bitwise_not(thresh))

        # 모션 이미지 업데이트
        sequence_image = cv2.add(bg, fg)

# 최종 시퀀스 이미지 출력
cv2.imshow('Sequence Image', sequence_image)
cv2.imwrite('motion_output.jpg', sequence_image)

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt

# Đọc ảnh gốc và chuyển sang grayscale
img = cv2.imread("D:\\download\\avatar-anh-meo-cute-21.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Khởi tạo SIFT detector
sift = cv2.SIFT_create()

# Phát hiện keypoints và tính descriptor
keypoints, descriptors = sift.detectAndCompute(gray, None)
# In thông tin cơ bản
print(f'Số lượng keypoints phát hiện được: {len(keypoints)}')
print(f'Kích thước của descriptor: {descriptors.shape}')  # (N, 128)

# Vẽ keypoints lên ảnh
img_with_kp = cv2.drawKeypoints(img, keypoints, None,
                                flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Hiển thị ảnh với keypoints
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(img_with_kp, cv2.COLOR_BGR2RGB))
plt.title('Ảnh với các điểm SIFT keypoints')
plt.axis('off')
plt.show()

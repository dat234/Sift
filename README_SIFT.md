
# 📌 README - SIFT (Scale-Invariant Feature Transform)

## 🔍 Giới thiệu
SIFT (Scale-Invariant Feature Transform) là một thuật toán nổi tiếng trong lĩnh vực thị giác máy tính, được phát triển bởi David Lowe năm 2004. Mục tiêu của SIFT là phát hiện và mô tả các điểm đặc trưng (keypoints) trong ảnh sao cho chúng bất biến với:
- Thay đổi tỉ lệ (scale)
- Xoay (rotation)
- Thay đổi ánh sáng nhỏ và nhiễu

SIFT thường được ứng dụng trong:
- Ghép ảnh panorama (image stitching)
- Nhận dạng đối tượng (object recognition)
- Theo dõi chuyển động (tracking)
- Dựng lại ảnh 3D (3D reconstruction)

---

## ⚙️ Các bước chính của thuật toán SIFT

### 1. Tạo không gian đa tỉ lệ (Scale-space)
- Ảnh gốc được làm mờ bằng bộ lọc Gaussian với nhiều mức sigma khác nhau.
- Mỗi mức độ mờ tương ứng với một mức tỉ lệ (scale).
- Nhóm ảnh cùng độ phân giải thành một "Octave", sau đó giảm kích thước xuống 1/2 để tạo Octave tiếp theo.

### 2. Difference of Gaussian (DoG)
- Tính hiệu của hai ảnh Gaussian liên tiếp: `DoG = G(kσ) - G(σ)`.
- DoG giúp phát hiện những thay đổi mạnh (cạnh, góc) giữa các mức tỉ lệ.
- DoG xấp xỉ Laplacian of Gaussian nhưng nhẹ hơn về tính toán.

### 3. Phát hiện và tinh chỉnh keypoint
- Mỗi pixel trong ảnh DoG được so sánh với 26 điểm lân cận (3x3x3 không gian).
- Nếu là cực trị cục bộ → là keypoint tiềm năng.
- Loại bỏ điểm có độ tương phản thấp hoặc nằm trên biên (dựa trên đạo hàm và ma trận Hessian).
- Dùng nội suy Taylor để tìm vị trí và scale chính xác của keypoint.

### 4. Gán hướng cho keypoint (Orientation Assignment)
- Với mỗi keypoint, tính gradient magnitude và direction quanh vùng lân cận.
- Tạo histogram 36 hướng (mỗi bin 10 độ).
- Hướng nào phổ biến nhất → gán làm hướng chính.
- Nếu có hướng phụ nổi bật (> 80%) → tạo thêm keypoint phụ.

### 5. Mô tả keypoint (Descriptor)
- Lấy vùng 16x16 quanh keypoint, chia thành 4x4 ô (cell).
- Mỗi ô tạo histogram 8 hướng → 4x4x8 = **128 chiều**.
- Chuẩn hóa vector để tăng tính ổn định (L2-norm, cắt >0.2 nếu cần).

Kết quả: một vector 128 chiều đại diện cho vùng quanh mỗi keypoint.

---

## 📌 SIFT trong ghép ảnh (Image Stitching)

1. Phát hiện keypoint trong mỗi ảnh bằng SIFT.
2. Tính descriptor và so khớp (matching) giữa hai ảnh.
3. Dùng RANSAC để lọc điểm sai và tính ma trận biến đổi homography.
4. Dùng `cv2.warpPerspective()` để biến đổi ảnh và `cv2.stitcher()` để ghép.

---


## 📦 Kết luận
SIFT là một trong những thuật toán nền tảng cho xử lý ảnh và thị giác máy tính, mạnh mẽ trong việc phát hiện điểm đặc trưng bất biến với các thay đổi hình học. Dù hiện tại có nhiều thuật toán nhanh hơn (như ORB, AKAZE), SIFT vẫn là một lựa chọn ổn định và chất lượng cao.



---

## 🧠 Tài liệu tham khảo
- Lowe, D. G. (2004). Distinctive Image Features from Scale-Invariant Keypoints.
- OpenCV Documentation: https://docs.opencv.org
- https://www.analyticsvidhya.com/blog/2019/10/detailed-guide-powerful-sift-technique-image-matching-python/

# 01 - Hàm mất mát phổ biến trong deep learning

---

- [Người hướng dẫn] Trong học máy,

hàm mất là một hàm toán học

định lượng lỗi

hoặc sự khác biệt giữa các kết quả đầu ra dự đoán của một mô hình,

và các giá trị mục tiêu thực tế trong dữ liệu huấn luyện.

Trong học sâu, các hàm mất mát phục vụ

làm nền tảng cho việc huấn luyện mạng lưới thần kinh,

khi họ cung cấp phản hồi

hoặc lỗi cần thiết cho quá trình tối ưu hóa

để cập nhật các tham số của mô hình,

đó là trọng số và độ lệch.

Bằng cách giảm thiểu giá trị của hàm mất mát,

người mẫu học cách đưa ra dự đoán

ngày càng chính xác theo thời gian.

Việc lựa chọn một hàm mất mát thích hợp là rất quan trọng,

bởi vì nó ảnh hưởng trực tiếp đến cách người mẫu học hỏi

và thực hiện các nhiệm vụ cụ thể.

Hồi quy như vậy, phân loại nhị phân,

hoặc phân loại nhiều lớp.

Đối với các nhiệm vụ hồi quy

trong đó mục tiêu là dự đoán các giá trị liên tục,

sai số bình phương trung bình,

hoặc chức năng mất MSE là một lựa chọn phổ biến.

MSE tính trung bình của chênh lệch bình phương

giữa giá trị dự đoán và giá trị thực.

Về mặt toán học, nó được thể hiện như ở đây,

trong đó YI đại diện cho các giá trị thực

của biến phụ thuộc trong dữ liệu huấn luyện,

Y mũ I đại diện cho các giá trị tiên đoán

của biến phụ thuộc và N là số mẫu.

Bình phương sự khác biệt đảm bảo

rằng sự mất mát luôn luôn dương,

và phạt những lỗi lớn hơn nặng nề hơn.

Mặc dù MSE được sử dụng rộng rãi nhưng nó có thể nhạy cảm với các giá trị ngoại lệ,

vì độ lệch lớn góp phần không tương xứng

đến sự mất mát.

Một cách khác là sai số tuyệt đối trung bình, MAE,

tính trung bình của các khác biệt tuyệt đối

giữa giá trị dự đoán và giá trị thực.

MAE mạnh mẽ hơn đối với các ngoại lệ,

nhưng có thể hội tụ chậm hơn MSE trong quá trình huấn luyện.

Đối với các bài toán phân loại nhị phân,

trong đó đầu ra đại diện cho một trong hai lớp có thể,

ví dụ: không hoặc một,

hàm mất entropy chéo nhị phân thường được sử dụng.

Hàm mất mát này đo lường sự khác biệt

giữa các xác suất dự đoán,

và các nhãn nhị phân thực tế.

Về mặt toán học, nó được định nghĩa như ở đây,

trong đó YI là các nhãn nhị phân thực sự, bằng 0 hoặc một,

và Y hat I là xác suất dự đoán

của lớp tích cực.

Entropy chéo nhị phân khuyến khích một mô hình

để tạo ra xác suất gần bằng một

cho lớp dương và gần bằng 0

đối với lớp tiêu cực.

Hàm mất mát này đặc biệt phù hợp

cho các nhiệm vụ như phát hiện thư rác, chẩn đoán y tế,

hoặc phát hiện gian lận, trong đó kết quả đầu ra là xác suất

đúng hoặc sai, có hoặc không, hoặc một hoặc không.

Đối với các bài toán phân loại nhiều lớp,

trong đó mục tiêu là gán đầu vào cho một

của một số lớp có thể,

sự mất mát entropy chéo phân loại được sử dụng rộng rãi.

Tương tự như entropy chéo nhị phân,

hàm mất mát này so sánh xác suất dự đoán

phân phối trên tất cả các lớp với nhãn lớp thực tế.

Về mặt toán học, nó được định nghĩa như ở đây,

trong đó N là số lượng mẫu,

K là một số lớp,

YIJ là chỉ báo nhị phân cho biết mẫu tôi có thuộc về hay không

vào lớp J, và Y hat IJ là xác suất dự đoán

đối với mẫu tôi đang học Lớp J.

Entropy chéo phân loại đặc biệt hiệu quả

cho các nhiệm vụ như phân loại hình ảnh,

nơi mô hình dự đoán một lớp

của nhiều loại có thể.

Entropy chéo phân loại giả định rằng các giá trị

của biến phụ thuộc được mã hóa dưới dạng một vectơ mũ.

Tuy nhiên, trong trường hợp các giá trị này được mã hóa

dưới dạng số nguyên, một phiên bản đơn giản hóa

của entropy chéo phân loại,

được gọi là entropy chéo phân loại thưa thớt,

có thể được sử dụng thay thế.

Ngoài các hàm mất mát thường được sử dụng được giới thiệu

ở đây, các nhiệm vụ deep learning nâng cao thường yêu cầu

chức năng mất mát chuyên biệt phù hợp

trước những thách thức và mục tiêu riêng của họ.

Ví dụ: trong các nhiệm vụ phát hiện hoặc phân đoạn đối tượng,

giao điểm về mất liên minh hoặc mất xúc xắc được sử dụng

để đánh giá sự chồng chéo giữa dự đoán

và các hộp giới hạn sự thật hoặc mặt nạ.

Đối với các tác vụ theo trình tự như dịch máy,

mất chuỗi thường được sử dụng

để xử lý các dự đoán có độ dài thay đổi.

Việc lựa chọn hàm mất mát phù hợp là điều cần thiết để đảm bảo

rằng mô hình deep learning học hiệu quả

cho nhiệm vụ được giao.

Hàm mất mát đóng vai trò là động lực

để đào tạo mô hình, hướng dẫn quá trình tối ưu hóa

để giảm thiểu lỗi và tối đa hóa độ chính xác dự đoán.
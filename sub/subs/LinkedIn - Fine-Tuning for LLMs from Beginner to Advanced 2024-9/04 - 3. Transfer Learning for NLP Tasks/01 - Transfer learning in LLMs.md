# 01 - Chuyển tiếp học tập trong LLM

---

- Hãy cùng hòa mình vào thế giới hấp dẫn

của các kỹ thuật học máy,

tập trung vào việc học chuyển giao

và tinh chỉnh trong các mô hình ngôn ngữ lớn.

Chúng ta sẽ bắt đầu bằng cách giới thiệu những khái niệm này bằng một phép loại suy,

sau đó khám phá cách chúng được áp dụng trong AI,

và hiểu khi nào nên sử dụng từng phương pháp một cách hiệu quả.

Hãy tưởng tượng bạn là một đầu bếp đang cố gắng chế biến nhiều món ăn khác nhau.

Nếu bạn chuyển đến một nhà hàng mới,

bạn không cần phải học lại mọi thứ về nấu ăn.

Thay vào đó, bạn hãy điều chỉnh kỹ năng của mình để phù hợp với nhà bếp và thực đơn mới.

Sự thích ứng này tương tự như học chuyển giao,

trong đó mô hình được phát triển cho một nhiệm vụ được điều chỉnh

để xử lý một nhiệm vụ liên quan nhưng hơi khác một chút.

Ngược lại, hãy tưởng tượng một đầu bếp

người không chỉ chuyển đến nhà hàng mới,

mà còn học cách nấu một món ăn hoàn toàn mới.

Những điều này sẽ yêu cầu đào tạo chuyên sâu hơn

và thực hành tương tự như tinh chỉnh,

trong đó một mô hình hiện có được đào tạo rộng rãi về một mô hình mới,

dữ liệu thường khác nhau đáng kể.

Về mặt kỹ thuật, chuyển giao việc học trong bối cảnh

của AI liên quan đến việc lấy một mô hình

đã được đào tạo trước trên một tập dữ liệu lớn,

và điều chỉnh nó cho phù hợp với một nhiệm vụ chuyên biệt

chỉ với những sửa đổi nhỏ.

Điều này thường được thực hiện bằng cách thêm một thành phần mới

hoặc đi đến mô hình

được đào tạo đặc biệt về nhiệm vụ mới,

trong khi vẫn giữ nguyên hầu hết cấu trúc của mô hình khu vực.

Ví dụ, một mô hình ngôn ngữ được đào tạo trước

có thể có một lớp đầu ra mới để phân loại cảm xúc qua email,

nơi chỉ có lớp mới này học từ email,

trong khi phần còn lại của mô hình vẫn không thay đổi.

Tuy nhiên, việc tinh chỉnh bao gồm việc điều chỉnh toàn bộ mô hình

và một tập dữ liệu mới.

Ở đây, tất cả các trọng số và độ lệch trong mô hình

được cập nhật thông qua đào tạo thêm.

Cách tiếp cận này tốn nhiều tài nguyên hơn,

nhưng cần thiết khi có nhiệm vụ mới

khác biệt đáng kể so với những

nơi mô hình ban đầu được đào tạo.

Trong khi học chuyển giao có thể được ví như

để cập nhật nhanh khóa học dành cho đầu bếp,

tinh chỉnh giống như trải qua

lại toàn bộ chương trình học nấu ăn.

Tinh chỉnh mô hình cho một nhiệm vụ chuyên biệt

như phân tích văn bản pháp luật

có thể yêu cầu tính toán và dữ liệu đáng kể,

phản ánh chi phí cao hơn và thời gian phát triển dài hơn.

Lựa chọn giữa học chuyển tiếp

và tinh chỉnh phụ thuộc vào nhu cầu cụ thể của bạn.

Học chuyển tiếp là lý tưởng

khi các nhiệm vụ tương tự nhau,

và nguồn lực bị hạn chế vì nó cho phép

để thích ứng nhanh hơn với ít dữ liệu hơn.

Tinh chỉnh là tốt nhất khi các nhiệm vụ rất khác nhau

hoặc khi độ chính xác tối đa là rất quan trọng,

mặc dù chi phí cao hơn và khung thời gian dài hơn.

Trong cuộc khám phá này, chúng tôi đã thấy cách học chuyển giao

và tinh chỉnh đóng vai trò then chốt

trong việc triển khai LMS một cách hiệu quả.

Bằng cách hiểu rõ những kỹ thuật này,

bạn có thể lập chiến lược phát triển mô hình của mình tốt hơn

để đáp ứng nhu cầu cụ thể của bạn, đảm bảo hiệu suất tối ưu

và quản lý tài nguyên.
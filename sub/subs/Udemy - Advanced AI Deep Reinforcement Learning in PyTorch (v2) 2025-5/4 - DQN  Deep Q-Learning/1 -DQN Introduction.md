# 1 -DQN Dịch giới thiệu

---

Trong video này, chúng tôi sẽ giới thiệu phần tiếp theo của khóa học về Q sâu

học tập. Về cơ bản, chúng tôi đã đề cập đến hầu hết nền tảng trong các phần trước,

đặc biệt là đoạn mã giới thiệu cho bạn cấu trúc cơ bản của học tăng cường

tập lệnh mà chúng tôi sẽ sử dụng trong khóa học này. Vì vậy phần này sẽ khá ngắn,

Tại thời điểm này, tất cả những gì chúng ta phải làm là giới thiệu các thủ thuật DQN để tạo nên DQN.

Cụ thể, chúng ta sẽ xem xét bộ đệm phát lại, đây là một cơ chế lưu trạng thái

các phần và phần thưởng mà chúng ta gặp phải, đồng thời sử dụng chúng để học thêm. Chúng ta sẽ nhìn vào mục tiêu

mạng và việc có hai mạng thần kinh sẽ tốt hơn việc chỉ có một mạng như thế nào. Chúng ta cũng sẽ xem xét

về cách cập nhật Epsilon theo thời gian để chúng tôi khám phá thêm ngay từ đầu và

ít hơn ở cuối, điều này sẽ giúp đặc vụ đào tạo nhanh hơn. Khi chúng ta đã xem hết tất cả các thủ thuật của DQN,

chúng ta sẽ chuyển sang triển khai DQN và Python.
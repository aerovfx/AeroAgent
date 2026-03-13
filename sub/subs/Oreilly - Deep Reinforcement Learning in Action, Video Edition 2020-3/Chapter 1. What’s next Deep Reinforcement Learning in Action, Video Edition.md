# Chương 1. Học tập tăng cường sâu tiếp theo là gì, Phiên bản video được dịch

---

Phần 1.8, tiếp theo là gì?

Trong chương tiếp theo, chúng ta sẽ đi sâu vào nội dung thực sự của RL, bao gồm nhiều

khái niệm cốt lõi, chẳng hạn như sự đánh đổi giữa thăm dò và khai thác, quyết định của Markov

quy trình, chức năng giá trị và chính sách.

Những điều khoản này sẽ sớm có ý nghĩa.

Nhưng trước tiên, ở phần đầu của chương tiếp theo, chúng tôi sẽ giới thiệu một số phương pháp giảng dạy

chúng tôi sẽ sử dụng xuyên suốt cuốn sách này.

Phần còn lại của cuốn sách sẽ đề cập đến các thuật toán DRL cốt lõi mà phần lớn nghiên cứu mới nhất được xây dựng

bắt đầu với các mạng Q sâu, tiếp theo là các phương pháp tiếp cận gradient chính sách và sau đó là dựa trên mô hình

thuật toán.

Chúng tôi chủ yếu sẽ sử dụng phòng tập thể dục của OpenAI, đã đề cập trước đó, để đào tạo các thuật toán của chúng tôi

hiểu động lực học phi tuyến, điều khiển robot và chơi trò chơi, hình 1.15.

Sau 1.15, mô tả bàn cờ vây, một trò chơi cổ xưa của Trung Quốc mà Google DeepMind đã sử dụng làm

một nền tảng thử nghiệm cho thuật toán học tăng cường AlphaGo của nó.

Kỳ thủ cờ vây chuyên nghiệp Lee Sedol chỉ thắng được 1/5 ván, đánh dấu bước ngoặt

để học tăng cường, vì Go từ lâu đã được cho là không thấm vào loại thuật toán

lý luận rằng cờ vua phải tuân theo.

Nguồn, liên kết này.

Trong mỗi chương, chúng ta sẽ mở đầu bằng một vấn đề hoặc dự án lớn mà chúng ta sẽ sử dụng để minh họa.

những khái niệm và kỹ năng quan trọng của chương đó.

Khi mỗi chương tiến triển, chúng ta có thể thêm độ phức tạp hoặc sắc thái cho vấn đề bắt đầu để đi sâu hơn.

vào một số nguyên tắc.

Ví dụ, trong chương 2 chúng ta sẽ bắt đầu với vấn đề tối đa hóa phần thưởng tại sòng bạc.

máy đánh bạc và bằng cách giải quyết vấn đề đó, chúng tôi sẽ đề cập đến hầu hết các nền tảng của RL.

Sau này, chúng tôi sẽ thêm một số vấn đề phức tạp vào vấn đề đó và thay đổi cài đặt từ sòng bạc thành doanh nghiệp

cần tối đa hóa số lần nhấp vào quảng cáo, điều này sẽ cho phép chúng tôi hoàn thiện thêm một số

các khái niệm.

Mặc dù cuốn sách này dành cho những người đã có kinh nghiệm về kiến thức cơ bản về deep learning,

chúng tôi hy vọng không chỉ dạy cho bạn các kỹ thuật RL thú vị và hữu ích mà còn trau dồi kiến thức chuyên sâu của bạn

kỹ năng học tập.

Để giải quyết một số dự án khó khăn hơn, chúng ta cần sử dụng một số

những tiến bộ mới nhất trong học sâu, chẳng hạn như mạng lưới đối thủ tổng quát, phương pháp tiến hóa,

siêu học tập và học chuyển giao.

Một lần nữa, tất cả điều này đều phù hợp với phương thức giảng dạy tập trung vào kỹ năng của chúng tôi, vì vậy chi tiết của những điều này

tiến bộ không phải là điều quan trọng.
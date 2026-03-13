# Chương 2. Tóm tắt Học tập tăng cường sâu trong thực tế, Phiên bản video

---

Bản tóm tắt. Không gian trạng thái là tập hợp tất cả các trạng thái có thể có của một hệ thống. Trong cờ vua, điều này

sẽ là tập hợp tất cả các cấu hình bảng hợp lệ. Một hành động là một chức năng ánh xạ một trạng thái

S sang trạng thái mới S'. Một hành động có thể mang tính ngẫu nhiên, sao cho nó ánh xạ trạng thái S theo xác suất

sang trạng thái mới S'. Có thể có một số phân phối xác suất trên tập hợp các khả năng mới

trạng thái mà từ đó cái được chọn. Không gian hành động là tập hợp tất cả các hành động có thể xảy ra đối với

một trạng thái cụ thể Môi trường là nguồn gốc của trạng thái, hành động và phần thưởng. Nếu

chúng tôi đang xây dựng thuật toán RL để chơi trò chơi, khi đó trò chơi chính là môi trường. Một người mẫu

của một môi trường là sự gần đúng của không gian trạng thái, không gian hành động và chuyển tiếp

xác suất. Phần thưởng là tín hiệu được tạo ra bởi môi trường

cho thấy sự thành công tương đối của việc thực hiện một hành động trong một trạng thái nhất định. Một phần thưởng được mong đợi

là một khái niệm thống kê đề cập một cách không chính thức đến giá trị trung bình dài hạn của một số biến ngẫu nhiên

biến X, trong trường hợp của chúng ta là phần thưởng, biểu thị giá trị kỳ vọng của X. Ví dụ: trong N-armed

trường hợp kẻ cướp, phần thưởng mong đợi cho hành động A là phần thưởng trung bình dài hạn của việc thực hiện

mỗi hành động N. Nếu chúng ta biết phân bố xác suất của các hành động A thì chúng ta

có thể tính toán giá trị chính xác của phần thưởng mong đợi cho một trò chơi có N lượt chơi như thế này, trong đó

N là số lần chơi của trò chơi, P(i) là xác suất của hành động A(i),

và R đề cập đến phần thưởng tối đa có thể. Một tác nhân là một thuật toán RL học cách

hành xử tối ưu trong một môi trường nhất định. Các tác nhân thường được triển khai như một mạng lưới thần kinh sâu

mạng. Mục tiêu của đại lý là tối đa hóa phần thưởng mong đợi hoặc tương đương để điều hướng

lên trạng thái có giá trị cao nhất. Chính sách là một chiến lược cụ thể. chính thức,

đó là một chức năng chấp nhận một trạng thái và tạo ra một hành động để thực hiện hoặc tạo ra

một phân bố xác suất trên không gian hành động, cho trước trạng thái. Một chính sách chung là

chiến lược tham lam epsilon, trong đó với xác suất epsilon chúng ta thực hiện một hành động ngẫu nhiên trong hành động

không gian và với xác suất epsilon trừ đi một, chúng ta chọn hành động tốt nhất mà chúng ta biết

cho đến nay. Nói chung, hàm giá trị là bất kỳ hàm nào

trả về phần thưởng mong đợi dựa trên một số dữ liệu liên quan. Nếu không có ngữ cảnh bổ sung, nó thường

đề cập đến hàm giá trị trạng thái, là hàm chấp nhận trạng thái và trả về

phần thưởng mong đợi khi bắt đầu ở trạng thái đó và hành động theo một chính sách nào đó. Q

giá trị là phần thưởng mong đợi cho một cặp hành động trạng thái và hàm Q là hàm

tạo ra các giá trị Q khi được cung cấp một cặp trạng thái-hành động.

Quá trình ra quyết định Markov là một quá trình ra quyết định mà qua đó có thể đưa ra

quyết định tốt nhất mà không cần tham khảo lịch sử của các trạng thái trước đó.
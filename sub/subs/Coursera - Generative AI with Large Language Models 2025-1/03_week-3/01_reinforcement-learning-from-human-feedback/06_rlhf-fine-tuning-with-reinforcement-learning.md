# 06 rlhf-tinh chỉnh-với-tăng cường-học tập

---

Hãy mang mọi thứ lại với nhau,

và xem bạn sẽ làm thế nào

sử dụng mô hình khen thưởng trong

sự gia cố

quá trình học tập

để cập nhật trọng số LLM,

và tạo ra một con người

mô hình liên kết.

Hãy nhớ rằng, bạn muốn

bắt đầu với một mô hình

đã có thành tích tốt rồi

về nhiệm vụ mà bạn quan tâm.

Bạn sẽ làm việc để sắp xếp một

hướng dẫn tìm thấy bạn và LLM.

Đầu tiên, bạn sẽ vượt qua lời nhắc

từ tập dữ liệu nhắc nhở của bạn.

Trong trường hợp này, một con chó là

để hướng dẫn LLM,

sau đó tạo ra

sự hoàn thành,

trong trường hợp này là một con vật có lông.

Tiếp theo, bạn gửi phần hoàn thành này,

và lời nhắc ban đầu để

mô hình khen thưởng như

cặp hoàn thành nhanh chóng.

Mô hình khen thưởng

đánh giá cặp

dựa trên phản hồi của con người

nó đã được đào tạo về,

và trả về giá trị phần thưởng.

Giá trị cao hơn như vậy

bằng 0,24 như hình

ở đây đại diện cho nhiều hơn

phản ứng phù hợp.

Một phản ứng ít phù hợp hơn

sẽ nhận được giá trị thấp hơn,

chẳng hạn như âm 0,53.

Sau đó bạn sẽ vượt qua

giá trị phần thưởng này

cho cặp hoàn thành buổi vũ hội

sự gia cố

thuật toán học tập

cập nhật trọng số của LLM,

và di chuyển nó về phía

tạo ra nhiều hơn

thẳng hàng, cao hơn

trả lời khen thưởng.

Hãy gọi đây là

phiên bản trung gian của

mô hình RL đã cập nhật LLM.

Những chuỗi bước này cùng nhau

tạo thành một lần lặp duy nhất

của quá trình RLHF.

Những lần lặp này tiếp tục

cho một số lượng sử thi nhất định,

tương tự như khác

các loại tinh chỉnh.

Ở đây bạn có thể thấy rằng

hoàn thành được tạo ra bởi

LLM cập nhật RL nhận được

điểm thưởng cao hơn,

chỉ ra rằng

cập nhật về trọng lượng

đã dẫn đến nhiều hơn

hoàn thiện phù hợp.

Nếu quá trình này hoạt động tốt,

bạn sẽ thấy phần thưởng được cải thiện

sau mỗi lần lặp

như người mẫu

tạo ra văn bản đó là

ngày càng phù hợp

với sở thích của con người.

Bạn sẽ tiếp tục lặp lại điều này

xử lý cho đến khi mô hình của bạn

được căn chỉnh dựa trên một số

tiêu chí đánh giá.

Ví dụ như đạt

một giá trị ngưỡng

vì sự hữu ích mà bạn đã xác định.

Bạn cũng có thể định nghĩa một

số bước tối đa,

ví dụ: 20.000 là

tiêu chí dừng

Lúc này, hãy tham khảo

mô hình được tinh chỉnh như

LLM phù hợp với con người.

Một chi tiết chúng tôi chưa có

thảo luận vẫn chưa

bản chất chính xác của

thuật toán học tăng cường.

Đây là thuật toán

cái đó lấy đầu ra

của mô hình khen thưởng và sử dụng nó

để cập nhật LLM

trọng lượng mô hình như vậy

rằng điểm thưởng

tăng theo thời gian.

Có một số khác nhau

các thuật toán mà bạn có thể

sử dụng cho phần này của

quá trình RLHF

Một lựa chọn phổ biến là gần

tối ưu hóa chính sách

hoặc gọi tắt là PPO.

PPO đẹp quá

thuật toán phức tạp,

và bạn không cần phải

làm quen với tất cả

của các chi tiết được

có khả năng sử dụng nó.

Tuy nhiên, nó có thể

một thuật toán phức tạp để

thực hiện và hiểu biết

hoạt động bên trong của nó trong

chi tiết hơn có thể giúp bạn

khắc phục sự cố nếu bạn đang gặp phải

vấn đề làm cho nó hoạt động.

Để giải thích cách PPO

thuật toán hoạt động chi tiết hơn,

Tôi đã mời đồng nghiệp AWS của mình,

Ek để giúp bạn tìm hiểu sâu hơn

về các chi tiết kỹ thuật.

Video tiếp theo này là tùy chọn

và bạn nên cảm thấy

có thể bỏ qua nó,

và chuyển sang

video hack phần thưởng.

Bạn sẽ không cần

thông tin ở đây để

hoàn thành các câu đố

hoặc phòng thí nghiệm của tuần này.

Tuy nhiên, tôi khuyến khích

bạn kiểm tra

các chi tiết khi RLHF đang trở thành

ngày càng quan trọng

để đảm bảo rằng

LLM hoạt động một cách an toàn và

cách phù hợp trong việc triển khai.
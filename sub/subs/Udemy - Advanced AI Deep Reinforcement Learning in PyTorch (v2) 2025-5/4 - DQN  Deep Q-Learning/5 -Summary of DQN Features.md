# 5 -Tóm tắt các tính năng của DQN đã được dịch

---

Vì vậy, trong các bài giảng trước, chúng ta đã khám phá một số thành phần quan trọng của mạng DeepQ

sẽ ổn định và cải thiện việc học tập và học tập củng cố.

Tóm lại, chúng ta sẽ xem xét bốn tính năng chính, epsilon phân rã tuyến tính, bộ đệm phát lại,

mạng mục tiêu và đào tạo từng bước, đồng thời thảo luận lý do tại sao mỗi bước lại cần thiết cho việc đào tạo

tác nhân học tăng cường sâu một cách hiệu quả.

Vì vậy, quá trình khám phá tham lam của epsilon và epsilon xác định tần suất các tác nhân chọn ngẫu nhiên

hành động chứ không phải là hành động tham lam nhằm tối đa hóa giá trị Q.

Ban đầu, epsilon cao khuyến khích sự khám phá, trong khi epsilon thấp hơn cho phép khai thác nhiều hơn

của các chính sách đã học.

Vậy tại sao điều này lại hữu ích?

1.

Nó ngăn chặn sự hội tụ sớm.

Epsilon ban đầu cao đảm bảo rằng tác nhân khám phá môi trường đầy đủ, tránh

bị mắc kẹt trong các chính sách chưa tối ưu.

2.

Nó cân bằng giữa thăm dò và khai thác.

Bằng cách phân rã tuyến tính epsilon theo thời gian, tác nhân chuyển tiếp một cách suôn sẻ, từ việc khám phá

chiến lược mới để tận dụng những gì đã học.

Trong 3.

Nó ngăn chặn sự ngẫu nhiên quá mức trong quá trình đào tạo muộn.

Nếu epsilon không đổi, tác nhân có thể tiếp tục thực hiện các hành động ngẫu nhiên không cần thiết, thậm chí

sau khi học được một chính sách tối ưu.

OK, bây giờ hãy xem lại bộ đệm phát lại.

Bộ đệm phát lại lưu trữ các trải nghiệm trong quá khứ và cho phép tác nhân đào tạo theo các đợt nhỏ,

được lấy mẫu ngẫu nhiên từ bộ đệm này.

Thay vì chỉ sử dụng quá trình chuyển đổi gần đây nhất, DQN thu thập một tập hợp kinh nghiệm đa dạng trong quá khứ

trước khi bắt đầu đào tạo.

Vậy tại sao điều này lại hữu ích?

Thứ nhất, nó phá vỡ mối tương quan tuần tự.

Việc đào tạo trên các mẫu ngẫu nhiên thay vì chuyển đổi liên tiếp sẽ ngăn ngừa việc trang bị quá mức cho các mẫu gần đây

kinh nghiệm và cải thiện sự ổn định.

2.

Nó cải thiện hiệu quả mẫu.

Giá được sử dụng nhiều lần, giảm số lượng tương tác cần thiết với môi trường.

Và 3.

Nó ổn định các bản cập nhật.

Sử dụng một đợt nhỏ thay vì một lần chuyển đổi đơn lẻ sẽ làm giảm sự khác biệt trong cập nhật độ dốc, dẫn đến

để việc học suôn sẻ hơn.

Được rồi, bây giờ hãy xem lại mạng mục tiêu.

Vì vậy DQN duy trì hai mạng xếp hàng riêng biệt.

Vì vậy, mạng trực tuyến học và cập nhật trong quá trình đào tạo, trong khi mạng mục tiêu

một bản sao bị trì hoãn của mạng trực tuyến được cập nhật định kỳ.

Mục tiêu học hàng đợi được tính toán bằng cách sử dụng mạng mục tiêu.

Vậy tại sao điều này lại hữu ích?

Thứ nhất, nó làm giảm tính ổn định.

Nếu không có mạng mục tiêu, các giá trị hàng đợi có thể dao động dữ dội, dẫn đến sự phân kỳ.

2.

Nó ổn định việc học tập.

Bằng cách giữ cố định mạng mục tiêu trong vài bước trước khi cập nhật, quá trình học

tránh những thay đổi mạnh mẽ trong ước tính giá trị.

Và 3.

Nó giảm thiểu sự thiên vị đánh giá quá cao.

Mạng mục tiêu cung cấp tham chiếu ổn định hơn cho các cập nhật giá trị hàng đợi.

Giảm nguy cơ đánh giá quá cao các giá trị hành động.

Vì vậy, bây giờ hãy xem lại ý tưởng rằng chúng tôi huấn luyện mô hình sau mỗi vài bước chúng tôi thực hiện

môi trường.

Vì vậy, thay vì cập nhật mạng hàng đợi sau mỗi lần tương tác với môi trường, DQN

huấn luyện cứ sau vài bước bằng cách sử dụng một đợt nhỏ từ bộ đệm phát lại.

Vậy tại sao điều này lại hữu ích?

Thứ nhất, nó cải thiện hiệu quả tính toán.

Việc tạo ra mỗi bước đều tốn kém về mặt tính toán.

Cập nhật hàng loạt cứ sau vài bước sẽ tạo ra sự cân bằng giữa hiệu quả và hiệu quả đã học được.

Thứ hai, nó làm mịn các bản cập nhật độ dốc.

Thay vì cập nhật các chuyển đổi liên tiếp có mối tương quan cao, cập nhật định kỳ với các đợt nhỏ

giúp việc học tập ổn định hơn.

Và thứ ba, nó có nhiệm vụ tín dụng tốt hơn.

Đào tạo quá thường xuyên có thể khiến nhân viên phản ứng quá mức với các phần thưởng ngắn hạn, trong khi

giãn cách các bản cập nhật cho phép học tập lâu dài tốt hơn.

Vì vậy, mỗi tính năng này, tuyến tính dẫn đến khóa epsilon, bộ đệm phát lại, mạng đích,

và đào tạo từng bước.

Đóng một vai trò quan trọng trong việc biến DQN trở thành một thuật toán học tăng cường sâu mạnh mẽ và hiệu quả.

Họ cùng nhau quản lý hoạt động khám phá, ổn định quá trình học tập, nâng cao hiệu quả lấy mẫu và ngăn ngừa

sự khác biệt thảm khốc.

Hiểu và điều chỉnh chính xác các thành phần này là điều cần thiết để đào tạo thành công ở cấp độ sâu

tác nhân học tăng cường.
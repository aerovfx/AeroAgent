# 02 - Các loại mô hình deep learning

---

- [Người trình bày] Có nhiều loại

của mạng lưới thần kinh sâu,

mỗi cái được thiết kế để giải quyết các loại vấn đề khác nhau.

Chúng ta hãy đi qua một vài trong số họ.

Một trong những mạng lưới thần kinh sâu cơ bản nhất

là một mạng lưới thần kinh tiếp nối sâu,

còn được gọi là mạng được kết nối đầy đủ.

Trong loại mạng này,

thông tin chảy theo một hướng duy nhất,

từ lớp đầu vào đến lớp đầu ra

không có bất kỳ vòng lặp hoặc chu kỳ nào.

Các mạng này rất phù hợp cho các nhiệm vụ

nơi các mối quan hệ trong dữ liệu

tương đối đơn giản,

chẳng hạn như các vấn đề phân loại cơ bản hoặc hồi quy.

Tuy nhiên, họ thường phải đối mặt với những thách thức

khi xử lý các mẫu dữ liệu phức tạp hơn

vì chúng thiếu cơ chế để nắm bắt thời gian

hoặc sự phụ thuộc tuần tự.

Đối với các vấn đề liên quan đến dữ liệu hình ảnh,

mạng lưới thần kinh tích chập hoặc CNN thì phù hợp hơn.

CNN chuyên dụng

trong việc xử lý các cấu trúc dữ liệu dạng lưới, chẳng hạn như hình ảnh,

bằng cách tự động phát hiện các mẫu phân cấp

như các cạnh, kết cấu và đối tượng.

Các mạng này sử dụng các lớp tích chập

áp dụng các bộ lọc trên dữ liệu đầu vào

để nắm bắt các mối quan hệ không gian,

khiến chúng trở nên lý tưởng cho các nhiệm vụ như phân loại hình ảnh,

phát hiện đối tượng và các lĩnh vực khác của thị giác máy tính.

Khi làm việc với dữ liệu tuần tự,

chẳng hạn như dữ liệu chuỗi thời gian hoặc ngôn ngữ,

mạng lưới thần kinh tái phát, RNN,

và các biến thể của chúng,

như mạng bộ nhớ ngắn hạn dài, LSTM,

hoặc các đơn vị định kỳ có kiểm soát, GRU,

có hiệu quả cao.

RNN được thiết kế đặc biệt để xử lý các chuỗi

bằng cách duy trì bộ nhớ của các đầu vào trước đó

thông qua các kết nối phản hồi.

Khả năng nắm bắt các hành vi phụ thuộc vào thời gian

làm cho RNN trở nên mạnh mẽ cho các nhiệm vụ như dịch ngôn ngữ,

nhận dạng giọng nói và dự đoán giá cổ phiếu trong tương lai.

LSTM và GRU xây dựng trên kiến trúc RNN truyền thống

bằng cách giải quyết vấn đề phụ thuộc lâu dài

nơi thông tin trước đó trong một chuỗi

có thể ảnh hưởng đáng kể đến những dự đoán sau này.

Máy biến áp đại diện cho một sự phát triển gần đây hơn

trong việc xử lý dữ liệu tuần tự.

Trong khi RNN và các biến thể của chúng xử lý dữ liệu

từng bước một,

máy biến áp khắc phục hạn chế này

bằng cách xử lý đồng thời toàn bộ chuỗi

sử dụng một cơ chế gọi là tự chú ý.

Điều này cho phép máy biến áp nắm bắt được mối quan hệ

giữa tất cả các phần tử của một chuỗi cùng một lúc

thay vì dựa vào trí nhớ của các bước trước đó.

Máy biến áp tạo thành xương sống kiến trúc

đằng sau những mô hình AI sáng tạo mới nhất đang được sử dụng ngày nay,

chẳng hạn như ChatGPT và Claude.

Mạng đối thủ sáng tạo, GAN,

là một loại mạng lưới thần kinh sâu khác

được sử dụng cho các nhiệm vụ sáng tạo.

GAN bao gồm hai mạng,

máy tạo và máy phân biệt,

đó cạnh tranh với nhau

trong quá trình cùng nhau cải thiện.

GAN đã rất thành công trong các nhiệm vụ

chẳng hạn như tạo ra hình ảnh thực tế,

tăng cường độ phân giải hình ảnh,

và thậm chí tạo ra tác phẩm nghệ thuật hoặc âm nhạc.

Các mạng này có khả năng học cách tạo ra dữ liệu

gần như không thể phân biệt được với dữ liệu trong thế giới thực.

Đối với các kịch bản phức tạp hơn,

chẳng hạn như ô tô tự lái, robot và lối chơi trong AI,

học tăng cường sâu hoặc DRL kết hợp học sâu

với việc học tăng cường

nơi các tác nhân học cách thực hiện hành động trong môi trường

để tối đa hóa một số khái niệm về phần thưởng tích lũy.

Trong bối cảnh này, mạng lưới thần kinh sâu hoạt động như những gì đã biết

như các hàm xấp xỉ,

giúp các đại lý đưa ra quyết định dựa trên dữ liệu đầu vào phức tạp,

chẳng hạn như quan sát trực quan hoặc đọc cảm biến.

Học sâu đã biến đổi nhiều ngành công nghiệp

bằng cách cung cấp các mô hình có khả năng

tự động học các biểu diễn phức tạp từ dữ liệu,

xử lý lượng thông tin khổng lồ,

và đạt được độ chính xác cao

và những nhiệm vụ từng được coi là vượt quá tầm với

của các kỹ thuật học máy truyền thống.

Những tiến bộ liên tục của nó tiếp tục thúc đẩy sự đổi mới

trong trí tuệ nhân tạo và học máy,

tạo điều kiện cho những khả năng mới

trong công nghệ, khoa học và đời sống hàng ngày.
# 05 - Những thách thức với deep learning

---

- [Giảng viên] Deep learning chắc chắn đã trở thành

nền tảng của đổi mới công nghệ,

mang lại những đột phá trong các lĩnh vực như thị giác máy tính,

xử lý ngôn ngữ tự nhiên và chăm sóc sức khỏe.

Tuy nhiên, bên cạnh những thành công của nó,

học sâu phải đối mặt với những thách thức đáng kể

điều đó hạn chế khả năng ứng dụng và hiệu quả rộng rãi hơn của ông.

Hiểu những thách thức này

và khám phá các giải pháp tiềm năng là rất quan trọng

để thúc đẩy công nghệ học sâu

và làm cho nó dễ tiếp cận và minh bạch hơn.

Một trong những thách thức chính của học sâu

là sự phụ thuộc của nó vào lượng dữ liệu khổng lồ.

Để thực hiện tốt,

mô hình học sâu yêu cầu bộ dữ liệu đào tạo mở rộng,

đặc biệt là khi giải quyết các nhiệm vụ phức tạp,

như nhận dạng hình ảnh

hoặc hiểu ngôn ngữ tự nhiên.

Điều này là do các mô hình này

với hàng triệu hoặc thậm chí hàng tỷ thông số

cần dữ liệu dồi dào để tìm hiểu

và khái quát hóa một cách hiệu quả.

Sự cần thiết của bộ dữ liệu được dán nhãn chất lượng cao

cũng có thể đặt ra một rào cản đáng kể cho việc học sâu.

Ví dụ: đào tạo mô hình nhận dạng khuôn mặt

có thể yêu cầu hàng triệu hình ảnh có chú thích,

trong khi dữ liệu hình ảnh y tế cần có sự chú thích của chuyên gia,

thêm các ràng buộc về chi phí và thời gian.

Một sự phức tạp khác phát sinh khi giải quyết tình trạng khan hiếm dữ liệu

hoặc các tập dữ liệu mất cân bằng,

có thể dẫn đến hiệu suất mô hình sai lệch.

Khi một lớp dữ liệu thống trị tập huấn luyện,

mô hình có thể quá phù hợp,

thiên về lớp đó và không có khả năng khái quát hóa tốt.

Sự mất cân bằng này có thể có những hậu quả nghiêm trọng.

Ví dụ: hệ thống nhận dạng khuôn mặt

đã cho thấy tỷ lệ lỗi cao hơn

dành cho những người có tông màu da tối hơn

khi được huấn luyện trên các tập dữ liệu không đa dạng.

Một phương pháp hiệu quả để giải quyết nhu cầu

đối với dữ liệu đào tạo mở rộng là tăng cường dữ liệu.

Quá trình này liên quan đến việc tạo các phiên bản sửa đổi

của dữ liệu hiện có bằng cách áp dụng các phép biến đổi,

chẳng hạn như xoay, lật, cắt hoặc thay đổi màu sắc.

Cách tiếp cận này giúp mở rộng tập dữ liệu một cách giả tạo,

làm cho mô hình mạnh mẽ hơn

và tốt hơn trong việc khái quát hóa

mà không cần dữ liệu hoàn toàn mới.

Để giảm bớt gánh nặng thu thập dữ liệu,

học chuyển giao cũng có thể được sử dụng.

Kỹ thuật này sử dụng các mô hình được đào tạo trước

đã học được những đặc điểm chung

từ một tập dữ liệu lớn có liên quan.

Những mô hình này sau đó có thể được tinh chỉnh

trên các tập dữ liệu nhỏ hơn, có nhiệm vụ cụ thể,

cho phép các ứng dụng học sâu hoạt động hiệu quả,

ngay cả với dữ liệu hạn chế.

Xây dựng bộ dữ liệu đa dạng và mang tính đại diện là rất quan trọng

để ngăn ngừa các kết quả đầu ra của mô hình bị sai lệch.

Cần nỗ lực tập trung vào việc tìm nguồn cung ứng dữ liệu

bao gồm nhân khẩu học đa dạng,

địa lý và điều kiện

để thúc đẩy kết quả công bằng và không thiên vị trong các mô hình.

Ngoài ra, việc hợp tác với các chuyên gia

để ghi nhãn dữ liệu theo miền cụ thể có thể đảm bảo chất lượng cao,

dữ liệu đào tạo chính xác.

Chi phí tính toán của việc đào tạo các mô hình deep learning

là một thách thức ghê gớm khác.

Đào tạo mạng sâu, đặc biệt cho các nhiệm vụ phức tạp,

đòi hỏi sức mạnh xử lý lớn và thời gian.

Quá trình này bao gồm nhiều hoạt động ma trận

và với hàng triệu thông số cần cập nhật.

Gánh nặng tính toán là đáng kể.

Phần cứng chuyên dụng, như GPU và TPU,

có thể đẩy nhanh quá trình này.

Nhưng ngay cả như vậy, việc đào tạo vẫn có thể mất vài ngày hoặc vài tuần.

Mức tiêu thụ năng lượng cần thiết

để đào tạo mô hình quy mô lớn

làm trầm trọng thêm thách thức này,

góp phần tạo ra lượng khí thải carbon đáng kể.

Nhu cầu nguồn lực cao có nghĩa là

rằng chỉ những tổ chức được tài trợ tốt

và các công ty công nghệ lớn có thể đủ khả năng

để tiến hành nghiên cứu tiên tiến,

hạn chế dân chủ hóa AI.

Các kỹ thuật như cắt tỉa mô hình

có thể giảm đáng kể kích thước của các mô hình học sâu.

Cắt tỉa liên quan đến việc loại bỏ các tham số ít tác động hơn

từ mô hình,

làm giảm tải tính toán

trong khi vẫn duy trì độ chính xác.

Sự phát triển của kiến trúc nhẹ,

như EffientNet,

và phương sai máy biến áp đã cho thấy

rằng có thể đạt được hiệu suất cao

với ít tham số hơn.

Những mô hình này được thiết kế để cân bằng độ chính xác

và yêu cầu tính toán

làm cho chúng dễ tiếp cận hơn đối với các tổ chức nhỏ hơn

và các ứng dụng có nguồn lực hạn chế.

Tận dụng nền tảng dựa trên đám mây

để đào tạo phân tán

giúp khắc phục những hạn chế về phần cứng.

Dịch vụ đám mây cung cấp cơ sở hạ tầng có thể mở rộng

cho phép xử lý song song,

cho phép thời gian đào tạo nhanh hơn

và giảm chi phí

để bảo trì phần cứng chuyên dụng trong nhà.

Sáng kiến AI Xanh thúc đẩy nghiên cứu

và thực tiễn phát triển

ưu tiên hiệu quả năng lượng.

Phát triển các mô hình đòi hỏi ít năng lượng hơn cho việc đào tạo

và suy luận có thể làm giảm đáng kể

tác động môi trường của học sâu.

Có sẵn các mô hình được đào tạo trước

thông qua các nền tảng như TensorFlow Hub

và Ôm Mặt Model Hub mang đến một phương pháp thiết thực

cho các cá nhân và tổ chức xây dựng trên công trình hiện có.

Những mô hình này có thể được điều chỉnh cho phù hợp với những nhiệm vụ cụ thể,

tiết kiệm cả thời gian và tài nguyên tính toán,

đồng thời mở rộng quyền truy cập

đến khả năng học sâu nâng cao.

Thách thức lớn thứ ba là thiếu khả năng diễn giải

và tính minh bạch trong các mô hình học sâu.

Các mô hình deep learning thường được gọi là hộp đen

vì sự phức tạp

và sự khó hiểu

cách họ đi đến những dự đoán cụ thể.

Ví dụ, trong khi một mô hình học sâu

trong chăm sóc sức khỏe có thể dự đoán chính xác

khả năng mắc bệnh cao,

nó có thể không giải thích được tại sao nó lại đưa ra dự đoán đó,

nâng cao niềm tin và mối quan tâm về đạo đức.

Độ mờ này là vấn đề trong các lĩnh vực đặt cược cao,

như chăm sóc sức khỏe và tài chính,

nơi mà khả năng giải thích là rất quan trọng để đạt được sự tin tưởng,

đáp ứng các tiêu chuẩn quy định,

và đảm bảo việc ra quyết định có đạo đức.

Việc thiếu khả năng diễn giải có thể dẫn đến

đến sự do dự trong việc áp dụng các hệ thống học sâu,

đặc biệt là khi số tiền đặt cược cao.

Trong tài chính, một mô hình được sử dụng để chấm điểm tín dụng

có thể vô tình gây ra sự thiên vị,

và nếu các bên liên quan không thể hiểu được

nó đưa ra quyết định như thế nào,

điều này có thể dẫn đến các vấn đề về đạo đức và pháp lý.

Để giải quyết bản chất hộp đen của học sâu,

các nhà nghiên cứu đang phát triển các phương pháp

để làm cho các mô hình dễ hiểu hơn.

Một cách tiếp cận là sử dụng các công cụ trực quan

tạo ra bản đồ nhiệt hoặc bản đồ chú ý,

hiển thị phần nào của đầu vào

ảnh hưởng đến quyết định của người mẫu/

Các kỹ thuật như SHAP,

Giải thích phụ gia SHApley và LIME,

Giải thích bất khả tri về mô hình có thể giải thích được tại địa phương,

cũng có thể được sử dụng để xác định

các tính năng quan trọng nhất ảnh hưởng đến quyết định của mô hình.

Những kỹ thuật này cung cấp cái nhìn sâu sắc về hành vi của mô hình

và giúp xây dựng niềm tin với người dùng cuối.

Một bước giảm thiểu khác là sử dụng các mô hình thay thế.

Đây là những mô hình đơn giản hơn

gần đúng với hành vi

của một hệ thống học sâu phức tạp.

Bằng cách sử dụng mô hình thay thế

bắt chước đầu ra của mô hình ban đầu,

các bên liên quan có thể đạt được sự hiểu biết

của quá trình ra quyết định

theo một cách dễ hiểu hơn.

Lan truyền liên quan theo lớp, LRP, là một kỹ thuật

theo dõi và trực quan hóa

sự đóng góp của từng nơ-ron riêng lẻ trong một mạng

đến một đầu ra nhất định.

Phương pháp này giúp phân tích hoạt động bên trong của một mô hình,

cung cấp sự minh bạch vào

thành phần nào ảnh hưởng đến quyết định cuối cùng.

Trong các miền có giá trị cao,

như chăm sóc sức khỏe và tài chính,

nơi mà khả năng giải thích và sự tin cậy là tối quan trọng,

các giải pháp phù hợp đang được phát triển để đáp ứng các quy định

và các chuẩn mực đạo đức.

Nỗ lực hợp tác giữa các nhà nghiên cứu,

các chuyên gia trong ngành và các nhà hoạch định chính sách là rất quan trọng

để tạo ra các mô hình có thể diễn giải được

và được người dùng tin tưởng.

Trong khi học sâu đã xúc tác

những tiến bộ công nghệ đáng kể,

tương lai phụ thuộc vào việc vượt qua thử thách

liên quan đến yêu cầu dữ liệu,

chi phí tính toán và khả năng giải thích.

Giải quyết những vấn đề này

thông qua các kỹ thuật xử lý dữ liệu được cải tiến,

phương pháp đào tạo tối ưu,

và các công cụ giải thích mạnh mẽ sẽ là chìa khóa

để khai phá toàn bộ tiềm năng của deep learning,

và nuôi dưỡng niềm tin rộng rãi hơn

và áp dụng trong các ngành công nghiệp.
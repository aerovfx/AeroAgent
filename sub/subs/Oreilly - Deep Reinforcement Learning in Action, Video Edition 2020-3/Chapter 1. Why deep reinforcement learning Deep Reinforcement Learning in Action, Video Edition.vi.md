# Chương 1. Tại sao học tăng cường sâu Học tăng cường sâu trong thực tế, Video Edition.vi

---

Phần 1.6 Tại sao học tăng cường

Chúng tôi đã đưa ra trường sâu

hợp lý cho học tăng cường, nhưng

tại sao lại là học tăng cường sâu?

Học tăng cường tồn tại từ

lâu trước khi có phổ biến học sâu.

Trên thực tế, một số phương pháp

pháp ban đầu mà chúng tôi

sẽ xem xét để nghiên cứu các mục

đích không có gì hơn là lưu

lưu trữ các trải nghiệm trong

tra cứu bảng, ví dụ: diction

Python và bảng cập nhật đó

trên mỗi vòng lặp của thuật toán.

Ý tưởng chính là tác nhân chơi trong môi trường

trường và xem những gì đang xảy ra, đồng thời lưu

lưu trữ những trải nghiệm của chính họ về những điều đó

điều gì đã xảy ra trong bất kỳ loại cơ sở dữ liệu nào.

Sau một thời gian, bạn có

có thể xem lại kiến trúc cơ sở dữ liệu

công thức này và đánh giá những gì

có kết quả và những gì không có.

Không có mạng thần kinh

hoặc các thuật toán lạ mắt khác.

Đối với các môi trường rất đơn giản,

điều này thực sự hoạt động tốt.

Ví dụ, trong xây dựng có

255.168 valid bảng vị trí.

Tra cứu bảng, còn được gọi là

bộ nhớ bảng sẽ có nhiều mục như

tương ứng, được lập trình từ mỗi trạng thái

status to a cụ thể hành động,

như trong Hình 1.12 và phần thưởng

khảo sát không được mô tả.

Trong quá trình đào tạo, thuật toán

toán có thể tìm hiểu được bất kỳ trạng thái nào

dẫn đến vị trí có lợi hơn và truy cập

update mục nhập vào bộ nhớ bảng.

Hình 1.12, bảng hoạt động nghiên cứu

dành riêng cho trò chơi XOX với chỉ

ba mục ở đó, người

chơi là một thuật toán, đóng vai X.

Khi người chơi được đưa ra

ra một vị trí trên cờ bàn,

tra cứu bảng sẽ được chỉ định

nước đi tiếp theo mà họ phải di.

Sẽ có một mục nhập cho mọi người

trạng thái có thể xảy ra trong trò chơi.

Khi môi trường trở nên phức tạp hơn, công việc

use the table of Memory will return nên khó khăn.

Ví dụ: mọi cấu hình màn hình của trò chơi điện tử

tử đều có thể được coi là một trạng thái đặc biệt.

Hình 1.13.

Hãy tưởng tượng bạn đang cố gắng lưu trữ mọi kết hợp có thể có

in the valid pixel value on the screen of game điện tử.

Thuật toán DQN của DeepMind, vốn dùng để

chơi Atari, được cung cấp 484 hình ảnh thang độ

xám có kích thước 84 pixel ở mỗi bước,

match 256 mũ 28.228 trạng thái trò chơi

duy nhất, mỗi pixel có 256 sắc thái xám khác

nhau và 4 nhân 84 nhân 84 bằng 28.228 pixel.

Con số này lớn hơn nhiều so với số nguyên tử

có trong vũ trụ mà người có thể quan sát được

và chắc chắn sẽ không

vừa với máy tính bộ nhớ.

Và điều này diễn ra sau khi thu nhỏ hình ảnh để giảm kích thước của

chúng có kích thước ban đầu của hình ảnh là 210 x 160 pixel.

Hình 1.13 là một loạt hình hình trong game Breakout,

trong đó các vị trí của các bóng hơi khác nhau ở từng khung hình.

Nếu bạn đang sử dụng bảng nghiên cứu, điều này tương thích

đáp ứng việc lưu trữ ba mục nhập duy nhất trong bảng.

Tra cứu bảng sẽ không khả thi vì nó có

quá nhiều trạng thái trò chơi để lưu trữ.

Việc lưu trữ mọi trạng thái có thể xảy ra là điều không

Tuy nhiên, có thể chúng tôi có thể thử giới hạn các khả năng.

Trong game Breakout, bạn sẽ điều khiển một mái chèo ở phía bên

Dưới màn hình có thể chuyển sang phải hoặc sang trái.

Mục tiêu của trò chơi là đánh bóng và

phá vỡ nhiều khối ở phía trên màn hình.

Trong trường hợp đó, chúng ta

có thể xác định các ràng buộc.

Chỉ quan sát các trạng thái khi bóng đang trở về mái chèo vì các hoạt động của

Chúng tôi không quan trọng khi chúng tôi đang chờ đợi kết quả bóng ở phía trên màn hình.

Hoặc chúng tôi có thể cung cấp

cấp các tính năng của riêng mình.

Thay vì cung cấp các hình ảnh thô, chỉ cần cung cấp

cấp độ của bóng, mái chèo và các khối còn lại.

Tuy nhiên, các phương pháp này yêu cầu người lập trình phải hiểu các chiến lược

cơ bản của trò chơi và chúng sẽ không dị hóa ở các môi trường khác.

Đó là lý do mà có học sâu.

Một thuật toán học sâu có thể nghiên cứu các vật tượng hóa chi tiết của các

sắp xếp các công cụ cụ thể và có thể học các trạng thái đặc biệt.

Vì một thuật toán sâu có giới hạn số lượng thông số nên chúng ta có thể sử dụng

sử dụng thuật toán đó để nén bất kỳ trạng thái nào có thể có bất kỳ thành phần nào

có thể xử lý hiệu quả, sau đó sử dụng cách biểu tượng mới để đưa ra quyết định.

Là kết quả của việc sử dụng các mạng nơ-ron, Atari DQN chỉ có 1792 thông số, mạng nơ-ron tích

nhanh với 16 bộ lọc 8x8, 32 bộ lọc 4x4 và một lớp kết nối ẩn hoàn toàn 256 nút, trái ngược

với từ 256 mũ 28 thành 228 khóa giá trị cặp cần thiết để lưu trữ toàn bộ trạng thái không giai đoạn.

Trong trường hợp trò chơi đột phá, độ sâu của mạng nơ-ron có thể tự động học cách nhận dạng các cấp độ tương thích cao cấp mà một cài đặt

người sử dụng phải thiết kế thủ công theo phương pháp đào tạo bảng tiếp theo.

Tức là, mạng có thể học cách nhìn thấy kết quả bóng,

Mái chèo, các khối và nhận được hướng dẫn của bóng.

Điều này khá tuyệt vời vì mạng chỉ

được cung cấp raw pixel dữ liệu.

Cuối chí còn thú vị hơn là các đặc sản cấp cao đã học

có thể chuyển các trò chơi hoặc môi trường khác.

Học sâu là tạo công thức bí mật

nên mọi thành công gần đây trong RL.

Không có lớp toán thuật toán nào khác có thể phát huy được sức mạnh

biểu tượng diễn đàn, hiệu quả và tính hoạt động sâu của mạng nơ-ron.
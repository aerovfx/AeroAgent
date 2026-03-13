# Chương 2. Áp dụng kẻ cướp để tối ưu hóa vị trí đặt quảng cáo Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Phần 2.3, áp dụng kẻ cướp để tối ưu hóa vị trí đặt quảng cáo.

Ví dụ về máy đánh bạc có vẻ không phải là một vấn đề đặc biệt trong thế giới thực, nhưng nếu

chúng ta thêm một yếu tố, nó sẽ trở thành một vấn đề kinh doanh thực tế, với một ví dụ điển hình là

vị trí đặt quảng cáo.

Bất cứ khi nào bạn truy cập một trang web có quảng cáo, công ty đặt quảng cáo đều muốn tối đa hóa

xác suất bạn sẽ nhấp vào chúng.

Giả sử chúng tôi quản lý 10 trang web thương mại điện tử, mỗi trang web tập trung vào việc bán một phạm vi rộng khác nhau.

Danh mục các mặt hàng bán lẻ như máy tính, giày dép, trang sức, v.v.

Chúng tôi muốn tăng doanh số bán hàng bằng cách giới thiệu khách hàng mua sắm trên một trong các trang web của chúng tôi đến một trang web khác

trang web mà họ có thể quan tâm.

Khi khách hàng thanh toán trên một trang web cụ thể trong mạng lưới của chúng tôi, chúng tôi sẽ hiển thị quảng cáo

đến một trong những trang web khác của chúng tôi với hy vọng họ sẽ đến đó và mua thứ khác.

Ngoài ra, chúng tôi có thể đặt quảng cáo cho một sản phẩm khác trên cùng một trang web.

Vấn đề của chúng tôi là chúng tôi không biết nên giới thiệu người dùng đến những trang web nào.

Chúng tôi có thể thử đặt quảng cáo ngẫu nhiên, nhưng chúng tôi nghi ngờ có thể có cách tiếp cận có mục tiêu hơn.

Phần 2.3.1, kẻ cướp theo ngữ cảnh.

Có lẽ bạn có thể thấy điều này chỉ tạo thêm một lớp phức tạp mới cho tên cướp không có vũ khí

vấn đề chúng ta đã xem xét ở đầu chương.

Ở mỗi lần chơi trò chơi, mỗi lần khách hàng kiểm tra một trang web cụ thể, chúng tôi có

n bằng 10 hành động chúng ta có thể thực hiện, tương ứng với 10 loại quảng cáo khác nhau

chúng tôi có thể đặt.

Điều khó khăn là vị trí đặt quảng cáo tốt nhất có thể phụ thuộc vào trang web hiện tại trên mạng.

khách hàng đang bật.

Ví dụ: một khách hàng xem trang web trang sức của chúng tôi có thể có tâm trạng mua hàng hơn

một đôi giày mới để đi cùng với chiếc vòng cổ kim cương mới của họ hơn là mua một chiếc mới

máy tính xách tay.

Vì vậy, vấn đề của chúng ta là tìm ra cách một trang web cụ thể liên quan đến một quảng cáo cụ thể.

Điều này dẫn chúng ta đến không gian trạng thái.

Vấn đề tên cướp không có vũ khí mà chúng tôi bắt đầu có không gian hành động phần tử n, không gian hoặc

tập hợp tất cả các hành động có thể xảy ra nhưng không có khái niệm về trạng thái.

Nghĩa là, không có thông tin nào trong môi trường có thể giúp chúng tôi chọn được một nhánh tốt.

Cách duy nhất để chúng ta có thể tìm ra loại vũ khí nào tốt là thử và sai.

Trong vấn đề quảng cáo, chúng ta biết người dùng đang mua thứ gì đó trên một trang web cụ thể, điều này có thể

cung cấp cho chúng tôi một số thông tin về tùy chọn của người dùng đó và có thể giúp hướng dẫn quyết định của chúng tôi

về việc nên đặt quảng cáo nào.

Chúng tôi gọi thông tin theo ngữ cảnh này là một trạng thái và loại vấn đề mới này là theo ngữ cảnh.

kẻ cướp xem hình 2.5.

Hình 2.5 tổng quan về kẻ cướp theo ngữ cảnh đối với vị trí đặt quảng cáo.

Tác nhân, là một thuật toán mạng thần kinh, nhận thông tin trạng thái.

Trong trường hợp này, trang web hiện tại mà người dùng đang truy cập, trang web này được sử dụng để chọn một trong số nhiều trang web

quảng cáo nên đặt ở bước thanh toán.

Người dùng sẽ nhấp vào quảng cáo hay không, dẫn đến tín hiệu phần thưởng được chuyển tiếp

quay lại đại lý để học hỏi.

Sự định nghĩa.

Một trạng thái trong trò chơi hay trong một bài toán học tăng cường tổng quát hơn là tập hợp thông tin

có sẵn trong môi trường có thể được sử dụng để đưa ra quyết định.

Phần 2.3.2 nêu phần thưởng cho hành động.

Trước khi tiếp tục, hãy củng cố một số thuật ngữ và khái niệm mà chúng tôi đã giới thiệu

cho đến nay.

Các thuật toán học tăng cường cố gắng mô hình hóa thế giới theo cách mà máy tính có thể

hiểu và tính toán.

Cụ thể, thuật toán RL mô hình hóa thế giới như thể nó chỉ liên quan đến một tập hợp các trạng thái,

S, không gian trạng thái, là tập hợp các đặc điểm về môi trường, tập hợp các hành động,

A, không gian hành động có thể được thực hiện trong một trạng thái nhất định và phần thưởng được trao cho

thực hiện một hành động trong một trạng thái cụ thể.

Khi chúng ta nói về việc thực hiện một hành động cụ thể trong một trạng thái cụ thể, chúng ta thường gọi nó là trạng thái

cặp hành động, S-A.

Ghi chú.

Mục tiêu của bất kỳ thuật toán RL nào là tối đa hóa phần thưởng trong suốt quá trình

tập.

Vì bài toán kẻ cướp N-armed ban đầu của chúng tôi không có không gian trạng thái, chỉ có không gian hành động,

chúng tôi chỉ cần tìm hiểu mối quan hệ giữa hành động và phần thưởng.

Chúng tôi đã học được mối quan hệ bằng cách sử dụng bảng tra cứu để lưu trữ kinh nghiệm nhận

phần thưởng cho những hành động cụ thể.

Chúng tôi đã lưu trữ các cặp phần thưởng hành động, A, K và R, K, trong đó phần thưởng khi chơi K là trung bình

trên tất cả các vở kịch trước đây liên quan đến việc thực hiện hành động, A, K.

Trong bài toán tên cướp N-armed của chúng tôi, chúng tôi chỉ có 10 hành động nên bảng tra cứu gồm 10 hàng là

rất hợp lý.

Nhưng khi chúng ta giới thiệu một không gian trạng thái với các kẻ cướp theo ngữ cảnh, chúng ta bắt đầu có một vụ nổ tổ hợp

của các bộ phần thưởng hành động trạng thái có thể có.

Ví dụ: nếu chúng ta có không gian trạng thái gồm 100 trạng thái và mỗi trạng thái được liên kết với

10 hành động, chúng ta có 1000 mẩu dữ liệu khác nhau cần lưu trữ và tính toán lại.

Trong hầu hết các bài toán mà chúng ta sẽ xem xét trong cuốn sách này, không gian trạng thái rất lớn,

vì vậy một bảng tra cứu đơn giản là không khả thi.

Đó là nơi mà việc học sâu xuất hiện.

Khi được đào tạo đúng cách, mạng lưới thần kinh sẽ học rất tốt các khái niệm trừu tượng

loại bỏ những chi tiết ít giá trị.

Họ có thể tìm hiểu các mẫu và quy luật có thể kết hợp trong dữ liệu để có thể nén một cách hiệu quả

một lượng lớn dữ liệu trong khi vẫn giữ được những thông tin quan trọng.

Do đó, mạng lưới thần kinh có thể được sử dụng để tìm hiểu các mối quan hệ phức tạp giữa hành động trạng thái

các cặp và phần thưởng mà chúng ta không cần phải lưu trữ tất cả những trải nghiệm đó dưới dạng ký ức thô.

Chúng ta thường gọi một phần của thuật toán RL đưa ra quyết định dựa trên một số thông tin

đại lý.

Để giải quyết vấn đề kẻ cướp theo ngữ cảnh mà chúng ta đã thảo luận, chúng ta sẽ sử dụng một nơron thần kinh.

mạng lưới làm đại lý của chúng tôi.

Tuy nhiên, trước tiên, chúng tôi sẽ dành chút thời gian để giới thiệu PyTorch.

Khung học sâu mà chúng tôi sẽ sử dụng trong suốt cuốn sách này để xây dựng mạng lưới thần kinh.
# 03 củng cố-học-từ-con người-phản hồi-rlhf

---

Hãy xem xét nhiệm vụ

về tóm tắt văn bản,

nơi bạn sử dụng mô hình để tạo

một đoạn văn bản ngắn ghi lại

những điểm quan trọng nhất

trong một bài viết dài hơn.

Mục tiêu của bạn là sử dụng tinh chỉnh để

cải thiện khả năng tóm tắt của mô hình,

bằng cách cho nó xem những ví dụ về

tóm tắt do con người tạo ra.

Năm 2020, các nhà nghiên cứu tại OpenAI đã xuất bản một

bài viết khám phá việc sử dụng tinh chỉnh

với phản hồi của con người để đào tạo một mô hình

viết tóm tắt ngắn các bài văn bản.

Ở đây bạn có thể thấy rằng một mô hình

tinh chỉnh phản hồi của con người được tạo ra

phản hồi tốt hơn mô hình được đào tạo trước,

một mô hình tinh chỉnh hướng dẫn, và

thậm chí là đường cơ sở tham khảo của con người.

Một kỹ thuật phổ biến để hoàn thiện kích thước lớn

mô hình ngôn ngữ với phản hồi của con người là

được gọi là học tăng cường từ

phản hồi của con người, hay gọi tắt là RLHF.

Đúng như tên gọi, RLHF sử dụng

học tăng cường, hoặc RL cho

Nói tóm lại, để hoàn thiện LLM

với dữ liệu phản hồi của con người,

dẫn đến một mô hình tốt hơn

phù hợp với sở thích của con người.

Bạn có thể sử dụng RLHF để đảm bảo rằng

mô hình của bạn tạo ra kết quả đầu ra

tối đa hóa tính hữu dụng và

mức độ liên quan đến lời nhắc đầu vào.

Có lẽ quan trọng nhất là RLHF có thể

giúp giảm thiểu khả năng gây hại.

Bạn có thể huấn luyện mô hình của mình để đưa ra những cảnh báo

thừa nhận những hạn chế của mình và

để tránh ngôn ngữ và chủ đề độc hại.

Một ứng dụng thú vị tiềm năng của

RLHF là sự cá nhân hóa của LLM,

nơi người mẫu tìm hiểu sở thích

của mỗi người dùng cá nhân thông qua

một quá trình phản hồi liên tục.

Điều này có thể dẫn tới những điều mới thú vị

các công nghệ như học tập cá nhân

kế hoạch hoặc trợ lý AI được cá nhân hóa.

Nhưng để hiểu được những điều này

các ứng dụng trong tương lai có thể được thực hiện

có thể, hãy bắt đầu bằng cách lấy

cái nhìn sâu hơn về cách thức hoạt động của RLHF.

Trong trường hợp bạn chưa quen

với việc học tăng cường,

đây là một cái nhìn tổng quan cấp cao về

những khái niệm quan trọng nhất.

Học tăng cường là một loại

học máy trong đó một tác nhân học

đưa ra các quyết định liên quan đến một vấn đề cụ thể

mục tiêu bằng cách thực hiện các hành động trong một môi trường,

với mục tiêu tối đa hóa

một số khái niệm về phần thưởng tích lũy.

Trong khuôn khổ này, đại lý liên tục

học hỏi từ kinh nghiệm của mình bằng cách

thực hiện hành động, quan sát kết quả

những thay đổi của môi trường và

nhận phần thưởng hoặc hình phạt,

dựa trên kết quả của hành động của mình.

Bằng cách lặp lại quá trình này,

đại lý dần dần hoàn thiện chiến lược của mình hoặc

chính sách để đưa ra quyết định tốt hơn và

tăng cơ hội thành công của nó.

Một ví dụ hữu ích để minh họa những ý tưởng này

đang đào tạo người mẫu chơi Tic-Tac-Toe.

Chúng ta hãy xem xét.

Trong ví dụ này, tác nhân là một mô hình hoặc

chính sách hoạt động như một người chơi Tic-Tac-Toe.

Mục tiêu của nó là giành chiến thắng trong trò chơi.

Môi trường là ba

bằng ba bảng trò chơi, và

trạng thái tại bất kỳ thời điểm nào,

là cấu hình hiện tại của bo mạch.

Không gian hành động bao gồm tất cả

các vị trí có thể mà người chơi có thể

chọn dựa trên trạng thái bảng hiện tại.

Người đại diện đưa ra quyết định bằng cách tuân theo

một chiến lược được gọi là chính sách RL.

Bây giờ, khi tác nhân thực hiện hành động,

nó thu thập phần thưởng dựa trên hành động'

hiệu quả trong

đang tiến tới chiến thắng.

Mục tiêu của việc học tăng cường là dành cho

đại lý để tìm hiểu chính sách tối ưu cho

một môi trường nhất định mà

tối đa hóa phần thưởng của họ.

Quá trình học tập này được lặp đi lặp lại và

bao gồm việc thử và sai.

Ban đầu, tác nhân lấy ngẫu nhiên

hành động dẫn đến một trạng thái mới.

Từ trạng thái này,

đại lý tiến hành khám phá tiếp theo

trạng thái thông qua các hành động tiếp theo.

Chuỗi hành động và

các trạng thái tương ứng tạo thành một playout,

thường được gọi là triển khai.

Khi đại lý tích lũy kinh nghiệm,

nó dần dần khám phá những hành động mang lại

phần thưởng dài hạn cao nhất,

cuối cùng dẫn đến thành công trong trò chơi.

Bây giờ chúng ta hãy xem làm thế nào

ví dụ Tic-Tac-Toe có thể được mở rộng

đối với trường hợp tinh chỉnh lớn

mô hình ngôn ngữ với RLHF

Trong trường hợp này, chính sách của đại lý

hướng dẫn các hành động là LLM,

và mục tiêu của nó là tạo ra

văn bản được coi là

phù hợp với sở thích của con người.

Điều này có thể có nghĩa là văn bản dành cho

ví dụ, hữu ích, chính xác và không độc hại.

Môi trường là bối cảnh

cửa sổ của mô hình,

không gian trong đó văn bản có thể

được nhập thông qua một dấu nhắc.

Trạng thái mà mô hình xem xét trước đó

thực hiện một hành động là bối cảnh hiện tại.

Điều đó có nghĩa là bất kỳ văn bản nào hiện tại

chứa trong cửa sổ ngữ cảnh.

Hành động ở đây là hành động

của việc tạo ra văn bản.

Đây có thể là một từ duy nhất,

một câu hoặc một văn bản dạng dài hơn,

tùy theo nhiệm vụ

do người dùng chỉ định.

Không gian hành động là từ vựng mã thông báo,

nghĩa là tất cả các token có thể có

mà mô hình có thể chọn

để tạo ra sự hoàn thành.

Cách LLM quyết định tạo ra lần tiếp theo

mã thông báo theo trình tự, phụ thuộc vào

sự biểu diễn thống kê của ngôn ngữ

mà nó đã học được trong quá trình đào tạo.

Tại bất kỳ thời điểm nào, hành động đó

mô hình sẽ lấy, có nghĩa là

mã thông báo nó sẽ chọn tiếp theo, tùy thuộc vào

văn bản gợi ý trong ngữ cảnh và

phân bố xác suất

trên không gian từ vựng.

Phần thưởng được phân bổ dựa trên cách thức

sự hoàn thiện chặt chẽ phù hợp với con người

sở thích.

Với sự đa dạng của con người

phản ứng với ngôn ngữ,

xác định phần thưởng phức tạp hơn

hơn trong ví dụ Tic-Tac-Toe.

Một cách bạn có thể làm điều này là

để có sự đánh giá của con người

tất cả sự hoàn thiện của mô hình

dựa trên một số thước đo căn chỉnh,

chẳng hạn như xác định xem liệu sản phẩm được tạo ra có

văn bản độc hại hoặc không độc hại.

Phản hồi này có thể được biểu diễn dưới dạng

một giá trị vô hướng, bằng 0 hoặc bằng một.

Trọng số LLM sau đó được cập nhật

lặp đi lặp lại để tối đa hóa phần thưởng

thu được từ bộ phân loại của con người,

cho phép mô hình tạo ra

hoàn thiện không độc hại.

Tuy nhiên, việc thu thập phản hồi của con người

có thể tốn thời gian và tốn kém.

Là một giải pháp thay thế thực tế và có thể mở rộng,

bạn có thể sử dụng một mô hình bổ sung,

được gọi là mô hình khen thưởng,

để phân loại đầu ra của LLM và

đánh giá mức độ phù hợp

với sở thích của con người.

Bạn sẽ bắt đầu với số lượng nhỏ hơn

ví dụ con người để đào tạo thứ cấp

mô hình theo truyền thống của bạn

phương pháp học tập có giám sát.

Sau khi được đào tạo, bạn sẽ sử dụng mô hình phần thưởng

để đánh giá đầu ra của LLM và

chỉ định một giá trị phần thưởng, từ đó nhận được

được sử dụng để cập nhật trọng số của LLM và

đào tạo một phiên bản mới phù hợp với con người.

Chính xác thì trọng số được cập nhật như thế nào

việc hoàn thành mô hình được đánh giá,

phụ thuộc vào thuật toán

được sử dụng để tối ưu hóa chính sách.

Bạn sẽ khám phá những vấn đề này

sâu hơn trong thời gian ngắn.

Cuối cùng, lưu ý rằng trong bối cảnh

của mô hình ngôn ngữ,

trình tự các hành động và

các tiểu bang được gọi là triển khai,

thay vì thuật ngữ playout được sử dụng

trong học tăng cường cổ điển.

Mô hình khen thưởng là thành phần trung tâm

của quá trình học tập tăng cường.

Nó mã hóa tất cả các sở thích mà

đã được học từ phản hồi của con người, và

nó đóng vai trò trung tâm trong cách mô hình

cập nhật trọng số của nó qua nhiều lần lặp.

Trong video tiếp theo, bạn sẽ thấy điều này như thế nào

mô hình được đào tạo và cách bạn sử dụng nó để

phân loại kết quả đầu ra của mô hình trong quá trình

quá trình học tập củng cố.

Chúng ta hãy tiếp tục và xem xét.
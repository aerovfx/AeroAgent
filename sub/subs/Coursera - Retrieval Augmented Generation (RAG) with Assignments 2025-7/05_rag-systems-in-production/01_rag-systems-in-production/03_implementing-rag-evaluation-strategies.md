# 03 chiến lược triển khai-rag-đánh giá

---

Bước đầu tiên tốt để giải quyết các thách thức trong sản xuất là xây dựng một hệ thống có khả năng quan sát mạnh mẽ.

Để bắt đầu, chúng ta hãy xem xét các thành phần khác nhau mà nó nên bao gồm.

Một nền tảng có khả năng quan sát cần theo dõi một số loại thông tin khác nhau.

Đầu tiên, nó phải theo dõi các số liệu hiệu suất phần mềm phổ biến như độ trễ, thông lượng, bộ nhớ,

và tính toán mức sử dụng.

Giống như hầu hết mọi hệ thống phần mềm sản xuất, bạn sẽ muốn biết có bao nhiêu yêu cầu

hệ thống đang xử lý, mất bao lâu và tiêu tốn bao nhiêu tài nguyên.

Tiếp theo, bạn sẽ cần theo dõi nhiều số liệu chất lượng.

Chất lượng ở đây có thể có nghĩa là mọi thứ từ sự hài lòng của người dùng với những phản hồi cuối cùng mà họ nhận được

để thu hồi chú chó tha mồi của bạn.

Ngoài việc biết hệ thống của bạn hoạt động nhanh chóng và hiệu quả như thế nào, bạn sẽ muốn

biết kết quả cuối cùng có đáp ứng được tiêu chuẩn chất lượng mà bạn đã đặt ra hay không.

Điều quan trọng nữa là thông tin này được thu thập và báo cáo như thế nào.

Hệ thống của bạn sẽ nắm bắt số liệu thống kê tổng hợp theo thời gian để giúp bạn theo dõi các xu hướng cấp cao

trong hiệu suất và nhanh chóng xác định sự hồi quy.

Riêng biệt, hệ thống sẽ ghi lại nhật ký chi tiết.

Những điều này sẽ cho phép bạn theo dõi hành trình của từng lời nhắc thông qua quy trình RAG của bạn,

đặc biệt hữu ích khi bạn đang cố gắng tìm hiểu nguyên nhân khiến hoạt động kém hiệu quả

những phản hồi.

Cuối cùng, hệ thống đánh giá của bạn lý tưởng nhất là nên cho phép thử nghiệm.

Nếu bạn đang cân nhắc chuyển sang mô hình ngôn ngữ mới, điều chỉnh lời nhắc hệ thống hoặc điều chỉnh

cài đặt trên chó tha mồi của bạn, bạn muốn chạy thử nghiệm tùy chỉnh một cách an toàn

những thay đổi về môi trường hoặc thử nghiệm A-B với người dùng trong quá trình sản xuất.

Khả năng giám sát tác động đến các số liệu hiệu suất và chất lượng là điều cuối cùng cần có

giúp bạn quyết định xem bạn có muốn chuyển những thử nghiệm này vào hệ thống sản xuất của mình hay không.

Với cấu trúc cấp cao đó, hãy xem xét các số liệu cụ thể mà bạn muốn theo dõi.

Một khuôn khổ tốt để suy nghĩ thấu đáo tất cả những điều này là phạm vi và loại người đánh giá.

Phạm vi ở đây có nghĩa là liệu đánh giá có nhắm mục tiêu vào một thành phần trong hệ thống RAG của bạn hay không

hệ thống tổng thể.

Trong khi đó, loại người đánh giá hỏi liệu đánh giá có dựa trên mã hay không, sử dụng LLM làm đánh giá hay

dựa vào phản hồi của con người.

Bạn có thể coi hai chiều này tạo thành một lưới, với các giá trị bạn chọn nằm trong

một trong những hình vuông kết quả.

Hãy cùng khám phá từng chiều và sau đó xem xét vị trí của một số giá trị phổ biến trong lưới đó.

Hãy bắt đầu với phạm vi eval.

Đánh giá ở mức chung thường dùng để tóm tắt hiệu năng tổng thể của hệ thống hoặc đưa ra đánh giá ở mức cao.

cái nhìn về cách mọi thứ đang diễn ra

Trong khi đó, các đánh giá ở cấp độ thành phần giúp bạn gỡ lỗi nguồn gốc của các vấn đề riêng lẻ.

Ví dụ: bạn có thể theo dõi độ trễ trên tổng thể hệ thống của mình và thấy rằng nó quá cao.

Tuy nhiên, để truy tìm nguồn gốc của vấn đề đó, bạn cần đánh giá ở cấp thành phần để

theo dõi xem liệu trình truy xuất, LLM của bạn hoặc thành phần khác cuối cùng có gây ra

vấn đề.

Loại người đánh giá tập trung vào cách tạo ra đánh giá.

Đánh giá dựa trên mã là rẻ nhất, đơn giản nhất và dễ thực hiện nhất.

Đây có thể là tất cả mọi thứ từ việc chỉ ghi lại số lượng lời nhắc mà hệ thống của bạn xử lý

một giây để chạy thử nghiệm đơn vị để đảm bảo LLM của bạn xuất ra JSON hợp lệ.

Điều quan trọng ở đây là những đánh giá này có thể được chạy tự động, mang tính quyết định và

gần như được chạy miễn phí.

Mặt khác của quang phổ là phản hồi và đánh giá của con người.

Một ví dụ phổ biến là người dùng ứng dụng của bạn đánh dấu phản hồi bằng biểu tượng thích hoặc không thích

xuống.

Ngay cả khi nó không cung cấp cho bạn nhiều thông tin chi tiết, thì việc nhiều người dùng đánh dấu

câu trả lời không thích của bạn là một dấu hiệu hữu ích cho thấy bạn có vấn đề cần khắc phục.

Bạn cũng có thể cung cấp cho người dùng một hộp văn bản để đưa ra phản hồi chi tiết hơn.

Các đánh giá khác có thể được chạy tự động nhưng ban đầu phụ thuộc vào dữ liệu đầu vào của con người.

Ví dụ: bạn có thể yêu cầu con người biên dịch trước bộ dữ liệu về lời nhắc và các tài liệu liên quan

cái đó cần được lấy lại.

Sau khi tập dữ liệu đó được biên soạn, bạn có thể nhanh chóng tính toán các số liệu phổ biến như độ chính xác và

nhớ lại.

Nhưng cần nhớ rằng tại một thời điểm nào đó con người cần biên soạn bài kiểm tra ban đầu đó

tập dữ liệu.

Nói chung, phản hồi và chú thích của con người là một cách tiếp cận tốn kém hơn nhưng nó nắm bắt được

thông tin mà các đánh giá dựa trên mã sẽ bỏ lỡ.

LLM với tư cách là giám khảo cố gắng phân chia sự khác biệt bằng cách sử dụng mô hình ngôn ngữ để chấm điểm khác nhau

các thành phần của hiệu suất hệ thống của bạn.

Ví dụ: LLM có thể xác định xem các tài liệu được truy xuất có phải là

thực sự có liên quan đến lời nhắc của người dùng.

LLM với tư cách là giám khảo linh hoạt hơn so với đánh giá dựa trên mã và rẻ hơn phản hồi của con người.

Tuy nhiên, LLM với tư cách là giám khảo vẫn cần phải được điều chỉnh cẩn thận.

Các mô hình có thể có những thành kiến ​​và phản hồi ủng hộ do mô hình từ chính gia đình của họ tạo ra.

Họ cũng cần các tiêu chí đánh giá rõ ràng và thường hoạt động tốt nhất với các tiêu chuẩn riêng biệt như

phù hợp hoặc không liên quan thay vì đánh giá theo thang điểm từ 0 đến 100.

Hãy xem làm thế nào tất cả các khái niệm đánh giá khác nhau này có thể được kết hợp lại thành một

nhưng bạn có thể bắt đầu thu thập bộ số liệu toàn diện.

Một ý tưởng hay để bắt đầu là thu thập cả số liệu về hiệu suất và chất lượng phần mềm cho từng chuyên ngành.

thành phần và sau đó là hệ thống tổng thể.

Các số liệu hiệu suất hệ thống như độ trễ, thông lượng, mức sử dụng bộ nhớ hoặc mã thông báo được tạo mỗi giây

là các đánh giá dựa trên mã, khiến chúng rẻ và dễ thu thập.

Bạn có thể dễ dàng nắm bắt dữ liệu này ở cả cấp độ thành phần và toàn hệ thống.

Đối với các số liệu chất lượng, thông thường bạn sẽ cần phải dựa vào các kỹ thuật sử dụng chú thích của con người

hoặc LLM với tư cách là thẩm phán.

Đối với các chỉ số chất lượng trên toàn hệ thống, bạn có thể cho phép người dùng tán thành hoặc không thích bạn

giảm bớt các phản hồi được tạo ra, cung cấp cho bạn phản hồi về chất lượng phản hồi tổng thể.

Để đánh giá một chú chó săn mồi, bạn có thể dành thời gian biên soạn một bài kiểm tra có chú thích của con người

tập hợp các tài liệu được truy xuất nhanh chóng và dự kiến, cho phép bạn tính toán thông thường

các số liệu như thu hồi và độ chính xác.

Để đánh giá chất lượng LLM, thông thường bạn sẽ sử dụng các đánh giá dựa trên LLM, giống như các đánh giá được tìm thấy trong

Thư viện Ragas, để đánh giá những thứ như mức độ liên quan của phản hồi, chất lượng trích dẫn hoặc cách thức

à, LLM đang bỏ qua thông tin được truy xuất không liên quan.

Cách tiếp cận như thế này mang lại cho bạn cái nhìn sâu sắc về cả hiệu suất và chất lượng của

hệ thống tổng thể và các thành phần riêng lẻ.

Nó cũng nắm bắt được sự cân bằng tốt giữa các đánh giá rẻ tiền như độ trễ và các số liệu đắt tiền hơn

dựa vào chú thích của con người hoặc các cuộc gọi LLM.

Từ đó, bạn có thể quyết định những lĩnh vực bổ sung nào bạn muốn xem xét kỹ hơn.

Đó là cái nhìn cấp cao nhanh chóng về những thành phần mà hệ thống quan sát RAG nên bao gồm

và sự đánh đổi khi thiết kế nó.

Hãy cùng tôi xem video tiếp theo và cùng xem xét kỹ hơn một số điều cần cân nhắc

phát sinh khi bạn thực sự triển khai hệ thống này.
# 02 chó săn-kiến trúc-tổng quan

---

Trong suốt mô-đun này, bạn sẽ tìm hiểu sâu về một số kỹ thuật tìm kiếm khác nhau, nhưng

việc có một mô hình tinh thần của toàn bộ hệ thống có thể sẽ hữu ích.

Với ý nghĩ đó, chúng ta hãy bắt đầu mô-đun này với cái nhìn tổng thể về cấu trúc của chó săn mồi

và cách mỗi thành phần bên trong nó hoạt động cùng nhau.

Khi hệ thống giá đỡ nhận được lời nhắc của bạn, trước tiên nó sẽ được gửi đến người truy xuất.

Chó tha mồi sẽ có quyền truy cập vào cơ sở kiến thức mà bạn có thể coi đó chỉ là một nhóm

của các tập tin văn bản nằm trong cơ sở dữ liệu.

Người truy tìm cần nhanh chóng quyết định tài liệu nào phù hợp nhất với lời nhắc

và trả lại chúng để chúng có thể được chuyển đến LLM.

Hầu hết các công cụ truy tìm hiện đại đều sử dụng hai kỹ thuật tìm kiếm khác nhau như một phần của quy trình này.

Đầu tiên là tìm kiếm từ khóa truyền thống hơn.

Điều này có nghĩa là công cụ truy xuất tìm kiếm các tài liệu có chứa các từ chính xác được tìm thấy trong

nhắc nhở.

Cách tiếp cận này đã được thử nghiệm theo thời gian và đã hỗ trợ các hệ thống truy xuất thông tin trong nhiều thập kỷ.

Cách tiếp cận thứ hai là tìm kiếm ngữ nghĩa.

Điều này có nghĩa là trình truy xuất tìm kiếm các tài liệu có ý nghĩa tương tự với lời nhắc.

Cách tiếp cận này làm cho công cụ truy tìm linh hoạt hơn vì nó cho phép nó tìm thấy các tài liệu

liên quan đến lời nhắc nhưng có thể không chứa các từ chính xác mà người dùng đưa vào trong lời nhắc của họ

nhắc nhở.

Mỗi kỹ thuật tìm kiếm sẽ được sử dụng để trả về một tập hợp tài liệu, có thể là 20-50 tài liệu

mỗi cái.

Thông thường sẽ có nhiều tài liệu xuất hiện trong cả hai danh sách nhưng do kiểu dáng

tìm kiếm là khác nhau, chúng có thể được xếp hạng cao hơn ở trang này so với trang khác.

Tại thời điểm này, mỗi danh sách được lọc dựa trên siêu dữ liệu của chúng.

Ví dụ: một số tài liệu trong cơ sở tri thức của bạn có thể liên quan đến các thành viên trong nhóm kỹ thuật của bạn.

nhóm và những người khác phù hợp hơn với những người làm việc trong lĩnh vực nhân sự.

Hệ thống sẽ biết người dùng là thành viên của nhóm nào và áp dụng bộ lọc siêu dữ liệu tại

điểm này để đảm bảo chỉ những tài liệu liên quan đến bộ phận đó mới được phép chuyển tiếp.

Bây giờ công cụ truy xuất có hai danh sách được lọc, một danh sách được tạo bằng tìm kiếm từ khóa và

khác bằng tìm kiếm ngữ nghĩa.

Hai danh sách này hiện được kết hợp để tạo ra thứ hạng cuối cùng cho các tài liệu phù hợp nhất.

Công cụ truy xuất trả về các tài liệu được xếp hạng cao nhất từ danh sách cuối cùng này và tại thời điểm này

việc truy xuất đã hoàn tất.

Các tài liệu được gửi cùng để được thêm vào lời nhắc tăng cường.

Kiểu tìm kiếm này được gọi là tìm kiếm kết hợp vì nó dựa trên nhiều kỹ thuật để

đưa ra xếp hạng tài liệu cuối cùng của nó.

Mỗi kỹ thuật đều mang lại những lợi ích góp phần vào hiệu suất chung của chó săn.

Tìm kiếm từ khóa đảm bảo hệ thống nhạy cảm với các từ chính xác mà người dùng đưa vào

nhắc nhở.

Tìm kiếm ngữ nghĩa giúp hệ thống linh hoạt hơn trong việc tìm kiếm các tài liệu có ý nghĩa tương tự

theo lời nhắc, ngay cả khi họ không sử dụng những từ giống nhau.

Lọc siêu dữ liệu cho phép hệ thống loại trừ các tài liệu dựa trên các tiêu chí cứng nhắc theo cách

mà cả hai cách tiếp cận khác đều không cho phép.

Thiết kế một chú chó săn mồi hiệu suất cao có nghĩa là phải hiểu được sức mạnh tương đối của từng loài.

của những kỹ thuật này và sau đó điều chỉnh sự cân bằng giữa chúng để phù hợp với nhu cầu của bạn

dự án.

Với ý nghĩ đó, chúng ta hãy bắt đầu đi sâu vào từng kỹ thuật trong số ba kỹ thuật này, bắt đầu

với cách đơn giản nhất trong ba cách đó là lọc siêu dữ liệu.
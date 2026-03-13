# 03 lọc siêu dữ liệu

---

Lọc siêu dữ liệu là kỹ thuật đơn giản nhất và có thể quen thuộc nhất được sử dụng bên trong công cụ truy xuất.

Chúng ta hãy xem nó được sử dụng như thế nào và những lợi ích cụ thể mà nó mang lại cho cách thức hoạt động của chó săn.

Lọc siêu dữ liệu sử dụng các tiêu chí cứng nhắc để thu hẹp các tài liệu được trình truy xuất trả về,

dựa trên siêu dữ liệu của tài liệu.

Siêu dữ liệu này có thể là thông tin, như tiêu đề, tác giả, ngày tạo, đặc quyền truy cập, v.v.

Đây là một ví dụ đơn giản về cách nó hoạt động.

Giả sử bạn làm việc tại một tờ báo và muốn xây dựng một công cụ truy tìm các bài báo được viết về lịch sử tờ báo của bạn.

Cơ sở kiến ​​thức sẽ chứa hàng ngàn bài viết khác nhau.

Mỗi bài viết được gắn thẻ với nhiều phần siêu dữ liệu, bao gồm tiêu đề của nó,

ngày bài viết được xuất bản, tác giả của bài viết,

bài báo xuất hiện ở mục nào của tờ báo, v.v.

Mặc dù toàn bộ nội dung của mỗi bài viết nằm ở đâu đó trong cơ sở kiến thức,

hệ thống chỉ có thể tìm kiếm các bài viết dựa trên siêu dữ liệu này.

Truy vấn loại chỉ mục này trông rất giống việc viết một truy vấn SQL.

Nếu bạn chỉ lọc dựa trên một phần siêu dữ liệu,

bạn có thể tìm thấy mọi bài báo được xuất bản vào một ngày nhất định hoặc thậm chí mọi bài báo được viết bởi một tác giả cụ thể.

Bạn cũng có thể viết các truy vấn phức tạp hơn và lọc trên nhiều phần siêu dữ liệu.

Ví dụ: bạn có thể tìm thấy tất cả các bài viết được viết cho mục ý kiến ​​từ tháng 6 đến tháng 7 năm 2024 bởi nhà báo yêu thích của bạn.

Chỉ những bài viết đáp ứng mọi điều kiện mới được trả về và những bài viết còn lại sẽ bị lọc ra.

Nếu bạn đã từng lọc một bảng trong bảng tính thì bạn đã lọc siêu dữ liệu.

Bạn chỉ đang sử dụng một bộ tiêu chí nghiêm ngặt để xác định thành viên nào trong bộ sưu tập dữ liệu lớn hơn mà bạn muốn sử dụng.

Bên trong hệ thống RAG điển hình, bạn sẽ không sử dụng tính năng lọc siêu dữ liệu để thực hiện truy xuất,

mà là để giúp thu hẹp kết quả được trả về bởi các kỹ thuật truy xuất khác.

Bản thân các bộ lọc cũng thường không được xác định bởi những gì người dùng nói trong lời nhắc,

mà là các thuộc tính khác của người dùng thực hiện yêu cầu.

Ví dụ, hãy xem xét ví dụ về tờ báo trước đây.

Giả sử một số bài viết của bạn được xuất bản miễn phí trên internet mở và những bài viết khác chỉ có thể được truy cập bởi những người đăng ký trả phí.

Mỗi bài viết có thể có một phần lưu trữ siêu dữ liệu cho dù đó là bài viết miễn phí hay trả phí.

Khi người dùng tìm kiếm cơ sở dữ liệu, hệ thống có thể phát hiện xem họ có đăng nhập với tư cách là người đăng ký trả phí hay không.

Nếu không, bộ lọc siêu dữ liệu sẽ được đặt để loại trừ các bài viết trả phí khỏi kết quả tìm kiếm.

Tương tự, nếu tờ báo của bạn in bài ở nhiều khu vực trên thế giới,

mỗi bài viết có thể có một phần siêu dữ liệu lưu trữ khu vực nơi bài viết được xuất bản.

Khi người đọc truy vấn hệ thống, bạn có thể phát hiện họ đang ở khu vực nào và chỉ trả lại các bài viết từ khu vực của họ.

Lọc siêu dữ liệu có một số lợi thế.

Thứ nhất, nó đơn giản về mặt khái niệm, giúp bạn dễ dàng hiểu cách hệ thống hoạt động và gỡ lỗi.

Thứ hai, đó là một cách tiếp cận nhanh chóng, hoàn thiện và được tối ưu hóa tốt.

Cuối cùng, và có lẽ là quan trọng nhất,

đó là cách tiếp cận duy nhất cho phép hệ thống của bạn quyết định xem tài liệu có được truy xuất hay không dựa trên tiêu chí cứng nhắc.

Nếu bạn muốn xác định rõ ràng loại tài liệu nào nên hoặc không nên đưa vào quá trình truy xuất,

lọc siêu dữ liệu là cách tiếp cận duy nhất có thể mang lại cho bạn hành vi đó.

Điều đó nói lên rằng, việc lọc siêu dữ liệu có những hạn chế đáng kể.

Nó không thực sự là một kỹ thuật tìm kiếm mà nó là một công cụ để tinh chỉnh kết quả của hai kỹ thuật còn lại mà bạn sẽ thấy trong mô-đun này.

Nó quá cứng nhắc, bỏ qua nội dung của tài liệu và thiếu bất kỳ cách xếp hạng tài liệu nào sau khi chúng đã vượt qua bộ lọc.

Mặc dù rất có thể hệ thống RAG mà bạn xây dựng sẽ bao gồm một số loại bộ lọc siêu dữ liệu,

việc xây dựng một công cụ truy tìm chỉ dựa vào tính năng lọc siêu dữ liệu về cơ bản là vô dụng.

Lọc siêu dữ liệu đơn giản và hiệu quả nhưng cần phải kết hợp với các kỹ thuật tìm kiếm khác để cung cấp giá trị thực.

Đặc biệt, bạn sẽ cần một cách để xác định xem nội dung của tài liệu có thực sự phù hợp với lời nhắc của bạn hay không.

Vì vậy, hãy cùng tôi xem video tiếp theo để xem tìm kiếm từ khóa giải quyết một số nhu cầu này như thế nào.
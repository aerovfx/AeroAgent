# 2 -Các thành phần xử lý trong langflow được dịch

---

Bây giờ, hãy xem lại các thành phần thuộc danh mục được gọi là xử lý.

Các thành phần này cho phép chúng ta thực thi một quy trình trong thành phần đó và chuyển đổi dữ liệu

trong một dòng chảy.

Bạn sẽ hiểu điều này một cách thực tế hơn.

Hãy bắt đầu với thành phần đầu tiên có tên là Dữ liệu kết hợp.

Thành phần này, như mô tả của nó cho biết, cho phép chúng ta kết hợp dữ liệu bằng các hoạt động khác nhau.

Ở đây chúng ta thấy nhiều loại hoạt động khác nhau mà chúng ta có thể thực hiện,

chẳng hạn như nối, nối thêm, trộn hoặc nối.

Nút này hoạt động như thế nào?

Bạn cần, như được chỉ ra ở đây, các nút thuộc loại dữ liệu đầu vào.

Hãy xem những nút nào chúng ta có thể sử dụng.

Ví dụ: chúng tôi nhận thấy rằng trong phần dữ liệu, có một số nút có thể hữu ích

cho mục đích này.

Ví dụ, để đặt ra, chúng ta có một vài thành phần của loại tệp.

Tôi sẽ chọn tập tin cho các thành phần này.

Tôi đã hoàn thành thông tin cho các tập tin.

Tôi sẽ thực hiện từng thành phần này một cách nhanh chóng.

Bạn có thể thấy rằng câu đầu tiên đề cập đến thông tin về tình trạng kiệt sức,

chúng tôi đã phân tích trước đây.

Nó kết thúc bằng dòng chữ bạn có thể nhìn thấy trên màn hình.

Trong khi thành phần thứ hai cho phép phân tích tin nhắn,

và bạn có thể thấy rằng về cơ bản đó là một vài lời nhắc có thể giúp chúng tôi tạo ra một số

hướng dẫn cho một thành phần mô hình AI.

Sau khi đã có 2 thành phần này mình sẽ tiến hành liên kết từng thành phần đó với Bộ kết hợp

Thành phần dữ liệu. Bây giờ, bạn có thể thấy loại nút này cho phép nhiều hơn một đầu vào.

Vì vậy, điều này có nghĩa là chúng ta có thể liên kết bao nhiêu thành phần tùy thích vào nút này.

Sử dụng thao tác nối, chúng ta sẽ bắt đầu thực thi thành phần.

Bạn có thể thấy rằng một hàng đã được tạo.

Hãy kiểm tra nội dung các bạn sẽ thấy nội dung của file TXT xuất hiện đầu tiên,

tiếp theo là phần về kiệt sức.

Do đó, như thao tác chỉ ra, thông tin từ cả hai tệp đang được nối

để tạo một bản ghi mới với tất cả dữ liệu đó.

Chúng ta có thể áp dụng bất kỳ thao tác nào trong số này tùy thuộc vào những gì chúng ta cần.

Tôi sẽ xóa các nút đó hoặc để nguyên như cũ.

Tiếp theo, bạn có thể thấy ở đây một nút có tên là,

hoặc một thành phần có tên là Văn bản kết hợp, cho phép chúng ta hợp nhất hai nguồn văn bản thành một bằng cách sử dụng

được phân cách cụ thể. Điều này có nghĩa là gì?

Hãy sử dụng hai nút nhập văn bản để xem thành phần này hoạt động như thế nào.

Tôi sẽ thêm chúng vào đây và gán cho trường văn bản đầu tiên giữa các con đường có chiều rộng,

xin chào, và đến thứ hai, ví dụ, giữa các con đường rộng, từ.

Khi chúng ta có cả hai thành phần, tôi sẽ kết nối chúng.

Dòng đầu tiên cho trường có nội dung, văn bản đầu tiên và dòng thứ hai cho trường có nội dung,

văn bản thứ hai. Bằng cách này, thông tin từ cặp thành phần này sẽ được nối với nhau.

Tiếp theo, chúng ta có thể định nghĩa một dấu phân cách. Ví dụ: hãy thêm một biểu tượng dạng ống.

Dấu phân cách sẽ chèn ký hiệu vào giữa cặp văn bản mà chúng ta đã chỉ định trước đó.

Chúng ta hãy xem điều này trong thực tế. Chúng ta hãy nhìn vào văn bản kết hợp. Như bạn có thể thấy, bây giờ chúng ta có

hợp nhất văn bản. Nhóc à, chúng ta có thể thấy biểu tượng mà chúng ta đã thêm vào và đó là cách thành phần này hoạt động.

Tiếp theo, chúng ta có các thành phần khác, chẳng hạn như thành phần này được gọi là dữ liệu vào khung dữ liệu, cho phép chúng ta

chuyển đổi một hoặc một số đối tượng dữ liệu thành một khung dữ liệu. Hãy nhớ rằng khung dữ liệu là một định dạng

giống như cái chúng ta thấy trong tệp này, trong đó thông tin phức tạp hơn dữ liệu. Dữ liệu là

thường là loại đầu ra đơn giản hơn, chẳng hạn như chứa thuộc tính văn bản và một số thuộc tính được xác định,

chẳng hạn như tên tệp, trong khi khung dữ liệu là một tập hợp các bản ghi phức tạp hơn cho phép chúng ta

xử lý thông tin. Vì vậy thành phần này cho phép chúng ta chuyển đổi một nút dữ liệu thành khung dữ liệu.

Trên thực tế, chúng ta có thể nhanh chóng kiểm tra điều này. Tôi sẽ vào thành phần tệp của mình và đính kèm đầu ra dữ liệu này

đến thành phần khung dữ liệu dữ liệu. Chúng tôi có thể chạy nó và như bạn thấy, chúng tôi đã có

chuyển đổi thành khung dữ liệu ở đây. Chúng tôi không có nhiều tài sản ở đây vì đầu ra của cái này

thành phần dữ liệu chỉ có một vài cột, vì vậy chúng tôi nhận được kết quả này như một phần của khung dữ liệu này.

Nhưng chúng ta cũng có thể thêm các loại văn bản khác, như chúng ta sẽ trình bày tiếp theo, bằng cách sử dụng các thành phần khác.

Tiếp tục với các ví dụ của chúng tôi. Ở đây chúng ta có một thành phần khác gọi là hoạt động khung dữ liệu,

cho phép bạn thực hiện các thao tác khác nhau trên khung dữ liệu. Hãy nhớ rằng, như tôi đã đề cập trước đây,

dữ liệu là một đối tượng gói gọn thông tin cá nhân, chẳng hạn như văn bản hoặc tài liệu,

trong khi khung dữ liệu là cấu trúc dạng bảng tổ chức và cho phép bạn thao tác nhiều

các yếu tố dữ liệu một cách có cấu trúc và tập thể. Điều này có nghĩa là gì? Hãy làm một việc thiết thực hơn

ví dụ để bạn có thể thấy các hoạt động của khung dữ liệu hoạt động như thế nào. Hãy thêm từ phần dữ liệu một thành phần

thuộc loại URL. Và chúng tôi sẽ sao chép một số URL từ tài liệu để cho bạn thấy nó hoạt động như thế nào.

Tôi sẽ gắn URL thứ hai từ một địa chỉ URL khác. Hãy thêm ba URL để chúng ta có thể

hình dung rõ hơn những điều này. Khi có ba URL này, chúng ta cần nối khung dữ liệu đầu ra từ

thành phần URL sẽ cung cấp cho chúng tôi thông tin về chúng. Và vì có thể thực hiện

nhiều thao tác khác nhau với khung dữ liệu, tại đây chúng ta có thể chọn hành động mà mình muốn thực hiện.

Bạn có thể thấy rằng hiện tại các URL, nếu chúng tôi chạy cụ thể thành phần này, bạn có thể thấy các URL

không theo thứ tự bảng chữ cái trong thuộc tính văn bản. Vì vậy, nếu chúng ta chuyển sang các thao tác khung dữ liệu và

chỉ định rằng chúng tôi muốn, chẳng hạn như sắp xếp dữ liệu của các URL, chúng tôi chỉ ra rằng điều đó nên làm

do đó thuộc tính được gọi là văn bản hoặc theo cột này được gọi là văn bản. Sau đó, nếu chúng ta chạy thành phần và

kiểm tra đầu ra, bạn sẽ nhận thấy rằng bây giờ chúng được sắp xếp tự động. Vì chúng tôi đã thêm

thành phần này cho phép chúng ta thực hiện các thao tác trên khung dữ liệu. Chúng tôi có các loại khác

các thao tác như xóa cột, lọc dữ liệu, đổi tên cột, thay thế các giá trị khác.

Đây là mục đích của thành phần hoạt động khung dữ liệu.

Chúng tôi cũng có các thành phần khác là một phần của quá trình xử lý. Chúng tôi có ba lựa chọn cho phép chúng tôi

để áp dụng các bộ lọc. Nếu chúng ta nhìn vào cái được gọi là dữ liệu bộ lọc, chúng ta sẽ thấy rằng nó cho phép chúng ta lọc

đối tượng dữ liệu đó dựa trên danh sách các khóa. Mục đích của thành phần này là cho phép bạn lọc

các thuộc tính hoặc các cột của một đối tượng. Ví dụ: tôi sẽ sao chép thành phần URL này và dán nó.

Tôi sẽ xóa hai URL này để chỉ để lại một. Tôi sẽ nhanh chóng chạy thành phần.

Hãy phân tích dữ liệu. Bạn có thể thấy thành phần này có các cột đầu ra là số.

Giả sử vì lý do nào đó, bạn chỉ cần trường văn bản hay cột văn bản?

Bạn cũng muốn nguồn hoặc URL gốc và thông tin của văn bản này?

Một cách để đạt được điều đó là chỉ định trong tiêu chí lọc các cột mà bạn quan tâm.

Đầu tiên tôi sẽ kết nối dữ liệu giữa các cặp thành phần rồi xác định rằng tôi muốn văn bản

và nguồn. Vì vậy, như một phần của tiêu chí lọc đầu tiên, tôi sẽ thêm tên của cột mà tôi

quan tâm. Tôi sẽ thêm một cột thứ hai gọi là nguồn. Hãy xem liệu điều này có hoạt động chính xác không.

Tôi chạy thành phần và nếu chúng tôi kiểm tra đầu ra, bạn có thể thấy một đối tượng trống xuất hiện.

Bây giờ, bạn có thể nghĩ rằng tính năng này đã ngừng hoạt động, nhưng thực ra phần mô tả chỉ ra rằng nó lọc

một đối tượng dữ liệu, nghĩa là một đối tượng dữ liệu duy nhất ở số ít. Vì vậy, thành phần URL này, nếu chúng tôi kiểm tra,

trả về một tập hợp các bản ghi. Hiện tại, chúng tôi chỉ thấy một, nhưng thực ra bản ghi này được chứa

trong một mảng bản ghi vì có thể có một hoặc nhiều hàng. Điều chúng ta cần làm bây giờ là

loại bỏ sự tham gia này mà chúng tôi đã có trước đây. Ngoài ra, chúng tôi còn có một số thành phần khác, như thành phần

được gọi là vòng lặp, cho phép chúng ta lặp lại tập hợp các phần tử khác. Trong trường hợp này, chúng tôi sẽ sử dụng

nó lặp lại một lần trên tập hợp các kết quả URL. Vòng lặp này sẽ đi qua một danh sách các đối tượng.

Trong trường hợp này là tập hợp các kết quả URL và nội dung của nó. Và chúng ta sẽ trích xuất thuộc tính này

hoặc không gọi là từng mục một bản ghi tại một thời điểm, đó là điều chúng tôi quan tâm.

Vì vậy, hãy kết nối đầu ra mục này với dữ liệu và bằng cách này chúng ta sẽ nhận được thông tin cho một

đối tượng dữ liệu duy nhất từ tập hợp các bản ghi này từ thành phần URL. Hãy thử nghiệm nó lần này.

Hãy nhìn vào kết quả. Bây giờ, bạn có thể thấy rằng lần này chúng ta đã in đậm một cách chính xác,

văn bản và nguồn, đây là hai thuộc tính mà chúng tôi muốn trích xuất từ ​​việc đọc URL

đầu ra. Ngoài ra, là một phần của các thành phần xử lý, chúng tôi tìm thấy một bộ lọc khác cho phép chúng tôi

chọn các giá trị. Ở đây, chúng ta có thể lọc bằng cách sử dụng khóa và giá trị cụ thể. Một yếu tố khác tôi

tôi thực sự thích thành phần được gọi là bộ lọc lambda, vì nó cho phép chúng ta sử dụng ngôn ngữ tự nhiên để

truy vấn dữ liệu đầu vào. Hãy kiểm tra thành phần này. Tôi sẽ sao chép thành phần URL chứa

ba địa chỉ bản vá và dán nó. Tôi sẽ kết nối các nút dữ liệu để tạo mối quan hệ trực tiếp.

Là một phần của bộ lọc lambda này, bạn có thể thấy nó chỉ ra rằng cần có LLM để tạo

hàm lambda lọc hoặc biến đổi dữ liệu có cấu trúc. Điều này có nghĩa là gì?

Chúng ta cần thêm một thành phần mô hình AI. Ví dụ, đây có thể là mô hình Grok,

một mô hình lambda, trong số những mô hình khác. Trong trường hợp của tôi, tôi sẽ sử dụng mô hình OpenAI mà chúng tôi đã sử dụng trước đây,

mà bạn đã biết nó hoạt động như thế nào và tất cả những gì bạn cần làm ở đây là chọn mô hình và

thêm khóa API OpenAI. Nhân tiện, tôi vẫn chưa chỉ cho bạn cách thêm biến toàn cục.

Bạn có thể làm điều này bằng cách nhấp vào nút này. Tại đây, bạn có thể thấy tập hợp các biến toàn cục.

Điều này đề cập đến điều gì? Đây là những biến bạn có thể sử dụng lại trong suốt quy trình công việc của mình.

Bạn có thể nhấp vào thêm biến mới và tại đây bạn có thể nhập tên bạn muốn sử dụng khi

bao gồm nó trong quy trình làm việc của bạn. Ví dụ: hãy thêm tên khóa OpenAI vào

tiếp theo là khóa được cổng OpenAI cung cấp cho bạn. Ở đây bạn cũng có thể chọn bất kỳ trường nào bạn

muốn thêm vào như một phần của khóa này. Trong trường hợp OpenAI, không cần thiết phải bổ sung thêm bất kỳ

trường, do đó bạn cũng có tùy chọn để thêm một số giá trị chung và khi bạn đã thực hiện xong việc đó,

bạn lưu biến. Bằng cách này, bạn sẽ có sẵn biến để chọn dễ dàng. Chỉ cần chọn cái này

nút và bạn đã tích hợp nó vào quy trình làm việc của mình. Khi bạn đã thiết lập nút OpenAI,

bạn nên tránh viết bất kỳ thông báo đầu vào hoặc hệ thống nào. Bạn chỉ cần kéo ngôn ngữ

nút mô hình, cho phép bạn kết nối một nút yêu cầu mô hình ngôn ngữ để sử dụng nút này

mô hình và khóa được chỉ định. Trong nội bộ, thành phần này sẽ xử lý tất cả các truy vấn cần thiết,

và đã có lời nhắc xác định trước cho phép bạn tạo trường Lambda ở đó.

Tất cả những gì bạn cần là dữ liệu thông tin, mô hình ngôn ngữ và hướng dẫn bạn muốn áp dụng

vào tập hợp các bản ghi đầu vào. Trong trường hợp của tôi, tôi đã viết sẵn lời nhắc mà bạn có thể thấy trên

màn hình. Lọc dữ liệu để chỉ bao gồm các hướng dẫn về cài đặt. Vì vậy, từ chuỗi URL này

hiển thị trên màn hình, chúng tôi sẽ kiểm tra xem có bất kỳ điều gì liên quan đến việc cài đặt hay không. Để làm cho nó nhiều hơn

thực tế, tôi sẽ đi tới phần cài đặt langflow, phần này giải thích cách cài đặt hệ thống này

trực tiếp hơn. Sau khi mọi thứ đã được cấu hình, tôi tiến hành bắt đầu thực thi thành phần này.

Bạn sẽ nhận thấy việc này sẽ lâu hơn một chút vì hướng dẫn đang được xử lý bằng AI

mô hình. Ở đây chúng tôi gặp phải một sự cố, vì vậy hãy chạy lại thành phần này. Trong trường hợp cụ thể này,

bạn có thể thấy một sự cố xảy ra, điều này thực sự tốt vì nó cho thấy rằng đôi khi mô hình AI không thể

tạo ra phản hồi mong đợi hoặc tạo ra kết quả đầu ra khác với những gì đã được lên kế hoạch.

Vậy chúng ta có thể làm gì trong những tình huống này? Một lựa chọn là cơ cấu lại các hướng dẫn

với công thức đã có sẵn. Nhưng chúng ta cũng có thể thay thế mô hình bằng một mô hình mạnh mẽ hơn. Ví dụ,

hãy thử GPD cho O. Có thể vào thời điểm bạn xem những chiếc xe này, cao cấp hơn và

mô hình cập nhật đã tồn tại. Bạn có thấy điều đó không? Trong trường hợp này, chúng tôi đã có phản hồi chính xác.

Nếu chúng tôi kiểm tra dữ liệu, bạn có thể thấy những dữ liệu này chỉ hiển thị bản ghi liên quan đến cài đặt langflow.

Các bản ghi khác liên quan đến vectơ được lưu trữ, một dự án viết blog và một người

phản hồi việc bắt đầu langflow đã bị bỏ qua vì chúng không được liên kết với quá trình cài đặt

một mình. Cái cuối cùng đã được bao gồm. Ba cái còn lại không liên quan đến việc cài đặt nên chúng đã được

được loại trừ, điều này giúp lọc dữ liệu đầu vào dễ dàng hơn. Chúng ta hãy tiếp tục khám phá

các thành phần trong danh mục xử lý nơi chúng tôi tìm thấy các phần tử hữu ích khác như

Bộ định tuyến LLM dành cho những người có tài khoản trên bộ định tuyến cao hơn. Điều này cho phép bạn chọn một mô hình AI

phù hợp theo thông số kỹ thuật của mô hình. Tôi thấy đây là một thành phần rất thú vị.

Chúng tôi cũng có một thành phần khác gọi là tin nhắn thành dữ liệu, cho phép bạn chuyển đổi tin nhắn hoặc

một đối tượng thông điệp thành một đối tượng dữ liệu. Chúng ta có thể nhanh chóng kiểm tra những điều này bằng cách viết tin nhắn. Ví dụ,

đây là một bài kiểm tra Bạn sẽ nhận thấy rằng sau khi chạy lệnh này, một kết quả đầu ra phức tạp hơn của

ống đối tượng dữ liệu được tạo ra, với một số tham số được hiển thị trên màn hình.

Chúng tôi cũng có thành phần tiếp theo được gọi là trình phân tích cú pháp, cho phép chúng tôi định dạng khung dữ liệu hoặc dữ liệu

đối tượng dưới dạng văn bản bằng cách sử dụng mẫu và bật tùy chọn có tên stringify để chuyển đổi đầu vào thành

một chuỗi văn bản. Trong trường hợp này, nếu bạn muốn sử dụng chế độ phân tích cú pháp, về cơ bản nó cho phép bạn trích xuất

thông tin từ một đối tượng giống như đối tượng hiển thị trên màn hình, hãy chọn một trường cụ thể để làm việc

chỉ dữ liệu đó và xử lý nó theo nhu cầu của bạn. Hãy kết nối các cặp thành phần này

và trong thành phần này được gọi là thông điệp dữ liệu tới dữ liệu, chúng ta thấy rằng chúng ta có một đầu ra. Ở đầu ra,

chúng tôi tìm thấy một thuộc tính được gọi là văn bản, mặc dù bạn có thể sử dụng bất kỳ thuộc tính nào trong số này để chứng minh hoặc kiểm tra chúng

thành phần. Trong trường hợp này, hãy tạm dừng việc muốn trích xuất thông tin từ thuộc tính này

gọi là văn bản. Vì vậy, điều chúng ta cần làm là điền vào mẫu bằng cách viết thuộc tính mà chúng ta quan tâm

bên trong niềng răng thuần túy. Ví dụ: ở đây chúng ta có thể thêm một thuộc tính khác là một phần của dữ liệu

chẳng hạn như người gửi. Hãy viết bên trong dấu ngoặc nhọn người gửi và đặt trước nó giải thưởng người gửi.

Điều này sẽ làm ở đầu ra là giữ nguyên văn bản này và chỉ thay thế văn bản bên trong

dấu ngoặc nhọn, ghi nhớ là một số biến được thay thế trong thời gian thực. Hãy kiểm tra xem nó hoạt động như thế nào.

Nếu mọi thứ đều chính xác, chúng tôi sẽ chạy thành phần đó và sau khi thay thế, bạn có thể thấy điều đó ở đây

văn bản nhận được từ tin nhắn đã xuất hiện dưới dạng văn bản và đối với người gửi, nó hiển thị đã biết vì không có

người gửi đã được tìm thấy. Bằng cách này, chúng ta có thể trích xuất thông tin từ dữ liệu đầu ra, điều này rất hữu ích khi chúng ta

có một đối tượng phức tạp và chỉ muốn có được một số thuộc tính nhất định. Trong danh mục này, chúng tôi có khác,

một số thành phần khác, chẳng hạn như thành phần được gọi là bộ trích xuất từ chối. Nó cho phép chúng ta nhập văn bản

chuỗi và sử dụng mẫu từ chối được gọi là loại chuỗi chúng ta có thể thêm để tìm kiếm mẫu

trong một chuỗi và trích xuất một chuỗi như số tệp. Chúng tôi có thể trích xuất phần mở rộng

của một tệp hoặc dữ liệu phức tạp hơn cũng như xác thực rằng một địa chỉ email hợp lệ trong số những địa chỉ khác.

Chúng tôi có các thành phần khác như thành phần này được gọi là lưu vào tệp, cho phép chúng tôi lưu thông tin

vào một tập tin văn bản. Chúng tôi cũng có một thành phần khác gọi là văn bản phân tách, rất hữu ích và

thú vị khi lưu trữ thông tin trong kho vector. Tại sao? Vì thành phần này cho phép

chúng tôi chia một văn bản rất lớn thành các phần nhỏ hơn để giúp việc tìm kiếm tiếp theo dễ dàng hơn. Làm sao chúng ta có thể

sử dụng nó? Giả sử chúng ta có một thành phần loại tệp ở đây. Tôi sẽ tải lên filebornout.pdf của mình

và khi tệp đã được tải lên, tôi sẽ kết nối dữ liệu với khung dữ liệu, đóng vai trò là

nút đầu vào cho một văn bản được phân chia. Khi việc này được thực hiện, với kết nối đã được thiết lập, ở đây chúng ta có thể

chỉ định phần chồng chéo, về cơ bản đề cập đến số lượng ký tự sẽ được chia sẻ

giữa các văn bản để duy trì tính liên tục. Vì vậy, văn bản không bị cắt đột ngột sau 200

nhân vật. Vì vậy, chúng ta sẽ kết hợp một phần văn bản vào từng phần đó.

Ngoài ra kích thước khối. Ở đây chúng ta có thể thấy thông tin về những gì thuộc tính này đề cập đến, đó là

về cơ bản là số lượng, độ dài tối đa cho mỗi đoạn văn bản. Và chúng tôi cũng có một số loại

dải phân cách có sẵn. Trong trường hợp chúng ta muốn thêm một cái để chia từng đoạn văn bản. Hãy thử nghiệm xem thế nào

thành phần đó hoạt động. Hãy phân tích đầu ra. Nhóc, chúng ta có một thuộc tính gọi là chunk, đó là

các đoạn văn bản. Bạn có thể thấy đoạn văn bản dài từ file pdf đã được chia thành

các đoạn khác nhau mà chúng ta có thể lưu trữ trong cơ sở dữ liệu để lấy thông tin khi cần.

Trên Node.deally, nó là một thành phần rất hữu ích. Cuối cùng, chúng ta có thành phần này được gọi là cập nhật

data, cho phép chúng tôi cập nhật động hoặc thêm dữ liệu vào một trường cụ thể. Chúng tôi có thể nhận được

văn bản đầu vào tại một số trường bổ sung và nhận được đầu ra mới. Như tôi đã đề cập trước đó,

chẳng hạn, chúng tôi có thể xử lý một nút dữ liệu để lọc thông tin và sau đó thêm một trường bổ sung

nếu chúng tôi cần nó, tùy thuộc vào yêu cầu của chúng tôi. Đây là những thành phần xử lý sẽ trở thành

rất hữu ích khi làm việc với Langflow.
# 8 -Workshop Tạo trình tạo bài đăng cho WordPress đã dịch

---

Nhưng bây giờ làm thế nào để sử dụng các công cụ trong Lancthlo.

Chúng tôi cũng biết cách tạo tác nhân, cách phát triển các luồng và các mẫu khác nhau mà chúng tôi có thể sử dụng

trong Lancthlo để thiết kế các chuỗi tác nhân sử dụng nhiều công cụ khác nhau.

Bây giờ chúng ta hãy chuyển sang một trường hợp thực tế.

Giả sử chúng ta muốn cho phép người dùng nhập lời nhắc hoặc hướng dẫn để

kết quả cuối cùng là một thẻ WordPress.

WordPress cho phép chúng tôi tạo một trang web hoặc blog nơi chúng tôi có thể xuất bản nội dung.

Bạn có thể thấy rằng chúng tôi có các thành phần hoặc phần khác nhau cho phép chúng tôi hiển thị thông tin

theo nhiều cách để sử dụng của chúng tôi.

Một trong những ưu điểm của WordPress là chúng ta có thể sử dụng thẻ để xây dựng loại trang web này.

Ý tôi là gì?

WordPress bao gồm một hệ thống gọi là Gutenberg cho phép chúng ta kéo hoặc tạo nhiều

blog để thiết kế một bài viết hoặc trang web.

Bạn có thể nhận thấy rằng nếu chúng ta sao chép một trong các thành phần, ví dụ như tiêu đề này,

thẻ được tạo như bạn có thể thấy trên màn hình.

Ở đây chúng tôi có văn bản thực tế, nhưng cả trước và sau chúng tôi đều tìm thấy các thẻ WordPress cho phép

chúng tôi định dạng một số phần nhất định của bài viết.

Chúng ta có thể thực hiện việc này với từng thành phần hoặc xem thông tin này cho từng thành phần.

Vì vậy, với thông tin này, chúng ta có thể sử dụng mô hình AIA để tạo hoặc tạo ra nội dung của

một blog.

Ngoài ra, chúng tôi cũng muốn tạo hình ảnh nổi bật cho bài đăng và trong

giống như cách chia số để nếu người dùng không muốn đọc bài viết và muốn nghe

với nó, họ có thể làm điều đó một cách dễ dàng.

Tôi sẽ thực hiện nhiệm vụ này trong langflow.

Để làm được điều này, tôi đã tạo luồng mới này và tác nhân này hay đúng hơn là chuỗi này sẽ là sự kết hợp

về những gì chúng tôi đã phân tích trước đây.

Thực ra đây là một mẫu được gọi là mẫu song song cũng được kết hợp với mẫu tuần tự

mẫu.

Hãy xem nó trông như thế nào.

Hãy bắt đầu bằng cách kéo một tác nhân vào langflow.

Hãy cấu hình nó để sử dụng GPT mini cho model cũ và hãy chỉnh sửa hướng dẫn

như bạn có thể thấy trên màn hình.

Tôi đã điều chỉnh lại một chút hướng dẫn này để bạn không gặp vấn đề gì khi sử dụng

dòng chảy này.

Ở đây về cơ bản nó nói rằng cần phải xác định một chủ đề dựa trên thông tin đầu vào của người dùng.

Hãy nhớ rằng người dùng sẽ nhập một cụm từ chẳng hạn như tạo một bài đăng về

bóng đá hoặc tạo một bài đăng về công thức nấu ăn cùng những người khác.

Vì vậy, mô hình AA xác định rõ nhất chủ đề tạo bàn phím được tối ưu hóa, tập hợp năm

các URL có thẩm quyền và cuối cùng trích xuất và tổng hợp các kết quả chính từ tìm kiếm đó.

Điều này có nghĩa là gì?

Về cơ bản nó có nghĩa là thực hiện tìm kiếm trên internet.

Để thực hiện hành động đầu tiên là tìm kiếm kết quả trên Google sẽ sử dụng thành phần

chúng tôi đã xem xét trước đây được gọi là API máy chủ Google.

Chìa khóa của ai chúng tôi đã lưu rồi.

Hãy nhớ rằng bạn có thể tạo một tài khoản miễn phí để cung cấp cho bạn các khoản tín dụng miễn phí để sử dụng trong việc này.

ví dụ.

Hãy cho biết rằng chúng tôi muốn chuyển đổi thành phần này thành một công cụ để kết nối nó với

người sẽ phụ trách phần nghiên cứu.

Hãy xác định rằng chúng tôi muốn nhận được năm kết quả từ tìm kiếm này và khi chúng tôi có ít nhất kết quả đó

của kết quả Google, bước tiếp theo sẽ là vào từng trang web và trích xuất những thông tin phù hợp nhất

thông tin từ mỗi trang.

Làm thế nào chúng ta có thể đạt được điều này?

Chúng tôi cũng đã thấy trước đây.

Có một dịch vụ tên là FireCroll cho phép chúng tôi trích xuất văn bản từ một trang web ở

Định dạng Martown.

Sau đó chúng ta kéo thành phần này.

Hãy lưu ý rằng chúng tôi cũng muốn biến nó thành một công cụ.

Bạn cũng phải nhập khóa API trong trường hợp bạn chưa có.

Chúng tôi sẽ để lại tất cả dữ liệu nhìn thấy và cuối cùng kết nối công cụ với đại lý chịu trách nhiệm

cho quá trình này.

Tôi sẽ tổ chức hai công cụ này tốt hơn một chút.

Bây giờ chúng ta sẽ tiến hành mô phỏng hoặc chạy flow này.

Chúng tôi sẽ nhập một đầu vào, một thành phần đầu vào trò chuyện hoặc trò chuyện và chúng tôi cũng sẽ kết nối một đầu ra trò chuyện

để xác minh rằng mọi thứ đều hoạt động chính xác.

Hãy bắt đầu trò chơi và nói với nó rằng chúng ta muốn có một bài đăng về năm địa điểm nên ghé thăm

ở Paris.

Khi chúng tôi thực hiện hướng dẫn đó, bạn có thể thấy rằng một bàn phím xuất hiện ở đây để tìm kiếm

sẽ được thực hiện bằng bàn phím trong trình duyệt Google.

Bạn có thể quan sát rằng công cụ sau hiện đang chạy, cung cấp cho chúng tôi một bộ trang web

với từng URL mà chúng tôi muốn điều tra.

Bước tiếp theo là trích xuất thông tin từ các trang web để có thêm dữ liệu và

có thể tạo đường dẫn chi tiết hơn hoặc giàu nội dung hơn.

Hãy đợi vài giây vì quá trình này có thể mất một chút thời gian.

Sau vài giây, chúng ta có thể thấy kết quả này cung cấp cho chúng ta thông tin hoặc bài đăng

về những địa điểm tham quan ở Paris.

Bạn có thể thấy rằng tất cả nghiên cứu này đã được hoàn thành bằng cách sử dụng các công cụ khác nhau tạo nên

đại lý.

Vì chúng ta đã có bài đăng chính nên bước tiếp theo là tạo hình ảnh do AI tạo cho

bài viết.

Làm thế nào để chúng ta đạt được điều này?

Tôi sẽ thêm một thành phần, ví dụ thành phần văn bản này và tôi sẽ chỉnh sửa văn bản hoặc nguồn

mã để bao gồm chức năng mà chúng tôi đã đề cập trong video trước cho phép chúng tôi sử dụng

dịch vụ để tạo ra một hình ảnh.

Bây giờ chúng ta sẽ tiến hành lưu các thay đổi.

Chúng tôi đã cấu hình thành phần này.

Hãy tạo hoặc kéo một tác nhân khác để công cụ tạo hình ảnh của chúng tôi có thể là một phần của tác nhân mới này

đại lý chúng tôi đã thêm.

Hãy chuyển đổi mô hình AI và cũng thay đổi hướng dẫn của tác nhân để cụ thể hơn,

chỉ ra rằng tác nhân này chịu trách nhiệm tạo hình ảnh cho một khối.

Vậy là tôi đã hoàn thành việc chỉnh sửa.

Bây giờ để dán tác nhân mới này một cách độc lập, tôi sẽ thêm một trường văn bản.

Điều này sẽ mô phỏng rằng chúng tôi đã tạo một bài đăng trên blog.

Tôi sẽ sao chép nội dung, xóa bản sao jugum và dán bất kỳ nội dung nào bạn muốn và tôi sẽ

kết nối nó với đầu vào của tác nhân để xem nó hoạt động như thế nào.

Hãy bắt đầu chạy đại lý.

Sau vài giây, hãy kiểm tra phản hồi.

Này nhóc, chúng ta có thể xem hình ảnh hoặc URL hình ảnh mà chúng ta quan tâm và chúng ta có thể xem nó trong

trình duyệt.

Này nhóc, chúng ta có hình ảnh này do Dali tạo ra.

Vì vậy, với điều này, chúng tôi xác nhận rằng tác nhân này đang hoạt động chính xác.

Những gì bạn có thể làm sau này là kết nối các công cụ khác có thể tạo hình ảnh với mô hình này

hoặc tới tác nhân cụ thể này, chẳng hạn như các trình tạo hình ảnh hoặc video khác.

Ví dụ: điều này sẽ phụ thuộc vào bạn và trường hợp sử dụng bạn muốn giải quyết.

Vì chúng tôi đã xác minh rằng những từ này là chính xác nên chúng tôi sẽ kết nối đầu ra của từ đầu tiên

tác nhân vào đầu vào của tác nhân này cho phép chúng ta tạo ra hình ảnh.

Bây giờ, bước tiếp theo là tạo một tác nhân khác cho phép chúng tôi tạo adioufai

từ bài đăng được tạo bởi tác nhân đầu tiên.

Làm thế nào để chúng tôi thực hiện được điều này?

Hãy tạo một phần khác.

Kid hãy kéo đặc vụ vào lần nữa nhé.

Hãy sửa đổi mô hình.

Bây giờ hãy thay đổi hướng dẫn.

Hướng dẫn này chỉ ra rằng tác nhân này chịu trách nhiệm tạo adioufai từ

một văn bản.

Một điều thực sự quan trọng ở đây là chúng tôi cũng đang xác định nên chọn cái tốt nhất

phong cách để tường thuật adiouf.

Và tại sao điều này lại xảy ra?

Chúng tôi sẽ sử dụng mô hình AIA có thể tạo ra cảm xúc cụ thể dựa trên chi tiết

hướng dẫn.

Tôi sẽ kéo một thành phần nhập văn bản khác vào và sửa đổi nó.

Vì tôi muốn sử dụng dịch vụ OpenAA cho phép chúng tôi tạo giọng nói từ văn bản.

Đây là mã tương ứng là một phần của kết quả biên dịch.

Lần này chúng tôi đang sử dụng dịch vụ cho phép chúng tôi tạo tệp MP3 từ văn bản.

Nhưng đó không phải là tất cả.

Chúng tôi cũng đang sử dụng một dịch vụ có tên thempfai.org cho phép chúng tôi tải adioufai lên.

Vì API trả về tệp MP3 và nó được lưu trên máy chủ.

Nhưng chúng tôi muốn giải nén hoặc tải tệp đó lên theo cách nào đó để có thể truy cập và hiển thị

nó dễ dàng hơn, giúp việc tạo tư thế WordPress trở nên đơn giản hơn.

Đó là lý do tại sao chúng tôi sử dụng dịch vụ này và tải lên tệp MP3 đã tạo để cung cấp

dưới dạng URL công khai.

Mã này sẽ có sẵn trong số các tài nguyên đính kèm bài học.

Vì vậy, tôi đã lưu các thay đổi.

Bây giờ chúng ta đã có thành phần sẵn sàng và ở đây chúng ta có thể cấu hình mô hình.

Cái bao gồm cảm xúc là cái kết thúc bằng Minity.ts.

Chúng tôi có thể chọn một giọng nói khác nếu bạn thích và hướng dẫn sẽ được tạo bởi

bản thân đại lý.

Bây giờ, hãy biến thành phần đó thành một công cụ và chỉ ra rằng nó sẽ là một phần của công cụ này

đại lý.

Một lần nữa, tác nhân này có thể được sửa đổi để sử dụng một dịch vụ cụ thể khác nếu bạn muốn.

Trong trường hợp của tôi, nó chỉ có sẵn một công cụ.

Chúng ta có thể kiểm tra tác nhân này bằng cách nhập bất kỳ văn bản nào, ví dụ: HelloWorth.

Hãy bắt đầu thực hiện tác nhân.

Ở đây chúng tôi có một đầu ra.

Hãy xem lại kết quả đầu ra và nhận thấy rằng hiện tại chúng ta có một URL hợp lệ trỏ đến tệp MP3.

Một điều quan trọng cần biết về dịch vụ này là nó chỉ giữ các tập tin trong khoảng

một giờ.

Vì vậy, bạn thường cần tải xuống tệp này để thực hiện một hành động khác mà chúng tôi sẽ thực hiện trong phần sau.

bước sau.

Chúng tôi sẽ đóng thiết lập này và bây giờ chúng tôi đã có tác nhân thứ hai.

Hay đúng hơn là đặc vụ thứ ba này.

Tiếp theo, chúng tôi sẽ kết nối đầu ra của tác nhân đầu tiên với đầu vào văn bản của tác nhân này mà chúng tôi

vừa tạo, chịu trách nhiệm tạo tệp MP3.

Vì các tác nhân này đã sẵn sàng nên bước tiếp theo là chuyển đổi văn bản hoặc đầu ra của bài đăng

vì như bạn đã nhớ, chúng tôi hiện có mã ở định dạng Martaun, không thể sử dụng lại

trực tiếp trong WordPress vì nó sẽ chỉ sao chép văn bản.

Những gì chúng ta cần làm là áp dụng các thẻ cụ thể của WordPress để đạt được một số định dạng.

Trong trường hợp cụ thể này, không cần thiết phải tạo một tác nhân vì chúng tôi muốn sử dụng tác nhân bên ngoài

công cụ.

Điều chúng tôi muốn là chính mô hình tác nhân định dạng văn bản đầu vào để thêm các thông tin cần thiết

thẻ.

Vì vậy, điều chúng ta cần làm là thêm một thành phần loại AI mở.

Bạn không thể tiếp cận mọi người bạn thích.

Tôi sẽ sửa đổi thông báo hệ thống và về cơ bản những gì tôi đang nói ở đây là

thành phần hoặc mô hình này là một chuyên gia trong việc tạo các bài đăng WordPress bằng thẻ.

Điều tôi đang trình bày cho người mẫu là tôi đang trình bày một số ví dụ về cách sử dụng thẻ

để tạo một bài đăng WordPress hợp lệ.

Hãy tiến hành chỉnh sửa hoàn tất.

Hãy thay đổi mô hình thành GPT cho Omini và tiếp theo, kết nối đầu ra của tác nhân đầu tiên,

tạo bài đăng vào đầu vào của thành phần AI mở này để thêm các thẻ cần thiết.

Bây giờ chúng ta đã có tất cả các phần tử, mục tiêu của chúng ta là tạo một mẫu hiển thị

đăng bài với thẻ WordPress.

Chúng tôi cũng muốn hiển thị hình ảnh nổi bật và cuối cùng là tệp âm thanh.

Làm thế nào chúng ta có thể tích hợp tất cả thông tin này?

Như bạn có thể nhớ, có một thành phần được gọi là nhắc nhở nơi chúng ta có thể thêm tất cả các biến

chúng tôi muốn.

Hãy sửa đổi lời nhắc này và trong trường hợp của tôi, điều tôi làm là tập hợp tất cả các điểm lại với nhau.

Cho biết cái nào là bài viết hay nội dung, cái nào là file âm thanh và cái nào là

hình ảnh đặc trưng.

Với điều này, giờ đây chúng ta có ba nút mà chúng ta có thể kết nối với thông tin.

Nút đầu tiên tương ứng với nội dung sẽ được lấy từ nút này được gọi là

OpenAI mà chúng tôi đã tạo gần đây.

Đầu ra của ai là văn bản được định dạng bằng thẻ WordPress.

Tiếp theo, hình ảnh nổi bật được lấy từ tác nhân thứ nhất hoặc đúng hơn là từ tác nhân thứ hai

tác nhân, là tác nhân được kết nối với trình tạo hình ảnh Danyi.

Vì vậy, tôi sẽ kết nối đầu ra này với đầu vào hình ảnh nổi bật và cuối cùng là URL tương ứng

vào tệp âm thanh, sẽ được kết nối với tác nhân chịu trách nhiệm tạo âm thanh

tập tin.

Hãy kết nối nó và bây giờ chúng ta đã có tất cả các thành phần được kết nối để tạo WordPress

bài đăng, hình ảnh nổi bật và tập tin âm thanh.

Hãy tiến hành dán quy trình làm việc.

Chúng tôi sẽ kết nối thành phần cuối cùng, đầu ra trò chuyện, để đảm bảo mọi thứ hoạt động chính xác

và kiểm tra toàn bộ quy trình làm việc.

Bây giờ chúng ta hãy đến khu vui chơi nhé.

Chúng tôi sẽ tạo một phiên mới và yêu cầu phiên đó tạo một bài đăng về một chủ đề cụ thể.

Trong phiên này, chúng tôi sẽ bắt đầu quy trình hoặc quy trình làm việc mà chúng tôi đã tạo trước đó.

Trong Lightflow, thật thú vị khi xem trực tiếp việc thực hiện một nhiệm vụ khác

trên vải.

Bạn có thể thấy rằng chúng tôi thực hiện song song ở đây.

Đó là lý do tại sao tôi đã đề cập rằng tác nhân này đưa ra một mức độ song song nhất định vì tất cả

ba nhiệm vụ chạy đồng thời.

Hình ảnh được tạo, tệp âm thanh được tạo và bài đăng WordPress có thuế được xuất bản.

Tất cả những điều này xảy ra từ người đại diện đầu tiên này, người đã thực hiện hoặc nên thực hiện bước đầu tiên.

nghiên cứu bằng hai công cụ chúng tôi đã đề cập.

Hãy quay lại sân chơi và xem kết quả.

Sau vài phút, chúng ta có thể thấy kết quả đầu ra như một phần của quy trình làm việc mà chúng ta đã thực hiện.

được tạo ra.

Tuy nhiên, bạn có thể nhận thấy một số khác biệt hoặc một số vấn đề nhất định với kết quả mà chúng tôi nhận được.

Đầu tiên, chúng tôi không có hình ảnh nổi bật đã được tạo.

Chúng tôi có liên kết tới tệp âm thanh mà bạn có thể truy cập và nghe tại đây, nhưng

hình ảnh đặc trưng được gửi hiển thị.

Một điểm khác tôi muốn nhấn mạnh là thông tin về trình soạn thảo WordPress là

được tạo ra mà không nên xảy ra.

Có một cách đơn giản để ghi lại những gì đã xảy ra trong quy trình làm việc này.

Chỉ cần thay thế đầu ra từ tác nhân đầu tiên để mở giao diện người dùng để kiểm tra phản hồi nào

đã được nhận.

Nếu chúng ta đến đại lý đầu tiên và xem xét các phản hồi, chúng ta có thể thấy đại lý đã bị dừng vì

đã đạt được số lần lặp tối đa.

Và để tránh việc lặp lại dư thừa khi mô hình AI giải quyết chính xác vấn đề của người dùng

ý định, hãy lưu ý rằng trong phần điều khiển có một số tham số bổ sung.

Một trong số đó là số lần lặp tối đa giới hạn số lần yêu cầu có thể được xử lý.

để ngăn chặn các vòng lặp vô hạn và do đó không sử dụng hết tất cả các cấp độ của mô hình AI mà chúng tôi đang có

sử dụng trong trường hợp này từ việc mở giao diện người dùng.

Chúng tôi muốn phân tích nút này đang trả về cái gì hoặc cái gì đang được tạo và chuyển đến

Nút OpenAI.

Bởi vì nếu chúng ta kiểm tra tin nhắn ở đây, bạn có thể thấy vấn đề bắt đầu từ đâu,

khi nó bắt đầu tạo ra thông tin không liên quan đến lịch sử của Ferrari, vốn đã

văn bản chúng tôi đã nhập.

Để xem kết quả do một nút tạo ra, chúng ta có thể sử dụng một trong các nút mà chúng ta đã xem xét trước đó,

được tìm thấy trong phần có tên Logic.

Ở đây chúng ta thấy nút này được gọi là Pass, cho phép truyền và nhập tin nhắn mà không cần sửa đổi

nó.

Nút này, mặc dù có vẻ không hữu ích lắm khi được sử dụng trong một luồng, nhưng thực tế có thể cung cấp

chúng tôi với thông tin về những gì xảy ra giữa hai thành phần.

Trong trường hợp này, hãy xem thành phần này đang nhận được đầu ra gì hay đúng hơn là đầu ra là gì

tạo đại lý đầu tiên và tại sao điều này không cung cấp thông tin chính xác như một phần

của quá trình này, thành phần được gọi là OpenAI.

Hãy tiến hành chạy lại hướng dẫn.

Bây giờ chúng ta đã có phản hồi được tạo, lần này chúng ta thấy rằng chúng ta đã có một bài đăng chính xác.

Chúng ta có thể thấy rằng hình ảnh đặc trưng ở đây và cả quảng cáo.

Nhưng ở đây chúng ta có một vấn đề, vì bạn có thể thấy rằng bài viết đang được lặp lại hai lần.

Vì vậy, chúng ta có thể thấy điều gì đó xảy ra ở hậu trường, mặc dù phản hồi hơi

tốt hơn trước.

Khi chúng tôi kiểm tra đầu ra từ thành phần đường dẫn này, chúng tôi thấy kết quả chỉ ra rằng bài đăng

đã được tạo thành công, nhưng với cấu hình xử lý, điều này có thể chỉ hoạt động với một

trong số 10 lần chẳng hạn.

Để giải quyết vấn đề này, một tùy chọn là chỉ định rằng tác nhân này sử dụng phức tạp hơn

công cụ hơn thành phần này, nên sử dụng mô hình khác và mạnh hơn, chẳng hạn như GPT-4.1

mô hình, một trong những mô hình chữa bệnh và tiên tiến nhất.

Vì vậy, khi chúng ta đã thay đổi tham số này, hãy chạy lại tham số này.

Lời nhắc này nhằm mục đích tạo một bài đăng về Ferrari và lịch sử của hãng.

Và với điều đó, chúng ta có thể thấy kết quả.

Sau vài phút, chúng ta có thể thấy rằng chúng ta đã thu được kết quả.

Chúng tôi quan sát thấy một số thành phần trong kết quả đầu ra mà chúng tôi nhận được, chẳng hạn như adiify, mà chúng tôi có thể

tải xuống từ URL hiển thị ở đây.

Chúng ta cũng thấy hình ảnh nổi bật đã được tạo và cuối cùng là bài đăng có

được tạo ra nhờ vào tất cả các thông tin và nghiên cứu được thực hiện thông qua các phương pháp khác nhau

dịch vụ.

Đây là cách chúng tôi có thể có được tất cả thông tin cần thiết để tạo một bài đăng WordPress mới.

Chúng ta sẽ có hình ảnh nổi bật, adiophile và cả bài đăng hoặc nội dung bài đăng.

Lab này kết thúc, tôi hy vọng bạn thích nó và nó giúp bạn hiểu rõ hơn

cách sử dụng đại lý.
# 002 Lập trình cập nhật chương trình cơ sở OTA Phần I vi

---

Chúng ta sẽ bắt đầu phần cập nhật OTA bằng cách xác định một số định nghĩa trạng thái liên quan đến việc liệu

bản cập nhật đang chờ xử lý, thành công hay không thành công và chức năng JavaScript của chúng tôi để nhận trạng thái

đã được chuẩn bị để phản ứng với những trạng thái này.

Vì vậy, chúng ta hãy đi tới tập tin nhạc jazz và xem qua.

Và ở đây ở trạng thái tốt là chức năng, nó cho biết nếu quá trình xả đã hoàn tất, trạng thái sẽ là một trạng thái khác,

đó là một điều tiêu cực.

Và ở đây chúng ta có tình huống thành công.

Và tình huống bất thành là ngay tại đây.

OK, vì vậy chúng ta cần gửi các trạng thái tương ứng ở phía máy chủ web để chức năng JavaScript này

phản ứng theo cách thích hợp.

Vì vậy bây giờ chúng ta hãy đi tới phần đầu của tập tin.

Và ở đây sẽ xác định bản cập nhật OTA đang chờ xử lý.

Như số không.

Và sau đó xác định.

Cập nhật OTA thành công.

Là một.

Và bây giờ hãy xác định cập nhật OTA không thành công.

Như một tiêu cực.

Ngoài ra, chúng ta thực sự không cần trạng thái less enum ở đây, vì vậy hãy loại bỏ nó.

Và trong file C chúng ta hãy loại bỏ cả case cho nó nhé.

OK, bây giờ hãy quay lại phần đầu của tập tin.

Hãy xác định chức năng gọi lại hẹn giờ.

Cuộc gọi khởi động lại ESP sau khi cập nhật chương trình cơ sở thành công.

Và ở đây sẽ nói cập nhật firmware, thiết lập lại, gọi lại.

Và nó cần một đối số con trỏ void.

ĐƯỢC RỒI.

Và hãy thực sự đặt tên cho nó một cách chính xác tại máy chủ HTP.

Được rồi, tốt hơn rồi.

Bây giờ chúng ta sẽ đi tới tập tin xem.

Và bao gồm.

ESP lên sân khấu.

Và đó là dành cho các chức năng OTA.

Và cũng bao gồm chương trình gạch chéo này, Dot H.

Và đó là dành cho macro đàn ông của chúng tôi.

Và sau đó chúng tôi muốn tạo một biến chung cho trạng thái cập nhật chương trình cơ sở.

Đó là một int tĩnh gọi nó là phần mềm gạch dưới toàn cầu, cập nhật gạch dưới, trạng thái gạch dưới

và đặt nó ở trạng thái chờ cập nhật OTA.

Và bây giờ hãy sao chép biến này và đưa nó lên màn hình theo bản cập nhật OTA thành công.

Và chúng ta hãy thiết lập là cập nhật OTA thành công.

ĐƯỢC RỒI.

Và sau đó cập nhật OTA không thành công, hãy đặt thành cập nhật OTA không thành công.

Vì vậy, bây giờ ở Mỹ, hãy xem chúng ta cần xác định những trình xử lý nào.

Trong bản cập nhật firmware.

Chúng tôi có một bài viết để cập nhật OTA.

ĐƯỢC RỒI.

Và khi trang Web được truy cập, trạng thái cập nhật được gọi.

Và ở đó chúng ta có trạng thái bị lãng quên.

Và đó cũng là một phương pháp đăng bài.

Vì vậy ở đây chúng ta phải đăng phương pháp cập nhật OTA và trạng thái OTA để xử lý.

Vì vậy, hãy quay trở lại tập tin C.

Và tùy thuộc vào người xử lý bạn hoặc tôi của chúng tôi.

Được rồi, vậy hãy vào đây đăng ký nào.

Trình xử lý cập nhật OTA.

Và chúng ta cần một phiên bản của đồng euro, một cấu trúc và gọi nó là cập nhật gạch dưới.

Và bạn đã đúng.

Sẽ được chuyển tiếp cập nhật OTA.

Và phương pháp sẽ là một bài viết hàng đầu.

Và trình xử lý sẽ gọi trình xử lý cập nhật OTA của máy chủ HTTP.

Và chúng tôi có thể thiết lập cho người dùng biết.

ĐƯỢC RỒI.

Sau đó gọi FTPd, đăng ký bạn hoặc người xử lý sâu bệnh để xử lý.

Và sau đó là tham chiếu đến cấu trúc cập nhật OTA.

ĐƯỢC RỒI.

Bây giờ sẽ đăng ký xử lý trạng thái.

Và gọi nó là một trạng thái.

Và vì điều đó, bạn nói đúng, đó sẽ là trạng thái OTA chuyển tiếp.

Và sau đó phương thức cũng sẽ là http post.

Và người xử lý.

Chúng tôi sẽ gọi máy chủ HTP, trình xử lý trạng thái OTA.

CTC của người dùng hiện đã có.

Và sau đó chúng ta sẽ đăng ký trình xử lý.

Truyền phần điều khiển và tham chiếu đến cấu trúc rái cá.

Được rồi, tiếp theo, hãy xác định trình xử lý cập nhật OTA.

Và hãy bình luận ở đây, nhận file bin.

Thông qua trang Web và xử lý việc cập nhật firmware.

Và tham số R e q là yêu cầu HTTP mà bạn đúng cần được xử lý.

Và sự trở lại là OK.

Ngược lại, PSG sẽ thất bại nếu hết thời gian chờ và không thể bắt đầu cập nhật.

Và kết quả trả về là loại lỗi ISP và đó là trình xử lý cập nhật OTA của chúng tôi, đưa con trỏ tới HTTP

loại yêu cầu và đó là RFQ.

Và ở đây chúng ta cần một thể hiện của cấu trúc điều khiển ELISpot.

Và chúng ta sẽ gọi nó là Otere Handle.

Và tiếp theo, chúng ta cần một bộ đệm để chứa dữ liệu nhận được từ trang Web, nên nói Char là bộ đệm và nó là

1024 byte.

Ngoài ra, chúng ta cần một biến để giữ độ dài nội dung.

Vì vậy, nói về chiều dài nội dung.

Bằng độ dài nội dung yêu cầu và chúng tôi có thể truy cập như vậy.

Ngoài ra, chúng ta cần theo dõi nội dung nhận được.

Và đặt nó về 0.

Và hãy thêm một biến khác để nhận dữ liệu từ mỗi hàm yêu cầu HTP, gọi và gọi nó và

để nhận được chiều dài.

Ngoài ra, chúng tôi cần một biến để cho chúng tôi biết khi tìm thấy nội dung tệp cập nhật chương trình cơ sở thực tế.

Vì vậy, chúng tôi sẽ nói Bull là yêu cầu, nhưng đã bắt đầu.

Và đặt nó thành sai.

Ngoài ra, chúng ta cần kiểm tra trạng thái xác thịt, gọi là xác thịt này thành công và đặt thành sai.

OK, bây giờ chúng ta cần một phiên bản của cấu trúc phân vùng ESP và đó là một con trỏ tới một phân vùng ESG không đổi

loại.

Và gọi nó là phân vùng cập nhật.

Bằng với kết quả của ESPN để nhận phân vùng cập nhật tiếp theo.

Và tham số là không.

ĐƯỢC RỒI.

Và nếu chúng ta làm theo chức năng này.

Chúng ta có thể thấy rằng nó trả về phân vùng ứng dụng OTA tiếp theo, phân vùng này sẽ được viết bằng phần sụn mới

và gọi hàm này để tìm phân vùng ứng dụng OTA, phân vùng này có thể được chuyển tới SPRO để bắt đầu.

Vì vậy, tiếp theo, hãy tạo một vòng lặp do while để nhận tệp cập nhật.

Và đó là trong khi nhận được chiều dài.

Lớn hơn 0 và nội dung đã nhận được.

Nó nhỏ hơn độ dài nội dung.

ĐƯỢC RỒI.

Và điều đầu tiên chúng ta sẽ làm ở đây là đọc dữ liệu cho yêu cầu.

Và nói, nếu nhận được chiều dài.

Bằng các yêu cầu HTTP nhận được.

Và tham số đầu tiên là Ari.

Q Thứ hai là bộ đệm.

Và thứ ba là mức tối thiểu giữa độ dài nội dung.

Và kích thước của bộ đệm.

Và nếu kết quả này nhỏ hơn 0.

Khi đó chúng ta cần xử lý trường hợp lỗi hết thời gian chờ ở đây.

Vì vậy, hãy kiểm tra xem thời gian chờ có xảy ra hay không.

Và sau đó chúng tôi sẽ đúng nếu nhận được độ dài.

httpd có bị hết thời gian phát sóng không?

Sau đó chúng tôi sẽ gửi một tin nhắn.

Bản cập nhật OTA xử lý chức năng này.

Đã trải qua thời gian chờ của ổ cắm.

Và sau đó, hãy nói tiếp tục.

Và chúng tôi sẽ đến và thử nhận lại nếu hết thời gian chờ.

Nếu không chúng ta có thể ghi lại một tin nhắn.

Rằng có một số lỗi khác.

Vì vậy, chúng tôi sẽ nói rằng trình xử lý cập nhật OTA, lỗi khác của OTA.

Và chúng tôi thực sự có thể in độ dài nhận được.

OK, vậy tại thời điểm này, chúng ta có thể trả về ESP thất bại.

Được rồi, bây giờ chúng ta có thể tiếp tục.

Và ở đây hãy in.

Hãy in ra rằng trình xử lý cập nhật OTA đã nhận được một số byte nội dung.

Và chúng tôi sẽ cung cấp cho nó nội dung nhận được theo độ dài nội dung.

Được rồi, sau đó chúng ta có thể kiểm tra.

Đây có phải là dữ liệu đầu tiên chúng tôi nhận được?

Nếu vậy.

Nó sẽ có thông tin trong tiêu đề mà chúng ta cần.

Và trước hết, hãy nói nếu nội dung yêu cầu chưa được bắt đầu.

Sau đó, chúng tôi sẽ đặt nội dung yêu cầu bắt đầu thành đúng.

Và sau đó chúng ta sẽ đến đây và lấy vị trí của -- nội dung.

Ý nghĩa sẽ xóa dữ liệu biểu mẫu Web khỏi yêu cầu.

OK, vậy bây giờ giả sử cha trỏ đến phần bắt đầu của phần thân gạch dưới P bằng chuỗi chuỗi của bộ đệm Otere.

Và chúng ta cần tìm những dấu gạch chéo này hoặc gạch chéo và gạch chéo hoặc gạch chéo và.

Và sau đó tăng lên điểm hai đến bốn.

Về độ dài của dấu gạch chéo hoặc phần cuối của dấu gạch chéo.

Được rồi, bây giờ chúng ta sẽ có chiều dài toàn bộ phần cơ thể.

Từ chiều dài nhận được.

Trừ đi sự khác biệt giữa điểm bắt đầu cơ thể.

Và sự khởi đầu của bộ đệm Otay.

Được rồi, vậy ở đây chúng ta cần lấy điểm bắt đầu của phần thân để trỏ đến điểm bắt đầu của dữ liệu mà chúng ta

muốn không có dữ liệu rác dưới dạng web.

Và chúng tôi cũng cần độ dài dữ liệu mà chúng tôi muốn để có thể chuyển thông tin này nhằm phát hiện quyền

và chúng ta sẽ làm điều đó sau.

Được rồi, tiếp theo, hãy in một số thông tin.

Về kích thước tệp OTA để nó hiển thị khi chúng tôi đang nhận tệp.

Và cung cấp cho nó độ dài nội dung.

Và ở đây chúng ta có thể nói lỗi loại lỗi ESP.

Bằng ESP để bắt đầu.

Và cung cấp cho nó phân vùng cập nhật và sau đó là kích thước tệp.

Kích thước không rõ.

Và sau đó đưa ra một tài liệu tham khảo cho du thuyền để xử lý.

Được rồi, chúng tôi sẽ nói nếu lỗi không bằng ESP, được chứ?

Sau đó in ra có lỗi.

Và chúng ta sẽ nói không khí với OK để bắt đầu.

Đang hủy OTA.

OK, sau đó quay lại, ESB thất bại.

Được rồi, vậy chúng ta sẽ nói khác.

Và sau đó chúng tôi sẽ in ra nội dung mà chúng tôi đang viết cho các chính trị gia.

Sẽ nói viết thư cho các chính trị gia tiểu loại.

Bù lại.

Và cung cấp loại phụ phân vùng cập nhật.

Và địa chỉ phân vùng cập nhật.

Vậy bây giờ hãy nói.

Đúng, phần đầu tiên này.

Của dữ liệu.

Và nói địa điểm, phải không?

Sau đó chuyển sang xử lý.

Cơ thể bắt đầu điểm tới.

Và chiều dài phần cơ thể.

Và sau đó chúng ta sẽ nói khác.

Trong trường hợp dữ liệu về cơ thể đã được tìm thấy và đó không phải là phần đầu tiên của dữ liệu mà chúng tôi

được nhận và viết bằng dấu chấm, đúng, và sau đó chúng ta muốn viết một dữ liệu.

Vì vậy hãy bình luận.

Phải.

Một dữ liệu.

Và chúng ta sẽ sử dụng SBO để viết.

Sau đó chuyền qua tay cầm du thuyền và lần này cho du thuyền một tấm đệm.

Và chúng tôi muốn độ dài nhận được lần này.

Và bây giờ chúng tôi muốn tăng nội dung nhận được.

Theo chiều dài nhận được.

Vì vậy, chúng ta sẽ thực hiện việc này khi độ dài nhận được lớn hơn 0.

Và nội dung nhận được nhỏ hơn độ dài nội dung khi chúng tôi tăng dần nội dung nhận được

với mỗi cuộc gọi để nhận dữ liệu.

Vì vậy, khi đã xong, chúng ta có thể nói liệu đoạn quảng cáo đó có kết thúc hay không.

Trong vượt qua tay cầm.

Và nếu điều đó trả về, ESP, được.

Sau đó hãy cập nhật phân vùng.

Và đúng rồi, nếu anh ấy nói đặt phân vùng khởi động và cung cấp cho nó phân vùng cập nhật.

Nếu đó là ESP thì được chứ?

Sau đó là loại phân vùng Konst ESP.

Phân vùng khởi động con trỏ.

Bằng vị trí để có được phân vùng khởi động.

Và bây giờ hãy ghi lại thông tin về phân vùng khởi động tiếp theo.

Và nói kiểu con phân vùng khởi động tiếp theo.

Đó có phải là sự bù đắp?

Và sau đó cung cấp kiểu con phân vùng khởi động.

Và địa chỉ phân vùng khởi động.

OK thì đặt xác thịt thành công thành true.

Nếu không, chúng tôi cần ghi lại một lỗi có nội dung lỗi xác thực.

Vì vậy, hãy đăng nhập về chức năng này.

Và chúng tôi sẽ nói lỗi xác thịt.

Và sau đó nếu thể thao điện tử kết thúc không suôn sẻ.

Chúng tôi cũng có một lỗi.

Và đó là chương trình phát sóng từ ESPN và.

Được rồi, và cuối cùng, chúng tôi muốn cập nhật các biến toàn cục trong toàn bộ tệp.

Vì vậy, hãy gửi một tin nhắn về trạng thái.

Và chúng ta có thể nói, nếu xác thịt thành công.

Và sau đó chúng ta có thể gửi một dòng tin nhắn theo dõi máy chủ HTTP này.

Cập nhật OTA tin nhắn HTP thành công.

Khác.

Chúng tôi sẽ gửi tin nhắn.

Cập nhật OTA tin nhắn http đó không thành công.

Được rồi.

Và bây giờ chúng ta có thể trả lại ESP, được chứ?

ĐƯỢC RỒI.

Làm tốt lắm, chúng ta còn một chút việc phải làm, nhưng tôi nghĩ bây giờ đã đủ thời gian.

Vì vậy chúng ta hãy nghỉ ngơi một chút và tiếp tục học bài tiếp theo.
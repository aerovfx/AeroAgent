# 61 - Tiếng Anh Tensorboard

---

Chào mừng mọi người quay trở lại, để hoàn thành phần này của khóa học, chúng ta sẽ thảo luận ngắn gọn về Tensas

bảng.

Ban kiểm duyệt là một công cụ trực quan của Google được thiết kế để hoạt động cùng với Tensor Flow nhằm

hình dung các khía cạnh khác nhau của mô hình của bạn.

Ở đây, chúng ta sẽ hiểu đơn giản cách xem bảng điều khiển Tensas trong trình duyệt của mình và phân tích bảng điều khiển hiện có

mô hình, một lưu ý thực sự quan trọng ở đây là bài giảng này yêu cầu bạn phải hiểu đường dẫn tệp

và vị trí hiện tại của sổ ghi chép mà bạn đang làm việc hoặc tệp DCPI của bạn.

Vì vậy, hãy ghi nhớ điều đó.

Chúng tôi đã ôn lại một số chủ đề này bằng bút, bài giảng đầu vào đầu ra này.

Vì vậy, bạn có thể muốn xem lại điều đó.

Bây giờ, hãy nhớ rằng, về mặt kỹ thuật, ban kiểm duyệt là một thư viện riêng biệt với luồng Tenzer, vì vậy anh ấy không

sử dụng tập tin môi trường của chúng tôi.

Bạn có thể cần cài đặt pip hoặc cài đặt bảng kiểm duyệt ngoài luồng Tenzer.

Nếu bạn đang sử dụng sổ ghi chép cộng tác của Google trực tuyến, hướng dẫn chính thức của Google thực sự có một sổ ghi chép được tạo sẵn

bạn chỉ cần chạy tất cả các ô và nó sẽ tự động upload bảng kiểm duyệt cho bạn.

Tôi có URL ở đây, nhưng chúng tôi cũng sẽ chỉ cho bạn cách bạn có thể tìm thấy URL đó và chúng tôi liên kết tới nó

trong sổ ghi chép của chúng tôi.

Hoặc bạn có thể chỉ cần tìm kiếm bảng kiểm duyệt của Google trong sổ ghi chép và chúng tôi cũng sẽ có liên kết đó.

Được rồi, hãy bắt đầu bằng cách chuyển đến thư mục từ tệp zip của chúng tôi.

Được rồi, tôi ở bên dưới thư mục của Anan.

Hãy tiếp tục và mở sổ ghi chép bảng tensor mà chúng tôi có ở đây dành cho bạn.

Đó là bảng Dash Tenzer số 0 năm.

Chà, chúng ta sắp làm việc này là chúng ta sẽ tạo ra một bảng căng thẳng, chạy ra khỏi mạng

ban đầu chúng tôi đã tạo trong bài giảng phân loại CARUS của mình.

Vì vậy, khi bạn mở sổ ghi chép của ban kiểm duyệt, nó sẽ trông giống như thế này.

Và có một liên kết ở đây để xem hướng dẫn chính thức đầy đủ thảo luận về nhiều khía cạnh thú vị của Tensor

bảng.

Chúng ta thực sự sẽ tìm hiểu những điều cơ bản trong bài giảng cụ thể này.

Nhưng nếu bạn nhấp vào liên kết đó, nó sẽ có liên kết bắt đầu này.

Và điều thực sự thú vị ở đây là nếu bạn đang sử dụng Google KB, tất cả những gì bạn cần làm là về cơ bản bạn có thể

gần như bỏ qua bài giảng này, chỉ cần mở liên kết có nội dung đang chạy Google CoLab.

Và điều này bắt đầu với sổ ghi chép bảng Tensor mà về cơ bản bạn có thể chạy tất cả các ô

và mọi thứ được thực hiện tự động cho bạn.

Hãy nhớ rằng ở đây chúng ta sẽ sử dụng một mô hình hơi khác một chút.

Việc thực hiện đã bỏ sót mạng nơ-ron tích chập mà chúng ta sẽ thấy ở phần sau của khóa học.

Nhưng những ý tưởng giống nhau.

Bạn sẽ tạo một thư mục nhật ký, tạo một số lệnh gọi lại và sau đó điều chỉnh nó.

Và bây giờ chúng ta cũng sẽ đề cập đến vấn đề này trong bài giảng của mình.

Vì vậy, bạn có thể tiếp tục xem bài giảng của chúng tôi, sau đó chỉ cần nhấp vào liên kết này rồi chạy sổ ghi chép này.

Và bạn có thể thực sự nhìn thấy bảng Tenzer bên trong sổ ghi chép của mình.

Vì vậy, hãy quay lại đây và chúng tôi sẽ chỉ cho bạn cách chạy cái này nếu bạn đang chạy lại nó cục bộ, nếu bạn

Chú Google, hầu như chỉ cần nhấp vào liên kết đó và bắt đầu chạy các ô.

Nhưng chúng tôi sẽ nhập khẩu gấu trúc.

Và con số tôi đọc trong tệp dữ liệu mà chúng tôi đã làm việc, việc phân loại ung thư đó sẽ tiếp tục

và lấy các giá trị đó, thực hiện quá trình phân chia và sau đó chia tỷ lệ dữ liệu.

Cho đến nay, không có gì khác biệt.

Và sau đó chúng ta cũng sẽ tạo mô hình, vì vậy chúng ta sẽ tạo mô hình.

Tôi cũng sẽ thêm vào việc dừng sớm.

Nhưng một thông báo hoặc một điều cần lưu ý ở đây là chúng tôi đang nhập một lệnh gọi lại bổ sung.

Vì vậy, từ lệnh gọi lại giấy bìa, bạn cũng sẽ nhập bảng Tenzer.

Vì vậy, ngay cả khi bạn không nhập tính năng dừng sớm cho mô hình cụ thể của mình để thực sự biên dịch và

có lều hoặc để theo dõi những nhật ký đó, chúng tôi sẽ truy cập từ bảng Kerrisdale Callbacks Import Tenzer.

Chúng ta sẽ tiếp tục và tạo lệnh gọi lại dừng sớm, giống như lần trước.

Và sau đó chúng tôi sẽ đảm bảo rằng chúng tôi hiểu sổ ghi chép này nằm ở đâu bằng cách chạy TWD.

Vì vậy, trong trường hợp của tôi, bây giờ tôi đã có đường dẫn tệp nơi sổ ghi chép này thực sự nằm ở đâu.

Được rồi.

Vì vậy, bây giờ đã đến lúc thực sự đi đến phần quan trọng nhất, đó là việc tạo ra Tenzer này

hội đồng gọi lại.

Vì vậy, một lần nữa, bảng Tenzer, nó là một công cụ trực quan.

Và điều sắp xảy ra là lệnh gọi lại mà chúng ta sẽ tạo bằng cách nhập bảng Tensas này,

nó sẽ ghi lại rất nhiều thứ và việc nó ghi gì và không ghi gì là tùy thuộc vào bạn.

Vì vậy, nó có thể ghi lại những thứ như biểu đồ huấn luyện, trực quan hóa, biểu đồ kích hoạt, lập hồ sơ mẫu

số liệu, sơ đồ tóm tắt, v.v.

Vì vậy, có nhiều đối số khác nhau mà bạn chuyển qua khi tạo một báo cáo căng thẳng, một biến gọi lại để biểu thị

bạn có muốn ghi lại điều gì đó hay không.

Vì vậy, điều quan trọng nhất nằm ở đây, thư mục nhật ký, về cơ bản là đường dẫn tệp đến

nhật ký.

Và chúng tôi sẽ chỉ cho bạn cách điền thông tin đó chỉ trong một giây.

Những cái khác chỉ là bạn có muốn tiếp tục ghi lại nội dung nào đó hay không, vì vậy tần số biểu đồ

là tần số và thời điểm để tính toán biểu đồ kích hoạt và chờ đợi cho các lớp của

mô hình.

Vì vậy, điều chúng ta sắp làm là đặt cái này thành 1 để về cơ bản sau mỗi giai đoạn đào tạo,

chúng ta sẽ tiếp tục tính toán tất cả trọng số cho các lớp của mình và sau đó chúng ta sẽ tạo biểu đồ của nó.

Và sau đó kỷ nguyên tiếp theo sẽ thực hiện một biểu đồ khác.

Vì vậy, chúng ta thực sự có thể thấy những biểu đồ này về cơ bản được xếp chồng lên nhau.

Và chúng ta sẽ có được hình ảnh 3D thú vị này cho thấy trọng số đang thay đổi như thế nào

trong suốt các thời kỳ đào tạo.

Và sau đó, nếu muốn, bạn cũng có thể trực quan hóa biểu đồ để chúng ta có thể đặt biểu đồ phù hợp và chúng ta có thể

đặt điều đó thành đúng.

Chúng ta cũng có thể quyết định xem có muốn viết hình ảnh hay không, có nên viết trọng lượng mô hình hay không, để trực quan hóa

như một bảng hình ảnh và kiểm duyệt, sau đó tần suất cập nhật cũng là thứ bạn có thể chọn.

Thông thường, tôi khuyên bạn nên cập nhật theo từng kỷ nguyên.

Nó thường dễ dàng hơn để giải thích theo cách đó.

Và cuối cùng, chúng ta cũng có thể chỉ định một lô hồ sơ để có thể lập hồ sơ lô đó để tính toán mẫu

đặc điểm.

Theo mặc định, chúng tôi có thể lập hồ sơ theo đợt thứ hai, vì vậy chúng tôi sẽ giữ nguyên cấu hình đó ở chế độ mặc định.

Và tần suất cá cược là tần suất trong EPOXI mà các chữ cái nhúng sẽ được hiển thị.

Nếu bạn đặt giá trị đó thành 0, bạn sẽ không bận tâm đến việc hình dung những thứ đó trên giường.

Có rất nhiều thứ khác nhau ở đó.

Điều khác cần lưu ý ở đây là nếu bạn chạy mô hình này nhiều lần với các thông số khác nhau

và bạn muốn đảm bảo rằng bạn có các thư mục khác nhau cho mỗi lần chạy mô hình này, tôi khuyên bạn nên làm như vậy

đang làm và đây cũng chính là điều họ đã thiết lập trong hướng dẫn chính thức, bạn sẽ nhận thấy rằng

bạn cuộn xuống, họ sẽ thiết lập nó với dấu ngày giờ.

Vì thế ở đây người ta gọi nó là ngày giờ, ngày giờ.

Về cơ bản, điều đó có nghĩa là nếu bạn nói từ ngày giờ, nhập ngày giờ và sau đó bạn nói, hãy để tôi

chỉ cần phóng to ở đây để bạn có thể thấy rõ ngày giờ này và sau đó sắp xếp thời gian với điều này cụ thể

lệnh.

Bạn sẽ nhận được chuỗi này, cho biết ngày và giờ hôm nay.

Và những gì bạn có thể làm là đặt tên thư mục của bạn.

Bằng cách đó, chỉ cần bạn đợi một phút trước khi chạy lại mô hình của mình, bạn sẽ có một nhật ký duy nhất

mỗi khi bạn chạy mô hình, chúng ta có thể quay lại và chỉnh sửa số lượng nơ-ron trong một lớp, v.v.

và hình dung từng mô hình đó bằng bảng tensor.

Bây giờ, trong trường hợp của chúng ta, chúng ta chỉ chạy cái này một lần, vì vậy chúng ta sẽ tiếp tục và chỉ cần thiết lập nhật ký của mình

thư mục vào nhật ký.

Và vì tôi đang dùng Windows nên tôi sẽ nói dấu gạch chéo ngược phù hợp.

Nếu bạn là Mac OS hoặc Linux, bạn có thể chỉ cần thực hiện một dấu gạch chéo ngược hoặc thậm chí là dấu gạch chéo lên.

Điều tôi khuyên bạn nên làm là nếu bạn quay lại đây, hãy chú ý sau khi bạn gõ W.D., nó thực sự báo cáo

quay lại cho bạn cú pháp bạn nên sử dụng.

Vì vậy, tôi nên sử dụng dấu gạch chéo ngược kép.

Đó là điều tôi sẽ làm ở dưới này.

Vì vậy, thư mục nhật ký của bạn, cơ sở của nó phải luôn là nhật ký và sau đó thư mục con tiếp theo sẽ là

phù hợp.

Vì vậy, sau khi tôi chạy cái này bên trong vị trí hiện tại của tôi, thư mục này của Anan, tôi sẽ thấy một thư mục

được gọi là Nhật ký được tạo và sau đó là một thư mục bên trong lệnh gọi đó cho phù hợp.

Vì vậy, chúng tôi phải nói rằng nhật ký phù hợp và sau đó, bạn có thể tùy ý thêm dấu thời gian cho thư mục duy nhất.

Vì vậy, đây là mã tự động thực hiện điều đó cho bạn.

Được rồi, bây giờ tôi có thư mục nhật ký thay đổi này, về cơ bản nó có nghĩa là tôi sẽ đi đâu

để nói những nhật ký này trong quá trình đào tạo?

Và theo mặc định, nó phải phù hợp với nhật ký.

Vì vậy, tôi chuyển nó vào làm thư mục nhật ký của mình.

Tôi sẽ nói tần số biểu đồ là một và sau đó chúng ta sẽ tiếp tục và nói biểu đồ bên phải là hình ảnh bên phải.

Có đúng không?

Cập nhật tần số

Mỗi kỷ nguyên sẽ giữ lại cấu hình ở mức hai vì đó là mặc định và tần suất nhúng sẽ

giữ nó ở một.

Và bạn cũng có thể thử nghiệm các tùy chọn này dựa trên những gì bạn đọc ở đây và những gì bạn thực sự

muốn ghi lại.

Vì thế.

Chúng ta sẽ tiếp tục và tạo lệnh gọi đó và bây giờ ngay trước khi chúng ta tiếp tục và tạo mô hình tương tự,

bạn thực sự không cần chỉnh sửa bất cứ điều gì trong mô hình của mình.

Vì vậy, chúng ta sẽ chạy mô hình đó giống như chúng ta đã làm trước đây.

Nơi bạn thực sự thêm phần này vào nằm bên dưới danh sách gọi lại của chúng tôi thay vì chỉ vượt qua điểm dừng sớm,

như chúng tôi đã làm trước đây.

Chúng ta cũng sẽ chuyển vào bảng biến này, bảng này gọi lại là hàm gọi lại bảng Tensas mà chúng ta vừa tạo.

Vì vậy, sau khi bạn tạo mô hình, hãy tiếp tục và điều chỉnh mô hình.

Được rồi, đây sẽ là buổi tập luyện và vì tôi đã dừng lại sớm ở đây nên đây không phải là buổi tập luyện

trong suốt sáu trăm kỷ nguyên.

Tôi nghĩ lần trước nó dừng lại ở mức hơn 120 một chút.

Vì vậy, chúng ta sẽ tiếp tục và để nó chạy một chút và cuối cùng nó sẽ ngừng huấn luyện một lần

nó đạt đến một nơi nào đó trên đó.

Được rồi, đây là điểm dừng sớm 1 giờ 26.

hoàn hảo.

Được rồi, bây giờ chúng ta sẽ chạy Tenzer Board.

Vì vậy, thay vì chạy các hình ảnh trực quan của riêng mình, hãy xem bảng Tenzer cung cấp những gì.

Điều đầu tiên cần lưu ý ở đây là bảng Tenzer sẽ chạy cục bộ trong trình duyệt của bạn tại

localhost sáu không không sáu.

Hãy tiếp tục và nhấp vào đó rồi mở nó trong một tab mới ngay bây giờ, vì chúng tôi chưa thực sự chạy bảng Tenzer

chưa.

Khi bạn chạy nó, nó sẽ trống hoặc có nội dung như không thể truy cập trang này vì

Sensabaugh vẫn chưa chạy trên đó.

Nó thực sự chạy bảng Tenzer hoặc chúng ta sẽ làm là chạy nó thông qua dòng lệnh.

Điều chính cần ghi nhớ là việc thu hồi thư mục nhật ký của bạn là gì?

Đó là biến chúng tôi đã tạo về cơ bản cho biết nơi chúng tôi thực sự lưu nhật ký của mình.

Hãy nhớ lại rằng chúng tôi đã lưu nó trong phần nhật ký phù hợp.

Trên thực tế, nếu bạn quay lại thư mục của Anan, bạn sẽ nhận thấy bây giờ chúng ta có thư mục nhật ký này và bên dưới

có một thư mục con và bên dưới có xác nhận huấn luyện và tệp đặc biệt dành cho Tenzer

bảng.

Và đây thực chất là những tệp thô mà bộ phận hỗ trợ sẽ sử dụng để hiển thị trực quan hóa.

Và có nhiều tệp hơn tùy thuộc vào mức độ bạn thực sự ghi.

OK, vậy điều quan trọng cần ghi nhớ là thư mục nhật ký của bạn là gì?

Trong trường hợp của chúng tôi, chúng tôi giữ nó đơn giản.

Nó chỉ là những bản ghi phù hợp.

Nhưng bạn cũng có thể có liên kết dấu thời gian dài hơn về điều đó.

Và điều tiếp theo cần nhớ lại là vị trí thực sự của bạn trên máy tính.

Đây là nơi tôi đang ở trên máy tính của mình.

Vì vậy, những gì chúng ta cần làm là đi đến dòng lệnh của chúng ta.

Đó là Annacone, dấu nhắc hoặc dấu nhắc lệnh cho người dùng Windows hoặc cho Mac OS hoặc Ubuntu

hoặc người dùng Linux.

Đó sẽ là thiết bị đầu cuối của bạn hoặc lời nhắc anakonda nếu bạn cài đặt nó với tư cách là người dùng Mac OS hoặc Linux.

Hãy tiếp tục và mở dòng lệnh của chúng ta, vì vậy điều quan trọng cần lưu ý là tệp này hiện ở đâu

nằm ở đâu và tên thư mục blog của cô ấy là gì?

Được rồi, tôi sẽ mở lời nhắc anakonda và bây giờ tôi đã mở lời nhắc anakonda của mình.

Bước tiếp theo là đảm bảo rằng tệp khóa học hoặc môi trường khóa học của tôi được kích hoạt.

Vì vậy, tôi sẽ nói QandA kích hoạt và sau đó bất kể môi trường khóa học nào sẽ được gọi.

Trong trường hợp của tôi, tôi sử dụng một môi trường hơi khác khi quay bài giảng này nên tôi sẽ nói QandA

kích hoạt GPU TAFTA.

Tuy nhiên, môi trường khóa học của bạn sẽ là môi trường bạn thiết lập trong bài giảng cài đặt.

Đáng lẽ bạn phải kích hoạt môi trường của mình khi xem qua các bài giảng này, vì vậy

không có gì mới đối với bạn.

OK, vậy là bạn đã kích hoạt xong môi trường và bây giờ việc cần làm là chúng ta cần thay đổi thư mục hoặc CD

vào thư mục cụ thể đã được gõ ra trong PTSD.

Vì vậy tôi sẽ xem những thứ này.

Trong giai đoạn này, các khóa học về dữ liệu, đó là nơi tôi tình cờ ở, các tệp của bạn có thể khác

trên máy tính của bạn và tôi đặc biệt khuyên bạn chỉ cần đánh dấu tab để hoàn thành việc này, vì nếu bạn

đánh vần sai gì cũng không được thì gõ lại C.

Và thư mục tiếp theo, trường hợp của tôi là Tenzer lại chuyển sang boot camp.

Chỉ cần sử dụng tính năng tự động hoàn thành tab để đảm bảo đúng chính tả.

Và cuối cùng là CD.

Vào số không ba và kết thúc, và chúng ta có nó.

Được rồi, bây giờ là lúc ra lệnh.

Vì vậy, lệnh chúng tôi sử dụng là đảm bảo bạn đã kích hoạt môi trường của mình.

Bạn sẽ có thể gõ bảng Tenzer.

Dấu gạch ngang, dấu gạch ngang dấu cách dya và sau đó là thư mục nhật ký của bạn.

Vì vậy, trong trường hợp của tôi, thư mục nhật ký của tôi, tôi đã in nó ra ở đây là nhật ký, các trang web phù hợp với dấu gạch chéo ngược sẽ là nhật ký,

dấu gạch chéo ngược phù hợp.

Và nếu bạn muốn xem nó trên một dòng, tôi có thể kéo dài nó ra.

Vì vậy, nó ở đây.

Vì vậy, các bước là kích hoạt môi trường của tôi.

Của bạn có thể được gọi khác tùy thuộc vào bài giảng cài đặt của bạn, sau đó CD vào thư mục nơi tôi đã xảy ra

để lưu các nhật ký đó hoặc sổ ghi chép đó đang chạy rồi chạy tensor board space, dash, dash, log

khoảng trống rồi đến đường dẫn file được in ra khi in ra, thư mục log lên đây

trong sổ ghi chép rồi tiếp tục và nhập khi nhấn enter.

Bạn sẽ thấy một số lệnh bật lên và cuối cùng điều gì sẽ xảy ra là nó sẽ cho bạn biết,

này, bảng kiểm duyệt chạy ở localhost six thu hồi 006.

Đó là URL chúng tôi đã mở trước đó.

Dù bạn làm gì, đừng nhấn điều khiển.

Ngoài ra, hãy xem, vì vậy đừng thực hiện chính sách kiểm soát để sao chép localhost này.

Nếu không thì điều đó thực sự thoát khỏi điều này.

Vì vậy, bạn chỉ sử dụng chính sách kiểm soát khi bạn đã sẵn sàng bỏ việc hoặc chúng tôi sẽ làm điều đó.

Hiện tại chúng tôi thực sự đã hoàn thành xong việc với anakonda.

Vì vậy, chúng ta sẽ đến với cuốn sách của mình trong trình duyệt.

Hãy nhớ lại rằng chúng tôi đã mở localhost sáu không không sáu.

Hãy tiếp tục và mở lại tab đó.

Và nếu nó báo là không thể truy cập trang web này, chẳng hạn như Yusoff, chỉ cần làm mới và bạn sẽ làm được.

thấy nó bật lên.

Và trong trường hợp không, bạn luôn có thể đến đây và chọn các đại lượng vô hướng.

Tuy nhiên, nếu bạn làm mọi thứ như tôi đã làm, nó sẽ tự động chuyển sang dạng vô hướng cho bạn,

như bạn có thể thấy ở đây trong YORO.

Được rồi, vậy hãy cùng khám phá một số trong số này.

Tôi sẽ thu nhỏ lại một chút để chúng ta không phóng to quá mức vào bảng Tensas này.

Và để bắt đầu, chúng ta có thể thấy sự mất mát của mình cả trong tập huấn luyện và tập xác thực, và chúng ta hiểu được điều này

cốt truyện tương tác thực sự hay và chúng tôi có thể làm cho nó rất mượt mà nếu chúng tôi chỉ muốn nắm bắt xu hướng chung.

Việc này có thể hơi quá trơn tru hoặc chúng ta có thể tắt hoàn toàn thứ gì đó để lấy dữ liệu thô như chúng ta đã làm.

làm trước đó.

Vì vậy, đây thực chất là một phiên bản tương tác của các âm mưu mà chúng tôi đã thực hiện trước đây với gấu trúc.

Và chúng ta có thể bắt đầu thử nghiệm bằng cách chuyển trục y thành logarit.

Bạn có thể tắt và bật nó.

Chúng tôi cũng có thể điều chỉnh tên miền cho phù hợp với dữ liệu.

Nó thực sự làm điều đó tự động.

Và sau đó bạn cũng có thể làm những việc như phóng to và phóng to.

Vì vậy, rất nhiều thứ khác nhau để chơi xung quanh.

Nếu bạn chỉ muốn xem xác thực, bạn có thể đánh dấu vào đây để xem nó, v.v.

Vì vậy, đây là những gì chúng ta thấy trong SCALARS.

Bạn có thể khám phá điều đó.

Sau đó chúng ta có hình ảnh.

Trong trường hợp của chúng tôi, chúng tôi thực sự đã quyết định ghi lại những hình ảnh này và điều này về cơ bản cho bạn thấy

hình ảnh, trọng lượng.

Và theo cách diễn giải điều này cho tập hợp cụ thể của chúng ta, vì chúng ta không xử lý dữ liệu hình ảnh, nên nó

không rõ ràng làm thế nào để giải thích điều này.

Đây thực chất là trọng lượng khi chúng trở nên tối hơn, nhạt hơn tùy thuộc vào thực tế sau này

TRÊN.

Vì vậy, chúng ta có thể thấy bản đồ ở đây, nhưng việc giải thích tổng thể điều này sẽ không giúp ích nhiều cho chúng ta bởi vì

chúng tôi không thực sự xử lý dữ liệu hình ảnh.

Và bạn cũng có thể thử nghiệm với độ tương phản, v.v., cũng như độ sáng.

Sau đó là biểu đồ.

Đây là biểu đồ chúng tôi đã tạo để bạn có thể thử nghiệm.

Bạn có thể khám phá nó.

Có một chú giải ở đây cho bạn biết mỗi nút này đang làm gì.

Nhưng đây là mô hình tuần tự mà chúng tôi đã tạo ra.

Chúng tôi có thể mở rộng về điều đó.

Chúng ta có thể thấy ở đây những gì chúng ta đã tạo ra, v.v.

Sau đó là sự phân bổ, phạm vi trọng số trên các lớp khác nhau này.

Vì vậy, đó là một.

Đó là hai.

Và sau đó là cái cuối cùng.

Hãy nhớ rằng, nếu diễn giải những điều này một cách trực tiếp, nó sẽ không thực sự giúp ích nhiều cho bạn trong trường hợp cụ thể này.

tập dữ liệu.

Điều này trở nên hữu ích hơn rất nhiều khi bạn xử lý những thứ như mạng tích chập.

Tất cả chúng ta đều có thể xem lại biểu đồ khi diễn giải điều này một cách trực tiếp, có thể không hữu ích lắm,

nhưng điều bạn có thể biết ở đây là mọi thứ đang thay đổi như thế nào theo thời gian.

Vì vậy, ví dụ, nếu chúng ta chỉ nhìn vào điệu nhảy đầu tiên này, đây chính là sự thiên vị.

Vì vậy, đây là các giá trị sai lệch cho mỗi kỷ nguyên trong suốt thời gian.

Vì vậy, bạn có thể thấy ngay từ đầu chúng đang thay đổi một cách dữ dội.

Nhưng khi bạn bắt đầu tiến tới thời kỳ dừng lại, hãy để ý, chúng không thay đổi nhiều lắm.

Biểu đồ của các giá trị sai lệch này không thay đổi, điều này có ý nghĩa.

Chúng ta nên kỳ vọng rằng khi chúng ta ngày càng tiến gần đến điểm dừng ban đầu đó, mọi thứ sẽ thay đổi

ngày càng ít đi.

Và biểu đồ cân nặng thực tế cũng tương tự như vậy.

Vì vậy, đây là các biểu đồ trong trường hợp sai lệch này và chờ đợi lớp dày đặc đầu tiên đó.

Vì vậy, bạn có thể thấy lúc đầu chúng bắt đầu thay đổi nhanh chóng, nhưng sau đó chúng bắt đầu ổn định theo hướng

bất kể trọng lượng cuối cùng của chúng là bao nhiêu.

Và chúng ta có thể xem điều đó cho các lớp.

OK, sau đó tùy thuộc vào bên nào để ghi, bạn có thể xem những thứ như hồ sơ và máy chiếu.

Những thứ này sẽ không hữu ích lắm cho chúng ta lúc này.

Vì vậy, chúng ta sẽ tiếp tục bỏ qua những điều này và quay lại bảng Tenzer khi chúng ta giải quyết vấn đề tích chập

mạng lưới thần kinh, vì khi đó nó sẽ thực sự hữu ích trong việc khám phá mạng lưới.

Nhưng hiện tại, chúng ta có thể thấy rằng thực ra chúng ta đã tự mình tạo ra rất nhiều hình ảnh như vậy, cụ thể là

sự mất mát của thời đại.

Đó là cái mà bạn thực sự sẽ sử dụng rất nhiều.

Và chúng ta đã biết cách tự mình tạo ra thứ này.

Những biểu đồ này, mặc dù hiện tại khá thú vị để bạn chú ý nhưng lại không có nhiều thứ cho bạn

có thể thực hiện việc chỉnh sửa các siêu tham số trên mạng thần kinh nhân tạo này chỉ dựa trên những

sơ đồ.

Khi bạn tiến bộ hơn, bạn có thể diễn giải điều này tốt hơn một chút.

Nhưng hiện tại, ý tưởng chính ở đây là bạn biết cách tạo bảng cảm biến.

Và chúng ta sẽ quay lại vấn đề này và khám phá những điều này chi tiết hơn khi chúng ta tìm hiểu về những vấn đề phức tạp hơn

những mô hình chúng tôi đang diễn giải.

Những biểu đồ này thực sự có thể giúp chúng tôi.

OK, cảm ơn mọi người và tôi sẽ gặp bạn ở phần tiếp theo của khóa học.
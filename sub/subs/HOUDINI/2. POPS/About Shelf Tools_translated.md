# Giới thiệu về Kệ Công cụ đã dịch

---

phần nhạc pop và ở đây chúng ta sẽ bắt đầu thực hiện những bước đầu tiên vào thế giới mô phỏng thực tế.

Nhưng trước khi chúng ta bắt đầu, tôi muốn nói nhanh về điều gì đó thực sự quan trọng đối với tôi và điều đó

là những công cụ kệ và về cơ bản tại sao chúng lại xấu xa. Tôi hoàn toàn không khuyên người mới bắt đầu sử dụng

chúng và có nhiều lý do cho việc đó. Vì vậy, tôi biết điều này nghe có vẻ đáng ngạc nhiên đối với người mới bắt đầu bởi vì,

bạn biết đấy, những biểu tượng đó ở ngay trước mặt bạn, nhưng ít nhất bạn nghe thấy nó ở đây đối với tôi,

chúng thực sự là một lựa chọn tồi và có nhiều lý do cho điều đó. Điều đầu tiên là bạn không

thực sự hiểu những gì họ đang làm. Bạn bấm vào nó và có điều gì đó xảy ra mà bạn không biết

chuyện gì đang xảy ra vậy Điều này tốt nếu mọi thứ hoạt động bình thường, nhưng ngay khi có sự cố xảy ra,

bạn không hiểu điều gì đang ngắt quãng và dù sao thì bạn cũng phải học các nốt. Vì thế nó không giúp ích gì

về mặt đó. Lý do thứ hai là rất nhiều thiết lập trong số đó thực sự khá tệ.

Vì vậy, nó thậm chí không phải là một cài đặt trước tốt mà bạn nhận được. Và một ví dụ điển hình ở đây là khi chúng ta đi vào

Bước hạt, là chủ đề mà chúng ta sẽ xem xét trong chương này, hãy tạo một hình cầu

đầu tiên ở cấp độ đối tượng vì sau đó nó cũng tạo ra một phạm vi phụ. Và khi tôi nói hạt nguồn

phát xạ, nó yêu cầu tôi chọn một đối tượng. Vì vậy, tôi làm điều này, nhấn Enter và bây giờ nó sẽ tạo ra thứ gì đó cho tôi.

Tôi không biết đây là gì. Tôi không biết mỗi ghi chú đang làm gì. Chúng ta sẽ làm gì trong khóa học

là chúng tôi sẽ xây dựng thiết lập từng bước cho từng ghi chú mà chúng tôi sẽ tạo bằng tay để chúng tôi thực sự

hiểu từng phần của nó làm gì, đặc biệt khi sau này bạn có những cảnh rất phức tạp,

bạn cần hiểu họ thực sự đang làm gì để giải quyết và thay đổi điều bạn mong muốn. Như tôi đã nói,

vấn đề thứ hai không có ở đây. Chúng ta có thể thấy điều này với công cụ shell này rồi. Nó tạo ra một thiết lập

Tôi hoàn toàn không khuyến khích. Nó tạo ra ba ghi chú ở cấp độ đối tượng về cơ bản giống nhau

mô phỏng. Vì vậy, nếu chúng ta nhìn vào các liên kết phụ thuộc của khung nhìn, chúng ta có thể thấy rằng chúng được kết nối và

về cơ bản những gì chúng ta thấy ở đây là đầu vào, bản thân mô phỏng và sau đó là đầu ra. Tại sao bạn lại làm

cái này à? Đây là một ý tưởng rất tồi. Bất cứ khi nào tôi nhìn thấy mạng auto-dop ở bất cứ đâu, tôi đều biết đây là

một người không biết mình đang làm gì hoặc đôi khi họ biết rất rõ họ đang làm gì,

nhưng đây lại là vấn đề khác khi bạn có kinh nghiệm đến mức bạn có thể sử dụng bất cứ thứ gì

bởi vì bạn biết sai sót ở đâu. Nhưng là người mới bắt đầu, tôi không khuyến khích điều đó. Tại sao? Bởi vì bạn

phải liên tục chuyển đổi giữa đầu vào và sau đó là mô phỏng thực tế và sau đó bạn phải

nhảy trở lại đầu ra. Đây là cách tôi sẽ làm để bạn hiểu tại sao điều này lại tốt hơn. Chúng tôi có thể

làm tất cả điều này ở cùng một nơi. Chúng ta có thể tạo một hình cầu, sau đó sử dụng pop-net như chúng ta sẽ thấy trong phần sau.

vài video tiếp theo và sau đó chúng ta có thể làm điều gì đó với kết quả đầu ra mà tôi không biết với phép biến đổi,

chúng tôi lấy những gì phát ra từ nó và tất cả những thứ trước mắt tôi những gì chúng tôi vừa thấy giờ đã được kết nối ở đây.

Thật dễ hiểu. Chúng ta có thể thay đổi đầu vào, mô phỏng và đầu ra ở cùng một nơi và chúng ta không

cần phải liên tục nhảy xung quanh. Vì vậy, đây thường là một thiết lập thực sự cồng kềnh và cả hành vi

thực sự là khá khó hiểu. Ví dụ: tôi tạo lại một hình cầu và tạo một bộ phát mới như chúng ta vừa

đã làm và những gì nó tạo ra lại là ba nút và những gì nó thực sự làm là khi tôi đặt trò chơi đó

từ hình cầu, vài điểm. Bây giờ hãy tạo một đối tượng thứ hai mà tôi muốn phát ra từ đó

bởi vì tôi nghĩ không sao, điều này hoạt động tốt. Bây giờ chúng ta hãy thêm hộp này và thêm mô phỏng của riêng nó cho

nó và tôi nhấp lại vào nút tương tự. Sau đó, những gì tôi nhận được là một cái gì đó khác nhau. Tôi không nhận được một

auto.net thứ hai hoạt động và đầu ra thứ hai nhưng điều này hiện sẽ được tích hợp vào cái hiện có.

Chắc chắn, ý tôi là điều này có thể thay đổi ở đây. Bạn thực sự có thể thay đổi điều này những gì nó nên được áp dụng

nhưng toàn bộ cách những kệ đó hướng tới kiểu phản ứng và hành xử là rất khó đoán bởi vì ai đó

về cơ bản đã viết một đoạn mã có nhiệm vụ thực hiện điều gì đó và bạn biết rằng bạn không biết trong đó

trước những gì thực sự sẽ xảy ra. Tại sao không tự mình xây dựng thì bạn sẽ biết chính xác ở đâu

mọi thứ đều như vậy và nó hoạt động cùng nhau như thế nào bởi vì khi tôi tự xây dựng nó như trước đây tôi có nó theo cách này

Tôi có một hình cầu, tôi có một popnet và tôi có một đầu ra và nếu tôi muốn một bản sao của nó, tôi chỉ cần sao chép nó

thay đổi đầu vào và mọi thứ đều dễ hiểu vì tôi tự tạo nó và nếu tôi muốn điều này

cả hai đều ở trong cùng một mô phỏng, tôi tự thực hiện việc này một cách thủ công. Đây là một cách tiếp cận tốt hơn nhiều và bằng cách

Đây không chỉ là ý kiến của tôi mà tôi còn kiểm tra kỹ điều này với rất nhiều đĩa CD hiệu ứng khác mà tôi biết

và tất cả họ đều đồng ý rằng điều này đặc biệt dành cho người mới bắt đầu không phải là một ý tưởng hay. Lại có hai loại

của những người sử dụng các công cụ trên kệ. Người mới bắt đầu tuyệt đối không biết họ đang làm gì hoặc siêu

những đĩa CD hiệu ứng có kinh nghiệm, những người thực sự biết rõ các công cụ đó từ trong ra ngoài và hiểu được những sai sót cũng như

quy trình làm việc rất tốt và về cơ bản biết công cụ kệ nào tốt và công cụ nào tệ nhưng với tư cách là một

người mới bắt đầu bạn không biết điều đó. Điều đó nói lên rằng thực tế có rất ít trường hợp tôi sẽ sử dụng

có sẵn các công cụ trong khóa học và đó là bằng cách phân tích những gì họ thực sự đang làm. Vì vậy không chỉ mù quáng

nhấp vào chúng và hy vọng điều tốt nhất nhưng chúng tôi thực sự sẽ xem xét một vài cài đặt trước ở đây mà chúng tôi

ví dụ như đối với đại dương nơi chúng ta có thể tìm hiểu từ nó những tác dụng phụ thực sự được dự định là quy trình làm việc

và sau đó chúng tôi không sử dụng các công cụ trên kệ nữa mà tự mình xây dựng các quy trình công việc đó từ những gì chúng tôi

đã học. Vì vậy, với tư cách là một công cụ học tập, tôi nghĩ các công cụ trên kệ có thể tốt nhưng đừng dựa vào chúng như một công cụ

người mới bắt đầu sản xuất thực tế. Một lý do khác khiến tôi nghĩ đây thực ra không chỉ là ý kiến của tôi là

trong vài năm gần đây với Houdini 18, tôi nghĩ các tác dụng phụ đã bắt đầu biến mất

kệ công cụ và đưa ra một khái niệm mới đó là cấu hình các cài đặt trước. Vì vậy thay vì chỉ

nhấp vào nút để điều kỳ lạ nào đó xảy ra và bạn không hiểu hết vì nó

tạo ra tất cả các loại hình học và bạn thậm chí không biết họ chuyển sang hệ thống ở đâu mà họ có

cung cấp cho bạn một số trợ giúp về một số cài đặt trước nhưng bạn truy cập chúng thông qua menu và chúng được gọi là cấu hình

cài đặt trước. Vì vậy, khi chúng tôi sử dụng bất kỳ cài đặt trước cấu hình nào ở đây, ví dụ như bong bóng, bạn có thể

hãy xem nó tạo ra nhiều nút cho chúng ta nhưng nó ở ngay trước mặt chúng ta nơi chúng ta đang cầm chuột

không tạo ra một số nút mà bạn biết ở đâu đó trên cấp độ đối tượng mà chỉ cụ thể là chúng ta đang ở đâu

ngay bây giờ. Một ví dụ điển hình khác cho điều này là các cấu hình pyro thậm chí còn tạo ra những kết quả đẹp mắt.

những thiết lập lớn nhưng chúng luôn dễ hiểu vì chúng ở ngay nơi tôi ở

bây giờ ở cấp độ phụ và những thứ chúng tôi thực sự sẽ sử dụng rất nhiều nhưng chúng tôi sẽ không sử dụng các công cụ trên kệ. Vâng, những cái đó

là những lý do tại sao chúng tôi sẽ không sử dụng các công cụ trên kệ trong khóa học, đặc biệt là với người mới bắt đầu, tôi sẽ không sử dụng

khuyên họ bạn không hiểu họ đang làm gì thường xuyên họ thậm chí còn sử dụng không tốt lắm

thiết lập và chúng làm phức tạp rất nhiều thứ mà không có lý do cụ thể. Vì vậy, đừng sử dụng chúng và

rất cẩn thận khi bạn xem hướng dẫn sử dụng chúng và vì lý do nào đó ngay cả tác dụng phụ cũng có một số

hướng dẫn sử dụng các công cụ kệ mà tôi thấy khá có vấn đề nhưng ít nhất bây giờ bạn đã nghe nó từ tôi

xây dựng từng thiết lập của bạn và đây là những gì chúng ta sẽ làm từ giờ trở đi trong phần còn lại của khóa học.

Vì vậy, điều này rất hữu ích không quá lan man, cảm ơn rất nhiều và hẹn gặp lại các bạn sau.
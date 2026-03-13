# 006 Cách xây dựng các vòng lặp lồng nhau

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong video này, chúng ta sẽ thấy.

Các chi tiết về các vòng lặp lồng nhau.

Một vòng lặp có thể lồng trong một vòng lặp khác được gọi là vòng lặp lồng nhau.

Các vòng lặp lồng nhau là cần thiết khi một quá trình lặp lại phải được lặp lại.

Giống như vậy.

Với những phát biểu.

Trong khi.

Và while người da đen có thể chứa các câu lệnh Python tùy ý, bao gồm cả các vòng lặp khác.

Do đó, một vòng lặp có thể được lồng trong một vòng lặp khác.

Vì vậy, ở đây.

Trong sơ đồ này.

Đúng vậy.

In ra bảng cửu chương bằng cách sử dụng hai vòng lặp for.

Vòng lặp for đầu tiên không có gì khác ngoài.

Vòng lặp bên ngoài.

Và vòng lặp for thứ hai không gì khác ngoài vòng lặp bên trong.

Điều quan trọng cần ghi nhớ ở đây là.

Khi luồng điều khiển đến vòng lặp bên trong.

Cái cụ thể.

Đối tượng có thể lặp lại hoặc biến ở vòng lặp bên ngoài.

Sau đó vòng lặp bên trong sẽ tự lặp lại.

Nhưng số lượng.

Các biến.

Trong chuỗi vòng lặp bên trong.

Có nghĩa là trong sơ đồ màu đen này.

Đối với I trong phạm vi từ 1 đến 10.

Vòng lặp for thứ hai cho j trong phạm vi từ 1 đến 10 in I nhân j.

Giả sử rằng ban đầu luồng điều khiển nằm ở vòng lặp for bên ngoài.

Đối với một trong phạm vi.

1 đến 10 tồn tại trong phạm vi, 1 đến 10.

Sau đó luồng điều khiển sẽ chuyển sang.

Bên trong vòng lặp bên trong chúng ta có.

Câu lệnh j trong phạm vi từ 1 đến 10.

Bây giờ là vòng lặp bên trong.

Sẽ lặp lại chính nó.

Chín lần từ 1 đến 9 vì biến bên ngoài bị loại trừ.

Vậy Outerloop có một ở vòng lặp bên trong thay đổi từ 1 đến 9 có nghĩa là một.

Và sau đó trong vòng lặp thay đổi từ 1 đến 9 một thành một, 1 trong 2, một, hai, ba, 1 trong 2, bốn.

1 trong 2 năm.

1 trong 2 sáu.

1 trong 2 bảy.

1 trong 2 tám và 1 trong 2 chín.

Sau đó.

Khi vòng lặp bên trong kết thúc.

Đó là một.

Lặp lại chín biến trong phạm vi hoặc trong chuỗi.

Sau đó luồng điều khiển sẽ di chuyển trở lại vòng lặp bên ngoài.

Để kiểm tra phần tử tiếp theo trong chuỗi.

Bây giờ tôi trở thành hai ở vòng ngoài.

Một lần nữa, luồng điều khiển sẽ chuyển sang vòng lặp bên trong.

Lại.

Vòng lặp bên trong.

J thay đổi từ 1 đến 9.

Thế là hai thành một, hai thành ba, hai thành bốn.

Hai thành năm, sáu, bảy, tám, chín.

Sau đó, luồng điều khiển sẽ quay trở lại vòng lặp bên ngoài và.

Nó sẽ kiểm tra tiếp theo.

Yếu tố trong.

Sự liên tiếp.

Đó là ba.

Vì vậy, với mỗi phần tử ở vòng lặp bên ngoài, vòng lặp bên trong sẽ tự lặp lại.

Lên đến số lượng phần tử trong chuỗi.

Đây là cách vòng lặp lồng nhau hoạt động.

Vòng lặp bên trong sẽ được ưu tiên khi luồng điều khiển đạt đến và luồng bên trong sẽ tự lặp lại

cho số lần.

Các yếu tố có trong.

Trình tự vòng lặp bên trong.

Vì vậy, chúng ta hãy xem thực tế vòng lặp lồng nhau hoạt động như thế nào trong Python.

Đây là bảng cửu chương mà chúng ta vừa thảo luận.

Từ 1 đến 10 trong chương trình, chúng ta phải dùng 11 thay vì 10.

Để lấy bảng cửu chương từ 1 đến 10.

Đây.

Vòng lặp bên ngoài.

Tương ứng với các cột từ 1 đến 10 và vòng lặp bên trong tương ứng với các hàng.

Phép nhân.

Bởi vì phép nhân xảy ra ở vòng lặp bên trong.

Đối với J trong phạm vi từ 1 đến 10.

Nhìn vào đây.

Khi vòng lặp bên ngoài, khi luồng điều khiển ở vòng ngoài và kiểm tra các số trong phạm vi,

1 đến 10 cho một vòng lặp bên trong sẽ lặp lại mười lần.

J thay đổi từ 1 đến 10.

Một thành 111 thành hai, hai, một thành 331 thành bốn, bốn một thành năm năm.

Một, hai, sáu, sáu.

Một, hai, bảy, bảy, tám, chín, mười.

Sau khi lặp lại vòng lặp bên trong 10 lần, luồng điều khiển sẽ quay trở lại vòng lặp bên ngoài và

luồng điều khiển sẽ kiểm tra phần tử tiếp theo trong chuỗi.

Tức là một trở thành hai.

Vì vậy, hai lần nữa, luồng điều khiển sẽ quay trở lại vòng lặp bên trong.

Vòng lặp bên trong sẽ lặp lại một lần nữa mười lần.

Đối với.

Biến đặc biệt.

Điều đó đúng ở vòng lặp bên ngoài.

Một lần nữa, vòng lặp bên trong thay đổi từ 1 đến 10.

Và tại thời điểm này, Vòng lặp bên ngoài.

Giá trị tới.

Hai thành một.

Vì ban đầu j thay đổi từ 1 đến 10.

Hai thành hai.

Khi luồng điều khiển kiểm tra phần tử tiếp theo trong vòng lặp bên trong.

J thay đổi từ 1 đến 2, một đến 10 đến 2 thành hai.

Vì khi biến vòng lặp bên trong J trở thành ba, thì hai thành ba trở thành ba.

Và cứ thế cho đến hai phần mười, tức là 20.

Sau đó, luồng điều khiển sẽ chuyển trở lại.

Biến bên ngoài.

Và kiểm tra phần tử tiếp theo là ba ba và vòng lặp bên trong thay đổi từ 1 đến 10, ba thành

133 thành hai, sáu ba thành ba chín.

Và cứ như vậy cho đến ba trên mười.

30.

Và cuối cùng.

Hoạt động này tiếp tục đến.

Phần tử cuối cùng trong chuỗi vòng lặp bên ngoài là 10.

Từ mười chia 110 đến mười chia mười bằng 100.

Chúng ta hãy quay trở lại công việc thực tế và xem.

Các ví dụ về vòng lặp lồng nhau

Vì vậy, ban đầu chúng tôi chỉ tạo các hàng và cột mà không có bất kỳ hàng nào.

Sản phẩm bên trong bàn.

Bảng nhân.

Chúng ta hãy lấy số hàng và cột trong bảng với sự trợ giúp của người dùng đó là kích thước.

Người dùng phải quyết định.

Thứ nguyên có nghĩa là các hàng và cột ma trận của ma trận.

Nhưng bảng cửu chương.

Ban đầu.

Chúng ta hãy bắt đầu với các hàng.

Đối với hàng trong phạm vi.

Một, hai.

Chúng tôi biết rằng phần tử cuối cùng bị loại trừ.

Đó là lý do tại sao để có được phần tử cuối cùng chúng ta cần.

Thêm một vào phần tử thực tế cuối cùng có kích thước cộng một, vì trong Python chỉ mục bắt đầu từ 0.

Vì vậy, ở đây chúng ta đang sử dụng hàm phạm vi để tạo chuỗi các giá trị từ một đến.

Kích thước cộng với một kích thước là.

Kích thước của.

Ma trận.

Do người dùng quyết định.

Và trong vòng lặp for thứ hai, chúng ta đang khởi tạo số cột.

Đối với cột trong phạm vi, một đến kích thước cộng một.

Và đó.

Sau vòng lặp thứ hai.

Và bên trong phần tiếp theo thứ hai, chúng tôi chỉ in số hàng và số cột.

Vì vậy hàng này chỉ hiển thị số hàng và cột này hiển thị số cột.

Và các yếu tố này được phân tách bằng.

Cái.

Không gian trống rỗng.

Và rồi kết thúc này.

Sẽ cách nhau một dấu cách.

Có nghĩa là các phần tử được phân tách bằng một khoảng trắng thay vì dòng tiếp theo.

Hãy để chúng tôi in cái này.

Một cái bàn.

Mà chỉ hiển thị số hàng và cột dưới dạng ma trận.

Cái này.

Chạy mã và xem kết quả.

Đúng vậy.

Nhập.

Kích thước bảng như.

Năm để hiểu rõ hơn.

Vì vậy, ở đây bạn có thể thấy Row.

Và số cột.

Hàng một cột.

Một hàng.

Một cột hai hàng.

Một cột ba hàng.

Một cột bốn hàng.

Một cột năm.

Như tôi đã nói trước đó.

Đối với mỗi hàng.

Trong vòng lặp bên ngoài có nghĩa là cho từng phần tử trong vòng lặp bên ngoài.

Vòng lặp bên trong sẽ tự lặp lại.

Tối đa số phần tử trong chuỗi ở vòng lặp bên trong có nghĩa là vòng lặp bên trong sẽ tự lặp lại

về số phần tử có trong dãy.

Vì vậy, ở đây số phần tử trong dãy không có gì ngoài 1 đến 6.

Giá trị bên ngoài được loại trừ.

Đó là sáu.

Vì vậy, chúng tôi sẽ chỉ nhận được các giá trị từ 1 đến 5.

Vì vậy, điều đó có thể được nhìn thấy ở đây.

Cột và sau đó là số cột.

Cột một.

Cột đến cột ba.

Cột bốn rồi đến cột năm.

Và luồng điều khiển sẽ quay trở lại vòng lặp bên ngoài.

Vòng lặp bên ngoài sẽ được.

Bây giờ hãy kiểm tra phần tử tiếp theo.

Đó là hai hàng hai và vòng lặp bên trong sẽ lặp lại năm lần.

Cột một đến cột ba, cột bốn và cột năm.

Một lần nữa, vòng lặp bên ngoài sẽ quay trở lại luồng điều khiển, sẽ quay trở lại vòng lặp bên ngoài và kiểm tra

cho phần tử tiếp theo đó là.

Yếu tố thứ ba.

Vì vậy, số hàng và giá trị số hàng.

Vòng quay và vòng trong thay đổi từ 1 đến 5.

Cột một trong hai.

Cột năm.

Vì vậy, đây là cách thực hiện.

Cái.

Các vòng lặp lồng nhau hoạt động.

Vòng lặp bên trong sẽ có mức độ ưu tiên cao nhất và tự lặp lại theo số phần tử có trong chuỗi

theo trình tự của nó.

Được rồi.

Sau đó, luồng điều khiển sẽ quay trở lại vòng lặp bên ngoài và vòng lặp bên ngoài cũng sẽ lặp lại.

Về số phần tử có trong dãy của nó.

Nhưng khi luồng điều khiển chuyển sang vòng lặp bên trong.

Vòng lặp bên trong sẽ tự lặp lại theo số phần tử có trong chuỗi của nó trước tiên.

Đây là bảng cửu chương.

Vì vậy, trong ví dụ tiếp theo, chúng tôi thực sự đang tạo tệp .

Số liệu sản phẩm.

Vì vậy, chúng tôi đang nhập kích thước của ma trận cho kích thước thay đổi và cho hàng trong phạm vi, một đến kích thước

cộng một và cho cột trong phạm vi.

Một hai công tắc cộng với một tích bằng hàng thành cột.

Chỉ cần thay thế này.

Các yếu tố.

Trong câu lệnh in, có hàng.

Số hàng.

Cột.

Số cột.

Tất cả đều được phân tách bằng khoảng trống với hàng sản phẩm thành cột.

Đúng vậy.

Rất đơn giản.

Được rồi.

Hàng và cột.

Điều này thật đơn giản.

Sản phẩm bằng hàng thành cột.

Đối với mỗi.

Giá trị ở vòng lặp bên ngoài.

Đó là từ 1 đến 5.

Vòng lặp bên trong sẽ thực hiện thao tác sản phẩm vì chúng ta đang sử dụng sản phẩm bên trong vòng lặp bên trong

là vòng lặp for thứ hai.

Vòng lặp bên trong sẽ in giá trị sản phẩm.

Mỗi phần tử cách nhau bởi

Hai miếng đệm.

Được rồi.

Trước đó.

Chúng tôi đang sử dụng một không gian.

Bây giờ chúng tôi đang sử dụng hai không gian.

Hãy để chúng tôi chạy mã này và phân tích.

Sử dụng Ctrl + nhập.

Hãy để chúng tôi nhập.

Kích thước của ma trận là năm.

Bây giờ hãy nhìn vào đây chúng ta có.

Phép nhân của từng phần tử.

Ở dạng.

Số liệu.

Hoặc bảng cửu chương.

Hãy để chúng tôi phân tích mã này.

Đối với mỗi giá trị trong hàng, nghĩa là.

Hàng ngang.

Một hàng, hai hàng, ba hàng.

Bốn hàng năm.

Những con số này là số vòng lặp bên ngoài.

Một, hai, ba, bốn, năm.

Vòng lặp bên trong sẽ thực hiện thao tác sản phẩm.

Đó là một trong một.

Một thành hai bằng một thành ba bằng ba.

Một thành bốn bằng bốn.

Một thành năm bằng năm.

Như thế này.

Bảng còn lại.

Hãy nhìn ra đây để tìm vòng lặp bên ngoài.

Trong một, 261.

Quan sát chuột của tôi để tìm cột trong phạm vi từ 1 đến 6.

Sản phẩm bằng hàng thành cột.

Vì thế.

Vòng lặp bên trong sẽ tự lặp lại theo số phần tử có trong chuỗi của nó.

Đầu tiên.

Được rồi, vòng lặp bên trong sẽ lặp lại năm lần.

126.

Vì vậy, tại thời điểm này, giá trị hàng vòng lặp bên ngoài là một thành một.

Đó là một vòng lặp bên trong cho cột sẽ.

Kiểm tra phần tử tiếp theo trong phạm vi có nghĩa là luồng điều khiển sẽ kiểm tra phần tử tiếp theo trong phạm vi

phạm vi đó là để.

Tuy nhiên, chúng ta có giá trị vòng lặp bên ngoài là một thành hai.

Đó là hai.

Vòng lặp bên trong cho cột sẽ kiểm tra phần tử tiếp theo có ba một thành ba không có gì ngoài ba,

một thành bốn.

Đó là bốn.

Một thành năm.

Đó là năm.

Sau đó, luồng điều khiển sẽ chuyển sang vòng lặp for bên ngoài và giá trị hàng bây giờ sẽ được thay đổi thành

hai.

Phần tử tiếp theo.

Một hai, sáu một đã được bảo hiểm.

Và phần tử tiếp theo không có gì ngoài hai.

Được rồi?

Hai.

Và sau đó vòng lặp sẽ tự lặp lại.

Năm lần từ 1 đến 5.

Giá trị vòng ngoài ở đây là hai.

Giá trị vòng lặp bên trong thay đổi từ 1 đến 5, hai thành 1 đến 2 thành hai không gì khác ngoài bốn.

Hai thành ba chẳng là gì ngoài sáu.

Hai phần bốn không gì khác hơn là tám và hai phần năm không gì khác hơn là mười.

Tiếp theo, luồng điều khiển sẽ quay trở lại vòng lặp bên ngoài và.

Lặp lại cho phần tử tiếp theo.

Đó là ba.

Khi dòng điều khiển.

Sạc lại vòng lặp bên trong.

Vòng lặp bên trong lặp lại năm lần một giây.

Vậy ba thành một chẳng qua là ba.

Ba thành hai chẳng qua là sáu.

Ba thành ba chẳng là gì ngoài chín.

Ba ăn bốn chẳng là gì ngoài 12.

Ba ăn năm chẳng là gì ngoài 15.

Tương tự cho phần tử tiếp theo ở vòng lặp bên ngoài.

Đó là cho.

Lên đến năm.

14 chia thành 5.

Không có gì ngoài 20.

Và tương tự, đối với phần tử cuối cùng ở vòng lặp bên ngoài là năm.

Sau đó, vòng lặp sẽ lặp lại năm lần.

Tức là năm thành một là năm.

Năm chia hai chẳng là gì ngoài mười.

Sau năm chia năm, đó là 25.

Tuyên bố in này sẽ.

Chuyển sang dòng tiếp theo.

Một khi vòng lặp bên trong.

Đó là cái này.

Thực hiện các hoạt động của.

Sản phẩm có nghĩa là một khi nó hoàn thành hoạt động của sản phẩm.

Để di chuyển cho hàng tiếp theo.

Chúng tôi đang sử dụng câu lệnh in.

Tuyên bố in này.

Sẽ chuyển đến.

Hàng tiếp theo.

Khi vòng lặp bên trong kết thúc phép nhân.

Với mỗi phần tử.

Theo trình tự của nó.

Nếu bạn không sử dụng câu lệnh print.

Khi đó hàng thứ hai này sẽ hiển thị ngay sau hàng đầu tiên.

Đó là 1 đến 5.

Chúng ta sẽ lấy hàng tiếp theo ở đây, 2 đến 10 và 3 đến 15 như thế.

Vì vậy, để tránh điều đó và hiển thị dưới dạng ma trận tương tự, chúng tôi đang sử dụng câu lệnh in ở vòng lặp bên trong.

Tời sau vòng bên trong.

Câu lệnh in này thực chất là phần thân của vòng lặp bên ngoài.

Khi vòng lặp bên trong kết thúc hoạt động tạo tệp.

Phép nhân cho hàng cụ thể.

Luồng điều khiển sẽ chuyển trở lại hàng tiếp theo.

Bởi vì tuyên bố in này.

Được rồi, vậy câu lệnh in này thuộc về vòng lặp bên ngoài, không phải vòng lặp bên trong.

Bởi vì các hàng tương ứng với vòng lặp bên ngoài.

Và sản phẩm và các cột tương ứng với vòng lặp bên trong.

Vì vậy, hãy nhìn vào đây logic.

Được rồi?

Chúng tôi đang sử dụng sản phẩm bên trong vòng lặp bên trong.

Bản thân vòng lặp bên trong này là phần thân của vòng lặp bên ngoài.

Một lần nữa.

Vòng lặp bên trong phải duy trì sự thụt đầu dòng của nó.

Đó là lý do tại sao phần thân vòng lặp bên trong lại ở đây.

Sau khi thụt lề.

Và nếu bạn nhìn vào vòng lặp for trong vòng lặp for và câu lệnh print của chúng tôi, chúng có cùng một vết lõm

có nghĩa là chúng là phần thân của vòng lặp bên ngoài dành cho hàng trong phạm vi, một đến kích thước cộng một.

Đây là cách bảng nhân hoặc vòng lặp lồng nhau hoạt động.

Và đây là cách chúng ta có thể tạo ra Ma trận.

Sử dụng các vòng lặp lồng nhau.

Nói theo thuật ngữ kỹ thuật, chúng ta có thể nói rằng vòng ngoài điều khiển.

Bây giờ chương trình in ra tổng cộng bao nhiêu hàng và vòng lặp bên trong.

Được thực hiện toàn bộ mỗi khi chương trình in một hàng.

In các phần tử riêng lẻ.

Và cả những sản phẩm

Đó là một hàng hoàn chỉnh?

Và.

Ma trận tương ứng.

Nếu bạn nhìn vào bảng cửu chương.

Các phần tử trong mỗi cột được sắp xếp không đẹp mắt.

Chúng ta có thể sử dụng tham số chuỗi để sắp xếp các phần tử trong mỗi cột.

Tuyệt vời.

Chúng ta sẽ xem cách sử dụng tham số sau khi trình bày.

Những sợi dây.

Trong Python.

Được rồi.

Hãy để chúng tôi chạy mã này.

Và.

Hiển thị bảng nhân ma trận cho.

Số mười.

Vì vậy, ở đây bạn có thể thấy bảng nhân ma trận.

Những gì chúng ta đã thảo luận trong.

Cầu trượt.

Đó là 1 đến 10.

Các cột được xếp không đẹp mắt.

Đừng lo lắng về điều đó.

Chúng tôi sẽ che nó.

Một khi chúng tôi.

Di chuyển đến phần dây.

Chúng ta hãy xem thêm một ví dụ nữa.

Đối với vòng lặp lồng nhau.

Các vòng lặp lồng nhau là cần thiết khi một quá trình lặp lại phải được lặp lại.

Vì vậy, khi.

Quá trình lặp đi lặp lại.

Bản thân nó phải được lặp lại.

Chúng ta phải sử dụng các vòng lặp lồng nhau vì như tôi đã nói với bạn trước đó, điều đó.

Khi luồng điều khiển đến vòng lặp trong cùng, vòng lặp trong cùng sẽ tự lặp lại theo số

thời gian nhân với các phần tử có trong dãy có mặt trong dãy của nó.

Chúng ta có thể thấy điều đó một cách tổng quát nhất trong ví dụ này.

Thực hiện hoán vị các chữ cái trong word.

Đó là A, B, c.

Vì vậy, ở đây chúng ta đã sử dụng ba bốn vòng lặp với các điều kiện.

Vì chúng ta có ba ký tự hoặc chữ cái trong từ A, B, C, đó là lý do tại sao chúng ta sử dụng ba ký tự cho

vòng lặp với điều kiện đó.

Những lá thư.

Không nên như vậy.

Lặp đi lặp lại.

Cho lần đầu tiên vào.

ABC.

Để minh họa các vòng lặp vòng lặp đầu tiên, vòng lặp thứ hai và vòng lặp thứ ba.

Chúng tôi chỉ sử dụng tên biến là thứ nhất, thứ hai và thứ ba.

Mục đích ở ABC.

Đây là trình tự lặp lại được.

Vòng lặp for tiếp theo.

Vòng lặp for bên trong tiếp theo.

Đó là vị trí thứ hai trong ABC.

Và tập thứ ba cho thứ ba trong ABC.

Để sắp xếp thứ tự và in ra hoán vị của chữ ABC.

Chúng tôi đang sử dụng ba vòng lặp.

Hãy để chúng tôi phân tích mã này bằng cách chạy nó.

Vì vậy, ở đây chúng ta có thể thấy đối với ABC, chúng ta có một, hai, ba, bốn, năm và sau đó là sáu chuỗi sắp xếp

như một hoán vị.

Nếu bạn quan sát từ thứ hai, ACB, từ thứ hai không được lặp lại.

Không có từ nào được lặp lại.

Vì vậy, để tránh lặp lại, chúng ta sử dụng điều kiện if trong vòng lặp for thứ hai và thứ ba.

Nếu thứ hai không bằng thứ nhất.

Sau đó chuyển sang vòng lặp for thứ ba.

Trong vòng lặp for thứ ba, chúng ta so sánh chữ cái đầu tiên và chữ cái thứ hai.

Nếu chữ cái đầu tiên không bằng chữ cái thứ ba không bằng chữ cái đầu tiên và thứ ba

chữ cái không bằng chữ cái thứ hai.

Sau đó in đầu tiên, cộng với thứ hai, cộng với thứ ba.

Vòng lặp bên trong sẽ tự lặp lại.

Ba lần vì ở đây chúng ta có ba.

Các biến trong chuỗi lặp.

Đó là A, B, c.

Hay nói cách khác, chuỗi này bao gồm ba phần tử hoặc các phần tử có thể lặp lại A, B và sau đó là C.

Hãy để chúng tôi phân tích mã này.

Đơn giản nhất có thể.

Đối với Boston, ABC.

Chữ cái đầu tiên ở đây, biến đầu tiên thay đổi từ A đến C.

Đứng thứ hai ở ABC.

Bức thư thứ hai.

Thứ hai cũng thay đổi từ A đến Z.

Nếu thứ hai không chỉ bằng thứ nhất thì chuyển sang thứ ba.

Vòng lặp For ở vòng lặp thứ ba chúng ta có vòng lặp thứ ba trong ABC.

Thứ ba cũng thay đổi từ A đến C.

Bên trong vòng lặp thứ ba, chúng ta có điều kiện if.

Nếu chữ cái thứ ba không bằng chữ cái đầu tiên và chúng ta đang sử dụng biểu thức boolean ghép cuối.

Chữ cái thứ ba không bằng chữ cái thứ hai.

Sau đó in trình tự.

Thứ nhất, thứ hai và thứ ba.

Hãy cùng chúng tôi tìm hiểu cơ chế hoạt động của vòng lặp này.

Đây.

Tổng số vòng lặp được thực hiện sẽ phụ thuộc vào.

Vòng lặp trong cùng thứ ba.

Nhân với thứ hai.

Vòng lặp trong cùng.

Nhân với vòng lặp bên ngoài đầu tiên.

Nhiều vòng lặp này sẽ được đánh giá, nhưng do điều kiện sai nên một số vòng lặp sẽ bị loại bỏ.

chấm dứt.

Đó là lý do tại sao chúng ta không nhận được tất cả các hoán vị có các từ được lặp lại.

Ký tự lặp đi lặp lại.

A, a B hãy như thế.

Sau khi tìm ra chương trình, chúng tôi sẽ hiểu nó hoạt động như thế nào.

Được rồi.

Chúng ta hãy bắt đầu với.

Chảy.

Dòng điều khiển.

Sẽ di chuyển từ bên ngoài.

Nhìn vào vòng lặp bên trong.

Khi hoạt động của vòng lặp bên trong kết thúc công việc của nó thì luồng điều khiển sẽ chuyển từ vòng lặp bên trong sang vòng lặp bên trong.

vòng lặp bên ngoài.

Vì vậy, đó là.

Ý nghĩa của câu này.

Hoạt động vòng lặp luồng điều khiển đi từ vòng lặp trong cùng đến vòng lặp ngoài cùng.

Một khi nó đi vào vòng trong cùng từ vòng ngoài cùng.

Chúng ta hãy bắt đầu phân tích từ vòng lặp bên ngoài.

Đó là lần đầu tiên ở ABC.

Vì vậy, chuyển từ vòng lặp for đầu tiên sang vòng lặp thứ ba.

Với điều kiện trong vòng lặp for thứ hai.

Để kiểm soát dòng chảy.

Giả sử rằng luồng điều khiển nằm trong vòng lặp đầu tiên và.

Luồng điều khiển đang kiểm tra phần tử đầu tiên.

Đó là một.

Vì vậy, hãy nhìn đầu tiên.

Với.

Biến đầu tiên có.

Giá trị.

Đây là biến đầu tiên có giá trị.

Tám.

Được rồi.

Sau đó, luồng điều khiển sẽ chuyển sang vòng lặp for thứ hai.

Vòng lặp for thứ hai.

Biến thứ hai cũng thay đổi từ.

A đến Z.

Vì vậy bây giờ biến cách thứ hai có giá trị.

Một giây cho vòng A và điều kiện.

Vì vậy hãy nhìn vào đây.

Nếu điều kiện thứ hai không bằng thứ nhất, vì biến thứ hai có biến A và tại

đồng thời phần tử vòng lặp đầu tiên có.

Biến có phần tử hoặc giá trị.

A A không bằng a, điều kiện trở thành sai.

Dòng điều khiển.

Sẽ không đánh giá cơ thể của.

Câu lệnh if đó là những dòng này.

Trực tiếp.

Luồng điều khiển sẽ chuyển sang vòng lặp bên ngoài vì điều kiện ở đây trở thành sai.

Bây giờ.

Ở vòng lặp bên ngoài.

Biến đầu tiên nhận giá trị tiếp theo.

Đó là được.

Bây giờ giá trị đầu tiên là a.

Trong khi giá trị vòng lặp for thứ hai là be.

Bởi vì chúng ta biết rằng khi luồng điều khiển di chuyển từ vòng lặp trong cùng đến vòng lặp ngoài cùng,

vòng lặp trong cùng sẽ có mức độ ưu tiên cao nhất và tự lặp lại theo số phần tử có mặt

trong trình tự của chúng.

Vì vậy, vòng lặp for thứ hai sẽ tự lặp lại tối đa ba lần đối với phần tử đầu tiên trong vòng lặp for mà

là một.

Vì vậy, thứ hai cho vòng B và điều kiện là.

Trong vòng lặp for thứ hai, chúng ta có điều kiện.

Bây giờ là thứ hai.

Biến có B và biến đầu tiên chỉ có A.

Điều kiện là B không bằng a.

Đó là sự thật.

Bây giờ phần thân của câu lệnh if sẽ được đánh giá vì điều kiện là đúng và luồng điều khiển

sẽ chuyển sang vòng lặp for thứ ba.

Bây giờ chúng ta đang ở vòng lặp for thứ ba.

Và bộ điều khiển sẽ làm như vậy.

Bắt đầu với phần tử đầu tiên trong chuỗi.

Đó là a và điều kiện.

Thứ ba không bằng thứ nhất.

Đó là a không bằng a.

Và thứ ba không bằng thứ hai.

Đó là a không bằng B vì biến vòng lặp for thứ hai là B.

Điều kiện trở thành sai vì.

Đúng và sai.

Lại trở thành sai vì chúng ta đang ở vòng lặp thứ ba trong cùng.

Vòng lặp này lặp lại trước, do đó luồng điều khiển sẽ kiểm tra phần tử tiếp theo trong

vòng lặp trong cùng là B, vậy vòng lặp thứ ba là B và điều kiện là.

Thứ ba không bằng thứ nhất.

Trong lần đầu tiên.

Chúng tôi có một.

Và.

Thứ ba không bằng thứ hai trong thứ hai chúng ta có.

Một lần nữa, điều kiện trở thành sai và luồng điều khiển sẽ lại chuyển sang vòng lặp for bên trong.

Có nghĩa là vòng lặp for bên trong sẽ tự lặp lại và luồng điều khiển sẽ kiểm tra phần tử tiếp theo.

Bây giờ hãy xem vòng lặp for thứ ba với phần tử.

Xem điều kiện và điều kiện được xem không bằng phần tử đầu tiên.

Đó là thứ ba không bằng thứ nhất và thứ ba không bằng thứ hai.

Tức là see không bằng B vì vẫn ở vòng for thứ 2, phần tử là B, điều khiển

dòng chảy ở phần tử B.

Bây giờ, lần này điều kiện trở thành đúng.

Nó in trình tự.

A, B, c.

Vì phần tử thứ nhất là a nên giá trị của biến thứ nhất là giá trị của biến thứ hai là B,

và giá trị của biến thứ ba là.

Nhìn thấy.

Do đó ta sẽ được ABC.

Vì vậy, để có được ABC.

Nhiều lần lặp lại đã kết thúc.

Nhìn vào đây.

A, B, c.

Vòng lặp for thứ ba vừa hoàn thành việc lặp cho phần tử thứ hai B trong vòng lặp for thứ hai.

Một lần nữa kiểm tra luồng điều khiển cho phần tử cuối cùng trong vòng lặp thứ hai được xem.

Vì vòng lặp for thứ hai vẫn chưa kết thúc vòng lặp của nó.

Luồng điều khiển bây giờ sẽ chuyển sang.

Biến thứ ba, nghĩa là.

Hãy xem chúng ta đang ở vòng lặp for thứ hai và bây giờ luồng điều khiển sẽ kiểm tra phần tử cuối cùng.

Bây giờ biến thứ hai trở thành C, vì vậy vòng lặp for thứ hai chúng ta có C.

Và điều kiện C không bằng A.

Cô ấy không bằng thì điều kiện trở thành sự thật.

Sau đó luồng điều khiển sẽ chuyển sang.

Vòng lặp for thứ ba.

Cực thứ ba không là gì ngoài thân thể của nó.

Câu lệnh if nằm trong vòng lặp for thứ hai.

Và bây giờ khi luồng điều khiển đạt đến vòng lặp for thứ ba.

Vòng lặp thứ ba sẽ được kích hoạt và lặp lại.

Ba lần từ A đến Z.

Tôi cho là vậy.

Luồng điều khiển sẽ bắt đầu bằng.

Ký tự A trong vòng lặp thứ ba.

Vòng lặp thứ ba.

Biến thứ ba có giá trị lần đầu tiên.

Và điều kiện.

30 không bằng thứ nhất và thứ ba không bằng thứ hai.

Thứ ba không bằng thứ nhất vì chúng ta có a ở vòng lặp đầu tiên.

Được rồi.

Và thứ ba không bằng C vì chúng ta có C trong vòng lặp for thứ hai.

Vì biến A đã được gán cho C.

Điều kiện trở thành sai.

Lấy lại luồng điều khiển sẽ kiểm tra phần tử tiếp theo trong vòng lặp for trong cùng là vòng lặp thứ ba.

Vòng lặp for thứ ba.

Phần tử tiếp theo là.

Trong điều kiện B không bằng A tức là thứ ba không bằng bus.

Đó là a và thứ ba không bằng thứ hai.

Đó là.

Xem điều kiện trở thành đúng.

Nó in ACB.

Bởi vì thứ nhất không là gì ngoài thứ hai không là gì ngoài C và thứ ba không là gì ngoài B.

Chúng ta đang ở vòng for thứ ba với phần tử cuối cùng là C.

Vòng điện thứ ba.

Nhìn thấy?

Và điều kiện là.

Thứ ba không bằng thứ nhất.

Tức là C không bằng A.

Và thứ ba không bằng thứ hai.

Đó là C không bằng C, Đó là C không là gì ngoài giá trị của vòng lặp for thứ hai.

Điều kiện trở thành sai.

Bây giờ, cả ba lần lặp đã hoàn thành cho vòng lặp for thứ ba.

Luồng điều khiển sẽ chuyển sang.

Đầu tiên.

Đối với vòng lặp.

Vòng lặp bên ngoài.

Vì vòng lặp for thứ hai cũng đã kết thúc từ A đến C nên hãy xem tại đây.

Vòng lặp thứ hai cho C chúng ta đã hoàn thành vòng lặp for thứ ba từ A đến C, vậy bây giờ vòng lặp for thứ ba đã được thực hiện

lặp lại ba lần.

Vòng lặp for thứ hai cũng đã được lặp lại ba lần.

Luồng điều khiển sẽ chuyển trở lại.

Đó là vòng lặp ngoài cùng.

Đầu tiên.

Và nó sẽ kiểm tra phần tử tiếp theo trong chuỗi.

Đó là B cho B.

Đầu tiên.

Vòng lặp for đầu tiên.

Đối với tôi.

Hãy nhìn cô ấy thật cẩn thận.

Nhiều lần lặp lại sẽ lặp lại.

Một lần nữa để tạo ra.

B, AC và BC.

Và đối với cô ấy.

Đối với phần tử cuối cùng.

Hãy xem, nhiều bước này sẽ được lặp lại.

Để tạo ra.

Trình tự, CCB và CCB.

Tôi hy vọng bạn đã có ý tưởng hoàn chỉnh về cách tạo hoán vị của bất kỳ bảng chữ cái nào.

Chuỗi của chúng tôi, không gì khác hơn là một đối tượng có thể lặp lại.

Hãy để chúng tôi giữ nó ở đây.

A.

Và lưu chương trình này.

Bất cứ khi nào bạn theo dõi.

Phần tử thứ hai là chương trình nghĩa là chương trình này bạn chỉ cần thay thế là các bước còn lại sẽ giữ nguyên

như nó vốn có.

Vòng lặp for thứ hai, từ A đến C và vòng lặp for thứ ba.

Từ đâu đến?

A đến Z.

Được rồi.

Bạn chỉ cần làm những công việc đơn giản này.

Vì vậy, tôi đã phân tích nó để tìm phần tử đầu tiên ở vòng ngoài cùng.

Đó là bạn.

Hãy làm công việc truy tìm.

Chương trình hoàn chỉnh cho phần tử thứ hai và thứ ba trong.

Sự liên tiếp.

ABC, nằm ở vòng ngoài cùng.

Cảm ơn vì đã xem cái này.

Chúng ta hãy gặp nhau trong bài học tiếp theo.
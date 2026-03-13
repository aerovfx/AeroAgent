# 81 - Hệ số chiết khấu phần thưởng và phương trình Bellman

---

Chào mừng mọi người quay trở lại với bài giảng về Khái niệm cốt lõi này trong loạt bài về khái niệm cốt lõi tăng cường, trong đó

chúng ta sẽ thảo luận về phần thưởng, hệ số chiết khấu và phương trình Bellmon.

Bây giờ để hiểu những thứ như chính sách, giá trị và phần thưởng, các yếu tố chiết khấu và nhân viên phục vụ

phương trình, chúng ta sẽ cần xem xét một môi trường ví dụ để thực sự hình dung được điều này.

Vì vậy, chúng ta sẽ sử dụng cái được gọi là môi trường thế giới lưới, một môi trường đầu tiên rất phổ biến.

khi chúng ta thảo luận về lý thuyết đằng sau học tăng cường, đặc biệt là học tăng cường dạng bảng,

chẳng hạn như việc học tập của trẻ em mà chúng ta sẽ thảo luận trong phần sau.

Vì vậy, hãy nói về môi trường thế giới tuyệt vời mà bạn sẽ chơi sau này.

Vì vậy, trong môi trường thế giới lưới, chúng ta có các lưới ở đây và tác nhân hiện có thể ở trên một trong các lưới này,

điển hình là trong môi trường thế giới lưới.

Chúng tôi có một số loại mục tiêu.

Vì vậy, ví dụ: chúng tôi có thể có một lưới cụ thể mang lại cho bạn phần thưởng cộng bốn hoặc trong lưới khác, có thể

có giá trị âm và bạn sẽ bị trừng phạt nếu nó kết thúc hoặc nếu đại lý của bạn hạ cánh

trên lưới cụ thể đó.

Và chúng ta cũng nên lưu ý rằng đây là những trạng thái cuối cùng, nghĩa là khi tác nhân đáp xuống một trong những trạng thái này

giá trị dương hoặc giá trị âm, trò chơi kết thúc.

Vì vậy, chúng tôi có trò chơi này và rõ ràng là chúng tôi muốn cố gắng đạt được cộng bốn chứ không phải đạt đến âm một.

Vì vậy, trong môi trường lưới cụ thể này, chúng ta chỉ có bốn hành động có thể thực hiện là lên, xuống, trái

hoặc đúng.

Bây giờ, một câu hỏi được đặt ra là có bao nhiêu trạng thái có thể xảy ra?

Điều thú vị về môi trường thế giới lưới là về mặt kỹ thuật mà nói, đó là thời đại.

Nó chỉ có thể di chuyển lên xuống, sang trái hoặc phải vào một không gian lưới khác.

Vậy thì thực sự chỉ có 16 vị trí có thể.

Vì vậy, lưới 4 x 4 tạo ra 16 vị trí có thể có cho tác nhân, có nghĩa là chúng ta có thể mô tả

toàn bộ thế giới lưới ở 16 trạng thái có thể.

Không có gì khác ngoài 16 vị trí mà tác nhân có thể đảm nhiệm có thể gây ra môi trường

để tạo ra một trạng thái có thể khác.

Đây là lý do tại sao thế giới lưới là môi trường đầu tiên phổ biến nơi chúng ta bắt đầu tìm hiểu về việc tăng cường

học vì thật dễ dàng để thấy chúng ta có 16 trạng thái riêng biệt như thế nào.

Chỉ có 16 nơi mà đặc vụ có thể ở.

Vì vậy, về cơ bản chỉ có 16 lần lặp lại có thể có của thế giới lưới này.

Và chúng ta sẽ nói về điều đó sau khi chúng ta thảo luận.

Q Học tập.

Và nhớ lại rằng tác nhân cũng có bốn hành động có thể thực hiện được.

Vì vậy, bây giờ chúng ta đã hiểu được các trạng thái và hành động.

Vì vậy, hãy tưởng tượng rằng hộp Scribd là một trạng thái.

Vì vậy, tôi có chiếc hộp tuyệt vời này làm trạng thái và tôi biết tôi có thể di chuyển lên xuống, sang trái, phải sang một trạng thái khác

chiếc hộp tuyệt vời và có bốn hành động tiềm năng ở đó.

Bây giờ, hãy tưởng tượng rằng có các giá trị liên quan đến ngày tiếp theo mà nhân viên có thể thực hiện

âm một ở trên, hai ở bên trái, ở dưới và bốn ở bên phải.

Vậy đại lý đó nên thực hiện hành động nào?

Rõ ràng, chúng tôi muốn tối đa hóa giá trị tiếp theo đó để tác nhân di chuyển sang phải và sửa

cái đó cho.

Và đây là những gì chúng ta sẽ bắt đầu giới thiệu phương trình Bellmon.

Vì vậy, phương trình bellman về cơ bản viết ra điều này như sau.

Người ta sẽ nói rằng giá trị của trạng thái là V của S bằng giá trị tối đa mà một tác nhân có thể

có được bằng cách thực hiện bất kỳ hành động nào.

Vì vậy, hãy làm rõ điều này.

Tác nhân ở đây có thể thực hiện bất kỳ một trong bốn hành động lên, xuống, trái hoặc phải.

Và nó hiện đang ở trạng thái đó.

Và ở giữa, rõ ràng là giá trị tối đa nó có thể nhận được ở trạng thái tiếp theo nếu nó thực hiện hành động

bên phải là bốn.

Vì vậy, chúng tôi thực sự kết thúc việc dán nhãn giá trị trạng thái hiện tại của nó.

Vì vậy, hãy quay lại lưới bên trái và xem liệu chúng ta có thể thực sự tính toán được điều này không.

Chà, nếu chúng ta nhìn vào các lưới, về mặt kỹ thuật mà nói, có thể có một cách để đi từ một

tạo lưới tiếp theo xung quanh dấu cộng cho lên, xuống, trái hoặc phải để nhận giá trị.

Vì vậy, đó là giá trị hiện tại.

Và bạn có thể thấy rằng điều này sau đó sẽ mở rộng nó sang các vị trí lưới lên xuống, trái và phải tiếp theo từ

những lực đó và vân vân và vân vân.

Vì vậy, chúng tôi đã gặp phải loại vấn đề khó hiểu này khi đột nhiên, nếu tôi tuân theo phương trình Bellmon này, tôi

về cơ bản là gán mọi thứ giá trị tối đa có thể trên toàn bộ lưới, vì về mặt lý thuyết

từ bất kỳ vị trí màu xanh nào trong số này, tôi vừa viết một bài nước ngoài, tôi sẽ có thể đạt được điểm cộng tối đa

cho giá trị màu xanh lá cây.

Vì vậy, hiện tại phương trình Belmond chưa hoàn thiện theo cách chúng ta mong muốn, bởi vì lưới này

đầy sức mạnh, mặc dù về mặt kỹ thuật là đúng, nhưng tôi có khả năng đạt tới giá trị bốn, tức là

giá trị tối đa có thể từ bất kỳ một trong các vị trí lưới đó.

Điều đó rất hữu ích và thực sự đang tìm ra một con đường hiệu quả để đạt được giá trị cộng bốn đó.

Vì vậy, tôi có một số hành động để tối đa hóa giá trị và tôi đã phác thảo toàn bộ lưới này với các giá trị trên

tất cả các lưới có thể mang lại cho tôi giá trị tối đa đó.

Và lưu ý ở đây rằng về mặt kỹ thuật, nếu tôi đi theo bất kỳ mũi tên nào trong số này, cuối cùng tôi có thể đạt được cộng bốn,

đó là lý do tại sao tôi chỉ nói rằng tôi có một giá trị cho toàn bộ lưới của mình.

Nhưng rõ ràng điều này không hiệu quả chút nào.

Tôi có thể thử làm cho nó hiệu quả hơn một chút bằng cách loại bỏ các hành động sau đó sẽ chuyển thành

bức tường.

Và bây giờ tôi phần nào hiểu rõ hơn một chút về nơi tôi nên đi từ một ô vuông cụ thể.

Nhưng vẫn còn rất nhiều hành động mà tôi sẽ thực hiện để khiến người đại diện của tôi phải chuyển sang làm việc khác.

lặp đi lặp lại, qua lại giữa các ô vuông nhất định cho đến khi nó thực sự chạm vào dấu cộng bốn và màu xanh lá cây

Tôi đang tìm kiếm.

Vì vậy, mặc dù điều này đúng về mặt kỹ thuật nhưng nó sẽ lãng phí rất nhiều thời gian.

Vì vậy sẽ thật tuyệt nếu bằng cách nào đó tôi có thể tìm ra cách điều chỉnh phương trình Bellmon này để

yêu cầu tôi chỉ những mũi tên này theo hướng hiệu quả nhất để đạt được điểm cộng.

Vì vậy, đây là nơi chúng tôi sẽ giới thiệu ý tưởng về phần thưởng tiềm năng.

Vì vậy, tôi thực sự sẽ thêm phần thưởng âm cho mỗi bước đã thực hiện, hãy nhớ rằng chúng tôi đã đề cập đến phần thưởng

có thể tích cực hoặc tiêu cực.

Về cơ bản, đây là một cách để nhân viên hỗ trợ của bạn hiểu liệu họ có thực hiện đúng hành động hay không

để cuối cùng tối đa hóa phần thưởng dài hạn đó và thực sự hoàn thành mục tiêu.

Vì vậy, điều tôi sắp làm ở đây là nếu chúng ta xem lại trạng thái ban đầu này, chuyển sang trạng thái khác và thực sự

gán nó cho giá trị tối đa mà một tác nhân có thể đạt được bằng cách thực hiện bất kỳ hành động nào, tôi sẽ làm gì

là tôi muốn trừ một cho mỗi bước bạn thực hiện.

Vì vậy, điều tôi sắp làm là điều chỉnh phương trình Belmond của mình với ý tưởng về phần thưởng ở trạng thái thực hiện

một hành động nhất định và đặc biệt cho môi trường thế giới rộng lớn này ở đây.

Tôi sẽ nói rằng tôi sẽ trừ một điểm cho mỗi bước mà nhân viên thực hiện.

Vì vậy, bây giờ đi bên phải vẫn là hành động tốt nhất có thể, nhưng giá trị của tôi hiện tại ở bang này đang tăng lên

phải giảm đi một.

Vì vậy, thay vì gán nó với giá trị chính xác là 4, tôi sẽ gán nó cho 4 trừ một, đó là

là ba.

Bây giờ, hãy áp dụng logic này của phần thưởng trừ đi một bước này, cộng với giá trị tối đa mà đại lý có thể

có được bằng cách thực hiện bất kỳ hành động nào.

Và chúng ta sẽ thấy rằng lưới này bây giờ sẽ trông khác.

Vì vậy, nhìn từ dấu cộng cho các ô vuông xung quanh nó, giá trị tối đa mà chúng có thể đạt được bằng cách đi lên,

xuống, trái hoặc phải sẽ bằng cộng bốn, trừ một cho bước họ đi.

Vì vậy, sau đó họ sẽ đi với giá trị là ba.

Ngoài ra, chúng ta có thể thấy rằng cuối cùng trò chơi này bắt đầu trông giống như một trò chơi quét mìn, ngoại trừ

trong trường hợp này chỉ cho bạn biết số bước để đạt được phần thưởng tối đa có thể.

Và sau đó chúng tôi mở rộng điều đó ra khỏi đó.

Và sau đó chúng ta có thể thấy ở đây rằng một chính sách mà chúng ta có thể đưa ra thực ra chỉ hướng đến giá trị cao nhất

trạng thái.

Vì vậy bây giờ điều tôi sắp làm ở đây là bắt đầu xem xét các hành động sẽ hướng tới giá trị cao nhất.

Vì vậy, không phải ở đây, nếu chúng ta nhìn vào góc trên bên phải, với giá trị hiện tại bằng 0, giá trị cao nhất

lưới hoặc điểm trạng thái bên cạnh nó, nó sẽ ở bên trái.

Vì vậy cần phải có hành động yêu cầu bạn đi bên trái.

Bây giờ, bạn để ý khi chúng ta đến đó, chúng ta đang ở một trạng thái và thực sự hiện có hai trạng thái hoặc hai vị trí lưới

với giá trị là hai, nghĩa là chúng ta có thể chọn ngẫu nhiên giữa một trong những hành động đó sang trái hoặc xuống

để có được cả hai và vân vân.

Và về cơ bản những gì chúng ta có ở đây là một bản đồ cho thấy cần bao nhiêu bước để có được hai cộng bốn.

Và ở kịch bản đã lớn hơn.

Thực tế, chúng ta có thể kết thúc với các giá trị âm như âm một hoặc âm ba, v.v. nếu chúng ta

thực sự rất xa so với điều này cộng với bốn.

Nhưng rõ ràng là chúng tôi đã nảy ra một ý tưởng ở đây bao gồm cả ý tưởng về phần thưởng, cộng với mức tối đa có thể.

giá trị để thực hiện một hành động nhằm bắt đầu xây dựng một chính sách.

Bây giờ, vẫn còn một cải tiến nữa mà chúng tôi có thể thực hiện đối với phần trích dẫn chưa được trích dẫn, đó là phương trình Bellmon.

Lý do tôi đặt phương trình Bellmon trong dấu ngoặc kép ở đây là vì tôi đã hơi lén lút và thực ra tôi đã

đã cho bạn thấy phương trình Bellmon cuối cùng thực sự.

Chúng tôi đã cho bạn thấy một phần của nó.

Chúng ta cần kết thúc nó bằng việc bổ sung thêm ý tưởng về hệ số chiết khấu.

Hãy cùng khám phá lý do đằng sau điều này.

Trên thực tế, trong một môi trường, chúng tôi muốn tối đa hóa phần thưởng dài hạn, tuy nhiên, chúng tôi sẽ

ít chắc chắn hơn về các giá trị xa hơn trong tương lai khi tác nhân đang học hỏi.

Hãy nhớ lại rằng trong ví dụ của chúng tôi, nhân viên thực sự chỉ có thể vượt qua một cấp độ.

Và điều chúng tôi thực sự muốn làm là tối đa hóa các giá trị lâu dài được mở rộng qua nhiều hành động.

Nhưng chúng ta sẽ càng ít chắc chắn hơn khi càng đi xa hơn vào tương lai.

Vì vậy, tôi ngày càng muốn cân nhắc sự chắc chắn của mình về những giá trị tương lai đó.

Để giải thích điều này, chúng ta có thể giới thiệu Gamma như một hệ số chiết khấu gắn liền với các giá trị trong tương lai.

Vì vậy, hãy xem lại thế giới lưới và chỉ sử dụng hệ số chiết khấu cho lựa chọn hành động của chúng ta, vì vậy hãy đặt sang một bên

phần thưởng bây giờ và chúng tôi sẽ chỉ xem xét yếu tố giảm giá.

Vì vậy, để giới thiệu hệ số chiết khấu, chúng tôi lại bắt đầu ở một số trạng thái lưới và chúng tôi có những hệ số đó

giá trị tăng, giảm, trái hoặc phải.

Và chúng tôi sắp giới thiệu ý tưởng thực hiện hành động sẽ thực sự cho phép chúng tôi

để tối đa hóa giá trị này ở trạng thái tiếp theo.

Nhưng bây giờ tôi sẽ nhân nó với giá trị chiết khấu.

Bằng cách đó, tôi càng đi xa thì giá trị được giữ lại càng ít.

Vì vậy, ví dụ, nếu tôi nói tôi bằng 0,9 thì cuối cùng tôi sẽ làm gì và

thu hồi Gamma phải nhỏ hơn một vì nó đang giảm giá.

Vậy điều sẽ xảy ra ở đây là tôi thực sự vẫn chọn đi bên phải, nhưng bây giờ

giá trị của tôi sẽ được gán khác vì nó gấp bốn lần không, chín trên ba điểm

sáu.

Điều thú vị ở đây là khi trước đây chúng ta sử dụng phần thưởng trừ một, bạn nhận thấy

rằng về cơ bản nó sẽ liên tục bị trừ một bất kể bạn ở đâu trong lưới.

Nhưng nếu chúng ta áp dụng ý tưởng về hệ số chiết khấu này thì kết quả sẽ hơi khác một chút.

Vì vậy, ví dụ, chúng ta sẽ có 90 phần trăm của cộng 4, kết quả là 3,6.

Và bây giờ đối với tập giá trị tiếp theo, thực ra tôi đang tính 90% của 90% A4 đó,

kết quả là ba phẩy hai bốn.

Sau đó, đối với chuỗi giá trị tiếp theo của trạng thái đó, bây giờ tôi tính 90 phần trăm của 90 phần trăm cho

akei, 90 phần trăm, ba phẩy hai bốn, sẽ là hai phẩy chín hai.

Và cho đỉnh cuối cùng đó.

Đúng, thực sự điều tôi đang làm là tôi đang tính toán 90% của 90% của 90% kết quả cuối cùng

bốn.

được rồi.

90 phần trăm của hai phẩy chín hai, cuối cùng là hai phẩy sáu ba.

Và đây là cách mà hệ số chiết khấu bây giờ có thể tính đến ý tưởng rằng bạn ngày càng ít chắc chắn hơn

bạn càng đi xa hơn tới những trạng thái trong tương lai.

Phương trình Belmond sau đó kết hợp ý tưởng về phần thưởng và các yếu tố chiết khấu để xác định giá trị của một

trạng thái hiện tại.

Vì vậy, về cơ bản những gì chúng ta sẽ làm là kết hợp ý tưởng thêm phần thưởng đó vào một hành động cho một mục tiêu nhất định

trạng thái và ý tưởng nhân giá trị tương lai đó với người chơi game.

Vì vậy, chúng ta sẽ có được phiên bản cuối cùng của phương trình Belmond trong đó tôi sẽ xác định giá trị

trạng thái hiện tại của tôi làm giá trị tối đa cho bất kỳ hành động nào tôi sẽ thực hiện.

Đó sẽ là phần thưởng cho hành động được thực hiện trong trạng thái hiện tại của tôi, cộng thêm hệ số giảm giá

lần giá trị đó của trạng thái mới.

Và tôi muốn ghi nhớ ý tưởng này về phương trình này, đặc biệt là khi chúng ta bắt đầu tìm hiểu về nó.

Q Học bảng.

Q Học tập.

Vì vậy, sau này tôi sẽ tìm ra cách giải quyết vấn đề này và chúng ta sẽ thấy rằng thực sự có nhiều cách đóng khung khác nhau

câu hỏi này và sau đó bạn có thể giải quyết nó về mặt kỹ thuật thông qua mạng lưới thần kinh.

Vì thế.

Để xem xét nhanh, những gì chúng tôi đã làm ở đây về cơ bản là chúng tôi đã quyết định ý tưởng về một chính sách

là một chính sách để lựa chọn hành động tiếp theo có thể được tạo ra từ phương trình Belmond, thực hiện

để tính đến cả phần thưởng và yếu tố chiết khấu.

Vì vậy, phần tiếp theo chúng ta sẽ thảo luận nhanh về các quá trình tất định và ngẫu nhiên trong

các khái niệm cốt lõi của học tập tăng cường.

Tôi sẽ gặp bạn ở đó.
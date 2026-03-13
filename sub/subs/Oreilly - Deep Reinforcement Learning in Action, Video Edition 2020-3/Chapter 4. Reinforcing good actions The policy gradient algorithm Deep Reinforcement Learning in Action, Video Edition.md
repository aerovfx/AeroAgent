# Chương 4. Củng cố các hành động tốt Thuật toán gradient chính sách Học tăng cường sâu trong hành động, Phiên bản video được dịch

---

Phần 4.2, củng cố các hành động tốt, thuật toán gradient chính sách.

Từ phần trước, bạn hiểu rằng có một lớp thuật toán cố gắng

để tạo một hàm đưa ra phân bố xác suất cho các hành động và điều này

hàm chính sách pi của s có thể được thực hiện bằng mạng nơ-ron.

Trong phần này, chúng ta sẽ đi sâu vào cách thực sự triển khai các thuật toán này và đào tạo,

that is, optimize them.

Mục 4.2.1, xác định mục tiêu.

Hãy nhớ lại rằng mạng lưới thần kinh cần một hàm mục tiêu có khả vi

đến trọng số, tham số của mạng.

Trong chương trước, chúng ta đã huấn luyện mạng Q sâu với sai số bình phương trung bình cực tiểu,

MSE, hàm mất mát đối với các giá trị Q dự đoán của nó và giá trị Q mục tiêu.

Chúng tôi đã có một công thức hay để tính giá trị Q mục tiêu dựa trên phần thưởng quan sát được,

vì giá trị Q chỉ là phần thưởng trung bình, tức là kỳ vọng.

Vì vậy, điều này không khác nhiều so với cách chúng tôi thường huấn luyện một hệ thống học sâu có giám sát.

thuật toán.

Làm cách nào để đào tạo một mạng lưới chính sách cung cấp cho chúng tôi phân phối xác suất theo các hành động

cho trước một trạng thái, xác suất của A cho trước s?

Không có cách rõ ràng nào để lập bản đồ các phần thưởng được quan sát của chúng tôi sau khi thực hiện hành động cập nhật

xác suất của A cho trước s.

Việc tạo DQN không khác nhiều so với việc giải quyết vấn đề học có giám sát, bởi vì

Mạng Q của chúng tôi đã tạo ra một vectơ các giá trị Q được dự đoán và bằng cách sử dụng công thức, chúng tôi đã

có thể tạo ra vectơ giá trị Q mục tiêu.

Sau đó, chúng tôi chỉ giảm thiểu sai số giữa vectơ đầu ra của mạng Q và vectơ mục tiêu của chúng tôi.

Với mạng chính sách, chúng tôi dự đoán các hành động một cách trực tiếp và không có cách nào để đưa ra

thay vào đó, một vectơ mục tiêu của các hành động mà lẽ ra chúng ta nên thực hiện, được trao phần thưởng.

Tất cả những gì chúng ta biết là liệu hành động đó dẫn đến phần thưởng tích cực hay tiêu cực.

Trên thực tế, hành động bí mật tốt nhất phụ thuộc vào hàm giá trị, nhưng với chính sách

mạng, chúng tôi đang cố gắng tránh tính toán trực tiếp các giá trị hành động này.

Hãy xem qua một ví dụ để xem cách chúng tôi có thể tối ưu hóa mạng chính sách của mình.

Chúng ta sẽ bắt đầu với một số ký hiệu.

Mạng chính sách của chúng tôi được ký hiệu là pi và được tham số hóa bằng vectơ theta, đại diện cho tất cả

các tham số, trọng số của mạng nơ-ron.

Như bạn đã biết, mạng nơ-ron có các tham số ở dạng ma trận nhiều trọng số, nhưng

nhằm mục đích dễ dàng ký hiệu và thảo luận, tiêu chuẩn là phải xem xét tất cả các tham số mạng

cùng nhau thành một vectơ dài duy nhất mà chúng ta biểu thị là theta.

Bất cứ khi nào chúng tôi chạy chuyển tiếp mạng chính sách, vectơ tham số theta sẽ cố định.

Biến là dữ liệu được đưa vào mạng chính sách, tức là trạng thái.

Khi chúng ta biểu thị chính sách được tham số hóa là pi theta, bất cứ khi nào chúng ta muốn chỉ ra rằng một số đầu vào của hàm là cố định,

chúng ta sẽ đưa nó vào dưới dạng chỉ số dưới thay vì dưới dạng đầu vào rõ ràng như pi của x theta, trong đó x là một số dữ liệu đầu vào,

đó là trạng thái của trò chơi.

Các ký hiệu như pi của x, theta cho thấy theta là một biến thay đổi theo x, trong khi pi theta chỉ ra rằng theta là một tham số cố định của hàm.

Giả sử chúng tôi cung cấp cho mạng chính sách chưa được đào tạo ban đầu pi theta, một số trạng thái trò chơi ban đầu cho thế giới lưới, ký hiệu là s,

và chạy nó về phía trước bằng cách tính pi theta của s.

Nó trả về phân bố xác suất trên bốn hành động có thể xảy ra, chẳng hạn như 0,25, 0,25, 0,25, 0,25, 0,25.

Chúng ta lấy mẫu từ phân bố này, và vì nó là phân bố đều nên cuối cùng chúng ta thực hiện một hành động ngẫu nhiên, hình 4.5.

Chúng tôi tiếp tục thực hiện các hành động bằng cách lấy mẫu từ phân phối hành động đã tạo cho đến khi kết thúc tập.

Hình 4.5. Tổng quan chung về các mức độ chính sách dành cho một môi trường có bốn hành động riêng biệt có thể thực hiện được.

Đầu tiên, chúng tôi nhập trạng thái vào mạng chính sách, mạng này tạo ra phân phối xác suất cho các hành động và sau đó chúng tôi lấy mẫu từ phân phối này để thực hiện một hành động tạo ra trạng thái mới.

Hãy nhớ rằng, một số trò chơi như thế giới lưới có tính chất theo từng tập, nghĩa là có điểm bắt đầu và điểm kết thúc được xác định rõ ràng cho một tập của trò chơi.

Trong thế giới dạng lưới, chúng ta bắt đầu trò chơi ở một số trạng thái ban đầu và chơi cho đến khi chạm hố, tiếp đất vào khung thành hoặc thực hiện quá nhiều nước đi.

Vì vậy, một tập là một chuỗi các trạng thái, hành động và phần thưởng từ trạng thái ban đầu đến trạng thái cuối nơi chúng ta thắng hoặc thua trò chơi.

Chúng tôi ký hiệu tập phim này là...

Biểu hiện này.

Mỗi bộ dữ liệu là một bước của trò chơi thế giới lưới hoặc quy trình quyết định Markov nói chung.

Sau khi xem hết tập phim vào thời điểm t, chúng tôi đã thu thập được một loạt dữ liệu lịch sử về những gì vừa xảy ra.

Giả sử rằng chúng tôi tình cờ đạt được mục tiêu chỉ sau ba nước đi do mạng lưới chính sách của chúng tôi xác định. Đây là tập phim của chúng tôi trông như thế nào.

Xem biểu hiện này.

Chúng tôi đã mã hóa các hành động dưới dạng số nguyên từ 0 đến 3, đề cập đến các chỉ số mảng của vectơ hành động và chúng tôi để lại các trạng thái được biểu thị bằng ký hiệu vì chúng thực sự là các vectơ có độ dài 64.

Có gì để học hỏi trong tập phim này? Chà, chúng tôi đã thắng trò chơi, được biểu thị bằng phần thưởng cộng 10 trong bộ dữ liệu cuối cùng, vì vậy hành động của chúng tôi chắc chắn là tốt ở một mức độ nào đó.

Với tình trạng hiện tại của chúng tôi, chúng tôi nên khuyến khích mạng lưới chính sách của mình thực hiện những hành động đó có nhiều khả năng xảy ra hơn vào lần tới.

Chúng tôi muốn củng cố những hành động đã dẫn đến phần thưởng tích cực tốt đẹp đó.

Chúng tôi sẽ giải quyết những gì xảy ra khi đại lý của chúng tôi thua cuộc, nhận được phần thưởng cuối cùng là âm 10 ở phần sau trong phần này, nhưng trong thời gian chờ đợi, chúng tôi sẽ tập trung vào việc củng cố tích cực.

Mục 4.2.2, tăng cường hành động.

Chúng tôi muốn thực hiện các cập nhật nhỏ, mượt mà cho độ dốc của mình để khuyến khích mạng chỉ định nhiều xác suất hơn cho những hành động chiến thắng này trong tương lai.

Hãy tập trung vào trải nghiệm cuối cùng trong tập với trạng thái S2.

Hãy nhớ rằng, chúng tôi giả định mạng chính sách của chúng tôi tạo ra phân bố xác suất hành động 0,25, 0,25, 0,25, 0,25, 0,25, vì nó chưa được huấn luyện.

Và ở bước thời gian cuối cùng, chúng ta thực hiện hành động 3, tương ứng với yếu tố 4 trong mảng xác suất hành động, kết quả là chúng ta thắng trò chơi với phần thưởng cộng 10.

Chúng tôi muốn củng cố tích cực hành động này, với trạng thái S2, sao cho bất cứ khi nào mạng chính sách gặp S2 hoặc một trạng thái rất giống nhau, nó sẽ tự tin hơn khi dự đoán hành động 3 là hành động có xác suất cao nhất sẽ thực hiện.

Một cách tiếp cận đơn giản có thể là thực hiện phân phối hành động mục tiêu 0 0 0 1, sao cho độ dốc giảm dần của chúng ta sẽ di chuyển các xác suất từ ​​0,25, 0,25, 0,25, gần đến 0 0 0 1, có thể kết thúc là 0,167, 0,167, 0,167, 0,5, xem hình 4.6.

Đây là điều chúng tôi thường làm trong lĩnh vực học tập có giám sát khi đào tạo bộ phân loại hình ảnh dựa trên softmax.

Nhưng trong trường hợp đó, chỉ có một phân loại chính xác duy nhất cho một hình ảnh và không có mối liên hệ tạm thời nào giữa mỗi dự đoán.

Trong trường hợp RL của chúng tôi, chúng tôi muốn có nhiều quyền kiểm soát hơn đối với cách chúng tôi thực hiện những cập nhật này.

Đầu tiên, chúng tôi muốn thực hiện các cập nhật nhỏ, mượt mà vì chúng tôi muốn duy trì một số tính ngẫu nhiên trong lấy mẫu hành động của mình để khám phá môi trường một cách đầy đủ.

Thứ hai, chúng ta muốn có thể đợi xem chúng ta gán bao nhiêu tín dụng cho mỗi hành động cho các hành động trước đó.

Chúng ta hãy xem lại một số ký hiệu khác trước khi đi sâu vào hai vấn đề này.

Hình 4.6. Khi một hành động được lấy mẫu từ phân phối xác suất của mạng chính sách, nó sẽ tạo ra trạng thái và phần thưởng mới.

Tín hiệu khen thưởng được sử dụng để củng cố hành động đã được thực hiện, nghĩa là nó làm tăng xác suất thực hiện hành động đó nếu trạng thái là tích cực.

Hoặc nó làm giảm xác suất nếu phần thưởng âm.

Lưu ý rằng chúng ta chỉ nhận được thông tin về hành động 3, phần tử 4, nhưng vì xác suất phải có tổng bằng 1 nên chúng ta phải hạ xác suất của các hành động khác xuống.

Hãy nhớ lại rằng mạng chính sách của chúng ta thường được ký hiệu là pi theta khi chúng ta chạy nó về phía trước, nghĩa là sử dụng nó để tạo ra xác suất hành động.

Bởi vì chúng tôi coi các tham số mạng, theta là cố định và trạng thái đầu vào là thứ thay đổi.

Do đó, việc gọi pi theta của s cho một số trạng thái s sẽ trả về phân bố xác suất cho các hành động có thể xảy ra với một bộ tham số cố định.

Khi đào tạo mạng chính sách, chúng ta cần thay đổi các tham số đối với đầu vào cố định để tìm một tập hợp tham số tối ưu hóa mục tiêu của chúng ta, nghĩa là giảm thiểu dưới dạng tổn thất hoặc tối đa hóa dưới dạng hàm tiện ích.

Đó là hàm pi s của theta.

Sự định nghĩa.

Xác suất của một hành động dựa trên các tham số của mạng chính sách được ký hiệu là pi sub s của một theta nhất định.

Điều này làm rõ rằng xác suất của một hành động a phụ thuộc rõ ràng vào việc tham số hóa của mạng chính sách.

Nói chung, chúng ta biểu thị xác suất có điều kiện là phân bố xác suất trên x cho trước y.

Điều này có nghĩa là chúng ta có một hàm nào đó nhận tham số y và trả về phân bố xác suất trên một số tham số x khác.

In order to reinforce action 3, we want to modify our policy network parameters theta such that we increase pi s of a3 given theta.

Hàm mục tiêu của chúng ta chỉ cần tối đa hóa pi s của a3 cho trước theta trong đó a3 là hành động 3 trong ví dụ của chúng ta.

Trước khi huấn luyện, pi s của a3 cho theta bằng 0,25.

Nhưng chúng ta muốn sửa đổi theta sao cho pi s của a3 cho theta lớn hơn 0,25.

Bởi vì tất cả các xác suất của chúng ta phải có tổng bằng 1, nên việc tối đa hóa số pi của a3 cho trước theta sẽ giảm thiểu các xác suất hành động khác.

Và hãy nhớ rằng, chúng ta muốn thiết lập mọi thứ để giảm thiểu hàm mục tiêu thay vì tối đa hóa, vì nó hoạt động tốt với các đèn pin pi được tích hợp trong trình tối ưu hóa.

Thay vào đó, chúng ta nên yêu cầu đèn pin pi giảm thiểu 1 trừ pi s của một theta đã cho.

Hàm mất mát này tiến tới 0 khi pi s của theta cho trước gần 1.

Vì vậy, chúng tôi đang khuyến khích các gradient tối đa hóa số pi của một theta nhất định cho hành động mà chúng tôi đã thực hiện.

Sau đó, chúng tôi sẽ bỏ chỉ số dưới a3 vì nó phải rõ ràng trong ngữ cảnh mà chúng tôi đang đề cập đến hành động nào.

Mục 4.2.3, log xác suất.

Về mặt toán học, những gì chúng tôi mô tả là đúng.

Nhưng do tính toán chính xác nên chúng tôi cần điều chỉnh công thức này để ổn định quá trình huấn luyện.

Một vấn đề là xác suất bị giới hạn bởi 0 và 1 theo định nghĩa.

Vì vậy, phạm vi giá trị mà trình tối ưu hóa có thể hoạt động bị hạn chế và nhỏ.

Đôi khi xác suất có thể cực kỳ nhỏ hoặc rất gần bằng 1 và điều này dẫn đến các vấn đề về số khi tối ưu hóa trên máy tính có độ chính xác số hạn chế.

Thay vào đó, nếu chúng ta sử dụng một mục tiêu thay thế, cụ thể là logarit tự nhiên âm của pi s của một theta đã cho, trong đó log là logarit tự nhiên.

Chúng tôi có mục tiêu có phạm vi động lớn hơn không gian xác suất thô, vì nhật ký của không gian xác suất nằm trong khoảng từ âm vô cực đến 0.

Và điều này làm cho xác suất log dễ tính toán hơn.

Hơn nữa, logarit có một tính chất rất hay là logarit của tích a và b bằng tổng logarit của a và logarit của b.

Điều đó có nghĩa là khi chúng ta nhân các xác suất log, chúng ta có thể biến phép nhân này thành một tổng, cũng ổn định hơn về mặt số lượng so với phép nhân.

Nếu chúng ta đặt mục tiêu của mình là logarit tự nhiên âm của số pi s của một theta nhất định thay vì 1 trừ pi s của một theta nhất định, thì sự mất mát của chúng ta vẫn tuân theo trực giác rằng hàm mất mát tiến tới 0 khi pi s của theta nhất định tiến tới 1.

Độ dốc của chúng tôi sẽ được điều chỉnh để cố gắng tăng pi s của theta nhất định lên 1, trong đó hành động bằng 3 cho ví dụ đang chạy của chúng tôi.

Mục 4.2.4, phân bổ tín chỉ. Hàm mục tiêu của chúng ta là logarit tự nhiên âm của số pi s của một theta nhất định, nhưng hàm này gán trọng số bằng nhau cho mọi hành động trong tập của chúng ta.

Trọng số trong mạng tạo ra hành động cuối cùng sẽ được cập nhật ở mức độ tương tự như hành động đầu tiên. Tại sao điều đó không nên như vậy?

Chà, thật hợp lý khi hành động cuối cùng ngay trước phần thưởng xứng đáng được ghi nhận nhiều hơn khi giành chiến thắng trong trò chơi so với hành động đầu tiên trong tập.

Theo tất cả những gì chúng tôi biết, hành động đầu tiên thực sự chưa tối ưu, nhưng sau đó chúng tôi đã quay trở lại và đạt được mục tiêu.

Nói cách khác, niềm tin của chúng ta về mức độ tốt của mỗi hành động sẽ giảm đi khi chúng ta càng xa điểm khen thưởng.

Trong một ván cờ, chúng ta cho rằng nước đi cuối cùng được thực hiện nhiều hơn nước đi đầu tiên.

Chúng tôi rất tự tin rằng nước đi trực tiếp dẫn chúng tôi đến chiến thắng là một nước đi tốt, nhưng chúng tôi càng trở nên kém tự tin hơn khi càng lùi về phía sau.

Nước đi cách đây 5 lần bước đóng góp bao nhiêu vào chiến thắng? Chúng tôi không chắc lắm. Đây chính là vấn đề phân bổ tín dụng.

Chúng tôi thể hiện sự không chắc chắn này bằng cách nhân độ lớn của bản cập nhật với hệ số chiết khấu mà bạn đã học ở chương ba trong khoảng từ 0 đến 1.

Hành động ngay trước khi tập kết thúc sẽ có hệ số chiết khấu là 1, nghĩa là nó sẽ nhận được bản cập nhật độ dốc đầy đủ, trong khi các bước di chuyển trước đó sẽ được chiết khấu theo một phần nhỏ chẳng hạn như 0,5, do đó các bước độ dốc sẽ nhỏ hơn.

Hãy thêm những thứ đó vào mục tiêu, mất mát, chức năng của chúng ta.

Hàm mục tiêu cuối cùng mà chúng ta sẽ yêu cầu pi torch giảm thiểu là âm gamma t nhân gt nhân log pi s của một theta cho trước.

Hãy nhớ rằng, gamma t là hệ số chiết khấu và chỉ số dưới t cho chúng ta biết giá trị của nó sẽ phụ thuộc vào bước thời gian t vì chúng ta muốn chiết khấu những hành động ở xa hơn những hành động gần đây.

Tham số gt được gọi là tổng lợi nhuận hoặc lợi nhuận tương lai tại thời điểm t. Đó là số tiền hoàn lại mà chúng tôi mong đợi thu được từ bước thời gian t cho đến khi kết thúc tập và có thể tính gần đúng bằng cách cộng phần thưởng từ trạng thái nào đó trong tập cho đến cuối tập.

Xem biểu hiện này.

Hành động cuối cùng dẫn đến trạng thái chiến thắng cộng một và nó không hề bị giảm giá. Hành động trước đó được chỉ định phần thưởng theo tỷ lệ bằng cách nhân phần thưởng cuối cùng với kết quả cuối cùng trả về.

Hành động cuối cùng dẫn đến trạng thái chiến thắng cộng một và nó không hề bị giảm giá.

Hành động trước đó được chỉ định phần thưởng theo tỷ lệ bằng cách nhân phần thưởng cuối cùng với gamma t trừ đi một hệ số chiết khấu mà chúng tôi đã đặt thành 0,99.

Mức chiết khấu giảm dần theo cấp số nhân từ một. Gamma t bằng gamma 0 với lũy thừa của tổng số bước thời gian, trừ đi bước thời gian địa phương cho một hành động cụ thể, nghĩa là chiết khấu tại bước thời gian địa phương cho một hành động cụ thể.

Bước tiếp theo cho một hành động cụ thể được tính là mức chiết khấu bắt đầu, ở đây là 0,99, được tính theo khoảng thời gian nguyên tính từ phần thưởng.

Độ dài của tập, tổng số bước thời gian, được ký hiệu là chữ t và bước thời gian cục bộ cho một hành động cụ thể là chữ thường t.

Tổng số bước thời gian trừ đi bước thời gian địa phương cho một hành động cụ thể bằng 0. Gamma tổng số bước thời gian trừ 0 bằng 0,99 lũy thừa 0 bằng 1.

Vì tổng số bước thời gian trừ bước thời gian địa phương cho một hành động cụ thể bằng hai,

tổng số bước thời gian gamma trừ hai bằng 0,99 lũy thừa của hai bằng 0,9801, v.v.

Mỗi lần lùi lại, hệ số chiết khấu được lũy thừa theo khoảng cách từ bước cuối cùng,

dẫn đến sự phân rã theo cấp số nhân của hệ số chiết khấu, càng xa vời và không liên quan,

hành động đó là kết quả khen thưởng.

Ví dụ: nếu tác nhân ở trạng thái S0 thì đó là bước thời gian t bằng 0,

và nó thực hiện hành động a1 và nhận phần thưởng tt cộng 1 bằng trừ 1,

bản cập nhật mục tiêu sẽ là cái này, là đầu ra xác suất nhật ký từ mạng chính sách,

hình 4.7.

Hình 4.7, sơ đồ chuỗi để huấn luyện mạng chính sách cho thế giới lưới.

Mạng chính sách là mạng thần kinh được tham số hóa bởi theta, các trọng số,

chấp nhận vectơ 64 chiều cho trạng thái đầu vào.

Nó tạo ra sự phân bố xác suất 4 chiều riêng biệt cho các hành động.

Hộp hành động mẫu lấy mẫu một hành động từ phân phối và tạo ra một số nguyên làm hành động,

được trao cho môi trường để tạo ra trạng thái và phần thưởng mới,

và hàm mất mát để chúng ta có thể củng cố hành động đó.

Tín hiệu phần thưởng cũng được đưa vào hàm mất,

mà chúng tôi cố gắng giảm thiểu đối với các tham số mạng chính sách.
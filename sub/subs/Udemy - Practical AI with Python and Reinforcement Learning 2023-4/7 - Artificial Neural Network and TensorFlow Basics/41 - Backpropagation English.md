# 41 - Lan truyền ngược tiếng Anh

---

Chào mừng mọi người trở lại với bài giảng về lan truyền ngược này.

Chủ đề cuối cùng mà chúng ta sẽ đề cập đến là sự lan truyền ngược và chúng ta sẽ bắt đầu bằng cách cố gắng

xây dựng một trực giác đằng sau việc truyền ngược và sau đó chúng ta sẽ đi sâu vào phép tính và ký hiệu của phép truyền ngược

sự lan truyền.

Tôi muốn chỉ ra rằng lan truyền ngược có lẽ là phần khó nhất trong toàn bộ chiều sâu lý thuyết.

quá trình học tập vì phép tính và ký hiệu liên quan đến phép tính đó, đặc biệt là khi chúng ta

bắt đầu nói về sự lan truyền ngược và xử lý một ma trận trọng số trong một ma trận sai lệch khác.

Vì vậy, hãy ghi nhớ điều đó.

Điều này sẽ khá khó khăn, đặc biệt nếu bạn đang dựa vào ký hiệu phép tính của mình.

Tuy nhiên, với ý nghĩ đó, nếu bạn hiểu được trực giác cơ bản thì về cơ bản bạn chỉ cần lùi lại

thông qua mạng để cập nhật trọng số và độ lệch, thì điều đó thực sự đủ để tiếp tục

phần còn lại của khóa học.

Vì vậy, nếu bạn chưa hiểu rõ phần tính toán của bài giảng này, đừng lo lắng quá nhiều về điều đó, bởi vì

không phải là bạn sẽ cần phải tự mình tính toán độ dốc.

Mã thực tế sẽ làm điều đó cho chúng tôi.

Vì vậy, về cơ bản, chúng tôi muốn biết kết quả của hàm chi phí thay đổi như thế nào đối với các trọng số

trong mạng, bằng cách đó chúng ta có thể cập nhật các trọng số để giảm thiểu hàm chi phí.

Và chúng tôi thực sự đã nói một chút về điều đó khi nói về những thứ như giảm độ dốc và cách

nó tiếp cận hàm chi phí.

Vì vậy, chúng ta hãy bắt đầu với một mạng rất đơn giản để hiểu được sự lan truyền ngược của nó.

Vì vậy, đây là một mạng siêu đơn giản.

Về cơ bản, mỗi lớp chỉ có một nơ-ron.

Vì vậy, chúng ta sẽ xem quá trình lan truyền ngược hoạt động như thế nào chỉ với một mạng lưới gồm một vài nơ-ron.

Và sau đó chúng ta có thể dễ dàng mở rộng điều này sang các mạng có nhiều nơ-ron trên mỗi lớp.

Vì vậy, như chúng ta đã biết, về cơ bản, mỗi đầu vào đều nhận được trọng số và độ lệch, do đó sẽ có đầu vào

trọng số được gắn vào cạnh và sau đó là từng nút hoặc nghĩa là mỗi nơ-ron có độ lệch riêng.

Vì vậy, chúng ta có được loại công thức trọng số một cộng độ lệch, một chiều đến độ lệch, trọng số ba cộng độ lệch ba

và vân vân.

Vì vậy, điều này có nghĩa là chúng ta có một số loại hàm chi phí phụ thuộc vào các trọng số và độ lệch đó.

Và chúng ta đã thấy quá trình này lan truyền về phía trước như thế nào, vì vậy hãy tiếp tục và bắt đầu từ cuối

để tìm hiểu về lan truyền ngược.

Vì vậy, chúng tôi đã lưu ý rằng cách chúng tôi ký hiệu các lớp là đặt lớp cuối cùng được gọi là EL sao cho

ký hiệu của chúng ta là Neron ở bên phải hoàn toàn nằm trong lớp, vậy thì bạn đang chuyển sang

bên trái của nó là L trừ một, L trừ hai, v.v. cho L trừ N lớp.

Bây giờ, hãy tiếp tục và chỉ tập trung vào hai lớp cuối cùng của mạng của chúng ta, bởi vì lan truyền ngược

bắt đầu từ cuối lớp mạng L sau khi chúng tôi đã hoàn tất quá trình chuyển tiếp nguồn cấp dữ liệu của mình

và chúng ta đang tập trung vào hai lớp này, tôi muốn nhắc nhở bản thân về ký hiệu chúng ta đang sử dụng

cho đến nay.

Chúng ta đã định nghĩa Z là W nhân X cộng B và X gợi lại X, ký hiệu đó của X thực sự chỉ có giá trị

ở lớp đầu tiên vì X là viết tắt của các đầu vào tính năng thô thực tế.

Khi bạn tiếp tục đi từ nơ-ron này sang nơ-ron khác vào lớp X về mặt kỹ thuật sẽ trở thành đầu ra của

nơ-ron trước đó, được định nghĩa là bởi vì.

Hãy nhớ rằng, sau khi chúng tôi áp dụng hàm kích hoạt cho Z chẳng hạn như Sigmoid của Z, chúng tôi gắn nhãn đó là ..

Vì vậy, khi bạn đi sâu hơn vào các lớp này, Z thực sự sẽ bằng Z bằng hai nhân A cộng

B, vì X về mặt kỹ thuật chỉ có giá trị ở lớp đầu tiên làm đầu vào tính năng thô.

Khi bạn thực sự chuyển nó vào tế bào thần kinh, về mặt kỹ thuật, bạn sẽ không xử lý các tính năng thô nữa.

Thay vào đó, bạn đang xử lý đầu ra của lớp nơ-ron trước đó, lớp này được phát biểu tốt hơn là

sigmoid của Z hoặc bất kỳ hàm kích hoạt nào bạn chọn.

Được rồi, vậy điều đó thực sự có ý nghĩa gì khi chúng ta tính đến lớp cuối cùng đó?

Chà, điều đó có nghĩa là Z ở lớp cuối cùng sẽ bằng với các trọng số đó ở thời gian của lớp cuối cùng

A của L trừ một.

Vậy một điểm trừ là gì?

Chà, khoảng trừ một chỉ đơn giản là đầu ra của Neron của lớp trước đó.

Vì vậy, L trừ một, cộng với Bevell, Bias ở lớp cuối cùng.

Vì vậy, một lần nữa, vì l nên đầu ra của hàm kích hoạt ở lớp cuối cùng đó bằng sigmoid hoặc

hàm kích hoạt bằng 0.

Vì vậy Nurse Hacia El được xác định bởi các trọng số và Bias ở lớp L đó và sau đó nó được xác định bởi

đầu ra của nơron trước đó.

Vì vậy, hy vọng bạn có thể tạo ra những kết nối này.

Và điều đó có nghĩa là khi đó hàm chi phí sẽ bằng RFL trừ Y, hoặc tại sao giá trị thực tế lại là

sản lượng thực bình phương?

Vì vậy, điều chúng tôi thực sự muốn hiểu là độ nhạy của hàm chi phí đối với những thay đổi của W. Và điều này

là nơi phát huy tác dụng của đạo hàm riêng vì chúng ta muốn tìm ra mối quan hệ giữa điều đó

hàm chi phí cuối cùng và trọng số trong trường hợp này tại LORELLE.

Vì vậy, chúng ta sẽ lấy đạo hàm riêng của hàm chi phí đó theo trọng số và

lớp el.

Và nếu bạn biết một số phép tính, thì bạn biết rằng có một quy tắc dây chuyền.

Và vì vậy nếu bạn lấy các công thức chúng ta vừa thấy ở đây và áp dụng quy tắc dây chuyền cho chúng theo thứ tự

để giải đạo hàm riêng mà chúng ta đã đề cập ở đây, bởi vì chúng ta muốn hiểu mối quan hệ

giữa hàm chi phí đó và các trọng số trong mạng.

Sau đó, bạn kết thúc việc tính toán công thức này.

Vì vậy, đây chỉ là quy tắc dây chuyền về cơ bản cho phép bạn lấy đạo hàm của một hàm trong

một chức năng.

Vì vậy, ở đây bạn thấy một số phép tính với quy tắc dây chuyền.

Chúng ta có thể xác định rằng đạo hàm riêng của hàm chi phí đó đối với các trọng số đó bằng nhau

với đạo hàm riêng của Z theo trọng số lần, đạo hàm riêng của

A đối với Z lần, một phần của hàm chi phí đối với quy tắc dây chuyền cơ bản

cho phép chúng ta tách các hàm này ra trong các hàm vì chúng ta đã thấy từ ba công thức trước đó

rằng hàm chi phí được xác định bởi các xác nhận AFL, sau đó được xác định bởi ZEVALIN và Zavala được xác định bởi WOFL

Ambarvale.

Bây giờ, hãy nhớ lại rằng hàm chi phí không chỉ là hàm của các trọng số mà còn là hàm

của BIAS'S, vì vậy chúng tôi muốn có thể hiểu được mối quan hệ của việc hàm chi phí thay đổi chứ không phải

chỉ ở các trọng số có độ lệch dọc theo mạng, vì vậy sau đó chúng ta có thể tính toán phần tương tự

phái sinh.

Vì vậy, đạo hàm riêng của hàm chi phí đối với các số hạng byas đó theo cùng một cách, về cơ bản

chỉ là trao đổi trọng số đó để lấy độ lệch.

Bây giờ, ý tưởng chính ở đây là chúng ta có thể sử dụng gradient để quay lại mạng và điều chỉnh

trọng số và độ lệch của chúng tôi để giảm thiểu đầu ra của vectơ không khí trên lớp đầu ra cuối cùng đó.

Và hãy nhớ lại rằng gradient về cơ bản là đạo hàm khi bạn xử lý các kích thước.

Vì vậy, bằng cách sử dụng một số ký hiệu tính toán, chúng ta có thể mở rộng ý tưởng này sang các mạng có nhiều nơ-ron trên mỗi lớp

và sẽ có một số ký hiệu mà bạn sẽ thấy ngay sau đây, một lần nữa, nếu bạn là người

một chút hoen gỉ về đại số tuyến tính hoặc phép tính, nó được gọi là sản phẩm nghệ thuật Hatam.

Và nó thực sự là một sản phẩm mà bạn đã quen thuộc vì nó là sản phẩm mặc định với

không.

Và đây là những thư viện dành cho deep learning, nơi bạn thực sự đang thực hiện phép nhân một phần tử bằng cách nhân các phần tử.

Vì vậy, một lần nữa, tích Hatami, ký hiệu chấm nhỏ đó, trông hơi giống một

biểu tượng hydro.

Về cơ bản ý nghĩa của nó chỉ là thực hiện một phần tử bằng cách nhân phần tử.

Và điều đó có nghĩa là hai ma trận phải có cùng kích thước, điều này hợp lý vì đó là

sẽ phù hợp với những thứ như trọng lượng và Bias.

Vì vậy, với ký hiệu này và lan truyền ngược, chúng ta chỉ cần có một số bước chính để huấn luyện mạng nơ-ron

bây giờ.

Không, một lần nữa, bạn không cần phải hiểu đầy đủ những chi tiết phức tạp này về phép tính hoặc ký hiệu

để tiếp tục với các phần viết mã của khóa học này.

Bây giờ chúng ta hãy xem lại quá trình học tập thực tế của một mạng.

Chúng ta bắt đầu chỉ với quy trình chuyển tiếp nguồn cấp dữ liệu rất cơ bản mà chúng ta đã quen thuộc ở bước một,

sử dụng đầu vào X, tức là các tính năng ban đầu, chúng tôi đặt hàm kích hoạt A cho lớp đầu vào.

Vì vậy, lớp đầu vào đầu tiên đó có nghĩa là chúng ta có Z bằng W, X cộng với B và sau đó là A, tức là

về cơ bản đầu ra ra khỏi lớp đầu vào đó sẽ bằng với hàm kích hoạt của bạn về

Z trong trường hợp này được biểu diễn dưới dạng sigmoid của Z.

Vì vậy, kết quả AI này sẽ được đưa vào lớp tiếp theo.

Vì vậy, bạn có lớp tiếp theo lấy AI, nghĩa là Z của nó sẽ bằng W nhân A cộng B của

lớp trước đó.

Vì vậy, sau đó bạn đi vào lớp tiếp theo và sau đó bạn lấy đầu ra của lớp đó, dán nó vào Z, thế là xong

và vân vân.

Vì vậy, chúng tôi nghĩ về điều này cho từng lớp, tất cả những gì chúng tôi đang làm là tính toán các Zeze và ASW đó vì

A dựa trên Z.

Vì vậy, nếu tôi gặp ở một nơi khác, thì điều tôi sẽ làm là đặt Z của lớp L hiện tại bằng

với các trọng số ở mức L nhân với đầu ra từ lớp trước đó là L trừ một, cộng với độ lệch

của lớp hiện tại của tôi.

Bevell, khi tôi đã có cấp độ của mình, tôi sẽ chuyển cấp độ đó qua chức năng kích hoạt của mình, trong trường hợp này

sigmoid.

Và sau đó tôi nhận được AI, lớp L hiện tại của tôi và sau đó tôi có thể chuyển nó sang lớp L cộng một tiếp theo

vân vân và vân vân.

Và sau đó chúng ta đến bước ba và ở đây chúng ta đã viết nó ra bằng ký hiệu tính toán đầy đủ của máy tính

vectơ lỗi của chúng tôi, nhưng về cơ bản điều chúng tôi muốn làm là nếu bạn xem xét và tập trung vào chính điều đó

số hạng đầu tiên, tất cả những gì nó đang làm về cơ bản là biểu thị tốc độ thay đổi của hàm chi phí đó với

liên quan đến kích hoạt đầu ra.

Và trong trường hợp của hàm chi phí bậc hai, thì về cơ bản điều đó cũng giống như việc nói

kích hoạt lớp đầu ra cuối cùng trừ Y, đó là giá trị thực.

Và về cơ bản điều chúng tôi muốn làm là có thể tính toán vectơ lỗi này và ngược lại, truyền bá nó,

về cơ bản tính toán lại lỗi qua từng lớp khác.

Bằng cách đó, chúng tôi có thể điều chỉnh trọng số và độ lệch cho lỗi đó.

Vì vậy, thay thế số hạng đầu tiên đó bằng chữ L viết hoa trừ Y, chúng ta nhận được công thức sau và một lần nữa, lý do

có sản phẩm được đánh dấu ở đây.

Vì vậy, điều tôi muốn làm là viết một công thức vectơ lỗi tổng quát và tôi sẽ viết nó

về lỗi ở lớp tiếp theo, điều này rất có ý nghĩa vì tất cả những gì chúng tôi đang làm là

chúng ta đang lùi lại.

Và một lưu ý nhanh thực sự ở đây là hơi khó để tìm một phông chữ hoặc chữ L viết thường trông khác với

số một.

Vì vậy, tôi có hai gạch đầu dòng nhỏ ở đó để cho bạn thấy những gì tôi đang nói đến.

Vì vậy, chữ L viết thường về cơ bản trông giống như một đường thẳng.

Số một, nó có một dấu gạch ngang nhỏ ở trên.

Vì vậy, hãy ghi nhớ điều đó khi bạn thấy điều gì sẽ xảy ra tiếp theo.

Lý do tôi sẽ không sử dụng chữ L viết hoa là vì nói chung chúng ta nên sử dụng chữ L viết hoa

để biểu thị lớp đầu ra cuối cùng.

Và điều tôi muốn làm là chỉ cho bạn công thức của vectơ lỗi và các phép tính đó cho bất kỳ lớp nào

L chữ thường L nằm trong mạng.

Vì vậy, những gì tôi sẽ làm là dành cho bước truyền ngược này cho mỗi lớp, bắt đầu từ chính

lớp cuối cùng Viết hoa L, sau đó chuyển sang viết hoa L trừ một, viết hoa L, trừ hai, vân vân, tất cả

cách cho tất cả các lớp này, khái quát rồi đến thuật ngữ lỗi.

Vì vậy, hạng lỗi delta với chữ L nhỏ hoặc chữ L viết thường sẽ bằng ma trận trọng số

L cộng một.

Đó là chữ L viết thường rồi hoán vị nó sao cho t thuật ngữ đó ở ngay đó, đó là chuyển vị của

ma trận trọng số và lớp tiếp theo ở phía bên phải của L cộng một, đó là chữ L viết thường và

sau đó chúng ta nhân chúng với số hạng lỗi ở lớp tiếp theo đó và sau đó chúng ta lấy phần đầu

của sản phẩm của chúng tôi một lần nữa với Z của L chuyển vào hàm kích hoạt.

Vì vậy, một lần nữa, tất cả những gì chúng ta đang làm là truyền ngược lại lỗi và ở đây chúng ta có lỗi tổng quát

cho bất kỳ lớp chữ thường L.

Vì vậy, khi chúng ta áp dụng ma trận trọng số chuyển vị thực tế đó, ma trận trọng số của L cộng với một chuyển vị,

chúng ta có thể nghĩ một cách trực quan về điều này giống như việc di chuyển không khí ngược qua mạng, mang lại cho chúng ta một số loại

đo lỗi ở đầu ra của lớp LTH đó.

Sau đó chúng tôi lấy Hatam, sản phẩm của chúng tôi vào thời điểm đó, Hatam, sản phẩm của chúng tôi về chữ Z lúc đó

lớp chuyển vào chức năng kích hoạt.

Và điều làm được là điều này sẽ chuyển lỗi ngược trở lại thông qua hàm kích hoạt.

Và Lorelle đã cho chúng tôi lỗi ở L. theo cách nhập dữ liệu vào lớp L..

Một lần nữa, đó là một thuật ngữ tổng quát, đó là lý do tại sao bạn thấy tôi sử dụng chữ L viết thường.

Và khi đó chúng ta có thể hiểu rằng độ dốc của hàm chi phí được cho bởi hai công thức này, gửi

cho mỗi lớp L trừ một, L trừ hai, v.v.

Tất cả những gì chúng tôi thực sự đang làm là tính đạo hàm riêng của hàm chi phí đối với

trọng số và độ lệch ở đó, và nghĩ rằng đó chỉ là ký hiệu cho chính các nơ-ron thực sự.

Sau đó, điều này cho phép chúng tôi điều chỉnh trọng số và độ lệch để giúp giảm thiểu hàm chi phí đó.

Vì vậy, tôi biết điều này khá khó hiểu về mặt ký hiệu của phép tính.

Và đừng lo lắng, nếu bạn không nhận được nó ngay lập tức, điều này thường mất ít nhất đối với tôi, chắc chắn là phải mất

một vài giờ để hiểu, chỉ cố gắng viết nó ra bằng giấy và bút chì.

Vì vậy, điều tôi đã làm là liên kết với bạn trong bài giảng này, một số liên kết bên ngoài bạn nên xem một chút

thư mục bật lên khi bạn đang xem bài giảng này hoặc ngay bên cạnh bài giảng có tiêu đề, bạn nên

thấy một thư mục thả xuống nhỏ.

Bạn có thể nhấp vào.

Có một số liên kết bên ngoài thực sự hoạt động và về cơ bản rút ra từng bước tất cả các phương trình này.

Vì vậy, nếu phần tổng quan này không đủ đối với bạn và bạn muốn xem từng bước cũng như toàn bộ nguồn gốc của

quá trình này, cộng với việc chứng minh các loại phương trình truyền ngược cơ bản bốn bước đó, hãy kiểm tra

ra các liên kết bên ngoài để biết nhiều chi tiết về điều đó.

Nhưng nếu bạn có sự hiểu biết chung rằng về cơ bản bạn đang tính toán sai số ngay từ đầu.

lớp cuối cùng rồi đi ngược lại qua mạng để tính toán tất cả các lỗi đó rồi điều chỉnh

trọng số và độ lệch tương ứng để giảm thiểu hàm chi phí đó, nếu bạn hiểu trực giác chung đó,

bạn biết đủ để tiếp tục và tiếp tục khóa học.

Được rồi, cảm ơn.

Và tôi sẽ gặp bạn ở bài giảng tiếp theo.
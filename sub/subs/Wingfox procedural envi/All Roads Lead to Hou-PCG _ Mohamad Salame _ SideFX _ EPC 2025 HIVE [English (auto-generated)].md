# Mọi con đường đều dẫn đến Hou-PCG Mohamad Salame SideFX EPC 2025 HIVE [Tiếng Anh (được tạo tự động)]

---

[Âm nhạc]

Bạn có muốn tạo cái này từ

gãi bằng cách sử dụng

Houdini và không thực

Động cơ? Một trò chơi hoàn toàn có thể chơi được

đấu trường, mô-đun, thủ tục và

có thể điều khiển được bằng

PCG. Các tập tin dự án có sẵn cho

tải xuống.

Tên tôi là Muhammad Salami, kỹ thuật viên

nghệ sĩ tại Side Effects Labs và đây là

một hội thảo APC về Houdini và PCG. bây giờ

trước khi chúng ta bắt đầu, hội thảo này là

dựa trên một loạt các hướng dẫn có sẵn

trên trang web tác dụng phụ. bạn có thể

tìm liên kết

bên dưới. nhanh chóng

tóm tắt lại. Sao chép vào điểm, về cơ bản là vậy

toàn bộ quy trình làm việc trong Houdini và trong

PCG.

Chúng tôi có một danh sách các mắt lưới và một điểm

đám mây đưa vào một bản sao tới các điểm với

một thuộc tính mảnh để khớp với từng lưới

mong muốn

điểm. Đây là

mắt lưới. Những mắt lưới này mang tính thủ tục. cho

Ví dụ, cây cột này đang sử dụng một cái ống và

các đường cong boolean, ép đùn, PDB, v.v.

Và các khe nguyên liệu từ các nhóm là

chỉ định nhiều tài liệu trong Unreal. Và

đây là đám mây điểm. Mỗi lưới có một

thuộc tính ID điểm

giá trị. Các điểm được sao chép là dành cho

chỉ trực quan hóa.

Đám mây điểm và các mắt lưới là những gì

là cần thiết cho

PCG. Chúng ta có thể xuất điểm

đám mây bằng cách sử dụng bảng dữ liệu CSV hoặc

Olympic. Tôi sẽ không đề cập đến CSV

phương pháp trong hội thảo này như nó vốn có

được phát triển cho Unreal 5.2 và 5.3. các

phương pháp được đề xuất là Olympic

tồn tại ở phiên bản 5.4 trở lên. Nút Olympic

xuất đám mây điểm với các thuộc tính.

Hãy chắc chắn rằng điểm của bạn có định hướng

thuộc tính để xoay và được chuẩn hóa

giữa số không và một. Chia tỷ lệ từ 100 đến

phù hợp với quy mô đơn vị Unreal.

Sử dụng lưới sinh sản tĩnh trong PCG với

loại bộ chọn lưới được đặt thành lưới PCG

được chọn theo thuộc tính cho phép chúng tôi khớp

và thiết lập danh sách các mắt lưới đến điểm

đám mây dựa trên một mảnh ID lưới

thuộc tính. Chúng tôi sử dụng tài sản dữ liệu để lưu trữ

danh sách các mắt lưới. Tạo một strct với

một lưới tĩnh và một số nguyên. Tạo một

bản thiết kế của loại tài sản dữ liệu chính.

Và cuối cùng tạo một nội dung dữ liệu để lưu giữ

đường dẫn lưới và ID lưới. Đây là

nội dung dữ liệu trông như thế nào. Đó là một

danh sách các mắt lưới có số nguyên

tương ứng với mỗi lưới đại diện

lưới của nó

ID. Tải ellic đọc điểm

đám mây. Khởi tạo thiết lập mẫu thành phố

làm việc với Houdini

biến đổi. Khi nhập lại điểm

đám mây sử dụng Olympic, bạn phải xả nước

bộ đệm. Bạn có thể làm điều đó bằng cách giữ

kiểm soát và lực lượng tạo ra khác

sẽ không có gì

cập nhật. Đây là thiết lập nút đầy đủ trong

PCG không có thật. So khớp và đặt thuộc tính

nút giống như sao chép vào điểm

ở Houdini. Bạn có thể sao chép các lưới tĩnh

đến điểm và vật liệu tĩnh

mắt lưới. Bạn cũng có thể sinh ra các diễn viên.

Nội dung dữ liệu đi vào thuộc tính get

từ nút đường dẫn đối tượng vào trận đấu và thiết lập

nút thuộc tính khớp với ID lưới

giữa đám mây điểm và danh sách

mắt lưới. Bạn có thể ghi đè nhiều

vật liệu trên mỗi lưới nếu mắt lưới của bạn có

nhiều hơn một

vật chất. Tôi đã sử dụng đổi tên thuộc tính thành

đổi tên khe vật liệu đầu tiên để tôi

không phải tạo strct mới cho mỗi

khe vật liệu. Đây là một ví dụ về

ghi đè vật liệu. Con lợn được làm bằng

hộp và hình cầu. Tôi đã sử dụng môi trường xung quanh

tắc mềm để tính toán

chuyển màu, sau đó gán vật liệu tối hơn

đến vùng tối hơn và vùng sáng hơn

vật liệu vào bật lửa

các khu vực. Bạn có thể trao đổi các lưới proxy của mình

với phiên bản cuối cùng chỉ bằng cách

cập nhật dữ liệu

tài sản. Đây là một ví dụ về tán lá cách điệu

sử dụng cùng Houdini Olympic để Unreal

phương pháp PCG

Tất cả chúng ta đều biết những người này. Mỗi một trong số

những mảnh Lego này là một ví dụ. Đó là

không tệ. PCG có thể xử lý nhiều

trường hợp. Sử dụng một thuộc tính để ghi đè

vật liệu và nhiều thuộc tính cho

nhiều vật liệu trên mỗi lưới.

Bởi vì chúng tôi đang sử dụng Houdini nên chúng tôi có thể làm

Những thứ Houdini như biến một

xây dựng thành

Lego. Sử dụng bộ lọc thuộc tính, chúng ta có thể

lọc theo lưới

ID. Đây là một ví dụ thú vị về việc lọc theo

thuộc tính khi chạy.

Đây là một đám mây điểm từ ma trận

demo. Tòa nhà đơn giản

mắt lưới và đây là nó trong Unreal bằng cách sử dụng

PCG. Đây là một con đường

ví dụ. Bạn có thể vẽ chúng bằng một đường cong

nút ở Houdini.

và dễ dàng trao đổi tài sản dữ liệu để chuyển đổi

giữa đường và

đường ống. Hoặc nếu bạn muốn tạo ra prefabs,

bạn có thể sử dụng phương pháp tương tự để sinh sản

diễn viên thay vì tĩnh

mắt lưới. Một ví dụ khác về PCG sử dụng

thực tế

tài sản. Đây là một ví dụ thú vị, nhưng nó

quá chậm. Tôi không khuyên bạn nên hoạt hình

PCG điểm bất cứ lúc nào, nhưng có thể trong

tương lai. Được rồi, quay lại tập tin ví dụ của chúng tôi.

Hãy thực hiện một số thay đổi cho tòa nhà này.

Hãy theo dõi nếu bạn có

các tập tin dự án

mở. Trong Unreal, mở biểu đồ PCG và

bỏ qua Olympic

nướng. Chúng tôi cần cái mới nhất

những thay đổi. Đảm bảo nút Olympic của bạn được

đọc đúng tập tin.

Giữ quyền kiểm soát để buộc tạo ra

thuộc hệ viền

những thay đổi. Đây là tài sản dữ liệu. bạn có thể

hãy xem nó đang sử dụng ID s chứ không phải ID lưới cho

thuộc tính mảnh. tôi sẽ giải thích

sau này. Và lưới sinh sản tĩnh là

sử dụng thuộc tính lưới cho đường dẫn lưới.

Được rồi, hãy tăng độ khó và xây dựng

một đường may che phủ. Đầu tiên, chúng ta nhìn vào

cách làm sai

mọi thứ. Vấn đề với việc lập mô hình với

nút là bạn không biết nút nào

tương ứng với phần nào của tòa nhà.

Và mỗi lần bạn muốn chỉnh sửa nó

một phần, bạn phải đi tìm

nút trong cấu trúc nút khổng lồ. Đó là

thực sự khó chịu. Có phải cái này không? Có phải không?

cái này à? Không. Không, không,

không. Tìm thấy nó.

Và bây giờ tôi có thể làm việc của mình

chỉnh sửa. Điều gì sẽ xảy ra nếu chúng ta làm

mô-đun và sử dụng HDA với Python

trạng thái để đặt các mô-đun?

sau đó tạo đấu trường từ

ở đó. Hãy nhớ rằng HDA này cần phải

xuất ra một đám mây điểm và một danh sách

lưới để xuất sang

PCG. Tôi đã làm ba cái độc đáo

làn đường, sau đó uốn cong chúng và ví dụ chúng.

Vấn đề với lưới uốn là

chúng hẹp hơn ở gần trung tâm

và xa trung tâm hơn. Vì vậy chúng tôi

cần một thuộc tính biến thể bổ sung để

theo dõi những thay đổi dọc theo

trục x. Vì vậy bây giờ chúng ta có một ID lưới và một

ID biến thể. Nhưng việc sao chép vào điểm có thể

chỉ lấy thuộc tính một mảnh. Vậy làm thế nào

chúng ta có thể làm cho việc sao chép thành điểm mất nhiều thời gian hơn không

hơn một thuộc tính chỉ có một mảnh

thuộc tính? bất kỳ

suy nghĩ? Một cách hay để theo dõi

các biến thể cùng với id lưới là bởi

nối các id lưới và

id biến thể trong thuộc tính chuỗi.

Một cái gì đó giống như

1_1 gạch dưới 2 1ore 3, v.v. Sau

uốn danh sách các mắt lưới được sử dụng là

khác với các mô-đun ban đầu. Vì vậy

bây giờ chúng ta cần giải nén chúng mà không cần bất kỳ

trùng lặp. Sau đó chúng tôi sử dụng phần trích xuất

lưới và đám mây điểm với

ID chuỗi được nối và chuỗi được sao chép

điểm. Quá nhiều mắt lưới để xuất

bằng tay. Chúng ta có thể sử dụng Python để xử lý hàng loạt

xuất khẩu

họ. Với vòng lặp for each, chúng ta có thể

lặp qua tất cả các mắt lưới và kích hoạt

Python để nhấn nút trên FBX

đầu ra.

Chúng tôi có một vấn đề. Chúng ta có quá nhiều

mắt lưới để điền vào tài sản dữ liệu cùng với

ID chuỗi. Vì vậy, chúng ta cần một kịch bản

công cụ để tự động điền tất cả. Đây là cách

các mắt lưới được đặt tên. Vì vậy, tôi có thể trích xuất

ID chuỗi từ tên lưới. Cái này

là công cụ viết kịch bản. Nó lặp lại

các lưới tĩnh đã chọn và gán

các mắt lưới và chuỗi trích xuất của chúng

ID cho nội dung dữ liệu. Để sử dụng

công cụ có thể tạo tập lệnh, hãy nhấp chuột phải vào

các mắt lưới đã chọn và tìm nó trong

tài sản có thể viết được

hành động. Bạn có thể chọn nội dung dữ liệu

bạn muốn điền vào. Bắt đầu và kết thúc hoặc

ký tự thừa trước và sau

số ID chuỗi. Có một

cũng tự động tạo tùy chọn va chạm. Cái này

thiết lập bây giờ đã quen thuộc. các

điều duy nhất đang diễn ra ở đây là

lưu tài sản dữ liệu PCG có thể được sử dụng để

nướng đám mây điểm Olympic thành một điều không thực

tài sản gốc thay vì phải tải

nó từ đĩa mọi lúc. Xóa bộ nhớ đệm

bởi controlclick để buộc

tạo ra và chúng tôi có mọi thứ

vào. Hãy nhìn vào tấm vải.

Tôi đã thử sử dụng chốt cho các sợi dây trong

Ban đầu không thực tế, nhưng hiệu suất

thất bại, nên cuối cùng tôi đã làm được một việc nhỏ

phần và xuất nó dưới dạng tĩnh

lưới. Trong hướng dẫn này, bạn có thể học

cách xuất splines giữa Houdini

và Không thực. BCG có thể đọc splines và nó

thực hiện tốt hơn so với cách tiêu chuẩn của

sinh ra các lưới spline với

bản thiết kế. Nhưng như tôi đã nói, đó là

vẫn chưa đủ hiệu quả trong

động cơ. Vì vậy tôi đã sử dụng lưới tĩnh

thay vào đó. Đầu tiên, hãy lấy điểm tại

đầu của mỗi lưới trên đấu trường. Sau đó

tạo một vòng trong và kết nối

điểm bằng một đường thẳng. chia dòng

và sử dụng một đoạn đường nối để treo nó trên

trục y. Sau đó, chúng tôi sử dụng những dòng đó như một

đối tượng va chạm cho giấy da

sim. Lập mô hình lưới đơn giản, sau đó chạy chúng

thông qua một tấm da để treo trên đầu

dòng. Một khi tôi hài lòng với kết quả, tôi

có thể sao chép chúng xung quanh.

Nhưng tôi chỉ cần xuất một trong số chúng.

của

tất nhiên, hãy nói về bán kính địa điểm

hình học

nút. Nó có thể mất nhiều nút

những con đường. Tương tự với việc hợp nhất đối tượng

nút, nhập trạng thái. Giữ shift và

nhấp chuột trái vào bất cứ nơi nào trên lưới để sinh sản

một cái mới

lưới. Bạn có thể chọn lưới ở bên trái

bấm một lần vào

nó. Shift trái bấm vào một lưới sẽ

trùng lặp

nó. Cuộn để thay đổi lưới

ID. Bạn có thể chọn xem bạn có muốn

uốn cong lưới hay không.

Ví dụ như bức tượng không nên

uốn cong. Đầu ra thứ tư trực quan hóa

cuối cùng

kết quả, nhưng bạn luôn có thể chỉnh sửa

bố cục. Trong tab cài đặt, bạn có thể

điều chỉnh số lượng phiên bản và

chiều dài của mỗi làn đường và những thứ khác.

Mỗi phiên bản có một hình ảnh dữ liệu vị trí

ID và vòng quay và tỷ lệ

được điều khiển trong khung nhìn bằng Python

tiểu bang. Chúng tôi có một vấn đề. Điều gì sẽ xảy ra nếu chúng ta

đặt hàng trăm điểm và mắt lưới nhưng

rồi mất HDA

thông số? Vâng, chúng tôi luôn có thể xuất khẩu

các thông số sử dụng một

JSON và sau đó đọc từ nó.

HDA này có thể xuất nhập khẩu

JSON. Vì vậy, tôi chỉ cần tải đấu trường

thiết lập tôi đã có trước đây

HDA. Mọi thứ đều có vẻ đúng. tôi là

sẽ tải một cái khác

JSON. Và đây là kết quả đầu ra đã sẵn sàng để

được xuất sang Unreal.

Trong Unreal hãy mở PCG

đồ thị. Nhấn E để tắt và bật

nút. Bỏ qua Olympic nướng để có được

những cập nhật mới nhất từ Houdini.

Ừm, có vẻ như

màu xanh. Chà, nếu chúng ta quay trở lại Houdini

và xuất lại đám mây điểm và

lực tạo ra

đồ thị

ở đó bằng cách thay đổi số nguyên vật liệu

giá trị trong Houdini, chúng ta có thể ghi đè

tài liệu trong Unreal.

Hãy đặt nó trở lại

không. Bạn có thể cắm nội dung dữ liệu của mình vào

các tham số của đồ thị PCG

cài đặt. Tôi cũng đã thêm tham số float

để lọc lưới bằng cách

thuộc tính và bạn có thể chỉnh sửa chúng trong

Ví dụ biểu đồ PCG ở cấp độ.

Hãy thực hiện một số thay đổi về bố cục.

Nhân đôi

biểu ngữ. Xóa một cột bằng điều khiển

nhấp chuột trái và xuất Olympic.

Rất tiếc, sai rồi

vật chất. Không phải một

vấn đề. Chúng ta có thể tìm thấy ID lưới của

biểu ngữ, trong trường hợp này là 50. Sau đó

viết một câu lệnh if cho biết nếu

ID lưới là 50, tôi muốn vật liệu

một sự khác biệt

số. Sau đó, biểu ngữ sẽ sử dụng một

tài liệu khác với tài sản dữ liệu.

Về chất liệu thì rất đơn giản.

Nó đang sử dụng kết cấu căn chỉnh thế giới trên một số

kết cấu được thực hiện với cảnh sát. Đây là

mạng lưới capernicus. Tôi muốn một họa sĩ

cảm thấy vậy nên tôi bắt đầu làm một vài chiếc cọ

đột quỵ, sau đó phân tán chúng

xung quanh, sau đó bóp méo chúng, giãn nở

lông vũ, và một chút tắc nghẽn xung quanh.

Tôi nhận thấy tôi phải chuyển hàng trên

đầu ra hình ảnh thô vì bình thường

bản đồ quá sáng trong Unreal. Chuyển đổi

hàng đã sửa gamma

vấn đề. Chúng ta hãy nhìn vào bàn chải

đột quỵ. Một tiếng ồn fractal đến RGB. Sau đó

quay lại mono để có được một điều tốt đẹp

tiếng ồn. Sau đó giãn ra,

bóp méo,

lông vũ hết lần này đến lần khác cho đến khi đó

cảm giác nhòe của nét cọ là

ở đó. Nếu bạn sống sót đến nay, tôi

sẽ đi sâu vào hình học xuyên tâm

HDA. Bắt đầu nào. Đầu tiên chúng ta tạo điểm

từ số lượng mục nhập nhiều phần.

Sau đó lấy giá trị của từng

nhập cảnh. Các mắt lưới được gán id lưới

được sử dụng trong thuộc tính mảnh trên một

sao chép

điểm. Hãy nhớ rằng chúng tôi đã

đã tạo một chuỗi ID trên các điểm tới

theo dõi sự khác biệt trên

trục x sẽ hữu ích khi chúng ta

uốn cong.

Bây giờ ở đây chúng tôi trích xuất nguồn gốc từ

từng trường hợp và uốn cong các điểm và

sao chép chúng

triệt để. Được rồi, quay lại với mắt lưới.

Căn giữa các mắt lưới và loại bỏ

trùng lặp. Sau đó chỉ uốn cong các mắt lưới

đã bật nút uốn cong của chúng.

Cuối cùng, chúng ta có thể có các mắt lưới uốn cong và

các điểm uốn cong với ID chuỗi là

có thể sao chép triệt để trong một mô-đun rõ ràng

đường. Các thuộc tính ISO là

thuộc tính chúng tôi đang sử dụng để lọc theo

thuộc tính trong PCG

Trong tab tập lệnh, bạn có thể tìm thấy

Tập lệnh Python để nhập và

xuất tham số với

JSON. Và đó là kịch bản gọi lại trên

nút để kích hoạt các chức năng này.

Trong tab tương tác, bạn có thể tìm thấy

các trạng thái Python cho phép khung nhìn

tương tác. Xưởng đã kết thúc rồi.

Bạn có thể rời đi. tôi sẽ nói về

Trạng thái Python một chút. Đây là những

chức năng kích hoạt các sự kiện trong

viewport. Bật

sự kiện nhập chuột xảy ra khi bạn

nhấp chuột trái

bấm vào. Có chưa được chọn và đang hoạt động.

Việc bỏ chọn xảy ra khi bạn nhấp một lần.

Trạng thái bật sẽ kích hoạt khi bạn kéo

chuột trong khung nhìn. Vì vậy, dưới

hoạt động, chúng tôi đặt một lưới mới trên một

lưới vô hình. Chúng tôi cập nhật bội số

các mục và vị trí của mục mới

lưới. Trong sự kiện quan trọng nhất thời, bạn có thể

kích hoạt các sự kiện bằng điều khiển và dịch chuyển.

Tôi đang thay đổi một giá trị số nguyên nếu tôi giữ

hoặc nhả điều khiển và dịch chuyển. Và khi tôi

sử dụng nút chuột trái có điều khiển

hoặc thay đổi, tôi có thể có thêm

chức năng. Chức năng giao nhau

cần hình học để giao nhau. Sau đó

chúng ta có được số nguyên của giao điểm

hình học. Và vì tất cả các mắt lưới của chúng tôi

được đóng gói, mỗi lưới về cơ bản là một

nguyên thủy. Vì mỗi lưới là một nguyên thủy và

có một số nguyên tố thì số đó có thể

tương ứng trực tiếp với số lượng

mục multiparm, làm cho nó thực sự dễ dàng

để theo dõi tất cả dữ liệu cần thiết cho mỗi

ví dụ. Nếu số nguyên tố tồn tại, chúng ta nhận được pt

ID, là phiên bản đa nhánh

số trong trường hợp này. Cập nhật

tay cầm. Nếu chúng ta nắm quyền kiểm soát,

xóa lưới.

Nếu chúng ta đang giữ phím shift, hãy thêm một lưới mới.

Eval parm tpple để đánh giá vectơ và

eval parm để đánh giá số float và

số nguyên. Parm và parm tpple có được

thuộc tính và sau đó đặt dấu chấm để đặt

giá trị mới. Trả về true để tiêu thụ

sự kiện nếu không sẽ không có gì

xảy ra. Sự kiện trên bánh xe chuột là

được kích hoạt khi bạn cuộn chuột. trong

trường hợp này, chúng tôi đang cập nhật ID lưới

của mục nhập đa nhánh đã chọn để cuộn

thông qua danh sách

mắt lưới. Và cuối cùng, chúng ta có một thực đơn

bật lên khi nhấp chuột phải và xử lý việc đó

đọc và viết vào

tình trạng. Và thế là xong. tôi muốn nói

cảm ơn vì tác dụng phụ và BDA cho

thực hiện hội thảo EPC này.
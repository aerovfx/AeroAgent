# Mọi con đường đều dẫn tới Hou-PCG Mohamad Salame SideFX EPC 2025 HIVE [Tiếng Việt]

---

[âm nhạc]

Bạn có muốn tạo ra sản phẩm này từ

đầu vào

Houdini và Unreal

Động cơ không?  Một trường chiến đấu có thể chơi hoàn toàn

, theo mô-đun, theo thủ tục và

can control

PCG.  Có thể tải xuống dự án tập tin

.

Tôi tên là Muhammad Salami,

nghệ sĩ kỹ thuật tại Side Effects Labs và đây là

hội thảo APC về Houdini và PCG.

Trước khi bắt đầu, hội thảo này

dựa trên một hướng dẫn có sẵn

trên trang web về tác dụng.  You can can

link finded

bên dưới.

Tóm tắt nhanh.  Sao chép vào các điểm, về cơ bản đó

toàn bộ quy trình làm việc trong Houdini và

PCG.

Chúng tôi có danh sách các mạng và một

đám mây đưa vào bản sao thành các điểm có

thuộc tính mảnh để phù hợp với từng mạng

điểm mong muốn.  Đây là

các mạng.  This lưới mang tính thủ tục.  Ví dụ

Ví dụ, xi lanh này sử dụng một ống và

boolean đường cong, phần lớn, PDB, v.v.

Và các vật liệu từ nhóm là để

chỉ định nhiều dữ liệu trong Unreal.  Và

đây là đám mây điểm.  Mỗi mạng có một

điểm ID thuộc tính có giá trị.  Các điểm được sao chép

chỉ mang tính chất minh họa.

Đám mây điểm và mạng là thứ thứ hai

cần thiết cho

PCG.  Chúng ta có thể xuất

đám mây điểm bằng CSV dữ liệu bảng hoặc

Olympic.  Tôi sẽ không đề cập đến

phương pháp CSV trong cuộc thảo luận này vì nó đã được thực hiện

phát triển cho Unreal 5.2 và 5.3.

Phương pháp được khuyến khích là Olympic

has in version 5.4 trở lên.  Nút Olympic

xuất đám mây có các thuộc tính.

Đảm bảo bạn có các điểm

thuộc tính định hướng để xoay và được chuẩn hóa

between 0 and 1. Tỷ lệ theo 100 để

phù hợp với tỷ lệ đơn vị Không thực tế.

Sử dụng bộ tạo lưới trong PCG với

bộ chọn mạng được đặt thành PCG mạng

được chọn theo thuộc tính được phép để chúng phù hợp

và thiết lập thành công danh sách

đám mây điểm dựa trên thuộc tính mảnh mảnh ID

.  Chúng tôi sử dụng tài sản dữ liệu để lưu trữ

list of lưới.  Tạo một strct with

một lưới tĩnh và một số nguyên.  Tạo

loại tài sản thiết kế chính của dữ liệu.

Và cuối cùng tạo một tài sản dữ liệu để lưu trữ

mạng đường dẫn và mạng ID.  Đây là

hình ảnh của dữ liệu tài sản.  Đây là

danh sách các mạng có số nguyên

match với mỗi biểu tượng nhóm

ID lưới của lưới đó.  Load elic reading

đám mây điểm.  Khởi tạo các mẫu thiết lập

for active with

cho phép Houdini biến đổi.  Khi nhập lại

đám mây điểm bằng Olympic, bạn phải xóa

bộ nhớ đệm.  Bạn có thể thực hiện điều đó bằng cách giữ

nút điều khiển và buộc phải tạo, nếu không sẽ

không có gì được

cập nhật.  Đây là đầy đủ nút thiết lập trong

PCG không có thật.  Match và đặt thuộc tính

Tương tự như sao chép vào các điểm

trong Houdini.  Bạn có thể sao chép lưới tĩnh

vào các điểm và vật liệu

lưới tĩnh.  Bạn cũng có thể tạo các diễn đàn.

Sản phẩm tài sản sẽ được đưa vào thuộc tính get

từ đối tượng đường dẫn đến nút phù hợp và đặt thuộc tính

tính toán phù hợp với mạng ID

giữa đám mây và danh sách

lưới.  Bạn có thể ghi đè nhiều

vật liệu trên mỗi mạng nếu mạng của bạn có

nhiều hơn một

data.  Tôi đã sử dụng thuộc tính đổi tên để

đổi tên vật liệu đầu tiên để

không phải tạo strct mới cho mỗi

khe dữ liệu.  Sau đây là một ví dụ về

ghi đè dữ liệu.  Con lợn được làm từ

những hộp và hình cầu này.  Tôi đã sử dụng

phần mềm ambient occlusion để tính toán

gradient, sau đó là max data only

for các vùng tối hơn và

sáng vật liệu hơn cho

các vùng sáng hơn.  Bạn có thể thay đổi proxy mạng của mình

with version end only by way

cập nhật dữ liệu

.  Sau đây là một ví dụ về tán lá cách điệu

sử dụng cùng một phương pháp Houdini Olympic hát Unreal

PCG.

Chúng ta đều biết những anh chàng này.  Mỗi

Mảnh Lego này là một ví dụ.  Ngoài ra

không có tiền tệ.  PCG có thể xử lý nhiều

field valid.  Sử dụng thuộc tính để ghi đè

vật liệu và nhiều thuộc tính cho

nhiều vật liệu trên mỗi mạng.

Vì chúng tôi đang sử dụng Houdini nên chúng tôi có thể làm được

những điều tương tự Houdini như một biến

thành công

Lego.  Sử dụng thuộc tính bộ lọc, chúng ta có thể

lọc theo

Mạng ID.  Đây là một ví dụ thú vị về lọc theo

thuộc tính khi chạy.

Đây là đám mây điểm từ bản demo ma trận

.  Một cách xây dựng đơn giản lưới

và đây là it in Unreal use

PCG.  Đây là một

ví dụ về đường dẫn.  Bạn có thể vẽ chúng bằng một đường cong

trong Houdini.

và dễ dàng trao đổi dữ liệu để chuyển đổi

giữa đường và

đường ống.  Hoặc nếu bạn muốn tạo sẵn các mô hình,

bạn có thể sử dụng phương pháp tương tự để tạo ra

các tác vụ thay thế

các lưới tĩnh.  Một ví dụ khác về việc sử dụng PCG

tài sản thực tế.  Đây là một ví dụ thú vị, nhưng nó

quá chậm.  Tôi không khuyến khích tạo ứng dụng hoạt động cho

PCG point to the current point, but can will be doing in

tương lai.  Đã xong, hãy quay lại ví dụ tệp của chúng tôi.

Hãy cùng thực hiện một số thay đổi cho tòa nhà này.   Bạn

có thể thoải mái theo dõi dù đã có

mở dự án tệp.  Trong Unreal, mở PCG và

bỏ qua

bước nướng Olympic.  Chúng ta cần

những thay đổi mới nhất.  Đảm bảo rằng nút Olympic của bạn đang

đọc tệp đúng.

Giữ quyền kiểm soát để tạo ra

những thay đổi ở hệ thống biên giới.  Đây là dữ liệu tài sản.  You can can

thấy nó sử dụng ID chứ không phải ID network cho

thuộc tính mảnh.  Tôi sẽ giải thích

sau.  Và trình tạo tĩnh tĩnh

sử dụng thuộc tính mạng cho đường dẫn.

Được rồi, hãy tăng độ khó và tạo

đường có thể che phủ.  Đầu tiên, chúng ta hãy xem xét

cách làm sai

.  Vấn đề với mô hình hóa

các nút bạn không biết nút nào

tương ứng với bất kỳ phần nào của nhà.

Và mỗi lần bạn muốn chỉnh sửa

phần đó bạn phải đi tìm

nút trong một nút cấu hình.

Thật sự là khó chịu.  Có phải cái này không?  Có phải

cái này phải không?  Không. Không, không,

không.  Đã tìm thấy nó.

Và hiện tại tôi có thể

chỉnh sửa chỉnh sửa.  chúng tôi tạo ra

module và use HDA with

Trạng thái Python để đặt các mô-đun thì sao?

sau đó xây dựng trường chiến đấu từ

đó.  Lưu ý rằng đây là HDA cần thiết

đưa ra một đám mây điểm và danh sách

các lưới để xuất

PCG.  Tôi đã tạo ra ba

Đặc biệt làn sóng đường đi tiếp theo đó chúng sẽ tạo ra phiên bản cho chúng.

Vấn đề với tuyến ngoại tuyến là

chúng thu hẹp hơn ở gần tâm

và rộng hơn ở xa tâm.  Vì vậy, chúng ta

cần một thuộc tính bổ sung để

theo dõi những thay đổi theo chiều dọc

trục x.  Bây giờ chúng ta có mạng ID và

ID có thể thay đổi.  Nhưng bản sao điểm có thể chỉ

use a attribute.  Vậy làm sao

chúng tôi có thể sao chép nhiều điểm

hơn một thuộc tính chỉ với một

thuộc tính mảnh?  You can

suy nghĩ gì không?  Một cách hay để theo dõi

các biến có thể giống với mạng ID là

kết nối mạng ID và

Biến ID có thể trong một chuỗi thuộc tính.

Giống như

1_1 gạch dưới 2 1ore 3 v.v. Sáu khi

bên cạnh, danh sách lưới sẽ được sử dụng

khác với các module ban đầu.

Bây giờ chúng ta cần trích xuất chúng mà không có bất kỳ

bản sao nào.  Sau đó, chúng tôi sử dụng các chuỗi đã trích xuất

và đám mây điểm có

ID string connect and

các điểm đã được sao chép.  Quá nhiều lưới để xuất

thủ công.  Chúng tôi có thể sử dụng Python để xuất hàng loạt

chúng.  Với mỗi vòng lặp, chúng ta có thể

lặp qua tất cả các mạng và kích hoạt

Nút nhấn của Python ở trên

đầu ra FBX.

Chúng ta đã có vấn đề rồi.  Chúng tôi có quá nhiều

lưới để điền dữ liệu tương tự

Chuỗi ID.  Vì vậy, chúng ta cần một

công cụ có thể tự động điền tất cả.  Đây là cách

đặt tên cho các mạng.  Vì vậy, tôi có thể trích xuất

Chuỗi ID từ mạng tên.  Đây

công cụ có thể cài đặt được.  Nó lặp lại

các lựa chọn và phân bổ tĩnh lưới

các chuỗi ID cùng được trích xuất của chúng

for data tài sản.  For use

công cụ có thể cài đặt, nhấp chuột phải vào

các nhóm đã chọn và tìm công cụ trong các nhóm

tài sản hành động có thể thiết lập trình tự.  You can choose data

bạn muốn điền.  Ký tự bắt đầu và kết thúc hoặc

ký tự thừa trước và sau

chuỗi ID số.

Ngoài ra còn có tùy chọn tự động tạo và chạm.

Thiết lập này hiện đã được chứng thực.

Điều bổ sung duy nhất ở đây là

PCG data được lưu có thể được sử dụng để

đưa đám mây điểm Olympic vào một

tài sản gốc của Unreal thay vì phải tải

nó từ đĩa mỗi lần.  Xóa bộ nhớ đệm

bằng cách nhấn controlclick để bắt buộc

create and we were many thứ

. Hãy xem xét.

Lúc đầu, tôi đã thử sử dụng spline cho sợi dây trong Unreal, nhưng hiệu suất

down down, tôi đã tạo một

phần nhỏ và xuất nó dưới dạng

lưới tĩnh.  Trong hướng dẫn này, bạn có thể học

cách xuất spline giữa Houdini

và Không thực.  BCG can be read spline đường cong và

hoạt động tốt hơn cách tạo

link spline normal

kế hoạch.  Nhưng như tôi đã nói,

cơ sở vẫn chưa đủ hiệu quả.  Vì vậy, tôi sử dụng lưới tĩnh

.  Đầu tiên, hãy lấy các điểm ở

đầu mỗi nhóm trên trường đấu.  Sau đó

tạo một vòng tròn trong và kết nối

các điểm lại với nhau bằng một đường thẳng.  chia nhỏ đường thẳng

và sử dụng một đường dốc để treo nó trên

trục y.  Sau đó, chúng tôi sử dụng những đường thẳng đó để làm

object va chạm cho giấy da

.  Tạo mô hình mạng đơn giản sau đó chúng

qua giấy da để treo lên trên

các đường kẻ.  Khi hài lòng với kết quả, tôi

có thể sao chép chúng.

Nhưng tôi chỉ cần xuất ra một số trong số đó.

Tất cả

nhiên, chúng ta hãy nói về vị trí nút học xuyên tâm

.  Nó có thể sử dụng nhiều

node path.  Tương tự như đối tượng hợp nhất nút

, enter status.  Giữ phím Shift và

nhấp chuột trái vào bất kỳ đâu trên mạng để tạo

new network.  Bạn có thể chọn một mạng bằng cách

click chuột trái một lần

mạng đó.  Nhấn Shift và nhấp chuột trái vào lưới để

sao chép

mạng đó.  Cuộn để thay đổi

Mạng ID.  You can choose

một mạng lưới hay không.

Ví dụ, bức tượng không được sử dụng

truong cong.  Màn hình thứ tư đầu tiên

kết quả cuối cùng, nhưng bạn luôn có thể chỉnh sửa

bố cục.  Trong quá trình cài đặt tab, bạn có thể

điều chỉnh số lượng và phiên bản

độ dài của mỗi làn sóng cũng như nhiều thứ khác.

Mỗi phiên bản đều có vị trí dữ liệu hình ảnh ID

và xoay chế độ và tỷ lệ được

kiểm tra trong khung nhìn

Python status.  Chúng ta đã có vấn đề rồi.  Sẽ thế nào nếu chúng ta

set hàng trăm điểm và mạng nhưng

sau đó lại bị mất

HDA tham số?  Vâng, chúng tôi luôn có thể xuất hiện

các tham số

JSON rồi đọc từ đó.

HDA này có thể xuất và nhập

JSON.  Vì vậy, tôi có thể dễ dàng tải

thiết lập trường đấu mà tôi đã có trước đó

HDA này.  Mọi thứ đều có vẻ ổn.  tôi

will upload one

JSON khác.  Và đây là kết quả đầu ra đã có sẵn

để xuất sang Unreal.

Trong Unreal, chúng ta hãy mở

biểu tượng PCG.  Nhấn E để tắt và bật

các nút.  Bỏ qua Olympic Bake để nhận

thông tin cập nhật mới nhất từ Houdini.

Ồ, trông nó có

màu xanh.  , if they ta quay lại Houdini Vâng

và xuất lại đám mây điểm và

buộc tạo

sơ đồ

ở đó bằng cách thay đổi dữ liệu nguyên giá trị

trong Houdini, chúng ta có thể ghi đè

vật liệu trong Unreal.

Please install it about

số không.  Bạn có thể cắm tài sản của mình vào

PCG biểu tượng cài đặt các tham số

.  Tôi cũng đã thêm float tham số

để lọc theo mạng

thuộc tính và bạn có thể chỉnh sửa chúng trong

PCG PCG version ở cấp độ đó.

Vui lòng thực hiện một số thay đổi về bố cục.

Sao chép

biểu tượng.  Xóa một cột bằng cách nhấp

chuột trái và xuất Olympic.

Ồ, sai rồi

tài liệu rồi.  Không

vấn đề gì.  Chúng tôi có thể tìm thấy mạng ID của

biểu ngữ, trong trường hợp này là 50. Sau đó, hãy

viết lệnh if nói rằng if

ID network là 50, tôi muốn vật liệu là

một

một số khác.  Sau đó, biểu tượng sẽ được sử dụng

data khác với data gốc.

Về phần vật liệu thì rất đơn giản.

Nó sử dụng thế giới điều chỉnh cấu hình trên một số

kết nối được tạo bằng cảnh báo.  Đây là

mạng lưới Capernicus.  Tôi muốn có

cảm giác như đang vẽ tranh, nên tôi bắt đầu vẽ một vài

mạnh mẽ, sau đó chúng sẽ xả rác

xung quanh, rồi căng chúng, làm giãn

nở lông vũ và một chút che khuất xung quanh.

Tôi nhận thấy mình phải chuyển đổi hàng trên

nguyên hình ảnh đầu ra vì

bản đồ bình thường quá sáng trong Unreal.  Việc chuyển đổi

hàng đã được giải quyết

gamma cố gắng.  Chúng ta hãy cùng xem

các cọ sắc nét.  Fractal to RGB.  Sau đó

chuyển sang âm đơn chế độ để có được

âm thanh hay.  Sau đó hãy giãn nở,

reactive, doing

nhiều lần cho đến khi

cảm giác giác giác nho nhỏ của sắc nét

known.  Nếu bạn đọc đến đây, tôi

sẽ đi sâu vào HDA hình học xuyên tâm

.  Chúng tôi bắt đầu ngừng hoạt động.  Đầu tiên chúng ta tạo điểm

từ nhiều phần nhập số lượng.

Sau đó lấy giá trị của từng

mục nhập.  Các nhóm được chỉ định nhóm ID

for use in attribute on

các điểm được sao chép.  Hãy nhớ rằng chúng tôi đã có

tạo một ID chuỗi trên các điểm để

theo dõi sai phương thức trên

trục x, điều này sẽ hữu ích khi chúng ta

truong cong.

Bây giờ chúng tôi trích xuất nguồn gốc từ

mỗi trường hợp và một số điểm rồi sao

copy chúng theo

hướng tâm trí.  Được rồi, quay lại với mạng.

Căn giữa các nhóm và loại bỏ các nhóm

lặp lặp nhóm.  Sau đó chỉ bổ sung các nhóm

có nút được bật.

Cuối cùng, chúng ta có thể có các nhóm và

các điểm với chuỗi ID để có

có thể sao chép theo hướng dẫn theo cách rõ ràng mô-đun

.  Thuộc tính ISO là

các thuộc tính mà chúng tôi sử dụng để lọc theo

thuộc tính trong PCG.

Trong tập lệnh tab, bạn có thể tìm thấy

Python command to enter and

xuất các tham số

JSON.  Và đó là lệnh gọi lại trên

nút để kích hoạt các chức năng này.

Trong tab tương tác, bạn có thể tìm thấy

allow Python status

tương tác với khung nhìn.  Buổi thảo luận đã kết thúc.

Bạn có thể rời đi.  Tôi sẽ nói

một chút về trạng thái của Python.  Đây là

sự kiện kích hoạt trong

view frame.

Sự kiện Enter trên chuột xảy ra khi bạn

click chuột trái

.  Có loại chưa được chọn và loại không được chọn.

Bỏ chọn xảy ra khi bạn nhấp một lần.   Chế độ

mode Onactive sẽ được kích hoạt khi bạn kéo dài

chuột trong khung nhìn.  Vì vậy, khi

đang hoạt động, chúng tôi thiết lập một mạng mới trên một

mạng lưới vô hình.  Chúng tôi đang cập nhật nhiều

mục nhập và vị trí của

new network.  Đối với sự kiện thoáng qua quan trọng, bạn có thể

kích hoạt sự kiện bằng cách điều khiển và chuyển đổi.

Tôi đang thay đổi giá trị nguyên nếu tôi giữ

hoặc thêm nút điều khiển và chuyển đổi.  Và khi tôi

sử dụng nút chuột trái với điều khiển phím

hoặc shift, tôi có thể có thêm nhiều

chức năng.  Hàm giao tiếp nhau

cần có hình học để giao tiếp với nhau.  Sau đó,

chúng ta có một số nguyên tố

hình học giao nhau.  Và bởi vì tất cả các mạng của chúng ta đều

được đóng gói nên cơ sở cho mỗi mạng là một

mẫu nguyên.  Vì mỗi nhóm là một prim và

có một số nguyên tố nên có thể có một số

tương ứng trực tiếp với số

mục multiparm, giúp dễ dàng

theo dõi tất cả các dữ liệu cần thiết cho mỗi

field valid.  Nếu nguyên tắc tồn tại, chúng tôi sẽ nhận được

ID pt, đây là đa nhánh phiên bản

in this field hợp lý.  Update

phần xử lý.  Nếu chúng ta đang kiểm soát, hãy

xóa khối.

Nếu họ giữ phím Shift, hãy thêm một mạng mới.

Đánh giá parm tpple để đánh giá các giá trị và

giá parm để đánh giá các số thực và

số nguyên.  Parm và parm tpple get

thuộc tính rồi đặt dấu chấm để đặt

new value for they.  Return về true để sử dụng

sự kiện, tuy nhiên sẽ không có gì

xảy ra.  Sự kiện bánh xe chuột được

kích hoạt khi bạn cuộn chuột.  Trọng

trường hợp này, chúng tôi đang cập nhật mạng ID

của nhiều cánh tay được chọn để cuộn

qua danh sách

các mạng.  Và cuối cùng, chúng ta có một menu

bật lên khi nhấp chuột phải và xử lý công việc

đọc và ghi vào

status.  Và thế là xong.  Tôi muốn

cảm ơn BDA và các phụ trợ tác vụ

this EPC EPC tổ chức.
# Chương 10. Triển khai hoạt động tự chú ý cho Học tập tăng cường sâu của MNIST, Phiên bản video được dịch

---

Phần 10.3, Thực hiện việc tự chú ý cho Ennist

Trước khi đi sâu vào những khó khăn của việc học tăng cường, chúng ta hãy thử xây dựng một

mạng tự chú ý để phân loại các chữ số MNIST. Bộ dữ liệu MNIST nổi tiếng là 60.000 bản vẽ tay

hình ảnh của các chữ số, trong đó mỗi hình ảnh có kích thước 28 x 28 pixel ở thang độ xám. Các hình ảnh được dán nhãn

theo chữ số được mô tả. Mục tiêu là đào tạo một mô hình học máy

để phân loại chính xác các chữ số. Bộ dữ liệu này rất dễ học, ngay cả với một cách đơn giản

mạng lưới thần kinh một lớp, một mô hình tuyến tính. CNN nhiều lớp có thể đạt được độ chính xác 99%

phạm vi. Mặc dù dễ dàng nhưng đây là một tập dữ liệu tuyệt vời để sử dụng làm công cụ kiểm tra độ chính xác, chỉ để đảm bảo

thuật toán của bạn có thể học được bất cứ điều gì. Đầu tiên chúng ta sẽ kiểm tra khả năng tự chú ý của mình

mô hình trên MNIST, nhưng cuối cùng chúng tôi dự định sử dụng nó làm mạng Q sâu trong việc chơi trò chơi,

do đó, sự khác biệt duy nhất giữa DQN và bộ phân loại hình ảnh là tính chiều

đầu vào và đầu ra sẽ khác nhau. Mọi thứ ở giữa có thể vẫn như cũ.

Mục 10.3.1, MNIST chuyển đổi

Trước khi xây dựng mô hình, chúng ta cần chuẩn bị dữ liệu và tạo một số hàm

để xử lý trước dữ liệu để nó ở dạng phù hợp với mô hình của chúng tôi. Đối với một, nguyên

Ảnh MNIST là mảng pixel thang độ xám, có giá trị từ 0 đến 255 nên chúng ta cần chuẩn hóa

các giá trị đó nằm trong khoảng từ 0 đến 1 hoặc độ dốc trong quá trình huấn luyện sẽ quá thay đổi và

luyện tập sẽ không ổn định. Bởi vì MNIST rất dễ dàng nên chúng ta cũng có thể làm căng mô hình của mình một chút

hơn nữa bằng cách thêm nhiễu và làm xáo trộn hình ảnh một cách ngẫu nhiên, ví dụ: các bản dịch ngẫu nhiên

và các phép quay. Điều này cũng sẽ cho phép chúng ta đánh giá tính bất biến tịnh tiến và quay.

Các chức năng tiền xử lý này được xác định trong danh sách sau.

Liệt kê 10.1, các hàm tiền xử lý

Chức năng Thêm điểm gạch dưới sẽ chụp một hình ảnh và thêm nhiễu ngẫu nhiên vào đó. Chức năng này

được sử dụng bởi chức năng Chuẩn bị hình ảnh gạch dưới, chức năng này chuẩn hóa các pixel hình ảnh giữa

0 và 1, và thực hiện các phép biến đổi nhỏ ngẫu nhiên, chẳng hạn như thêm nhiễu, dịch, dịch chuyển,

hình ảnh và xoay hình ảnh.

Hình 10.14 cho thấy một ví dụ về chữ số MNIST ban đầu và bị nhiễu. Bạn có thể thấy điều đó

hình ảnh được dịch lên trên và sang bên phải và có các chấm ngẫu nhiên được rải vào. Điều này làm cho

nhiệm vụ học tập khó khăn hơn vì mô hình của chúng ta phải học tịnh tiến, tiếng ồn,

và các tính năng bất biến quay để phân loại thành công. Dấu gạch dưới Chuẩn bị

chức năng hình ảnh có các tham số cho phép bạn điều chỉnh mức độ nhiễu của hình ảnh,

để bạn có thể kiểm soát được độ khó của vấn đề.

Hình 10.14, bên trái, chữ số MNIST ban đầu cho số 5. Bên phải, phiên bản được chuyển đổi

được dịch lên trên cùng bên phải và kèm theo tiếng ồn ngẫu nhiên.

Phần 10.3.2, mô-đun quan hệ. Bây giờ chúng ta có thể đi sâu vào mạng lưới thần kinh quan hệ

chính nó. Cho đến nay, tất cả các dự án trong cuốn sách này đều được thiết kế đủ hấp dẫn.

để minh họa một khái niệm quan trọng nhưng đủ đơn giản để có thể chạy trên máy tính xách tay hiện đại

mà không cần GPU. Nhu cầu tính toán của sự tự chú ý

tuy nhiên, mô-đun lớn hơn đáng kể so với bất kỳ mô hình nào khác mà chúng tôi đã xây dựng

cho đến nay trong cuốn sách. Bạn vẫn có thể thử chạy mô hình này trên máy tính xách tay của mình, nhưng nó sẽ

nhanh hơn đáng kể nếu bạn có GPU hỗ trợ CUDA. Nếu bạn không có GPU, bạn có thể dễ dàng

khởi chạy Notebook Jupyter dựa trên đám mây bằng Amazon SageMaker, Google Cloud hoặc Google

Colab, tính đến thời điểm viết bài này là miễn phí. Lưu ý, mã chúng tôi hiển thị trong cuốn sách này sẽ không

bao gồm những sửa đổi cần thiết nhưng rất nhỏ cần thiết để chạy trên GPU. Vui lòng tham khảo điều này

trang GitHub của cuốn sách tại liên kết này để xem cách kích hoạt mã chạy trên GPU hoặc tham khảo

tài liệu PyTorch tại liên kết này. Trong danh sách 10.2, chúng ta định nghĩa một lớp

mô-đun quan hệ. Nó là một mạng lưới thần kinh đơn lẻ nhưng phức tạp bao gồm một mạng lưới thần kinh ban đầu

tập hợp các lớp tích chập theo sau là các phép nhân ma trận khóa, truy vấn và giá trị.

Liệt kê 10.2, mô-đun quan hệ. Thiết lập cơ bản của mô hình của chúng tôi là khối ban đầu gồm bốn

các lớp chập mà chúng tôi sử dụng để xử lý trước dữ liệu pixel thô thành các tính năng cấp cao hơn.

Mô hình quan hệ lý tưởng của chúng ta sẽ hoàn toàn bất biến đối với các phép quay và biến dạng trơn tru,

và bằng cách bao gồm các lớp tích chập vốn chỉ bất biến dịch này, toàn bộ

mô hình bây giờ kém bền hơn trước các chuyển động quay và biến dạng. Tuy nhiên, các lớp CNN

hiệu quả tính toán hơn các mô-đun quan hệ, do đó thực hiện một số bước tiền xử lý với

CNN thường hoạt động tốt trong thực tế. Sau các lớp CNN, chúng ta có ba phép chiếu tuyến tính

các lớp chiếu một tập hợp các nút vào một không gian đặc trưng có chiều cao hơn. Chúng tôi cũng có một số

các lớp định mức lớp, được thảo luận chi tiết hơn trong thời gian ngắn và một vài lớp tuyến tính ở cuối.

Nhìn chung, nó không phải là một kiến ​​trúc phức tạp mà các chi tiết đều nằm trong đường dẫn phía trước của mô hình.

Liệt kê 10.3, chuyển tiếp, tiếp tục từ liệt kê 10.2.

Chúng ta hãy xem đường chuyển tiếp này tương ứng như thế nào với sơ đồ phía sau trong hình 10.13.

Có một số điểm mới được sử dụng trong mã này chưa được đề cập ở đâu khác trong cuốn sách này,

và có thể bạn chưa biết. Một là việc sử dụng lớp định mức lớp trong PyTorch,

không có gì đáng ngạc nhiên khi nó là viết tắt của chuẩn hóa lớp. Định mức lớp là một dạng chuẩn hóa mạng thần kinh.

Một cách phổ biến khác được gọi là chuẩn hóa lô, hay chỉ là định mức lô. Vấn đề với việc không chuẩn hóa

mạng nơ-ron là độ lớn của đầu vào cho mỗi lớp trong mạng nơ-ron có thể khác nhau

đáng kể và phạm vi giá trị mà đầu vào có thể nhận có thể thay đổi theo từng đợt.

Điều này làm tăng sự thay đổi của gradient trong quá trình huấn luyện và dẫn đến sự mất ổn định,

có thể làm chậm đáng kể quá trình đào tạo. Chuẩn hóa tìm cách giữ tất cả đầu vào ở mỗi bước chính của

tính toán trong phạm vi hẹp tương đối cố định, nghĩa là với giá trị trung bình và phương sai không đổi.

Điều này giữ cho độ dốc ổn định hơn và có thể giúp việc đào tạo nhanh hơn nhiều.

Như chúng ta đã thảo luận, sự tự chú ý và lớp quan hệ hoặc đồ thị rộng hơn,

các mô hình có khả năng đạt được những thành tựu mà các mô hình chuyển tiếp thông thường gặp khó khăn do

độ lệch quy nạp của dữ liệu có tính chất quan hệ. Thật không may, vì mô hình liên quan đến softmax trong

ở giữa, điều này có thể làm cho việc đào tạo không ổn định và khó khăn vì softmax hạn chế đầu ra ở bên trong

một phạm vi rất hẹp có thể trở nên bão hòa nếu đầu vào quá lớn hoặc nhỏ. Như vậy, nó là

điều quan trọng là bao gồm các lớp chuẩn hóa để giảm bớt những vấn đề này và trong các thử nghiệm của chúng tôi,

định mức lớp cải thiện đáng kể hiệu suất đào tạo, như mong đợi.

Mục 10.3.3, phép rút gọn tensor và ký hiệu Einstein.

Điểm mới lạ khác trong mã này là việc sử dụng hàm torch.einsam.

Einsam là viết tắt của phép tính tổng Einstein, còn gọi là ký hiệu Einstein. Nó được giới thiệu bởi

Albert Einstein như một ký hiệu mới để biểu diễn một số loại phép toán bằng tensor.

Mặc dù chúng ta có thể viết cùng một mã mà không cần Einsam, nhưng với nó thì đơn giản hơn nhiều,

và chúng tôi khuyến khích sử dụng nó khi nó mang lại khả năng đọc mã được cải thiện.

Để hiểu nó, bạn phải nhớ lại rằng tensor, theo nghĩa máy học, chúng ở đâu

chỉ là mảng đa chiều, có thể có 0 hoặc nhiều chiều được truy cập bởi các

chỉ số. Hãy nhớ lại rằng một số vô hướng, một số, là một tensor bằng 0. Một vectơ là một tensor,

một ma trận là một tensor hai, v.v. Con số tương ứng với số lượng chỉ số mà mỗi tensor có.

Một vectơ có một chỉ mục vì mỗi phần tử trong một vectơ có thể được đánh địa chỉ và truy cập bởi một

giá trị chỉ số nguyên không âm. Một phần tử ma trận được truy cập bởi hai chỉ mục, hàng và cột của nó

các vị trí. Điều này khái quát hóa các kích thước tùy ý. Nếu bạn đã tiến xa đến mức này,

bạn đã quen với các phép toán như bên trong, dấu chấm, tích giữa hai vectơ và ma trận

phép nhân, nhân một ma trận với một vectơ hoặc một ma trận khác.

Việc khái quát hóa các phép toán này thành các tensor có thứ tự tùy ý, ví dụ như phép nhân

của hai ba tensor, được gọi là sự co tensor. Ký hiệu Einstein giúp dễ dàng biểu diễn và

tính toán bất kỳ sự co rút tensor tùy ý nào và với sự tự chú ý, chúng ta đang cố gắng thu gọn

hai ba tenxơ, và sau đó là hai bốn tenxơ. Vì vậy việc sử dụng Einstein trở nên cần thiết, nếu không chúng ta sẽ

phải định hình lại ba tensor thành một ma trận, thực hiện phép nhân ma trận bình thường và sau đó định hình lại nó

trở lại tensor ba, khó đọc hơn nhiều so với việc chỉ sử dụng Einstein. Đây là cái chung

Công thức rút gọn tensor của hai ma trận. Xem công thức này. Đầu ra bên trái,

CYK, là ma trận kết quả từ việc nhân ma trận A dấu hai chấm 1 với J và B dấu hai chấm J với K,

trong đó IJK là các kích thước, sao cho kích thước J của mỗi ma trận có cùng kích thước,

mà chúng ta biết là cần thiết để thực hiện phép nhân ma trận. Điều này cho chúng ta biết là phần tử C 0 0,

ví dụ: bằng tổng của A 0, JBJ 0 cho tất cả J. Phần tử đầu tiên trong

ma trận đầu ra C được tính bằng cách lấy từng phần tử ở hàng đầu tiên của A, nhân nó với mỗi phần tử

phần tử trong cột đầu tiên của B, sau đó tổng hợp tất cả những phần tử này lại với nhau. Chúng ta có thể tìm ra từng phần tử

của C bằng quá trình tính tổng một chỉ số chung cụ thể giữa hai tensor. Tổng kết này

trên một chỉ mục được chia sẻ là quá trình rút gọn tensor, vì chúng ta bắt đầu bằng, chẳng hạn,

hai tensor đầu vào với mỗi tensor có hai chỉ số, tổng cộng có bốn chỉ số và đầu ra có hai

chỉ số vì hai trong số bốn bị thu hẹp lại. Nếu chúng ta thực hiện phép co tensor trên hai ba

tensor, kết quả sẽ là một tensor bốn. Sự co rút của tensor, ví dụ. Hãy giải quyết vấn đề bê tông

ví dụ về sự co tensor. Chúng ta sẽ rút gọn hai ma trận bằng ký hiệu Einstein.

Xem biểu hiện này. Ma trận A là ma trận hai nhân ba và ma trận B là ma trận ba nhân hai. chúng tôi sẽ

dán nhãn kích thước của các ma trận này bằng các ký tự tùy ý. Ví dụ: chúng ta sẽ gắn nhãn ma trận A

dấu hai chấm Y theo J với các thứ nguyên, chỉ số i và J, và ma trận B dấu hai chấm J theo K với các chỉ số J và K.

Chúng ta có thể gắn nhãn các chỉ mục bằng cách sử dụng bất kỳ ký tự nào, nhưng chúng ta muốn thu gọn các chỉ mục được chia sẻ.

kích thước của A J bằng B J bằng ba, vì vậy chúng tôi gắn nhãn cho chúng bằng các ký tự giống nhau.

Xem biểu hiện này. Ma trận C này đại diện cho đầu ra. Mục tiêu của chúng tôi là tìm ra các giá trị

của các giá trị X, được gắn nhãn theo vị trí được lập chỉ mục của chúng. Sử dụng phép co tensor trước đó

công thức, chúng ta có thể tìm ra X zero zero bằng cách tìm hàng 0 của ma trận A và cột 0 của ma trận B

dấu hai chấm A 0, J bằng một trừ hai bốn, và B J 0 bằng trừ ba năm 0 lũy thừa

của T. Bây giờ chúng ta lặp lại chỉ số J, nhân từng phần tử của A 0, J với B J 0, rồi sau đó

tổng hợp chúng lại với nhau để có được một số duy nhất, sẽ là X zero zero. Trong trường hợp này, X không

số 0 bằng tổng của A 0, J bởi B J 0 bằng một nhân trừ ba, cộng trừ hai

nhân năm, cộng bốn nhân không, bằng trừ ba trừ mười bằng trừ mười ba. Đó là

phép tính chỉ cho một phần tử trong ma trận đầu ra, phần tử C zero zero. Chúng tôi làm tương tự

xử lý tất cả các phần tử trong C và chúng tôi nhận được tất cả các giá trị. Tất nhiên, chúng tôi không bao giờ làm điều này bằng tay,

nhưng đây là điều đang diễn ra bên trong khi chúng ta thực hiện phép co tensor, và quá trình này

khái quát hóa thành các tensor có bậc cao hơn chỉ là ma trận. Hầu hết thời gian bạn sẽ thấy Einstein

ký hiệu được viết mà không có ký hiệu tính tổng, trong đó giả sử chúng ta tính tổng theo chỉ mục được chia sẻ.

Nghĩa là, thay vì viết rõ ràng C i k bằng tổng của A i j bởi B j k, chúng ta thường

chỉ cần viết C i k bằng A i j bởi J k và bỏ qua phép tính tổng. Ký hiệu Einstein cũng có thể dễ dàng

biểu diễn phép nhân ma trận theo lô, trong đó chúng ta có hai tập hợp ma trận,

và chúng ta muốn nhân hai ma trận đầu tiên với nhau, hai ma trận thứ hai với nhau, v.v.,

cho đến khi chúng ta có được một tập hợp ma trận nhân mới. Đây là phương trình Einstein cho

phép nhân ma trận hàng loạt. Biểu thức này, trong đó kích thước B là kích thước lô,

và chúng ta chỉ thu gọn về chiều J chung. Chúng ta sẽ sử dụng ký hiệu Einstein để làm ma trận batch

phép nhân, nhưng chúng ta cũng có thể sử dụng nó để thu gọn nhiều chỉ số cùng một lúc, khi sử dụng mức cao hơn

sắp xếp tensor hơn ma trận. Trong danh sách 10.3, chúng tôi đã sử dụng A bằng điểm ngọn đuốc Einstein của B phí Bg Aero BFG QK,

để tính phép nhân ma trận hàng loạt của ma trận Q và K. Einstein chấp nhận một chuỗi

chứa các hướng dẫn về chỉ số nào sẽ co lại và sau đó các tensor sẽ được

ký hợp đồng. Chuỗi BFE BGE Aero BFG liên kết với tensor Q và K có nghĩa là Q là tensor có

ba chiều được dán nhãn BFE và K là một tenxơ có ba chiều được dán nhãn BGE và chúng ta muốn

thu gọn các tensor này để có được một tensor đầu ra có ba chiều được dán nhãn BFG.

Chúng tôi chỉ có thể thu gọn các kích thước có cùng kích thước và được dán nhãn giống nhau,

vì vậy trong trường hợp này, chúng tôi thu gọn theo chiều E, là chiều đặc trưng của nút,

để lại cho chúng ta hai bản sao của kích thước nút, đó là lý do tại sao đầu ra có kích thước B x N x M.

Khi sử dụng Einstein, chúng ta có thể gắn nhãn kích thước của mỗi tensor bằng bất kỳ ký tự chữ cái nào,

nhưng chúng ta phải đảm bảo rằng kích thước mà chúng ta muốn thu gọn được dán nhãn giống nhau

ký tự cho cả hai tensor. Sau khi nhân ma trận theo lô, chúng ta có ma trận không chuẩn hóa

ma trận kề, chúng tôi đã thực hiện A bằng A chia cho NP chấm SQRT của kích thước gạch dưới nút tự dấu chấm,

để điều chỉnh lại ma trận nhằm giảm các giá trị quá lớn và cải thiện hiệu suất huấn luyện.

Đây là lý do tại sao trước đây chúng tôi gọi đây là sự chú ý của sản phẩm theo tỷ lệ chấm.

Để có được ma trận Q, K và V, như chúng ta đã thảo luận trước đó, chúng ta lấy đầu ra của

lớp tích chập cuối cùng, là một tenxơ có kích thước theo từng kênh theo chiều cao và chiều rộng,

và chúng ta thu gọn kích thước chiều cao và chiều rộng thành một chiều cao theo chiều rộng bằng N,

đối với số lượng nút, vì mỗi vị trí pixel sẽ trở thành một nút hoặc đối tượng tiềm năng trong

ma trận nút. Do đó, chúng ta nhận được ma trận nút ban đầu gồm N dấu hai chấm B x C x N mà chúng ta định hình lại thành

N dấu hai chấm B by N by C. Bằng cách thu gọn các chiều không gian thành một chiều duy nhất,

sự sắp xếp không gian của các nút bị xáo trộn và mạng sẽ gặp khó khăn để phát hiện ra điều đó

một số nút nhất định, ban đầu là các pixel lân cận, có liên quan về mặt không gian. Đó là lý do tại sao chúng tôi thêm hai

các thứ nguyên kênh bổ sung mã hóa vị trí x, y của mỗi nút trước khi nó bị thu gọn.

Chúng tôi chuẩn hóa các vị trí nằm trong khoảng 0, 1, vì việc chuẩn hóa hầu như luôn giúp ích

với hiệu suất. Thêm các tọa độ không gian tuyệt đối này vào cuối vectơ đặc trưng của mỗi nút

giúp duy trì thông tin không gian, nhưng nó không lý tưởng vì các tọa độ này nằm trong

tham chiếu đến hệ tọa độ bên ngoài, có nghĩa là chúng ta đang giảm bớt một số tính bất biến

về mặt lý thuyết đối với các phép biến đổi không gian mà một mô-đun quan hệ nên có. Mạnh mẽ hơn

Cách tiếp cận là mã hóa các vị trí tương đối đối với các nút khác, điều này sẽ duy trì không gian

bất biến. Tuy nhiên, cách tiếp cận này phức tạp hơn và chúng ta vẫn có thể đạt được hiệu suất tốt

và khả năng diễn giải với mã hóa tuyệt đối. Sau đó chúng tôi chuyển ma trận nút ban đầu này qua ba

các lớp tuyến tính khác nhau để chiếu nó thành ba ma trận khác nhau với khả năng khác nhau

thứ nguyên kênh, mà chúng ta sẽ gọi thứ nguyên tính năng nút từ thời điểm này, như được hiển thị trong hình 10.15.

Hình 10.15, bước phóng chiếu trong quá trình tự chú ý. Các nút đầu vào được chiếu vào một

thường là không gian đặc trưng có chiều cao hơn bằng phép nhân ma trận đơn giản.

Sau khi nhân truy vấn và ma trận khóa, chúng ta sẽ nhận được ma trận trọng số chú ý không chuẩn hóa,

dấu hai chấm b x n x n, trong đó b bằng lô và n bằng số nút. Sau đó chúng tôi bình thường hóa nó

bằng cách áp dụng softmax trên các hàng, thứ nguyên 1, đếm từ 0, sao cho mỗi hàng có tổng bằng một.

Điều này buộc mỗi nút chỉ chú ý đến một số lượng nhỏ các nút khác hoặc để truyền bá nó.

sự chú ý rất mỏng trên nhiều nút. Sau đó chúng ta nhân ma trận chú ý với ma trận giá trị

để có được ma trận nút được cập nhật, sao cho mỗi nút bây giờ là sự kết hợp có trọng số của tất cả các nút khác

nút. Vì vậy, nếu nút 0 đặc biệt chú ý đến nút 5 và 9 nhưng bỏ qua các nút khác, khi chúng ta

nhân ma trận chú ý với ma trận giá trị, nút 0 sẽ được cập nhật thành trọng số

sự kết hợp của các nút 5 và 9, và chính nó, bởi vì các nút thường chú ý đến chính chúng.

Hoạt động chung này được gọi là truyền tin nhắn, bởi vì mỗi nút gửi một tin nhắn,

nghĩa là vectơ đặc trưng của chính nó tới các nút mà nó được kết nối.

Khi chúng tôi có ma trận nút được cập nhật, chúng tôi có thể giảm nó xuống một vectơ duy nhất bằng cách lấy trung bình

hoặc gộp tối đa trên kích thước nút để có được một vectơ D chiều duy nhất sẽ tóm tắt

đồ thị như một tổng thể. Chúng ta có thể chuyển nó qua một vài lớp tuyến tính thông thường trước khi nhận được

đầu ra cuối cùng, chỉ là một vectơ của các giá trị Q, do đó chúng tôi đang xây dựng một mạng Q sâu có quan hệ,

LIÊN QUAN. Phần 10.3.4, đào tạo mô-đun quan hệ. Bạn có thể đã nhận thấy điều cuối cùng

lệnh gọi hàm trong mã thực sự là log gạch dưới softmax, đây không phải là thứ chúng tôi sẽ sử dụng

cho việc học Q. Nhưng trước khi bắt đầu học Q, chúng ta sẽ kiểm tra mô-đun quan hệ về phân loại

M-nist và so sánh nó với mạng nơ ron tích chập phi quan hệ thông thường.

Cho rằng mô-đun quan hệ của chúng tôi có khả năng mô hình hóa các mối quan hệ đường dài theo cách

mà một mạng nơ-ron tích chập đơn giản không thể làm được, chúng tôi mong đợi mô-đun quan hệ của mình sẽ thực hiện

tốt hơn trước những biến đổi mạnh mẽ. Hãy xem nó hoạt động như thế nào. Liệt kê 10.4, vòng huấn luyện M-nist.

Đây là một vòng lặp đào tạo khá đơn giản để đào tạo bộ phân loại M-nist của chúng tôi. Chúng tôi đã bỏ qua

mã cần thiết để lưu trữ các tổn thất để hiển thị sau này, nhưng có thể tìm thấy mã không rút gọn

trong kho GitHub của cuốn sách này. Chúng tôi đã yêu cầu chức năng chuẩn bị hình ảnh gạch dưới ngẫu nhiên

xoay hình ảnh lên đến 30 độ theo một trong hai hướng, đây là một con số đáng kể.

Hình 10.16 cho thấy mô-đun quan hệ hoạt động như thế nào sau 1000 kỷ nguyên.

Đó là không đủ dài để đạt được độ chính xác tối đa. Các cốt truyện có vẻ tốt, nhưng đây chỉ là hiệu suất trên

dữ liệu huấn luyện. Hình 10.16, độ mất mát và độ chính xác qua các giai đoạn huấn luyện của quan hệ

module về phân loại chữ số M-nist. Để thực sự biết nó hoạt động tốt như thế nào, chúng ta cần chạy mô hình

trên dữ liệu thử nghiệm, đây là một tập dữ liệu riêng biệt mà mô hình chưa từng thấy trước đây. Chúng tôi sẽ chạy

nó trên 500 mẫu từ dữ liệu thử nghiệm để tính toán độ chính xác của nó. Liệt kê 10.5, độ chính xác của phép kiểm tra M-nist.

Chúng tôi nhận được độ chính xác gần 95% tại thời điểm thử nghiệm với mô-đun quan hệ chỉ sau 1000 kỷ nguyên

thử nghiệm. Một lần nữa, 1000 kỷ nguyên với kích thước lô 300 là không đủ để đạt được độ chính xác tối đa.

Độ chính xác tối đa khi bật bất kỳ mạng thần kinh nào, không bị xáo trộn. M-nist chắc tầm 98-99

dấu phần trăm, nhưng ở đây chúng tôi sẽ không đạt được độ chính xác tối đa. Chúng tôi chỉ đảm bảo nó hoạt động,

và nó hoạt động tốt hơn mạng nơ ron tích chập có số lượng tham số tương tự.

Chúng tôi sử dụng CNN đơn giản sau đây làm đường cơ sở, có 88.252 tham số có thể huấn luyện,

so với các module quan hệ 85.228. CNN thực sự có nhiều hơn khoảng 3.000 thông số so với

mô-đun quan hệ của chúng tôi, vì vậy nó có một chút lợi thế. Liệt kê 10.6, mạng nơ ron tích chập

đường cơ sở cho M-nist. Khởi tạo CNN này và hoán đổi nó cho mô-đun quan hệ trong

vòng đào tạo trước đó để xem nó so sánh như thế nào. Chúng tôi nhận được độ chính xác kiểm tra chỉ 87,80% với điều này

CNN, chứng minh rằng mô-đun quan hệ của chúng tôi hoạt động tốt hơn kiến trúc CNN, kiểm soát

số lượng tham số. Hơn nữa, nếu bạn tăng mức độ chuyển đổi, chẳng hạn như thêm nhiều hơn

tiếng ồn, xoay nhiều hơn, mô-đun quan hệ sẽ duy trì độ chính xác cao hơn CNN.

Như chúng tôi đã lưu ý trước đó, việc triển khai mô-đun quan hệ cụ thể của chúng tôi không thực tế

bất biến đối với phép quay và biến dạng, vì một phần chúng ta đã thêm tọa độ tuyệt đối

các vị trí. Nó không hoàn toàn mang tính quan hệ, nhưng nó có khả năng tính toán các mối quan hệ đường dài giữa

các đặc điểm trong ảnh, trái ngược với CNN chỉ có thể tính toán các đặc điểm cục bộ.

Chúng tôi muốn giới thiệu các mô-đun quan hệ, không chỉ vì chúng có thể có độ chính xác cao hơn

trên một số tập dữ liệu, nhưng vì chúng dễ hiểu hơn các mô hình mạng thần kinh truyền thống.

Chúng ta có thể kiểm tra các mối quan hệ đã học trong ma trận trọng số chú ý để xem phần nào của

đầu vào mà mô-đun quan hệ đang sử dụng để phân loại hình ảnh hoặc dự đoán giá trị Q như trong hình

17/10. Hình 10.17, cột bên trái, đầu vào ban đầu, ảnh M-nist, sau khi chuyển đổi. Đúng

cột, các trọng số tự chú ý tương ứng cho biết nơi mà mô hình chú ý nhiều nhất.

Chúng tôi trực quan hóa bản đồ chú ý này bằng cách định hình lại bản đồ chú ý thành một hình ảnh vuông.

Xem mã này. Ma trận trọng số chú ý là một lô theo ma trận N x N trong đó N là số lượng

các nút, có 16 bình phương bằng 256 trong ví dụ của chúng tôi. Vì sau các lớp chập,

phạm vi không gian giảm từ 28 xuống 28 ban đầu. Lưu ý trong hai ví dụ trên của hình 10.17,

bản đồ chú ý đó làm nổi bật đường viền của chữ số, nhưng với cường độ cao hơn ở một số phần nhất định.

Nếu bạn xem qua một số bản đồ chú ý này, bạn sẽ nhận thấy rằng mô hình có xu hướng chú ý đến

chú ý nhất đến điểm uốn và điểm chéo của chữ số. Đối với chữ số 8, có thể

phân loại thành công hình ảnh này là số 8, chỉ bằng cách chú ý đến trung tâm của số 8

và phần dưới cùng. Bạn cũng có thể nhận thấy rằng không có ví dụ nào chú ý đến

thêm các điểm nhiễu ở đầu vào. Chỉ chú ý đến phần chữ số thực của hình ảnh,

chứng minh rằng mô hình đang học cách tách tín hiệu khỏi nhiễu ở mức độ lớn.
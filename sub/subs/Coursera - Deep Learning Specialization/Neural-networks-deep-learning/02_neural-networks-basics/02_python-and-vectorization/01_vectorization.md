# 01 vector hóa

---

Chào mừng trở lại. Vector hóa về cơ bản là

nghệ thuật loại bỏ các vòng lặp for rõ ràng trong mã của bạn.

Trong kỷ nguyên deep learning, đặc biệt là deep learning trong thực tế,

bạn thường thấy mình phải đào tạo trên các tập dữ liệu tương đối lớn,

bởi vì đó là lúc các thuật toán deep learning có xu hướng phát huy tác dụng.

Vì vậy, điều quan trọng là bạn phải viết mã thật nhanh vì nếu không,

nếu nó đang huấn luyện một tập dữ liệu lớn,

mã của bạn có thể mất nhiều thời gian để chạy thì bạn chỉ cần tìm

bản thân bạn đang chờ đợi một thời gian rất dài để có được kết quả.

Vì vậy trong kỷ nguyên học sâu,

Tôi nghĩ khả năng thực hiện vector hóa đã trở thành một kỹ năng quan trọng.

Hãy bắt đầu với một ví dụ.

Vậy Vector hóa là gì?

Trong hồi quy logistic, bạn cần tính Z bằng W hoán vị X cộng B,

trong đó W là vectơ cột này và X cũng là vectơ này.

Có thể chúng là những vectơ rất lớn nếu bạn có nhiều tính năng.

Vì vậy, W và X đều là các vectơ chiều R và không có R, NX.

Vì vậy, để tính W chuyển vị X,

nếu bạn có cách triển khai không được vector hóa,

bạn sẽ làm điều gì đó như Z bằng 0.

Và sau đó đối với I trong phạm vi của X.

Vì vậy, với I bằng 1, 2 NX,

Z cộng bằng W I nhân XI.

Và sau đó có thể bạn sẽ tính Z cộng bằng B ở cuối.

Vì vậy, đó là cách triển khai không được vector hóa.

Sau đó, bạn thấy rằng điều đó sẽ rất chậm.

Ngược lại, việc triển khai theo vector sẽ chỉ tính toán trực tiếp W chuyển vị X.

Trong Python hoặc một Numpy,

lệnh bạn sử dụng cho điều đó là Z bằng np.W,

X, do đó tính toán W hoán vị X.

Và bạn cũng có thể thêm B trực tiếp vào đó.

Và bạn thấy rằng điều này nhanh hơn nhiều.

Chúng ta hãy thực sự minh họa điều này bằng một bản demo nhỏ.

Vì vậy, đây là sổ ghi chép Jupiter của tôi, trong đó tôi sẽ viết một số mã Python.

Vì vậy, trước tiên, hãy để tôi nhập thư viện gọn gàng để nhập.

Gửi P. Và như vậy, ví dụ,

Tôi có thể tạo A dưới dạng một mảng như sau.

Giả sử in A.

Bây giờ, sau khi viết xong đoạn mã này,

nếu tôi nhấn shift enter,

sau đó nó thực thi mã.

Vì vậy, nó tạo ra mảng A và in ra.

Bây giờ, hãy thực hiện bản demo Vectorization.

Tôi sẽ nhập các thư viện thời gian,

vì chúng tôi sử dụng nó,

để tính thời gian các hoạt động khác nhau diễn ra trong bao lâu.

Họ có thể tạo một mảng A không?

Những vòng suy nghĩ ngẫu nhiên đó.

Điều này tạo ra một mảng triệu chiều với các giá trị ngẫu nhiên.

b = np.random.rand.

Một mảng triệu chiều khác.

Và bây giờ, tic=time.time, vậy cái này đo thời gian hiện tại,

c = np.dot (a, b).

toc = thời gian.thời gian.

Và bản in này,

nó là phiên bản vector hóa.

Đây là một phiên bản vector hóa.

Và vì vậy, hãy in ra.

Hãy xem lần cuối nhé

vậy là có toc - tic x 1000,

để chúng ta có thể diễn đạt điều này trong mili giây.

Vì vậy, ms là mili giây.

Tôi sẽ nhấn Shift Enter.

Vì vậy, đoạn mã đó mất khoảng 3 mili giây hoặc lần này là 1,5,

có thể khoảng 1,5 hoặc 3,5 mili giây mỗi lần.

Nó thay đổi một chút khi tôi chạy nó,

nhưng có vẻ như trung bình nó mất khoảng 1,5 mili giây,

có thể là hai mili giây khi tôi chạy cái này.

Được rồi.

Hãy tiếp tục thêm vào khối mã này.

Đó không phải là triển khai phiên bản không vector hóa.

Hãy xem, c = 0,

thì tic = time.time.

Bây giờ hãy triển khai một vòng lặp for.

Đối với tôi trong tầm 1 triệu,

Tôi sẽ chọn ra số 0 đúng không.

C += (a,i) x (b,

i), rồi toc = time.time.

Cuối cùng, in nhiều hơn vòng lặp đầy đủ rõ ràng.

Thời gian cần là 1000 x toc - tic + "ms"

để biết rằng chúng tôi đang thực hiện việc này trong một phần nghìn giây.

Hãy làm một điều nữa.

Hãy in ra giá trị của C mà chúng ta

tính toán nó để đảm bảo rằng nó có cùng giá trị trong cả hai trường hợp.

Tôi sẽ nhấn shift enter để chạy cái này và kiểm tra cái kia.

Trong cả hai trường hợp, phiên bản vectorize

và phiên bản không vector hóa tính toán các giá trị giống nhau,

như bạn đã biết, 2,50 đến 6,99, v.v.

Phiên bản vectorize mất 1,5 mili giây.

Phiên bản vòng lặp for và không vector hóa rõ ràng mất khoảng 400, gần 500 mili giây.

Phiên bản không vector hóa mất khoảng 300

dài hơn nhiều lần so với phiên bản vectorize.

Với ví dụ này, bạn sẽ thấy rằng nếu bạn nhớ vector hóa mã của mình,

mã của bạn thực sự chạy nhanh hơn 300 lần.

Hãy chạy lại lần nữa.

Chỉ cần chạy lại nó.

Vâng. Vectorize phiên bản 1,5 mili giây và vòng lặp for.

Vậy là 481 mili giây, một lần nữa,

chậm hơn khoảng 300 lần khi thực hiện vòng lặp for rõ ràng.

Nếu động cơ x chậm lại,

đó là sự khác biệt giữa mã của bạn có thể mất một phút để

chạy so với việc phải mất năm giờ để chạy.

Và khi bạn đang triển khai các thuật toán học sâu,

bạn thực sự có thể nhận được kết quả nhanh hơn.

Sẽ nhanh hơn nhiều nếu bạn vector hóa mã của mình.

Một số bạn có thể đã nghe điều đó rất nhiều

Việc triển khai deep learning có thể mở rộng được thực hiện trên GPU hoặc bộ xử lý đồ họa.

Nhưng tất cả các bản demo tôi vừa thực hiện trong máy tính xách tay Jupiter, thực tế là trên CPU.

Và hóa ra cả GPU và CPU đều có hướng dẫn song song hóa.

Đôi khi chúng được gọi là hướng dẫn SIMD.

Đây là viết tắt của một lệnh nhiều dữ liệu.

Nhưng điều này về cơ bản có nghĩa là,

nếu bạn sử dụng các chức năng tích hợp như thế này

np.function hoặc các hàm khác không yêu cầu bạn triển khai vòng lặp for một cách rõ ràng.

Nó cho phép Phyton Pi lấy

lợi thế tốt hơn nhiều của tính song song để thực hiện tính toán của bạn nhanh hơn nhiều.

Và điều này đúng cả khi tính toán trên CPU và tính toán trên GPU.

Chỉ là GPU hoạt động rất tốt

những tính toán SIMD này nhưng thực tế CPU cũng không quá tệ ở khoản đó.

Có lẽ không tốt bằng GPU.

Bạn đang thấy việc vector hóa có thể tăng tốc đáng kể mã của bạn như thế nào.

Quy tắc ngón tay cái cần nhớ là bất cứ khi nào có thể,

tránh sử dụng vòng lặp for rõ ràng.

Chúng ta hãy chuyển sang video tiếp theo để xem thêm một số ví dụ về

vector hóa và cũng bắt đầu vector hóa hồi quy logistic.
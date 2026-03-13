# 71 - CNN về CIFAR10 Đánh giá mô hình

---

Chào mừng trở lại, mọi người.

Ở bài giảng trước.

Chúng tôi tiếp tục đọc dữ liệu, xử lý trước dữ liệu và sau đó huấn luyện mô hình của mình.

Hãy tiếp tục và đánh giá mô hình của chúng tôi.

Tôi sẽ quay lại cuốn sổ tay Yooper mà chúng ta đã dừng lại lần trước.

Được rồi.

Chúng tôi chỉ đào tạo mô hình của chúng tôi.

Hãy tiếp tục và đọc các số liệu đó.

Có phải những tổn thất đó dựa trên lịch sử mô hình bằng cách nói khung dữ liệu suy nghĩ PD và gọi nó là lịch sử mô hình,

lịch sử.

Và điều chúng ta sắp làm ở đây là chúng ta có thể tự kiểm tra các số liệu bằng cách chạy nó như vậy,

nhưng có lẽ sẽ thú vị hơn nếu vẽ chúng ra, giả sử là các số liệu.

Hãy gọi nó là cột thật nhanh.

Tiết kiệm cho mình một chút đánh máy.

Chúng tôi sẽ nói số liệu trên.

Và chúng ta hãy tiếp tục và lấy.

Bạn có thể lấy tất cả chúng và sau đó chỉ cần xóa một số trong số này.

Vì vậy, chúng tôi sẽ dán nó vào và chúng tôi sẽ so sánh độ chính xác với xác nhận, độ chính xác.

Và hãy tiếp tục và vạch ra điều đó.

Được rồi, có vẻ như việc đào tạo thực sự tiếp tục tăng lên và có vẻ như mức độ xác nhận, độ chính xác

giống như nó cũng đang tiếp tục tăng lên một chút và đi ngang.

Nhưng hãy nhớ rằng, chúng tôi đã chỉ ra rằng chúng tôi muốn dừng lại vì thua lỗ.

Vì vậy, điều đó có lẽ sẽ cung cấp nhiều thông tin hơn về lý do tại sao chúng tôi ngừng tập luyện sớm.

Vậy ta sẽ nói thua so với.

Mất xác nhận.

Hãy tiếp tục và vẽ biểu đồ đó ra và đây là biểu đồ thực sự mang tính biểu thị để chúng ta có thể thấy mức lỗ giao dịch đang diễn ra

ngừng hoạt động, nhưng chúng tôi không nhận được bất kỳ cải thiện nào về việc mất xác thực và trên thực tế, có vẻ như vậy

đã bắt đầu đi lên.

Vì vậy, có lẽ nên bắt đầu kết thúc khóa đào tạo với số tiền khoảng 70 đô la.

Như mọi khi, chúng ta có thể nhận được số liệu đánh giá cuối cùng chỉ bằng cách nhìn vào hàng cuối cùng này trong dữ liệu của chúng ta

frame hoặc bằng cách nói đánh giá mô hình và chúng ta có thể đánh giá bằng bài kiểm tra X.

Tại sao không thể kiểm tra cả hai đều bằng 0, do đó bạn không thấy kết quả in lớn và nếu bạn chạy nó,

về cơ bản nó cho bạn thấy kết quả tương tự.

Vậy không điểm chín tám năm quay lại đây, không phải là không điểm chín mươi lăm và sau đó bạn có số không

điểm sáu chín và không có điểm sáu chín.

Vì vậy, kết quả tương tự như trong lịch sử thực tế.

Hãy tạo một báo cáo phân loại và ma trận nhầm lẫn để đánh giá thêm điều này khi Nhập số liệu của chúng tôi

Báo cáo phân loại.

Sự nhầm lẫn, ma trận.

Hãy thực sự nhận được những dự đoán của chúng ta, đó là các lớp dự đoán mô hình.

Sau khi thử nghiệm, sau đó chúng tôi sẽ in ra một báo cáo phân loại so sánh các giá trị thực đã biết của chúng tôi từ thử nghiệm Y,

trong trường hợp này, chúng tôi không chuyển vào phân loại.

Chúng tôi chỉ cần những con số thực tế so với dự đoán của chúng tôi.

Hãy in nó ra và chúng ta có thể thấy độ chính xác của mình.

Nhớ lại điểm F1 cũng như độ chính xác tổng thể của chúng tôi.

Vì vậy, điều chúng tôi muốn nghĩ đến là độ chính xác tốt đến mức nào.

Độ chính xác sáu mươi chín phần trăm?

Chà, điều đầu tiên là so sánh nó chỉ là đoán ngẫu nhiên.

Và bởi vì chúng ta có mười lớp ở đây nên một lần đoán ngẫu nhiên có 10% cơ hội đúng.

Vì vậy, về tổng thể, chúng tôi đạt được độ chính xác là 69 phần trăm, điều đó có nghĩa là các mô hình của chúng tôi thực sự hoạt động khá tốt.

cũng có điều kiện.

Và ở đây, điều thực sự thú vị về báo cáo phân loại này là tôi có thể xem xét những lớp nào

nó thực sự không hoạt động tốt như vậy.

Và bạn có thể thấy nó có xu hướng hoạt động kém ở lớp thứ ba.

Và chúng ta có thể nhìn vào đây và thấy không một, hai, ba.

Vậy có vẻ như nó đang gặp rắc rối với mèo.

Và nếu chúng ta nhìn xem nếu chúng ta có ba con ở đây thì tức là bốn hoặc năm con, chúng ta có chó.

Hãy nhìn lại đây.

Bạn cũng sẽ nhận thấy điều đó không có tác dụng tốt với chó.

Và trên thực tế, chúng hoạt động rất giống nhau.

Và đó là bởi vì khi bạn làm mờ một hình ảnh đến mức nó chỉ có kích thước ba mươi hai x ba mươi hai con mèo và con chó

có thể trông thực sự giống với một máy tính.

Vì vậy, chúng tôi thực sự mong đợi sẽ hoạt động khá kém ở đây.

Bạn có thể thấy nó hoạt động khá tốt ở loại số một, đó là ô tô, có lẽ là

đặc biệt nhất trong số này.

Tuy nhiên, bạn nhận thấy cũng có xe tải.

Vì vậy, thực tế là nó có thể hoạt động rất tốt đối với ô tô, vì đã có danh mục xe tải,

khá giống với ô tô, nó khá ấn tượng.

Vậy chúng ta sẽ quay lại đây.

Một điều khác bạn có thể làm như trước đây là tự mình đưa ra những dự đoán thực tế.

Bạn có thể nói rằng có bao nhiêu người đúng, thực ra là việc phân loại sai mọi thứ như mọi khi.

Nhập khẩu Seabourne dưới dạng S.A.S. và sau đó nói rằng bản đồ nhiệt Asness trên ma trận nhầm lẫn này có thể khiến nó trở thành một

lớn hơn một chút, sẽ nói là con số TLT.

Kích thước cố định tương đương với thứ gì đó như hãy tiếp tục và nói 10 x 6, hãy chạy nó.

Và điều thú vị ở đây là dựa trên màu sắc, bạn có thể nhanh chóng biết được nó đang phân loại sai

mọi thứ.

Vì vậy có vẻ như có sự nhầm lẫn giữa ba và năm.

Và chúng ta có thể nhận được một chú thích để xem số lượng phân loại sai thực tế ở đây.

Như vậy các bạn có thể thấy dựa vào màu sắc thì có sự nhầm lẫn giữa ba và năm, bốn quay lại đây.

Đó là không một, hai, ba con mèo so với chó.

Vì vậy, nó gặp rắc rối với những loại động vật có lông nhỏ này.

Có ý nghĩa.

Chúng khá giống nhau trên hình ảnh 32 x 32.

Nhưng hãy tiếp tục và xem nó hoạt động như thế nào chỉ trên một hình ảnh.

Vì vậy, nếu chúng ta muốn dự đoán một hình ảnh, chúng ta sẽ lấy một hình ảnh ngay trước đó.

Vì vậy, ai đó quay lại, này, đây là dữ liệu hình ảnh của tôi.

Và hãy nhớ lại, dữ liệu này đã được thu nhỏ lại.

Vì vậy, nếu họ đưa cho bạn một hình ảnh thô, bạn sẽ phải chia tỷ lệ nó bằng cách nói chia cho hai năm mươi lăm.

Nhưng tôi có thể làm gì ở đây, Kielty nói.

Hãy tiếp tục và hiển thị hình ảnh của tôi.

Đây là hình ảnh của tôi.

Tôi thực sự không chắc đây là gì, vì vậy có lẽ chúng ta phải nói.

Tại sao phải kiểm tra ở mức 0 và đó là ba, vì vậy đó phải là giới hạn.

Chúng ta sẽ xem nó hoạt động tốt như thế nào.

Hãy đi vào và nói mô hình.

Các lớp và vật là thứ duy nhất chúng ta phải đảm bảo rằng chúng ta định hình lại cái này một cách chính xác.

Vì vậy, đó là một hình ảnh, 32 x 32 với ba kênh màu, hãy tiếp tục và chạy nó.

Và có vẻ như tôi đã dự đoán khá tốt.

Vì vậy, điều đó thật đáng ngạc nhiên vì bản thân tôi cũng không thể dự đoán được điều này.

Được rồi, và tôi nghĩ hình ảnh chúng tôi hiển thị trong tập dữ liệu thực tế hoặc sổ ghi chép giải pháp là hình ảnh số 16,

điều đó rõ ràng hơn nhiều rằng ở đây có một con chó và sau đó chúng ta có thể đối đầu với nó.

Tại sao bài kiểm tra là 16, vậy nên đó là một con chó cho lớp, nó cũng thực hiện đúng.

Vì vậy, hiệu suất khá tốt nếu xét đến hoàn cảnh ở đây.

Chà, tiếp theo chúng ta sẽ đề cập đến cách xử lý, trích dẫn dữ liệu hình ảnh thực, không trích dẫn.

Vì vậy, thông thường, hình ảnh của bạn sẽ không tải chúng chỉ bằng một lệnh gọi CARUS đơn giản.

Thay vào đó, có thể bạn sẽ tải chúng từ một thư mục, một thư mục trên máy tính của bạn.

có một số loại jpeg hoặc tập tin trong bài giảng tiếp theo.

Chúng tôi sẽ chỉ cho bạn cách tải xuống tập dữ liệu mà chúng tôi làm việc cùng.

Và sau đó các bài giảng tiếp theo sẽ chỉ cho bạn cách sử dụng keris được tích hợp trong trình tạo và tạo hình ảnh

từ các chức năng thư mục đến thực sự hoạt động với các tệp JPEG thực.

Cảm ơn.

Và chúng ta sẽ gặp lại bạn ở bài giảng tiếp theo.
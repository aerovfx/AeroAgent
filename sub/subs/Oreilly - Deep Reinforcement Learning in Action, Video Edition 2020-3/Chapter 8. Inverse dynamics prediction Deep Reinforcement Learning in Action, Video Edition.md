# Chương 8. Dự đoán động lực học nghịch đảo Học tăng cường sâu trong hành động, Phiên bản video đã dịch

---

Phần 8.2, Dự đoán động lực nghịch đảo.

Chúng tôi đã mô tả cách chúng tôi có thể sử dụng lỗi dự đoán làm tín hiệu tò mò.

Mô-đun lỗi dự đoán ở phần trước được triển khai dưới dạng một hàm,

hàm f, lấy đầu vào, viết hoa S, T và A, T, và tạo ra dấu mũ S,

T cộng 1, nhận một trạng thái và hành động được thực hiện và trả về trạng thái tiếp theo được dự đoán,

hình 8.6.

Đó là dự đoán tương lai, tương lai, trạng thái của môi trường,

nên chúng tôi gọi nó là mô hình dự đoán tương lai.

Hình 8.6, Sơ đồ chức năng của module dự đoán thuận f,

lấy đầu vào vốn S, T và A, T và sản xuất vốn S hat, T cộng 1,

ánh xạ trạng thái hiện tại và hành động tới trạng thái tiếp theo được dự đoán.

Hãy nhớ rằng, chúng tôi chỉ muốn dự đoán những khía cạnh thực sự quan trọng của trạng thái,

không phải là những phần tầm thường hoặc ồn ào.

Cách chúng tôi xây dựng ràng buộc không quan trọng đối với mô hình dự đoán

là thêm một mô hình khác gọi là mô hình nghịch đảo, hàm G,

lấy đầu vào viết hoa S, T và viết hoa S, T cộng 1, tạo ra dấu mũ A, T.

Đây là hàm G nhận một trạng thái và trạng thái tiếp theo,

và sau đó trả về dự đoán về hành động nào đã được thực hiện dẫn đến quá trình chuyển đổi

từ S, T đến S, T cộng 1, như trên hình 8.7.

Hình 8.7, mô hình nghịch đảo có hai trạng thái liên tiếp

và cố gắng dự đoán hành động nào đã được thực hiện.

Bản thân mô hình nghịch đảo này không thực sự hữu ích.

Có một mô hình bổ sung được kết hợp chặt chẽ với mô hình nghịch đảo

gọi là mô hình mã hóa, ký hiệu là phi.

Các hàm mã hóa, hàm phi, ánh xạ chữ S,

T thành mũ S mũ T, nhận một trạng thái và trả về chữ hoa S được mã hóa dấu ngã T,

sao cho kích thước của vốn S dấu ngã T thấp hơn đáng kể so với vốn nhà nước thô S T,

hình 8.8.

Trạng thái thô có thể là khung video RGB với chiều cao, chiều rộng và kích thước kênh,

và phi sẽ mã hóa trạng thái đó thành một vectơ có chiều thấp.

Ví dụ: một khung có thể có kích thước 100 pixel x 100 pixel theo 3 kênh màu với tổng số 30.000 phần tử.

Nhiều pixel trong số đó sẽ dư thừa và không hữu ích,

vì vậy, chúng tôi muốn bộ mã hóa của mình mã hóa trạng thái này thành một vectơ 200 phần tử với các tính năng không dư thừa cấp cao.

Hình 8.8, mô hình bộ mã hóa có biểu diễn trạng thái nhiều chiều như mảng RGB

và mã hóa nó dưới dạng vectơ có chiều thấp.

Lưu ý, một biến có ký hiệu dấu ngã ở trên, chẳng hạn như chữ S viết hoa chữ T,

biểu thị một số loại phiên bản được chuyển đổi của biến cơ bản, có thể có chiều khác nhau.

Một biến có ký hiệu mũ phía trên, chẳng hạn như chữ S viết hoa, dấu ngã T, biểu thị một giá trị gần đúng hoặc dự đoán,

của trạng thái cơ bản và có cùng chiều.

Mô hình bộ mã hóa được huấn luyện thông qua mô hình nghịch đảo, bởi vì chúng tôi thực sự sử dụng các trạng thái được mã hóa làm đầu vào cho các mô hình thuận và nghịch đảo F và G,

chứ không phải là trạng thái thô.

Nghĩa là mô hình thuận trở thành hàm F, lấy tích phi của vốn S, T và A, T,

và ánh xạ nó tới phi mũ của chữ S, đến cộng 1, trong đó phi mũ của chữ S, T cộng 1,

đề cập đến dự đoán về trạng thái được mã hóa và mô hình nghịch đảo trở thành hàm G,

lấy tích phi của vốn S, T và phi mũ của vốn S, T cộng 1, và ánh xạ nó thành mũ A,

T, hình 8.9.

Hàm ký hiệu P, lấy các phần tử từ tập hợp A và tập hợp B làm đầu vào và ánh xạ chúng tới tập hợp C,

có nghĩa là chúng ta định nghĩa một hàm P nào đó nhận vào một cặp A, B và biến đổi nó thành một đối tượng mới C.

Hình 8.9. Mô-đun dự đoán chuyển tiếp thực sự sử dụng các trạng thái được mã hóa chứ không phải trạng thái thô.

Các trạng thái được mã hóa được ký hiệu là phi viết hoa S, T hoặc viết hoa S dấu ngã T.

Mô hình bộ mã hóa không được đào tạo trực tiếp, nó không phải là bộ mã hóa tự động, nó chỉ được đào tạo thông qua mô hình nghịch đảo.

Mô hình nghịch đảo đang cố gắng dự đoán hành động được thực hiện để chuyển từ trạng thái này sang trạng thái tiếp theo,

sử dụng các trạng thái được mã hóa làm đầu vào và để giảm thiểu lỗi dự đoán của chính nó, lỗi của nó sẽ truyền ngược trở lại mô hình bộ mã hóa cũng như chính nó.

Sau đó, mô hình bộ mã hóa sẽ học cách mã hóa các trạng thái theo cách hữu ích cho nhiệm vụ của mô hình nghịch đảo.

Điều quan trọng là, mặc dù mô hình chuyển tiếp cũng sử dụng các trạng thái được mã hóa làm đầu vào, nhưng chúng tôi không truyền ngược từ mô hình chuyển tiếp sang mô hình bộ mã hóa.

Nếu chúng tôi làm như vậy, mô hình chuyển tiếp sẽ buộc mô hình bộ mã hóa ánh xạ tất cả các trạng thái thành một đầu ra cố định duy nhất, vì đó sẽ là cách dễ dự đoán nhất.

Hình 8.10. Hiển thị cấu trúc biểu đồ tổng thể.

Truyền tiến của các thành phần và cả truyền ngược, lan truyền ngược, truyền để cập nhật các tham số mô hình.

Cần nhắc lại rằng mô hình nghịch đảo truyền ngược trở lại mô hình bộ mã hóa và mô hình bộ mã hóa chỉ được huấn luyện cùng với mô hình nghịch đảo.

Chúng ta phải sử dụng phương pháp tách của PyTorch để tách mô hình chuyển tiếp khỏi bộ mã hóa để nó không truyền ngược vào bộ mã hóa.

Mục đích của bộ mã hóa không phải là cung cấp cho chúng ta đầu vào chiều thấp để cải thiện hiệu suất mà là học cách mã hóa trạng thái bằng cách sử dụng biểu diễn chỉ chứa thông tin liên quan để dự đoán hành động.

Điều này có nghĩa là các khía cạnh của trạng thái dao động ngẫu nhiên và không có tác động đến hành động của tác nhân sẽ bị loại bỏ khỏi biểu diễn được mã hóa này.

Về lý thuyết, điều này sẽ tránh được vấn đề TV ồn ào.

Hình 8.10. Mô-đun tò mò. Đầu tiên, bộ mã hóa sẽ mã hóa các trạng thái viết hoa S, T và viết hoa S, T+1 thành các vectơ có chiều thấp lần lượt là 5 chữ S, T và 5 chữ S viết hoa, T+1.

Các trạng thái được mã hóa này được chuyển sang mô hình thuận và mô hình nghịch đảo. Lưu ý rằng mô hình nghịch đảo truyền ngược lại mô hình được mã hóa, do đó huấn luyện nó thông qua lỗi của chính nó.

Mô hình chuyển tiếp được huấn luyện bằng cách truyền ngược từ hàm lỗi của chính nó, nhưng nó không truyền ngược qua bộ mã hóa như mô hình nghịch đảo.

Điều này đảm bảo rằng bộ mã hóa học cách tạo ra các biểu diễn trạng thái chỉ hữu ích cho việc dự đoán hành động nào đã được thực hiện.

Vòng tròn màu đen biểu thị thao tác sao chép sao chép đầu ra từ bộ mã hóa và chuyển các bản sao sang mô hình thuận và mô hình nghịch đảo.

Lưu ý rằng đối với cả mô hình thuận và mô hình nghịch đảo, chúng ta cần truy cập vào dữ liệu để chuyển đổi hoàn toàn, nghĩa là chúng ta cần viết hoa S, T, A, T, viết hoa S, T cộng 1.

Đây không phải là vấn đề khi chúng ta sử dụng bộ nhớ phát lại trải nghiệm, như chúng ta đã làm trong chương 3 về học Q sâu, vì bộ nhớ sẽ lưu trữ một loạt các loại bộ dữ liệu này.
# 02 - Tiền xử lý và đưa dữ liệu vào mô hình của bạn

---

- [Người hướng dẫn] Hãy chuyển sang bước tiếp theo

trong hành trình của chúng tôi với TensorFlow.

Trong phần này chúng ta sẽ đi sâu

vào quá trình quan trọng của tiền xử lý dữ liệu.

Tiền xử lý là yếu tố quan trọng trong bất kỳ quy trình học máy nào.

Nó đảm bảo rằng dữ liệu của bạn ở trạng thái tốt nhất có thể

trước khi nó được đưa vào mô hình của bạn, trực tiếp

ảnh hưởng đến chất lượng dự đoán của mô hình của bạn.

Như người ta nói, rác vào, rác ra.

Vì vậy sơ chế là bước vàng

trong bất kỳ quy trình học máy nào.

Hãy bắt đầu

bằng cách khám phá tập dữ liệu mà chúng tôi sẽ làm việc.

Sau đó, chúng ta sẽ chuyển sang chia tỷ lệ, hình dung,

và chuẩn bị nó cho mô hình của chúng tôi.

Trước hết chúng ta hãy mở Codespaces

và sau đó tìm thư mục src,

và nhấp vào 03_02_begin.py.

Vì vậy, đây là nơi chúng ta sẽ bắt đầu viết mã

và chúng ta sẽ kết thúc ở 03_02_end.py.

Vì vậy, hãy tiếp tục và bắt đầu nhập thư viện vào đây.

Vì vậy chúng ta sẽ phải có pandas, numpy, matplotlib,

seaborn, sklearn và tensorflow.

Vì vậy, nhiệm vụ của chúng tôi ở đây là xem những gì còn thiếu

và bắt đầu thêm từng cái một.

Vì vậy hãy tiếp tục và bắt đầu với Pandas,

nhập gấu trúc dưới dạng pd,

và sau đó nhập numpy dưới dạng np.

Sau đó chúng ta sẽ đi tiếp

và nhập các thư viện trực quan như matplotlib,

và sau đó chúng ta sẽ cần pyplot cụ thể,

thì chúng ta sẽ gọi nó là plt.

Tiếp theo chúng ta sẽ nhập thư viện trực quan hóa khác,

đó là Seaborn, được xây dựng trên Matplotlib,

và sau đó chúng ta sẽ gọi nó là sns.

Sau đó chúng ta có sklearn.datasets,

nhậpfetch_california_housing.

Sau đó chúng ta có sklearn.model_selection,

nhập test_train_split.

Sau đó, chúng ta có sklearn.preprocessing import StandardScaler.

Chúng tôi cũng muốn nhập thêm một điều nữa ở đây,

đó là bánh mì và bơ của khóa học của chúng tôi,

đó là tenorflow dưới dạng tf.

Vậy là tổng hợp được thư viện của chúng tôi

mà chúng ta sẽ làm việc ở đây.

Một lần nữa, Pandas được sử dụng để thao tác và phân tích dữ liệu.

NumPy được sử dụng để tính toán số.

Nó giống như một chiếc máy tính ưa thích dành cho các chương trình của chúng ta.

Sau đó chúng ta có matplotlib.pyplot và seaborn.

Đây là để trực quan hóa dữ liệu.

Seaborn được xây dựng trên Matplotlib

và cung cấp giao diện cấp cao

vẽ đồ họa thống kê hấp dẫn và nhiều thông tin.

Sau đó, chúng tôi có tập dữ liệu Fetch_california_housing,

tải dữ liệu nhà ở California cho chúng tôi.

Sau đó, chúng ta có test_train_split, chia tách tập dữ liệu

vào các tập huấn luyện, xác nhận và kiểm tra,

tiếp theo là StandardScaler, chia tỷ lệ các tính năng

bằng cách loại bỏ giá trị trung bình và chia tỷ lệ thành phương sai đơn vị.

Tiếp theo, hãy tiếp tục và tiếp tục với mã.

Vì vậy chúng ta sẽ tìm nạp và chuẩn bị tập dữ liệu

giống như chúng tôi đã làm trong phần trước.

Chúng tôi tạo một biến nhà ở và sau đó tiếp tục

và sử dụng công cụ tìm nạp_california_housing,

tải tập dữ liệu nhà ở California

vào nhà ở biến đổi.

Tiếp theo chúng ta có Pandas.

Hãy tiếp tục và thực sự tạo ra nó ngay tại đây.

Vậy sau biến nhà ở, chúng ta sẽ tiếp tục

và chuyển đổi sang DataFrame để hiển thị dễ dàng hơn,

và về cơ bản chúng tôi đang chuẩn bị dữ liệu của mình

ở định dạng tốt nhất có thể

để hình dung dễ dàng và trực quan.

Chúng tôi sẽ gọi đây là housing_df.

Vì vậy chúng ta sẽ gọi pd.DataFrame

để chuyển đổi dữ liệu này thành Pandas DataFrame.

Như vậy dữ liệu sẽ là housing.data mà chúng ta vừa cài đặt.

Khi đó chúng ta sẽ có các cột bằng housing.feature_names.

Sau đó chúng ta sẽ tiếp tục và nói housing_df, Target,

và điều này sẽ bằng housing.target.

Đây là cách chúng tôi xác định mục tiêu,

trong đó thêm biến mục tiêu,

trong trường hợp này, giá nhà đất được tính vào DataFrame.

Vậy chúng ta hãy tiếp tục

và bắt đầu trực quan hóa dữ liệu từ đây trở đi.

Vì vậy, hãy sửa đổi mã Python cho điều đó.

Chúng tôi sẽ trực quan hóa dữ liệu từ bây giờ,

và chúng ta sẽ bắt đầu bằng cách hiển thị một vài hàng đầu tiên,

xem dữ liệu của chúng tôi trông như thế nào, để xem cấu trúc.

Vì vậy, hãy tiếp tục và làm điều đó.

Vì vậy, hãy in, hãy gọi DataFrame, housing_df.head.

Điều này sẽ in một vài hàng đầu tiên của tập dữ liệu của chúng tôi.

Tiếp theo chúng ta có thể tiếp tục

và tạo biểu đồ SNS, đây là biểu đồ biểu đồ

với ước tính mật độ hạt nhân của biến mục tiêu

để hình dung sự phân bổ giá trị ngôi nhà.

Vì vậy, để làm được điều đó, chúng ta sẽ phải đi

và bắt đầu hình dung sự phân bố,

hình dung, những ghi chú này rất quan trọng.

Hãy tưởng tượng rằng bạn quay lại mã này sau một vài tháng.

Chúng ta có thể không nhớ mọi thứ về mật mã

mà chúng tôi đã viết, vì vậy đây luôn là một cách thực hành tốt

để tiếp tục và đưa ra một số nhận xét về những gì chúng tôi đang làm.

Vì vậy, ở đây chúng ta có hình dung về sự phân bố

của biến mục tiêu.

Vì vậy, trong trường hợp này chúng ta sẽ tiếp tục

và bắt đầu vẽ hình bằng plt.figure.

Vì vậy, đây thực sự là khởi tạo hình của chúng ta ở đây,

và sau đó chúng tôi sẽ cung cấp cho nó một kích thước.

Vậy hãy tiếp tục và làm điều đó, figsize,

và trong trường hợp này chúng ta sẽ có 10,6.

Sau đó chúng ta sẽ bắt đầu vẽ biểu đồ.

Vì vậy, điều chúng tôi sẽ làm là bắt đầu

bằng cách mã hóa sns.histplot,

và sau đó chúng ta sẽ mở dấu ngoặc đơn, housing_df,

và sau đó chúng ta sẽ có Target, và sau đó chúng ta sẽ tiếp tục

và gọi các thùng bằng 50,

và khi đó kde bằng True,

đó là ước tính mật độ hạt nhân.

Đây là ước tính của biến mục tiêu

để hình dung sự phân bổ giá trị nhà ở.

Vì vậy, hãy tiếp tục và sửa lỗi đánh máy ở đây thành Đúng.

Tuyệt vời. Vì vậy, sau đó, hãy tiếp tục và đặt cho nó một tiêu đề.

Vậy tiêu đề trong trường hợp này là

sẽ là Phân phối Giá trị Ngôi nhà.

Hãy tiếp tục và đặt cho nó một nhãn xlabel.

Vậy xlabel ở đây trong trường hợp này

sẽ là Giá trị ngôi nhà trung bình.

Sau đó chúng ta sẽ có plt.ylabel,

và nó sẽ nói Tần suất.

Vì vậy, sau khi chúng ta đưa ra nhãn y, hãy tiếp tục

và lưu hình này bằng cách nói plt.savefig.

Và sau đó chúng ta có thể nói đơn giản là vị trí,

và tất cả các số liệu sẽ được đặt trong thư mục đầu ra

như bạn có thể thấy ở khung bên trái.

Vì vậy chúng ta sẽ nói đầu ra/, tên chương, 03_02_,

và sau đó hãy gọi nó là distribution_plot.png.

Vì vậy, điều đó đảm bảo việc lưu cốt truyện.

Tiếp theo chúng ta sẽ chuyển sang biểu đồ cặp.

Vì vậy, hãy tiếp tục và nói sơ đồ các tính năng

để hiểu các mối quan hệ.

Vì vậy, điều này sẽ tạo ra một cặp âm mưu

của tất cả các tính năng và biến mục tiêu

để hình dung các mối quan hệ tiềm năng giữa chúng.

Hãy tiếp tục và tạo nó ngay bây giờ.

Vì vậy chúng ta sẽ sử dụng thư viện Seaborn

và đó là một hàm đơn giản được gọi là pairplot.

Và hàm pairplot này sẽ lấy housing_df.

Sau đó chúng ta sẽ tiếp tục và làm điều tương tự, lưu hình,

và sau đó chúng ta sẽ lưu nó vào đầu ra,

và sau đó nó sẽ có 03_02_feature_pairplot.png.

Được rồi, sau đó chúng ta có thể tiếp tục và plt.close.

Vì vậy, hãy làm điều đó, để nó không còn mở ở đây.

Và hãy tiếp tục và làm điều tương tự

trên hình trước đó là tốt.

Được rồi, tiếp theo chúng ta sẽ tiến hành chia nhỏ dữ liệu

vào các tập huấn luyện, xác nhận và kiểm tra.

Vì vậy, đầu tiên chúng tôi chia dữ liệu

vào các tập huấn luyện, xác nhận và kiểm tra.

Và sau đó là lần chia thứ hai, chia toàn bộ tập huấn luyện

thành một tập huấn luyện và xác nhận nhỏ hơn.

Vì thế điều này không mới,

do đó chúng ta có thể di chuyển nhanh hơn một chút về vấn đề này.

Vì thế chúng ta tiếp tục từ đây và chúng ta tiếp tục

và chuẩn hóa dữ liệu bằng StandardScaler.

Tiếp theo, chúng tôi chỉ định X_train,

và sau đó chúng tôi nói X_valid, rồi X_test.

Vì vậy, hãy tóm tắt lại những gì chúng tôi đã làm sau khi chia nhỏ dữ liệu

vào các tập huấn luyện, xác nhận và kiểm tra.

Chúng tôi giới thiệu StandardScaler, giúp chia tỷ lệ các tính năng

có trung bình bằng 0 và phương sai bằng 1,

và sau đó chúng tôi áp dụng fit_transform,

phù hợp với bộ chia tỷ lệ trên dữ liệu huấn luyện

và biến đổi nó.

Và sau đó chúng tôi sử dụng phép biến đổi,

áp dụng sự chuyển đổi tương tự cho việc xác thực

và bộ kiểm tra để đảm bảo tính nhất quán ở đây.

Vì vậy, trước hết, chúng tôi sử dụng fit_transform cho X_train,

và sau đó chúng tôi áp dụng phép biến đổi tương tự để xác thực

và bộ kiểm tra để đảm bảo tính nhất quán.

Tiếp theo, chúng ta sẽ tiếp tục và trực quan hóa các tính năng được chia tỷ lệ.

Vì vậy, để làm được điều đó, chúng tôi sẽ tạo một DataFrame xe lửa có tỷ lệ.

Vì vậy, hãy tiếp tục và làm điều đó ngay bây giờ.

Chúng tôi sẽ nói,

trực quan hóa một số điểm dữ liệu đào tạo được chia tỷ lệ đầu tiên,

và sau đó chúng tôi nói đã chia tỷ lệ_train_df bằng pd.DataFrame.

Và sau đó chúng ta sẽ cung cấp dữ liệu là X_train.

Hãy tiếp tục và sửa lỗi này, X_train,

và sau đó là các cột thành housing.feature_names.

Vì vậy đây sẽ là cột của chúng tôi.

Vì vậy, hãy tiếp tục và tạoscaled_train_df,

và sau đó chúng ta sẽ tạo một biến có tên Target.

Và lưu ý rằng tôi đang thay đổi dấu ngoặc đơn

và dấu ngoặc kép ở đây và ở đó.

Miễn là bạn bắt đầu với cùng một trích dẫn

và kết thúc với cùng một kiểu trích dẫn, bạn ổn.

Việc bạn sử dụng trích dẫn nào không quan trọng.

Vì vậy, cái này sẽ bằng y_train.

Được rồi, sau đó chúng ta sẽ tiếp tục

và tạo một biểu đồ hộp.

Vì vậy, trước khi tạo sơ đồ hộp, hãy đảm bảo

rằng chúng tôi đang inscaled_train_df,

vì vậy ít nhất một vài hàng.

Vậy hãy tiếp tục và làm điều đó ở đây,

in tỉ lệ_train_df.head.

Vì vậy, hãy quay lại đây và tóm tắt những gì chúng tôi đã làm.

Vì vậy, những gì chúng tôi đã làm trong pd.DataFrame đầu tiên là

chúng tôi đã chuyển đổi dữ liệu đào tạo được chia tỷ lệ thành DataFrame

để dễ hình dung hơn.

Tiếp theo, chúng tôi đã thêm biến Target

đến DataFrame đào tạo theo tỷ lệ.

Vì vậy, bây giờ DataFrame của chúng tôi chứa biến Target.

Tiếp theo, chúng tôi đang chuẩn bị sẵn sàng

để trực quan hóa sự phân bố của các tính năng được chia tỷ lệ.

Vậy hãy tiếp tục và làm điều đó ngay bây giờ,

trực quan hóa sự phân bố của các tính năng được chia tỷ lệ.

Vì vậy, chúng ta sẽ tiếp tục

và tạo một cốt truyện mới, plt.figure.

Và sau đó chúng ta sẽ lại đưa ra kích thước của cái này,

hình kích thước 12 đến 8.

Và hãy đảm bảo rằng chúng ta cũng đưa ra dấu ngoặc đơn bên trong.

Sau đó chúng ta tiếp tục và gọi Seaborn.

Những gì chúng ta gọi bây giờ là boxplot.

Vì vậy, âm mưu này là một âm mưu hình hộp

để trực quan hóa sự phân bố của các tính năng được chia tỷ lệ.

Sau đó, chúng tôi cung cấp dữ liệu là gì,

trong trường hợp của chúng tôi làscaled_train_df,

và sau đó chúng ta sẽ tiếp tục bỏ biến Target.

Vì vậy chúng ta sẽ nói .drop,

và sau đó bên trong chúng ta sẽ nói, được rồi, hãy bỏ cột Mục tiêu.

Vậy các cột bằng Target.

Vậy điều sẽ xảy ra ở đây là chúng ta sẽ có tất cả dữ liệu,

nhưng cột Mục tiêu, nghĩa là các tính năng, phải không?

Vì vậy, chúng tôi sẽ có tất cả các tính năng ở đây.

Tiếp theo chúng ta sẽ nói plt.title,

và sau đó chúng ta có thể gọi nó là Phân phối các tính năng được chia tỷ lệ.

Được rồi? Tiếp theo chúng ta sẽ nói plt.xticks.

Và khi đó chúng ta sẽ có một vòng quay là 45.

Và tiếp theo là plt.savefig một lần nữa.

Hãy đặt cho nó một vị trí và tên.

Vì vậy, đây lại là thư mục đầu ra mà chúng ta đang sử dụng.

Và sau đó chúng tôi đặt tên phần 03_02_,

và sau đó chúng ta sẽ nói,

đây là Scaled_features_distribution.png.

Tiếp theo chúng ta sẽ tiếp tục và đóng cái này lại.

Vì vậy sau khi chúng ta chăm sóc

của biểu đồ phân phối các tính năng được chia tỷ lệ

sử dụng thư viện Seaborn, tiếp theo là

khởi tạo một mô hình tuần tự đơn giản.

Vì vậy, hãy tiếp tục và tiếp tục với điều đó.

Vì vậy, chúng ta sẽ khởi tạo một mô hình tuần tự đơn giản,

và sau đó mô hình sẽ bằng tf.keras.Sequential.

Vì vậy, điều này khởi tạo mô hình tuần tự.

Vì vậy hãy tiếp tục và mở dấu ngoặc đơn,

thì chúng ta sẽ nói tf.keras,

và sau đó chúng ta sẽ có .layers.Dense,

và sau đó chúng tôi sẽ cho nó 30 nơ-ron.

Vì vậy, điều này bổ sung thêm một lớp dày đặc, được kết nối đầy đủ với 30 nơ-ron.

Điều này tương tự như mô hình mà chúng tôi đã xây dựng trước đó.

Chúng tôi sẽ có một kích hoạt dưới dạng relu.

Vì vậy chúng ta hãy tiếp tục và làm điều đó ở đây.

Tiếp theo chúng ta sẽ đưa ra hình dạng đầu vào

để thiết lập số lượng tính năng trong dữ liệu huấn luyện,

đó là input_shape bằng X_train.shape, từ 1 trở đi.

Được rồi, dấu phẩy.

Và sau đó điều chúng tôi làm là tiếp tục

và thêm lớp đầu ra với một nơ-ron tiếp theo.

Vì vậy, để làm điều đó, chúng tôi lại gọi tf.keras.layers,

và lần này chúng tôi nói Dày đặc,

và sau đó chúng tôi tạo cho nó một lớp.

Tiếp theo chúng ta có dấu ngoặc đơn đóng, dấu ngoặc đơn đóng.

Sau đó chúng ta tiếp tục và biên dịch mô hình.

Vậy hãy đặt tiêu đề cho nó,

biên dịch mô hình.

Vì vậy chúng ta sẽ nói model.compile,

cấu hình mô hình cho việc huấn luyện.

Chúng ta phải chấp nhận sự mất mát.

Vì vậy, chúng ta sẽ nói tổn thất bằng hai sai số bình phương trung bình.

Vì vậy chúng ta sẽ nói có nghĩa là bình phương_lỗi,

và sau đó chúng tôi sẽ cung cấp một trình tối ưu hóa,

đó là độ dốc giảm dần ngẫu nhiên trong trường hợp của chúng tôi.

Vì vậy, hãy tiếp tục và làm điều đó, trình tối ưu hóa bằng sgd.

Vì vậy, đây là trình tối ưu hóa của chúng tôi ở đây.

Vì vậy, sau đó, chúng ta tiếp tục và huấn luyện mô hình.

Vì vậy, hãy tiếp tục và làm điều đó, đào tạo mô hình.

Và để làm được điều đó, chúng tôi sử dụng model.fit,

và chúng tôi cung cấp cho nó X_train,

và sau đó chúng tôi cung cấp các tính năng

và biến mục tiêu, y_train.

Và sau đó chúng tôi cho rằng kỷ nguyên là 20,

đó là số lần lặp.

Và sau đó chúng tôi đưa ra validation_data bằng,

chúng tôi đã chuẩn bị sẵn những thông tin đó là X_valid và y_valid.

Chúng ta phải tiếp tục và chỉ định nó

đến một biến gọi là lịch sử.

Vì vậy, sau khi đào tạo mô hình, chúng tôi sẽ tiếp tục và đánh giá nó.

Vì vậy, chúng tôi bắt đầu với việc đánh giá mô hình.

Sau tiêu đề, chúng ta hãy tiếp tục và làm điều đó.

Vì vậy chúng ta sẽ sử dụng sai số bình phương trung bình để đánh giá.

Vì vậy, chúng ta sẽ nói, mse_test bằng model.evaluate,

và sau đó việc này sẽ thực hiện X_test.

Về cơ bản so sánh nó với X_test với y_test,

và sau đó nó sẽ đưa ra một lỗi bình phương trung bình cho chúng ta.

Sau đó hãy tiếp tục và in kết quả

bằng cách nói in giá trị trung bình,

giống như chúng ta đã làm trước đó, bình phương lỗi trên tập kiểm tra.

Và sau đó chúng tôi sẽ cung cấp cho nó mse_test. Tuyệt vời.

Vì vậy, để tóm tắt, mã bắt đầu bằng cách tải

và khám phá bộ dữ liệu nhà ở California,

trực quan hóa việc phân phối dữ liệu và các mối quan hệ tính năng.

Nó chia dữ liệu thành đào tạo và xác nhận,

và các bộ kiểm tra, sau đó chia tỷ lệ cho các tính năng.

Và sau khi trực quan hóa dữ liệu được chia tỷ lệ, nó sẽ xây dựng

và huấn luyện một mạng lưới thần kinh đơn giản bằng cách sử dụng TensorFlow.

Cuối cùng, mô hình được đánh giá trên tập kiểm tra,

và lỗi bình phương trung bình được in

để đánh giá hiệu quả của các mô hình.

Vì vậy, nếu bạn làm theo, thật tuyệt.

Nếu không, hãy mở 03_02_end.py,

và chạy thử bằng cách nhấp vào hình tam giác nhỏ.

Và sau đó chúng ta hãy xem lại kết quả một lần nữa

trước khi chúng ta kết thúc phiên xử lý trước cụ thể này

và nó ảnh hưởng như thế nào đến các mô hình TensorFlow.

Vì vậy, chỉ mất vài phút, không quá lâu,

và nó sẽ bắt đầu in kết quả của chúng ta ở đây.

Những cảnh báo này là ổn và được mong đợi.

Vì vậy, đây là tập dữ liệu của chúng tôi.

Vậy chúng ta có thu nhập trung bình, tuổi nhà, số phòng trung bình,

phòng ngủ trung bình, dân số, công suất sử dụng trung bình,

vĩ độ, kinh độ và mục tiêu.

Mục tiêu là loại giá trị bình thường hóa của giá nhà.

Vì vậy, ở đây chúng ta đang thấy ảnh chụp nhanh của tập dữ liệu nhà ở của chúng ta

mà chúng tôi đã in lúc đầu.

Đây là những gì chúng ta thấy ở đây qua bản in.

Vì vậy, nó vẫn chạy ở chế độ nền,

và chúng ta có thể theo dõi tiến trình trong thiết bị đầu cuối

và xem mã của chúng tôi đang hoạt động như thế nào.

Và sau đó, chúng ta có thể

tiếp tục và thực hiện một số so sánh

và phán đoán dựa trên kết quả.

Vậy là nó đã trải qua hơn 20 lần lặp như chúng tôi yêu cầu.

Vì thế phải nhanh chóng,

vì chúng tôi cũng đã loại bỏ việc sử dụng GPU,

và nó sẽ bắt đầu in ra lỗi bình phương trung bình

trên tập kiểm tra của chúng tôi, là 0,35.

Và đầu ra là

làm nổi bật sơ đồ phân phối mà chúng ta có.

Vì vậy, chúng ta có thể thấy sự phân bổ về giá trị ngôi nhà trung bình

bằng cách mở thư mục đầu ra

và tìm phiên cụ thể mà chúng ta đang tham gia,

đó là 03_02_distribution_plot.

Tiếp theo, chúng ta có thể thấy các cặp đặc điểm,

và chúng ta có thể phải phóng to để xem các cặp đặc điểm.

Vì vậy, đây là cách mục tiêu thay đổi theo tuổi nhà,

phòng trung bình, phòng ngủ trung bình, vân vân,

và tất cả các tính năng khác mà chúng ta có thể thấy ở đây.

Chúng ta có thể nhìn vào mối quan hệ giữa chúng.

Tiếp theo chúng ta có thể thấy sự phân bổ các tính năng được chia tỷ lệ.

Đây là thu nhập trung bình của chúng ta, tuổi nhà, số phòng trung bình,

phòng ngủ trung bình, dân số, công suất sử dụng trung bình,

vĩ độ và kinh độ sau khi chúng tôi thực hiện chia tỷ lệ.

Cuối cùng, chúng tôi đánh giá mô hình

và sau đó in lỗi bình phương trung bình

như được hiển thị trong thiết bị đầu cuối.

Vì vậy, điều này tóm tắt phần của chúng tôi,

quá trình xử lý trước ảnh hưởng đến mô hình TensorFlow như thế nào.

Hẹn gặp lại các bạn trong buổi tiếp theo.
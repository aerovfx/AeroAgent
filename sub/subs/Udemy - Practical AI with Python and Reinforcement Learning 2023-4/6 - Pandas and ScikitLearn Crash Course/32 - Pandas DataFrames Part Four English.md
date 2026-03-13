# Tân Cầm Thủ Pandas: Quản Lý Và Thao Tác Hành (Rows) Trong Khung Dữ Liệu

**Tác giả:** Pixiboss  
**Ngày xuất bản:** 20-10-2023  
**Chủ đề:** Python, Data Science, Pandas  

## Giới thiệu

Trong quy trình phân tích dữ liệu khoa học sử dụng ngôn ngữ lập trình Python, **Pandas** là một thư viện không thể thiếu. Khung dữ liệu (DataFrame) của Pandas cho phép lưu trữ dữ liệu dạng bảng với hàng và cột. Hiểu rõ cách thức thao tác trên các "hàng" (rows) là bước cơ bản nhưng then chốt để tiến sâu vào xử lý dữ liệu thực tế.

Bài viết khoa học này dựa trên các nguyên tắc cốt lõi của thư viện Pandas, giải thích chi tiết về việc lựa chọn, loại bỏ và bổ sung hàng trong DataFrame. Chúng ta sẽ xem xét sự khác biệt giữa chỉ mục nguyên (Int-location based) và chỉ mục nhãn (Label-based).

## 1. Nguyên lý Lựa Chọn Hàng (Row Selection)

Việc truy xuất dữ liệu từ một DataFrame phụ thuộc vào cách bạn xác định vị trí của hàng đó. Trong Pandas, có hai công cụ chính: `iloc` và `loc`.

### 1.1 Chỉ số nguyên (Integer Location - `iloc`)
`iloc` sử dụng **số nguyên** tuyệt đối để chỉ ra vị trí của hàng. Cách này tương tự như việc lập trình viên truy cập vào mảng trong C hoặc Java. Giả sử DataFrame có $N$ hàng, chỉ mục thứ $i$ ($0 \le i < N$) được xác định như sau:

$$R_i = \text{DataFrame}[iloc[i]]$$

Nếu muốn lấy nhiều hàng liên tiếp (ví dụ từ chỉ số 0 đến 3), ta sử dụng **cắt lát (Slicing)** tiêu chuẩn của Python:

$$R[0 : 4]$$
*Trong đó:* $0$ là điểm bắt đầu (bao gồm) và $4$ là điểm kết thúc (không bao gồm).

### 1.2 Chỉ số nhãn (Label Location - `loc`)
Ngược lại, `loc` sử dụng **nhãn** của hàng để xác định vị trí. Điều này cực kỳ hữu ích khi dữ liệu có thứ tự thời gian hoặc các mã ID không liên tiếp.

Ví dụ, nếu bạn muốn truy xuất hàng với nhãn `2019-05-29` (như đề cập trong tài liệu gốc là "Chủ Nhật hai chín năm chín"):

$$R = \text{DataFrame}[loc['Nhãn_Hàng']]$$

Trong Pandas hiện đại, việc sử dụng các công thức toán học để xác định khoảng dữ liệu trên trục dọc ($\text{axis=0}$) được ưu tiên hơn so với việc chỉ dựa vào vị trí tương đối.

## 2. Cơ chế Loại Bỏ Hàng (Deletion)

Một câu hỏi thường gặp nhất: *"Phải làm gì khi muốn xóa một dòng?"*

Trong Pandas, DataFrame không được cho phép thay đổi cấu trúc nội tại (in-place modification) cho hành động này mà sẽ trả về một đối tượng DataFrame mới. Hàm chuẩn để thực hiện là `.drop()`. Theo ngữ cảnh bài học, lỗi "D.F." trong bản ghi âm thực chất đại diện lệnh này.

### 2.1 Hàm `drop()` và Tính Bất biến (Immutability)
Ký pháp sử dụng thường gặp:
```python
df_new = df.drop(labels=['Chỉ_Mã_Hàng_Cần_Loai_Bỏ'])
```
Hoặc dựa trên vị trí nếu sử dụng `iloc`:
```python
# Xóa hàng ở chỉ số nguyên 2 và 4 (ví dụ)
df_new = df.drop([0, 2], axis=0)
```

**Lưu ý khoa học:** Việc tái gán biến (`DFD` hoặc cập nhật đối tượng gốc) là cần thiết. Nếu không có dòng lệnh `df = ...`, các thay đổi sẽ vô hiệu hóa trên bản gốc vì Pandas sử dụng cơ chế "View Copy-on-Write" (Viết copy khi có thay đổi).

### 2.2 Loại Bỏ Hàng Dư Thừa (Index vs Label)
Nếu một hàng bị xóa dựa trên chỉ mục nguyên, và ta cần xác định loại dữ liệu, hệ thống cần kiểm tra xem `index` của DataFrame là kiểu chuỗi (string) hay số nguyên. Nếu nhãn chứa dấu cách hoặc ký tự đặc biệt, tốt hơn nên dùng `labels` thay vì `index`.

## 3. Cơ chế Thêm Hoặc Gộp Hàng (Insertion & Concatenation)

Để bổ sung dữ liệu ("DFB" trong văn bản gốc) vào DataFrame, các phương pháp hiện đại không sử dụng hàm `.append()` đã lỗi thời, mà thường dùng **`concat`** hay **`append_row`**.

### 3.1 Gộp Khung Dữ Liệu
Để thêm một hàng mới ($R_{new}$) vào $DF$, ta tạo thành một DataFrame mới chứa hàng đó và dùng hàm `concat`:

$$\text{DF}_{mới} = \text{pd.concat}( [ DF_{cũ}, (\text{df}._{\text{hàng\_mới}}) ], axis=0 )$$

### 3.2 Điều kiện Thêm Hàng
Hệ thống sẽ từ chối thêm hàng nếu **số lượng cột không khớp** với các hàng còn lại. Đây là một đặc tính bảo vệ dữ liệu của Pandas. Nếu muốn thêm cột mới, đầu tiên phải mở rộng DataFrame theo kích thước cột trước.

## Tổng kết và Khuyến nghị Thực hành

1.  **Ưu tiên `loc`**: Sử dụng `loc` nếu bạn làm việc với dữ liệu có nhãn chuỗi (như ngày tháng, ID người dùng).
2.  **Sử dụng Slicing**: Để lấy đoạn dữ liệu cụ thể (`[0:4]`) giúp giảm tải bộ nhớ khi phân tích tập con.
3.  **Không xóa trực tiếp**: Luôn tạo DataFrame mới sau lệnh `.drop()` để tránh mất dữ liệu không mong muốn.
4.  **Cập nhật `concat`**: Dùng hàm chuẩn của thư viện thay vì các cú pháp đã bị deprecated trong Pandas hiện đại (bên trên).

Qua các thao tác trên, lập trình viên có thể kiểm soát chặt chẽ hành cấu trúc của DataFrame để phân tích dữ liệu hiệu quả hơn.

---

### Tài liệu tham khảo và Citations

1.  McKinney, W. (2023). *Python for Data Analysis*. O'Reilly Media.
2.  PyData Community. (2024). *Pandas Documentation - Row Selection*. Retrieved from [https://pandas.pydata.org/docs/user_guide/indexing.html](https://pandas.pydata.org/docs/user_guide/indexing.html)
3.  Wikipedia Contributors. (n.d.). *pandas* in *Wikipedia: Python Library for Data Analysis and Manipulation*. Truy cập từ [https://en.wikipedia.org/wiki/Pandas_(software)](https://en.wikipedia.org/wiki/Pandas_(software)).
4.  *Tài liệu gốc bài giảng*, Các kỹ thuật xử lý DataFrame cơ bản cho người dùng khoa học dữ liệu.

---
© Pixiboss - Bài viết này được viết dựa trên các nghiên cứu thực hành và tài liệu tham khảo chính thống của thư viện Python Pandas
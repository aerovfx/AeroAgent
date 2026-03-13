# Chương 4. Tóm tắt Học tập tăng cường sâu trong thực tế, Phiên bản video đã được dịch

---

Bản tóm tắt.

Xác suất là một cách ấn định mức độ tin cậy về các kết quả khác nhau có thể xảy ra trong một quá trình không thể đoán trước.

Mỗi kết quả có thể xảy ra được ấn định một xác suất trong khoảng 0, 1, sao cho tất cả xác suất cho tất cả các kết quả có tổng bằng 1.

Nếu chúng ta tin rằng một kết quả cụ thể có nhiều khả năng xảy ra hơn kết quả khác, thì chúng ta gán cho nó một xác suất cao hơn.

Nếu chúng ta nhận được thông tin mới, chúng ta có thể thay đổi cách gán xác suất.

Phân bố xác suất là sự mô tả đầy đủ các xác suất được ấn định cho các kết quả có thể xảy ra.

Phân phối xác suất có thể được coi là hàm PO ánh xạ tới khoảng 0, 1.

Điều đó ánh xạ tất cả các kết quả có thể xảy ra thành một số thực trong khoảng 0, 1, sao cho tổng của hàm này trên tất cả các kết quả là 1.

Phân bố xác suất suy biến là phân bố xác suất trong đó chỉ có một kết quả có thể xảy ra.

Nghĩa là, nó có xác suất là 1 và tất cả các kết quả khác có xác suất là 0.

Xác suất có điều kiện là xác suất được gán cho một kết quả, giả sử bạn có một số thông tin bổ sung, thông tin có điều kiện.

Chính sách là một hàm, tích của pi và s dẫn đến a, ánh xạ trạng thái tới hành động và thường được triển khai dưới dạng hàm xác suất, pi nhân với xác suất của một s nhất định, tạo ra phân bố xác suất cho các hành động nhất định ở một trạng thái.

Tiền hoàn lại là tổng số phần thưởng được chiết khấu trong một giai đoạn của môi trường.

Phương pháp gradient chính sách là một phương pháp học tăng cường cố gắng học trực tiếp một chính sách bằng cách sử dụng hàm được tham số hóa làm hàm chính sách, chẳng hạn như mạng thần kinh và huấn luyện nó để tăng xác suất hành động dựa trên phần thưởng được quan sát.

Củng cố là cách triển khai đơn giản nhất của phương pháp gradient chính sách. Về cơ bản, nó tối đa hóa xác suất của một hành động nhân với phần thưởng được quan sát sau khi thực hiện hành động đó, sao cho xác suất của mỗi hành động, trong một trạng thái, được điều chỉnh theo quy mô của phần thưởng được quan sát.
## 🚀 Smart Regex Patterns

Thay vì hardcode từng cụm từ, sử dụng pattern tổng quát:

```python
r'(Trắc\s*nghiệm|Bài\s*tập|Đề\s*thi)\s+[^:]*\s*\(?có\s*đáp\s*án\)?\s*:?\s*'
```

- **Kết quả:** Bắt được mọi biến thể về khoảng trắng, dấu câu, viết hoa/thường.

---

## 🧠 Multi-Layer Cleaning Pipeline

**Layer 0: Normalize Text**
- Chuẩn hóa dấu nháy, dấu gạch, khoảng trắng
- Chuẩn hóa dấu câu

**Layer 1: Smart Pattern Removal**
- 7 nhóm pattern tổng quát
- Case-insensitive, multiline matching
- Tự động xử lý biến thể

**Layer 2: Smart Validation**
- `is_valid_question()`: Kiểm tra blacklist, độ dài, tỷ lệ chữ cái
- `is_valid_option()`: Đáp án hợp lý, loại bỏ text chỉ có số/ký tự đặc biệt

**Layer 3: Final Cleanup**
- Xóa markdown dư thừa
- Làm sạch dấu câu
- Chuẩn hóa text lần cuối

---

## 📊 Enhanced Parsing với Multiple Patterns

- 4 patterns khác nhau xử lý mọi format:
    1. Standard "Câu X:" format
    2. Direct question format
    3. Compact format
    4. Multi-line questions
- Fallback: State machine parsing khi regex thất bại

---

## 🛡️ Robust Validation System

**Question validation:**
- Tối thiểu 15 ký tự
- Kiểm tra blacklist
- Ít nhất 3 từ có nghĩa
- Tỷ lệ chữ cái ≥ 50%

**Option validation:**
- Tối thiểu 3 ký tự
- Không nằm trong blacklist
- Tỷ lệ chữ cái ≥ 30%
- Không chỉ chứa số

---

## 🎯 Key Benefits

- Không hardcode cụm từ cụ thể
- Tự động nhận diện biến thể mới
- Hỗ trợ đa dạng format website
- Đảm bảo chất lượng quiz
- Dễ bảo trì, mở rộng, debug

---

## 📈 Performance Improvements

**Trước khi có smart system:**
- Input: `"Trắc nghiệm Vật Lí 12 Kết nối tri thức Bài 8 (có đáp án): Câu 1: Một vật dao động..."`
- Output: `"Trắc nghiệm Vật Lí 12 Kết nối tri thức Bài 8 (có đáp án): Một vật dao động..."` ❌

**Sau khi có smart system:**
- Input: `"Trắc nghiệm Vật Lí 12 Kết nối tri thức Bài 8 (có đáp án): Câu 1: Một vật dao động..."`
- Output: `"Một vật dao động điều hòa đang chuyển động từ vị trí biên về vị trí cân bằng..."` ✅

---

## 🔧 Extensibility

**Thêm pattern mới:**
```python
# Chỉ cần thêm vào patterns dictionary
'new_category': [
    r'pattern_for_new_noise_type',
    r'another_variant_pattern'
]
```

**Thêm validation rule mới:**
```python
def is_valid_question(self, question: str) -> bool:
    # ... existing validation ...
    # Thêm rule mới
    if self.contains_mathematical_symbols(question):
        return self.validate_math_question(question)
    return True
```

---

## 💡 Optional Extensions

1. **Fuzzy Matching cho edge cases:**
    ```python
    from rapidfuzz import fuzz

    def fuzzy_blacklist_check(self, text: str) -> bool:
        for keyword in self.question_blacklist:
            if fuzz.partial_ratio(keyword, text.lower()) > 85:
                return True
        return False
    ```

2. **NLP-based validation:**
    ```python
    import spacy

    def nlp_validate_question(self, question: str) -> bool:
        doc = self.nlp(question)
        has_verb = any(token.pos_ == "VERB" for token in doc)
        has_noun = any(token.pos_ == "NOUN" for token in doc)
        return has_verb and has_noun
    ```

3. **Statistical filtering:**
    ```python
    def statistical_filter(self, questions: List[str]) -> List[str]:
        avg_length = np.mean([len(q) for q in questions])
        std_length = np.std([len(q) for q in questions])
        return [q for q in questions if abs(len(q) - avg_length) <= 2 * std_length]
    ```

---

Hệ thống này giúp làm sạch dataset hiệu quả, linh hoạt và dễ mở rộng.
from docx import Document
import io

def parse_rubric(doc_bytes: bytes) -> list[dict]:
    doc = Document(io.BytesIO(doc_bytes))
    criteria = []
    for table in doc.tables:
        for row in table.rows[1:]:  # Skip header
            criterion = row.cells[0].text.strip()
            desc = row.cells[1].text.strip()
            max_points = float(row.cells[2].text.strip())
            criteria.append({"criterion": criterion, "desc": desc, "max": max_points})
    return criteria
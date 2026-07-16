from utils.file_handler import FileHandler


def test_read_json_file(tmp_path):
    path = tmp_path / "employees.json"
    path.write_text('[{"employee_id": 1, "name": "Alice"}]', encoding="utf-8")
    data = FileHandler.read_json(str(path))
    assert data[0]["name"] == "Alice"

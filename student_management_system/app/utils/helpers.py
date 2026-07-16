import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(exist_ok=True)


class StudentExample:
    def __init__(self, name: str, grade: int):
        self.name = name
        self.grade = grade

    def describe(self) -> str:
        if self.grade >= 90:
            return "Excellent"
        elif self.grade >= 70:
            return "Good"
        else:
            return "Needs Improvement"


def demonstrate_python_concepts() -> Dict[str, Any]:
    sample_list = ["Classes", "Functions", "JSON"]
    sample_dict = {"topic": "FastAPI", "level": "Intermediate"}
    items = []

    for item in sample_list:
        if item:
            items.append(item)
            if item == "JSON":
                break
        continue

    comprehension_example = [item.lower() for item in items]
    return {
        "list_example": sample_list,
        "dict_example": sample_dict,
        "for_loop_example": items,
        "comprehension_example": comprehension_example,
        "isinstance_example": isinstance(sample_dict, dict),
        "dir_example": [name for name in dir(StudentExample) if not name.startswith("__")],
        "callable_example": callable(demonstrate_python_concepts),
    }


def read_json(file_name: str) -> List[Dict[str, Any]]:
    path = DATA_DIR / file_name
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(file_name: str, data: List[Dict[str, Any]]) -> None:
    path = DATA_DIR / file_name
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, default=str)


def now_timestamp() -> str:
    return datetime.utcnow().isoformat()

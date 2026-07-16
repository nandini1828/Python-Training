import json
from pathlib import Path
from typing import Any, Dict, List


class FileStorage:
    def __init__(self, file_name: str):
        self.base_dir = Path(__file__).resolve().parents[1] / "data"
        self.base_dir.mkdir(exist_ok=True)
        self.file_path = self.base_dir / file_name

    def read(self) -> List[Dict[str, Any]]:
        if not self.file_path.exists():
            return []
        with self.file_path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def write(self, data: List[Dict[str, Any]]) -> None:
        with self.file_path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, default=str)

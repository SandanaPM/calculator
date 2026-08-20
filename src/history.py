import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


class HistoryManager:
    """Stores and retrieves calculator history using JSON persistence."""

    def __init__(self, file_path: str = "data/history.json") -> None:
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.records: List[Dict[str, Any]] = []
        self.load()

    def load(self) -> None:
        if not self.file_path.exists():
            self.records = []
            return

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            self.records = data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            # A damaged/missing file should not stop the application.
            self.records = []

    def save(self) -> None:
        temporary = self.file_path.with_suffix(".tmp")
        with temporary.open("w", encoding="utf-8") as file:
            json.dump(self.records, file, indent=2)
        temporary.replace(self.file_path)

    def add(self, operation: str, operands: List[str], result: str) -> Dict[str, Any]:
        record = {
            "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
            "operation": operation.upper(),
            "operands": operands,
            "result": result,
        }
        self.records.append(record)
        self.save()
        return record

    def clear(self) -> None:
        self.records = []
        self.save()

    def search(self, keyword: str) -> List[Dict[str, Any]]:
        keyword = keyword.strip().lower()
        if not keyword:
            return self.records.copy()

        return [
            record
            for record in self.records
            if keyword in record["operation"].lower()
            or keyword in record["result"].lower()
            or any(keyword in str(value).lower() for value in record["operands"])
        ]

    def sort_records(self, key: str = "timestamp", reverse: bool = True) -> List[Dict[str, Any]]:
        allowed = {"timestamp", "operation", "result"}
        if key not in allowed:
            raise ValueError(f"Sort key must be one of: {', '.join(sorted(allowed))}.")
        return sorted(
            self.records,
            key=lambda record: record.get(key, ""),
            reverse=reverse,
        )

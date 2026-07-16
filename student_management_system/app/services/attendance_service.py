from datetime import date, datetime
from typing import List, Optional

from app.models.attendance_model import Attendance, AttendanceCreate, AttendanceUpdate
from app.utils.file_handler import FileStorage


class AttendanceService:
    def __init__(self):
        self.storage = FileStorage("attendance.json")

    def list_attendance(self, skip: int = 0, limit: int = 100, student_id: Optional[int] = None, course_id: Optional[int] = None) -> List[Attendance]:
        attendance = self.storage.read()
        if student_id is not None:
            attendance = [record for record in attendance if record.get("student_id") == student_id]
        if course_id is not None:
            attendance = [record for record in attendance if record.get("course_id") == course_id]
        return [Attendance.model_validate(record) for record in attendance[skip: skip + limit]]

    def get_attendance(self, attendance_id: int) -> Optional[Attendance]:
        for record in self.storage.read():
            if record.get("id") == attendance_id:
                return Attendance.model_validate(record)
        return None

    def create_attendance(self, attendance_data: AttendanceCreate) -> Attendance:
        attendance = self.storage.read()
        attendance_id = max((record.get("id", 0) for record in attendance), default=0) + 1
        payload = attendance_data.model_dump()
        payload["id"] = attendance_id
        payload["created_at"] = datetime.utcnow().isoformat()
        attendance.append(payload)
        self.storage.write(attendance)
        return Attendance.model_validate(payload)

    def update_attendance(self, attendance_id: int, attendance_data: AttendanceUpdate) -> Optional[Attendance]:
        attendance = self.storage.read()
        for index, record in enumerate(attendance):
            if record.get("id") == attendance_id:
                updated = {**record, **attendance_data.model_dump(exclude_unset=True)}
                attendance[index] = updated
                self.storage.write(attendance)
                return Attendance.model_validate(updated)
        return None

    def delete_attendance(self, attendance_id: int) -> bool:
        attendance = self.storage.read()
        remaining = [record for record in attendance if record.get("id") != attendance_id]
        if len(remaining) == len(attendance):
            return False
        self.storage.write(remaining)
        return True

    def get_summary(self) -> dict:
        records = self.storage.read()
        total = len(records)
        present = sum(1 for record in records if record.get("status") == "present")
        absent = sum(1 for record in records if record.get("status") == "absent")
        late = sum(1 for record in records if record.get("status") == "late")
        excused = sum(1 for record in records if record.get("status") == "excused")
        return {
            "total": total,
            "present": present,
            "absent": absent,
            "late": late,
            "excused": excused,
        }

    def seed_demo_data(self) -> None:
        if self.storage.read():
            return
        demo_attendance = [
            {
                "id": 1,
                "student_id": 1,
                "course_id": 1,
                "attendance_date": date.today(),
                "status": "present",
                "notes": "On time",
                "created_at": datetime.utcnow().isoformat(),
            },
            {
                "id": 2,
                "student_id": 2,
                "course_id": 2,
                "attendance_date": date.today(),
                "status": "absent",
                "notes": "Sick leave",
                "created_at": datetime.utcnow().isoformat(),
            },
        ]
        self.storage.write(demo_attendance)

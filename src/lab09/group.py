import csv
import sys
from pathlib import Path
sys.path.append("../lab08")
from models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists() or self.path.stat().st_size == 0:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
                writer.writeheader()

    def _read_all(self):
        students = []
        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(
                    Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                )
        return students 

    def list(self):
       return self._read_all()

    def add(self, student: Student):
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def find(self, substr: str):
        students = self._read_all()
        found = []
        
        for student in students:
            if substr in student.fio:
                found.append(student)
        
        return found


    def remove(self, fio: str):
        students = self._read_all()
        
        for i in range(len(students)):
            if students[i].fio == fio:
                students.pop(i) 
                
                with self.path.open("w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["fio", "birthdate", "group", "gpa"])
                    for student in students:
                        writer.writerow([student.fio, student.birthdate, student.group, student.gpa])
                return True
        
        return False  
         

    def update(self, fio: str, **fields):
        students = self._read_all()
        updated = False
        
        for student in students:
            if student.fio == fio:
                if "fio" in fields:
                    student.fio = fields["fio"]
                if "birthdate" in fields:
                    student.birthdate = fields["birthdate"]
                if "group" in fields:
                    student.group = fields["group"]
                if "gpa" in fields:
                    student.gpa = float(fields["gpa"])
                updated = True
                break
        
        if updated:
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])
                for student in students:
                    writer.writerow([student.fio, student.birthdate, student.group, student.gpa])
        
        return updated
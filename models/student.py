from pydantic import BaseModel, Field
from enum import Enum

class HighSchoolType(str, Enum):
    public = "public"
    private = "private"
    other = "other"

class Student(BaseModel):
    age: int
    gender: str
    high_school_type: HighSchoolType
    enem_score: float
    family_income: float
    works: bool
    weekly_work_hours: int
    first_semester_failures: int
    scholarship_holder: bool
    distance_to_campus_km: float

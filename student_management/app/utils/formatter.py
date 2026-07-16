from app.models.course import Course
from app.models.student import Student
from app.utils.converter import safe_int
from app.utils.helper import describe_object


def student_to_dict(student: Student) -> dict[str, object]:
    return {
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "address": student.address.full_address(),
        "courses": student.courses,
        "python_topics": {
            "data_types": {
                "student_id": type(student.student_id).__name__,
                "name": type(student.name).__name__,
                "age": type(student.age).__name__,
                "courses": type(student.courses).__name__,
            },
            "oop": "Student is a class. Each saved student is an object.",
            "composition": "Student has an Address object inside it.",
            "dunder_methods": {
                "__str__": str(student),
                "__len__": len(student),
            },
            "introspection": {
                "type": type(student).__name__,
                "is_student": isinstance(student, Student),
                "dir_sample": dir(student)[:5],
                "helper_result": describe_object(student),
            },
            "truthiness": {
                "has_courses": bool(student.courses),
                "has_name": bool(student.name),
            },
        },
    }


def course_to_dict(course: Course) -> dict[str, object]:
    course_dictionary = {
        "course_id": course.course_id,
        "name": course.name,
        "duration_weeks": course.duration_weeks,
    }

    return {
        **course_dictionary,
        "summary": course.summary(),
        "enrolled_student_ids": course.enrolled_student_ids,
        "python_topics": {
            "list": {
                "value": course.enrolled_student_ids,
                "meaning": "A list is ordered and changeable.",
            },
            "tuple": {
                "value": ("beginner", "api"),
                "meaning": "A tuple is ordered and usually not changed.",
            },
            "set": {
                "value": list(set(course.enrolled_student_ids)),
                "meaning": "A set keeps unique values.",
            },
            "dictionary_and_json": {
                "dictionary": course_dictionary,
                "json_like_response": "FastAPI converts dictionaries to JSON.",
            },
            "type_casting": {
                "duration_as_string": str(course.duration_weeks),
                "duration_as_float": float(course.duration_weeks),
            },
            "safe_conversions": "Use helper functions when user input may be invalid.",
            "safe_casting_example": {
                "valid_number": safe_int(str(course.duration_weeks)),
                "invalid_number": safe_int("not-a-number"),
            },
            "type_hints": "This function returns dict[str, object].",
            "dunder_methods": {
                "__len__": len(course),
            },
        },
    }

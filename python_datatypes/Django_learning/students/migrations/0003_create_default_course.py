from django.db import migrations


def create_default_course(apps, schema_editor):
    Course = apps.get_model("students", "Course")
    Course.objects.get_or_create(name="Django", defaults={"description": "Core Django course"})
    Course.objects.get_or_create(name="DRF", defaults={"description": "Django REST Framework"})


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0002_course_student_owner_profile_student_courses"),
    ]

    operations = [
        migrations.RunPython(create_default_course, reverse_code=migrations.RunPython.noop),
    ]

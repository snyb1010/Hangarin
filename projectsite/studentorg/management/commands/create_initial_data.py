from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_colleges()
        self.create_programs()
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def create_colleges(self):
        colleges = [
            'College of Engineering and Technology',
            'College of Sciences',
            'College of Humanities and Social Sciences',
            'College of Business and Accountancy',
            'College of Education',
            'College of Nursing and Health Sciences',
        ]
        for college_name in colleges:
            College.objects.get_or_create(college_name=college_name)

        self.stdout.write(self.style.SUCCESS(
            'Initial data for colleges created successfully.'
        ))

    def create_programs(self):
        programs = [
            ('Bachelor of Science in Computer Science', 'College of Engineering and Technology'),
            ('Bachelor of Science in Information Technology', 'College of Engineering and Technology'),
            ('Bachelor of Science in Civil Engineering', 'College of Engineering and Technology'),
            ('Bachelor of Science in Biology', 'College of Sciences'),
            ('Bachelor of Science in Mathematics', 'College of Sciences'),
            ('Bachelor of Arts in Communication', 'College of Humanities and Social Sciences'),
            ('Bachelor of Science in Psychology', 'College of Humanities and Social Sciences'),
            ('Bachelor of Science in Accountancy', 'College of Business and Accountancy'),
            ('Bachelor of Science in Business Administration', 'College of Business and Accountancy'),
            ('Bachelor of Secondary Education', 'College of Education'),
            ('Bachelor of Elementary Education', 'College of Education'),
            ('Bachelor of Science in Nursing', 'College of Nursing and Health Sciences'),
        ]
        for prog_name, college_name in programs:
            college = College.objects.filter(college_name=college_name).first()
            if college:
                Program.objects.get_or_create(prog_name=prog_name, college=college)

        self.stdout.write(self.style.SUCCESS(
            'Initial data for programs created successfully.'
        ))

    def create_organization(self, count):
        fake = Faker()

        for _ in range(count):
            words = [fake.word() for _ in range(2)]
            organization_name = ' '.join(words)

            Organization.objects.create(
                name=organization_name.title(),
                college=College.objects.order_by('?').first(),
                description=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS(
            'Initial data for organization created successfully.'
        ))

    def create_students(self, count):
        fake = Faker('en_PH')

        for _ in range(count):
            Student.objects.create(
                student_id=f"{fake.random_int(2020, 2025)}-"
                           f"{fake.random_int(1, 8)}-"
                           f"{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=Program.objects.order_by('?').first()
            )

        self.stdout.write(self.style.SUCCESS(
            'Initial data for students created successfully.'
        ))

    def create_membership(self, count):
        fake = Faker()

        for _ in range(count):
            OrgMember.objects.create(
                student=Student.objects.order_by('?').first(),
                organization=Organization.objects.order_by('?').first(),
                date_joined=fake.date_between(
                    start_date="-2y", end_date="today"
                )
            )

        self.stdout.write(self.style.SUCCESS(
            'Initial data for student organization created successfully.'
        ))

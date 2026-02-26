from django.core.management.base import BaseCommand
from studentorg.models import College, Program, Organization, Student, OrgMember
from datetime import date


class Command(BaseCommand):
    help = 'Create actual initial data for the application'

    def handle(self, *args, **kwargs):
        OrgMember.objects.all().delete()
        Student.objects.all().delete()
        Organization.objects.all().delete()
        Program.objects.all().delete()
        College.objects.all().delete()
        self.stdout.write(self.style.WARNING('Existing data cleared.'))

        self.create_colleges()
        self.create_programs()
        self.create_organizations()
        self.create_students()
        self.create_memberships()

    def create_colleges(self):
        colleges = [
            'College of Science',
            'College of Engineering',
            'College of Teacher Education',
            'College of Nursing and Health',
            'College of Arts and Humanities',
            'College of Business and Accountancy',
            'College of Hospitality and Tourism Management',
            'College of Architecture and Design',
        ]
        for college_name in colleges:
            College.objects.get_or_create(college_name=college_name)
        self.stdout.write(self.style.SUCCESS('Colleges created successfully.'))

    def create_programs(self):
        programs = [
            ('Bachelor of Science in Computer Science', 'College of Science'),
            ('Bachelor of Science in Information Technology', 'College of Science'),
            ('Bachelor of Science in Civil Engineering', 'College of Engineering'),
            ('Bachelor of Secondary Education Major in Mathematics', 'College of Teacher Education'),
            ('Bachelor of Elementary Education', 'College of Teacher Education'),
            ('Bachelor of Science in Nursing', 'College of Nursing and Health'),
            ('Bachelor of Arts in Political Science', 'College of Arts and Humanities'),
            ('Bachelor of Science in Accountancy', 'College of Business and Accountancy'),
            ('Bachelor of Science in Tourism Management', 'College of Hospitality and Tourism Management'),
            ('Bachelor of Science in Architecture', 'College of Architecture and Design'),
        ]
        for prog_name, college_name in programs:
            college = College.objects.filter(college_name=college_name).first()
            if college:
                Program.objects.get_or_create(prog_name=prog_name, college=college)
        self.stdout.write(self.style.SUCCESS('Programs created successfully.'))

    def create_organizations(self):
        orgs = [
            ('SITE', 'College of Science'),
            ('ACS', 'College of Science'),
        ]
        for org_name, college_name in orgs:
            college = College.objects.filter(college_name=college_name).first()
            Organization.objects.get_or_create(
                name=org_name,
                defaults={'college': college, 'description': ''}
            )
        self.stdout.write(self.style.SUCCESS('Organizations created successfully.'))

    def create_students(self):
        bsit = Program.objects.filter(prog_name='Bachelor of Science in Information Technology').first()
        bscs = Program.objects.filter(prog_name='Bachelor of Science in Computer Science').first()

        students = [
            ('2022-8-0400', 'Rivera', 'Vince Alshie', 'Viray', bsit),
            ('2019-8-0093', 'Estoya', 'Ethan Laureen', 'E', bscs),
        ]
        for student_id, lastname, firstname, middlename, program in students:
            if program:
                Student.objects.get_or_create(
                    student_id=student_id,
                    defaults={
                        'lastname': lastname,
                        'firstname': firstname,
                        'middlename': middlename,
                        'program': program
                    }
                )
        self.stdout.write(self.style.SUCCESS('Students created successfully.'))

    def create_memberships(self):
        memberships = [
            ('Rivera', 'SITE', date(2022, 8, 8)),
            ('Estoya', 'ACS', date(2019, 8, 12)),
        ]
        for lastname, org_name, date_joined in memberships:
            student = Student.objects.filter(lastname=lastname).first()
            org = Organization.objects.filter(name=org_name).first()
            if student and org:
                OrgMember.objects.get_or_create(
                    student=student,
                    organization=org,
                    defaults={'date_joined': date_joined}
                )
        self.stdout.write(self.style.SUCCESS('Org memberships created successfully.'))

from ..models import DepartmentModel
from ..config import session

def dept_seed():
    print('Department seeder running ...')
    try:
        departments = [
            DepartmentModel(dept_name='Cardiology'),
            DepartmentModel(dept_name='Dermatology'),
            DepartmentModel(dept_name='Radiology'),
            DepartmentModel(dept_name='Pediatrics'),
            DepartmentModel(dept_name='Orthopedics'),
            DepartmentModel(dept_name='Neurology'),
            DepartmentModel(dept_name='Endocrinology'),
            DepartmentModel(dept_name='Gastroenterology'),
            DepartmentModel(dept_name='Oncology'),
            DepartmentModel(dept_name='Psychiatry'),
            DepartmentModel(dept_name='Ophthalmology'),
            DepartmentModel(dept_name='Gynecology'),
            DepartmentModel(dept_name='Urology'),
            DepartmentModel(dept_name='Emergency Medicine'),
            DepartmentModel(dept_name='Pulmonology'),
            DepartmentModel(dept_name='Hematology'),
            DepartmentModel(dept_name='Rheumatology'),
            DepartmentModel(dept_name='Internal Medicine'),
            DepartmentModel(dept_name='Nephrology'),
            DepartmentModel(dept_name='Surgery')
        ]
        session.add_all(departments)
        session.commit()
    except Exception as e:
        session.rollback()
        print('Department Seeder fail, ', e)
        return
    print('Department seeder success ...')

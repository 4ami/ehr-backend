from .user_seed import seed_users
from .patient_seed import seed_patients
from .department_seed import dept_seed
if __name__ == '__main__':
    seed_users()
    seed_patients()
    dept_seed()

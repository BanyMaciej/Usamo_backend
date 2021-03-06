from enum import Enum


class AccountType(Enum):
    STANDARD = 1
    STAFF = 2
    EMPLOYER = 3


ACCOUNT_TYPE_CHOICES = [
    (AccountType.STANDARD.value, 'Standard'),
    (AccountType.STAFF.value, 'Staff'),
    (AccountType.EMPLOYER.value, 'Employer')
]


class StaffGroupType(Enum):
    STAFF_VERIFICATION = 'staff_verification'
    STAFF_CV = 'staff_cv'
    STAFF_JOBS = 'staff_jobs'
    STAFF_BLOG_CREATOR = 'staff_blog_creator'
    STAFF_BLOG_MODERATOR = 'staff_blog_moderator'

    @staticmethod
    def get_all_types():
        return [e.value for e in StaffGroupType]


STAFF_GROUP_CHOICES = [
    (StaffGroupType.STAFF_VERIFICATION.value, 'staff_verification'),
    (StaffGroupType.STAFF_CV.value, 'staff_cv'),
    (StaffGroupType.STAFF_JOBS.value, 'staff_jobs'),
    (StaffGroupType.STAFF_BLOG_CREATOR.value, 'staff_blog_creator'),
    (StaffGroupType.STAFF_BLOG_MODERATOR.value, 'staff_blog_moderator')
]

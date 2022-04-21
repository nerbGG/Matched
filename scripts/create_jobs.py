# import os, django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
# django.setup()

from Apply.models import Jobs
from Apply.constant_variables import jobs


def run():
    job_delete = Jobs.objects.all()
    job_delete.delete()
    for job in jobs:
        company = job["company"]
        position = job["position"]
        salary = job["salary"]
        interests = job["interests"]
        new_job = Jobs(company=company, position=position, expected_salary=salary, interests=interests)
        new_job.save()

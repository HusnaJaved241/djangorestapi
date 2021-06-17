from students.viewsets import StudentsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students',StudentsViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrieve
from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema
principal_teacher_resources = Blueprint('principal_teacher_resources',__name__)

@principal_teacher_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """List all teachers"""
    teachers_list = Teacher.get_teachers()
    teachers_list_dump = TeacherSchema().dump(teachers_list, many=True)
    return APIResponse.respond(data=teachers_list_dump)


import flask
from Project.toolbox import config_page

# @config_page(template_name= 'after_test_student.html')
# @config_page(template_name= 'tests.html')
@config_page(template_name= 'after_test_teacher.html')
def render_tests():
    return {}
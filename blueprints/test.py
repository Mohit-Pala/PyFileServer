from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas.test import TestSchema

blp = Blueprint("Test", __name__, url_prefix="/test", description="Test")


@blp.route("/pussy")
class Test(MethodView):
    @blp.arguments(TestSchema)
    @blp.response(201, TestSchema)
    def post(self, test_data):
        print(test_data)
        return test_data

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas.sound import SoundSchema
from pandasFileSave import get_all_data

blp = Blueprint("Sound", __name__, url_prefix="/sound", description="Sounds")

@blp.route("/getall")
class GetAllSounds(MethodView):
    @blp.response(200, SoundSchema(many=True))
    def get(self):
        sounds = get_all_data()
        return sounds.to_dict('records')
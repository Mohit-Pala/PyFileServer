from marshmallow import Schema, fields

class TestSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
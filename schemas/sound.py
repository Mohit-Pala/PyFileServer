from marshmallow import Schema, fields

class SoundSchema(Schema):
    Id = fields.Int(required=True)
    Name = fields.Str(required=True)
    Description = fields.Str()
    FilePath = fields.Str(required=True)
    UploadedBy = fields.Str(required=True)
    Status = fields.Str(required=True)
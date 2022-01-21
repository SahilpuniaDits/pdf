from models.db import db


class pdf(db.Model):
    _tablename_ = "file"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    file = db.Column(db.models.FileField(("file"), upload_to=None, max_length=100))

    def __init__(self,name,file):
        self.name = name
        self.file = file


    def __repr__(self):
        record = {"name": self.name,"file":self.name}
        return record

    def serialize(self):
        return {"name": self.name,"file":self.name}
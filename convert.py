from flask import Flask,render_template,make_response
from flask_restful import Api, Resource,reqparse

import pdfkit
 
app = Flask(__name__)

class index(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('html',type =pdfkit.from_string)
        args = parse.parse_args()
        pdf = args['html']
        pdf.save()
        response = make_response(pdf)
        return response
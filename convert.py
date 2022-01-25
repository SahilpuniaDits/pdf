from os import name
from flask import Flask,render_template,make_response,request,jsonify
from flask_restful import Api, Resource,reqparse

import pdfkit
# from models.pdf import pdf
 
app = Flask(__name__)

class index(Resource):
    def post(self,file):

        html = request.json.get('html')
        
        config = pdfkit.configuration(
            wkhtmltopdf="C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe")
        pdfkit.from_string(html, file+".pdf",configuration=config)
        return jsonify({'status': 'Pdf successfully generated',
                        'click on this link for view': f"C:\Flask\pdf/{file}.pdf"})
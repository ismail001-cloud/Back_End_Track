from flask import request, jsonify
from flask_restful import Resource, Api
from flask import Blueprint
from ...db.models.sections import Section
from ...db.core import db

#create blueprint for sections routes
sections_bp = Blueprint("sections", __name__)
api = Api(sections_bp)

#to create, getSingle, update and delete
class SectionListResource(Resource):
    def get (self, section_id):
        section = Section.query.get(section_id)
        if not section:
            return {"message": "user not found"}, 404
        return jsonify(section.serialize())

    def put(self, section_id):
        """Update an existing section"""
        data = request.get_json()
        section = Section.query.get(section_id)
        if not section:
            return {"message": "Section not found"}, 404

        if "name" in data:
            if Section.query.filter_by(name=data["name"]).first():
                return {"message": "Section name already exists"}, 400
            section.name = data["name"]

        db.session.commit()
        return jsonify({"message": "Section updated successfully", "section": section.serialize()})

    def delete(self, section_id):
        """ to delete a section"""
        section = Section.query.get(section_id)
        if not section:
            return {"message": "Section not found"}, 404

        db.session.delete(section)
        db.session.commit()
        return {"message": "Section deleted successfully"}, 200


#to get all
class SectionResource(Resource):
    """handle collection of sections"""

    def get(self):
        """list all sections"""
        sections = Section.query.all()
        return {"sections": [section.serialize() for section in sections]}, 200

    def post(self):
        """Create a new section"""
        data = request.get_json()
        if not data or "name" not in data:
            return {"message": "Missing name in request"}, 400

        if Section.query.filter_by(name=data["name"]).first():
            return {"message": "Section name already exists"}, 400

        new_section = Section(name=data["name"])
        db.session.add(new_section)
        db.session.commit()

        return jsonify({"message": "Section created successfully", "section": new_section.serialize()}), 201


#register routes
api.add_resource(SectionResource, '/sections')
api.add_resource(SectionListResource, '/sections/<int:section_id>')

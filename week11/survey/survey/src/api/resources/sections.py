from flask import request, jsonify
from flask_restful import Resource, Api
from flask import Blueprint
from src.db.models.sections import Section
from src.db.core import db

# Create blueprint for sections routes
sections_bp = Blueprint("sections", __name__)
api = Api(sections_bp)

class SectionList(Resource):
    def get(self, section_id):
        """Retrieve a specific section by ID"""
        section = Section.query.get(section_id)
        if not section:
            return {"message": "Section not found"}, 404
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
        """Delete a section"""
        section = Section.query.get(section_id)
        if not section:
            return {"message": "Section not found"}, 404

        db.session.delete(section)
        db.session.commit()
        return {"message": "Section deleted successfully"}, 200


class SectionResource(Resource):
    def get(self):
        """Retrieve all sections"""
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
            


# Register routes
api.add_resource(SectionList, "/sections/<int:section_id>")
api.add_resource(SectionResource, "/sections")  
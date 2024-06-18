import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import db
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from resources.schemas import StoreSchema


blp = Blueprint("Stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("DELETE not yet working")


@blp.route("/store")
class StoreList(MethodView):
    @blp.response(201, StoreSchema(many=True))
    def get(self):
        """
        Retrieve a List of All Stores
        """
        return stores.values()

    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        """
        Create a New Store
        """
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="There is already a store with this name")
        except SQLAlchemyError:
            abort(500, message="Error inserting the store")


        return store, 201

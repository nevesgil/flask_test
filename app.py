# from flask_openapi3 import Info, OpenAPI
from flask import redirect
from flask import Flask
from flask_smorest import Api
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "PUCAPP REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


@app.get("/")
def home():
    """
    SIMPLE REDIRECT FOR ACCESSING THE SWAGGER
    """
    return redirect("/docs")


api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


# app = Flask(__name__)

# info = Info(title="my first API test PUCAPP 2222", version="1.0.0")
# app = OpenAPI(__name__, info=info)

# @app.get("/")
# def home():
#     """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
#     return redirect("/openapi")


# @app.get("/store")
# def get_stores():
#     """
#     GETS ALL THE STORES
#     """
#     return {"stores": list(stores.values())}


# @app.get("/item")
# def get_all_items():
#     """
#     GETS ALL ITEMS
#     """
#     return {"items": list(items.values())}


# @app.post("/store")
# def create_store():
#     """
#     CREATES A STORE
#     """
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(
#             400, message="Bad request. Enrure 'name' is included in the JSON payload"
#         )
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message="Store already exists.")
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201


# @app.post("/item")
# def create_item():
#     """
#     CREATES AN ITEM IN A STORE
#     """
#     item_data = request.get_json()
#     if (
#         "price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload",
#         )
#     for item in items.values():
#         if (
#             item_data["name"] == item["name"]
#             and item_data["store_id"] == item["store_id"]
#         ):
#             abort(400, message=f"Item already exists.")
#     # if item_data["store_id"] not in stores:
#     #     return abort(404, message="Store not found")

#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item
#     return item, 201


# @app.route("/store/<store_id>", methods=["GET"])
# def get_store(store_id):
#     """
#     GETS STORE FROM ID
#     """
#     try:
#         return stores[store_id]
#     except KeyError:
#         return abort(404, message="Store not found")


# @app.route("/item/<item_id>", methods=['GET'])
# def get_item(item_id):
#     """
#     GETS ITEM FROM ITEM_ID
#     """
#     try:
#         return items[item_id]
#     except KeyError:
#         return abort(404, message="Item not found")

# @app.route("/item/<string:item_id>", methods=['DELETE'])
# def delete_item(item_id):
#     """
#     DELETE ITEM FROM ITEM_ID
#     """
#     try:
#         del items[item_id]
#         return {"message" : "Item deleted"}
#     except KeyError:
#         return abort(404, message="Item not found")


# @app.route("/store/<string:store_id>", methods=['DELETE'])
# def delete_store(store_id):
#     """
#     DELETE STORE FROM STORE_ID
#     """
#     try:
#         del stores[store_id]
#         return {"message" : "store deleted"}
#     except KeyError:
#         return abort(404, message="store not found")


# @app.route("/item/<string:item_id>", methods=['PUT'])
# def update_item(item_id):
#     item_data = request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400, message="Bad request Ensure name and price are included in the JSON payload.")
#     try:
#         item = items[item_id]
#         item |= item_data
#         return item
#     except:
#         abort(404, message="Item not found")

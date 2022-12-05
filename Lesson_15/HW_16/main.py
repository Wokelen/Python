import json
import data
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(100))
    description = db.Column(db.Text(100))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    address = db.Column(db.Text(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }


def fill_db():
    db.drop_all()
    db.create_all()
    for user_data in data.users:
        new_user = User(
            id=user_data["id"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            age=user_data["age"],
            email=user_data["email"],
            role=user_data["role"],
            phone=user_data["phone"]
        )
        db.session.add(new_user)
        db.session.commit()

    for order_data in data.orders:
        new_order = Order(
            id=order_data["id"],
            name=order_data["name"],
            description=order_data["description"],
            start_date=order_data["start_date"],
            end_date=order_data["end_date"],
            address=order_data["address"],
            price=order_data["price"],
            customer_id=order_data["customer_id"],
            executor_id=order_data["executor_id"]
        )
        db.session.add(new_order)
        db.session.commit()

    for offer_data in data.offers:
        new_offer = Offer(
            id=offer_data["id"],
            order_id=offer_data["order_id"],
            executor_id=offer_data["executor_id"]
        )
        db.session.add(new_offer)
        db.session.commit()


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        user_list = []
        for row in User.query.all():
            user_list.append(row.to_dict())
        return json.dumps(user_list)
    if request.method == "POST":
        user_data = json.loads(request.data)
        new_user = User(
            id=user_data["id"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            age=user_data["age"],
            email=user_data["email"],
            role=user_data["role"],
            phone=user_data["phone"]
        )
        db.session.add(new_user)
        db.session.commit()
        return "User is created"


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user(uid: int):
    if request.method == "GET":
        return json.dumps(User.query.get(uid).to_dict())
    if request.method == "PUT":
        user_data = json.loads(request.data)
        u = User.query.get(uid)
        u.first_name = user_data["first_name"],
        u.last_name = user_data["last_name"],
        u.age = user_data["age"],
        u.email = user_data["email"],
        u.role = user_data["role"],
        u.phone = user_data["phone"]
        db.session.add(u)
        db.session.commit()
        return "User is updated"
    if request.method == "DELETE":
        u = User.query.get(uid)
        db.session.delete(u)
        db.session.commit()
        return "User is deleted"


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        order_list = []
        for row in Order.query.all():
            order_list.append(row.to_dict())
        return json.dumps(order_list)
    if request.method == "POST":
        order_data = json.loads(request.data)
        new_order = Order(
            id=order["id"],
            name=order["name"],
            description=order_data["description"],
            start_date=order_data["start_date"],
            end_date=order_data["end_date"],
            address=order_data["address"],
            price=order_data["price"],
            customer_id=order_data["customer_id"],
            executor_id=order_data["executor_id"]
        )
        db.session.add(new_order)
        db.session.commit()
        return "Order is created"


@app.route("/orders/<int:uid>", methods=["GET", "PUT", "DELETE"])
def order(uid: int):
    if request.method == "GET":
        return json.dumps(Order.query.get(uid).to_dict())
    if request.method == "PUT":
        order_data = json.loads(request.data)
        o = Order.query.get(uid)
        o.name = order_data["name"],
        o.description = order_data["description"],
        o.start_date = order_data["start_date"],
        o.end_date = order_data["end_date"],
        o.address = order_data["address"],
        o.price = order_data["price"],
        o.customer_id = order_data["customer_id"],
        o.executor_id = order_data["executor_id"]
        db.session.add(o)
        db.session.commit()
        return "Order is updated"
    if request.method == "DELETE":
        o = Order.query.get(uid)
        db.session.delete(o)
        db.session.commit()
        return "Order is deleted"


@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        offer_list = []
        for row in Offer.query.all():
            offer_list.append(row.to_dict())
        return json.dumps(offer_list)
    if request.method == "POST":
        offer_data = json.loads(request.data)
        new_offer = Offer(
            id=offer["id"],
            order_id=offer_data["order_id"],
            execute_id=offer_data["execute_id"]
        )
        db.session.add(new_offer)
        db.session.commit()
        return "Offer is created"


@app.route("/offers/<int:uid>", methods=["GET", "PUT", "DELETE"])
def offer(uid: int):
    if request.method == "GET":
        return json.dumps(Offer.query.get(uid).to_dict())
    if request.method == "PUT":
        offer_data = json.loads(request.data)
        o = Offer.query.get(uid)
        o.order_id = offer_data["order_id"],
        o.execute_id = offer_data["execute_id"]
        db.session.add(o)
        db.session.commit()
        return "Offer is updated"
    if request.method == "DELETE":
        o = Offer.query.get(uid)
        db.session.delete(o)
        db.session.commit()
        return "Offer is deleted"


if __name__ == '__main__':
    fill_db()
    app.run(debug=True)

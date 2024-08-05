from litestar import Litestar

from app.controllers import UserController, TravelController, AccommodationController, TransportController, ActivityController, ExpenseController, CityController
from app.database import db_plugin


app = Litestar(
    [UserController, TravelController, AccommodationController, TransportController, ActivityController, ExpenseController, CityController],
    debug=True,
    plugins=[db_plugin],
)

from datetime import datetime
from typing import Sequence

from advanced_alchemy.exceptions import NotFoundError
from advanced_alchemy.filters import CollectionFilter
from litestar import Controller, delete, get, patch, post
from litestar.dto import DTOData
from litestar.exceptions import HTTPException, NotFoundException
from sqlalchemy import select
from sqlalchemy.sql.functions import user

from app.dtos import (
    UserReadFullDTO,
    UserCreateDTO,
    UserReadDTO,
    UserUpdateDTO,
    TravelReadFullDTO,
    TravelCreateDTO,
    TravelReadDTO,
    TravelUpdateDTO,
    AccommodationReadFullDTO,
    AccommodationCreateDTO,
    AccommodationReadDTO,
    AccommodationUpdateDTO,
    TransportsReadFullDTO,
    TransportsCreateDTO,
    TransportsReadDTO,
    TransportsUpdateDTO,
    ActivityReadFullDTO,
    ActivityCreateDTO,
    ActivityReadDTO,
    ActivityUpdateDTO,
    ExpenseReadFullDTO,
    ExpenseCreateDTO,
    ExpenseReadDTO,
    ExpenseUpdateDTO,
    CityReadFullDTO,
    CityCreateDTO,
    CityReadDTO,
    CityUpdateDTO,



    TravelReadFullDTO,
    AccommodationReadFullDTO,
    TransportReadFullDTO,
    ActivityReadFullDTO,
    ExpenseReadFullDTO,
    CityReadFullDTO,

)
from app.models import User, Travel, Accommodation, Transport, Activity, Expense, City
from app.repositories import (
    UserRepository,
    TravelRepository,
    AccommodationRepository,
    TransportRepository,
    ActivityRepository,
    ExpenseRepository,
    CityRepository,
    provide_user_repo,
    provide_travel_repo,
    provide_accommodation_repo,
    provide_transport_repo,
    provide_activity_repo,
    provide_expense_repo,
    provide_city_repo,
)

class UserController(Controller):
    path = "/users"
    tags = ["users"]
    return_dto = UserReadFullDTO
    dependencies = {"user_repo": provide_user_repo}


    @get("/", return_dto=UserReadDTO)
    async def list_users(self, user_repo: UserRepository) -> list[User]:
        return user_repo.list()
    
    @get("/{user_id:int}")
    async def get_user(self, user_repo: UserRepository, user_id: int) -> User:
        try:
            return user_repo.get(user_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e
        
    @post("/", dto=UserCreateDTO)
    async def add_user(self, user_repo: UserRepository, data: User) -> User:
        return user_repo.add(data)

    @patch("/{user_id:int}", dto=UserUpdateDTO)
    async def update_user(
        self, user_repo: UserRepository, user_id: int, data: DTOData[User]
    ) -> User:
        try:
            user, _ = user_repo.get_and_update(
                id=user_id, **data.as_builtins(), match_fields=["id"]
            )
            return user
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e

    @delete("/{user_id:int}")
    async def delete_user(self, user_repo: UserRepository, user_id: int) -> None:
        try:
            user_repo.delete(user_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Usuario {user_id} no encontrado") from e


class TravelController(Controller):
    path = "/travels"
    tags = ["travels"]
    return_dto = TravelReadFullDTO
    dependencies = {"travel_repo": provide_travel_repo}

    @get("/", return_dto=TravelReadDTO)
    async def list_travels(self, travel_repo: TravelRepository) -> list[Travel]:
        return travel_repo.list()
    
    @get("/{travel_id:int}")
    async def get_travel(self, travel_repo: TravelRepository, travel_id: int) -> Travel:
        try:
            return travel_repo.get(travel_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e
        
    @post("/", dto=TravelCreateDTO)
    async def add_travel(self, travel_repo: TravelRepository, data: Travel) -> Travel:
        return travel_repo.add(data)

    @patch("/{travel_id:int}", dto=TravelUpdateDTO)
    async def update_travel(
        self, travel_repo: TravelRepository, travel_id: int, data: DTOData[Travel]
    ) -> Travel:
        try:
            travel, _ = travel_repo.get_and_update(
                id=travel_id, **data.as_builtins(), match_fields=["id"]
            )
            return travel
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

    @delete("/{travel_id:int}")
    async def delete_travel(self, travel_repo: TravelRepository, travel_id: int) -> None:
        try:
            travel_repo.delete(travel_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Viaje {travel_id} no encontrado") from e

class AccommodationController(Controller):
    path = "/accommodations"
    tags = ["accommodations"]
    return_dto = AccommodationReadFullDTO
    dependencies = {"accommodation_repo": provide_accommodation_repo}

    @get("/", return_dto=AccommodationReadDTO)
    async def list_accommodations(self, accommodation_repo: AccommodationRepository) -> list[Accommodation]:
        return accommodation_repo.list()
    
    @get("/{accommodation_id:int}")
    async def get_accommodation(self, accommodation_repo: AccommodationRepository, accommodation_id: int) -> Accommodation:
        try:
            return accommodation_repo.get(accommodation_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e
        
    @post("/", dto=AccommodationCreateDTO)
    async def add_accommodation(self, accommodation_repo: AccommodationRepository, data: Accommodation) -> Accommodation:
        return accommodation_repo.add(data)

    @patch("/{accommodation_id:int}", dto=AccommodationUpdateDTO)
    async def update_accommodation(
        self, accommodation_repo: AccommodationRepository, accommodation_id: int, data: DTOData[Accommodation]
    ) -> Accommodation:
        try:
            accommodation, _ = accommodation_repo.get_and_update(
                id=accommodation_id, **data.as_builtins(), match_fields=["id"]
            )
            return accommodation
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e

    @delete("/{accommodation_id:int}")
    async def delete_accommodation(self, accommodation_repo: AccommodationRepository, accommodation_id: int) -> None:
        try:
            accommodation_repo.delete(accommodation_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {accommodation_id} no encontrado") from e


class TransportController(Controller):
    path = "/transports"
    tags = ["transports"]
    return_dto = TransportsReadFullDTO
    dependencies = {"transport_repo": provide_transport_repo}

    @get("/", return_dto=TransportsReadDTO)
    async def list_transports(self, transports_repo: TransportRepository) -> list[Transport]:
        return transports_repo.list()
    
    @get("/{transports_id:int}")
    async def get_transports(self, transports_repo: TransportRepository, transports_id: int) -> Transport:
        try:
            return transports_repo.get(transports_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transports_id} no encontrado") from e
        
    @post("/", dto=TransportsCreateDTO)
    async def add_transports(self, transports_repo: TransportRepository, data: Transport) -> Transport:
        return transports_repo.add(data)

    @patch("/{transports_id:int}", dto=TransportsUpdateDTO)
    async def update_transports(
        self, transports_repo: TransportRepository, transports_id: int, data: DTOData[Transport]
    ) -> Transport:
        try:
            transports, _ = transports_repo.get_and_update(
                id=transports_id, **data.as_builtins(), match_fields=["id"]
            )
            return transports
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transports_id} no encontrado") from e

    @delete("/{transports_id:int}")
    async def delete_transports(self, transports_repo: TransportRepository, transports_id: int) -> None:
        try:
            transports_repo.delete(transports_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Transporte {transports_id} no encontrado") from e

class ActivityController(Controller):
    path = "/activities"
    tags = ["activities"]
    return_dto = ActivityReadFullDTO
    dependencies = {"activity_repo": provide_activity_repo}

    @get("/", return_dto=ActivityReadDTO)
    async def list_activites(self, activity_repo: ActivityRepository) -> list[Activity]:
        return activity_repo.list()
    
    @get("/{activity_id:int}")
    async def get_activity(self, activity_repo: ActivityRepository, activity_id: int) -> Activity:
        try:
            return activity_repo.get(activity_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {activity_id} no encontrado") from e
        
    @post("/", dto=ActivityCreateDTO)
    async def add_activity(self, activity_repo: ActivityRepository, data: Activity) -> Activity:
        return activity_repo.add(data)

    @patch("/{activity_id:int}", dto=ActivityUpdateDTO)
    async def update_activity(
        self, activity_repo: ActivityRepository, activity_id: int, data: DTOData[Activity]
    ) -> Activity:
        try:
            activity, _ = activity_repo.get_and_update(
                id=activity_id, **data.as_builtins(), match_fields=["id"]
            )
            return activity
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {activity_id} no encontrado") from e

    @delete("/{activity_id:int}")
    async def delete_activity(self, activity_repo: ActivityRepository, activity_id: int) -> None:
        try:
            activity_repo.delete(activity_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Alojamiento {activity_id} no encontrado") from e

class ExpenseController(Controller):
    path = "/expenses"
    tags = ["expenses"]
    return_dto = ExpenseReadFullDTO
    dependencies = {"expense_repo": provide_expense_repo}

    @get("/", return_dto=ExpenseReadDTO)
    async def list_expenses(self, expense_repo: ExpenseRepository) -> list[Expense]:
        return expense_repo.list()
    
    @get("/{expense_id:int}")
    async def get_expense(self, expense_repo: ExpenseRepository, expense_id: int) -> Expense:
        try:
            return expense_repo.get(expense_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e
        
    @post("/", dto=ExpenseCreateDTO)
    async def add_expense(self, expense_repo: ExpenseRepository, data: Expense) -> Expense:
        return expense_repo.add(data)

    @patch("/{expense_id:int}", dto=ExpenseUpdateDTO)
    async def update_expense(
        self, expense_repo: ExpenseRepository, expense_id: int, data: DTOData[Expense]
    ) -> Expense:
        try:
            expense, _ = expense_repo.get_and_update(
                id=expense_id, **data.as_builtins(), match_fields=["id"]
            )
            return expense
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e

    @delete("/{expense_id:int}")
    async def delete_expense(self, expense_repo: ExpenseRepository, expense_id: int) -> None:
        try:
            expense_repo.delete(expense_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Gasto {expense_id} no encontrado") from e

class CityController(Controller):
    path = "/cities"
    tags = ["cities"]
    return_dto = CityReadFullDTO
    dependencies = {"city_repo": provide_city_repo}

    @get("/", return_dto=CityReadDTO)
    async def list_cities(self, city_repo: CityRepository) -> list[City]:
        return city_repo.list()
    
    @get("/{city_id:int}")
    async def get_city(self, city_repo: CityRepository, city_id: int) -> City:
        try:
            return city_repo.get(city_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Ciudad {city_id} no encontrado") from e
        
    @post("/", dto=CityCreateDTO)
    async def add_city(self, city_repo: CityRepository, data: City) -> City:
        return city_repo.add(data)

    @patch("/{city_id:int}", dto=CityUpdateDTO)
    async def update_city(
        self, city_repo: CityRepository, city_id: int, data: DTOData[City]
    ) -> City:
        try:
            city, _ = city_repo.get_and_update(
                id=city_id, **data.as_builtins(), match_fields=["id"]
            )
            return city
        except NotFoundError as e:
            raise NotFoundException(detail=f"Ciudad {city_id} no encontrado") from e

    @delete("/{city_id:int}")
    async def delete_city(self, city_repo: CityRepository, city_id: int) -> None:
        try:
            city_repo.delete(city_id)
        except NotFoundError as e:
            raise NotFoundException(detail=f"Ciudad {city_id} no encontrado") from e

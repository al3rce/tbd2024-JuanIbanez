from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import User, Travel, Accommodation, Transport, Activity, Expense, City


class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"grupo_users_travels","grupo_expenses","enabled"})


class UserReadFullDTO(SQLAlchemyDTO[User]):
    pass

class UserCreateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_users_travels","grupo_expenses", "enabled"})

class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_users_travels", "grupo_expenses", "enabled"}, partial=True)


class TravelReadFullDTO(SQLAlchemyDTO[Travel]):
    pass
class TravelCreateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id","grupo_accommodations","grupo_transports","grupo_expenses", "grupo_users_travels", "enabled"})
class TravelReadDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"grupo_accommodations","grupo_transports","grupo_expenses", "grupo_users_travels", "enabled"})
class TravelUpdateDTO(SQLAlchemyDTO[Travel]):
    config = SQLAlchemyDTOConfig(exclude={"id","grupo_accommodations","grupo_transports","grupo_expenses", "grupo_users_travels", "enabled"}, partial=True)
    

class AccommodationReadFullDTO(SQLAlchemyDTO[Accommodation]):
    pass
class AccommodationCreateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_cities","grupo_travels", "enabled"})
class AccommodationReadDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"grupo_cities","grupo_travels", "enabled"})
class AccommodationUpdateDTO(SQLAlchemyDTO[Accommodation]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_cities","grupo_travels", "enabled"}, partial=True)
    

class TransportReadFullDTO(SQLAlchemyDTO[Transport]):
    pass
class TransportsCreateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_cities","grupo_cities2","grupo_travels", "enabled"})
class TransportsReadDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"grupo_cities","grupo_cities2","grupo_travels", "enabled"})
class TransportsUpdateDTO(SQLAlchemyDTO[Transport]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_cities","grupo_cities2","grupo_travels", "enabled"}, partial=True)
    

class ActivityReadFullDTO(SQLAlchemyDTO[Activity]):
    pass
class ActivityCreateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_cities","grupo_travels", "enabled"})
class ActivityReadDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"grupo_cities","grupo_travels", "enabled"})
class ActivityUpdateDTO(SQLAlchemyDTO[Activity]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_cities","grupo_travels", "enabled"}, partial=True)

    
class ExpenseReadFullDTO(SQLAlchemyDTO[Expense]):
    pass
class ExpenseCreateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_users","grupo_travels", "enabled"})
class ExpenseReadDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"grupo_users","grupo_travels", "enabled"})
class ExpenseUpdateDTO(SQLAlchemyDTO[Expense]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_users","grupo_travels", "enabled"}, partial=True)

    
class CityReadFullDTO(SQLAlchemyDTO[City]):
    pass
class CityCreateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_accommodations","grupo_transports", "grupo_transports2","grupo_activities", "enabled"})
class CityReadDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"grupo_accommodations","grupo_transports","grupo_transports2", "grupo_activities", "enabled"})
class CityUpdateDTO(SQLAlchemyDTO[City]):
    config = SQLAlchemyDTOConfig(exclude={"id", "grupo_accommodations","grupo_transports","grupo_transports2", "grupo_activities", "enabled"})
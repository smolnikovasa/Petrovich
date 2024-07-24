from values.users_dto import UserDTO


BASE_URL = "https://petstore.swagger.io/v2/user"
LOGIN = "api_key"
PASSWORD = "special-key"

METHOD_GET = 'GET'
METHOD_POST = 'POST'
METHOD_PUT = 'PUT'
METHOD_DELETE = 'DELETE'


def dict_user(user_dto: UserDTO):
    return {
        "id": 0,
        "username": user_dto.username,
        "firstName": user_dto.first_name,
        "lastName": user_dto.last_name,
        "email": user_dto.user_email,
        "password": user_dto.password,
        "phone": user_dto.user_phone,
        "userStatus": 0,
    }

from clients.courses.courses_client import get_courses_client, CreateCourseRequestDictSchema
from clients.files.files_client import get_files_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
# Вместо CreateUserRequestDict импортируем CreateUserRequestSchema
from clients.users.users_schema import CreateUserRequestSchema
# Вместо CreateFileRequestDict импортируем CreateFileRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from tools.fakers import fake

public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиенты
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Загружаем файл
# Вместо CreateFileRequestDict используем CreateFileRequestSchema
create_file_request = CreateFileRequestSchema(
    filename="hold.jpg",
    directory="courses",
    upload_file="/Users/uladzimirrudnik/PycharmProjects/Python_API/testdata/files/hold.jpg"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestDictSchema(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,  # Используем атрибуты место ключей
    createdByUserId=create_user_response.user.id  # Используем атрибуты место ключей
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)
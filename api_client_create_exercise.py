from clients.courses.courses_client import get_courses_client, CreateCourseRequestSchema
from clients.exercises.exercises_client import CreateExerciseRequestSchema, get_exercises_client
from clients.files.files_client import get_files_client
# Вместо CreateFileRequestDict импортируем CreateFileRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
# Вместо CreateUserRequestDict импортируем CreateUserRequestSchema
from clients.users.users_schema import CreateUserRequestSchema

public_users_client = get_public_users_client()

# Больше нет необходимости передавать значения, они будут генерировать автоматически
# Создаем пользователя
create_user_request = CreateUserRequestSchema()
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
# Автоматическая генерация данных, кроме необходимых параметров
create_file_request = CreateFileRequestSchema(upload_file="/Users/uladzimirrudnik/PycharmProjects/Python_API/testdata/files/hold.jpg")
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Используем сгенерированные значения для создания курса
# Создаем курс
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,  # Используем атрибуты место ключей
    created_by_user_id=create_user_response.user.id  # Используем атрибуты место ключей
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем exercise
create_exercise_request = CreateExerciseRequestSchema()

exercise_client = get_exercises_client(authentication_user)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)



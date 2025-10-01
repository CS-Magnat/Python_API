pytest_plugins = (
    "fixtures.users",
    "fixtures.authentication",
    "fixtures.files",  # Добавляем фикстуры для работы с файлами
    "fixtures.courses",  # Добавляем фикстуры для работы с курсами
    "fixtures.exercises",  # Добавляем фикстуры для работы с exercises
)
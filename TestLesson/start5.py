variable = 5

# ------ Проверка если "variable" равняется True или False ------

# Это условие Выполнится при variable = любое что угодно КРОМЕ когда оно False
if variable:
    pass

# Это условие Выполнится при variable = только False
if not variable:
    pass


# ------ Проверка если "variable" равняется None (пустое) или (не пустое, в нем int, str, list) ------

# Это условие Выполнится при variable = только None
if variable is None:
    pass

# Это условие Выполнится при variable = любое что угодно КРОМЕ когда оно None
if variable is not None:
    pass

# ------ Обычные IF ------

if variable >= 5:
    pass

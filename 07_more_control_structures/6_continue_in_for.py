# La sentencia (statement) `continue` se usa para saltar la iteracion actual del bucle (loop) y pasar a la siguiente.
# Cuando se encuentra `continue`, el codigo restante en la iteracion actual se salta.
# Sintaxis:
#     for <variable> in <iterable>:
#         if <condicion>:
#             continue
#         <codigo a ejecutar>

# Ejemplo 1: Saltar productos agotados en una lista
products = [
    "laptop",
    "tablet (agotado)",
    "smartphone",
    "monitor (agotado)"]
for product in products:
    if "agotado" in product:
        continue  # Saltar productos agotados
    print('Producto disponible:', product)


###############################################


# Ejemplo 2: Filtrar direcciones de correo electronico invalidas
emails = ["user1@example.com", "invalid@", "user2@example.com", "@wrong.com"]
valid_emails = []
for email in emails:
    if "@" not in email or "." not in email:
        continue  # Saltar correos invalidos
    valid_emails.append(email)
print("Correos validos:", valid_emails)

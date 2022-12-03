import calendar
 
fecha = calendar.TextCalendar(
    calendar.SUNDAY)

print(fecha.prmonth (2022, 12))

#segunda forma hecha para imprimir todo el año

#Instancia de TextCalendar
anio_entero = calendar.TextCalendar()

#Elegimos el formato del año
calendario_2023 = anio_entero.formatyear(2023)

#Mostramos el resultado
print(calendario_2023)

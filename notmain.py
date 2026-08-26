from vehiculo import Vehiculo


# 1. crear 3 vehiculos con datos inventados
vehiculo1  = Vehiculo("AB1234", 2018)
vehiculo2  = Vehiculo("CD5678", 2020)
vehiculo3  = Vehiculo("EF9012", 2023)

# 2. ingresarlos al taller
print(vehiculo1.ingresar())
print(vehiculo2.ingresar())
print(vehiculo3.ingresar())

# 3. imprimir su tarifa por hora
print(f"tarifa por hora del primer vehiculo: $(vehiculo1.tarifa_hora())")
print(f"tarifa por hora del segundo vehiculo: $(vehiculo2.tarifa_hora())")
print(f"tarifa por hora del tercer vehiculo: $(vehiculo3.tarifa_hora())")
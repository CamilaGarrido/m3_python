recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]]

"""
1) Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.

"""
recordatorios.insert(1, ['2021-02-02', '06:00', 'Empezar el Año'])

"""
2)  Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. 
Editar de tal manera que sea el 16 de Julio
"""
for i, evento in enumerate(recordatorios):
    if evento[0] == '2021-07-15':
        recordatorios[i][0] = '2021-07-16'

"""
3) Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día 
del trabajo.
"""
recordatorios = [evento for evento in recordatorios if "trabajar" not in evento[2].lower()]

"""
4) Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a 
las 22 hrs.
"""
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

recordatorios.sort()# Ordenar la lista por fecha y hora.
[print(evento) for evento in recordatorios]# Imprimir lista. 
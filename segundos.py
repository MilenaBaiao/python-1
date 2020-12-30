NúmerodeSegundos = input("Por favor, entre com o númerod e segundos que deseja converter: ")

Dias = int(NúmerodeSegundos) / 86400)
Horas = int(NúmerodeSegundos) / 3600)
Minutos = int(NúmerodeSegundos) /60)
Segundos = int(NúmerodeSegundos) % 60)

print(Dias, "dias, " +  Horas, "horas, " + Minutos, "minutos, " + Segundos, "e segundos.")

segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
totalsegundos = int(segundos)


horas = totalsegundos // 3600
dias = horas//86400

segundosrestantes = totalsegundos % 3600
minutos = segundosrestantes // 60
segs_restantes_final = segundosrestantes % 60

if (horas >= 24): 

	dias = int(horas / 24)
	horas = int(horas % 24)


print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_final,"segundos.")

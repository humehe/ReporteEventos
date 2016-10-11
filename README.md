# ReporteEventos
Este script un archivo ascii que contiene los totales de eventos por alumno necesario para generar el informe semanal del curso,
sin necesidad de copiar uno a uno los valores individuales por alumno.

Para ello es necesario generar tres informe independientes de eventos, es decir uno para chat, otro para foro y uno más para tareas, con 
totales por usuario. También es necesario tener el listado del número total de participantes por grupo en un archivo individual. 
Todos los archivos deben estar en formato .csv y se debe tener cuidado al momento de descargar los informes de la plataforma, pues en 
ocasiones la última linea está incompleta, faltando el total de eventos e incluso parte del nombre del último maestro, además de comentar 
el encabezado de los archivos (añadir #).

Sólo hay que indicar la localización en su computadora de los archivos, modificando la linea: 

home = expanduser("~") + '/Dropbox/Curso-SEP-16/Reportes/' + user

Y luego cada uno de los nombres de los archivos, 
1.- Listado de participantes
2.- Foros
3.- Tareas
4.- Chat

en las siguientes lineas:

1.- MSTR_TBL    = home +  'Informe-Reporte_Inicial_Visitas-PLA_241-MASTER.dat'#'Informe-Reporte_Inicial_Visitas-EXP_241-MASTER.csv'
2.- TBL_EVN_FRM = home +  'Informe-Reporte_Incial_Evento_Foro-PLA_241.csv'#'Informe-Reporte_Inicial_Eventos_Foros-EXP_241.csv'
3.- TBL_EVN_HWK = home +  'Informe-Reporte_Incial_Evento_Tareas-PLA_241.csv'#'Informe-Reporte_Inicial_Eventos_Tareas-EXP_241.csv'
4.- TBL_EVN_CHT = home +  'Informe-Reporte_Incial_Evento_Chat-PLA_241.csv'#'Informe-Reporte_Inicial_Eventos_Chat-EXP_241.csv'

y finalmente como quieren que se llame el archivo de salida:

op_tbl_B    = home  + 'Informe-Reporte_Eventos-PLA_241.dat'

El script genera copias de los archivos de entrada y el informe de eventos por evento por alumno, todos en formato ascii.
Estos archivos pueden abrirse para copiar y pegar directamente en una hoja de cálculo. 



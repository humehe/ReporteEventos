import astropy,os
from astropy import table
#from astropy.table import Table
import numpy as np
import shutil
from os.path import expanduser

os.system('clear')

user = 'Hugo'

home = expanduser("~") + '/Dropbox/Curso-SEP-16/Reportes/' + user + '/'

#Table Names
MSTR_TBL    = home + 'Informe-Reporte_Inicial_Visitas-PLA_241-MASTER.dat'#'Informe-Reporte_Inicial_Visitas-EXP_241-MASTER.csv'
TBL_EVN_FRM = home + 'Informe-Reporte_Incial_Evento_Foro-PLA_241.csv'#'Informe-Reporte_Inicial_Eventos_Foros-EXP_241.csv'
TBL_EVN_HWK = home + 'Informe-Reporte_Incial_Evento_Tareas-PLA_241.csv'#'Informe-Reporte_Inicial_Eventos_Tareas-EXP_241.csv'
TBL_EVN_CHT = home + 'Informe-Reporte_Incial_Evento_Chat-PLA_241.csv'#'Informe-Reporte_Inicial_Eventos_Chat-EXP_241.csv'
#TBL_VST     = home  + 'Informe-Reporte_Inicial_Visitas-EXP_241.csv'
#TBL_NO_VST  = home  + 'Informe-Reporte_Inicial_No_Visitas-EXP_241.csv'

op_tbl_B    = home  + 'Informe-Reporte_Eventos-PLA_241.dat'
#Table Formats
tbl_format_ipt    = 'ascii.csv'#'ascii.fixed_width_two_line'       #ascii,csv,fits,ascii.fixed_width_two_line
tbl_format_opt    = 'ascii.tab'#.fixed_width_two_line'       #ascii,csv,fits,ascii.fixed_width_two_line

#############################################################################################################################

def Table_Read(table_name,format_tbl,*args, **kwargs):
	EVENT = kwargs.get('EVENT',False)
	ftbl = table.Table.read(table_name, format='ascii.no_header')
	ftbl.sort('col2')

	c1  = ftbl['col1']
	c2  = ftbl['col2']
	c3  = ftbl['col3']

	ftbl.write(table_name.split('.csv',1)[0]+str('.dat'), format=tbl_format_opt)
	print 'ASCII table version: ', table_name.split('.csv',1)[0] +'.dat'
	if EVENT == True:
		c4  = ftbl['col4']
		#print ftbl
		return(ftbl,c1,c2,c3,c4)
	elif EVENT == False:
		#print ftbl
		return(ftbl,c1,c2,c3)
	

	
#############################################################################################################################

tbl_master = Table_Read(MSTR_TBL,tbl_format_ipt)
tbl_forums = Table_Read(TBL_EVN_FRM,tbl_format_ipt)
tbl_hworks = Table_Read(TBL_EVN_HWK,tbl_format_ipt)
tbl_chat   = Table_Read(TBL_EVN_CHT,tbl_format_ipt)

id_master = tbl_master[1]
id_forums = tbl_forums[1]
id_hworks = tbl_hworks[1]
id_chat   = tbl_chat[1]


name_master = tbl_master[2]
name_forums = tbl_forums[2]
name_hworks = tbl_hworks[2]
name_chat   = tbl_chat[2]


tot_master = tbl_master[3]
tot_forums = tbl_forums[3]
tot_hworks = tbl_hworks[3]
tot_chat   = tbl_chat[3]

STD=[]
NME=[]
FRM=[]
HWK=[]
CHT=[]
print
for student in range(len(id_master)):
	STD.append(id_master[student])
	NME.append(name_master[student])

	if id_master[student] in id_forums:
		indx=int(np.where(id_forums==id_master[student])[0])
		FRM.append(tot_forums[indx])
	elif id_master[student] not in id_forums:
		pass
		FRM.append(0)
	if id_master[student] in id_hworks:
		indx=np.where(id_hworks==id_master[student])[0]
		HWK.append(tot_hworks[indx])
	elif id_master[student] not in id_hworks:
		pass
		HWK.append(0)
	if id_master[student] in id_chat:
		indx=int(np.where(id_chat==id_master[student])[0])
		CHT.append(tot_chat[indx])
	elif id_master[student] not in id_chat:
		pass
		CHT.append(0)

rtB                = table.Table()
rtB['ID']          = STD
rtB['Nombre']      = NME
rtB['Foros']       = FRM
rtB['Tareas']      = HWK
rtB['Chat']        = CHT

print

rtB.write(op_tbl_B, format=tbl_format_opt)#'ascii.fixed_width_two_line')	

print 'Tabla con los totales por evento por alumno: foros, tareas y chat en : '
print op_tbl_B


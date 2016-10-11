import astropy,os
from astropy import table
import numpy as np
from os.path import expanduser

os.system('clear')

user = 'Hugo'

home = expanduser("~") + '/Dropbox/Curso-SEP-16/Reportes/' + user + '/'

#Table Names
MSTR_TBL    = home + 'Informe-Reporte_Inicial_Visitas-EXP_241-MASTER.csv'
TBL_EVN_FRM = home + 'Informe-Reporte_Inicial_Eventos_Foros-EXP_241.csv'
TBL_EVN_HWK = home + 'Informe-Reporte_Inicial_Eventos_Tareas-EXP_241.csv'
TBL_EVN_CHT = home + 'Informe-Reporte_Inicial_Eventos_Chat-EXP_241.csv'

#Otput table
op_tbl_B    = home  + 'Informe-Reporte_Eventos-PLA_241.dat'

#Table Formats
tbl_format_ipt    = 'ascii.csv'
tbl_format_opt    = 'ascii.tab'

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
	
def Create_Informe_Eventos(tbl_master,tbl_foros,tbl_tareas,tbl_chats):

	tbl_master = Table_Read(MSTR_TBL,tbl_format_ipt)
	tbl_foros  = Table_Read(TBL_EVN_FRM,tbl_format_ipt)
	tbl_tareas = Table_Read(TBL_EVN_HWK,tbl_format_ipt)
	tbl_chats  = Table_Read(TBL_EVN_CHT,tbl_format_ipt)

	id_master = tbl_master[1]
	id_forums = tbl_foros[1]
	id_hworks = tbl_tareas[1]
	id_chat   = tbl_chats[1]

	name_master = tbl_master[2]
	name_forums = tbl_foros[2]
	name_hworks = tbl_tareas[2]
	name_chat   = tbl_chats[2]


	tot_master = tbl_master[3]
	tot_forums = tbl_foros[3]
	tot_hworks = tbl_tareas[3]
	tot_chat   = tbl_chats[3]

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
			#print 'It is',id_master[student],tot_forums[indx]
			FRM.append(tot_forums[indx])
		elif id_master[student] not in id_forums:
			pass
			FRM.append(0)
			#print 'Not'

		if id_master[student] in id_hworks:
			indx=np.where(id_hworks==id_master[student])[0]
			#print 'It is',id_master[student],tot_hworks[indx]
			HWK.append(tot_hworks[indx])
		elif id_master[student] not in id_hworks:
			pass
			HWK.append(0)
			#print 'Not'

		if id_master[student] in id_chat:
			indx=int(np.where(id_chat==id_master[student])[0])
			#print 'It is',id_master[student],tot_chat[indx]
			CHT.append(tot_chat[indx])
		elif id_master[student] not in id_chat:
			pass
			CHT.append(0)
			#print 'Not'		


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

#############################################################################################################################

Create_Informe_Eventos(MSTR_TBL,TBL_EVN_FRM,TBL_EVN_HWK,TBL_EVN_CHT)



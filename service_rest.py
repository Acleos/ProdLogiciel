import mysql.connector



def connection():
	return mysql.connector.connect(host='infoweb', user='E145516U', passwd='E145516U',db='E145516U')


def affichage(parametre):
	conn=connection()
	cursor=conn.cursor()
	try:
		int(parametre)
		cursor.execute("Select `Code Postal` from installations where `Code Postal` like '"+parametre+"%';")
	except valuerror:
		cursor.execute("Select `Nom de la commune` from installations where `Nom de la commune` like '"+parametre+"%';")
		commune=cursor.fetchall()
		cursor.execute("`` from installations where `Nom de la commune` like '"+parametre+"%';")
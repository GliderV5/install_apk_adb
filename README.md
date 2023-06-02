# Utilisation
## Windows 
Editer le fichier bat en changeant le port et l'adresse IP de connexion que adb doit utiliser à cette ligne : 

	<adb_path> connect <ip>:<port>

Il faut aussi remplacer <adb_path> par le chemin d'installation de adb.

	

pour installer un apk, faites simplement un glissé-déposé de l'apk sur le fichier bat pour lancer l'installation. 

## Chromebook
Créez un dossier dans lequel stocker les apk que vous voulez installer sur votre chromebook. Placez-y également le fichier install.py. Pour installer une application, employez la syntaxe suivante : 
	
	python3 install.py <votre_apk.apk>

> <em>Si adb n'est pas installé sur le Chromebook, le script vous le fera savoir et vous demandera si vous souhaitez qu'il l'installe pour vous. </em>
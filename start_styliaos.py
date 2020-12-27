import os

def startStyliaOS():
	os.system('py styliaos.py')


fileBoot = open('log.txt', 'w+')
fileBoot.write("[StyliaOS] Launching. Thanks for using !")
fileBoot.close()
print("[StyliaOS] Boot files... 99%")
startStyliaOS()



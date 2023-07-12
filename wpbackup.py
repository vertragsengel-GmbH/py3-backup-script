import os
import csv
import errno
import shutil
from time import strftime, gmtime


DONTBACKUP = ["BACKUPS", "wpbackup.py", "toBackup.csv", "readme.txt"]

class Backup():
        def __init__(self, sitename, dest_path="BACKUPS", format="zip"):
            self.sitename = sitename
            self.wp_dir = f"./{self.sitename}"
            self.dest_path = dest_path
            self.backupName = self.setBackupName()
            self.format = format
    
        def getBackupTime(self):
            return strftime("%Y-%m-%d-%S", gmtime())
        
        def setBackupName(self):
            return f"BACKUP-{self.getBackupTime()}-{self.sitename}"

        def createDir(self):
            try:
                os.makedirs(self.dest_path)
            except OSError as err:
                if err.errno == errno.EEXIST:
                    print(f"ERROR: Can't create directory: {self.dest_path}")
            
        def run(self):
            if not os.path.exists(self.dest_path):
                self.createDir()
            if self.doesExist() == False:
                return
            shutil.make_archive(f"{self.backupName}", self.format, self.wp_dir.upper())
            shutil.move(f"{self.backupName}.{self.format}", self.dest_path)
        
        def doesExist(self):
            return os.path.exists(self.sitename)
        
def checkToBackup():
    if not os.path.exists("toBackup.csv"):
        try:
            open('toBackup.csv', 'w')
        except OSError as err:
            if err.errno == errno.EEXIST:
                print(f"ERROR: Can't create directory: toBackup.csv")
        
def main():
    try: 
        with open("./toBackup.csv", 'r') as file:
            csvreader = list(csv.reader(file))
            if len(csvreader) < 1:
                print("Empty CSV")
                raise
            for file in csvreader:
                backup = Backup(str(file[0].upper()))
                backup.run()
    except:
        for file in list(os.listdir("./")):
                    if file in DONTBACKUP:
                        continue
                    backup = Backup(str(file.upper()))
                    backup.run()
    
if __name__ == "__main__":
    main()
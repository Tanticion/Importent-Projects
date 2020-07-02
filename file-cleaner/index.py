import glob
import shutil
import os

def start(FileType,dest,source2):

    for sorce in os.listdir(source2):
         print(sorce)
         source = "{}".format(sorce)
         for file in glob.glob(os.path.join(source,"*{}".format(FileType))):
             if sorce not in os.listdir(dest)  :
                 os.mkdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                 os.chdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                 shutil.copy2(file,'/Users/ivy_nova/Desktop/k/{}'.format(sorce))
             else:
                 os.chdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                 shutil.copy2(file, '/Users/ivy_nova/Desktop/k/{}'.format(sorce))

         for file in glob.glob(os.path.join(source, "*{}".format(FileType))):

              if sorce not in os.listdir(dest):
                  os.mkdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                  os.chdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                  shutil.copy2(file, '/Users/ivy_nova/Desktop/k/{}'.format(sorce))
              else:
                  os.chdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                  shutil.copy2(file, '/Users/ivy_nova/Desktop/k/{}'.format(sorce))
         for file in glob.glob(os.path.join(source, "*{}").format(FileType)):
               if sorce not in os.listdir(dest):
                    os.mkdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                    os.chdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                    shutil.copy2(file, '/Users/ivy_nova/Desktop/k/{}'.format(sorce))
               else:
                    os.chdir('/Users/ivy_nova/Desktop/k/{}'.format(sorce))
                    shutil.copy2(file, '/Users/ivy_nova/Desktop/k/{}'.format(sorce))

fileType = input('InsertFileType: ')
dest = input('Insert the destination: ')
source = input("Insert the source: ")

start(fileType,dest,source)
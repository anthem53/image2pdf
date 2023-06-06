import argparse
import os
import time
import shutil
from PIL import Image
import natsort

parser = argparse.ArgumentParser(description='루트 폴더에 있는 모든 작품들의 image를 pdf로 변환하는 프로그램.')

parser.add_argument('--root', required=True, help='Root Folder')
args = parser.parse_args()

DEBUGROOT = args.root

imageExtension = ["jpg","png","webp","jpeg"]

def createClearDir(address):
    try : 
        os.mkdir(address)
    except FileExistsError :
        shutil.rmtree(address)
        os.mkdir(address)

def createPDF(dir,dirName,resultFolder):

    if os.path.isdir(dir) == False:
        return

    cvt_rgb_0 = None
    img_list = []
    

    for e in natsort.natsorted(os.listdir(dir)):
        if e.split(".")[-1] not in imageExtension:
            continue

        targetFolder = dir+"\\"+e
        im_buf = Image.open(targetFolder)
        cvt_rgb = im_buf.convert('RGB')
        if cvt_rgb_0 == None:
            cvt_rgb_0 = cvt_rgb
        else:  pass

        img_list.append(cvt_rgb)
    
    pdfName = resultFolder+"\\"+dirName+".pdf"
    cvt_rgb_0.save(pdfName,save_all=True, append_images=img_list)

if __name__ == "__main__":

    rootDir = DEBUGROOT
    resultDir = rootDir+"\\PDF"
    # create result folder. If exist, clear and make again.
    createClearDir(resultDir)

    for mangaName in os.listdir(rootDir):
        
        if mangaName != "PDF":
            
            targetDir = rootDir+"\\"+mangaName
            print(targetDir)
            resultTargetDir = resultDir+"\\"+mangaName
            createClearDir(resultTargetDir)
            if os.path.isdir(targetDir) == True:
                for epiName in os.listdir(targetDir):
                    curEpiDir = targetDir + "\\" + epiName
                    createPDF(curEpiDir,epiName,resultTargetDir)
            else: pass

        else:
            pass

    print("Process Complete!")

    
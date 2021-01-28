count1 = 0
for imgname in os.listdir(imagefolder):
    count += 1

    #if count == 10:
    #    break

    imgn = imgname.split('.')[0]
    image1 = cv2.imread(imagefolder + imgname)
    bbox1 = readboxyolo5(labelfolder, imgn, image1)
    #print(bbox1)
    bbx = bbox1.shape
    if bbx[0] == 0:
        print(imgname)
        os.remove(imagefolder + imgname)
        os.remove(labelfolder + imgn + '.txt')
        count1 +=1
print(count1)
    

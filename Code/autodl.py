import os
import sys
import urllib.request 
from curses.ascii import isdigit
from bs4 import BeautifulSoup 



j = 2177 

loop = 36 

def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


#================================================================#




def childGetter(url, path, i):
    
    opener = urllib.request.FancyURLopener({})
    url = url.__str__()

    f = opener.open(url)
    content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    
    age = "UU"
    myParas = soup.find_all("p", {"class": "question"})
    pex = ""
    if myParas.__len__() > 0:
        for myPara in myParas:
            pex = myPara.decode_contents().strip()
            pex = BeautifulSoup(pex, 'html.parser')
            for ques in pex.findAll('strong'):
                if "Age" in str(ques):
                    if isdigit(str(pex)[22]) and isdigit(str(pex)[23]):
                        age = "{}{}".format(str(pex)[22], str(pex)[23])
                    
    if age is None:
        age = "UU"

    mydivs = soup.find_all("div", {"class": "case-imageset"})
    tex = ""
    for mydiv in mydivs:
        tex += mydiv.decode_contents().strip()
    tex = BeautifulSoup(tex, 'html.parser')
    global j
    for link in tex.findAll('a'):
        
        bf = "b"
        if link.get('href')[-8] != "a" and link.get('href')[-8] != "b":
            bf = link.get('href')[-5]
        else:
            bf = link.get('href')[-8]
            
        
        # {CASE_uniqueNumber_personNumber_side_beforeOrAfter_gender_age_quality_noise_rotation_crop_source}     
        
        # CASE --> case 
        # uniqueNumber --> 0000001..9999999
        # personNumber --> 00001..99999
        # side --> L: looking left , R: looking right , F: looking front , X: looking LF , Y: looking RF , D: looking up
        # beforeOrAfter --> B: before , A: after
        # gender --> M: male , F: female
        # age --> 10..99
        # quality --> H: high , L: low , D: dark  T: dark and low
        # noise --> B: blurry , W: watermark , N: none
        # rotation --> G: good , B: bad
        # crop --> G: good , B: bad , N: blur on face , T: blur on face and bad crop
        # source --> 01..99
        
        
        name = "case_{uniqueNum:07d}_{personNum:05d}_F_{beforeOrAfter}_F_{age}_H_N_G_G_01".format(uniqueNum = j,
                                                                                                  personNum = i,
                                                                                                  beforeOrAfter = bf,
                                                                                                  age = age)
        
        download_image(link.get('href'), path, name)

        j += 1

#================================================================#

from bs4 import BeautifulSoup 
import urllib.request


def dlall(myRange1,myRange2):
    for x in range(myRange1,myRange2):
        opener = urllib.request.FancyURLopener({})
        url = "https://www.plasticsurgery.org/photo-gallery/procedure/rhinoplasty/page/{}".format(x)
        f = opener.open(url)
        content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        mydivs = soup.find_all("div", {"class": "gallery grid-container Component"})
        
        fex = mydivs[0]

        i = 1
        count = 0
        
        global loop
        i = (loop * 10) + i
        loop += 1
        
        for link in fex.findAll('a'):
             
            if count < 11:

                count += 1
                
                
                
                path = "/page/{}".format(i)
                
                if link.get('href')[0] == 'h':
                    childGetter(link.get('href'), path, i)
                    print("         ----- case {:05d} completed -----         ".format(i))
                else:
                    i -= 1
                    
            i += 1
            
        print("***----------- page {: 5d} completed -----------***".format(x))


#================================================================#

start = int(sys.argv[1])
end = int(sys.argv[2])
dlall(start, end)




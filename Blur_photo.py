import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Poniższy program przedstawia działanie 3 róznych filtrów dolnoprzepustowych i działanie splotu.
"""


"""
blur photo using convolution. Input: img and average.
Average is a positive number (reasonably range is from 1 to 100)
kernel is a identity matrix divided by square of average
return blur photo
"""
def convolution2D(img):
    avg = getPositiveNumber("Enter a number of how blurry the photo should be(1-100):")
    kernel = np.ones((avg, avg), np.float32) / (avg ** 2)
    return cv2.filter2D(img, -1, kernel)

"""
Filtrowanie gaussowskie jest bardzo skuteczne w usuwaniu szumu gaussowskiego z obrazu.
"""
def gaussianFiltering(img):
    value = getPositiveNumber("Enter a number of how blurry the photo should be(odd number):")
    if(value%2==0):
        print("WRONG NUMBER, Photo not changed")
        return img
    return cv2.GaussianBlur(img, (value, value), cv2.BORDER_DEFAULT)

""" 
Funkcja cv2.medianBlur () oblicza medianę wszystkich pikseli pod oknem jądra, a środkowy piksel jest
zastępowany tą wartością mediany. Jest to bardzo skuteczne w usuwaniu hałasu solnego i pieprzowego.
Ciekawą rzeczą do odnotowania jest to, że w filtrach Gaussa i filtrach pudełkowych filtrowana 
wartość dla elementu centralnego może być wartością, która może nie istnieć na oryginalnym obrazie.
Jednak nie jest tak w przypadku filtrowania medianowego, ponieważ centralny element jest zawsze zastępowany 
pewną wartością piksela na obrazie. To skutecznie redukuje hałas. Rozmiar jądra musi być dodatnią nieparzystą
liczbą całkowitą.
"""
def medianFiltering(img):
    value = getPositiveNumber("Enter a number of how blurry the photo should be(odd number):")
    if(value%2==0):
        print("WRONG NUMBER, Photo not changed")
        return img
    return cv2.medianBlur(img,value)

"""
W przeciwieństwie do poprzednich nie usuwa krawędzi. Usuwa szumy ale jest wolniejsze

"""

def bilateralFilter(img):
    value = getPositiveNumber("Enter a number of how blurry the photo should be:")
    return cv2.bilateralFilter(img,value,75,75)

def getPositiveNumber(string):
    while True:
        try:
            user_input = int(input(string))
        except ValueError:
            print("this is not an int!")
            continue
        else:
            if user_input > 0:
                return user_input
                break
            print("Try with positive number!")


img = cv2.imread('butterfly.png')
print("Try some photo processing:")
print("1. Convolution2D")
print("2. Gaussian Filtering")
print("3. medianFiltering")
print("4. convolution2D")
print("5. bilateralFilter")

while (True):
    type = getPositiveNumber("What type of photo processing do you want? ")
    if type == 1:
        dst = convolution2D(img)
    elif type == 2:
        dst = gaussianFiltering(img)
    elif type == 3:
        dst = medianFiltering(img)
    elif type == 4:
        dst = bilateralFilter(img)
    else:
        print("type is out of range")
        continue

    # create plot to comparison photos
    plt.subplot(121)
    plt.imshow(img),
    plt.title('Original'),plt.xticks([]),plt.yticks([])
    plt.subplot(122)
    plt.imshow(dst)
    plt.title("Blured"),plt.xticks([]),plt.yticks([])
    plt.show()

    # save changed photo
    img=dst



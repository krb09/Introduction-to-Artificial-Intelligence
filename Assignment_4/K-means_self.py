import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
import cv2
import math
import random
from PIL import Image


X = cv2.imread('scarlet_tanager.jpg',  cv2.IMREAD_COLOR)     ## read the image ( M * N * 3)
img = Image.fromarray(X, 'RGB')
img.save('my1.png')
img.show()

print(X.shape)
print(X[1])

X = X.reshape((-1,3))
print(X.shape)

print('********reshape to original*********')
X_new = X.reshape((240,420,-1))
print(X_new[1])
print(X_new.shape)

class K_Means:
    def __init__(self, k=29, tol=0.001, max_iter=300):
        self.k = k                                      ## number of clusters
        self.tol = tol                                  ## the tol. if the centroids do not move by 0.001, stop
        self.max_iter = max_iter                        ## number of iterations

    def fit(self,data):

        self.centroids = []                             ##initially the centroids dictionary is empty

        for i in range(self.k):
            val = random.choice(data)
            self.centroids.append(val)                 ## initialize the centroids with first K pixels in the image. Can also randomize it as well


        for i in range(self.max_iter):                  ## start to run for max-iterations

            print('******start of Kmeans*****')
            self.classifications = {}                   ## always begin by new classifications. That is the number of pixels for each centroid as a dictionary

            for i in range(self.k):
                self.classifications[i] = []            ## the intial classification is always empty, and then we get K classifications

            for pixel in data:
                distances = []
                for centroid in self.centroids:
                    distance = math.sqrt( 2*( pixel[0] - centroid[0])**2 + 4*(pixel[1] - centroid[1])**2 + 3*(pixel[2] - centroid[2])**2 )
                    distances.append(distance)

                classification = distances.index(min(distances))
                # print('**classification**')
                # print(classification)
                self.classifications[classification].append(pixel)

            print('***classifications******')
            print(self.classifications[2])
            #print(self.classifications)

            print('***printing self-centroids****')
            prev_centroids = self.centroids[:]
            print(self.centroids)
            print(prev_centroids)


            for classification in self.classifications:
                self.centroids[classification] = np.around(np.average(self.classifications[classification],axis=0))

            print(type(self.centroids))


            print('***after classifications*****')
            print(self.centroids)

            check_tol = True

            size = len(prev_centroids)
            print(size)
            print(len(self.centroids))
            for c in range(0,size):
                print('****start of checking for tolerance****')
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]

                distance_moved = math.sqrt( ( original_centroid[0] - current_centroid[0])**2 + (original_centroid[1] - current_centroid[1])**2 + (original_centroid[2] - current_centroid[2])**2 )
                original_dist = math.sqrt( (original_centroid[0])**2 + (original_centroid[1])**2 + (original_centroid[2])**2 )

                if (distance_moved - original_dist)/original_dist*100.0 > self.tol:
                    check_tol = False

            if check_tol:
                break

clf = K_Means()

clf.fit(X)

print(clf.centroids)
print(len(clf.centroids))



print(type(X[1]))
print(type(clf.centroids[1]))

for pixel in X:
    distances = []
    for centroid in clf.centroids:
        distance = math.sqrt( ( pixel[0] - centroid[0])**2 + (pixel[1] - centroid[1])**2 + (pixel[2] - centroid[2])**2 )
        distances.append(distance)
    ind = distances.index(min(distances))
    pixel[:] = clf.centroids[ind][:]


X = X.reshape((240,420,-1))
print(X[1])
img2 = Image.fromarray(X, 'RGB')
img2.save('my.png')
img2.show()

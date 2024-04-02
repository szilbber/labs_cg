import numpy as np
from PIL import Image, ImageOps
import math
from random import randint

#3------------------------------------
f=open('C:\labs_kg\lab2\model_1.obj')
vertiecs = []
for s in f:
    splitted = s.split(' ')
    if(splitted[0] == 'v'):
        v = [float(splitted[1]), float(splitted[2]), float(splitted[3])]
        vertiecs.append(v)
#print(vertiecs)

#5-----------------------------------
f=open('C:\labs_kg\lab2\model_1.obj')
poligons = []
for s in f:
    splitted = s.split(' ')
    # print(splitted)
    if(splitted[0] == 'f'):
        arr = []
        for i in range(1,4):
            f = str(splitted[i]).split('/')
            arr.append(int(f[0]))
        #print(f)
        poligons.append(arr)
#print(poligons)

#6-----------------------------------
def line3(image, x0, y0, x1, y1): 
    flag = False 
    if (abs(y1-y0)>abs(x1-x0)): 
        y0,x0 = x0,y0 
        y1,x1 = x1,y1 
        flag = True 
    if(x0>x1): 
        x1,x0 = x0,x1 
        y1,y0 = y0,y1 

    y = y0 
    dy = 2*abs((y1-y0)) 
    derror=0 
    if y1>y0: 
        y_update = 1 
    else: 
        y_update = -1 

    for x in range(x0, x1): 
        if (flag):      
            image[x,y] = 255 
        else: 
            image[y,x] = 255 
        derror += dy 
        if derror>(x1-x0): 
            derror -= 2*(x1-x0) 
            y += y_update 

matrix_ex_5 = np.zeros((2000, 2000), dtype = np.uint8)
for i in range(len(poligons)):
    arr_0=vertiecs[poligons[i][0]-1]#указываем вершину 0
    x_0=int(10000*arr_0[0]+1000)#абсцисса вершины 0
    y_0=int(10000*arr_0[1]+1000)#ордината вершины 0
    
    arr_1=vertiecs[poligons[i][1]-1]#указываем вершину 1
    x_1=int(1000+10000*arr_1[0])#абсцисса вершины 1
    y_1=int(10000*arr_1[1]+1000)#ордината вершины 1
    
    arr_2=vertiecs[poligons[i][2]-1]#указываем вершину 2
    x_2=int(10000*arr_2[0]+1000)#абсцисса вершины 2 
    y_2=int(10000*arr_2[1]+1000)#ордината вершины 2
    line3(matrix_ex_5, x_0, y_0, x_1, y_1)
    line3(matrix_ex_5, x_0, y_0, x_2, y_2)
    line3(matrix_ex_5, x_2, y_2, x_1, y_1)
# img_ex_5 = Image.fromarray(matrix_ex_5)
# img_ex_5 = ImageOps.flip(img_ex_5)
# img_ex_5.show()


#LR2
zbuf = [[1500.0 for j in range(2000)] for i in range(2000)]
#7-----------------------------------------------
def bar(x,y,x0,y0,x1,y1,x2,y2):
    lambda0 = ((x1 - x2)*(y - y2) - (y1 - y2)*(x - x2)) / ((x1 -x2)*(y0 - y2) - (y1 - y2)*(x0 - x2))
    lambda1 = ((x2 - x0)*(y - y0) - (y2 - y0)*(x - x0)) / ((x2 -x0)*(y1 - y0) - (y2 - y0)*(x1 - x0))
    lambda2 = 1.0 - lambda0 - lambda1
    return [lambda0, lambda1, lambda2]


#2 часть 2 лабы
#11---------------------
def normal_of_triangle(x0,y0,z0, x1,y1,z1, x2,y2,z2):
    vec1 = np.array([x1 - x2, y1 - y2, z1 - z2])
    vec2 = np.array([x1 - x0, y1 - y0, z1 - z0])
    return np.cross(vec1, vec2)
#12---------------------
def clipping_nonface_faces(x0,y0,z0, x1,y1,z1, x2,y2,z2):
    n = normal_of_triangle(x0,y0,z0, x1,y1,z1, x2,y2,z2)
    l = [0,0,1]
    return np.dot(n, l)/math.sqrt(n[0]**2 + n[1]**2 + n[2]**2) 

#15---------------------
def rotation(point, a, b, y,tx,ty):
    matr1 = [[1, 0, 0], [0, math.cos(a), math.sin(a)], [0, -math.sin(a), math.cos(a)]]
    matr2 = [[math.cos(b), 0, math.sin(b)], [0, 1, 0], [-math.sin(b), 0, math.cos(b)]]
    matr3= [[math.cos(y), math.sin(y), 0], [-math.sin(y), math.cos(y), 0], [0, 0, 1]]
    matrbuf =  np.matmul(matr1, matr2)
    R = np.matmul(matrbuf, matr3)
    new_point = np.matmul(R, point)
    new_point[0]+=tx
    new_point[1]+=ty
    return new_point


#8-----------------------------------------------
matrix_ex_8 = np.zeros((2000, 2000), dtype = np.uint8)
def draw_of(color, img,x0,y0,z0,x1,y1,z1,x2,y2,z2):
    xmin = int(min(x0,x1,x2))-1
    ymin = int(min(y0,y1,y2))-1
    xmax = int(max(x0,x1,x2))+1
    ymax = int(max(y0,y1,y2))+1
    # color = randint(0,255)
    if(xmin<0): xmin=0
    if(ymin<0): ymin=0
    if(xmax>2000): xmax=2000
    if(ymax>2000): ymax=2000
    for i  in range(xmin, xmax):
        for j in range(ymin, ymax):
            coord = bar(i,j,x0,y0,x1,y1,x2,y2)
            if((coord[0])>=0 and (coord[1])>=0 and (coord[2])>=0):
                z = coord[0]*z0 + coord[1]*z1 + coord[2]*z2
                if(z<zbuf[j][i]):
                    img[j,i] = (0,0,color)
                    zbuf[j][i] = z
                # img[j,i] = (0,0,color)
                
# draw_of(matrix_ex_8, 2000, 600, 0, 2000, 500, 0)
img_ex_8 = Image.fromarray(matrix_ex_8)
img_ex_8 = ImageOps.flip(img_ex_8)
# img_ex_8.show()
#9-----------
#10----------
matrix_ex_5 = np.zeros((2000, 2000, 3), dtype = np.uint8)
for i in range(len(poligons)):
    arr_0=vertiecs[poligons[i][0]-1]#указываем вершину 0
    x_0=(10000*arr_0[0]+1000)#абсцисса вершины 0
    y_0=(10000*arr_0[1]+1000)#ордината вершины 0
    z_0=(10000*arr_0[2]+1000)#ордината вершины 0
    
    arr_1=vertiecs[poligons[i][1]-1]#указываем вершину 1
    x_1=(1000+10000*arr_1[0])#абсцисса вершины 1
    y_1=(10000*arr_1[1]+1000)#ордината вершины 1
    z_1=(10000*arr_1[2]+1000)#ордината вершины 1
    
    arr_2=vertiecs[poligons[i][2]-1]#указываем вершину 2
    x_2=(10000*arr_2[0]+1000)#абсцисса вершины 2 
    y_2=(10000*arr_2[1]+1000)#ордината вершины 2
    z_2=(10000*arr_2[2]+1000)#ордината вершины 2
    
    tx,ty = 1700, -450
    
    point0 = rotation([x_0,y_0,z_0],0,91,0,tx,ty)
    point1 = rotation([x_1,y_1,z_1],0,91,0,tx,ty)
    point2 = rotation([x_2,y_2,z_2],0,91,0,tx,ty)
    
    # считаем цвет
    # nonface = clipping_nonface_faces(x_0, y_0,z_0, x_1, y_1,z_1, x_2, y_2,z_2)
    nonface = clipping_nonface_faces(point0[0], point0[1],point0[2], point1[0], point1[1], point1[2], point2[0], point2[1], point2[2])
    color = -255*nonface
    # color = randint(0,255)
    if(nonface<0):
        # draw_of(color, matrix_ex_5, x_0, y_0,z_0, x_1, y_1,z_1, x_2, y_2,z_2)
        draw_of(color, matrix_ex_5, point0[0], point0[1],point0[2], point1[0], point1[1], point1[2], point2[0], point2[1], point2[2])
        
img_ex_8 = Image.fromarray(matrix_ex_5)
img_ex_8 = ImageOps.flip(img_ex_8)
img_ex_8.show()
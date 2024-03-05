import numpy as np
from PIL import Image, ImageOps
import math
# 1-----—
#H, W = 50,50

#инициализация полутонового изображения размера HxW чёрными пикселями
#matrix_1 = np.zeros((H, W), dtype = np.uint8)
#matrix_2 = np.full((H,W), 255, dtype = np.uint8)
#matrix_3 = np.full((H, W, 3), [255,0,0],dtype=np.uint8)
#matrix_4 = np.zeros((H,W,3), dtype=np.uint8)

# for h in range(H):
#     for w in range(W):
#         for i in range(3):
#             matrix_4[h,w,i] = (h+w+i)%256
        


#img_1 = Image.fromarray(matrix_1, mode='L')
#img_2 = Image.fromarray(matrix_2, mode='L')
#img_3 = Image.fromarray(matrix_3, mode='RGB')
#img_4 = Image.fromarray(matrix_4, mode='RGB')

#img_1.show()
#img_2.show()
#img_3.show()
#img_4.show()

#img_1.save("demo1.jpeg")
#img_2.save("demo2.jpeg")
#img_3.save('demo3.jpeg')
#img_4.save('demo4.jpeg')

# 2--------------------------------
# def line1(image, x0, y0, x1, y1):
#     count = int(math.sqrt((x0-x1)**2 + (y0 - y1)**2))
#     step = 1 / count
#     for t1 in range(0,count):
#         t = t1 * step
#         x = int((1-t)*x0 + t*x1)
#         y = int((1-t)*y0 + t*y1)
#         image[y,x] = 255

# def line2(image, x0, y0, x1, y1):
#     flag = False
#     if (abs(y1-y0)>abs(x1-x0)):
#         y0,x0 = x0,y0
#         y1,x1 = x1,y1
#         flag = True
#     if(x0>x1):
#         x1,x0 = x0,x1
#         y1,y0 = y0,y1
#     for x in range(x0, x1):
#         t = (x-x0)/(x1-x0)
#         y = round((1-t)*y0 + t*y1)
#         if (flag):
#             image[x,y] = 255
#         else:
#             image[y,x] = 255

# def line3(image, x0, y0, x1, y1): 
#     flag = False 
#     if (abs(y1-y0)>abs(x1-x0)): 
#         y0,x0 = x0,y0 
#         y1,x1 = x1,y1 
#         flag = True 
#     if(x0>x1): 
#         x1,x0 = x0,x1 
#         y1,y0 = y0,y1 

#     y = y0 
#     dy = 2*abs((y1-y0)) 
#     derror=0 
#     if y1>y0: 
#         y_update = 1 
#     else: 
#         y_update = -1 

#     for x in range(x0, x1): 
#         if (flag):      
#             image[x,y] = 255 
#         else: 
#             image[y,x] = 255 
#         derror += dy 
#         if derror>(x1-x0): 
#             derror -= 2*(x1-x0) 
#             y += y_update 


# matrix_5 = np.zeros((200, 200), dtype = np.uint8)

# for i in range(13):
#     x0,y0 = 100, 100
#     a = (2*math.pi*i)/13
#     x1,y1 = int(100 + 95*math.cos(a)),int(100 + 95*math.sin(a))
#     line3(matrix_5, x0,y0,x1,y1)
# img_5 = Image.fromarray(matrix_5)
# img_5.show()

#3------------------------------------
f=open('model_1.obj')
vertiecs = []
for s in f:
    splitted = s.split(' ')
    if(splitted[0] == 'v'):
        v = [float(splitted[1]), float(splitted[2]), float(splitted[3])]
        vertiecs.append(v)
#print(vertiecs)
        
#4-----------------------------------
# matrix_ex_4 = np.zeros((1000, 1000), dtype = np.uint8)
# for i in range(len(vertiecs)):
#     x = int(5000*vertiecs[i][0]) +500
#     y = int(5000*vertiecs[i][1]) +500
#     matrix_ex_4[y,x] = 255
# img_ex_4 = Image.fromarray(matrix_ex_4)
# img_ex_4 = ImageOps.flip(img_ex_4)
#img_ex_4.show()

#5-----------------------------------
f=open('model_1.obj')
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
img_ex_5 = Image.fromarray(matrix_ex_5)
img_ex_5 = ImageOps.flip(img_ex_5)
img_ex_5.show()
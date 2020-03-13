# author:Zhaoran ZHAO
# contact: zhaozhaoran@bupt.edu.cn
# datetime:2020/3/12 8:38 pm
# software: PyCharm

import numpy as np
import sys
sys.path.append('/Users/nannan/PycharmProjects/SingleCaliPython/SingleCali/SingleCamera')
from SingleCali.SingleCamera import SingleCamera


# The homogeneous world coodinate

# Although it would be more appropriate to write a function to read the coordinates, 
# we've simplified it by listing the coordinates directly in array.

# world corrdinate
w_xz = np.array([8, 0, 9, 1, 8, 0, 1, 1, 6, 0, 1, 1, 6, 0, 9, 1])
w_xz = w_xz.reshape(4, 4)
# w_xy=np.array([5,1,0,5,9,0,4,9,0,4,1,0])
w_xy = np.array([5, 1, 0, 1, 5, 9, 0, 1, 4, 9, 0, 1, 4, 1, 0, 1])
w_xy = w_xy.reshape(4, 4)
# w_yz=np.array([0,4,7,0,4,8,0,8,3,0,8,7])
w_yz = np.array([0, 4, 7, 1, 0, 4, 8, 1, 0, 8, 3, 1, 0, 8, 7, 1])
w_yz = w_yz.reshape(4, 4)
w_coor = np.vstack((w_xz, w_xy, w_yz))
print(w_coor)
# pixel coordinate
c_xz = np.array([275, 142, 312, 454, 382, 436, 357, 134])
c_xz = c_xz.reshape(4, 2)
c_xy = np.array([432, 473, 612, 623, 647, 606, 464, 465])
c_xy = c_xy.reshape(4, 2)
c_yz = np.array([654, 216, 644, 368, 761, 420, 781, 246])
c_yz = c_yz.reshape(4, 2)
c_coor = np.vstack((c_xz, c_xy, c_yz))
print(c_coor)
# coordinate for validation whether the M is correct or not
w_check = np.array([6,0,5,1,3,3,0,1,0,4,0,1,0,4,4,1,0,0,7,1])
w_check=w_check.reshape(5,4)
c_check=np.array([369,297,531,484,640,468,646,333,556,194])
c_check=c_check.reshape(5,2)




def main():
    aCamera=SingleCamera(w_coor,c_coor,12) # 12 points in total are used
    aCamera.composeP()
    aCamera.svdP()
    aCamera.workInAndOut()
    
    # validate the result by putting in a world coordinate
    # def myCheck(new_world,new_pixel,aM):
    #     pass
    # w_test=np.array([7,0,2,1])
    # test_pix=np.dot(aCamera.returnM(),w_test)
    # u=test_pix[0]/test_pix[2]
    # v=test_pix[1]/test_pix[2]
    # print(u,v)
    aCamera.selfcheck(w_check,c_check)


if __name__=="__main__":
    main()


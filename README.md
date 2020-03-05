# CameraCaliPython
## Introduction
The demo for single camera calibration by a 3d-rig picture.
And it is compiled by Pycharm, use python3 and a library named numpy.
There are several steps in this demo:
1. Choose a picture of 3D-rig online, as shown in *Jietu20200301-091513.jpg*
Though we do not have a real rig, but this would not change the core method of camera calibration because 
it's okay to assume that the length and width of each small square is the unit length.
2. Mark some cross points by Labelme (or any other app with similar function) and record the pixel coordinate of them with the correspondings
in world coordinate system. In this demo, the three intersections of planes are chosen as x,y and z axis of world coordinate system, which 
follow right-handed system.  (as shown in *Jietu20200301-091513.jpg*)
In this demo, 12 points are chosen. Generally speaking, though 6 points are enough theoretically, more points are good for the precesion of camera matrix estimation. 
In the image, three quadrangles are labeled by *Labelme* and only their vertex are useful,i.e., only their corrdinates would be recorded by *labelme* in image coordination system. The cooresponding value in world coordination system is recorded in pink in the image. The direction of the arrow indicates the order of coordinate recording.
3. Use the chosen points to work out M, K, R,t by methods on class.
4. To verify the calibration results, we bring in some points from the world coordination system and check whether they can be mapped to corresponding pixels by M.

## Usage
To Use the demo, you can download from github to your own IDE, remember to change the *sys.path.append* and *from..import..* row according to your own settings.
Of course, the IDE is not necessary, you can alse run by command line if your python3 and numpy are ready.

# CameraCaliPython
## 介绍
通过3D摄像机标定物的单张图像进行摄像机标定。
由Pycharm编译，使用python3和numpy的库。
此演示中有几个步骤：
1.该示例选取网络上的一个立体标定物图片虽然没有真正的摄像机标定装置，但是可以假设每个小方块的长度和宽度都是单位长度。在线选择3D装备的图片，如*Jietu20200301-091513.jpg*所示
尽管我们没有真正的装备，但这不会改变相机校准的核心方法，因为
可以假设
2.用Labelme（或其他具有类似功能的应用程序）标记一些交叉点，并用相应的点记录它们的像素坐标
在世界坐标系中。在此演示中，选择三个平面的交点作为世界坐标系的x，y和z轴，
遵循右手系统。 （如* Jietu20200301-091513.jpg *中所示）
在此演示中，选择了12点。一般而言，尽管理论上6个点就足够了，但更多点可以用于相机矩阵估计。
在图像中，三个四角形用* Labelme *标记，并且只有它们的顶点才有用，即，在图像协调系统中，* labelme *只会记录它们的corcordinates。世界协调系统中的对应值以粉红色记录在图像中。箭头的方向指示坐标记录的顺序。
3.使用选定的点通过类上的方法算出M，K，R，t。
4.为了验证校准结果，我们从世界坐标系中引入一些点，并检查它们是否可以通过M映射到相应的像素。

## 用法
要使用该演示，您可以从github下载到自己的IDE，请记住根据自己的设置更改* sys.path.append *和* from..import .. *行。
当然，IDE不是必需的，如果您的python3和numpy准备好了，也可以通过命令行运行。

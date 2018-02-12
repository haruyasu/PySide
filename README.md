# PySide Training

## Python helped create the visual effects

### Pipline engineers, developers
* Python
  * PyQt/PySide

### Computer grahics research and development
* C++

## PyCharm Tips
* VOS(Git)
1. Share Project on GitHub
2. Add File (Ctrl + Alt + A)
3. Commit Changes (Ctrl + K)
4. Push (Ctrl + Shift + K)

### Qt Designer Tips
* add path
  * C:\Python27\Lib\site-packages\PySide
  * C:\Python27\Scripts
* command line
  * show.ui -> showGui.py
    * pyside-uic.exe show.ui -o showGui.py
  * icons.qrc -> icons_rc.py
    * pyside-rcc.exe icons.qrc -o icons_rc.py

## Coding Conventions
PEP 8 -- Style Guide for Python Code
https://www.python.org/dev/peps/pep-0008/

### Class names
o class MyClassName(object):

x class myclassName(object):

### Variable names
o skin_joints = ['joint1', 'joint2']

x skinJoints = ['joint1', 'joint2']

###  Function names
o def calculate_bounds():

x def calculateBounds():

###  Spacing
o [1, 2, 3, 4]

x [1,2,3,4]

o if joint_height > 10.0:

x if joint_height>10.0:

o get_export_nodes(root='skeleton_grp')

x get_export_nodes( root = 'skeleton_grp' )

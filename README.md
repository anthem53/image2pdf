# image2pdf

## Environment

- argparse
- shutil
- pillow
- natsort


Maybe... argparse and shutil is built-in module in Python, so you just download pillow and natsort module with pip library.

You can copy and paste below code to bash

```
pip install argparse pillow natsort
```

## How to Use

I will guide with one kind of example. 
![image](https://github.com/anthem53/image2pdf/assets/28498486/c6175f48-b949-41bb-bac0-2f3e39fe1f74)




1.  Set the root directory. That directory is Root folder of example file
2.  Root directory has child directories. Each child directory has some hw directories. 
3.  Each hw has a lot of image file. Current Project support image extension only "jpg","png","webp","jpeg". These image files are submitted file in above example image.
4.  In this directory system, you type on bash as  ```python main.py --root "root directory path"```. if root directory path is ```/root/workspace/python_server/test```, type  ```python main.py --root "/root/workspace/python_server/test"```
5.  Then, the result is saved on PDF directory that is under root directory path.
6.  You can get the merged pdf file.



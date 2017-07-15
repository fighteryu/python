# python & c 共存
# ZigBee中已包含.h文件

# python文档 http://python.usyiyi.cn/   https://docs.python.org/3/
# 扩展包 http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil
#       https://pypi.python.org

## 生成pyc文件
* import py_compile
* py_compile.compile('path') //path是包括.py文件名的路径

## 生成exe文件
* pip pyinstaller 
* pyinstaller -F  .py --noconsole //取消调试框


## 生成当前环境安装包列表
* pip freeze>requirements.txt


## 正则匹配
```
a='<title>helloworld</title>'
b=re.findall('<title>(.*?)</title>',a,flags=re.S)[0]
print(b)#helloworld
```

## jupyter更改默认路径
* cmd----jupyter notebook --generate-config 生成jupyter_notebook_config.py文件
* 更改文件配置
```
## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = 'D:\\jupyter'
```

  

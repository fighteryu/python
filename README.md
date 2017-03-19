# python & c 共存
# ZigBee中已包含.h文件

# python文档 http://python.usyiyi.cn/   https://docs.python.org/3/
# 扩展包 http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil
#       https://pypi.python.org

## 生成pyc文件
* import py_compile
* py_compile.compile('path') //path是包括.py文件名的路径

## 生成exe文件
* pip installer 
* installer -F  .py
## 正则匹配
```
a='<title>helloworld</title>'
b=re.findall('<title>(.*?)</title>',a,flags=re.S)[0]
print(b)#helloworld
```

  

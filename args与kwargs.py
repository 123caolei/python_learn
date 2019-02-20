# -*- mode: python; coding: utf-8 -*-

def func1(*args):   #形参
    print(args)
func1('qwe')      #输出为('qwe',)

def func2(x,y,*args):
    print(x,y,args)
func2(1,2,3,4,5)   #输出为(1, 2, (3, 4, 5))

def func3(x,y,**kwargs):
    print(x,y,kwargs)
func3(1,2,z=3)   #输出为(1, 2, {'z': 3})

def func4(arg,*args,**kwargs):
    print(arg,args,kwargs)
func4(1,2,3,4,5,a=8,b=9,c=0)#输出为(1, (2, 3, 4, 5), {'a': 8, 'c': 0, 'b': 9})
#一个arg只代表一个参数，＊args可以代表n个参数，一般直接给值，　　＊＊kwargs也可以是n个参数，给值时是以键值的形式

def fun5(**kwargs):
    kwargs.setdefault('start','1')  #kwargs是字典,字典的内建方法,不存在这个键值对就新建
    print(kwargs)
    kwargs.pop('second','2')
    print(kwargs)   #存在这个键值对就删除
fun5(second=2)


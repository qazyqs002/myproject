"""
闭包：
　　在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。

https://www.cnblogs.com/s-1314-521/p/9763376.html

闭包有啥用？？！！

　　很多伙伴很糊涂，闭包有啥用啊？？还这么难懂！

　　 3.1装饰器！！！装饰器是做什么的？？其中一个应用就是，我们工作中写了一个登录功能，我们想统计这个功能执行花了多长时间，
我们可以用装饰器装饰这个登录模块，装饰器帮我们完成登录函数执行之前和之后取时间。
　　 3.2面向对象！！！经历了上面的分析，我们发现外函数的临时变量送给了内函数。大家回想一下类对象的情况，对象有好多类似的属性和方法，
所以我们创建类，用类创建出来的对象都具有相同的属性方法。闭包也是实现面向对象的方法之一。在python当中虽然我们不这样用，在其他编程语
言入比如avaScript中，经常用闭包来实现面向对象编程
　　 3.3实现单例模式！！ 其实这也是装饰器的应用。单例模式毕竟比较高大，，需要有一定项目经验才能理解单例模式到底是干啥用的，我们就不探讨了。
"""
#闭包函数的实例
def outer(a):
    # outer是外部函数 a和b都是外函数的临时变量
    b = 10
    # inner是内函数
    def inner():
     #在内函数中 用到了外函数的临时变量
        print(a+b)
    # 外函数的返回值是内函数的引用
    return inner


if __name__ == '__main__':
    # 在这里我们调用外函数传入参数5
    # 此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
    # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
    demo = outer(5)
    print(demo)
    # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
    # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
    demo() # 15
    demo2 = outer(7)
    demo2()#17


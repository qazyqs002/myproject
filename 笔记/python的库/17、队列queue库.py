# _*_ coding:utf-8 _*_
# File:17、队列queue库.py
# Time:2021/11/22  16:17
# Author: yqs
import queue

# 一、构造方法
# Queue是构造方法，函数签名是Queue(maxsize=0) ，其中maxsize设置队列的大小。
q = queue.Queue(maxsize=100)
# 二、实例方法
item = ""
q.qsize() # 返回queue的近似值。注意：qsize>0 不保证(get)取元素不阻塞。qsize<maxsize不保证(put)存元素不会阻塞
q.empty() # 判断队列是否为空。和上面一样注意
q.full() # 判断是否满了。和上面一样注意
q.put(item, block=True, timeout=None) # 往队列里放数据。如果满了的话，blocking = False 直接报 Full异常。如果blocking = True，就是等一会，timeout必须为 0 或正数。None为一直等下去，0为不等，正数n为等待n秒还不能存入，报Full异常。
q.put_nowait(item) # 往队列里存放元素，不等待
q.get(item, block=True, timeout=None) # 从队列里取数据。如果为空的话，blocking = False 直接报 empty异常。如果blocking = True，就是等一会，timeout必须为 0 或正数。None为一直等下去，0为不等，正数n为等待n秒还不能读取，报empty异常
q.get_nowait(item) # 从队列里取元素，不等待两个方法跟踪入队的任务是否被消费者daemon进程完全消费
q.task_done() # 表示队列中某个元素呗消费进程使用，消费结束发送的信息。每个get()方法会拿到一个任务，其随后调用task_done()表示这个队列，这个队列的线程的任务完成。就是发送消息，告诉完成啦！
# 如果当前的join()当前处于阻塞状态，当前的所有元素执行后都会重启（意味着收到加入queue的每一个对象task_done()调用的信息）
# 如果调用的次数操作放入队列的items的个数多的话，会触发ValueError异常
q.join()  # 一直阻塞直到队列中的所有元素都被取出和执行未完成的个数，只要有元素添加到queue中就会增加。未完成的个数，只要消费者线程调用task_done()表明其被取走，其调用结束。当未完成任务的计数等于0，join()就会不阻塞


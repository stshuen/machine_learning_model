import tensorflow as tf

a = tf.constant([1.0, 2.0], name='a')  # 定义一个常量使用tf.constant方法
b = tf.constant([1.0, 2.0], name='b')
result = a + b
# 通过a.graph可以查看张量所属的计算图，如果没有特别指定，则属于当前默认的计算图
print(a.graph is tf.get_default_graph())  # 输出为True

g1 = tf.Graph()
with g1.as_default():
    # 在计算图g1中定义变量'v',并设置初始值为0。
    v = tf.get_variable('v', initializer=tf.zeros_initializer()(shape=[1]))

g2 = tf.Graph()
with g2.as_default():
    # 在计算图g2中定义变量'v',并设置初始值为1。
    v = tf.get_variable('v', initializer=tf.ones_initializer()(shape=[1]))

# 在计算图g1中读取变量'v'的取值
with tf.Session(graph=g1) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('', reuse=True):
        # 在计算图g1中，变量'v'的取值应该为0，下一行代码会输出[0.]。
        print(sess.run(tf.get_variable('v')))

# 在计算图g2中读取变量'v'的取值
with tf.Session(graph=g2) as sess:
    tf.global_variables_initializer().run()
    with tf.variable_scope('', reuse=True):
        # 在计算图g2中，变量'v'的取值应该为1，下一行代码会输出[1.]。
        print(sess.run(tf.get_variable('v')))

g = tf.Graph()
# 指定计算运行的设备。
with g.device('/gpu:0'):
    result = a + b

# tf.constant是一个计算，这个计算的结果为一个张量，保存在变量a中。
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([1.0, 2.0], name='b')
result = tf.add(a, b, name='add')
print(result)
'''
输出：Tensor("add:0", shape=(2,), dtype=float32)
'''

# 1、 创建一个会话
with tf.Session() as sess:
    print(sess.run(result))

# tensorflow中需要手动指定默认会话，当该会话指定后，可以通过tf.Tensor.eval函数来计算一个张量的取值。
# 2、 创建一个默认的会话
sess = tf.Session()
with sess.as_default():
    print(result.eval())

# 3、 创建一个会话
sess = tf.Session()
# 下面两个命令等价
print(sess.run(result))
print(result.eval(session=sess))

# 在交互式环境下，使用设置默认会话的方法来获取张量的取值更加方便，tensorflow提供了一种在交互式环境下直接构建
# 默认会话的函数，tf.InteractiveSession。该函数会自动将生成的会话注册为默认会话。
sess = tf.InteractiveSession()
print(result.eval())
sess.close()

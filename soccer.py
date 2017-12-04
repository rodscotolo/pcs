"""
    Placeholder in tensorflow
"""
import numpy as np
import tensorflow as tf

"""
    RANK 2
"""
a = tf.placeholder(tf.int32, shape=(90, 2), name='a')

placar = tf.reduce_sum(a, axis=0, name='placar')

print("\nPlaceholders in TensorFlow\n")
print(a)
print()

timeA = 0
timeB = 0
games = 1
with tf.Session() as sess:

    while games < 100:
        data = np.loadtxt('data/jogo'+str(games)+'.txt')
        a_val = a.eval(feed_dict={a: data})
        placar_val = placar.eval(feed_dict={a: data})
        games = games + 1

        if placar_val[0] > placar_val[1]:
            timeA = timeA + 3
        elif placar_val[0] > placar_val[1]:
            timeB = timeB + 3
        else:
            timeA = timeA + 1
            timeB = timeB + 1

    if timeA > timeB:
        print("TimeA foi campeão, seu numero de pontos foram:\n", timeA)
    elif timeB == TimeA:
        print("EMPATE!! O numero de pontos foram:\n", timeA)
    else:
        print("TimeB foi campeão, seu numero de pontos foram:\n", timeB)
    #print("The value of a:\n", a_val)
    #print("\nThe value of placar:\n", placar_val)
    #print()

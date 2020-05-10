s1 = {1, 2, 3, 4, 6, 7, 8, 9}
s2 = {3, 4, 6, 7, 12, 13, 14, 15}
print("Intersection:", s1.intersection(s2))  #求s1和s2的交集
print("Union:", s1.union(s2))                #求s1和s2的并集
print("Difference:", s1.difference(s2))      #求s1和s2的差集
print("Symmetric difference:", s1.symmetric_difference(s2))  #求s1和s2的对称差集
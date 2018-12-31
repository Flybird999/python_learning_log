# 彩蛋
#import this 
# 保留字
'''import keyword
print(keyword.kwlist)'''

import sys

print("命令行参数如下：")
for i in sys.argv:
    print(i)
print('\n\n Python 路径为：',sys.path,'\n')
#作者：邓超
#学号：1901010076
#内容：用for...in..语法打印九九乘法表
#用时：3小时左右

print('打印九九乘法表')     #将range的数列储存进a的变量当中
for a in range(1,10):    #还是将range这个数列储存在b的变量中（range里为什么是1，a+1，暂时不懂）
    for b in range(1,a+1):    #按照乘法表格式序打印出来，但此时打印出来的是连续的，没有回车换行。
            print(a,  '*', b, '=', a * b, sep='', end='  ')   
    print()       #增加回车换行。       


#作者：邓超
#学号：1901010076
#作业：用while循环打印九九乘法表并用条件语句去除掉偶数行
#用时：约10小时左右

print('打印九九乘法表并去出偶数行')
f = 1       #设置一个起始数的变量f
while f <= 9:      #当f小于等于9：（设置f的最大数为9）
     if f % 2 != 0:     #如果f除2的余数不等于0：（不等于0就往下运行）
          h = 1     #设置一个起始数为1的变量h
          while h < f + 1:      #当h小余f+1时：（条件只要成立就行）
              print(f, "*", h, '=',f*h, sep='', end='  ')       #打印（f乘h=f*h,
              h += 1        #在h的循环中循环一次加1
          print()       #循环换行
     f += 1     #在f的的循环中循环一次加1






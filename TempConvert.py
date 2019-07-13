#TempConvert.py
datat=input('请输入带有符号的温度值:')
if datat[0] in ['F','f']:
    C=(eval(datat[1:])-32)/1.8
    print('转换后的温度值是C{:.2f}'.format(C))
elif datat[0] in ['C','c']:
    F=eval(datat[1:])*1.8+32
    print('转换后的温度值是F{:.2f}'.format(F))
else:
    print('输入格式错误')

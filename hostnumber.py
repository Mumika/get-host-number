import os


def loop(netnum):
    host = []
    count = 0
    f = open(r'C:\Users\ECHO\Desktop\output\ping.txt', 'w')  # 路径写一个真实存在的就行
    for i in range(1, 256):
        text = 'ping ' + netnum + str(i)
        if (readcmd(text)):
            f.write(text + ' ' + '连接成功\n')
            host.append(text)
            count += 1
        else:
            f.write(text + ' ' + '连接失败\n')
    print('当前wifi共分配了' + str(count) + '台主机地址')
    f.write('当前wifi共分配了' + str(count) + '台主机地址\n')
    print('分别是：')
    f.write('分别是：\n')
    for i in host:
        print(i)
        f.write(i + ' ')
    f.close()


def readcmd(text):  # 使用ping的cmd命令，若能ping到，则返回True
    result = os.popen(text)
    context = result.read()
    if "无法访问目标主机" in context:
        ans = text + ' ' + '连接失败'
        print(ans)
    else:
        ans = text + ' ' + '连接成功'
        print(ans)
        return True

    result.close()


if __name__ == '__main__':
    netnum = '192.168.31.'  # 这里写自己的网络号，注意，后面几位不用写
    loop(netnum)

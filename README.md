# get-host-number
不用知道路由器的密码也能得出当前wifi有多少设备连接。
不是什么复杂的操作，也就是用cmd的命令ping到每个当前同一网络号下的IP地址。
如果能ping成功就说明这个连接着。
然后进行汇总，得出成功的数量，就是当前网络有几个设备连接了。
因为ping需要时间，且循环要255次，缺点也很明显，已经遍历过的IP地址，状态发生改变的话，也查不出来。
所以属于一个很粗糙的代码。
如果有更好的实现方法欢迎讨论。

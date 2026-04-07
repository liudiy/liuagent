## 第 1 页

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


## 第 2 页

声明
版权
Copyright ©2025北京东方通科技股份有限公司或其关联公司（以下简称“东方通”）。保留所有权利。
版权声明
• 本文档的所有权和知识产权归属于东方通所有。
• 除非另有明确约定，东方通不授予任何明示或暗示的许可或权利，使用者不得以任何方式将本文档中的
任何内容用于商业目的。
• 东方通对本文档享有版权。本文档的所有内容，包括但不限于文字、图像、图表、图标、示意图、屏幕
截图等，均受版权法和国际版权条约的保护。
• 未经东方通明确授权，任何人不得对本文档以任何形式复制、修改、传播、分发、展示或进行衍生创
作。
商标声明
•
、TongTech 标识以及其他相关东方通图形、徽标、服务名称和商标（以下统称为“东方通商
标”）是东方通或其关联公司的注册商标或商标。
• 未经东方通明确授权，任何人不得以任何方式使用、复制或展示东方通商标。此外，未经东方通事先书
面同意，不得将东方通商标与其他商标、标识或徽标进行混淆、链接或结合使用。
• 除非另有明确约定，本商标声明不授予任何明示或暗示的许可或权利，对东方通商标的使用须获得东方
通的明确授权。
• 本文档提及的所有其他商标、标识、徽标或产品名称均为其各自所有者的财产，并可能受其各自的商标
法保护。
免责声明
请在使用东方通产品之前仔细阅读本免责声明，并根据自身情况判断是否继续使用。如有任何问题，请联系
我们的客户支持团队。
• 本产品的使用是基于用户自己的判断和风险评估。本文档仅作为使用指导，不对使用本产品所产生的结
果做任何明示或暗示的担保。
• 东方通不对用户未按照本文档中的指导正确使用东方通产品而导致的任何损失或损害承担责任；
• 本文档可能会包含第三方提供的内容、链接或资源，这些内容由第三方自行负责。东方通对于这些内容
的准确性、完整性、合法性或可靠性不承担责任。用户在使用这些内容时应自行判断和承担风险。
• 由于产品版本升级或其他原因，本文档内容会不定期更新。东方通保留在不事先通知用户的情况下随时
对文档进行修改、更新或中止的权利。
如需获取有关东方通产品的许可或使用权，请联系东方通或授权代理商。任何违反本声明的行为将受到适用
法律的追究。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
1


## 第 3 页

前言
本文档是 TongHttpServer 产品手册之一，提供使用 TongHttpServer 过程中遇到的常见问题及解决方案。
阅读前注意事项
通过阅读本文档，您确认并同意自行承担因未具备必要专业背景和知识而导致的任何风险或后果。在使用本
文档中提供的信息和指南时，请始终谨慎，并在必要时寻求专业人士建议和指导。
• 适用对象
本文档主要适用于使用本产品的系统管理员阅读，部分内容同样适用于基于本产品进行应用开发或应用
部署的人员阅读。
• 专业背景
本文内容可能涉及到操作系统、服务器硬件、网络等相关领域的知识。请确保您具备相关背景和知识，
以便更好地理解和应用本手册的内容。
• 技能要求
为了能够充分理解和应用本文档的内容，建议您具备如下技能：
◦基本系统管理任务
◦掌握 Linux 系统基本操作
◦掌握 Docker/K8s 基本操作
◦在终端窗口发布命令
◦使用 Web 浏览器
• 术语和概念
本文档可能使用一些专业术语和概念。请确保您熟悉这些术语和概念，或者有能力查阅相关资料以便进
一步理解。
• 实践经验
为了最大程度地受益于本文档，建议您具备一定实践经验。这将帮助您更好地应用文档中的操作指南和
建议。
请注意，本文档不适用于没有相关专业背景和知识的用户。如果您对本文档的内容或所需背景有任何疑问，
请在使用之前咨询相关专业人士或寻求额外的支持。
用户手册集
TongHttpServer 为您提供如下用户使用手册。
编号
用户手册
说明
1
001_TongHttpServer_V6.0产品用户手册
提供 TongHttpServer 单节点使用说明。
2
002_TongHttpServer_V6.0监控配置手册
提供 TongHttpServer 监控使用说明。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
2


## 第 4 页

编号
用户手册
说明
3
003_TongHttpServer_V6.0常见配置指令手册
提供 TongHttpServer 常见配置指令说
明。
4
004_TongHttpServer_V6.0国密证书解密手册
提供国密 SSL 双证书签发流程、加密证
书解密说明。
5
005_TongHttpServer_V6.0常见问题手册
提供使用 TongHttpServer 过程中遇到的
常见问题及解决方案。
6
006_TongHttpServer_V6.0版本说明手册
记录当前版本相对于上一个版本的变更
说明。
技术支持
东方通产品将为您提供全方位的技术支持，您可以通过以下方式获得技术支持：
• 网址：www.tongtech.com
• 电话：400-650-7088
• 邮箱：support@tongtech.com
您在取得技术支持时，请提供如下信息：
• 您的姓名
• 您的公司信息
• 您的联系方式
• 操作系统及其版本
• 产品版本号
• 日志等错误的详细信息
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
3


## 第 5 页

目录
声明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1
前言. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
1. THS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  5
1.1. THS 启动时报 getgrnam("nobody") failed. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  5
1.2. 访问静态文件报 403 错误. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  6
1.3. 配置高可用所有节点都存在漂移 IP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
1.4. POST 接口报 413 错误. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9
1.5. 日志中出现 proxy_temp failed (13: Permission denied) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
1.6. 日志中出现 client_body_temp failed (13: Permission denied). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  11
1.7. 访问后端节点静态文件不成功. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
1.8. 单独访问节点正常，代理后就不正常了. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
1.9. 后端应用获取不到前端传的包头，怀疑 THS 将包头丢弃. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
4


## 第 6 页

1. THS
1.1. THS 启动时报 getgrnam("nobody") failed
问题现象：
执行 THS start.sh 脚本启动 httpserver 时，报 “getgrnam("nobody") faild (2: No such file or directory)” 
错误，如下图所示。
原因分析：
如果以 root 用户启动 THS 时，worker 进程会切换到 nobody 用户 nobody 组运行。
如果配置系统不存在 nobody 用户或存在 nobody 用户但不属于 nobody 组则会报错。
解决方案一：
1. 打开 linux 终端。
2. 执行如下命令，查询是否存在 nobody 用户及 nobody 用户所在组。
groups nobody
◦若回显信息为 “nogroup”，则请执行步骤 3。
root@dest:/opt/THS/bin# groups nobody
nobody : nogroup
◦若回显信息为 “no such user”，则请参考 解决方案二。
root@dest:/opt/THS/bin# groups nobody
groups: ‘nobody’: no such user
3. 修改 “THS/conf/httpserver.conf” user 配置指令。
将如下配置：
#user nobody;
修改为：
user nobody nogroup;
4. 再次启动 THS，通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
5


## 第 7 页

解决方案二：
1. 执行如下命令，添加一个 “nologin” 新用户。
如下以 “www” 用户为例说明。
useradd -r -s /usr/sbin/nologin www
回显信息，如下所示。
root@donny:/opt/THS/bin# useradd -r -s /usr/sbin/nologin www
root@donny:/opt/THS/bin# groups www
www : www
2. 修改 “THS/conf/httpserver.conf” user 配置指令。
将如下配置：
#user nobody;
修改为：
user www www;
3. 再次启动 THS，通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
1.2. 访问静态文件报 403 错误
问题现象：
THS 部署静态文件，浏览器访问静态文件报 403 错误。
原因分析：
THS 的 worker 进程无静态文件的读权限。
THS 静态文件的权限目录需要 “755” 权限，文件需要 “644” 权限。
为了保障系统的安全，请勿简单地将文件及目录的权限修改为 “777”。
解决方案：
1. 执行如下命令，查看 httpserver worker 进程的用户。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
6


## 第 8 页

ps -ef | grep httpserver
回显信息，如下所示。
root@dest:/opt/THS/html# ps -ef | grep httpserver
root      285046       1  0 14:12 ?        00:00:00 httpserver: master process /opt/THS/bin/httpserver -p
/opt/THS -c /opt/THS/conf/httpserver.conf
www       285047  285046  0 14:12 ?        00:00:00 httpserver: worker process
www       285048  285046  0 14:12 ?        00:00:00 httpserver: worker process
www       285049  285046  0 14:12 ?        00:00:00 httpserver: worker process
www       285050  285046  0 14:12 ?        00:00:00 httpserver: worker process
说明：
以上示例 master 进程以 root 用户执行，worker 进程以 www 用户运行。
2. 执行如下命令，查看目录链权限。
namei -m /opt/THS/html/www/index.html
回显信息，如下所示。
root@donny:/opt/THS/html/www# namei -m /opt/THS/html/www/index.html
f: /opt/THS/html/www/index.html
 drwxr-xr-x /
 drwxr-xr-x opt
 drwx------ THS
 drwxr-xr-x html
 drwx------ www
 -rw------- index.html
说明：
以上示例中存在三处权限不对：
◦THS 目录的访问权限为 “700”，需要 “755” 权限;
◦www 目录的权限为 “700”，需要 “755” 权限;
◦index.html 权限为 “600”，需要 “644”。
3. 修改 THS 目录及静态文件权限。
◦执行如下命令，修改 THS 目录权限
由于 THS 同级目录可能存在其他文件夹，为避免影响其他文件夹的权限，请单独修改。
root@dest:/opt/THS/html/www# cd /opt/
root@dest:/opt# chmod 755 THS
◦执行如下命令，修改 THS 静态应用部署文件权限
由于静态应用存在多个文件夹及多个文件，单独修改很耗时，可以使用以下命令进行修改。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
7


## 第 9 页

目录权限修改：
root@dest:/opt/THS/html# chmod 755  $(find  . -type d)
文件权限修改：
root@dest:/opt/THS/html# chmod 644  $(find  . -type f)
4. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
1.3. 配置高可用所有节点都存在漂移 IP
问题现象：
当配置高可用集群时，通过 ip a
 
 命令查看，所有 THS 服务器上都存在漂移 IP。
原因分析：
httpserverHA 集群间通信使用 VRRP 协议。若防火墙未开启 VRRP 协议，则会导致节点间无法通信，所有
节点都认为自己是主节点，出现脑裂。
解决方案：
• 防火墙使用 iptables
1. 执行如下命令，查看防火墙状态。
service iptables status
2. 执行如下命令，查看 iptables 规则是否开启 VRRP 协议。
iptables -S
3. 若上一步中显示未开启 VRRP 协议，则分别执行如下命令，开启 VRRP 协议。
iptables -I INPUT -i enp -d 224.0.0.0/8 -p vrrp -j ACCEPT
iptables -I OUTPUT -o enp -d 224.0.0.0/8 -p vrrp -j ACCEPT
4. 开启 VRRP 协议后，执行如下命令，保存修改。
service iptables save
• 防火墙使用 firewall-cmd
1. 执行如下命令，查看防火墙状态。
firewall-cmd --state
2. 执行如下命令，查看 iptables 规则是否开启 VRRP 协议。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
8


## 第 10 页

firewall-cmd --list-all
3. 若上一步中显示未开启 VRRP 协议，则执行如下命令，开启 VRRP 协议。
firewall-cmd --zone=public --add-protocol=vrrp --permanent
4. 开启 VRRP 协议后，执行如下命令，保存修改。
firewall-cmd --reload
说明：
若服务器使用阿里云、京东云、腾讯云等云服务器，VRRP 协议的开启，需要联系云厂商按厂商文档进
行配置。
1.4. POST 接口报 413 错误
问题现象：
POST 上传文件，接口报 413 Request Entity Too Large错误。
原因分析：
THS 默认允许上传文件最大为 1 兆，超过1兆的上传会报 413 错误。
解决方案：
1. 修改 “THS/conf/httpserver.conf” 配置文件。
添加 client_max_body_size  配置。
http {
    .....
    server {
        .....
        client_max_body_size 10m;
        .....
    }
    .....
}
2. 分别执行如下命令，热加载 THS。
cd THS/bin
start.sh reload
3. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
9


## 第 11 页

1.5. 日志中出现 proxy_temp failed (13: Permission
denied)
问题现象：
下载大文件时接口报 500 错误，查看 THS error.log，日志中出现 proxy_temp 无权限错误。
原因分析：
THS 下载后端文件时，当文件过大，会将文件缓存到 “THS/temp/proxy_temp” 目录。
当 worker 进程无写此目录的权限时会报错。
解决方案：
1. 修改 “THS/temp” 目录为 worker 进程的用户。
a. 执行如下命令，确认 worker 进程的用户。
ps -elf | grep httpserver |grep worker
b. 执行如下命令，确认该用户的组。
groups user

示例中 “user” 为上一步中查出的用户名。
2. 执行如下命令，更改 “THS/temp” 目录所属用户和组。
以 “www” 用户及 “nogroup” 为例说明。
cd THS/
chown www:nogroup temp -R
3. 执行如下命令，排查 temp 绝对路径上的权限是否正确。
namei -m /a/b/../THS/temp/proxy_temp
回显信息，如下所示。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
10


## 第 12 页

说明：
上图中可以看出 data 目录的权限不是 “700”，需要 “755”。
执行如下命令，修改 data 目录的权限。
chmod 755 /data
4. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
1.6. 日志中出现 client_body_temp failed (13:
Permission denied)
问题现象：
上传文件时接口报 500 错误，查看THS error.log，日志中出现 client_body_temp/0000000000 failed (13:
Permission denied) 无权限错误。
原因分析：
THS 接收文件时，当文件过大，会将文件缓存到 “THS/temp/client_body_temp”。
当 worker 进程无写此目录的权限时会报错。
解决方案：
1. 修改 “THS/temp” 目录为 worker 进程的用户。
a. 执行如下命令，确认 worker 进程的用户。
ps -elf | grep httpserver |grep worker
b. 执行如下命令，确认该用户的组。
groups user

示例中 “user” 为上一步中查出的用户名。
2. 分别执行如下命令，更改 “THS/temp” 目录所属用户和组。
以 “www” 用户及 “nogroup” 为例说明。
cd THS/
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
11


## 第 13 页

chown www:nogroup temp -R
3. 执行如下命令，排查 temp 绝对路径上的权限是否正确。
namei -m /a/b/../THS/temp/client_body_temp
回显信息，如下所示。
说明：
上图中可以看出 data 目录的权限为 “700”，需要 “755”。
执行如下命令，修改 data 目录的权限。
chmod 755 /data
4. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
1.7. 访问后端节点静态文件不成功
问题现象：
静态文件 “.css”、“.js” 部署在后端节点，通过 THS 反向代理到后端节点。
• 单独访问后端节点的静态文件正常；
• 通过 THS 访问后端静态文件地址正常；
• 通过应用首页不能加载静态文件。
THS 单独访问页面正常
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
12


## 第 14 页

THS 访问应用静态页面不正常
原因分析：
浏览器将请求发送到 THS，THS 充当代理客户端将请求转发给后端节点，如东方通 TongWeb。
由于THS 转发包头中 HTTP Referer 中的内容为网站应用的地址，而 THS 转发给后端的 Host 包头为后端服
务器的IP 和端口，二者不一致，在后端限制的时候导致访问不成功。
解决方案一：
1. 修改 “THS/httserver.conf” 配置文件。
在对应的 location 中添加，也可以添加到 server 块中。
location / {
    ...
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
13


## 第 15 页

    proxy_set_header Host $http_host;
    ...
}
说明：
示例中 $http_host  为浏览器传给 THS 的 host，是 THS 内置变量。
这段配置的作用是让 THS 转发将浏览器的 Host 直接转发给后端，不要使用后端的 IP:port 生成 Host。
2. 进入 “THS/bin” 目录，并热加载 THS。
cd THS/bin
./start.sh reload
3. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
解决方案二：
1. 修改 “THS/httserver.conf” 配置文件。
在对应的 location 中添加，也可以添加到 server 块中。
location / {
    ...
    proxy_set_header Referer "";
    ...
}
说明：
既然是 Referer 和 Host 不匹配导致的问题，将 Referer 设置为空也能解决问题。
2. 进入 “THS/bin” 目录，并热加载 THS。
cd THS/bin
./start.sh reload
3. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
1.8. 单独访问节点正常，代理后就不正常了
问题现象：
单独访问后端节点正常，通过 THS 代理后出现莫名其妙的错误。
原因分析：
出现这种问题的原因很多、但多数是由于 THS 传给后端的包头不对，被后端限制了，如上一节中介绍的
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
14


## 第 16 页

Referer 和 Host 不匹配。
此时，可以通过对比 THS 传给后端的包头及用浏览器单独访问后端节点的包头，进行对比修改。
解决方案：
1. 抓取 THS 到后端节点的包头。
a. 进入 “THS/tools” 目录。
b. 修改 “nettool.conf” 的 port 和 interface 配置。
说明：
▪interface：THS 到后端节点数据传输使用的网络接口名，如 lo、eth0 等。
▪port：后端节点的端口。
c. 以 root 用户启动 netool。
./netool
d. 通过浏览器访问 THS 端口，netool 会输出 THS 转给后端的完整数据包。
说明：
“logs/nettool.log” 中也有完整的日志输出。
2. 浏览器 “F12”，查看单独访问后端节点的包头。
3. 将浏览器的包头和 netool 的包头进行对比。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
15


## 第 17 页

4. 根据对比，调整 “THS/conf/httpserver.conf” 配置。
5. 进入 “THS/bin” 目录，并热加载 THS。
cd THS/bin
./start.sh reload
6. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
1.9. 后端应用获取不到前端传的包头，怀疑 THS 将包头丢
弃
问题现象：
THS 前端的代理如 F5 传了一个包头给 THS，希望 THS 将此包头传给后端，但是后端程序怎么也获取不到
包头，怀疑 THS 将包头丢弃。
后端应用获取不到 chinese 包头，怀疑 THS 丢弃
原因分析：
THS 默认会将前端的包头转给后端。
若包头有错，THS error.log 中会有对应错误日志输出。
若没有错误日志，后端获取不到包头，应该首先怀疑后端丢弃了包头，通过 netool 排查解决问题。
解决方案：
1. 抓取 THS 到后端节点的包头，确认是否正常转发。
a. 进入 THS tools 目录。
b. 修改 “nettool.conf” 的 port 和 interface 配置。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
16


## 第 18 页

说明：
▪interface：THS 到后端节点数据传输使用的网络接口名，如 lo、eth0 等。
▪port：后端节点的端口。
c. 以 root 用户启动 netool。
./netool
d. 通过浏览器访问 THS 端口，netool 会输出 THS 转给后端的完整数据包。
说明：
“logs/nettool.log” 中也有完整的日志输出。
从 netool 输出可以看出 THS 已经将 chinese 及 X509Certificate.SubietDN 包头转发给后端节点。
2. 调整后端节点服务器，如东方通 TongWeb 需要将 GBK 改为 utf-8。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
17


## 第 19 页

3. 通过上述操作即可解决该问题。
若仍存在此问题，请联系东方通技术人员获取支持。
东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
18


## 第 20 页

东方通负载均衡软件 TongHttpServer V6.0 常见问题手册
6015A01
版权所有©东方通
19



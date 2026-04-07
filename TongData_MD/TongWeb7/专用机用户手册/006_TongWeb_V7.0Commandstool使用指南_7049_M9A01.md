## 第 1 页

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


## 第 2 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
i 
声明 
版权 
Copyright ©2025北京东方通科技股份有限公司或其关联公司（以下简称“东方通”）。保留所有权利。 
版权声明 
⚫ 
本文档的所有权和知识产权归属于东方通所有。 
⚫ 
除非另有明确约定，东方通不授予任何明示或暗示的许可或权利，使用者不得以任何方式将本文
档中的任何内容用于商业目的。 
⚫ 
东方通对本文档享有版权。本文档的所有内容，包括但不限于文字、图像、图表、图标、示意图、
屏幕截图等，均受版权法和国际版权条约的保护。 
⚫ 
未经东方通明确授权，任何人不得对本文档以任何形式复制、修改、传播、分发、展示或进行衍
生创作。 
 
商标声明 
⚫ 
、TongTech标识以及其他相关东方通图形、徽标、服务名称和商标（以下统称为“东方
通商标”）是东方通或其关联公司的注册商标或商标。 
⚫ 
未经东方通明确授权，任何人不得以任何方式使用、复制或展示东方通商标。此外，未经东方通
事先书面同意，不得将东方通商标与其他商标、标识或徽标进行混淆、链接或结合使用。 
⚫ 
除非另有明确约定，本商标声明不授予任何明示或暗示的许可或权利，对东方通商标的使用须获
得东方通的明确授权。 
⚫ 
本文档提及的所有其他商标、标识、徽标或产品名称均为其各自所有者的财产，并可能受其各自
的商标法保护。 
 
免责声明 
请在使用东方通产品之前仔细阅读本免责声明，并根据自身情况判断是否继续使用。如有任何问题，
请联系我们的客户支持团队。 
⚫ 
本产品的使用是基于用户自己的判断和风险评估。本文档仅作为使用指导，不对使用本产品所产
生的结果做任何明示或暗示的担保。 
⚫ 
东方通不对用户未按照本文档中的指导正确使用东方通产品而导致的任何损失或损害承担责任； 
⚫ 
本文档可能会包含第三方提供的内容、链接或资源，这些内容由第三方自行负责。东方通对于这
些内容的准确性、完整性、合法性或可靠性不承担责任。用户在使用这些内容时应自行判断和承
担风险。 
⚫ 
由于产品版本升级或其他原因，本文档内容会不定期更新。东方通保留在不事先通知用户的情况
下随时对文档进行修改、更新或中止的权利。 
 
如需获取有关东方通产品的许可或使用权，请联系东方通或授权代理商。任何违反本声明的行为将受
到适用法律的追究。


## 第 3 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
ii 
版本变更说明 
本手册的更新是累积的。因此，最新的手册版本包含对以前版本所做的所有更改。 
手册版本 
适用于产品版本 
更新内容 
7049_M9A01 7.0.4.9_M9 
修改如下章节： 
2.11delete-file-user，默认域defaultRealm 中默认提供的监视管理员
monitor，不允许删除。 
7049_M8A01 7.0.4.9_M8 
无 
7049_M7A01 7.0.4.9_M7 
修改如下章节： 
2.10 update-file-user，新增“--oldpassword oldpassword”参数，需
要输入旧密码才能更新用户信息。 
7049_M6A01 7.0.4.9_M6 
新增如下章节： 
1.2.1 设置命令行访问白名单 
修改如下章节： 
⚫ 
2.82 update-license，新增licenseType和publicKey参数，支持
remote和active模式。 
⚫ 
2.36 create-jdbc-connection-pool，补充“--connectionProperties”
连接参数说明，当数据库类型配置为goldendb时，添加
mysqlCompatible=true连接属性配置，兼容Mysql驱动。 
⚫ 
2.37 update-jdbc-connection-pool，补充
“--connectionProperties”连接参数说明，当数据库类型配置为
goldendb时，添加mysqlCompatible=true连接属性配置，兼容
Mysql驱动。 
7049_M5A01 7.0.4.9_M5 
新增如下章节： 
2.78 generate-tdg-token，生成TDG服务的token加密字符串。 
修改如下章节： 
⚫ 
1.2 安全认证，新增“加密字符串时，必须在目标
${TongWeb_HOME}/bin 目录中执行password脚本；否则，生
成的加密字符串将会不一样，从而导致无法成功解密”说明。 
⚫ 
2.41 deploy，新增“--deployTimeout”参数，部署超过此时间，
系统将中断部署流程，默认600秒。 
⚫ 
2.49 update-auto-deploy-config，新增“--deployTimeout”参数。
自动部署耗时超过此时间，系统将中断部署流程，默认600秒。 
7049_M4A01 7.0.4.9_M4 
新增如下章节： 
⚫ 
2.16 create-session-manager 


## 第 4 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
iii 
手册版本 
适用于产品版本 
更新内容 
⚫ 
2.17 list-session-manager 
⚫ 
2.18 delete-session-manager 
修改如下章节： 
⚫ 
2.41 deploy，新增“sessionManager”参数及说明。 
7049_M3A01 7.0.4.9_M3 
无 
7049_M2A01 7.0.4.9_M2 
无 
7049_M1A01 7.0.4.9_M1 
无 
7049A01 
7.0.4.9 
修改如下章节： 
⚫ 
2.3 config-password，删除“修改thanos账号密码时，若是首
次使用thanos账号，请使用set-server-arg命令设置服务器参数”
的说明。 
⚫ 
2.16 create-http-listener，国密认证JDK要求由“JDK8-JDK11”
变更为“JDK8及以上版本”，当在JDK17环境下，需要额外
添加启动参数。 
⚫ 
2.20 update-http-listener，国密认证JDK要求由“JDK8-JDK11”
变更为“JDK8及以上版本”，当在JDK17环境下，需要额外
添加启动参数。 
⚫ 
2.36
 
create-jdbc-connection-pool
，
最
大
连
接
数 
jdbcmaxactive 的默认值从“10”修改为“100”。 
⚫ 
2.37  
update-jdbc-connection-pool ，最大连接数 
jdbcmaxactive 的默认值从“10”修改为“100”。 
7048A01 
7.0.4.8 
修改如下章节： 
⚫ 
2.2 change-admin-password，新增“修改密码时要求5次以内
密码不能重复”的说明。 
⚫ 
2.10 update-file-user，filepassword修改为非必选参数，设置
该参数时要求5次内密码不重复。 
⚫ 
2.16 create-http-listener 和 2.17 update-http-listener，国密认证
JDK环境要求由“JDK8小版本”修改为“JDK8-JDK11”。 
⚫ 
2.38 deploy，新增“enableHotSwap”开启类热加载功能。 
⚫ 
所有命令：修改secure参数描述。 
⚫ 
2.82 update-license，新增licenseIps参数，使用License Server
服务进行License认证。 
7047A01 
7.0.4.7 
⚫ 
新增如下章节： 
◼ 
2.4 list-permission：查看命令权限编码。 
◼ 
2.5 set-permission：给命令行用户增加权限、删除权限。 
◼ 
1.6.2 离线模式-创建安全域：新增离线模式示例。 


## 第 5 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
iv 
手册版本 
适用于产品版本 
更新内容 
⚫ 
修改如下章节： 
◼ 
“第1章 使用前必读”章节，新增在线模式和离线模式
说明。 
◼ 
新增Commandstool命令行离线模式。 
除了如下命令，其它命令均增加offline离线模式，包含描
述及实例。 
- 
2.9 create-file-user 
- 
2.10 update-file-user 
- 
2.32 delete-virtual-server 
- 
2.41 deploy 
- 
2.42 redeploy 
- 
2.43 undeploy 
- 
2.44 enable-app 
- 
2.45 disable-app 
- 
2.48 backup-app 
- 
2.50 list-app 
- 
2.52 create-jms-connection-factory 
- 
2.55 create-jms-destination 
- 
2.58 create-connector-connection-pool 
- 
2.61 create-threadpool 
- 
2.64 create-adapter-adminobject 
- 
2.72 update-web-container-config 
- 
2.80 create-sharedlib 
- 
2.81 delete-sharedlib 
◼ 
新增支持TLSv1.3协议 
“2.16 create-http-listener”章节，enabledProtocols参数，
新增支持TLSv1.3协议。 
◼ 
“ 2.36  
create-jdbc-connection-pool ” 和“ 2.37 
update-jdbc-connection-pool
”
章
节
，
新
增
createCountEveryTime和intervalEveryTime参数及说明。 
◼ 
“2.38 deploy”，新增应用前缀的优先级说明。 
7046A01 
7.0.4.6 
⚫ 新增如下章节： 
◼ 
2.44 enable-app 
◼ 
2.45 disable-app 
⚫ 修改如下章节： 
◼ 
“2.72 update-web-container-config”，新增ecsm、sii、cip、
cua参数。 


## 第 6 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
v 
手册版本 
适用于产品版本 
更新内容 
◼ 
新增initsql参数 
- 
2.36 create-jdbc-connection-pool 
- 
2.37 update-jdbc-connection-pool 
◼ 
新增offline参数 
- 
2.2  change-admin-password 
- 
2.20 update-http-listener 
- 
2.75 set-jvm-arg 
◼ 
realmdigest加密类型新增支持SM2 
- 
2.9 create-file-user 
2.10 update-file-user 
7045A01 
7.0.4.5 
⚫ 新增如下章节： 
◼ 
2.3 config-password 
◼ 
2.13 create-realm-role 
◼ 
2.14  delete-realm-role 
◼ 
2.15 list-realm-role 
◼ 
2.31 update-virtual-server 
◼ 
2.46 show-backup-appdir 
◼ 
2.47 update-backup-appdir 
◼ 
2.48 backup-app 
⚫ 修改如下章节： 
◼ 
增加maxSwallowSize参数 
- 
2.16 create-http-listener 
- 
2.20 update-http-listener 
◼ 
增加vsName参数 
2.49 update-auto-deploy-config 
◼ 
更新关于组的描述 
- 
2.9 create-file-user 
- 
2.10 update-file-user 
- 
2.11 delete-file-user 
- 
2.12 list-file-users 
◼ 
更新实例内容 
- 
2.10 update-file-user 
- 
2.61 create-threadpool 
- 
2.64 create-adapter-adminobject 
⚫ 
“2.72 update-web-container-config”，更改“应用退休时间”
参数。 


## 第 7 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
vi 
手册版本 
适用于产品版本 
更新内容 
7044A01 
7.0.4.4 
⚫ 新增如下章节： 
2.66 update-license 
1.7 审计日志 
⚫ 修改如下章节： 
◼ 
将${TW_HOME}改为${TongWeb_HOME} 
◼ 
在2.26中添加数据源加密参数--isEncrypt 
◼ 
“2.57 update-web-container-config”中增加“--xbe”参数 
◼ 
“2.2 change-admin-password”更新--newpassword密码参数
说明 
◼ 
“2.6 create-file-user”更新--filepassword密码参数说明 
⚫ 
“2.7 update-file-user”更新--filepassword 密码参数说明 
7043A01 
7.0.4.3 
修改如下章节： 
⚫ 在2.6/2.7/2.15中添加新参数--properties 
⚫ 在2.6/2.7中添加新参数--maxHttpHeaderSize  
⚫ 在2.4 create-file-user中更新密码长度及最长使用期限的说明 
⚫ 在2.10及2.11中更新maxPostSize说明 
⚫ 在1.5部署应用示例、2.31deploy、2.32redeploy及2.33undeploy
中删除远程部署内容 
⚫ 在1.2安全认证中添加了修改cli用户初始密码的说明 
⚫ 在1.3基本参数中加入了--secure的参数说明 
⚫ 第2章命令列表中添加create-sharedlib及delete-sharedlib 
⚫ 2.31 deploy中添加--sharedLibNames 
7042A01 
7.0.4.2 
无 
7041A01 
7.0.4.1 
⚫ 统一使用TongWeb用户使用手册模板。 
整合原《TongWeb7 用户手册》附录9 命令行使用说明 


## 第 8 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
vii 
前言 
本文档是TongWeb 产品的用户使用手册之一，详细提供命令行工具Commandstool 的使用说明，基本参
数及所有命令示例。 
 
适合的对象 
本手册主要适用于生产环境中的系统管理员，部分内容同样适用于应用开发人员和应用部署人员。  
本手册假定您已经具备如下技能： 
1. 基本系统管理任务； 
2. 安装软件； 
3. 使用Web浏览器； 
4. 启动数据库服务器； 
5. 在终端窗口中发布命令。 
 
用户使用手册集 
TongWeb 为您提供的用户使用手册集包含的文档有：  
⚫ 000_TongWeb_V7.0用户手册导读：各版本手册集的目录及手册版本说明。 
⚫ 001_TongWeb_V7.0快速使用手册：提供各版本客户快速安装，应用部署，及常用配置的说明。 
⚫ 002_TongWeb_V7.0产品简介及安装指南：提供各版本各平台上的安装启动的步骤。 
⚫ 003_TongWeb_V7.0服务配置指南：提供Web容器、EJB容器、启动参数配置及各项基础服务的配置
说明。 
⚫ 004_TongWeb_V7.0应用管理指南：提供管理控制台对应用进行部署和管理操作的说明。 
⚫ 005_TongWeb_V7.0工具使用指南：提供Eclipse、IDEA、Patch、TongAPM、appclient、pinpoint、
web应用迁移等工具的使用说明。 
⚫ 006_TongWeb_V7.0Commandstool使用指南：提供命令行Commandstool的使用说明，基本参数及所
有命令示例。 
⚫ 007_TongWeb_V7.0与Tivoli集成手册：对JSON整体结构及各监视项的说明。 
⚫ 008_TongWeb_V7.0二次开发接口：TongWeb的JMX、REST、SNMP接口说明。 
⚫ 009_TongWeb_V7.0应用开发手册：提供在TongWeb上开发应用的各类规范说明。 
⚫ 010_TongWeb_V7.0等级保护指南：提供等级保护功能开启后的使用说明。 
⚫ 100_TongWeb _V7.0集群管理指南：详细介绍集群的配置和管理。 
⚫ 200_TongWeb_V7.0用户使用手册-轻量级版：提供轻量级版本客户详细的服务配置及应用管理的说
明。 
 
技术支持 
东方通产品将为您提供全方位的技术支持，您可以通过以下方式获得技术支持：  


## 第 9 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
viii 
网址：www.tongtech.com  
电话：400-650-7088 
邮箱：support@tongtech.com 
 
您在取得技术支持时，请提供如下信息： 
1.  您的姓名  
2.  您的公司信息  
3.  您的联系方式  
4.  操作系统及其版本  
5.  产品版本号  
6.  日志等错误的详细信息 
 
 


## 第 10 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
ix 
目 录 
第1章 使用前必读 ............................................................................................................................................. 1 
1.1 执行方式 .................................................................................................................................................. 1 
1.2 安全认证 .................................................................................................................................................. 2 
1.2.1 设置命令行访问白名单 ................................................................................................................... 2 
1.2.2 用户名和密码 ................................................................................................................................... 2 
1.3 基本参数 .................................................................................................................................................. 4 
1.4 注意事项 .................................................................................................................................................. 5 
1.5 错误提示 .................................................................................................................................................. 5 
1.6 示例说明 .................................................................................................................................................. 6 
1.6.1 在线模式-部署应用 .......................................................................................................................... 6 
1.6.2 离线模式-创建安全域 ...................................................................................................................... 7 
1.7 审计日志 .................................................................................................................................................. 7 
第2章 命令列表 ................................................................................................................................................. 8 
2.1 help ............................................................................................................................................................ 8 
2.2 change-admin-password ............................................................................................................................ 8 
2.3 config-password ....................................................................................................................................... 10 
2.4 list-permissions ......................................................................................................................................... 11 
2.5 set-permissions ........................................................................................................................................ 12 
2.6 create-auth-realm ..................................................................................................................................... 14 
2.7 delete-auth-realm ..................................................................................................................................... 17 
2.8 list-auth-realms ........................................................................................................................................ 18 
2.9 create-file-user ......................................................................................................................................... 19 
2.10 update-file-user ...................................................................................................................................... 21 
2.11 delete-file-user ....................................................................................................................................... 23 
2.12 list-file-users .......................................................................................................................................... 25 
2.13 create-realm-role .................................................................................................................................... 26 
2.14 delete-realm-role .................................................................................................................................... 27 
2.15 list-realm-role ........................................................................................................................................ 29 
2.16 create-session-manager .......................................................................................................................... 30 
2.17 list-session-manager .............................................................................................................................. 31 
2.18 delete-session-manager .......................................................................................................................... 32 
2.19 create-http-listener ................................................................................................................................. 33 
2.20 update-http-listener ................................................................................................................................ 38 


## 第 11 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
x 
2.21 delete-http-listener ................................................................................................................................. 43 
2.22 list-http-listeners .................................................................................................................................... 44 
2.23 start-http-listener .................................................................................................................................... 45 
2.24 stop-http-listener .................................................................................................................................... 46 
2.25 create-ajp-listener .................................................................................................................................. 47 
2.26 delete-ajp-listener .................................................................................................................................. 50 
2.27 list-ajp-listeners...................................................................................................................................... 51 
2.28 start-ajp-listener ..................................................................................................................................... 52 
2.29 stop-ajp-listener ..................................................................................................................................... 54 
2.30 create-virtual-server ............................................................................................................................... 55 
2.31 update-virtual-server .............................................................................................................................. 58 
2.32 delete-virtual-server ............................................................................................................................... 60 
2.33 list-virtual-servers .................................................................................................................................. 61 
2.34 start-virtual-server .................................................................................................................................. 62 
2.35 stop-virtual-server .................................................................................................................................. 64 
2.36 create-jdbc-connection-pool .................................................................................................................. 65 
2.37 update-jdbc-connection-pool ................................................................................................................. 72 
2.38 delete-jdbc-connection-pool .................................................................................................................. 78 
2.39 ping-jdbc-connection-pool ..................................................................................................................... 79 
2.40 list-jdbc-connection-pools ..................................................................................................................... 81 
2.41 deploy .................................................................................................................................................... 82 
2.42 redeploy ................................................................................................................................................. 84 
2.43 undeploy ................................................................................................................................................ 85 
2.44 enable-app .............................................................................................................................................. 87 
2.45 disable-app ............................................................................................................................................. 88 
2.46 show-backup-appdir .............................................................................................................................. 89 
2.47 update-backup-appdir ............................................................................................................................ 90 
2.48 backup-app ............................................................................................................................................. 91 
2.49 update-auto-deploy-config ..................................................................................................................... 92 
2.50 list-apps .................................................................................................................................................. 94 
2.51 list-sys-properties ................................................................................................................................... 95 
2.52 create-jms-connection-factory ............................................................................................................... 96 
2.53 delete-jms-connection-factory ............................................................................................................... 98 
2.54 list-jms-connection-factory .................................................................................................................... 99 
2.55 create-jms-destination .......................................................................................................................... 100 


## 第 12 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
xi 
2.56 delete-jms-destination .......................................................................................................................... 101 
2.57 list-jms-destination .............................................................................................................................. 102 
2.58 create-connector-connection-pool ........................................................................................................ 103 
2.59 delete-connector-connection-pool ........................................................................................................ 105 
2.60 list-connector-connection-pools ........................................................................................................... 107 
2.61 create-threadpool ................................................................................................................................. 108 
2.62 delete-threadpool ................................................................................................................................. 109 
2.63 list-threadpools ..................................................................................................................................... 110 
2.64 create-adapter-adminobject ................................................................................................................... 111 
2.65 delete-adapter-adminobject ................................................................................................................... 113 
2.66 list-adapter-adminobject ....................................................................................................................... 114 
2.67 create-connector-security-map .............................................................................................................. 115 
2.68 delete-connector-security-map .............................................................................................................. 117 
2.69 list-connector-security-maps ................................................................................................................. 118 
2.70 version .................................................................................................................................................. 119 
2.71 web-container-config ........................................................................................................................... 120 
2.72 update-web-container-config ............................................................................................................... 121 
2.73 server-log-config .................................................................................................................................. 124 
2.74 update-server-log-config ...................................................................................................................... 125 
2.75 set-jvm-arg ........................................................................................................................................... 127 
2.76 delete-jvm-arg ...................................................................................................................................... 128 
2.77 set-server-arg ....................................................................................................................................... 129 
2.78 generate-tdg-token ............................................................................................................................... 130 
2.79 delete-server-arg .................................................................................................................................. 131 
2.80 create-sharedlib .................................................................................................................................... 132 
2.81 delete-sharedlib .................................................................................................................................... 134 
2.82 update-license ...................................................................................................................................... 135 
附录A 
术语及缩略语 ................................................................................................................................. 137 


## 第 13 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
1 
第1章 使用前必读 
TongWeb 提供以commandstool 命名的手动部署及管理应用的工具。命令行的启动脚本位于
${TongWeb_HOME}/bin 目录下，有bat（Windows）和sh（Linux/Unix）两个版本。 
Commandstool 支持TongWeb 启动或者不启动的情况下运行，分别为“在线模式”和“离线模式”。 
⚫ 
在线模式： 
Commandstool命令行在TongWeb启动的情况下进行配置。 
⚫ 
离线模式： 
Commandstool命令行在不启动TongWeb的情况下，完成一些基础配置类的操作，进行预配置。 
离线模式是在原有命令行参数的基础上，新增了一个参数“offline”，当该参数值为“true”时，
表示当前命令行的执行方式为离线模式。 
本手册提供commandstool 的使用说明及所有命令的详细列表。 
1.1 执行方式 
Commandstool 命令行工具有直接执行和多级交互式执行两种执行方式，介绍如下。 
⚫ 
直接执行 
进入${TongWeb_HOME}/bin 目录后，直接在命令提示符下输入脚本文件、相应命令及参数即可。
例如： 
Windows：${TongWeb_HOME}/bin>commandstool list-sys-properties 
Linux:   ${TongWeb_HOME}/bin>sh commandstool.sh list-sys-properties 
⚫ 
多级交互式执行 
先启动${TongWeb_HOME}/bin 目录下的commandstool 脚本，进入次级命令提示符
commandstool>。 
之后只需输入相应命令，不用多次执行commandstool 脚本。例如： 
Windows：${TongWeb_HOME}/bin>.\commandstool.bat 
Linux:   ${TongWeb_HOME}/bin>sh commandstool.sh 
commandstool>list-sys-properties 


## 第 14 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
2 
1.2 安全认证 
1.2.1 设置命令行访问白名单 
用户可以通过在“启动参数”或者“${TongWeb_HOME}/bin/external.vmoptions”中配置 
“-Dcommond.ip.whitelist=[IP 正则表达式]”的方式来设置客户端IP 白名单。只有符合此条件的客户端IP
才能访问命令行接口。默认情况下不进行校验，只有在添加了该参数后才会进行检查。 
1.2.2 用户名和密码 
在TongWeb 中，每一次执行命令都需要进行安全认证，安全认证是系统应用资源受保护所需的认证。
执行命令时，需要提供正确的用户名密码才能通过认证，  
Commandstool 用户名和密码如下所示。 
⚫ 
用户名：cli 
⚫ 
初始密码：cli123.com（您可以根据需要进行修改） 
注意： 
首次使用“cli”用户时，需要使用“change-admin-password”修改密码。 
认证方式分为“交互方式”和“直接方式”两种方式。 
⚫ 
交互方式 
可以通过用户名密码的提示来进行认证。 
commandstool>list-sys-properties 
Please enter the admin user name>cli 
Please enter the admin password>cli123.com 
If you are using 'cli' for the first time, please use the 'change-admin-password' command to change 
your password! 
commandstool>change-admin-password --user cli 
Please enter the old admin password>cli123.com 
Please enter the new admin password>Cli123.com 
Please enter the new admin password again>Cli123.com 
Command change-admin-password executed successfully. 


## 第 15 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
3 
commandstool>list-sys-properties 
Please enter the admin user name>cli 
Please enter the admin password>Cli123.com 
************************ 
说明： 
如上所示，如果是首次使用commandstool，需要修改cli 用户的初始密码后才能执行命令。 
⚫ 
直接方式 
直接在输入命令时，提供需认证的用户名与密码文件。 
密码文件需要您通过执行password.sh（或password.bat）脚本，生成密文，并保存的用户密码文件。 
注意： 
如果需要获取某个字符串的加密字符串，必须在目标“${TongWeb_HOME}/bin”目录中执行该脚
本；否则，生成的加密字符串将会不一样，从而导致无法成功解密。 
执行命令时，直接传递生成的密码文件即可。 
例如： 
commandstool>list-sys-properties --user=cli --passwordfile=<passwordfile> 
◼ 
--user 
需要认证的用户名。 
◼ 
--passwordfile 
生成密码文件的操作步骤，如下所示。 
1. 进入“${TongWeb_HOME}/bin”目录。 
2. 
执行password.sh（或password.bat）脚本，生成密文。 
]# sh password.sh Cli123.com 
encrypt 'Cli123.com' :YVqM2THQjUlRIp1F72yuZw== 
其中，“YVqM2THQjUlRIp1F72yuZw==”就是生成后的密文，将该密文放入<passwordfile>
中。 
3. 新建一个无扩展名“passwordfile”的文件，并将“属性名”设置为“AS_ADMIN_password”，
“属性值”为生成的密文，如下所示。 


## 第 16 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
4 
 
4. 在使用create-http-listener 命令时，可以通过--passwordfile 参数传递passwordfile 文件，如下
所示。 
- Linux 下：--passwordfile=${TongWeb_HOME}/bin/passwordfile 
- Windows 下：路径使用“\\”或者“/”，如：--passwordfile=C:\\passwordfile 
1.3 基本参数 
命令行包含一些基本参数，这些参数适用于任何命令。 
例如：启动本地端口为1111 的服务器实例上处于停止状态的test-listener 通道的命令，如下所示。 
commandstool>start-http-listener --port=1111 --secure=false test-listener 
命令行基本参数说明，如下所示。 
⚫ 
--terse：可选，修改命令行日志输出级别，true 为INFO，false 为FINE，默认“false”。 
⚫ 
--echo：可选，将一条完整的命令反馈出来。 
⚫ 
--interactive：可选，是否使用交互方式执行命令。“true”使用交互方式，“false”不使用交互方式。
默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：可选，用于远程连接。若需要连接远程服务器，host 代表需要连接的远程IP 地址。默认
“localhost”。 
注意：命令行中的host 禁止远程连接。 
⚫ 
--port：可选，待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访问服务器。默认
为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文件
“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此参数，则需要
设置为“true”。 
⚫ 
--user：可选，执行命令的用户名。 


## 第 17 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
5 
⚫ 
--password：可选，进行交互认证时认证用户所需的密码。如不填写，则专门进行交互输入。默认
为“cli123.com”。 
⚫ 
--passwordfile：可选，保存用户密码的文件（文件中的属性名必须是AS_ADMIN_password,如：
AS_ADMIN_password=cli123.com） 
⚫ 
--offline：可选，命令行离线模式，默认不开启“false”。支持在不启动TongWeb 的情况下，
进行预配置，完成一些基础配置类操作。 
⚫ 
--help：帮助信息。 
所有的参数都可以--param=value 的格式进行输入，如果参数为boolean 值（布尔值），则可以省略
“=value”，参数的数值为描述属性的默认值。 
若参数的值当中包含空格（如一些文件和地址等作为属性值），或者特殊字符如“&”等符号，需要将
该属性用“”包括起来，命令行才会识别这个值。 
例如：jdbcurl="jdbc:mysql://localhost/tw?useUnicode=true&characterEncoding=GBK"。 
1.4 注意事项 
使用commandstool 命令传递参数时，若该命令携带参数及“目标参数”，“目标参数”必须放在命令
最后，否则系统无法识别，会导致执行命令失败。 
例如：stop-http-listener，目标参数为“httplistener_id”。 
stop-http-listener [--terse=false] [--echo=false] [--interactive=true] [--host=localhost] 
[--port=system_http_port] [--secure=true | -s=true]  [--user=root] [--passwordfile file_name] 
httplistener_id 
⚫ 
正确方式 
./commandstool.sh stop-http-listener --user=cli --passwordfile=/root/pass test-http-listener 
⚫ 
错误方式 
./commandstool.sh stop-http-listener test-http-listener --user=cli --passwordfile=/root/pass 
1.5 错误提示 
当输入错误命令的时候，命令行工具会提示输入错误；如果输入的内容不包含必选参数，命令行工具


## 第 18 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
6 
还会提示哪个参数是必需的。像create-**一类的命令，都需要一个操作数。 
例如：create-http-listener 要创建一个名为test-listener 的通道，则“test-listener”就是这个操作数，如果输
入的命令不包含test-listener 这个操作数，命令行工具也会给出错误提示。 
错误提示如下所示。 
 
1.6 示例说明 
1.6.1 在线模式-部署应用 
使用commandstool 定义的deploy 命令，可以部署Web 应用、EJB 应用及企业应用等。 
Deploy 不支持离线模式，以在线模式举例说明。 
commandstool>deploy --contextroot=ejb3_1_war --precompilejsp=true -- 
applocation=C:\\TongWeb\\samples\\ejb\\ejb3_1_war.war testapp1 
常用参数说明如下。 
⚫ 
--applocation：必选，客户端应用文件的路径（注：windows下路径使用“\\”或者“/”）。 
⚫ 
--defaultvs：虚拟服务器。 
⚫ 
--contextroot：应用前缀。只有在web应用部署时可用。 
⚫ 
--precompilejsp：JSP是否预编译。 
⚫ 
--deployorder：设置部署顺序。 


## 第 19 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
7 
⚫ 
--appdescription：应用描述。 
⚫ 
--delegate：类加载策略，默认是子优先false，如果想配置父优先则设置为true。 
⚫ 
目标参数：必选，应用名称（例如：testapp1/testapp2）。 
1.6.2 离线模式-创建安全域 
使用commandstool 定义的create-auth-realm 命令，创建安全域。 
Create-auth-realm 支持离线模式，如下以离线模式举例说明。 
commandstool> create-auth-realm --realmtype=file --groupfilename=groups.properties 
--userfilename=users.properties --offline=true test-cli-realm 
常用参数说明如下。 
⚫ 
--realmtype：安全域类型，file|sql|ldap|jaas|script|spi，默认为“file”。 
⚫ 
--groupfilename：当安全域类型选择“file”时生效，指定组文件路径，默认为系统默认的组文
件。 
⚫ 
--userfilename：当安全域类型选择“file”时生效，指定用户文件路径，默认为系统默认的用
户文件。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。当使用离线模式时，设置为“true”。 
⚫ 
目标参数：必选，目标参数，安全域名称。名称由数字、字母、下划线和'-'组成，首字符为英文。 
1.7 审计日志 
命令行工具成功执行操作后审计日志写入${TongWeb_HOME}/logs/command-audit-log 文件中。 


## 第 20 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
8 
第2章 命令列表 
以下为所有commandstool 的命令列表。 
如下命令中的实例，均以“交互方式”举例说明。 
2.1 help 
功能说明 
显示所有命令。 
相关参数 
- 
实例 
help 
2.2 change-admin-password 
功能说明 
用于修改管理密码。该命令只能修改位于“cli”组的管理用户。支持离线模式。 
注意： 
⚫ 请先修改命令行默认账号cli的密码，才能操作其他命令。 
⚫ 修改密码时要求5次以内密码不能重复。 
默认此命令为“交互式”命令，提示用户提供旧的和新的管理密码并进行确认。 
若非交互式修改密码，需要设置参数--interactive=false，并且传入参数
--newpassword。 
基本参数 
直接方式，基本参数： 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：可选，用于远程连接。若需要连接远程服务器，host代表需要连接的远程
IP地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 


## 第 21 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
9 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
注意： 
若使用“直接方式”修改管理密码，“passwordfile”为“必选”参数。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
若使用直接方式，请根据需要设置如下参数。 
◼ 
--newpassword：新密码，密码必须由大写字母、小写字母、数字、特殊字符
4种组成。 
◼ 
--accountExpireDates：账号过期时间。 
◼ 
username：必选，目标参数，用户名。 
⚫ 
若使用交互方式，根据提示信息修改密码即可。 
实例 
⚫ 
在线模式 
◼ 
直接方式 
change-admin-password --interactive=false --user cli --newpassword=Cli123.com 
–passwordfile=passwordfile cli 
◼ 
交互方式 
commandstool>change-admin-password --user cli 
Please enter the old admin password>cli123.com 
Please enter the new admin password>Cli123.com 
Please enter the new admin password again>Cli123.com 
⚫ 
离线模式 
change-admin-password --offline=true  --accountExpireDates=90 


## 第 22 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
10 
验证方式 
执行命令list-http-listeners 时，输入用户名cli，密码Cli123.com，可以正确查
看所有的通道。 
2.3 config-password 
功能说明 
修改管理控制台账号的密码。支持离线模式。 
用于修改默认用户security、auditor、thanos 的密码。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为“INFO”，false为“FINE”，默认
“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 


## 第 23 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
11 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--adminuser：必选，用户名。 
⚫ 
--adminoldpassword：必选，旧密码。 
⚫ 
--adminnewpassword：必选，新密码，必须由大写字母、小写字母、数字、特殊
字符4种组成。 
实例 
⚫ 
在线模式 
◼ 
直接方式 
config-password --interactive=false --user=cli 
--passwordfile=passwordfile --adminuser=thanos 
--adminoldpassword=thanos123.com --adminnewpassword=Thanos123.com 
◼ 
交互方式： 
commandstool>config-password --adminuser=thanos 
--adminoldpassword=thanos123.com --adminnewpassword=Thanos123.com 
Please enter the admin user name>cli 
Please enter the admin password>Cli123.com 
Command config-password executed successfully. 
⚫ 
离线模式 
config-password --adminuser=thanos --adminoldpassword=thanos123.com 
--adminnewpassword=AAA123.com --offline=true 
验证方式 
1. 登录TongWeb管理控制台。 
2. 输入用户名“thanos”，密码“Thanos123.com”。 
可以正常访问TongWeb管理控制台。 
2.4 list-permissions 
功能说明 
查看命令权限编码。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”


## 第 24 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
12 
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--adminuser：用户名。 
实例 
⚫ 
在线模式： 
list-permissions --adminuser=clitest1 
⚫ 
离线模式： 
list-permissions --adminuser=clitest1 --offline=true 
2.5 set-permissions 
功能说明 
给命令行用户增加权限、删除权限。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为


## 第 25 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
13 
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--type：设置权限类型，可设置为“add”或者“del”。“add”表示添加权限。
“del”表示删除权限。 
⚫ 
--adminuser：用户名。 
⚫ 
--permissions：权限编码。您可以使用list-permissions命令查询权限编码。多
个权限使用英文逗号分隔。 
实例 
⚫ 
在线模式 
set-permissions --type=add --adminuser=clitest1 --permissions=35,2,6 
⚫ 
离线模式 


## 第 26 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
14 
set-permissions --type=add --adminuser=clitest1 --permissions=35,2,6 
--offline=true 
2.6 create-auth-realm 
功能说明 
创建安全域。若用相同名称创建即是更新。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--realmtype：安全域类型，file|sql|ldap|jaas|script|spi，默认为“file”。 


## 第 27 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
15 
⚫ 
--allrolesmodel：对角色认证的限制级别，strict|authOnly|strictAuthOnly，
默认“strict”。 
⚫ 
--usecontextclassloader：选择类加载方式，true|fale，默认为“true”。 
⚫ 
--digestSaltLength：当安全域类型选择“LDAP”时生效，加强字节长度，默认8
位。 
⚫ 
--digestIterations：当安全域类型选择“LDAP”时生效，迭代加密次数，默认3
次。 
⚫ 
--passLength：当安全域类型选择“LDAP”时生效，密码长度，默认10位。 
⚫ 
--groupfilename：当安全域类型选择“FILE”时生效，指定组文件路径，默认为
系统默认的组文件。 
⚫ 
--userfilename：当安全域类型选择“FILE”时生效，指定用户文件路径，默认
为系统默认的用户文件。 
⚫ 
--usedatasource：当安全域类型选择“SQL”时生效，使用数据源。 
⚫ 
--datasourcename：当安全域类型选择“SQL”时生效，JDBC数据源名称。 
⚫ 
--jdbcurl：当安全域类型选择“SQL”时生效，JDBC的url地址。 
⚫ 
--dbuser：当安全域类型选择“SQL”时生效，数据库用户名。 
⚫ 
--jdbcdriver：当安全域类型选择“SQL”时生效，JDBC驱动名。 
⚫ 
--dbpassword： 当安全域类型选择“SQL”时生效，数据库密码。 
⚫ 
--isEncrypt：当安全域类型选择“SQL”时生效，JDBC密码是否加密，true表示
密码是密文，false表示密码是明文。 
⚫ 
--userselect：当安全域类型选择“SQL”时生效，选择用户sql，默认值为SELECT 
user_name,user_pass FROM users WHERE user_name = ?。 
⚫ 
--groupselect：当安全域类型选择“SQL”时生效，组sql，默认值为SELECT 
user_name,user_pass FROM users WHERE user_name = ?。 
⚫ 
--x509UsernameRetrieverClassName ：X509 证书解析器实现类，默认
com.tongweb.catalina.realm.X509SubjectDnRetriever。 
⚫ 
--lockEnabled：是否使用锁定机制，默认“锁定”。 
⚫ 
--failureCount：允许错误次数，默认5次。 
⚫ 
--lockOutTime：锁定超时，默认“300”秒。 


## 第 28 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
16 
⚫ 
--cacheRemovalWarningTime：最小缓存时间被锁定的用户在缓存中的时间少于此
值，则记录警告日志，默认3600秒。 
⚫ 
--cacheSize：缓存大小，默认1000个。 
⚫ 
--connectionURL：当安全域类型选择“LDAP”时生效，服务器主机名。 
⚫ 
--connectionName：当安全域类型选择“LDAP”时生效，连接ldap服务器的root
域。 
⚫ 
--connectionPassword：当安全域类型选择“LDAP”时生效，服务器密码。 
⚫ 
--userBase：当安全域类型选择“LDAP”时生效，用户基本域名。 
⚫ 
--userName：当安全域类型选择“LDAP”时生效，用户名属性。 
⚫ 
--userPassword：当安全域类型选择“LDAP”时生效，密码属性。 
⚫ 
--roleBase：当安全域类型选择“LDAP”时生效，角色基本属性。 
⚫ 
--roleName：当安全域类型选择“LDAP”时生效，角色名属性。 
⚫ 
--roleSearchUser：当安全域类型选择“LDAP”时生效，角色对应用户属性。 
⚫ 
--loginModuleClassNames：当安全域类型选择“JAAS”时生效，LoginModule名
称。 
⚫ 
--userClassNames：当安全域类型选择“JAAS”时生效，自定义用户principal
实现类。 
⚫ 
--roleClassNames：当安全域类型选择“JAAS”时生效，自定义组principal实现
类。 
⚫ 
--scriptURI：当安全域类型选择“Script”时生效，脚本路径。 
⚫ 
--engineName：当安全域类型选择“Script”时生效，脚本引擎。 
⚫ 
realm_name：必选，目标参数，安全域名称。名称由数字、字母、下划线和'-'
组成，首字符为英文。 
实例 
⚫ 
在线模式 
◼ 
file类型 
create-auth-realm --realmtype=file 
--groupfilename=groups.properties --userfilename=users.properties 
test-cli-realm 
◼ 
jdbc类型 


## 第 29 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
17 
create-auth-realm --realmtype=sql --usedatasource=false 
--jdbcdriver=com.mysql.jdbc.Driver 
--jdbcurl=jdbc:mysql://localhost:3306/test --dbuser=root 
--dbpassword=root --isEncrypt=false test-cli-realm 
⚫ 
离线模式 
◼ 
file类型 
create-auth-realm --realmtype=file 
--groupfilename=groups.properties --userfilename=users.properties 
--offline=true test-cli-realm 
◼ 
sql类型 
create-auth-realm --realmtype=sql --usedatasource=false 
--jdbcdriver=com.mysql.jdbc.Driver 
--jdbcurl=jdbc:mysql://localhost:3306/test --dbuser=root 
--dbpassword=root --isEncrypt=false --offline=true test-cli-realm 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“安全服务”>“安全域管理”，进入安全域管理页面。 
3. 查看test-cli-realm已经创建成功。 
2.7 delete-auth-realm 
功能说明 
删除认证域。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 


## 第 30 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
18 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
realm_name：必选，目标参数，安全域名称。 
实例 
⚫ 
在线模式： 
delete-auth-realm test-cli-realm 
⚫ 
离线模式： 
delete-auth-realm --offline=true test-cli-realm  
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“安全服务”>“安全域管理”，进入安全域管理页面。 
3. 查看test-cli-realm已经被删除。 
2.8 list-auth-realms 
功能说明 
列出身份验证领域。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”


## 第 31 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
19 
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-auth-realms 
⚫ 
离线模式： 
list-auth-realms --offline=true 
2.9 create-file-user 
功能说明 
创建安全域类型为file 的安全域用户。 
注意：不支持等保2.0 的配置项，比如邮箱，双因子开关等。 
不支持离线模式，创建用户涉及user 和安全域的权限验证，离线模式下无法通过。 


## 第 32 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
20 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--groupname：必选，角色名，即用户所属角色，多个可用逗号分隔。 
⚫ 
--filepassword：非必选，密码，必须由大写字母、小写字母、数字、特殊字符
4种组成。 
⚫ 
--realmname：必选，安全域名称。 
⚫ 
--realmdigest：加密类型，包括SM3|MD5|SHA-1|SHA-256|SHA-512|DIGEST|SM2。 
⚫ 
--minAge：密码最短使用期限，范围0-90，默认“0”表示立即生效。 
⚫ 
--maxAge：密码最长使用期限，范围0-90，默认90天。 


## 第 33 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
21 
⚫ 
--passLength：密码长度，范围10~32的整数，默认10位。 
⚫ 
--saltLength：将密码和一些随机数字混合加密，增加强度，加强字节长度，默
认“8”，取值范围“2-32”之间的整数。 
⚫ 
--iterations：迭代多次加密，增加强度，默认3。 
⚫ 
--passExpireSwitch：密码过期开关，开启后，第一次登录和密码过期时需要修
改密码。默认为“开启”。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
⚫ 
user_name：必选，目标参数，安全域用户名称。名称由数字、字母、下划线和
'-'组成，首字符为英文。 
实例 
create-file-user --groupname=test --filepassword=Test124.com --realmname=test-cli-realm 
samantha 
说明： 
1. 
其中--realmname=test-cli-realm这里指定的realmname，必须是在安全域中是已经存
在的。 
2. 
在默认域defaultRealm创建用户，groupname取值为tongweb、security、auditor，分
别对应系统管理员、安全保密员、安全审计员的角色。 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“安全服务”>“安全域管理”，进入安全域管理页面。 
3. 找到安全域名称test-cli-realm。 
4. 单击“管理用户”，进入用户管理页面。 
查看samantha用户已经创建成功，所属角色为“test”。 
2.10 update-file-user 
功能说明 
更新安全域类型为“file”的安全域用户。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”不
使用交互方式。默认为“true”。不设置该参数时，采用默认值。 


## 第 34 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
22 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地址。
默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互输
入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--groupname：必选，角色名，即用户所属角色，多个可用逗号分隔。 
⚫ 
--realmname：必选，安全域名称。 
⚫ 
--oldpassword：必选，输入旧密码才能更新用户信息。 
⚫ 
--filepassword：非必选，密码，必须由大写字母、小写字母、数字、特殊字符4种
组成。密码可不设置，不设置表示不修改密码。若设置该参数，相当于重新设置
密码，要求5次内密码不能重复。 
⚫ 
--realmdigest：加密类型，包括SM3|SM2|MD5|SHA-1|SHA-256|SHA-512|DIGEST。 
⚫ 
--minAge：密码最短使用期限，默认“0”表示立即生效。 
⚫ 
--maxAge：密码最长使用期限，默认“90”天。 
⚫ 
--passLength：密码长度，范围10~32之间的整数，默认10。 
⚫ 
--saltLength：加强字节长度，将密码和一些随机数字混合加密，增加强度，默认8。 
⚫ 
--iterations：迭代多次加密，增加强度，默认3次。 


## 第 35 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
23 
⚫ 
--passExpireSwitch：密码过期开关，开启后，第一登录和密码过期时需要修改密
码。默认为“开启”。 
⚫ 
user_name：必选，目标参数，安全域用户名称。名称由数字、字母、下划线和
'-'组成，首字符为英文。 
实例 
⚫ 
在线模式： 
update-file-user --groupname=test --filepassword=Test125.com 
--realmname=test-cli-realm --realmdigest=MD5 samantha 
说明： 
◼ 
其中--realmname=test-cli-realm这里指定的realmname，必须是在安全域中是已
经存在的。 
◼ 
在默认域defaultRealm创建用户，groupname取值为tongweb、security、auditor，
分别对应系统管理员、安全保密员、安全审计员的角色。 
◼ 
不建议修改defaultRealm域下，默认三个用户的groupname属性。 
⚫ 
离线模式： 
update-file-user --groupname=test --filepassword=Test125.com 
--realmname=test-cli-realm --realmdigest=MD5 --offline=true samantha 
验证方式 
1. 
登录TongWeb管理控制台。 
2. 
左侧导航栏中，选择“安全服务”>“安全域管理”，进入安全域管理页面。 
3. 
找到安全域名称test-cli-realm。 
4. 
单击“管理用户”，进入用户管理页面。 
查看samantha已经被更新。 
2.11 delete-file-user 
功能说明 
删除指定文件安全域用户。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 


## 第 36 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
24 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--realmname：必选，安全域名称。 
⚫ 
user_name：必选，目标参数，安全域用户名称。 
实例 
执行命令前，请保证realmname=test-cli-realm 以及用户Samantha 已经存在。 
⚫ 
在线模式： 
delete-file-user --realmname=test-cli-realm Samantha 
⚫ 
离线模式： 
delete-file-user --realmname=test-cli-realm --offline=true Samantha 
注意： 
默认域defaultRealm 中默认提供的监视管理员monitor，不允许删除。 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“安全服务”>“安全域管理”，进入安全域管理页面。 


## 第 37 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
25 
3. 找到安全域名称test-cli-realm。 
4. 单击“管理用户”，进入用户管理页面。 
查看用户samantha已删除。 
2.12 list-file-users 
功能说明 
列举指定文件类型安全域的用户列表。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 


## 第 38 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
26 
相关参数 
user_name：必选，目标参数，安全域名称。 
实例 
⚫ 
在线模式： 
list-file-users test-cli-realm 
⚫ 
离线模式： 
list-file-users --offline=true test-cli-realm  
2.13 create-realm-role 
功能说明 
创建并管理安全域的角色，包括新增和修改（修改只能修改角色描述）。 
支持离线模式。 
注意：默认安全域下不能创建角色。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互


## 第 39 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
27 
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--realmname：必选，安全域名称。创建安全域角色时，安全域已存在，否则创建
角色会失败。 
⚫ 
--roledescribe：角色描述。 
⚫ 
rolename：必选，目标参数，角色名称，名称由数字、字母、下划线和'-'组成，
首字符为英文。 
实例 
注意： 
该命令执行前，请保证--realmname=test 的安全域已经存在。 
⚫ 
在线模式： 
create-realm-role --realmname=test rolename 
⚫ 
离线模式： 
create-realm-role --realmname=test --offline=true rolename 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“安全服务”>“安全域管理”，进入安全域管理页面。 
3. 找到安全域名称test。 
4. 单击“管理角色”，进入角色管理页面。 
查看rolename已经在列表中。 
2.14 delete-realm-role 
功能说明 
删除指定文件类型安全域的角色。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地


## 第 40 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
28 
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--realmname：必选，安全域名称。 
⚫ 
rolename：必选，目标参数，角色名称。 
实例 
该命令执行前需要保证realmname=test 的安全域存在。 
⚫ 
在线模式： 
delete-realm-role --realmname=test rolename 
⚫ 
离线模式： 
delete-realm-role --realmname=test --offline=true rolename 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“安全服务”>“安全域管理”，进入安全域管理页面。 
3. 找到安全域名称test。 
4. 单击“管理角色”，进入角色管理页面。 
查看rolename角色已被删除。 


## 第 41 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
29 
2.15 list-realm-role 
功能说明 
查看指定文件类型安全域的角色列表。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
realmname：必选，目标参数，安全域名称。 
实例 
◼ 
在线模式： 
list-realm-role realmname 


## 第 42 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
30 
◼ 
离线模式： 
list-realm-role --offline=true realmname 
2.16 create-session-manager 
功能说明 
添加session 管理器。支持离线模式。 
相关参数 
◼ 
--sessionManagerType：session管理器类型，可配置为“memory”、“tdg”或
“redis”分别对应“内存”“TDG”、“Redis”。 
“内存”表示session存储到内存。 
注意：session管理器类型不能为空。 
◼ 
当sessionManagerType=tdg 
➢ 
tongdatagrid-enabled：是否启动TDG，可设置为“true”或“false”。 
➢ 
tongdatagrid_cluster_members：TDG地址。比如：127.0.0.1:5701； 
如果有多个缓存节点要用英文逗号分割，如
127.0.0.1,10.10.4.50:5701,192.168.0.1:5702,… 
➢ 
tongdatagrid_group_name：要连接到的缓存集群组名称，默认值为“dev”，
用于连接到特定的缓存集群。 
➢ 
tongdatagrid_group_password：要连接到的缓存集群组密码，默认值
“dev-pass”，用于连接到特定的缓存集群。 
➢ 
tongdatagrid-asyncwrite：异步写入开关是否开启异步存储会话数据的功
能，默认值为“false”表示不开启。 
➢ 
tongdatagrid_timeout：会话备份超时时间（单位：毫秒），默认值为“500”。 
➢ 
tongdatagrid-stick：是否使用亲和性会话，可设置为“true”或“false”。 
◼ 
当sessionManagerType=redis 
➢ 
redisModeType：redis架构模式，支持单机模式、哨兵模式或集群模式。 
◆ 单机模式：single 
◆ 哨兵模式：sentry 
◆ 集群模式：mult 
➢ 
redisClusterNodes：哨兵模式时填写哨兵节点列表；集群模式时填写整个
集群节点列表。节点列表逗号分隔，如：127.0.0.1:6379,127.0.0.1:6380。 


## 第 43 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
31 
➢ 
redisMasterNodeName：哨兵模式时，主节点名称。 
➢ 
redisClientName：哨兵或者集群模式下，redis客户端名称。 
➢ 
redisHost：单机模式下，redis主机名，如：127.0.0.1。 
➢ 
redisPort：单机模式下，redis端口，默认“6379”。 
➢ 
redisDatabase：单机或哨兵模式下，redis几号数据库，默认“0”号库。 
➢ 
redisPassWord：哨兵或集群模式下，redis密码。 
➢ 
maxRedirects：单机或集群模式下，最大重试次数。 
➢ 
redisConnectionTimeOut：单机、哨兵或集群模式下，redis连接超时时间
（单位：毫秒），默认值为“5000”。 
➢ 
redisSoTimeOut：单机、哨兵或集群模式下，redis响应超时时间（单位：
毫秒），默认值为“5000”。 
⚫ 
--sessionTimeout：session超时时间，单位：分钟。 
⚫ 
manager_name：必选，目标参数，session管理器名称。 
实例 
⚫ 
在线模式 
create-session-manager --sessionManagerType=tdg --tongdatagrid-enabled=true 
--tongdatagrid_cluster_members=127.0.0.1:5701 test 
⚫ 
离线模式 
create-session-manager --sessionManagerType=tdg --tongdatagrid-enabled=true 
--tongdatagrid_cluster_members=127.0.0.1:5701 --offline=true test 
验证方式 
1. 
登录TongWeb管理控制台。 
2. 
左侧导航栏中，选择“Web容器配置”>“session管理”，进入session管理页面。 
3. 
可以查看到创建的session管理器“test”。 
2.17 list-session-manager 
功能说明 
列出存在的session 管理器。支持离线模式。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-session-manager 
⚫ 
离线模式： 


## 第 44 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
32 
list-session-manager --offline=true 
2.18 delete-session-manager 
功能说明 
删除指定session 管理器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”不
使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地址。
默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
session_name：必选，目标参数，session 管理器的名称。 
实例 
执行命令前，请保证session 管理器已经存在，如“test”。 


## 第 45 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
33 
⚫ 
在线模式： 
delete-session-manager test 
⚫ 
离线模式： 
delete- session-manager --offline=true test 
验证方式 
1. 
登录TongWeb管理控制台。 
2. 
左侧导航栏中，选择“WEB容器配置”>“session管理”，进入session管理页面。 
3. 
可以查看到session管理器test已经删除成功。 
 
2.19 create-http-listener 
功能说明 
创建新的HTTP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 


## 第 46 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
34 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--listenerport：必选，指定连接器的监听端口，取值范围为“1-65535”之间的
整数。 
⚫ 
--defaultvs：必选，指定默认的虚拟主机，默认为“server”。 
⚫ 
--listeneraddress：指定连接器的监听地址。默认监听本机所有地址。 
⚫ 
--xpowered：启用后，在响应header中有如“X-Power-By:Servlet/3.0 JSP/2.2”，
默认“false”。 
⚫ 
--redirectport：指定连接器的重定向端口，取值范围为“1-65535”之间的整数，
默认为空。当http通道类型选择为“https”时，不需要配置。 
⚫ 
--backlog：等待队列，默认“100”。取值范围为“1-2147483647” 之间的整数。
开启线程自我调节后，不可配置。 
⚫ 
--maxthreads：最大线程数，连接器可创建的最大线程数。默认200，取值范围为
“1-2147483647” 之间的整数。 
⚫ 
--minsparethreads：初始线程数，默认为“10”，初始线程数不能大于最大线程
数。取值范围为“0-2147483647” 之间的整数。开启线程自我调节后，不可配置。 
⚫ 
--sslalias：SSL证书别名。 
⚫ 
--keystorefile：证书路径，存放服务器证书文件的路径。默认指向服务器conf
目录下的".keystore"文件。默认为“conf/server.keystore”。 
⚫ 
--keystorepass：证书密码。 
⚫ 
--keystoretype：证书类型，默认“JKS”。 
⚫ 
--ssltype：SSL协议类型，选择HTTPS后才设置SSL协议类型，默认“TLS”。支持
“SSL”、“SSLv3”、“TLS”、“TLSv1”、“TLSv1.1”、“TLSv1.2”、“TLSv1.3”、
“GMSSLv1.1”。 
⚫ 
--clientauth：http通道类型选择为“https”时有效，是否使用客户端认证，默
认为“false”。 


## 第 47 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
35 
⚫ 
--truststorefile：开启客户端认证时生效，信任证书路径。默认为
“conf/server.keystore”。 
⚫ 
--truststorepass：开启客户端认证时生效，信任证书密码。 
⚫ 
--truststoretype：开启客户端认证时生效，信任证书类型。默认为“JKS”。 
⚫ 
--securitabled：“false”建立http连接器，“true”则建立https连接器，默
认“false”。 
⚫ 
--ioMode：io模式，有bio、nio、nio2、apr四个参数，默认“nio”。 
⚫ 
--proxyUrl：代理服务器URL，格式为:http(s)://proxyName:proxyPort。 
⚫ 
--connectionTimeout：连接超时，单位毫秒，默认60000ms，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--tcpNoDelay：设置ServerSocket的TCP_NO_DELAY，多数场景下可提高性能，
默认“false”。 
⚫ 
--oomParachute：内存释放空间，单位字节，默认1048576（1MB），取值范围为
“1-2147483647”之间的整数。 
⚫ 
--asyncTimeout：异步超时时间，单位毫秒，默认10000ms，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--keepAliveTimeout：请求超时时间，单位毫秒，默认60000ms，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--maxKeepAliveRequests ：最大长连接请求数，默认100 ，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--maxConnections：最大连接数，默认10000，取值范围为“1-2147483647”之间
的整数。 
⚫ 
--processorCache：处理器缓存数量，默认200，取值范围为“-1-2147483647”
之间的整数。 
⚫ 
--maxParameterCount：最大参数个数，默认10000，取值范围为“1-2147483647”
之间的整数。 
⚫ 
--selfTuned：线程池自调节，默认false，若开启，通道线程池将使用自调节线
程池。 
⚫ 
--threadPriority：线程优先级，1-10正整数，默认5。 


## 第 48 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
36 
⚫ 
--compression：压缩属性，on/force/off，默认为“on”，压缩文本数据，force
表示强制压缩，off表示不使用压缩。 
⚫ 
--compressableMimeType：压缩时需要用到的MIME类型，默认为text/html、
text/xml、text/plain。 
⚫ 
--compressionMinSize：压缩内容最小值，单位KB，默认2048kb，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--noCompressionUserAgents：排除的浏览器，正则表达式，用于匹配user-agent 
Header指定哪些HTTP clients不使用compression。 
⚫ 
--notAllowHTTPMethods：禁用HTTP请求方法，默认为：TRACE、OPTIONS、HEAD、
CONNECT、DELETE、PUT。 
⚫ 
--maxPostSize：请求最大字节数，默认2MB，-1表示没有限制，取值范围为
“-1-2147483647” 的整数。 
⚫ 
--maxSwallowSize：可吞下的请求正文的最大数量，默认2MB，-1表示没有限制，
取值范围为“-1-2147483647” 的整数。 
⚫ 
--connectionUploadTimeout：上传超时的时间，单位毫秒。 
⚫ 
--disableUploadTimeout：是否开启上传超时，默认false。 
⚫ 
--uriEncoding：URL编码格式，用于解码URI字符的编码格式，默认GBK，可选择
UTF-8、ISO-8859-1、GB2312、GB18030、Big5、HZ、GBK、EUC-JP、ISO-202-JP、
Shift-JIS、ISO-8859-2。 
⚫ 
--parseBodyMethods：用于rest风格，默认支持GET/POST，可选择GET、POST、PUT、
DELETE。 
⚫ 
--useBodyEncodingForUri：uri处理，默认false，如果ContentType中指定了编
码规范，则可以不使用URL编码格式。 
⚫ 
--useIpvHosts：虚拟主机，true/false，基于IP的虚拟主机。默认为false。 
⚫ 
--enableLookups：DNS反向查找，默认false。 
⚫ 
--refererHeaderCheck：referer头验证，默认false。开启验证HTTP Rererer请
求头，不被允许的Referer请求将被禁止。 
⚫ 
--allowRefererHosts：开启Referer头验证时，允许的主机名称。 
⚫ 
--allowRefererIps：开启Referer头验证时，允许的ip地址。 


## 第 49 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
37 
⚫ 
--enableRC4：是否开启RC4加密算法，默认false，不开启。 
⚫ 
--ciphers：指定加密算法，用逗号分隔。 
⚫ 
--enabledProtocols：http通道类型选择为“https”时有效。启动协议参数，默
认不传，取值控制在SSLv3、TLSv1、TLSv1.1、TLSv1.2、TLSv1.3。 
注意： 
若使用TLSv1.3,Java环境要求为JDK1.8.0_261及以上版本。 
⚫ 
--opensslEnabled：是否启用openSSL，默认“true”。 
⚫ 
--http2Enabled：是否启用Http2，默认false。 
⚫ 
--maxHttpHeaderSize：请求与请求头最大值，默认8192bytes。 
⚫ 
--properties：其它Property属性。 
用法：--properties=key1:value1;key2:value2。 
⚫ 
--gmEnabled：开启国密认证，默认为“false”。 
注意： 
◼ 
若启用国密认证，Java环境要求为JDK8及以上版本。 
◼ 
若在JDK17环境下，需要额外添加如下启动参数。 
--add-opens=java.base/sun.security.rsa=ALL-UNNAMED 
--add-opens=java.base/sun.security.util=ALL-UNNAMED 
--add-opens=java.base/sun.security.jca=ALL-UNNAMED 
⚫ 
--gmEncFile：开启国密认证时生效，加密证书路径，默认为
“conf/EncrytionKey.p12”。 
⚫ 
--gmEncPass：开启国密认证时生效，加密证书密码。 
⚫ 
listener_id：必选，目标参数，HTTP侦听器名称。 
实例 
⚫ 
在线模式： 
create-http-listener --listeneraddress=0.0.0.0 --securitabled=false 
--listenerport=7272 --defaultvs=server test-listener 
⚫ 
离线模式： 
create-http-listener --listeneraddress=0.0.0.0 --securitabled=false 
--listenerport=7273 --defaultvs=server --offline=true xy-listener 
验证方式 
1. 登录TongWeb管理控制台。 


## 第 50 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
38 
2. 左侧导航栏中，选择“Web容器配置”>“HTTP通道管理”，进入HTTP通道页面。 
3. 可查看到test-listener已经创建成功。 
2.20 update-http-listener 
功能说明 
更新HTTP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--listenerport：必选，指定连接器的监听端口，取值范围为“1-65535”之间的


## 第 51 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
39 
整数。 
⚫ 
--defaultvs：必选，指定默认的虚拟主机，默认为“server”。 
⚫ 
--listeneraddress：指定连接器的监听地址。默认监听本机所有地址。 
⚫ 
--xpowered：启用后，在响应header中有如“X-Power-By:Servlet/3.0 JSP/2.2”，
默认“false”。 
⚫ 
--redirectport：指定连接器的重定向端口，取值范围为“1-65535”之间的整数，
默认为空。当http通道类型选择为“https”时，不需要配置。 
⚫ 
--backlog：等待队列，默认“100”。取值范围为“1-2147483647” 之间的整数。
开启线程自我调节后，不可配置。 
⚫ 
--maxthreads：最大线程数，连接器可创建的最大线程数。默认200，取值范围为
“1-2147483647” 之间的整数。 
⚫ 
--minsparethreads：初始线程数，默认为“10”，初始线程数不能大于最大线程
数。取值范围为“0-2147483647” 之间的整数。开启线程自我调节后，不可配置。 
⚫ 
--sslalias：SSL证书别名。 
⚫ 
--keystorefile：证书路径，存放服务器证书文件的路径。默认指向服务器conf
目录下的".keystore"文件。默认为“conf/server.keystore”。 
⚫ 
--keystorepass：证书密码。 
⚫ 
--keystoretype：证书类型，默认“JKS”。 
⚫ 
--ssltype：SSL协议类型，选择HTTPS后才设置SSL协议类型，默认“TLS”。支持
“SSL”、“SSLv3”、“TLS”、“TLSv1”、“TLSv1.1”、“TLSv1.2”、“TLSv1.3”、
“GMSSLv1.1”。 
⚫ 
--clientauth：http通道类型选择为“https”时有效，，支持“true”、“false”、
“want”客户端数字证书认证方式，默认为“false”。 
◼ 
true：强制双向SSL验证，必须验证客户端证书。 
◼ 
false：单向SSL验证。 
◼ 
want：可以验证客户端证书，有客户端证书就验证，没有客户端证书时系统不
会报错。 
⚫ 
--truststorefile：开启客户端认证时生效，信任证书路径。默认为
“conf/server.keystore”。 


## 第 52 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
40 
⚫ 
--truststorepass：开启客户端认证时生效，信任证书密码。 
⚫ 
--truststoretype：开启客户端认证时生效，信任证书类型。默认为“JKS”。 
⚫ 
--securitabled：“false”建立http连接器，“true”则建立https连接器，默
认“false”。 
⚫ 
--ioMode：io模式，有bio、nio、nio2、apr四个参数，默认“nio”。 
⚫ 
--proxyUrl：代理服务器URL，格式为:http(s)://proxyName:proxyPort。 
⚫ 
--connectionTimeout：连接超时，单位毫秒，默认60000ms，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--tcpNoDelay：设置ServerSocket的TCP_NO_DELAY，多数场景下可提高性能，默
认“false”。 
⚫ 
--oomParachute：内存释放空间，单位字节，默认1048576（1MB），取值范围为
“1-2147483647”之间的整数。 
⚫ 
--asyncTimeout ：异步超时时间，单位毫秒，默认10000ms ，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--keepAliveTimeout：请求超时时间，单位毫秒，默认60000ms，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--maxKeepAliveRequests ：最大长连接请求数，默认100 ，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--maxConnections：最大连接数，默认10000，取值范围为“1-2147483647”之间
的整数。 
⚫ 
--processorCache：处理器缓存数量，默认200，取值范围为“-1-2147483647”
之间的整数。 
⚫ 
--maxParameterCount：最大参数个数，默认10000，取值范围为“1-2147483647”
之间的整数。 
⚫ 
--selfTuned：线程池自调节，默认false，若开启，通道线程池将使用自调节线
程池。 
⚫ 
--threadPriority：线程优先级，1-10正整数，默认5。 
⚫ 
--compression：压缩属性，on/force/off，默认为“on”，压缩文本数据，force
表示强制压缩，off表示不使用压缩。 


## 第 53 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
41 
⚫ 
--compressableMimeType：压缩时需要用到的MIME类型，默认为text/html、
text/xml、text/plain。 
⚫ 
--compressionMinSize：压缩内容最小值，单位KB，默认2048kb，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--noCompressionUserAgents：排除的浏览器，正则表达式，用于匹配user-agent 
Header指定哪些HTTP clients不使用compression。 
⚫ 
--notAllowHTTPMethods：禁用HTTP请求方法，默认为：TRACE、OPTIONS、HEAD、
CONNECT、DELETE、PUT。 
⚫ 
--maxPostSize：请求最大字节数，默认2MB，-1表示没有限制，取值范围为
“-1-2147483647” 的整数。 
⚫ 
--maxSwallowSize：可吞下的请求正文的最大数量，默认2MB，-1表示没有限制，
取值范围为“-1-2147483647” 的整数。 
⚫ 
--connectionUploadTimeout：上传超时的时间，单位毫秒。 
⚫ 
--disableUploadTimeout：是否开启上传超时，默认false。 
⚫ 
--uriEncoding：URL编码格式，用于解码URI字符的编码格式，默认GBK，可选择
UTF-8、ISO-8859-1、GB2312、GB18030、Big5、HZ、GBK、EUC-JP、ISO-202-JP、
Shift-JIS、ISO-8859-2。 
⚫ 
--parseBodyMethods：用于rest风格，默认支持GET/POST，可选择GET、POST、PUT、
DELETE。 
⚫ 
--useBodyEncodingForUri：uri处理，默认false，如果ContentType中指定了编
码规范，则可以不使用URL编码格式。 
⚫ 
--useIpvHosts：虚拟主机，true/false，基于IP的虚拟主机。默认为false。 
⚫ 
--enableLookups：DNS反向查找，默认false。 
⚫ 
--refererHeaderCheck：referer头验证，默认false。开启验证HTTP Rererer请
求头，不被允许的Referer请求将被禁止。 
⚫ 
--allowRefererHosts：开启Referer头验证时，允许的主机名称。 
⚫ 
--allowRefererIps：开启Referer头验证时，允许的ip地址。 
⚫ 
--enableRC4：是否开启RC4加密算法，默认false，不开启。 
⚫ 
--ciphers：指定加密算法，用逗号分隔。 


## 第 54 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
42 
⚫ 
--enabledProtocols：http通道类型选择为“https”时有效。启动协议参数，默
认不传，取值控制在SSLv3、TLSv1、TLSv1.1、TLSv1.2、TLSv1.3。 
注意： 
若使用TLSv1.3,Java环境要求为JDK1.8.0_261及以上版本。 
⚫ 
--opensslEnabled：是否启用openSSL，默认“true”。 
⚫ 
--http2Enabled：是否启用Http2，默认false。 
⚫ 
--maxHttpHeaderSize：请求与请求头最大值，默认8192bytes。 
⚫ 
--properties：其它Property属性。 
用法：--properties=key1:value1;key2:value2。 
⚫ 
--gmEnabled：开启国密认证，默认为“false”。 
注意： 
◼ 
启动国密认证，JDK要求JDK8-JDK11版本。 
◼ 
若启用国密认证，Java环境要求为JDK8及以上版本。 
若在JDK17环境下，需要额外添加如下启动参数。 
--add-opens=java.base/sun.security.rsa=ALL-UNNAMED 
--add-opens=java.base/sun.security.util=ALL-UNNAMED 
--add-opens=java.base/sun.security.jca=ALL-UNNAMED 
⚫ 
--gmEncFile：开启国密认证时生效，加密证书路径，默认为
“conf/EncrytionKey.p12”。 
⚫ 
--gmEncPass：开启国密认证时生效，加密证书密码。 
⚫ 
listener_id：必选，目标参数，HTTP侦听器名称。 
实例 
⚫ 
在线模式： 
update-http-listener--listeneraddress=0.0.0.0 --securitabled=false 
--listenerport=7273--defaultvs=server test-listener 
⚫ 
离线模式： 
update-http-listener--listeneraddress=0.0.0.0 
--securitabled=false 
--listenerport=7273--defaultvs=server --offline=true test-listener 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“HTTP通道管理”，进入HTTP通道页面。 


## 第 55 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
43 
3. 可查看到test-listener属性修改成功。 
2.21 delete-http-listener 
功能说明 
删除指定的HTTP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
httplistener_id，必选，目标参数，HTTP 侦听器名称。 
实例 
执行命令前，请保证test-listener 已经存在。 


## 第 56 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
44 
⚫ 
在线模式： 
delete-http-listener test-listener 
⚫ 
离线模式： 
delete-http-listener --offline=true test-listener 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“HTTP通道管理”，进入HTTP通道页面。 
4. 可查看到test-listener已经被删除。 
2.22 list-http-listeners 
功能说明 
列出现有HTTP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互


## 第 57 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
45 
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-http-listeners 
⚫ 
离线模式： 
list-http-listeners --offline=true 
2.23 start-http-listener 
功能说明 
启动指定的HTTP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 


## 第 58 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
46 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
httplistener_id：必选，目标参数，HTTP 侦听器名称。 
实例 
执行命令前，请保证test-listener 已经存在。 
⚫ 
在线模式： 
start-http-listener test-listener 
⚫ 
离线模式： 
start-http-listener --offline=true test-listener 
验证方式 
4. 
登录TongWeb管理控制台。 
5. 
左侧导航栏中，选择“Web容器配置”>“HTTP通道管理”，进入HTTP通道页面。 
6. 
可查看到test-listener启动成功。 
2.24 stop-http-listener 
功能说明 
停止指定的HTTP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 


## 第 59 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
47 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
httplistener_id：必选，目标参数，HTTP 侦听器名称。 
实例 
执行命令前，请保证test-listener 已经存在。 
⚫ 
在线模式： 
stop-http-listener test-listener 
⚫ 
离线模式： 
stop-http-listener --offline=true test-listener 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“HTTP通道管理”，进入HTTP通道页面。 
3. 可查看到test-listener已经被停止。 
2.25 create-ajp-listener 
功能说明 
添加新的AJP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 


## 第 60 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
48 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此
参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--listenerport：必选，指定连接器的监听端口。 
⚫ 
--requireSecret：必选，ajp协议密码。 
⚫ 
--listeneraddress：指定连接器的监听地址。默认监听本机所有地址。 
⚫ 
--xpowered：X-Powered-By，启用后，在响应header中有如，X-Powered-By：
Servlet/3.0 JSP/2.2，默认为“false”。 
⚫ 
--maxthreads：最大线程数，连接器可创建的最大线程数，默认为200，取值范围
为“1-2147483647” 之间的整数。 
⚫ 
--minsparethreads：初始线程数，也是最小备用线程，默认10，取值范围为
“0-2147483647” 之间的整数。 
⚫ 
--backlog：等待队列，默认100，取值范围为“1-2147483647” 之间的整数。 
⚫ 
--ioMode：io模式，bio、nio、nio2、apr，默认为“nio”。 


## 第 61 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
49 
⚫ 
--proxyUrl：代理服务器URL，代理服务器的url，格式
为:http(s)://proxyName:proxyPort。 
⚫ 
--connectionTimeout：连接超时，socket超时（网络连接超时），默认60000ms，
以毫秒为单位。取值范围为“-1”或者“1-2147483647”之间的整数。 
⚫ 
--tcpNoDelay：设置ServerSocket的TCP_NO_DELAY属性，属性值true/false。默
认为“true”。 
⚫ 
--asyncTimeout：异步超时时间，单位毫秒，默认值10000ms。servlet3.0新特性，
支持servlet的异步处理。取值范围为“1-2147483647” 之间的整数。 
⚫ 
--keepAliveTimeout：请求超时时间，keep-alive下的超时时间，默认60000ms，
单位为毫秒。在这个时间内没有新的请求，则断开连接。取值范围为
“1-2147483647” 之间的整数。 
⚫ 
--maxConnections：最大连接数，默认10000，取值范围为“1-2147483647”之间
的整数。 
⚫ 
--processorCache：处理器缓存数量，默认“200”。协议处理器通过缓存处理器
对象来提高性能，表示有多少对象被缓存，如果为-1则无限制。取值范围为
“-1-2147483647” 之间的整数。 
⚫ 
--selfTuned：线程池自调节，属性true/false，默认为“false”。 
⚫ 
--threadPriority：线程优先级，输入1-10正整数，默认为“5”。 
⚫ 
--notAllowHTTPMethods：禁用HTTP请求方法，默认为：OPTIONS、TRACE。 
⚫ 
--maxPostSize：请求最大字节数，默认2MB，-1表示没有限制，取值范围为
“-1-2147483647” 的整数。 
⚫ 
--maxParameterCount：最大参数个数，默认10000，取值范围为“1-2147483647”
之间的整数。 
⚫ 
--uriEncoding：URL编码格式，用于解码URI字符的编码格式，默认“GBK”，可
选择UTF-8、ISO-8859-1、GB2312、GB18030、Big5、HZ、GBK、EUC-JP、ISO-202-JP、
Shift-JIS、ISO-8859-2。 
⚫ 
--parseBodyMethods：用于rest风格，默认支持“GET”、“POST”。可选择GET、
POST、PUT、DELETE。 
⚫ 
--useBodyEncodingForUri：uri处理，默认为“false”。如果ContentType中指


## 第 62 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
50 
定了编码规范，则可以不使用URL编码格式。 
⚫ 
--useIpvHosts：虚拟主机，true/false，默认为“false”。基于IP的虚拟主机。 
⚫ 
--enableLookups：DNS反向查找，true/false，默认为“false”。 
⚫ 
--refererHeaderCheck：referer头验证，默认“false”。开启验证HTTP Rererer
请求头，不被允许的Referer请求将被禁止。 
⚫ 
--allowRefererHosts：开启Referer头验证时，允许的主机名称。 
⚫ 
--allowRefererIps：开启Referer头验证时，允许的ip地址。 
⚫ 
listener_id：必选，目标参数，AJP通道名称。名称由数字、字母、下划线或者
“-”组成，首字母为英文。 
实例 
⚫ 
在线模式： 
create-ajp-listener --listeneraddress=0.0.0.0 --listenerport=8383 
--requireSecret=ajp test-ajp-listener 
⚫ 
离线模式： 
create-ajp-listener --listeneraddress=0.0.0.0 --listenerport=8383 
--requireSecret=ajp --offline=true xy-ajp-listener 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“AJP通道管理”，进入HTTP通道页面。 
3. 可查看到test-ajp-listener已经创建成功。 
2.26 delete-ajp-listener 
功能说明 
删除指定的AJP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地
址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 


## 第 63 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
51 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访
问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
ajplistener_id：必选，目标参数，AJP 侦听器名称。 
实例 
执行命令前，请保证test-ajp-listener 已经存在。 
⚫ 
在线模式： 
delete-ajp-listener test-ajp-listener 
⚫ 
离线模式： 
delete-ajp-listener --offline=true test-ajp-listener 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“AJP通道管理”，进入HTTP通道页面。 
3. 可查看到test-ajp-listener已经被删除。 
2.27 list-ajp-listeners 
功能说明 
列出现有AJP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为


## 第 64 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
52 
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置
文件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-ajp-listeners 
⚫ 
离线模式： 
list-ajp-listeners  --offline=true 
2.28 start-ajp-listener 
功能说明 
启动指定的AJP 侦听器。支持离线模式。 


## 第 65 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
53 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
ajplistener_id：必选，目标参数，AJP 侦听器名称。 
实例 
执行命令前，请保证test-ajp-listener 已经存在。 
⚫ 
在线模式： 
start-ajp-listener test-ajp-listener 
⚫ 
离线模式： 
start-ajp-listener --offline=true xy-ajp-listener 


## 第 66 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
54 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“AJP通道管理”，进入AJP通道页面。 
3. 可以查看到test-ajp-listener已经被启动。 
2.29 stop-ajp-listener 
功能说明 
启动指定的AJP 侦听器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 


## 第 67 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
55 
相关参数 
ajplistener_id：必选，目标参数，AJP 侦听器名称。 
实例 
执行命令前，请保证test-ajp-listener 已经存在。 
⚫ 
在线模式： 
stop-ajp-listener test-ajp-listener 
⚫ 
离线模式： 
stop-ajp-listener --offline=true test-ajp-listener 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“AJP通道管理”，进入AJP通道页面。 
3. 可以查看到test-ajp-listener已经被停止。 
2.30 create-virtual-server 
功能说明 
添加新的虚拟主机。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 


## 第 68 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
56 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--listeners：与虚拟主机关联的通道列表，多个通道使用英文逗号分隔。 
⚫ 
--hostalias：虚拟主机别名，虚拟主机别名为ip或者域名或者由数字、字母、
下划线组成，首字母为英文，多个名称可用逗号分割。虚拟主机别名不能与虚
拟主机名相同。 
⚫ 
--accesslog：“true”表示开启访问日志，默认为“false”，属性值true/false。 
⚫ 
--accesslogDir：开启访问日志后有效，访问日志目录。默认为“logs/access”。 
⚫ 
--addValve：自定义Valve。自定义的Valve会添加到虚拟主机的valve链里。访
问应用时执行自定义的操作。 
⚫ 
--remoteFilterEnabled：是否开启远程过滤。默认为“false”。true表示开
启，false表示不开启。 
⚫ 
--ssoEnabled：是否开启SSO。默认为“false”。true表示开启，false表示不
开启。 
⚫ 
--allowAddr：开启远程过滤后有效，允许的IP地址，正则表达式或者具体的ip
地址。 
⚫ 
--denyAddr：开启远程过滤后有效，禁止的IP地址，正则表达式或者具体的ip
地址。 
⚫ 
--allowHost：开启远程过滤后有效，允许的主机名，正则表达式或者具体的主
机名称。 
⚫ 
--denyHost：开启远程过滤后有效，禁止的主机名，正则表达式或者具体的主
机名称。 
⚫ 
--filterHostType：开启远程过滤后有效，远程过滤开启主机名过滤，值为allow
或者deny，默认为“allow”。与“--allowHost”参数成对配置使用。 
⚫ 
--filterAddrType：开启远程过滤后有效，远程过滤开启IP过滤，值为allow或
者deny，默认为“allow”。与“—allowAddr”参数成对配置使用。 


## 第 69 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
57 
⚫ 
--ltpaEnabled：是否开启ltpa，默认为“false”，“true”表示开启，“false”
表示不开启。 
⚫ 
--cookieName：ltpacookie名称。 
⚫ 
--desKey：3DESKey，从WebSphere中导出的秘钥文件中的3DESKey，加密cookie
的密钥。 
⚫ 
--privateKey：从WebSphere中导出的秘钥文件中的PrivateKey，私钥，对cookie
签名。 
⚫ 
--publicKey：从WebSphere中导出的秘钥文件中的PublicKey，公钥，验证cookie
签。 
⚫ 
--ltpaPassword：从WebSphere中导出的密钥时设定的密码，解密3DESKey和私
钥的密码。 
⚫ 
--cookieDomain：cookie的作用域。 
⚫ 
--expireTime：cookie失效时间，cookie过期时间，单位为：秒，默认1800秒。
取值范围为“1-2147483647” 之间的整数。 
⚫ 
--properties：其它Property属性。 
用法：--properties=key1:value1;key2:value2。 
⚫ 
virtual_server_id：必选，目标参数，虚拟机名称。允许的主机名称由字母、
数字、下划线、"-"组成。 
实例 
⚫ 
在线模式： 
create-virtual-server --hostalias=jmcom 
--listeners=tong-http-listener test-virtual-host 
⚫ 
离线模式： 
create-virtual-server --hostalias=jmcom 
--listeners=tong-http-listener --offline=true test-virtual-host 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“虚拟主机管理”，进入虚拟主机管理
页面。 
3. 
可以查看到test-virtual-host已经创建成功。 


## 第 70 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
58 
2.31 update-virtual-server 
功能说明 
修改虚拟主机。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”，默认为“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--listeners：与虚拟主机关联的通道列表，多个通道使用英文逗号分隔。 
⚫ 
--hostalias：虚拟主机别名，虚拟主机别名为ip或者域名或者由数字、字母、
下划线组成，首字母为英文，多个名称可用逗号分割。虚拟主机别名不能与虚
拟主机名相同。 


## 第 71 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
59 
⚫ 
--accesslog：“true”表示开启访问日志，默认为“false”，属性值true/false。 
⚫ 
--accesslogDir：开启访问日志后有效，访问日志目录。默认为“logs/access”。 
⚫ 
--addValve：自定义Valve。自定义的Valve会添加到虚拟主机的valve链里。访
问应用时执行自定义的操作。 
⚫ 
--remoteFilterEnabled：是否开启远程过滤。默认为“false”。 
⚫ 
--ssoEnabled：是否开启SSO。默认为“false”。true表示开启，false表示不
开启。 
⚫ 
--allowAddr：开启远程过滤后有效，允许的IP地址，正则表达式或者具体的ip
地址。 
⚫ 
--denyAddr：开启远程过滤后有效，禁止的IP地址，正则表达式或者具体的ip
地址。 
⚫ 
--allowHost：开启远程过滤后有效，允许的主机名，正则表达式或者具体的主
机名称。 
⚫ 
--denyHost：开启远程过滤后有效，禁止的主机名，正则表达式或者具体的主
机名称。 
⚫ 
--filterHostType：开启远程过滤后有效，远程过滤开启主机名过滤，值为allow
或者deny，默认为“allow”。与“--allowHost”参数成对配置。 
⚫ 
--filterAddrType：开启远程过滤后有效，远程过滤开启IP过滤，值为allow或
者deny，默认为“allow”。与“—allowAddr”参数成对配置。 
⚫ 
--ltpaEnabled：是否开启ltpa，默认为“false”，“true”表示开启，“false”
表示不开启。 
⚫ 
--cookieName：ltpacookie名称。 
⚫ 
--desKey：3DESKey，从WebSphere中导出的秘钥文件中的3DESKey，加密cookie
的密钥。 
⚫ 
--privateKey：从WebSphere中导出的秘钥文件中的PrivateKey，私钥，对cookie
签名。 
⚫ 
--publicKey：从WebSphere中导出的秘钥文件中的PublicKey，公钥，验证cookie
签。 
⚫ 
--ltpaPassword：从WebSphere中导出的密钥时设定的密码，解密3DESKey和私


## 第 72 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
60 
钥的密码。 
⚫ 
--cookieDomain：cookie的作用域。 
⚫ 
--expireTime：cookie失效时间，cookie过期时间，单位为：秒，默认1800秒。
取值范围为“1-2147483647” 之间的整数。 
⚫ 
--properties：其它Property属性。 
用法：--properties=key1:value1;key2:value2。 
⚫ 
virtual_server_id：必选，目标参数，虚拟机名称。允许的主机名称由字母、
数字、下划线、"-"组成。 
实例 
⚫ 
在线模式： 
update-virtual-server --hostalias=testcom --accesslog=true 
test-virtual-host 
⚫ 
离线模式： 
update-virtual-server --hostalias=testcom --accesslog=true 
--offline=true test-virtual-host 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“虚拟主机管理”，进入虚拟主机管理
页面。 
3. 可以查看到test-virtual-host已经修改成功。 
2.32 delete-virtual-server 
功能说明 
删除指定的虚拟主机。 
不支持离线模式。 
删除虚拟机需要查询关联的app，依赖内存中的运行时数据，所以离线模式无法删除。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP


## 第 73 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
61 
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
virtual_server_id：必选，目标参数，虚拟机名称。 
实例 
delete-virtual-server test-virtual-host 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“虚拟主机管理”，进入虚拟主机管理
页面。 
3. 可以查看到test-virtual-host已经被删除。 
2.33 list-virtual-servers 
功能说明 
列出存在的虚拟服务器。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”


## 第 74 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
62 
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-virtual-servers 
⚫ 
离线模式： 
list-virtual-servers  --offline=true 
2.34 start-virtual-server 
功能说明 
启动指定的虚拟主机。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为


## 第 75 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
63 
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
virtual_server_id：必选，目标参数，虚拟机名称。 
实例 
执行命令前，请保证test-virtual-host 已经存在。 
⚫ 
在线模式： 
start-virtual-server test-virtual-host 
⚫ 
离线模式： 
start-virtual-server  --offline=true test-virtual-host 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“虚拟主机管理”，进入虚拟主机管理


## 第 76 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
64 
页面。 
3. 可以查看到test-virtual-host已经被启动。 
2.35 stop-virtual-server 
功能说明 
停止指定的虚拟主机。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
virtual_server_id：必选，目标参数，虚拟机名称。 


## 第 77 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
65 
实例 
执行命令前，请保证test-virtual-host 已经存在。 
⚫ 
在线模式： 
stop-virtual-server test-virtual-host 
⚫ 
离线模式： 
stop-virtual-server  --offline=true test-virtual-host 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“Web容器配置”>“虚拟主机管理”，进入虚拟主机管理
页面。 
3. 可以查看到test-virtual-host已经被停止。 
2.36 create-jdbc-connection-pool 
功能说明 
注册具有指定JDBC 连接池名称的JDBC 连接池。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为“true”
或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”不使用
交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地址。
默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访问服
务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此参
数，则需要设置为“true”。 


## 第 78 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
66 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--jdbcdriver：必选，选择数据库驱动类名。 
您可以设置为： 
◼ 
oracle.jdbc.driver.OracleDriver 
◼ 
com.mysql.jdbc.Driver 
◼ 
com.mysql.cj.jdbc.Driver 
◼ 
com.sybase.jdbc3.jdbc.SybDriver 
◼ 
dm.jdbc.driver.DmDriver 
◼ 
com.kingbase.Driver 
◼ 
com.kingbase8.Driver 
◼ 
com.oscar.Driver 
◼ 
org.hsqldb.jdbcDriver 
◼ 
com.sybase.jdbc.SybDriver 
◼ 
net.sourceforge.jtds.jdbc.Driver 
◼ 
org.hsqldb.jdbcDriver 
◼ 
org.postgresql.Driver 
◼ 
oracle.jdbc.driver.OracleDriver 
◼ 
org.gjt.mm.mysql.Driver 
◼ 
com.microsoft.jdbc.sqlserver.SQLServerDriver 
◼ 
net.sourceforge.jtds.jdbc.Driver 
◼ 
com.microsoft.sqlserver.jdbc.SQLServerDriver 
◼ 
org.apache.derby.jdbc.ClientDriver 
◼ 
org.apache.derby.jdbc.EmbeddedDriver 
◼ 
com.informix.jdbc.IfxDriver 


## 第 79 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
67 
◼ 
COM.ibm.db2.jdbc.net.DB2Driver 
◼ 
COM.ibm.db2.jdbc.app.DB2Driver 
◼ 
com.informix.jdbc.IfxDriver 
◼ 
com.gbase.jdbc.Driver 
◼ 
org.srdbsql.Driver 
◼ 
com.ibm.db2.jcc.DB2Driver 
◼ 
com.highgo.jdbc.Driver 
◼ 
com.uxsino.uxdb.Driver 
◼ 
com.huawei.gauss.jdbc.ZenithDriver 
◼ 
com.inspur.jdbc.KdDriver 
◼ 
com.datapps.linkoopdb.jdbc.JdbcDriver 
◼ 
com.alipay.oceanbase.obproxy.mysql.jdbc.Driver 或者org.postgresql.Driver  
◼ 
com.goldendb.jdbc.Driver 
⚫ 
--jdbcurl：必选，连接数据库所需的url。对应数据库类型可以设置连接url。 
◼ 
Oracle Type 4 Driver for Oracle：“jdbc:oracle:thin:@[host]:[1521]:[dbName]” 
◼ 
Mysql5&mysql8：“jdbc:mysql://[host]:[3306]/[dbName]” 
◼ 
Sybase15 Driver：jdbc:sybase:Tds:[host]:[5000]/[dbName] 
◼ 
Dameng Driver：jdbc:dm://127.0.0.1:12345/TEST 
◼ 
Kingbase Driver：jdbc:kingbase://[host]:[54321]/[dbName] 
◼ 
Kingbase8 Driver：jdbc:kingbase8://[host]:[54321]/[dbName] 
◼ 
Oscar Driver：jdbc:oscar://[host]:[2003]/[dbName] 
◼ 
HSQL Driver：jdbc:hsqldb:hsql://[host]:[9001]/default 
◼ 
Sybase type 4 Driver for sysbase 11.x: jdbc:sybase:Tds:[host]:[2048]/[dbName] 
◼ 
Jtds Sysbase：jdbc:jtds:sybase://[ip]:[1433]/[dbName] 
◼ 
PostgreSQL type 4 Driver for postgreSq 
◼ 
Oracle OCI Driver for Oracle：jdbc:oracle:oci8:@[dbName] 
◼ 
MM.MySQL Type 4 Driver for MySQL：
jdbc:mysql://[host]:[3306]/[dbName]?user=test 
◼ 
Sqlserver：jdbc:microsoft:sqlserver://[host]:[1433];DatabaseName=[dbName] 


## 第 80 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
68 
◼ 
Jtds sqlserver：
jdbc.url=jdbc:jtds:sqlserver://[ip]:[1433];databaseName=[dbname] 
◼ 
Sqlserver2005：jdbc:postgresql://[host]:[5432]/[dbName] 
◼ 
Derby Client Driver：jdbc:derby://[host]:[port]/[database] 
◼ 
Derby Embedded Driver：jdbc:derby://[host]:[port]/[database] 
◼ 
IBM Type 4 Driver for infomix：
jdbc:informix-sqli://[host]:[1526]/[dbName]:informixserver=[myserver];user=[u
sername];password=[password] 
◼ 
IBM Type 4 Driver for DB2：jdbc:db2://[host]:6789/[dbName] 
◼ 
IBM Type 2 Driver for DB2：jdbc:db2:[dbname] 
◼ 
Gbase8t
：
jdbc:informix-sqli://127.0.0.1:1526/dbname:informixserver=servername 
◼ 
Gbase8s：jdbc:GBase://localhost:5258/dbname 
◼ 
Sr：jdbc:srdbsql://localhost:1975/dbname 
◼ 
Db2：jdbc:db2://[ip]:[50000]/[dbname] 
◼ 
Highgo：jdbc:highgo://[ip]:[5866]/[dbname] 
◼ 
Uxdb：jdbc:uxdb://[ip]:[5431]/[dbname] 
◼ 
gaussDB 100：jdbc:zenith:db:@[ip]:[port] 
◼ 
inspurk-DB：jdbc:inspur:thin:@[ip]:[port]:[db_name] 
◼ 
linkoopdb：jdbc:linkoopdb:tcp://[ip]:[9105]/[dbname] 
◼ 
oceanbase：jdbc:oceanbase://[host]:[port]/[database] 
◼ 
MogDB：jdbc:postgresql://[host]:[port]/[dbName] 
◼ 
goldendb：jdbc:goldendb://[host]:[3307]/[dbName] 
⚫ 
--dbuser：必选，连接数据库所需的用户名。 
⚫ 
--dbpassword：必选，用户名密码。 
⚫ 
--isEncrypt：必选，密码是否加密，“true”表示密码是密文；“false”表示密码是明
文。 
⚫ 
--testquery：测试连接。默认测试SQL语句，默认值为“SELECT 1”。 
⚫ 
--initsqlfile：建立连接时首次执行的SQL语句文件名。指定安装目录/conf/jdbc目


## 第 81 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
69 
录下的文件，只能为txt或sql类型的文件，此文件中的SQL语句可以用来执行初
始化语句。 
注意： 
每次建立连接都会执行一次，谨慎使用。 
⚫ 
--jtamanaged：使用jta管理。，可设置为“true”或者“false”，默认为“true”。 
⚫ 
--testonborrow：获取连接时验证。指明是否在从池中取出连接前进行检验，，
可设置为“true”或者“false”，默认为“false”。 
⚫ 
--testonconnect：创建连接时验证。指明是否在创建连接时时进行检验。可设置
为“true”或者“false”，默认为“false”。 
⚫ 
--testonreturn：归还连接时验证。指明是否在归还到池中前进行检验，可设置为
“true”或者“false”，默认为“false”。 
⚫ 
--testWhileIdle：线程回收开关，，可设置为“true”或者“false”，默认为“false”。 
⚫ 
--jdbcclasspath：驱动路径。 
⚫ 
--jdbcinitialsize：jdbc初始化连接数，不得大于最大连接数，默认为“10”，取值范
围为“1-900”之间的整数。 
⚫ 
--jdbcmaxactive：最大连接数，默认为“100”，取值范围为“1-900”之间的整数。 
⚫ 
--jdbcmaxwaittime：最大等待时间，默认为“30000”，取值范围“250-2147483647”，
单位为毫秒。 
⚫ 
--removeabandonedtimeout：泄露超时时间。在这段时间内跟踪连接池中的连接
泄漏，并将获取连接的调用栈（堆栈）记录下来，当超时后，以warning级别将
该堆栈信息输出到日志。以秒为单位。默认值为“2”。 
⚫ 
--threshold：SQL的查询时间，单位：毫秒，默认值“1000”。 
⚫ 
--maxCache：语句最大缓存数，取值范围为“0-2147483647”之间的整数。 
⚫ 
--prepared：PreparedStatement语句缓存，可设置为“true”或者“false”，默认为
“false”。 
⚫ 
--callable：CallableStatement语句缓存，可设置为“true”或者“false”，默认为“false”。 
⚫ 
--stmtcache：语句缓存，默认为“false”。可设置为“true”或者“false”。 
⚫ 
--sqllog：sql日志，可设置为“true”或者“false”，默认值“false”。 
⚫ 
--stmtfn：语句跟踪，默认为“false”。可设置为“true”或者“false”。 


## 第 82 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
70 
⚫ 
--leakCheck：即时泄露回收。如果设置为“true”，进行泄漏检测，当完成泄漏连
接跟踪后，将泄漏的连接销毁。默认值为“false”。可设置为“true”或者“false”。 
⚫ 
--fairQueue：是否采用公平锁获取连接，true/false，默认“true”。 
⚫ 
--queryTimeout：在该时间后将终止运行时间异常长的查询（以秒为单位）。应
用服务器将在所创建的语句上设置“QueryTimeout”。默认值为0，表示未启用该
属性。 
⚫ 
--isXa：是否XA连接，默认值为“false”。可设置为“true”或者“false”。 
⚫ 
--validationQueryTimeout：验证超时。测试连接活动的最长时间，以秒为单位，
不能小于1s。默认为“5”。 
⚫ 
--defaultAutoCommit：自动提交，连接池创建的连接的默认的auto-commit 状态。
默认为“true”，可设置为true或者false。 
⚫ 
--commitOnReturn：释放连接时提交。默认为“true”，连接返回时提交，不开启
默认回滚。可设置为“true”或者“false”。 
⚫ 
--assocWithThread：线程连接关联。JDBC连接与线程绑定，默认为“false”。 
⚫ 
--minEvictableIdleTime：空闲超时时间。连接在池中保持空闲而不被连接回收器
线程回收的最小时间值，单位毫秒，默认为60000ms，不能超过连接最大寿命。 
⚫ 
--timeBetweenEvictionRuns：空闲检查周期。空闲连接回收器线程运行期间休眠
的时间值， 单位：毫秒，默认为60000ms。 
⚫ 
--logAbandoned：连接泄漏时打印日志。 
⚫ 
--maxAge：连接最大寿命，保持连接的最大毫秒数，不能低于30000ms，默认为
“1800000”。 
⚫ 
--clientInfo：获取数据库的基本信息。 
⚫ 
--validationInterval：连接验证时间间隔，指明是否在归还到池中前进行检验。避
免过度验证，保证验证不超过这个频率，以毫秒为单位。如果一个连接应该被
验证，但上次验证未达到指定间隔，将不进行再次验证，默认30000。 
⚫ 
--removeAbandoned：泄露回收。如果设置为“true”，进行泄漏检测，当完成泄漏
连接跟踪后，将泄漏的连接销毁。默认值为“false”。可设置为“true”或者“false”。 
⚫ 
--connectionProperties：连接参数，当用Driver建立新连接时被发送给JDBC 驱动
的连接参数，格式必须是propertyName=property，多个连接参数之间以分号分割。 


## 第 83 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
71 
注意： 
当“--jdbcdriver”和“--jdbcurl”设置为“goldendb”数据库的驱动和连接url时，
连接参数需要添加“mysqlCompatible=true”连接属性，兼容Mysql驱动。 
⚫ 
--minIdle：最小空闲连接数，默认为10，取值范围“0-900”。 
⚫ 
--logValidationErrors：打印验证失败信息。可配置为true或者false，默认值为
“false”。 
⚫ 
--ignoreExceptionOnPreLoad：打印初始化连接异常，可配置为true或者false，默
认值为“false”。 
⚫ 
--testFrequencySeconds：测试频率，单位秒，默认120秒。 
⚫ 
--jdbcConnectionPoolRefs：数据源列表，用逗号分隔。 
⚫ 
--createCountEveryTime：每次创建个数，默认值为“0”,表示不启用。取值范围为
“0-2147483647”。 
⚫ 
--intervalEveryTime：每次创建连接间的时间间隔，单位：毫秒，默认值为“0”，
表示不启动。取值范围为“0-2147483647”。 
⚫ 
jdbc_name：必选，目标参数，数据源名称。名称由数字、字母、下划线、'-'和
'/'组成，首字符为英文，尾字符不能为'/'。 
实例 
⚫ 
在线模式： 
create-jdbc-connection-pool --jdbcdriver=com.mysql.jdbc.Driver 
--jdbcurl=jdbc:mysql://10.10.4.55:3306/test1 --dbuser=cli --dbpassword=cli123.com 
--jdbcclasspath=/path/to/mysql-connector-java-5.1.18.jar test-cli-jdbc 
⚫ 
离线模式： 
create-jdbc-connection-pool --jdbcdriver=com.mysql.jdbc.Driver 
--jdbcurl=jdbc:mysql://10.10.20.27:3306/test_db --dbuser=root 
--dbpassword=Aa123456 --jdbcclasspath=D:\temp\mysql-connector-java-5.1.43.jar   
--offline=true test-cli-jdbc 
验证方式 
1. 
登录TongWeb管理控制台。 
2. 
左侧导航栏中，单击“JDBC配置”，进入连接池管理页面。 
3. 
可以查看到test-cli-jdbc已经成功创建。 


## 第 84 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
72 
2.37 update-jdbc-connection-pool 
功能说明 
修改指定名称的JDBC 连接池属性。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为“true”
或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”不使用
交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地址。
默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访问服
务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此参
数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--jdbcdriver：必选，选择数据库驱动类名。 
您可以设置为： 
◼ 
oracle.jdbc.driver.OracleDriver 
◼ 
com.mysql.jdbc.Driver 


## 第 85 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
73 
◼ 
com.mysql.cj.jdbc.Driver 
◼ 
com.sybase.jdbc3.jdbc.SybDriver 
◼ 
dm.jdbc.driver.DmDriver 
◼ 
com.kingbase.Driver 
◼ 
com.kingbase8.Driver 
◼ 
com.oscar.Driver 
◼ 
org.hsqldb.jdbcDriver 
◼ 
com.sybase.jdbc.SybDriver 
◼ 
net.sourceforge.jtds.jdbc.Driver 
◼ 
org.hsqldb.jdbcDriver 
◼ 
org.postgresql.Driver 
◼ 
oracle.jdbc.driver.OracleDriver 
◼ 
org.gjt.mm.mysql.Driver 
◼ 
com.microsoft.jdbc.sqlserver.SQLServerDriver 
◼ 
net.sourceforge.jtds.jdbc.Driver 
◼ 
com.microsoft.sqlserver.jdbc.SQLServerDriver 
◼ 
org.apache.derby.jdbc.ClientDriver 
◼ 
org.apache.derby.jdbc.EmbeddedDriver 
◼ 
com.informix.jdbc.IfxDriver 
◼ 
COM.ibm.db2.jdbc.net.DB2Driver 
◼ 
COM.ibm.db2.jdbc.app.DB2Driver 
◼ 
com.informix.jdbc.IfxDriver 
◼ 
com.gbase.jdbc.Driver 
◼ 
org.srdbsql.Driver 
◼ 
com.ibm.db2.jcc.DB2Driver 
◼ 
com.highgo.jdbc.Driver 
◼ 
com.uxsino.uxdb.Driver 
◼ 
com.huawei.gauss.jdbc.ZenithDriver 
◼ 
com.inspur.jdbc.KdDriver 


## 第 86 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
74 
◼ 
com.datapps.linkoopdb.jdbc.JdbcDriver 
◼ 
com.alipay.oceanbase.obproxy.mysql.jdbc.Driver 或者org.postgresql.Driver  
◼ 
com.goldendb.jdbc.Driver 
⚫ 
--jdbcurl：必选，连接数据库所需的url。对应数据库类型可以设置连接url。 
◼ 
Oracle Type 4 Driver for Oracle：“jdbc:oracle:thin:@[host]:[1521]:[dbName]” 
◼ 
Mysql5&mysql8：“jdbc:mysql://[host]:[3306]/[dbName]” 
◼ 
Sybase15 Driver：jdbc:sybase:Tds:[host]:[5000]/[dbName] 
◼ 
Dameng Driver：jdbc:dm://127.0.0.1:12345/TEST 
◼ 
Kingbase Driver：jdbc:kingbase://[host]:[54321]/[dbName] 
◼ 
Kingbase8 Driver：jdbc:kingbase8://[host]:[54321]/[dbName] 
◼ 
Oscar Driver：jdbc:oscar://[host]:[2003]/[dbName] 
◼ 
HSQL Driver：jdbc:hsqldb:hsql://[host]:[9001]/default 
◼ 
Sybase type 4 Driver for sysbase 11.x: jdbc:sybase:Tds:[host]:[2048]/[dbName] 
◼ 
Jtds Sysbase：jdbc:jtds:sybase://[ip]:[1433]/[dbName] 
◼ 
PostgreSQL type 4 Driver for postgreSq 
◼ 
Oracle OCI Driver for Oracle：jdbc:oracle:oci8:@[dbName] 
◼ 
MM.MySQL Type 4 Driver for MySQL：
jdbc:mysql://[host]:[3306]/[dbName]?user=test 
◼ 
Sqlserver：jdbc:microsoft:sqlserver://[host]:[1433];DatabaseName=[dbName] 
◼ 
Jtds sqlserver：
jdbc.url=jdbc:jtds:sqlserver://[ip]:[1433];databaseName=[dbname] 
◼ 
Sqlserver2005：jdbc:postgresql://[host]:[5432]/[dbName] 
◼ 
Derby Client Driver：jdbc:derby://[host]:[port]/[database] 
◼ 
Derby Embedded Driver：jdbc:derby://[host]:[port]/[database] 
◼ 
IBM Type 4 Driver for infomix：
jdbc:informix-sqli://[host]:[1526]/[dbName]:informixserver=[myserver];user=[u
sername];password=[password] 
◼ 
IBM Type 4 Driver for DB2：jdbc:db2://[host]:6789/[dbName] 
◼ 
IBM Type 2 Driver for DB2：jdbc:db2:[dbname] 


## 第 87 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
75 
◼ 
Gbase8t
：
jdbc:informix-sqli://127.0.0.1:1526/dbname:informixserver=servername 
◼ 
Gbase8s：jdbc:GBase://localhost:5258/dbname 
◼ 
Sr：jdbc:srdbsql://localhost:1975/dbname 
◼ 
Db2：jdbc:db2://[ip]:[50000]/[dbname] 
◼ 
Highgo：jdbc:highgo://[ip]:[5866]/[dbname] 
◼ 
Uxdb：jdbc:uxdb://[ip]:[5431]/[dbname] 
◼ 
gaussDB 100：jdbc:zenith:db:@[ip]:[port] 
◼ 
inspurk-DB：jdbc:inspur:thin:@[ip]:[port]:[db_name] 
◼ 
linkoopdb：jdbc:linkoopdb:tcp://[ip]:[9105]/[dbname] 
◼ 
oceanbase：jdbc:oceanbase://[host]:[port]/[database] 
◼ 
MogDB：jdbc:postgresql://[host]:[port]/[dbName] 
◼ 
goldendb：jdbc:goldendb://[host]:[3307]/[dbName] 
⚫ 
--dbuser：必选，连接数据库所需的用户名。 
⚫ 
--dbpassword：必选，用户名密码。 
⚫ 
--isEncrypt：必选，密码是否加密，“true”表示密码是密文；“false”表示密码是明
文。 
⚫ 
--testquery：测试连接。默认测试SQL语句，默认值为“SELECT 1”。 
⚫ 
--initsqlfile:建立连接时首次执行的SQL语句文件名。指定安装目录/conf/jdbc目录
下的文件，只能为txt或sql类型的文件，此文件中的SQL语句可以用来执行初始
化语句。 
注意： 
每次建立连接都会执行一次，谨慎使用。 
⚫ 
--jtamanaged：使用jta管理。，可设置为“true”或者“false”，默认为“true”。 
⚫ 
--testonborrow：获取连接时验证。指明是否在从池中取出连接前进行检验，，
可设置为“true”或者“false”，默认为“false”。 
⚫ 
--testonconnect：创建连接时验证。指明是否在创建连接时时进行检验。可设置
为“true”或者“false”，默认为“false”。 
⚫ 
--testonreturn：归还连接时验证。指明是否在归还到池中前进行检验，可设置为


## 第 88 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
76 
“true”或者“false”，默认为“false”。 
⚫ 
--testWhileIdle：线程回收开关，，可设置为“true”或者“false”，默认为“false”。 
⚫ 
--jdbcclasspath：驱动路径。 
⚫ 
--jdbcinitialsize：jdbc初始化连接数，不得大于最大连接数，默认为“10”，取值范
围为“1-900”之间的整数。 
⚫ 
--jdbcmaxactive：最大连接数，默认为“100”，取值范围为“1-900”之间的整数。 
⚫ 
--jdbcmaxwaittime：最大等待时间，默认为“30000”，取值范围“250-2147483647”，
单位为毫秒。 
⚫ 
--removeabandonedtimeout：泄露超时时间。在这段时间内跟踪连接池中的连接
泄漏，并将获取连接的调用栈（堆栈）记录下来，当超时后，以warning级别将
该堆栈信息输出到日志。以秒为单位。默认值为“2”。 
⚫ 
--threshold：SQL的查询时间，单位：毫秒，默认值“1000”。 
⚫ 
--maxCache：语句最大缓存数，取值范围为“0-2147483647”之间的整数。 
⚫ 
--prepared：PreparedStatement语句缓存，可设置为“true”或者“false”，默认为
“false”。 
⚫ 
--callable：CallableStatement语句缓存，可设置为“true”或者“false”，默认为“false”。 
⚫ 
--stmtcache：语句缓存，默认为“false”。可设置为“true”或者“false”。 
⚫ 
--sqllog：sql日志，可设置为“true”或者“false”，默认值“false”。 
⚫ 
--stmtfn：语句跟踪，默认为“false”。可设置为“true”或者“false”。 
⚫ 
--leakCheck：即时泄露回收。如果设置为“true”，进行泄漏检测，当完成泄漏连
接跟踪后，将泄漏的连接销毁。默认值为“false”。可设置为“true”或者“false”。 
⚫ 
--fairQueue：是否采用公平锁获取连接，true/false，默认“true”。 
⚫ 
--queryTimeout：在该时间后将终止运行时间异常长的查询（以秒为单位）。应
用服务器将在所创建的语句上设置“QueryTimeout”。默认值为0，表示未启用该
属性。 
⚫ 
--isXa：是否XA连接，默认值为“false”。可设置为“true”或者“false”。 
⚫ 
--validationQueryTimeout：验证超时。测试连接活动的最长时间，以秒为单位，
不能小于1s。默认为“5”。 
⚫ 
--defaultAutoCommit：自动提交，连接池创建的连接的默认的auto-commit 状态。


## 第 89 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
77 
默认为“true”，可设置为true或者false。 
⚫ 
--commitOnReturn：释放连接时提交。默认为“true”，连接返回时提交，不开启
默认回滚。可设置为“true”或者“false”。 
⚫ 
--assocWithThread：线程连接关联。JDBC连接与线程绑定，默认为“false”。 
⚫ 
--minEvictableIdleTime：空闲超时时间。连接在池中保持空闲而不被连接回收器
线程回收的最小时间值，单位毫秒，默认为60000ms，不能超过连接最大寿命。 
⚫ 
--timeBetweenEvictionRuns：空闲检查周期。空闲连接回收器线程运行期间休眠
的时间值， 单位：毫秒，默认为60000ms。 
⚫ 
--logAbandoned：连接泄漏时打印日志。 
⚫ 
--maxAge：连接最大寿命，保持连接的最大毫秒数，不能低于30000ms，默认为
“1800000”。 
⚫ 
--clientInfo：获取数据库的基本信息。 
⚫ 
--validationInterval：连接验证时间间隔，指明是否在归还到池中前进行检验。避
免过度验证，保证验证不超过这个频率，以毫秒为单位。如果一个连接应该被
验证，但上次验证未达到指定间隔，将不进行再次验证，默认30000。 
⚫ 
--removeAbandoned：泄露回收。如果设置为“true”，进行泄漏检测，当完成泄漏
连接跟踪后，将泄漏的连接销毁。默认值为“false”。可设置为“true”或者“false”。 
⚫ 
--connectionProperties：连接参数，当用Driver建立新连接时被发送给JDBC 驱动
的连接参数，格式必须是propertyName=property，多个连接参数之间以分号分割。 
注意： 
当“--jdbcdriver”和“--jdbcurl”设置为“goldendb”数据库的驱动和连接url时，
连接参数需要添加“mysqlCompatible=true”连接属性，兼容Mysql驱动。 
⚫ 
--minIdle：最小空闲连接数，默认为10，取值范围“0-900”。 
⚫ 
--logValidationErrors：打印验证失败信息。可配置为true或者false，默认值为
“false”。 
⚫ 
--ignoreExceptionOnPreLoad：打印初始化连接异常，可配置为true或者false，默
认值为“false”。 
⚫ 
--testFrequencySeconds：测试频率，单位秒，默认120秒。 
⚫ 
--jdbcConnectionPoolRefs：数据源列表，用逗号分隔。 


## 第 90 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
78 
⚫ 
--createCountEveryTime：每次创建个数，默认值为“0”,表示不启用。取值范围为
“0-2147483647”。 
⚫ 
--intervalEveryTime：每次创建连接间的时间间隔，单位：毫秒，默认值为“0”，
表示不启动。取值范围为“0-2147483647”。 
⚫ 
jdbc_name：必选，目标参数，数据源名称。名称由数字、字母、下划线、'-'和
'/'组成，首字符为英文，尾字符不能为'/'。 
实例 
执行命令前，请保证test-cli-jdbc 已经存在。 
在线模式： 
update-jdbc-connection-pool --jdbcdriver=com.mysql.jdbc.Driver 
--jdbcurl=jdbc:mysql://10.10.4.55:3306/test1--dbuser=cli --dbpassword=cli123.com 
--jdbcclasspath=/path/to/mysql-connector-java-5.1.18.jar --jdbcinitialsize=11 test-cli-jdbc 
离线模式： 
update-jdbc-connection-pool --jdbcdriver=com.mysql.jdbc.Driver 
--jdbcurl=jdbc:mysql://10.10.4.55:3306/test1--dbuser=cli --dbpassword=cli123.com 
--jdbcclasspath=/path/to/mysql-connector-java-5.1.18.jar --jdbcinitialsize=11 
--offline=true test-cli-jdbc 
验证方式 
1. 
登录TongWeb管理控制台。 
2. 
左侧导航栏中，单击“JDBC配置”，进入连接池管理页面。 
3. 
可以查看到test-cli-jdbc连接池的属性已修改成功。 
2.38 delete-jdbc-connection-pool 
功能说明 
删除具有指定JDBC 连接池名称的JDBC 连接池。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为“true”
或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”不使用
交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP地址。
默认“localhost”。 


## 第 91 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
79 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https访问服
务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置此参
数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交互
输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
pool_name：必选，目标参数，jdbc 连接池名称。 
实例 
执行命令前，请保证test-cli-jdbc 已经存在。 
⚫ 
在线模式： 
delete-jdbc-connection-pool test-cli-jdbc 
⚫ 
离线模式： 
delete-jdbc-connection-pool --offline=true test-cli-jdbc 
验证方式 
1. 
登录TongWeb管理控制台。 
2. 
左侧导航栏中，单击“JDBC配置”，进入连接池管理页面。 
3. 
可以查看到test-cli-jdbc已经删除成功。 
2.39 ping-jdbc-connection-pool 
功能说明 
测试连接池是否可用。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 


## 第 92 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
80 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
pool_name：必选，目标参数，jdbc 连接池名称。 
实例 
执行命令前，请保证test-cli-jdbc 已经存在。 
⚫ 
在线模式： 
ping-jdbc-connection-pool test-cli-jdbc 
⚫ 
离线模式： 
ping-jdbc-connection-pool --offline=true test-cli-jdbc 


## 第 93 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
81 
2.40 list-jdbc-connection-pools 
功能说明 
获取已创建的JDBC 连接池。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-jdbc-connection-pools 


## 第 94 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
82 
⚫ 
离线模式： 
list-jdbc-connection-pools   --offline=true 
2.41 deploy 
功能说明 
部署企业应用程序、Web 应用程序、EJB 模块。 
不支持离线模式。 
部署相关命令都依赖于tongweb 的运行。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 


## 第 95 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
83 
相关参数 
⚫ 
--applocation：必选，客户端应用文件的路径。 
⚫ 
--contextroot：应用前缀。只有在web应用程序部署时可用。 
应用前缀的优先级由高到低依次是：“-contextroot参数” > 
“tongweb-web.xml” > “默认值（包名）”。 
⚫ 
--defaultvs：虚拟服务器。 
⚫ 
--precompilejsp：jsp是否预编译。默认为“false”，可设置为“true”或者
“false”。 
⚫ 
--requestparameterslostvalidation:默认为“false”,请求参数丢失校验参
数。可设置为“true”或者“false”，true表示校验参数，false表示不校验。 
⚫ 
--deployorder：设置部署顺序。默认的部署顺序是100，如果需要调整部署顺
序的话，可以指定。取值范围为“1-2147483647”之间的整数。 
⚫ 
--delegate：类加载策略，默认是子优先“false”，如果想配置父优先则设置
为“true”。 
⚫ 
--appdescription：应用描述。 
⚫ 
--sharedLibNames：指定共享库名称，可以指定多个，以“，”分隔。 
⚫ 
--enableHotSwap：开启类热加载，默认为“false”。当设置为“true”时，在TongWeb
服务器启动且应用在运行过程中，自动检测应用的class文件更新。若class文件存
在更新，则更新的class文件立即生效，无需重启TongWeb服务器。 
注意： 
◼ 
新增或者删除的class文件不会触发热加载。 
◼ 
应用停止或解部署后，TongWeb服务器停止应用的类热加载的监听。 
◼ 
生产环境请谨慎开启。 
◼ 
类热加载不支持变更了结构类的加载，只支持热加载修改类方法内部的代
码。 
⚫ 
--deployTimeout：部署超时时间，若部署超过此时间，系统将中断部署流程，
默认600秒。 
⚫ 
--sessionManager：指定session管理器的名称。 
⚫ 
app_name：必选，目标参数，应用名称。 
实例 
deploy--contextroot=/dbpooltest --precompilejsp=true --applocation =D:\\dbpooltest.war 


## 第 96 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
84 
--sharedLibNames=a1,b1,c1 testapp 
注意事项 
仅支持本地主机文件或目录部署。 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，单击“应用管理”，进入应用管理页面。 
3. 可以查看到testapp已经部署成功。 
2.42 redeploy 
功能说明 
重新部署在指定目标上的组件。 
不支持离线模式。 
部署相关命令都依赖于tongweb 的运行。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交


## 第 97 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
85 
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
--applocation：客户端应用文件的路径。 
app_name：必选，目标参数，应用名称。 
实例 
⚫ 
若需要重部署一个新的应用文件，如下所示。 
redeploy --applocation =E:/test.war testapp 
⚫ 
若重部署当前应用，而不替换文件，如下所示。 
redeploy testapp 
注意： 
⚫ 
testapp表示应用名称。 
⚫ 
重部署应用时，需要正确的指定应用名称。 
应用名称的默认值是去掉文件后缀之后的应用名称。 
例如：应用为c:/test2.ear，默认的应用名称为test2。 
若应用名称不正确，将导致重部署失败。 
为了确认应用名称，可以查看TongWeb 的管理控制台上已部署应用的应用名称这一
项。 
注意事项 
仅支持本地主机文件或目录部署。 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，单击“应用管理”，进入应用管理页面。 
3. 查看testapp，并单击应用所在行的“http访问”，查看修改是否生效。 
2.43 undeploy 
功能说明 
解除部署的应用。 
不支持离线模式，部署相关命令都依赖于tongweb 的运行。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”


## 第 98 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
86 
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
app_name：必选，目标参数，应用名称。 
实例 
undeploy testapp 
注意：解部署应用时，需要正确的指定应用名称。 
应用名称的默认值是去掉文件后缀之后的应用名称， 
例如：应用为c:/test2.ear，默认的应用名称为test2。 
若应用名称不正确，将导致解部署失败。 
为了确认应用名称，可以通过list-apps 查看是否有当前应用的名称存在。 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，单击“应用管理”，进入应用管理页面。 
3. 可以查看到testapp已经解除部署。 


## 第 99 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
87 
2.44 enable-app 
功能说明 
启动应用。不支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
app_name：必选，目标参数，应用名称。 
实例 
执行命令前，请保证testapp 已经存在。 
enable-app testapp 
验证方式 
1. 登录TongWeb管理控制台。 


## 第 100 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
88 
2. 左侧导航栏中，单击“应用管理”，进入应用管理页面。 
3. 可以查看到testapp已经被启动。 
2.45 disable-app 
功能说明 
停止应用。不支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
app_name：必选，目标参数，应用名称。 
实例 
执行命令前，请保证testapp 已经存在。 


## 第 101 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
89 
disable-app testapp 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，单击“应用管理”，进入应用管理页面。 
3. 可以查看到testapp已经被停止。 
2.46 show-backup-appdir 
功能说明 
查看应用备份目录。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 


## 第 102 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
90 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
show-backup-appdir 
⚫ 
离线模式： 
show-backup-appdir  --offline=true 
2.47 update-backup-appdir 
功能说明 
修改应用备份目录。该命令不支持相对路径。 
支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交


## 第 103 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
91 
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
backup_dir：必选，目标参数，应用备份目录名称。该命令不支持相对路径。 
实例 
⚫ 
在线模式： 
update-backup-appdir D:\\temp 
⚫ 
离线模式： 
update-backup-appdir --offline=true  D:\\temp 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，单击“应用管理”，进入应用管理页面。 
3. 单击“设置应用备份路径”，弹出应用备份目录窗口。 
4. 可以查看到应用备份目录已经修改成功。 
2.48 backup-app 
功能说明 
备份应用。 
不支持离线模式。部署相关命令都依赖于tongweb 的运行。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文


## 第 104 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
92 
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
appName：必选，目标参数，应用名称。 
实例 
backup-app testapp 
验证方式 
在${TongWeb_HOME}/app-bak 目录下，testapp 备份成功。 
2.49 update-auto-deploy-config 
功能说明 
修改自动部署开关。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 


## 第 105 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
93 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--autoDeployEnabled：自动部署开关。Boolean型，默认true。 
⚫ 
--autoDeployDir：自动部署路径。默认空字符串。 
⚫ 
--autoDeployCheckInterval：自动部署超时时间，单位：毫秒，默认3000。 
⚫ 
--hotDeployEnabled：热部署开关。Boolean型，默认“false”。 
⚫ 
--vsName：配置自动部署虚拟主机名称。 
⚫ 
--deployTimeout：自动部署耗时超过此时间，系统将中断部署流程，默认600
秒。 
实例 
⚫ 
在线模式： 
update-auto-deploy-config --autoDeployEnabled=true 
--autoDeployDir="d:/temp/autodeploy" --autoDeployCheckInterval=4444 
--hotDeployEnabled=false --vsName=test-virtual-host 
⚫ 
离线模式： 
update-auto-deploy-config --autoDeployEnabled=false 
--autoDeployDir="d:/temp/autodeploy" --autoDeployCheckInterval=4444 
--hotDeployEnabled=false --vsName=xy-virtual-host  --offline=true 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，单击“服务”，进入服务配置页面。 
3. 可以查看到对应属性已修改为设置的值。 


## 第 106 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
94 
2.50 list-apps 
功能说明 
列出所有部署的应用。 
该命令暂不支持离线模式，直接获取内存中的数据，离线模式下无法获取。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
- 
实例 
list-apps 


## 第 107 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
95 
2.51 list-sys-properties 
功能说明 
列出服务器系统属性。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-sys-properties 


## 第 108 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
96 
⚫ 
离线模式： 
list-sys-properties --offline=true 
2.52 create-jms-connection-factory 
功能说明 
创建具有指定JMS 连接工厂名称的JMS 连接工厂。 
不支持离线模式，离线模式下无法执行相关类加载的逻辑。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--restype：连接工厂类型，可选。其取值是javax.jms.ConnectionFactory、


## 第 109 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
97 
javax.jms.QueueConnectionFactory、javax.jms.TopicConnectionFactory中
的任意一个。默认值为javax.jms.ConnectionFactory。 
⚫ 
--adapter：连接工厂所使用的资源适配器，默认为genericra。可以是其他的
已部署好的资源适配器。 
⚫ 
--description：描述。 
⚫ 
--minSize：连接池的初始化连接数，默认为10。取值范围为“0-2147483647” 
之间的整数。初始连接数不能大于最大连接数。 
⚫ 
--maxSize：连接池中的最大连接数，默认为“100”，取值范围为“1-2147483647” 
之间的整数。 
⚫ 
--blockingTimeoutSeconds：从连接池中获取连接的最长等待时间，单位为秒，
默认为60秒，取值范围为“1-2147483647” 之间的整数。 
⚫ 
--idleTimeoutMinutes：连接的空闲超时时间，单位为分。默认为10分钟，取
值范围为“1-2147483647” 之间的整数。 
⚫ 
--matchConnections：获取连接时由资源适配器进行匹配，默认为false。 
⚫ 
--transactionSupport：连接池的事务支持类型，默认值为NoTransaction。用
此参数指定时，其取值是NoTransaction、LocalTransaction或者XATransaction
中的任意一个。 
⚫ 
--properties：属性。取决于所使用的适配器。格式为key:value，如果有多项
则用;隔开。 
⚫ 
factory_name：必选，目标参数，JMS连接工厂名称。 
实例 
create-jms-connection-factory --restype javax.jms.ConnectionFactory 
--adapter genericra test 
或者 
create-jms-connection-factory --restype=javax.jms.ConnectionFactory 
--adapter=genericra --description=test --minSize=11 --maxSize=101 
--blockingTimeoutSeconds=60 --idleTimeoutMinutes=10 
--matchConnections=false --transactionSupport=NoTransaction 
--properties=ConnectionFactoryJndiName:test test 
验证方式 
1. 登录TongWeb管理控制台。 


## 第 110 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
98 
2. 左侧导航栏中，选择“JMS服务”>“JMS连接工厂”，进入JMS连接工厂页面。 
3. 可以查看到JMS连接工厂test已经创建成功。 
2.53 delete-jms-connection-factory 
功能说明 
删除具有指定JMS 连接工厂名称的JMS 连接工厂资源。 
支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 


## 第 111 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
99 
相关参数 
factory_name：必选，目标参数，JMS 连接工厂名称。 
实例 
执行命令前，请保证JMS 连接工厂test 已经存在。 
⚫ 
在线模式： 
delete-jms-connection-factory test 
⚫ 
离线模式： 
delete-jms-connection-factory --offline=true test 
2.54 list-jms-connection-factory 
功能说明 
获取已创建的JMS 连接工厂资源。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 


## 第 112 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
100 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-jms-connection-factory 
⚫ 
离线模式： 
list-jms-connection-factory  --offline=true 
2.55 create-jms-destination 
功能说明 
创建具有指定JMS 目的地名称的JMS 目的地资源。 
不支持离线模式，离线模式下无法执行相关类加载的逻辑。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 


## 第 113 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
101 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--restype：目的地类型，默认值为javax.jms.Queue。用该参数指定时取值为
javax.jms.Queue、javax.jms.Topic中的任意一个。 
⚫ 
--adapter：连接工厂所使用的资源适配器，默认为“genericra”。也可是其
他的已部署好的资源适配器。 
⚫ 
--description：JMS目的地的描述。 
⚫ 
--properties：属性。取决于所使用的适配器。格式为key:value，如果有多项
则用;隔开。 
⚫ 
destination_name：必选，目标参数，目的地名称。 
实例 
create-jms-destination --adapter genericra --restype javax.jms.Topic test 
或者 
create-jms-destination --restype=javax.jms.Queue --adapter=genericra 
--description=test --properties=DestinationJndiName:test test 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JMS服务”>“JMS目的地”，进入JMS目的地页面。 
3. 可以查看到JMS目的地test已经成功创建。 
2.56 delete-jms-destination 
功能说明 
删除具有指定JMS 目的地名称的JMS 目的地资源。 
支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 


## 第 114 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
102 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
destination_name：必选，目标参数，目的地名称。 
实例 
⚫ 
在线模式： 
delete-jms-destination test 
⚫ 
离线模式： 
delete-jms-destination --offline=true test 
2.57 list-jms-destination 
功能说明 
获取已创建的JMS 目的地资源。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 


## 第 115 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
103 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-jms-destination 
⚫ 
离线模式： 
list-jms-destination --offline=true 
2.58 create-connector-connection-pool 
功能说明 
创建具有指定JCA 连接池名称的JCA 连接池。 
不支持离线模式，离线模式下无法执行相关类加载的逻辑。 


## 第 116 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
104 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--adapter：必选，连接工厂所使用的资源适配器。必须是已部署好的资源适配
器。 
⚫ 
--definition：必选，连接器应用中ra.xml中定义。
connection-definition-interface。 
⚫ 
--minSize：连接池的初始化连接数，默认为10，取值范围为“0-2147483647” 
之间的整数。 
⚫ 
--maxSize：连接池中的最大连接数，默认为“100”，取值范围为“1-2147483647” 


## 第 117 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
105 
之间的整数。 
⚫ 
--takeTimeout：从连接池中获取连接的最长等待时间，单位为秒，默认为60秒，
取值范围为“1-2147483647” 之间的整数。 
⚫ 
--idleTimeoutMinutes：连接的空闲超时时间，单位为分。默认为10分钟，取
值范围为“1-2147483647” 之间的整数。 
⚫ 
--matchConnections：获取连接时由资源适配器进行匹配，默认为false。 
⚫ 
--transactionSupport：连接池的事务支持类型，默认值为NoTransaction。用
此参数指定时，其取值是NoTransaction、LocalTransaction和XATransaction
中的任意一个。 
⚫ 
--properties：属性。取决于所使用的适配器。格式为key:value，如果有多项
则用;隔开。 
⚫ 
pool_name：必选，目标参数，JCA连接池名称。名称由数字、字母、下划线、
'-'和'/'组成，首字符为英文，尾字符不能为'/'。 
实例 
create-connector-connection-pool --adapter genericra --definition 
javax.jms.ConnectionFactory test 或者create-connector-connection-pool 
--adapter genericra --definition javax.jms.ConnectionFactory --minSize=11 
--maxSize=101 --takeTimeout=60 --idleTimeoutMinutes=10 
--matchConnections=false --transactionSupport=NoTransaction 
--properties=ConnectionFactoryJndiName:test test 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JCA”>“JCA连接池”，进入JCA连接池页面。 
3. 可以查看到JCA连接池test创建成功。 
2.59 delete-connector-connection-pool 
功能说明 
删除具有指定JCA 连接池名称的JCA 连接池资源。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”


## 第 118 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
106 
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
pool_name：必选，目标参数，JCA 连接池名称。 
实例 
执行命令前，请保证test 已经存在。 
⚫ 
在线模式： 
delete-connector-connection-pool test 
⚫ 
离线模式： 
delete-connector-connection-pool --offline=true    test 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JCA”>“JCA连接池”，进入JCA连接池页面。 
3. 可以查看到JCA连接池test已经删除成功。 


## 第 119 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
107 
2.60 list-connector-connection-pools 
功能说明 
获取已创建的JCA 连接池资源。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-connector-connection-pools 


## 第 120 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
108 
⚫ 
离线模式： 
list-connector-connection-pools --offline=true 
2.61 create-threadpool 
功能说明 
创建具有指定名称的JCA 线程池。 
不支持离线模式，离线模式下无法执行相关类加载的逻辑。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--minjcathreads：线程池内的核心线程数，最小线程数，默认为“10”，，取


## 第 121 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
109 
值范围为“0-2147483647”之间的整数。初始线程数不能大于最大线程数。 
⚫ 
--maxjcathreads：线程池内的最大线程数，默认为“200”，取值范围为
“1-2147483647”之间的整数。 
⚫ 
--waitqueue：等待队列，当核心线程全部被占用时，新的任务将被保存在等待
队列中，默认为“100” ，取值范围为“1-2147483647”之间的整数。 
⚫ 
--threadtimeout：线程空闲时间，超出核心线程数的线程如果在该空闲时间内
没有收到新的任务，则销毁该线程，单位为秒，配置为0表示关闭线程空闲超时，
默认为“3600”，取值范围为“0-2147483647”之间的整数。 
⚫ 
pool_name：必选，目标参数，JCA线程池的名称，唯一标识符。名称由数字、
字母、下划线、'-'和'/'组成，首字符为英文，尾字符不能为'/'。 
实例 
create-threadpool --minjcathreads=10 --maxjcathreads=200 --waitqueue=10 
--threadtimeout=3600 test 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JCA”>“JCA线程池”，进入JCA线程池页面。 
3. 可以查看到JCA线程池test已经成功创建。 
2.62 delete-threadpool 
功能说明 
删除具有指定名称的JCA 线程池。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 


## 第 122 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
110 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
pool_name：必选，目标参数，JCA 线程池的名称。 
实例 
执行命令前，请保证test 已经存在。 
⚫ 
在线模式： 
delete-threadpool test 
⚫ 
离线模式： 
delete-threadpool --offline=true test 
验证方式 
4. 登录TongWeb管理控制台。 
5. 左侧导航栏中，选择“JCA”>“JCA线程池”，进入JCA线程池页面。 
6. 可以查看到JCA线程池test已经删除成功。 
2.63 list-threadpools 
功能说明 
获取已创建的JCA 线程池。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 


## 第 123 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
111 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-threadpools 
⚫ 
离线模式： 
list-threadpools --offline=true 
2.64 create-adapter-adminobject 
功能说明 
创建托管对象资源。 
不支持离线模式，离线模式下无法执行相关类加载的逻辑。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为


## 第 124 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
112 
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--restype：目的地类型，默认值为javax.jms.Queue。用该参数指定时取值为
javax.jms.Queue、javax.jms.Topic中的任意一个。 
⚫ 
--adapter：连接工厂所使用的资源适配器，默认为genericra。也可是其他的
已部署好的资源适配器。 
⚫ 
--properties：属性。取决于所使用的适配器。格式为key:value，如果有多项
则用;隔开。 
⚫ 
destination_name：必选，目标参数，目的地名称。 
实例 
create-adapter-adminobject --adapter=genericra --restype=javax.jms.Topic 
test 


## 第 125 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
113 
或者 
create-adapter-adminobject --restype=javax.jms.Queue --adapter=genericra 
--properties=DestinationJndiName:test test 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JCA”>“托管对象资源”，进入托管对象资源页面。 
3. 可以查看到托管对象资源test已经成功创建。 
2.65 delete-adapter-adminobject 
功能说明 
删除托管对象资源。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 


## 第 126 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
114 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
adminobject_name：必选，目标参数，托管对象资源jndi 名称。 
实例 
执行命令前，请保证test 已经存在。 
⚫ 
在线模式： 
delete-adapter-adminobject test 
⚫ 
离线模式： 
delete-adapter-adminobject --offline=true test 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JCA”>“托管对象资源”，进入托管对象资源页面。 
3. 可以查看到托管对象资源test已经删除成功。 
2.66 list-adapter-adminobject 
功能说明 
获取已创建的托管资源对象。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 


## 第 127 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
115 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
list-adapter-adminobject 
⚫ 
离线模式： 
list-adapter-adminobject --offline=true 
2.67 create-connector-security-map 
功能说明 
为指定JCA 连接池创建安全性映射。如果不存在安全性映射，则会创建新的安全性
映射。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 


## 第 128 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
116 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--poolname：必选，JCA连接池名称，为必要参数。 
⚫ 
--principals：主体。该项与usergroups只能选择其一。调用方的身份，即在
访问带安全的应用时，成功登陆的用户的身份，可以用已定义的主体或用户组
代表。 
⚫ 
--usergroups：必选，用户组。名称由数字、字母、下划线和“-”组成，首字
符为英文。 
⚫ 
--mappedusername：必选，访问EIS所需的用户名，为必要参数。名称由数字、
字母、下划线和“-”组成，首字符为英文。 
⚫ 
--mappedpw：必选，访问EIS所需的密码。为必要参数。 
⚫ 
security_name：必选，目标参数，安全映射名称名称，由数字、字母、下划线、
“-”和“/”组成，首字符为英文，尾字符不能为“/”。 
实例 
⚫ 
在线模式： 
create-connector-security-map --poolname=testpool 
--usergroups=eis_groups --mappedusername=hewj --mappedpw=test 
testpoolmap 
⚫ 
离线模式： 
create-connector-security-map --poolname=xc-test 


## 第 129 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
117 
--usergroups=eis_groups --mappedusername=hewj --mappedpw=test 
--offline=true testpoolmap 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JCA”>“JCA连接池”，进入JCA连接池页面。 
3. 单击目标JCA连接池testpool所在行的“安全映射”，进入安全映射管理页面。 
4. 可以查看到安全映射testpoolmap已经创建成功。 
2.68 delete-connector-security-map 
功能说明 
删除指定JCA 连接池的安全性映射。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 


## 第 130 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
118 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
--poolname：必选，JCA 连接池名称，为必要参数。 
security_name：必选，目标参数，安全映射的名称。 
实例 
执行命令前，请保证testpool 已经存在。 
⚫ 
在线模式： 
delete-connector-security-map --poolname=testpool testpoolmap 
⚫ 
离线模式： 
delete-connector-security-map --poolname=testpool --offline=true 
testpoolmap 
验证方式 
1. 登录TongWeb管理控制台。 
2. 左侧导航栏中，选择“JCA”>“JCA连接池”，进入JCA连接池页面。 
3. 单击目标JCA连接池testpool所在行的“安全映射”，进入安全映射管理页面。 
5. 可以查看到安全映射testpoolmap已经删除。 
2.69 list-connector-security-maps 
功能说明 
列出属于指定连接器连接池的安全性映射。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 


## 第 131 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
119 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
pool_name：必选，目标参数，JCA 连接池名称。名称由数字、字母、下划线、'-'
和'/'组成，首字符为英文，尾字符不能为'/'。 
实例 
执行命令前，请保证testpool 已经存在。 
⚫ 
在线模式： 
list-connector-security-maps testpool 
⚫ 
离线模式： 
list-connector-security-maps --offline=true testpool 
2.70 version 
功能说明 
查看TongWeb 的版本号。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 


## 第 132 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
120 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
version 
⚫ 
离线模式： 
version --offline=true 
2.71 web-container-config 
功能说明 
查看web 容器参数配置。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 


## 第 133 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
121 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
web-container-config 
⚫ 
离线模式： 
web-container-config --offline=true 
2.72 update-web-container-config 
功能说明 
更新web 容器参数配置。 
不支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为


## 第 134 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
122 
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--jvmroute：在负载均衡场景中所必须的唯一标识，以支持session亲和。名称
由数字、字母、下划线和'-'组成，首字符为英文。 
⚫ 
--jspdevelopment：启用JSP开发模式。默认为“true”。 
⚫ 
--parameterencoding：默认请求参数解码字符集，此属性修改后需要重启服务
器才能生效。默认为“GBK”，可选择为“GBK”、“UTF-8”、“ISO-8859-1”、
“US-ASCII”。 
⚫ 
--responseencoding：默认应答编码字符集，此属性修改后需要重启服务器才
能生效。默认为“GBK”，可选择为“GBK”、“UTF-8”、“ISO-8859-1”、“US-ASCII”。 
⚫ 
--sessiontimeout：session超时时间，以分钟为单位。默认为“30”，取值范


## 第 135 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
123 
围为“1-2147483647” 之间的整数。 
⚫ 
--xbe：禁止引入外部xml文件，取值范围[true|false]，默认为“false”。 
⚫ 
--htt：hungThreadThreshold：超时线程阈值。默认为“0”，以秒为单位，取
值范围[1-2147483647]，大于0则启用超时线程日志。取值范围为
“1-2147483647” 之间的整数。 
⚫ 
--uld：应用退休超时时间，默认为“2”，以秒为单位，取值范围[0-600]的整
数。 
⚫ 
--awcr：启用META-INF/resources，true/false。默认为“false”。是否将
WEB-INF/classes/META-INF/resources作为静态资源目录，Servlet3及以上有
效。 
⚫ 
--hv：主机名验证器，用于验证SSL连接的主机名是否被篡改。取值范围
[TWHostnameVerifier|NullHostnameVerifier|CustomerHostnameVerifier:Fu
llClassName]。TW主机名验证器和自定义主机名验证器。 
⚫ 
--sl：session复制日志开关，取值范围[true|false]，默认为“false”。 
⚫ 
--cmts：开启http慢攻击检测时有效。完整请求时间，单位为秒，默认为“0”，
取值范围[1-2147483647]。 
⚫ 
--mat：开启http慢攻击检测时有效。慢攻击容忍次数，默认为“3”，取值范
围[1-2147483647]，大于0会启用http慢攻击检测。 
⚫ 
--beh：开启http慢攻击检测时有效。黑名单移除时间，单位为小时，默认为“12”，
取值范围[1-2147483647]。 
⚫ 
--icc：开启http慢攻击检测时有效。中断当前连接，默认为“true”，取值范
围[true|false]。 
⚫ 
--hgg：防host头攻击，默认为“false”，取值范围[true|false]。 
⚫ 
--hggw：开启防host头攻击时有效，主机名白名单。多个主机名以英文逗号分
隔。 
⚫ 
--ecsm：开启反爬虫管理，防止利用爬虫攻击导致session创建过多问题，取值
范围[true|false]，默认false。 
⚫ 
--sii：爬虫会话超时时间，默认“60”，单位为“秒”，取值范围为“0-2147483647” 
之间的整数。 


## 第 136 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
124 
⚫ 
--cip：通过正则表达式识别并匹配指定的爬虫IP，默认为空。 
⚫ 
--cua ：通过正则表达式识别并匹配指定的爬虫User-Agent ，默认
为.*[bB]ot.*|.*Yahoo! Slurp.*|.*Feedfetcher-Google.*。 
实例 
update-web-container-config --jvmroute=a1 --jspdevelopment=false 
--parameterencoding=GBK --responseencoding=GBK --sessiontimeout=60 
--sl=false --htt=180 --hv=TWHostnameVerifier --cmts=60 --mat=10 --beh=1 
--icc=true --hgg=false --hggw=127.0.0.1 
2.73 server-log-config 
功能说明 
查看系统日志参数配置。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交


## 第 137 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
125 
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
- 
实例 
⚫ 
在线模式： 
server-log-config 
⚫ 
离线模式： 
server-log-config --offline=true 
2.74 update-server-log-config 
功能说明 
更新系统日志参数配置。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 


## 第 138 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
126 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--verbose：是否在命令行输出系统日志信息，默认“true”。 
⚫ 
--rotation：是否开启系统日志的轮转，默认为“true”。 
⚫ 
--rotationtype：系统日志轮转类型，可选值为bysize、bytime、byday。分别对应
“按大小轮转”、“按周期轮转”、“按天轮转”。默认为“bysize”。 
⚫ 
--rotationvalue：系统日志轮转数值，该数值由数字和单位组成。 
◼ 
系统日志轮转类型为bysize时，单位可选KB或MB。当配置超过100MB时，
以100MB为准，默认为“50MB”。 
◼ 
系统日志轮转类型为bytime时，单位可选H或D，当配置超过10D（10天）
时，以10D为准。 
◼ 
系统日志轮转类型为byday时，不需要填写该数值。 
⚫ 
--filecount：系统日志超过该数量后，则会自动删除较早的日志文件，默认为
“20”。当设置为“0”时，表示日志数量不限制。 
⚫ 
--asynclogOn：是否启用异步日志，true/false，默认为“false”。 
⚫ 
--serverlogDir：日志目录。设置系统日志目录，不填默认设置为服务器根目录下
的logs目录。 
⚫ 
--capacity：异步日志队列缓存数。默认为“2147483647”，无界队列。 
⚫ 
--threadNum：异步日志线程数，默认值为“1”，推荐配置也为“1”。开启异
步日志后，可配置。取值范围为“1-2147483647” 之间的整数。 
实例 
⚫ 
在线模式： 
update-server-log-config --verbose=true --rotation=true 
--rotationtype=bysize --rotationvalue=100MB --filecount=50 
⚫ 
离线模式： 
update-server-log-config --verbose=true --rotation=true 


## 第 139 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
127 
--rotationtype=bysize --rotationvalue=100MB --filecount=50 
--offline=true 
2.75 set-jvm-arg 
功能说明 
配置启动脚本JVM 参数。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
--arg：jvm 参数。每次只能加一个参数。 


## 第 140 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
128 
实例 
⚫ 
在线模式： 
set-jvm-arg --arg=-Xmx1024m 
⚫ 
离线模式： 
set-jvm-arg --arg=-Xmx1024m --offline=true 
2.76 delete-jvm-arg 
功能说明 
删除启动脚本JVM 参数。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 


## 第 141 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
129 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
--arg：必选，jvm 参数。 
实例 
⚫ 
在线模式： 
delete-jvm-arg --arg=-Xmx1024m 
⚫ 
离线模式： 
delete-jvm-arg --arg=-Xmx1024m --offline=true 
2.77 set-server-arg 
功能说明 
设置启动脚本服务器参数。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 


## 第 142 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
130 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
--arg=-Dxxx=yyy：必选,服务器参数名和值。xxx 为参数名，yyy 为参数值。 
实例 
⚫ 
在线模式： 
set-server-arg --arg=-DWebModuleOnly=true 
⚫ 
离线模式： 
set-server-arg --arg=-Dhahaha=true --offline=true 
2.78 generate-tdg-token 
功能说明 
生成TDG 服务的token 加密字符串。不支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 


## 第 143 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
131 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
--tongdatagrid_group_name：必填，目标参数，TDG 缓存集群组名称。 
--tongdatagrid_group_password：可选，自定义缓存集群组密码。 
实例 
在线模式： 
generate-tdg-token --tongdatagrid_group_name=admin 
--tongdatagrid_group_password=admin123.com 
返回结果： 
返回访问TDG 服务的token 加密字符串 
使用说明： 
例如：在单机控制台创建了TDG 类型的session 管理器，组名是 admin 密码是
admin123.com。 
1. 
如果要保证连上TDG服务端，那么TDG服务端也要配置相同的组名和组密码。
这时就要依靠generate-tdg-token命令行通过输入原组名和原密码，生成token串即
组密码加密串。 
2. 
此处需要手动编辑TDG服务配置文件（如 
${TongWeb_HOME}/TongDataGrid/bin/tongdatagrid.xml），修改组名为admin，
组密码为命令行输出的加密token串。 
2.79 delete-server-arg 
功能说明 
设置启动脚本服务器参数。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP


## 第 144 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
132 
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
arg-name：必选，目标参数，服务器参数名。 
实例 
⚫ 
在线模式： 
delete-server-arg WebModuleOnly 
⚫ 
离线模式： 
delete-server-arg --offline=true WebModuleOnly 
2.80 create-sharedlib 
功能说明 
创建共享库。 
不支持离线模式，离线模式下无法执行相关类加载的逻辑。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 


## 第 145 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
133 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
⚫ 
--sharedpath：必选，共享库目录，需要提前将共享jar包拷贝到服务器上的一
个指定目录。 
⚫ 
--sharedtype：共享库类型，public/private，默认为“public”。 
⚫ 
sharedLib_name：必选，目标参数，共享库名称。 
实例 
⚫ 
创建公有共享库： 
create-sharedlib --sharedpath=/home/test/HelloWorldJar.jar shared1 
⚫ 
创建私有共享库： 
create-sharedlib --sharedpath=/home/test/HelloWorldJar.jar 
--sharedtype=private shared1 
注意事项 
执行命令创建之后，文件集和共享库均被创建为相同的名称，即指定的共享库名，


## 第 146 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
134 
如shared1。 
2.81 delete-sharedlib 
功能说明 
删除共享库。 
不支持离线模式，离线模式下无法执行相关类加载的逻辑。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
相关参数 
sharedLib_name：必选，目标参数，共享库名称。 
实例 
delete-sharedlib shared1 


## 第 147 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
135 
注意事项 
执行命令删除之后，文件集和共享库均被删除，如shared1。如果被该共享库被应用
占用则无法删除。 
2.82 update-license 
功能说明 
更新License。支持离线模式。 
基本参数 
⚫ 
--terse：修改命令行日志输出级别，true为INFO，false为FINE，默认“false”。 
⚫ 
--echo：将一条完整的命令反馈出来，默认为“false”不反馈出来。可设置为
“true”或者“false”。 
⚫ 
--interactive：是否使用交互方式执行命令。“true”使用交互方式，“false”
不使用交互方式。默认为“true”。不设置该参数时，采用默认值。 
⚫ 
--host：用于远程连接。若需要连接远程服务器，host代表需要连接的远程IP
地址。默认“localhost”。 
注意：命令行中的host禁止远程连接。 
⚫ 
--port：待连接的端口，默认为“9060”。不设置该参数时，采用默认值。 
⚫ 
--secure：可选，boolean类型，可以写为“--secure”或者“-s”，选择http/https
访问服务器。默认为“false”，即“http”。 
当system-http-listener通道设为https后，使用命令行工具前需要先手动修改配置文
件“${TongWeb_HOME}/conf/commandsenv.conf）”。 
◼ 
设置AS_ADMIN_SECURE=true。 
◼ 
https通道支持的协议必须支持AS_ADMIN_PROTOCOL的值（默认SSLv3）。 
修改完成后，该参数默认值变更为“true”（即“https”）。所有命令行若设置
此参数，则需要设置为“true”。 
⚫ 
--user：执行命令的用户名。 
⚫ 
--password：进行交互认证时认证用户所需的密码。如不填写，则专门进行交
互输入。默认为“cli123.com”。 
⚫ 
--passwordfile：保存用户密码的文件（文件中的属性名必须是
AS_ADMIN_password,如：AS_ADMIN_password=cli123.com）。 
⚫ 
--offline：命令行离线模式，默认不开启“false”。 
相关参数 
⚫ 
--licenseType：如果配置了licenseIps或者publicKey就必须配licenseType才能生效。


## 第 148 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
136 
licenseType支持remote或者active两种。 
◼ 
remote：表示远程模式，调用远程授权管理平台License Server，加载授权证
书，校验授权证书内容。 
◼ 
active：既支持从本地（“${TongWeb_HOME}/active”目录）读取license.dat
文件，也支持从License Server平台加载授权证书进行授权认证。 
⚫ 
--licenseIps：若选择更新为License Server服务提供License认证，则设置License 
Server的IP+端口。多个IP+端口以英文逗号分隔。 
⚫ 
--publicKey：License Server 秘钥，需要从 License Server 获取。 
例如：update-license --licenseType =remote --licenseIps=127.0.0.1:8888,127.0.0.1:8889 
--publicKey=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsD9sFJrfF
banWDp3tQRcWAkXA9ibNZcIJklqZSUX+cSKBVmEYMzk3jK+aZTiwz8ilJxoHR1YP8
EEGnVWOYwkhvCDqTe+/hGeTKnx9Ia5RQjFDYA3MaxQqD9AZBQfBtnhvq7VcE2e5
zcuDiPz5phwD/9GNM9l+n+wSACpafx6Zi9kw/fZMmsgvcVjdyMMi9v9NFm0d/XJWJH
GR5fg48zNIz46JJmQ5TuHvF5go/8u3JowsCBgdmcY1xFtc4ztLD3AOfDZfZ7cULl5lhpr2
OagnDNCuCWxniULhP+5qWgDnqOhhlWPWc+5s9FyzERIkS5pes6vDtDEXCRgxFCW
mu4aK 
注意事项 
若使用License 文件进行License 认证，动态替换License 文件前需要将最新的
license.dat 文件以ftp 或其他方式拷贝到${TongWeb_HOME}/license_update 目录下。 
实例 
⚫ 
在线模式： 
update-license 
⚫ 
离线模式： 
update-license  --offline=true 


## 第 149 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
137 
附录A 术语及缩略语 
名称 
说明 
TongWeb(简称TW) 
东方通应用服务器 
${TongWeb_HOME} 
TongWeb 的安装路径 
JVM 
Java Virtual Machine，Java 虚拟机 
AJP 
Apache JServ Protocol，定向包协议 
JDBC 
Java Database Connectivity，Java 数据库连接 
SNMP 
简单网络管理协议 
TongWeb 域 
逻辑服务器管理 


## 第 150 页

东方通应用服务器软件TongWeb_V7.0Commandstool 使用指南 
7049_M9A01 
版权所有©东方通 
138 
 



## 第 1 页

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


## 第 2 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
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

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
ii 
版本变更说明 
本手册的更新是累积的。因此，最新的手册版本包含对以前版本所做的所有更改。 
手册版本 
适用于产品版本 
更新内容 
7049_M9A01 7.0.4.9_M9 
无 
7049_M8A01 7.0.4.9_M8 
无 
7049_M7A01 7.0.4.9_M7 
无 
7049_M6A01 7.0.4.9_M6 
无 
7049_M5A01 7.0.4.9_M5 
无 
7049_M4A01 7.0.4.9_M4 
无 
7049_M3A01 7.0.4.9_M3 
无 
7049_M2A01 7.0.4.9_M2 
无 
7049_M1A01 7.0.4.9_M1 
无 
7049A01 
7.0.4.9 
无 
7048A01 
7.0.4.8 
无 
7047A01 
7.0.4.7 
无 
7046A01 
7.0.4.6 
无 
7045A01 
7.0.4.5 
无 
7044A01 
7.0.4.4 
无 
7043A01 
7.0.4.3 
无 
7042A01 
7.0.4.2 
无 
7041A01 
7.0.4.1 
⚫ 统一使用TongWeb用户使用手册模板。 
⚫ 更名及整合原《IBM TIVOLI集中监控返回json使用手册》。 
 


## 第 4 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
iii 
前言 
本文档是TongWeb产品的用户使用手册之一，对JSON整体结构及各监视项的进行详细说明。 
 
适合的对象  
本手册主要适用于生产环境中的系统管理员，部分内容同样适用于应用开发人员和应用部署人员。  
本手册假定您已经具备如下技能：  
1. 
基本系统管理任务； 
2. 
安装软件； 
3. 
使用Web浏览器； 
4. 
启动数据库服务器； 
5. 在终端窗口中发布命令。 
 
用户使用手册集 
TongWeb为您提供的用户使用手册集包含的文档有：  
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
⚫ 100_TongWeb_V7.0集群管理指南：详细介绍集群的配置和管理。 
⚫ 200_TongWeb_V7.0用户使用手册-轻量级版：提供轻量级版本客户详细的服务配置及应用管理的说
明。 
 
技术支持 
东方通产品将为您提供全方位的技术支持，您可以通过以下方式获得技术支持：  
网址：www.tongtech.com  
电话：400-650-7088 
邮箱：support@tongtech.com 


## 第 5 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
iv 
 
您在取得技术支持时，请提供如下信息：  
1.  您的姓名  
2.  您的公司信息  
3.  您的联系方式  
4.  操作系统及其版本  
5.  产品版本号  
6.  日志等错误的详细信息 
 


## 第 6 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
v 
目 录 
第1章 Json整体结构说明 ................................................................................................................................. 1 
1.1 地址格式 ................................................................................................................................................. 1 
1.2 返回json示例 ........................................................................................................................................... 1 
第2章 监视项说明 ............................................................................................................................................. 2 
2.1 告警指标项 ............................................................................................................................................. 2 
2.2 垃圾回收监视项 ..................................................................................................................................... 2 
2.3 JDBC监视项 ............................................................................................................................................ 5 
2.4 线程池监视项 ......................................................................................................................................... 8 
2.5 应用程序状态监视项 ............................................................................................................................ 11 
2.6 应用程序会话监视项 ........................................................................................................................... 13 
附录A 
术语及缩略语 ................................................................................................................................... 15 


## 第 7 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
1 
第1章 Json整体结构说明 
因为需求是要求获取所有节点的监控状态，所以需要启动TongWeb的集中管理工具，管理节点。IBM端
可定时获取所有监视量的信息。 
1.1 地址格式 
http://masterIP:masterPort/heimdall/notinrealm/rest/monitor/ibm/view 
1.2 返回json示例 
 
图 1.2-1：返回json示例 
返回json 格式： 
nodes：代表节点集合。每个集合里面包括： 
⚫ 
nodeHome：节点路径 
⚫ 
nodeIp：节点IP 
⚫ 
nodeStatus：节点状态，started代表已启动、stopped代表已停止。如果为“--”则代表无法与节点所
在机器agent正常连接。 
⚫ 
monitorList：节点获取到的监视量列表。monitorList中每一个对象都是固定的json格式。 
◼ 
appname：应用名称 
◼ 
dbname：数据源名称 
◼ 
servletName：servlet名称，因为应用和数据源是有多个的情况，比如相同的应用监视量对应
着不同的应用名则可以通过该属性进行定位。如果都不属于这几种类型，这个属性则为空。 
◼ 
monitorName：监视量名称 
◼ 
monitorType：监视量类型 
◼ 
monitorValue：监视量值 


## 第 8 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
2 
第2章 监视项说明 
2.1 告警指标项 
获取monitorList下monitorType为“warn”的对象。 
表 2.1-1：告警指标项 
monitorName 
说明 
UsedHeapSizePerce
nt 
堆内存占用百分比，用于HXB_YN_JVMHeap_AVG5_Pct_A 
HXB_YN_JVMHeap_AVG10_Pct_A的计算 
示例： 
{ 
          "appname": "", 
          "dbname": "", 
          "monitorName": "UsedHeapSizePercent", 
          "monitorType": "warn", 
          "monitorValue": "15.56%", 
"threadPoolName": "", 
          "servletName": "" 
 } 
 
2.2 垃圾回收监视项 
获取monitorList下monitorType为“gc”的对象。 
表 2.2-1：垃圾回收监视项 
monitorName 
说明 
Process_ID 
对应Process_ID，理解为JVM进程ID 
Times_Run 
对应Times_Run，返回的是GC次数 
Real_Time 
对应Real_Time，理解为GC时间。 
Real_Time_Percent 
 
对应Real_Time_Percent，GC时间占比。 
计算方式：GC时间/（当前时间-启动时间） 
GC_Rate 
对应GC_Rate，GC次数占比。 
计算方式：GC次数/（当前时间-启动时间） 
Heap_Used_Percent 
对应Heap_Used_Percent 
Kbytes_Used 
对应Kbytes_Used，理解为正在使用的堆大小 
Kbytes_Free 
对应Kbytes_Free， 
计算方式：总的堆内存-使用的堆内存 


## 第 9 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
3 
示例： 
{ 
          "appname": "", 
          "dbname": "", 
          "monitorName": "Process_ID", 
          "monitorType": "gc", 
          "monitorValue": "7944", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
        { 
          "appname": "", 
          "dbname": "", 
          "monitorName": "Times_Run", 
          "monitorType": "gc", 
          "monitorValue": "56", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
        { 
          "appname": "", 
          "dbname": "", 
          "monitorName": "Real_Time", 
          "monitorType": "gc", 
          "monitorValue": "9619", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
        { 
          "appname": "", 
          "dbname": "", 
          "monitorName": "Real_Time_Percent", 
          "monitorType": "gc", 
          "monitorValue": "0.09%", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
        { 


## 第 10 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
4 
          "appname": "", 
          "dbname": "", 
          "monitorName": "GC_Rate", 
          "monitorType": "gc", 
          "monitorValue": "52.563", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
        { 
          "appname": "", 
          "dbname": "", 
          "monitorName": "Heap_Used_Percent", 
          "monitorType": "gc", 
          "monitorValue": "15.56%", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
        { 
          "appname": "", 
          "dbname": "", 
          "monitorName": "Kbytes_Used", 
          "monitorType": "gc", 
          "monitorValue": "72531.109", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
        { 
          "appname": "", 
          "dbname": "", 
          "monitorName": "Kbytes_Free", 
          "monitorType": "gc", 
          "monitorValue": "465977.169", 
"threadPoolName": "", 
          "servletName": "" 
        }, 
 


## 第 11 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
5 
2.3 JDBC监视项 
获取monitorList下monitorType为“db”的对象，dbName为JDBC连接池对应的名称。 
表 2.3-1：JDBC监视项 
monitorName 
说明 
Connections_Created 
该连接池创建的全部连接数。 
Connections_Destroyed 
该连接池销毁的全部连接数。 
Connections_Allocated 
当前连接池大小。 
Return_Count 
归还到连接池中的连接数。 
Maximum_Pool_Size 
连接池的连接数量上限。 
ConnectionHandle 
当前正在使用的连接数。 
Threads_Timed_Out 
在连接池中获取连接时超时的数量。 
示例： 
{ 
                    "appname": "", 
                    "dbname": "testdb", 
                    "monitorName": "Connections_Created", 
                    "monitorType": "db", 
                    "monitorValue": "20", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "testdb", 
                    "monitorName": "Connections_Destroyed", 
                    "monitorType": "db", 
                    "monitorValue": "0", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "testdb", 
                    "monitorName": "Connections_Allocated", 
                    "monitorType": "db", 
                    "monitorValue": "20", 


## 第 12 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
6 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "testdb", 
                    "monitorName": "Return_Count", 
                    "monitorType": "db", 
                    "monitorValue": "20", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "testdb", 
                    "monitorName": "Maximum_Pool_Size", 
                    "monitorType": "db", 
                    "monitorValue": "20", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "testdb", 
                    "monitorName": "ConnectionHandle", 
                    "monitorType": "db", 
                    "monitorValue": "0", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "testdb", 
                    "monitorName": "Threads_Timed_Out", 
                    "monitorType": "db", 
                    "monitorValue": "0", 
"threadPoolName": "", 
                    "servletName": "" 


## 第 13 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
7 
                }, 
                { 
                    "appname": "", 
                    "dbname": "test2", 
                    "monitorName": "Connections_Created", 
                    "monitorType": "db", 
                    "monitorValue": "10", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "test2", 
                    "monitorName": "Connections_Destroyed", 
                    "monitorType": "db", 
                    "monitorValue": "0", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "test2", 
                    "monitorName": "Connections_Allocated", 
                    "monitorType": "db", 
                    "monitorValue": "10", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "test2", 
                    "monitorName": "Return_Count", 
                    "monitorType": "db", 
                    "monitorValue": "10", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 


## 第 14 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
8 
                    "appname": "", 
                    "dbname": "test2", 
                    "monitorName": "Maximum_Pool_Size", 
                    "monitorType": "db", 
                    "monitorValue": "100", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "test2", 
                    "monitorName": "ConnectionHandle", 
                    "monitorType": "db", 
                    "monitorValue": "0", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
                { 
                    "appname": "", 
                    "dbname": "test2", 
                    "monitorName": "Threads_Timed_Out", 
                    "monitorType": "db", 
                    "monitorValue": "0", 
"threadPoolName": "", 
                    "servletName": "" 
                }, 
 
2.4 线程池监视项 
获取monitorList下monitorType为“threadpool”的对象。 
表 2.4-1：线程池监视项 
monitorName 
说明 
Summary_of_Thread_Pools 
当前(通道)线程池总数 
Thread_pool_name 
当前线程池名称 
Maximum_Pool_Size 
当前线程池最大值 
Threads_Created 
采样周期内线程创建个数 
Threads_Destroyed 
采样周期内线程销毁个数 


## 第 15 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
9 
Threads_Created_Rate 
采样周期内线程创建速率 
Thread_Destruction_Rate 
采样周期内线程销毁速率 
Average_Active_Threads 
活动线程平均数 
Average_Pool_Size 
线程池线程大小平均数 
Average_Free_Threads 
空闲线程平均数 
示例： 
   { 
     "appname":"", 
      "dbname":"", 
      "monitorName":"Summary_of_Thread_Pools", 
      "monitorType":"threadpool", 
      "monitorValue":"4", 
"threadPoolName":"http-nio-8084", 
      "servletName":"" 
   }, 
   { 
    "appname":"", 
    "dbname":"", 
    "monitorName":"Thread_pool_name", 
    "monitorType":"threadpool", 
    "monitorValue":"http-nio-8084", 
"threadPoolName":"http-nio-8084", 
    "servletName":"" 
    }, 
    { 
     "appname":"", 
     "dbname":"", 
     "monitorName":"Maximum_Pool_Size", 
     "monitorType":"threadpool", 
     "monitorValue":"200", 
"threadPoolName":"http-nio-8084", 
     "servletName":"" 
    }, 
    { 
    "appname":"", 
     "dbname":"", 
      "monitorName":"Threads_Created", 
      "monitorType":"threadpool", 


## 第 16 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
10 
      "monitorValue":"0", 
"threadPoolName":"http-nio-8084", 
      "servletName":"" 
    }, 
    { 
     "appname":"", 
      "dbname":"", 
      "monitorName":"Threads_Destroyed", 
      "monitorType":"threadpool", 
      "monitorValue":"0", 
"threadPoolName":"http-nio-8084", 
      "servletName":"" 
    }, 
    { 
     "appname":"", 
     "dbname":"", 
     "monitorName":"Threads_Created_Rate", 
     "monitorType":"threadpool", 
     "monitorValue":"0", 
"threadPoolName":"http-nio-8084", 
     "servletName":"" 
    }, 
    { 
     "appname":"", 
     "dbname":"", 
     "monitorName":"Thread_Destruction_Rate", 
      "monitorType":"threadpool", 
      "monitorValue":"0", 
"threadPoolName":"http-nio-8084", 
      "servletName":"" 
    }, 
    { 
    "appname":"", 
    "dbname":"", 
    "monitorName":"Average_Active_Threads", 
    "monitorType":"threadpool", 
    "monitorValue":"0", 
"threadPoolName":"http-nio-8084", 


## 第 17 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
11 
    "servletName":"" 
    }, 
    { 
     "appname":"", 
     "dbname":"", 
     "monitorName":"Average_Pool_Size", 
     "monitorType":"threadpool", 
     "monitorValue":"10", 
"threadPoolName":"http-nio-8084", 
     "servletName":"" 
     }, 
     { 
      "appname":"", 
      "dbname":"", 
      "monitorName":"Average_Free_Threads", 
      "monitorType":"threadpool", 
      "monitorValue":"10", 
"threadPoolName":"http-nio-8084", 
      "servletName":"" 
     }, 
2.5 应用程序状态监视项 
获取monitorList下monitorType为“application”的对象。 
表 2.5-1：应用程序状态监视项 
monitorName 
说明 
Status 
应用服务器启动状态，启动为true。 
Version 
应用服务器产品版本号，如6.0.0.0。 
Start_Date_and_Time 
应用服务器启动时间。 
Process_ID 
应用服务器进程ID。 
CPU_Used 
应用服务器JVM进程CPU占用时间，单位毫秒。 
CPU_Used_Percent 
应用服务器JVM进程CPU占用比率。 
示例： 
  { 
      "appname":"", 
      "dbname":"", 
      "monitorName":"Status", 
      "monitorType":"application", 


## 第 18 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
12 
      "monitorValue":"true", 
      "servletName":"" 
    }, 
    { 
      "appname":"", 
      "dbname":"", 
      "monitorName":"Version", 
      "monitorType":"application", 
      "monitorValue":"6.0.0.0", 
      "servletName":"" 
     }, 
     { 
      "appname":"", 
      "dbname":"", 
      "monitorName":"Start_Date_and_Time", 
      "monitorType":"application", 
      "monitorValue":"2017-01-13 11:20:26", 
      "servletName":"" 
      }, 
      { 
       "appname":"", 
       "dbname":"", 
       "monitorName":"Process_ID", 
       "monitorType":"application", 
       "monitorValue":"24041", 
       "servletName":"" 
       }, 
       { 
        "appname":"", 
        "dbname":"", 
        "monitorName":"CPU_Used", 
        "monitorType":"application", 
        "monitorValue":"134240000000", 
        "servletName":"" 
        }, 
        { 
          "appname":"", 
          "dbname":"", 


## 第 19 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
13 
          "monitorName":"CPU_Used_Percent", 
          "monitorType":"application", 
          "monitorValue":"11.22%", 
          "servletName":"" 
        }, 
2.6 应用程序会话监视项 
获取monitorList下monitorType为“application”的对象 
表 2.6-1：应用程序会话监视项 
monitorName 
说明 
Web_Application_Archive 
Web应用部署路径。 
appname 
Web应用名称。 
Summary_of_Servlet_Sessions 
Web应用当前会话总数。 
Sessions_Created 
Web应用创建的会话总数。 
Sessions_Invalidated 
Web应用失效会话总数。 
Session_Creation_Rate 
采样周期内Web应用会话创建速率 
Session_Invalidation_Rate 
采样周期内Web应用会话失效速率 
Average_Session_Lifetime 
Web应用会话平均存活时间 
示例： 
{ 
"appname":"/server/WebTest", 
"dbname":"", 
"monitorName":"Web_Application_Archive", 
"monitorType":"application", 
"monitorValue":"/home/test/hf/Agent/nodes/tongweb-1/deployment/WebTest", 
"servletName":"" 
}, 
{ 
"appname":"/server/WebTest", 
"dbname":"", 
"monitorName":"Summary_of_Servlet_Sessions", 
"monitorType":"application", 
"monitorValue":"0", 
"servletName":"" 
}, 
{ 
"appname":"/server/WebTest", 


## 第 20 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
14 
"dbname":"", 
"monitorName":"Sessions_Created", 
"monitorType":"application", 
"monitorValue":"0", 
"servletName":"" 
}, 
{ 
"appname":"/server/WebTest", 
"dbname":"", 
"monitorName":"Sessions_Invalidated", 
"monitorType":"application", 
"monitorValue":"0", 
"servletName":"" 
}, 
{ 
"appname":"/server/WebTest", 
"dbname":"", 
"monitorName":"Session_Creation_Rate", 
"monitorType":"application", 
"monitorValue":"0", 
"servletName":"" 
}, 
{ 
"appname":"/server/WebTest", 
"dbname":"","monitorName":"Session_Invalidation_Rate", 
"monitorType":"application", 
"monitorValue":"0", 
"servletName":"" 
}, 
{ 
"appname":"/server/WebTest", 
"dbname":"", 
"monitorName":"Average_Session_Lifetime", 
"monitorType":"application", 
"monitorValue":"0", 
"servletName":"" 
}, 


## 第 21 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
15 
附录A 术语及缩略语 
名称 
说明 
TongWeb(简称TW) 
东方通应用服务器 
${TongWeb_HOME} 
TongWeb的安装路径 
JVM 
Java Virtual Machine，Java虚拟机 
AJP 
Apache JServ Protocol，定向包协议 
JDBC 
Java Database Connectivity，Java数据库连接 
SNMP 
简单网络管理协议 
TongWeb域 
逻辑服务器管理 
 


## 第 22 页

东方通应用服务器软件TongWeb_V7.0与Tivoli集成手册 
7049_M9A01 
版权所有©东方通 
16 
 



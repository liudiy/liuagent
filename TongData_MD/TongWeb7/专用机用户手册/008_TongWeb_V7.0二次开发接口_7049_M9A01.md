## 第 1 页

 
V7049A01 
1 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


## 第 2 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
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

东方通应用服务器软件TongWeb_V7.0二次开发接口 
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
修改如下章节： 
2.2.4.12 数据源信息，非XA数据源实时信息表格中新增
ConnectionUsedPercentBaseMaxSize属性。 
7049_M7A01 7.0.4.9_M7 
无 
7049_M6A01 7.0.4.9_M6 
无 
7049_M5A01 7.0.4.9_M5 
新增如下章节： 
3.2 heimdall集群控制台REST接口 
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
修改如下章节： 
⚫ 
2.2.4.12 数据源信息，数据源实时状态列表中新增区分单数据
源与多数据源的isMulti字段。 
⚫ 
2.2.4.12 数据源信息，新增XA数据源实时信息属性列表说明。 
⚫ 
3.1.2 接口地址调用示例，“/rest/api/datasource_detail”接口删
除“attrName”和“pathValue”属性。 
7048A01 
7.0.4.8 
新增如下章节： 
2.3.3 Jconsole通过JMX MP协议登录认证。 
7047A01 
7.0.4.7 
修改如下章节： 
⚫ 
3.2章节 接口地址调用示例：给出findDeadLockedThreads参数
说明：查询死锁线程（开销大） 
⚫ 
2.2.4.4 章节：给出findDeadLockedThreads说明 
⚫ 
3.2章节 接口地址调用示例：给出hungThreads：通道线程池，
执行请求超过配置时间（hungTime）的线程 
⚫ 
3.1章节：给出curl命令执行时，若url中含有‘&’等特殊字符，
url需要加引号。 
7046A01 
7.0.4.6 
⚫ 删除“第3章 REST调用”中描述内容以及“3.1 
HttpClient3”、“3.2 HttpClient4”章节 
⚫ “2.1 获取TongWeb的监视量”更改“说明”描述、“3.1 REST
接口列表”增加“说明”描述 
⚫ “2.2.4.1 JVM内存信息”表2.2-5MemoryUsage属性列表中增
加free属性、free_percent属性 
⚫ “2.2.4.10 TongWeb信息”表2.2-19中增加stateName属性 
⚫ “2.2.4.11 通道信息”表2.2-20HttpListenerMonitor$Count
属性列表中增加maxThreads属性、canConnect属性 
⚫ “2.2.4.12 数据源信息”表2.2-21中增加CreateCount属性、


## 第 4 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
iii 
手册版本 
适用于产品版本 
更新内容 
MaxUseCount属性、AwaitingConnectionFailureCount属性、
AwaitingConnectionHighCount属性、ConnectionUsedPercent
属性 
⚫ “2.2.4.15 应用细节信息”表2.2-25中增加stateName属性 
⚫ “2.2.4.16 应用会话信息”表2.2-26中增加activeSessions
属性 
⚫ “2.1 获取TongWeb的监视量”、“2.2.3 应用管理”、
“2.2.4.11 通道信息”更新JMX service url描述 
⚫ “2.2.4.12 数据源信息”新增“表2.2-23：数据源实时状
态”。“3.1 REST接口列表”的“表3.1-1：REST接口”、“3.2 
接口地址调用示例”的“表3.2-1：REST接口地址调用示例”
新增“获取jdbc健康状态”、“获取http通道健康状态”、
“获取server健康状态”功能 
⚫ “3.1 REST接口列表”更新描述信息 
7045A01 
7.0.4.5 
⚫ “3.3REST接口列表”增加系统日志rest接口和sql日志rest接
口，“3.4接口地址调用示例”增加系统日志和sql日志调用示
例 
⚫ “2.2.4.12数据源信息”增加LeakCount和
AccumlateleakCount监控量 
⚫ 将${TW_HOME}改为${TongWeb_HOME} 
⚫ “2.1.2获取各Mbean的监控数据”更改“注意”描述 
⚫ 修改“第5章 配置监控推送参数及说明” 
⚫ “3.3 REST接口列表”增加免登录访问rest接口参数 
⚫ “REST接口列表”表3.3-1 中添加“查看所有hung线程、查看
hung线程详细、获取慢sql日志”Rest API。“接口地址调用
示例”表3.4-1 中添加“查看所有hung线程、查看hung线程详
细、获取慢sql日志”Rest API调用示例。 
⚫ “3.3 REST接口列表”描述内容增加调用方式；表3.3-1删除
“应用管理列表子模块（仅ear类型才有子模块）、系统日志、
sql日志、根据时间段和执行耗时获取sql日志列表”接口 
⚫ 
“3.4 接口地址调用示例”表3.4-1 删除“应用管理列表子模
块”接口；更新“应用细节信息、应用会话信息、应用类加载
器信息、应用资源缓存信息”接口的描述 
7044A01 
7.0.4.4 
⚫ 更新“表2.2-29：TongWeb信息”和“表4.1-13：TongWeb服务
信息”中port为7090（原来为8005） 
⚫ 更新验证了JMX接口的所有属性及其类型和参考值 
⚫ 移动“系统使用信息”至“2.2.4监视明细”下，删除原“监
视概览” 
⚫ “2.2JMX接口列表中”添加JDK8支持的说明 
⚫ 
增加“第5 章 配置监控推送” 
7043A01 
7.0.4.3 
无 


## 第 5 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
iv 
手册版本 
适用于产品版本 
更新内容 
7042A01 
7.0.4.2 
无 
7041A01 
7.0.4.1 
⚫ 统一使用TongWeb用户使用手册模板。 
⚫ 整合原《TongWeb7二次开发接口》 


## 第 6 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
v 
前言 
本文档是TongWeb产品的用户使用手册之一，详细提供TongWeb的JMX、REST、SNMP接口说明。 
 
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
邮箱：pqmo@tongtech.com 


## 第 7 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
vi 
 
您在取得技术支持时，请提供如下信息： 
1.  您的姓名  
2.  您的公司信息  
3.  您的联系方式  
4.  操作系统及其版本  
5.  产品版本号  
6.  日志等错误的详细信息 
 


## 第 8 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
vii 
目录 
第1章 TongWeb开发接口概述 ........................................................................................................................... 1 
第2章 JMX使用 ................................................................................................................................................... 1 
2.1 获取TongWeb的监视量 .......................................................................................................................... 1 
2.1.1 获取TongWeb中监控Mbean的ObjectName ................................................................................... 1 
2.1.2 获取各Mbean的监控数据 ............................................................................................................... 1 
2.1.3 获取虚拟机集合 ............................................................................................................................. 2 
2.2 JMX接口列表 ........................................................................................................................................... 2 
2.2.1 WEB容器配置.................................................................................................................................. 2 
2.2.2 JDBC配置......................................................................................................................................... 3 
2.2.3 应用管理 ......................................................................................................................................... 4 
2.2.4 监视明细 ......................................................................................................................................... 6 
2.2.5 监视配置 ....................................................................................................................................... 18 
2.2.6 EJB ................................................................................................................................................. 19 
2.2.7 JCA ................................................................................................................................................. 21 
2.3 使用JMX MP协议 ................................................................................................................................... 23 
2.3.1 开启jmx mp协议 ........................................................................................................................... 23 
2.3.2 使用JMX MP协议 ........................................................................................................................... 24 
2.3.3 Jconsole通过JMX MP协议登录认证 ............................................................................................ 24 
2.4 绑定IPv6的jmx地址 ............................................................................................................................. 24 
第3章 REST调用 ............................................................................................................................................... 24 
3.1 Console控制台REST接口 ..................................................................................................................... 24 
3.1.1 REST接口列表 ............................................................................................................................... 24 
3.1.2 接口地址调用示例 ....................................................................................................................... 26 
3.1.3 请求参数及返回值 ....................................................................................................................... 29 
3.2 heimdall集群控制台REST接口 ............................................................................................................. 31 
3.2.1 REST接口列表 ............................................................................................................................... 31 
3.2.2 返回值格式说明 ........................................................................................................................... 32 
3.2.3 接口地址调用示例 ....................................................................................................................... 32 
第4章 SNMP ....................................................................................................................................................... 39 
4.1 OID列表 ................................................................................................................................................. 39 
4.1.1 操作系统信息 ............................................................................................................................... 39 
4.1.2 java运行时信息 ........................................................................................................................... 39 
4.1.3 java类加载信息 ........................................................................................................................... 41 
4.1.4 java编译信息 ............................................................................................................................... 41 
4.1.5 java内存信息 ............................................................................................................................... 41 
4.1.6 java线程信息 ............................................................................................................................... 42 


## 第 9 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
viii 
4.1.7 java垃圾回收信息 ....................................................................................................................... 43 
4.1.8 JDBC连接池信息 ........................................................................................................................... 43 
4.1.9 Web容器信息 ................................................................................................................................. 45 
4.1.10 线程池信息 ................................................................................................................................. 45 
4.1.11 TongWeb应用信息 ....................................................................................................................... 47 
4.1.12 TongWeb管理信息 ....................................................................................................................... 51 
4.1.13 TongWeb服务信息 ....................................................................................................................... 52 
第5章 配置监控推送 ....................................................................................................................................... 53 
附录A 术语及缩略语 ....................................................................................................................................... 54 
 


## 第 10 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
1 
第1章 TongWeb开发接口概述 
TongWeb的应用开发所涉及的领域包括Web、EJB、JPA等，TongWeb为了提高用户在这些领域的开发效率，
提供了许多的辅助工具，包括JMX使用、REST调用、SNMP接口。本手册将介绍TongWeb对Web、EJB、JPA开发
提供的技术支持，并介绍辅助工具在实际开发中的使用。 
 
第2章 JMX使用 
JMX是在TongWeb中用于获取监视量的工具，本节将介绍在TongWeb中使用JMX获取监视量的方法以及
JMX对象ObjectName接口的对应表。 
2.1 获取TongWeb的监视量 
用户可以编写客户端程序来远程访问TongWeb所在的JVM中的Mbean，获取TongWeb运行时状态的监视
信息，为此应用开发时首先需要创建与TongWeb的Mbean Server的连接。 
JMXServiceURL jmxUrl = new JMXServiceURL( 
"service:jmx:rmi://127.0.0.1:7200/jndi/rmi://127.0.0.1:7200/jmxrmi"); 
Map<String, String[]> env = new HashMap<String, String[]>(); 
env.put(JMXConnector.CREDENTIALS, new String[]{"用户名", "密码"}); 
JMXConnector jmxConnector = JMXConnectorFactory.connect(jmxUrl, env); 
MBeanServerConnection mbsc = jmxConnector.getMBeanServerConnection(); 
说明： 
127.0.0.1为本机IP，应替换为TongWeb所在机器的IP地址。用户名、密码与TongWeb管理控制台相同
（thanos/初始密码thanos123.com）。使用JMX时，密码无最长使用期限，即90天后不会强制要求修改密码。 
2.1.1 获取TongWeb中监控Mbean的ObjectName 
通过ObjectName.getInstance(“ObjectName”)获取ObjectName实例,参数{ObjectName}说明请参见“JMX
接口列表”章节。 
2.1.2 获取各Mbean的监控数据 
通过获取的ObjectName调用对应Mbean的getAttribute方法，传入对应Mbean的ObjectName和具体监视量
名称，可以获取对应Mbean的监控数据。 
得到的数据类型转化为javax.management.openmbean.CompositeDataSupport类型，通过
CompositeDataSupport.get(String key)方法得到对应的数据。实现代码如下： 
CompositeDataSupport data = (CompositeDataSupport) mbsc.invoke( 
    ObjectName.getInstance("monitor:name=listeners,type=HttpListenerMonitor"), 


## 第 11 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
2 
    "count", new String[]{"tong-http-listener"}, new String[]{"java.lang.String"}); 
String value = data.get("connectionCount").toString(); 
System.out.println(value); 
 
返回的CompositeDataSupport类型的监视量数据结构如下： 
{canConnect=true, connectionCount=0, currentThreadCount=10, currentThreadsBusy=0, 
currentThreadsIdle=10, keepAliveCount=-1, maxThreads=200, threadPoolUsage=0.0} 
 
因此通过get方法可以得到对应key的值。其中，通过CompositeData.get("connectionCount")获取到的值是
long类型，通过CompositeData.get("current")获取到的值是String类型，通过CompositeData.get("name")获取到
监控量的名称，通过CompositeData.get(“description”)获取到监控量的描述。 
注意： 
如果取出的数据类型不是CompositeData的，需要引入${TongWeb_HOME}/lib目录下bootstrap.jar包，将
其强制转换为确定的类型后再取值。 
2.1.3 获取虚拟机集合 
获取TongWeb的虚拟机集合数据的示例如下： 
List<VirtualHost> virtualHosts = (List<VirtualHost>) mbsc.getAttribute( 
    ObjectName.getInstance("config:name=WebContainer,parent=/Tongweb/Server"), 
    "virtualHost"); 
System.out.println(virtualHosts); 
2.2 JMX接口列表 
按TongWeb控制台菜单，可将JMX接口分为以下6类：Web容器配置、JDBC配置、应用管理、监视明细、
监视配置。 
2.2.1 WEB容器配置 
表 2.2-1：WEB 容器配置 
ObjectName 
config:name=WebContainer,parent=/Tongweb/Server 
功能描述 
虚拟主机管理、http通道管理、AJP通道管理列表数据 
属性列表 
属性名称 
描述 
类型 
virtualHost 
虚拟主机集合数据 
List<VirtualHost> 
httpListener 
http通道管理集合数据 
List<HttpListener> 
ajpListener 
AJP通道管理集合数据 
List<AjpListener> 
virtualHost属性清单 


## 第 12 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
3 
属性名称 
描述 
类型 
参考值 
name 
名称 
String 
— 
alias 
别名 
String 
— 
listeners 
通道 
String 
— 
httpListener属性清单 
属性名称 
描述 
类型 
参考值 
name 
名称 
String 
— 
status 
状态 
String 
— 
port 
端口 
Integer 
— 
defaultVirtualHo
st 
默认虚拟主机 
String 
— 
sslEnabled 
 
类型 
 
Boolean 
若值为true 则类型为
https，反之为http 
ajpListener属性清单 
属性名称 
描述 
类型 
参考值 
name 
名称 
String 
— 
status 
状态 
String 
— 
port 
监听端口 
Integer 
— 
2.2.2 JDBC配置 
表 2.2-2：JDBC 容器配置 
ObjectName 
config:name=Server,parent=/Tongweb 
功能描述 
连接池管理列表和单个数据源查看 
属性列表 
属性名称 
描述 
类型 
jdbcConnectPool 
连接池管理集合数据 
List<JDBCConnectionPool> 
JDBCConnectionPool属性清单 
属性名称 
描述 
类型 
默认值 
name 
名称 
String 
— 
jdbcDriver 
驱动 
String 
— 
jdbcUrl 
连接URL 
String 
— 
userName 
用户名 
String 
— 
password 
密码 
String 
— 
jtaManaged 
jta管理 
String 
— 
connectionProperties 
连接参数 
String 
— 
defaultAutoCommit 
是否自动提交 
String 
— 


## 第 13 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
4 
commitOnReturn 
释放连接时提交 
String 
— 
initialSize 
初始化连接数 
String 
— 
maxActive 
最大连接数 
String 
— 
minIdle 
最小空闲连接数 
String 
— 
maxWaitTime 
等待超时时间（毫秒） 
String 
— 
validationQuery 
默认测试SQL语句 
String 
— 
validationQueryTimeout 
验证超时（秒） 
String 
— 
testOnBorrow 
获取连接时验证 
String 
— 
testOnConnect 
创建连接时验证 
String 
— 
testOnReturn 
归还连接时验证 
String 
— 
timeBetweenEvictionRuns 
空闲检查周期 
String 
— 
minEvictableIdleTime 
空闲超时时间 
String 
60000ms 
removeAbandoned 
泄露回收 
String 
— 
removeAbandonedTimeout 
泄露超时时间 
String 
— 
logAbandoned 
连接泄漏时打印日志 
String 
— 
validationInterval 
连接验证时间间隔 
（毫秒） 
String 
— 
maxAge 
连接最大寿命 
String 
— 
 
2.2.3 应用管理 
表 2.2-3：应用管理 
ObjectName 
com.tongweb.deploy:type=DeployCommand,name=DeployCommand 
功能描述 
应用管理的列表 
属性列表 
操作名称 
描述 
类型 
allapps 
返回应用的列表数据 
CompositeData[] 
属性清单 
属性名称 
描述 
类型 
参考值 
name 
名称 
String 
— 
contextRoot 
前缀 
String 
— 
type 
应用类型 
String 
 
autoDeploy 
部署方式 
String 
true->自动部署 
false->控制台部署 
status 
状态 
String 
started 
deployOrder 
部署顺序 
String 
100 


## 第 14 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
5 
location 
文件位置 
String 
— 
jspCompile 
是否支持jsp预编译 
String 
true->支持 
false->不支持 
delegate 
 
类加载顺序，默认为子
优先，可调整 
String 
true->父优先 
false->子优先 
cacheMaxSize 
静态资源缓存最大值,
以KB为单位 
String 
— 
description 
该应用的描述信息 
String 
— 
获取示例： 
JMXServiceURL jmxUrl = new JMXServiceURL( 
"service:jmx:rmi://127.0.0.1:7200/jndi/rmi://127.0.0.1:7200/jmxrmi"); 
Map<String, String[]> env = new HashMap<String, String[]>(); 
env.put(JMXConnector.CREDENTIALS, new String[]{"用户名", "密码"}); 
JMXConnector jmxConnector = JMXConnectorFactory.connect(jmxUrl, env); 
MBeanServerConnection mbsc = jmxConnector.getMBeanServerConnection(); 
CompositeData[] list = (CompositeData[]) mbeanServer.invoke( 
  ObjectName.getInstance("com.tongweb.deploy:type=DeployCommand,name=DeployCommand"), 
"allapps", null, null); 
for (int i = 0; i < list.length; i++) { 
     CompositeData data = list[i]; 
     System.out.println("应用："+data.get("name")+",类型："+data.get("type")+",状态：
"+data.get("status")); 
    } 
表 2.2-4：应用管理EAR 子模块 
ObjectName 
com.tongweb.deploy:type=DeployCommand,name=DeployCommand 
功能描述 
应用管理的列表ear项目子模块 
属性列表 
操作名称 
描述 
类型 
getEarChildapps(DeployI
nfo) 
ear项目的子项目列表 
List<DeployInfo> 
DeployInfo属性清单 
属性名称 
描述 
类型 
参考值 
name 
名称 
String 
— 
contextRoot 
前缀 
String 
— 
type 
应用类型 
String 
war、ejb 
accessURLSSL 
Ssl的访问地址 
String 
— 


## 第 15 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
6 
accessURL 
访问地址 
String 
— 
子模块获取示例： 
JMXServiceURL jmxUrl = new JMXServiceURL( 
"service:jmx:rmi://127.0.0.1:7200/jndi/rmi://127.0.0.1:7200/jmxrmi"); 
Map<String, String[]> env = new HashMap<String, String[]>(); 
env.put(JMXConnector.CREDENTIALS, new String[]{"用户名", "密码"}); 
JMXConnector jmxConnector = JMXConnectorFactory.connect(jmxUrl, env); 
MBeanServerConnection mbsc = jmxConnector.getMBeanServerConnection(); 
ObjectName oName = ObjectName.getInstance( 
"com.tongweb.deploy:type=DeployCommand,name=DeployCommand"); 
CompositeType type = new CompositeType( 
"com.tongweb.deploy.interfaces.DeployInfo", 
"description", new String[]{"name"}, 
        new String[]{"name description"}, new OpenType[]{SimpleType.STRING}); 
DeployInfo deployInfo = new DeployInfo(); 
deployInfo.setName("ejb3_1_ear"); 
Object[] params = {DeployerUtils.toCompositeData(deployInfo)}; 
CompositeData[] compositeDatas =(CompositeData[])mbsc.invoke( 
        oName, "getEarChildapps", params, 
        new String[]{CompositeData.class.getName()}); 
    for (int i =0;i< compositeDatas.length;i++) { 
        CompositeData data = compositeDatas[i]; 
        System.out.println("应用管理EAR子模块："+"名称：" + data.get("name") 
+"前缀："+data.get("contextRoot")+"应用类型"+data.get("type")+" SSl的访问地址" 
+data.get("accessURLSSL")+"访问地址："+data.get("accessURL")); 
    } 
2.2.4 监视明细 
监视明细可获取JVM信息、操作系统信息、TongWeb信息、服务配置信息、应用信息等，具体监视参数
及对应属性如下表所示。 
2.2.4.1 JVM内存信息 
表 2.2-5：JVM 内存信息 
ObjectName 
java.lang:type=Memory 
功能描述 
获取JVM内存信息 
属性列表 


## 第 16 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
7 
属性名称 
描述 
类型 
参考值 
HeapMemoryUsage 
堆内存使用 
CompositeData 
— 
NonHeapMemoryUsage 
非堆内存使用 
CompositeData 
— 
ObjectPendingFinalizationCo
unt 
正在回收的对象数量 
Integer 
— 
Verbose 
是否有内存变动日志
信息 
Boolean 
— 
MemoryUsage属性列表 
属性名称 
描述 
类型 
参考值 
init 
初始大小（Byte） 
Long 
— 
used 
已使用（Byte） 
Long 
— 
committed 
已提交（Byte） 
Long 
— 
max 
最大（Byte） 
Long 
— 
free 
JVM对内空闲值 
Integer 
— 
free_percent 
JVM堆空闲占比 
Integer 
— 
 
2.2.4.2 JVM内存池信息 
表 2.2-6：JVM 内存池信息1 
ObjectName 
java.lang:type=MemoryPool,name=PS Eden Space 
功能描述 
获取PS Eden Space信息，JDK8支持 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
名称 
String 
PS Eden Space 
Type 
类型 
String 
HEAP 
Usage 
内存使用情况 
CompositeData 
— 
 
表 2.2-7：JVM 内存池信息2 
ObjectName 
java.lang:type=MemoryPool,name=PS Survivor Space 
功能描述 
获取PS Survivor Space信息，JDK8支持 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
名称 
String 
PS Survivor Space 
Type 
类型 
String 
HEAP 
Usage 
内存使用情况 
CompositeData 
— 


## 第 17 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
8 
表 2.2-8：JVM 内存池信息3 
ObjectName 
java.lang:type=MemoryPool,name=PS Old Gen 
功能描述 
获取PS Old Gen信息，JDK8支持 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
名称 
String 
PS Old Gen 
Type 
类型 
String 
HEAP 
Usage 
内存使用情况 
CompositeData 
— 
表 2.2-9：JVM 内存池信息4 
ObjectName 
java.lang:type=MemoryPool,name=Metaspace 
功能描述 
获取Metaspace信息（元空间JDK 1.8-JDK 1.14） 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
名称 
String 
Metaspace 
type 
类型 
String 
NON_HEAP 
Usage 
内存使用情况 
CompositeData 
— 
 
表 2.2-10：JVM 内存池信息5 
ObjectName 
java.lang:type=MemoryPool,name=Compressed Class Space 
功能描述 
获取Compressed Class Space信息（压缩空间JDK 1.8-JDK 1.14） 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
名称 
String 
Compressed Class Space 
type 
类型 
String 
NON_HEAP 
Usage 
内存使用情况 
CompositeData 
— 
 
表 2.2-11：JVM 内存池信息6 
ObjectName 
java.lang:type=MemoryPool,name=Code Cache 
功能描述 
获取Code Cache信息，JDK8支持 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
名称 
String 
Code Cache 
Type 
类型 
String 
NON_HEAP 
Usage 
内存使用情况 
CompositeData 
— 


## 第 18 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
9 
2.2.4.3 JVM垃圾收集器信息 
表 2.2-12：JVM 垃圾收集器信息 
ObjectName 
java.lang:type=GarbageCollector,name=PS MarkSweep 
java.lang:type=GarbageCollector,name=PS Scavenge 
功能描述 
获取JVM垃圾收集器信息，JDK8支持 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
垃圾收集器名称 
String 
— 
Valid 
是否有效 
Boolean 
— 
CollectionCount 
收集次数 
Long 
— 
CollectionTime 
累积耗时(毫秒) 
Long 
— 
MemoryPoolNames 
管理的内存池名称 
String[] 
— 
2.2.4.4 JVM线程信息 
表 2.2-13：JVM 线程信息 
ObjectName 
java.lang:type=Threading 
功能描述 
获取JVM线程信息 
属性列表 
属性/操作名称 
描述 
类型 
参考值 
ThreadCount 
当前线程数 
Integer 
— 
PeakThreadCount 
活跃线程数峰值 
Integer 
— 
TotalStartedThreadCount 
所有运行过的线程数
量 
Long 
— 
DaemonThreadCount 
当前守护线程数量 
Integer 
— 
AllThreadIds 
所有线程id 
Long[] 
— 
findDeadlockedThreads 
查询死锁线程（开销
大） 
Long[] 
— 
2.2.4.5 JVM编译器信息 
表 2.2-14：JVM 编译器信息 
ObjectName 
java.lang:type=Compilation 
功能描述 
获取JVM编译器信息 
属性列表 
属性名称 
描述 
类型 
参考值 
CompilationTimeMonit
oringSupported 
是否支持监视编译耗时 
Boolean 
— 


## 第 19 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
10 
TotalCompilationTime 
编译耗时近似值 
Long 
— 
Name 
编译器名称 
String 
HotSpot 64-Bit Tiered Compilers 
2.2.4.6 JVM类加载信息 
表 2.2-15：JVM 类加载信息 
ObjectName 
java.lang:type=ClassLoading 
功能描述 
获取JVM类加载信息 
属性列表 
属性名称 
描述 
类型 
参考值 
LoadedClassCount 
当前已加载的类数量 
Integer 
— 
UnloadedClassCount 
所有卸载过的类数量 
Long 
— 
TotalLoadedClassCount 
所有加载过的类数量 
Long 
— 
Verbose 
是否有类加载日志信息 
Boolean 
— 
2.2.4.7 JVM运行时信息 
表 2.2-16：JVM 运行时信息 
ObjectName 
java.lang:type=Runtime 
功能描述 
获取JVM运行时信息  
属性列表 
属性名称 
描述 
类型 
参考值 
SpecName 
jvm规范名称 
String 
Java Virtual Machine 
Specification 
SpecVersion 
jvm规范版本 
String 
1.8 
SpecVendor 
jvm规范供应商 
String 
Oracle Corporation 
VmName 
jvm实现名称 
String 
Java HotSpot™ 64-Bit Server 
VM 
VmVersion 
jvm实现版本 
String 
25.144-b01 
VmVendor 
jvm实现供应商 
String 
Oracle Corporation 
StartTime 
jvm启动时间 
Long 
— 
Uptime 
jvm运行时长 
Long 
— 
LibraryPath 
库文件路径 
String 
— 
BootClassPath 
引导类路径， 
JDK8支持 
String 
— 
ClassPath 
系统类路径 
String 
— 
BootClassPathSupport
ed 
是否支持从引导类路
径搜索类文件 
Boolean 
— 


## 第 20 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
11 
InputArguments 
jvm启动输入参数 
String[] 
— 
SystemProperties 
系统属性列表 
TabularDataSupp
ort 
— 
2.2.4.8 操作系统信息 
表 2.2-17：操作系统信息 
ObjectName 
java.lang:type=OperatingSystem 
功能描述 
获取操作系统信息 
属性列表 
属性名称 
描述 
类型 
参考值 
Name 
系统名称 
String 
Windows 7 
Version 
系统版本 
String 
6.1 
Arch 
系统架构 
String 
amd64 
AvailableProcessors 
核心处理器数量 
Integer 
4 
2.2.4.9 系统使用信息 
表 2.2-18：监视概览-系统使用信息 
ObjectName 
monitor:name=systemStatus,type=SystemStatusMonitor 
功能描述 
获取系统使用信息 
属性列表 
属性名称 
描述 
类型 
参考值 
CpuPercent 
Cpu使用率（百分制） 
String 
10 
MemPercent 
内存使用率（百分制） 
String 
70 
2.2.4.10 TongWeb信息 
表 2.2-19：TongWeb 信息 
ObjectName 
TONGWEB:type=Server 
功能描述 
获取TongWeb信息 
属性列表 
属性名称 
描述 
类型 
参考值 
serverInfo 
服务器名称 
String 
TongWeb 
serverNumber 
服务器版本 
String 
7.0.6.1 
serverBuilt 
服务器构建日期 
String 
2019-09-16 09:53:02 
address 
停止服务监听地址 
String 
localhost 
port 
停止服务监听端口 
Integer 
7090 
stateName 
示例状态 
String 
STARTED 


## 第 21 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
12 
2.2.4.11 通道信息 
表 2.2-20：通道信息 
ObjectName 
monitor:name=listeners,type=HttpListenerMonitor 
功能描述 
获取TongWeb通道信息 
属性列表 
操作名称 
描述 
类型 
count 
连接数、线程数对象 
CompositeData 
stat 
统计信息 
CompositeData 
HttpListenerMonitor$Count属性列表 
属性名称 
描述 
类型 
参考值 
connectionCount 
当前连接数 
String 
— 
keepAliveCount 
当前keep-alive连接数 
String 
— 
currentThreadCount 
当前线程池线程数 
String 
— 
currentThreadsBusy 
正在执行任务的线程数 
String 
— 
threadPoolUsage 
线程池使用率（正在执行
任务的线程数/线程池最
大值） 
String 
— 
maxThreads 
最大处理线程数 
Integer 
— 
canConnect 
TongWeb连接状态 
String 
— 
HttpListenerMonitor$Stat属性列表 
属性名称 
描述 
类型 
参考值 
bytesSent 
发送的字节数 
String 
— 
bytesReceived 
接收的字节数 
String 
— 
processingTime 
处理时间 
String 
— 
errorCount 
错误数 
String 
— 
maxTime 
最大处理时间(毫秒) 
String 
— 
requestCount 
请求数 
String 
— 
 
获取示例： 
JMXServiceURL jmxUrl = new JMXServiceURL( 
"service:jmx:rmi://127.0.0.1:7200/jndi/rmi://127.0.0.1:7200/jmxrmi"); 
Map<String, String[]> env = new HashMap<String, String[]>(); 
env.put(JMXConnector.CREDENTIALS, new String[]{"用户名", "密码"}); 
JMXConnector jmxConnector = JMXConnectorFactory.connect(jmxUrl, env); 
MBeanServerConnection mbsc = jmxConnector.getMBeanServerConnection(); 
CompositeData data = (CompositeData)mbeanServer.invoke( 


## 第 22 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
13 
    ObjectName.getInstance("monitor:name=listeners,type=HttpListenerMonitor"), 
"count", new Object[]{"system-http-listener"}, new String[]{String.class.getName()}); 
    System.out.println(data.get("connectionCount")); 
 
2.2.4.12 数据源信息 
表 2.2-21：非XA 数据源实时信息 
ObjectName 
com.tongweb.hulk:type=Pool (datasourcename) 
功能描述 
获取非XA数据源实时信息 
属性列表 
属性名称 
描述 
类型 
参考值 
ActiveConnections 
当前正在使用的连接数 
int 
— 
IdleConnections 
当前空闲的连接数 
int 
— 
TotalConnections 
当前池中连接总数 
int 
— 
ThreadsAwaitingConnection 
等待连接的线程数 
int 
— 
LeakCount 
当前泄漏的连接数 
Integer 
— 
AccumlateleakCount 
累计回收泄漏连接数 
Integer 
— 
CreateCount 
创建的连接数 
Integer 
— 
MaxUseCount 
最大使用连接数 
Integer 
— 
AwaitingConnectionFailureCount 
jdbc当前等待连接失败数 
Integer 
— 
AwaitingConnectionHighCount 
jdbc等待连接峰值数 
Integer 
— 
ConnectionUsedPercent 
jdbc连接池使用占比（在用连接
数/已建连接数） 
String 
— 
ConnectionUsedPercentBaseMaxSize 
jdbc连接池使用占比（在用连接
数/最大连接数） 
String 
— 
 
表 2.2-22：XA 数据源实时信息 
ObjectName 
com.tongweb.hulk:type=Pool (datasourcename) 
功能描述 
获取XA数据源实时信息 
属性列表 
属性名称 
描述 
类型 
参考值 
Active 
当前正在使用的连接数 
int 
— 
Idle 
当前空闲的连接数 
int 
— 
size 
当前池中连接总数 
int 
— 
WaitCount 
等待连接的线程数 
int 
— 
NumConnCreated 
创建的连接数 
Integer 
— 


## 第 23 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
14 
NumConnDestroyed 
销毁的连接数 
Integer 
— 
NumConnReleased 
释放的连接数 
Integer 
— 
NumConnTimeout 
超时的连接数 
Integer 
— 
LeakCount 
当前泄漏的连接数 
Integer 
— 
AccumlateleakCount 
累计回收泄漏连接数 
Integer 
— 
 
表 2.2-23：数据源配置信息 
ObjectName 
com.tongweb.hulk:type=PoolConfig (datasourcename) 
功能描述 
获取数据源配置信息 
属性列表 
属性名称 
描述 
类型 
参考值 
ConnectionTimeout 
maxWait，单位ms，不能小于四分之一秒，线程
等待获取连接最大时长，超出后则得到异常信息 
long 
— 
MaximumPoolSize 
正整数，不会小于minimumIdle 和 
defaultPoolSize的最大值 
Int 
— 
IdleTimeout 
minEvictableIdleTimeMillis，单位ms，不能小于
10秒，且不能大于 maxLifetime 
long 
— 
ValidationInterval 
连接验证时间间隔，即上次验证到当前时间点。
若不超过此值，则认为验证通过，无需再验证 
long 
— 
PoolName 
连接池名称 
Strin
g 
— 
MinimumIdle 
MinIdle，最小连接数 
Int 
— 
MaxLifetime 
MaxAge，单位ms，不能小于30秒，连接的最大
寿命，超出后回收 
long  
— 
ValidationTimeout 
最长验证时间 
long 
— 
LeakDetectionThreshol
d 
RemoveAbandonedTimeout最长未归还时间，超
出后认为泄漏 
long 
— 
DefaultPoolSize 
InitialSize初始连接池大小 
Int 
— 
 
表 2.2-24：数据源实时状态 
名称 
数据源状态监控 
ObjectName 
monitor:name=jdbcPool,type=JdbcPoolMonitor 
功能描述 
获取数据源实时状态 
属性列表 
操作名称 
描述 
类型 
 
stat(jdbcName) 
获取jdbc数据源实时状态信
JdbcPoolMonitor$ResultInfo 
 


## 第 24 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
15 
息，jdbcName表示数据源名称，
可为空，为空时返回所有数据
源信息 
JdbcPoolMonitor$ResultInfo类型属性列表 
属性名称 
描述 
类型 
参考值 
jdbcPoolStats 
数据源状态列表 
JdbcPoolMonitor$JdbcPoolS
tat 
 
topFiveSlowSqls 
数据源开启慢SQL日志情况下，
返回所有数据源1个小时内的前
5条慢SQL信息 
JdbcPoolMonitor$SlowSql 
 
JdbcPoolMonitor$JdbcPoolStat类型属性列表 
属性名称 
描述 
类型 
参考值 
isMulti 
区分单数据源与多数据源 
Boolean 
- 
name 
数据源名称 
String 
- 
status 
状态 
String 
Running_O
k 正常 
Running_W
arning 有
告警 
Error 连接
异常 
msg 
错误、告警信息 
String 
 
JdbcPoolMonitor$SlowSql类型属性列表 
属性名称 
描述 
类型 
参考值 
sql 
慢SQL语句 
String 
 
elapsedTime 
耗时（毫秒） 
String 
Running_O
k 正常 
Running_W
arning 有
告警 
Error 连接
异常 
execTime 
执行时间 
String 
yyyy-MM-d
d 
HH:mm:ss 
 


## 第 25 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
16 
2.2.4.13 事务信息 
表 2.2-25：事务信息 
ObjectName 
monitor:name=trans,type=TransactionManagerMonitor 
功能描述 
获取事务信息 
属性列表 
操作名称 
描述 
类型 
count 
事务数对象 
CompositeData 
stat 
配置信息 
CompositeData 
TransactionManagerMonitor$Count属性列表 
属性名称 
描述 
类型 
参考值 
commits 
所有提交的事务数 
Long 
— 
rollbacks 
所有回滚的事务数 
Long 
— 
active 
当前事务数 
Long 
— 
TransactionManagerMonitor$Stat属性列表 
属性名称 
描述 
类型 
参考值 
defaultTransaction
TimeoutMillisecon
ds 
默认的事务超时时间 
String 
1 HOURS 
 
2.2.4.14 JCA信息 
表 2.2-26：JCA 信息 
ObjectName 
monitor:name={JCAConnectionPoolName},group=jca 
功能描述 
获取JCA信息 
属性列表 
属性名称 
描述 
类型 
参考值 
BusyNum 
正在使用的连接数 
Integer 
— 
ConnNum 
连接池中的连接数 
Integer 
— 
FreeNum 
空闲连接数 
Integer 
— 
 
2.2.4.15 应用细节信息 
表 2.2-27：应用细节信息 
ObjectName 
TONGWEB:j2eeType=WebModule,name=//server/{appName}, 
J2EEApplication={appName},J2EEServer=TongWeb 
功能描述 
获取应用细节信息 


## 第 26 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
17 
属性列表 
属性名称 
描述 
类型 
参考值 
baseName 
应用名称 
String 
— 
path 
未编码应用路径 
String 
— 
encodedPath 
URL编码应用路径 
String 
— 
docBase 
应用目录 
String 
— 
workDir 
应用工作目录（jsp编译缓存） 
String 
— 
delegate 
父优先加载 
Boolean 
— 
requestCount 
应用请求数 
Integer 
— 
errorCount 
应用请求错误数 
Integer 
— 
processingTi
me 
应用请求处理时间 
Long 
— 
maxTime 
应用请求最大处理时间（毫秒） 
Long 
— 
minTime 
应用请求最小处理时间（毫秒） 
Long 
— 
sessionTimeo
ut 
会话超时时间 
Integer 
— 
startTime 
应用启动时间 
Long 
— 
startupTime 
应用启动耗时 
Long 
— 
cookies 
是否基于Cookie 存取会话ID 
Boolean 
— 
ignoreAnnotat
ions 
是否忽略注解 
Boolean 
— 
stateName 
应用状态 
String 
— 
 
2.2.4.16 应用会话信息 
表 2.2-28：应用会话信息 
ObjectName 
TONGWEB:type=Manager,host=server,context=/{appName} 
功能描述 
获取应用会话信息 
属性列表 
属性名称 
描述 
类型 
参考值 
expiredSessions 
过期的会话数 
Long 
— 
maxActive 
活跃会话数峰值 
Integer 
— 
maxActiveSessions 
限制的最大活跃会话数 
Integer 
— 
rejectedSessions 
拒绝的会话数 
Integer 
— 
pathname 
会话保存文件 
String 
SESSIONS.ser 
sessionCounter 
创建过的所有会话数 
Long 
— 
sessionMaxAliveTi
最大会话存活时长(秒) 
Integer 
— 


## 第 27 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
18 
me 
sessionAverageAlive
Time 
失效会话平均存活时长(秒) 
Integer 
— 
activeSessions 
应用当前session数 
Integer 
— 
 
2.2.4.17 应用类加载器信息 
表 2.2-29：应用类加载信息 
ObjectName 
TONGWEB:type=Loader,host=server,context=/{appName} 
功能描述 
获取应用类加载信息 
属性列表 
属性名称 
描述 
类型 
参考值 
loaderClass 
类加载器全名称 
String 
— 
delegate 
父优先加载 
Boolean 
— 
loaderRepositor
ies 
类加载路径 
String[] 
— 
reloadable 
可重复加载 
Boolean 
— 
 
2.2.4.18 应用资源缓存信息 
表 2.2-30：应用资源缓存信息 
ObjectName 
TONGWEB:type=WebResourceRoot,host=server,context=/{appName},name=C
ache 
功能描述 
获取应用资源缓存信息 
属性列表 
属性名称 
描述 
类型 
默认值 
size 
当前缓存数 
Long 
— 
maxSize 
最大缓存数 
Long 
— 
hitCount 
命中缓存 
Long 
— 
lookupCount 
查找次数 
Long 
— 
ttl 
缓存条目存活时长（毫
秒） 
Long 
5000 
 
2.2.5 监视配置 
表 2.2-31：监视配置信息 


## 第 28 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
19 
ObjectName 
config:name=Server,parent=/Tongweb 
功能描述 
获取监视配置信息 
属性列表 
属性名称 
描述 
类型 
monitorService 
监视配置服务信
息  
MonitorService 
MonitorService类型属性清单 
属性名称 
描述 
类型 
参考值 
monitorConfig 
监控配置集合信
息 
List<MonitorConfig> 
— 
monitoringEnabled 
是否启用监控 
Boolean 
— 
flushInterval 
检测周期（秒） 
Integer 
— 
flushTimeThreshold 
数据存活时间
（秒） 
Integer 
— 
persistEnabled 
数据是否持久化 
Boolean 
— 
MonitorConfig类型属性清单 
属性名称 
描述 
类型 
参考值 
name 
监控项名称 
String 
— 
monitoringEnabled 
是否启用监控 
Boolean 
— 
produceInterval 
采集数据周期
（秒） 
Integer 
— 
persistEnabled 
数据是否持久化 
Boolean 
一 
 
2.2.6 EJB 
2.2.6.1 无状态会话Bean、有状态会话Bean、单例会话Bean、消息驱动Bean配置
管理 
表 2.2-32：Bean 配置管理 
ObjectName 
config:name=EjbContainer,parent=/Tongweb/Server 
功能描述 
无状态会话Bean配置管理 
有状态会话Bean配置管理 
单例会话Bean配置管理 
消息驱动Bean配置管理 
属性列表 
属性名称 
描述 
类型 
参考值 


## 第 29 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
20 
stateless 
无状态会话Bean配置数据 
Stateless 
- 
stateful 
有状态会话Bean配置数据 
Stateful 
- 
singleton 
单例会话Bean配置数据 
Singleton 
- 
mdb 
消息驱动Bean配置数据 
Mdb 
- 
Stateless类型属性清单 
属性名称 
描述 
类型 
默认值 
accessTimeout 
等待超时（秒） 
String 
30 
maxSize 
最大实例数 
String 
10 
minSize 
最小实例数 
String 
0 
strictPooling 
池溢出策略 
String 
true：等待池空闲 
false：创建临时实例 
maxAge 
实例超时时间（小时） 
String 
0 
replaceAged 
是否允许实例超时替换 
String 
true：允许 
false：不允许 
replaceFlushed 
是否允许刷新 
String 
true：允许 
false：不允许 
maxAgeOffset 
创建实例延迟参数（%） 
String 
0% 
idleTimeout 
实例空闲超时时间（分钟） 
String 
0 
garbageCollectio
n 
实例是否回收 
String 
true：允许 
talse：不允许 
sweepInterval 
设置扫描频率（分钟） 
String 
5 
callbackThreads 
设置执行实例替换或者丢弃的线
程池的最小线程数 
String 
5 
closeTimeout 
关闭池操作的超时时间（分钟） 
String 
5 
Stateful类型属性清单 
属性名称 
描述 
类型 
默认值 
accessTimeout 
等待超时（秒） 
String 
30 
timeout 
会话空闲超时时间（分钟） 
String 
20 
frequency 
检查的频率（秒） 
String 
60 
capacity 
缓存最大容量 
String 
1000 
bulkPassivate 
每次进行钝化处理的实例数量 
String 
100 
Singleton类型属性清单 
属性名称 
描述 
类型 
默认值 
accessTimeout 
等待超时（秒） 
String 
30 
Mdb类型属性清单 
属性名称 
描述 
类型 
默认值 
accessTimeout 
等待超时（秒） 
String 
30 


## 第 30 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
21 
maxSize 
最大实例数 
String 
10 
minSize 
最小实例数 
String 
0 
strictPooling 
池溢出策略 
String 
true：等待池空闲 
false：创建临时实例 
maxAge 
实例超时时间（小时） 
String 
0 
replaceAged 
是否允许实例超时替换 
String 
true：允许 
false：不允许 
replaceFlushed 
是否允许刷新 
String 
true：允许 
false：不允许 
maxAgeOffset 
创建实例延迟参数（%） 
String 
0% 
idleTimeout 
实例空闲超时时间（分钟） 
String 
0 
garbageCollectio
n 
实例垃圾是否回收 
String 
true：开启 
false：关闭 
sweepInterval 
设置扫描频率（分钟） 
String 
5 
callbackThreads 
设置执行实例替换或者丢弃的线
程池的最小线程数 
String 
5 
closeTimeout 
实例关闭超时时间（分钟） 
String 
5 
 
2.2.6.2 EJB远程调用配置管理 
表 2.2-33：EJB 远程调用配置管理 
ObjectName 
config:name=Server,parent=/Tongweb 
功能描述 
EJB远程调用配置管理 
属性列表 
属性名称 
描述 
类型 
参考值 
remote 
远程调用信息 
Remote 
一 
Remote类型属性清单 
属性名称 
描述 
类型 
参考值 
port 
监听端口 
Integer 
一 
 
2.2.7 JCA 
2.2.7.1 JCA线程池 
表 2.2-34：JCA 线程池 
ObjectName 
config:name=Server,parent=/Tongweb 


## 第 31 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
22 
功能描述 
JCA线程池 
属性列表 
属性名称 
描述 
类型 
参考值 
jcaThreadPool 
JCA线程池集合信息 
List<JCAThreadPool> 
一 
JCAThreadPool类型属性清单 
属性名称 
描述 
类型 
参考值 
name 
线程池名称 
String 
一 
minThreads 
最小线程数 
Integer 
10 
maxThreads 
最大线程数 
Integer 
200 
queue 
等待队列数 
Integer 
100 
keepAliveTime 
线程空闲时间（秒） 
Integer 
3600 
 
2.2.7.2 JCA连接池 
表 2.2-35：JCA 连接池 
ObjectName 
config:name=Server,parent=/Tongweb 
功能描述 
JCA连接池 
属性列表 
属性名称 
描述 
类型 
jcaConnectionPool 
JCA连接池集合
信息 
List<JCAConnectionPool> 
JCAConnectionPool类型属性清单 
属性名称 
描述 
类型 
参考值 
name 
连接池名称 
String 
一 
adapterName 
适配器名称 
String 
一 
connectionDefinition 
连接定义 
String 
一 
minPoolSize 
最小连接数 
Integer 
一 
maxPoolSize 
最大连接数 
Integer 
一 
takeConnectionTimeout 
等待超时（秒） 
Integer 
一 
idleTimeout 
空闲超时（分） 
Integer 
一 
matchConnections 
是否连接匹配 
Boolean 
一 
transType 
事务支持类型 
String 
NoTransaction 
LocalTransaction 
XATransaction 
 


## 第 32 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
23 
2.2.7.3 托管对象资源 
表 2.2-36：托管对象资源 
ObjectName 
config:name=Server,parent=/Tongweb 
功能描述 
托管对象资源 
属性列表 
属性名称 
描述 
类型 
adapterAdminobjectReso
urce 
托管对象集合数据 
List<AdapterAdminobjectResource> 
AdapterAdminobjectResource类型属性清单 
属性名称 
描述 
类型 
参考值 
name 
名称 
String 
一 
resourceAdapter 
资源适配器 
String 
一 
resourceType 
资源类型 
String 
一 
 
2.3 使用JMX MP协议 
TongWeb的JMX支持两种协议，分别是rmi协议和mp协议。默认是rmi协议。其切换的开关在TongWeb
的配置文件tongweb.xml中。其中关于jmx的描述如下： 
<jmx-service port="7200" address="127.0.0.1" protocol="rmi"/> 
protocol指定了TongWeb启动时所使用的协议。 
当前版本停止端口shutdown-port默认和jmx端口共用“7200”。 
说明： 
若需要停止端口单独使用“7200”，则可按照如下方式操作。 
⚫ 
将7200端口的jmx协议由“rmi”改为“mp”协议<jmx-service port="7200" address="127.0.0.1" 
protocol="mp"/>。 
⚫ 
关闭jmx的7200端口，jmx则启用7090端口。 
<jmx-service port="7200" address="127.0.0.1" enabled="false"> 
2.3.1 开启jmx mp协议 
操作步骤，如下所示。 
1. 打开“${TongWeb_HOME}/conf/tongweb.xml”，将“protocol”修改为“mp”，如下所示。 
<jmx-service port="7200" address="127.0.0.1" protocol="mp"/> 
2. 配置完成后，重启TongWeb服务器，即可生效。 


## 第 33 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
24 
2.3.2 使用JMX MP协议 
使用jmx mp协议时，需要进行登录认证，示例如下所示。 
JMXServiceURL jmxUrl = new JMXServiceURL("service:jmx:jmxmp://127.0.0.1:7200"); 
Map<String, String[]> env = new HashMap<String, String[]>(); 
env.put("jmx.remote.profiles", "SASL/PLAIN"); 
env.put("jmx.remote.sasl.callback.handler", new UserPasswordCallBackHandler("用户名", "
密码")); 
JMXConnector jmxConnector = JMXConnectorFactory.connect(jmxUrl, env); 
MBeanServerConnection mbsc = jmxConnector.getMBeanServerConnection(); 
 
2.3.3 Jconsole通过JMX MP协议登录认证 
Jconsole支持JMX MP协议登录认证。 
前置条件 
从技术支持人员处获取“jmxremote_mp.jar”。 
约束说明 
JDK7u40及以上版本，JDK11不支持。 
操作步骤 
1. 将获取的“jmxremote_mp.jar”包放在JDK目录“jdk\jre\lib\ext”下。 
2. 
Jconsole即可使用JMX MP协议进行登录认证。 
2.4 绑定IPv6的jmx地址 
如果需要TongWeb绑定IPv6类型的jmx地址则需要在启动脚本中指定实际的IPv6地址。在
${TongWeb_HOME}/bin/external.vmoptions中添加参数的方式来支持，配置如下。 
-Djava.rmi.server.hostname=[2001:da8:2004:1000:202:116:160:41] 
注意：地址需要用中括号括起来。 
 
第3章 REST调用 
3.1 Console控制台REST接口 
3.1.1 REST接口列表 
REST所有接口后均需添加username和password两个参数，如果未添加这两个参数，则无权限访问REST
接口信息。 


## 第 34 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
25 
例如：使用http://168.1.13.108:9060/console/rest/api/web_container?username=thanos&password=thanos123.c
om访问控制台时，无需登录便可查看到REST接口信息。 
也可使用如下方式curl --user name:password http://168.1.13.108:9060/console/rest/api/web_container进行
访问。 
说明： 
⚫ 
用户名、密码与TongWeb管理控制台相同（thanos/初始密码thanos123.com）。调用REST时，密码无
最长使用期限，即90天后不会强制要求修改密码。 
⚫ 
curl命令执行时，若url中含有‘&’等特殊字符，url需要加引号。 
以下表格列出了console控制台所有模块的REST接口的请求地址。 
表 3.1-1：REST接口 
功能名称 
类型 
请求地址 
WEB容器配置 
GET 
/rest/api/web_container 
JDBC配置 
GET 
/rest/api/jdbc_config 
EJB-BEANS配置 
GET 
/rest/api/ejb_container 
EJB远程调用配置 
GET 
/rest/api/ejb_config 
应用管理列表 
GET 
/rest/api/application_management 
JCA线程池 
GET 
/rest/api/jca_thread_pool 
JCA连接池 
GET 
/rest/api/jca_connector_pool 
托管对象资源 
GET 
/rest/api/jca_adapter_resource 
JVM内存信息 
GET 
/rest/api/jvm_memory_detail 
JVM内存池信息 
GET 
/rest/api/jvm_memory_pool 
JVM垃圾收集器信息 
GET 
/rest/api/jvm_garbage_collector_detail 
JVM线程信息 
GET 
/rest/api/jvm_threading_detail 
JVM编译器信息 
GET 
/rest/api/jvm_compilation_detail 
JVM类加载信息 
GET 
/rest/api/jvm_classloading_detail 
JVM运行时信息 
GET 
/rest/api/runtime_detail 
操作系统基本信息 
GET 
/rest/api/operating_system_detail 
操作系统使用情况 
GET 
/rest/api/operating_system_usage 
TongWeb信息 
GET 
/rest/api/tongweb_server_detail 
通道信息 
GET 
/rest/api/listener_detail 
数据源信息 
GET 
/rest/api/datasource_detail 
事务信息 
GET 
/rest/api/transaction_detail 
JCA信息 
GET 
/rest/api/jca_detail 
应用细节信息 
GET 
/rest/api/application_detail 
应用会话信息 
GET 
/rest/api/application_session 
应用类加载器信息 
GET 
/rest/api/application_classloader 
应用资源缓存信息 
GET 
/rest/api/application_resource_cache 


## 第 35 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
26 
功能名称 
类型 
请求地址 
监视配置 
GET 
/rest/api/monitor_config 
查看所有hung线程 
GET 
/rest/api/hungThreads 
查看hung线程详细 
GET 
/rest/api/hungThreadDetail 
获取慢sql日志 
GET 
/rest/api/searchLog 
获取jdbc健康状态 
GET 
/rest/api/health/jdbc 
获取http通道健康状态 
GET 
/rest/api/health/connector 
获取server健康状态 
GET 
/rest/api/health/server 
3.1.2 接口地址调用示例 
接口地址中给出的不是全部参数的对应值，具体参考功能名称对应JMX的MBEAN属性列表。 
表 3.1-2：REST 接口地址调用示例 
功能名称 
请求类型 
请求地址 
WEB容器配置 
GET 
/rest/api/web_container?attrName=virtualHost,httpListener,ajpListener 
JDBC配置 
GET 
/rest/api/jdbc_config?attrName=jdbcConnectionPool 
EJB-BEAN配置 
GET 
/rest/api/ejb_container?attrName=stateless,stateful 
EJB远程 
调用配置 
GET 
/rest/api/ejb_config?attrName=remote 
应用管理 
列表 
GET 
/rest/api/application_management?operatorName=allapps 
JCA线程池 
GET 
/rest/api/jca_thread_pool?attrName=jcaThreadPool 
JCA连接池 
GET 
/rest/api/jca_connector_pool?attrName=jcaConnectionPool 
托管对象 
资源 
GET 
/rest/api/jca_adapter_resource?attrName=adapterAdminobjectResource 
JVM 
内存 
GET 
/rest/api/jvm_memory_detail?attrName=HeapMemoryUsage,NonHeapMemoryUsag
e, 
ObjectPendingFinalizationCount,Verbose 
JVM 
内存池 
GET 
/rest/api/jvm_memory_pool?attrName=Name,Type,Usage 
JVM 
垃圾收集器 
GET 
/rest/api/jvm_garbage_collector_detail?attrName=Name,Valid,CollectionCount, 
CollectionTime,MemoryPoolNames 
JVM线程 
GET 
/rest/api/jvm_threading_detail?attrName=ThreadCount,PeakThreadCount&operatorN
ame= 


## 第 36 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
27 
功能名称 
请求类型 
请求地址 
findDeadlockedThreads 
findDeadLockedThreads：查询死锁线程（开销大）。 
JVM 
编译器信息 
GET 
/rest/api/jvm_compilation_detail?attrName=CompilationTimeMonitoringSupported,T
otalCompilationTime,Name 
JVM 
类加载信息 
GET 
/rest/api/jvm_classloading_detail?attrName=LoadedClassCount,UnloadedClassCount
,TotalLoadedClassCount,Verbose 
JVM 
运行时信息 
GET 
/rest/api/runtime_detail?attrName=SpecName,SpecVersion,SpecVendor,VmName,V
mVersion 
操作系统 
基本信息 
GET 
/rest/api/operating_system_detail?attrName=Name,Version,Arch,AvailableProcessors 
操作信息 
使用信息 
GET 
/rest/api/operating_system_usage?attrName=CpuPercent,MemPercent 
TongWeb 
信息 
GET 
/rest/api/tongweb_server_detail?attrName=serverInfo,serverNumber,serverBuilt,addr
ess,port 
通道信息 
GET 
/rest/api/listener_detail?operatorName=count:{httpListenerName},stat: 
{httpListenerName} 
httpListenerName参考WEB容器配置接口的httpListener值中的name属性，以下示
例： 
/rest/api/listener_detail?operatorName=count:system-http-listener,stat:system-http-lis
tener 
/rest/api/listener_detail?operatorName=count:tong-http-listener,stat:tong-http-listener 
/rest/api/listener_detail?operatorName=count:ejb-server-listener,stat:ejb-server-listen
er 
数据源信息 
GET 
/rest/api/datasource_detail 
事务信息 
GET 
/rest/api/transaction_detail?operatorName=count,stat 
JCA信息 
GET 
/rest/api/jca_detail?pathValue={jcaConnectorPoolName}&attrName=BusyNum,Con
nNum,FreeNum 
jcaConnectorPoolName参考JCA连接池中name属性 
应用细节 
信息 
GET 
/rest/api/application_detail?pathValue={appName}&vhost={virtualHost}&attrName
= 
baseName,path,docBase,workDir 
appName参考应用管理列表接口的name属性，支持EJB、WAR类型，virtualHost
为虚拟主机名称，默认为server 
应用会话 
信息 
GET 
/rest/api/application_session?pathValue={appName}&vhost={virtualHost}&attrNam
e=expiredSessions,maxActive,maxActiveSessions,rejectedSessions,pathname 


## 第 37 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
28 
功能名称 
请求类型 
请求地址 
appName参考应用管理列表接口的name属性，支持EJB、WAR类型，virtualHost
为虚拟主机名称，默认为server 
应用 
类加载器 
信息 
GET 
/rest/api/application_classloader?pathValue={appName}&vhost={virtualHost}&attr
Name=loaderClass,delegate,loaderRepositories,reloadable 
appName参考应用管理列表接口的name属性，支持EJB、WAR类型，virtualHost
为虚拟主机名称，默认为server 
应用 
资源缓存 
信息 
GET 
/rest/api/application_resource_cache?pathValue={appName}&vhost={virtualHost}&
attrName=size,maxSize,hitCount,lookupCount,ttl 
appName参考应用管理列表接口的name属性，支持EJB、WAR类型，virtualHost
为虚拟主机名称，默认为server 
监视配置 
GET 
/rest/api/monitor_config?attrName=monitorService 
查看所有hung线程 
GET 
/rest/api/hungThreads 
hungThreads：通道线程池，执行请求超过配置时间（hungTime）的线程。 
查看hung线程详细 
GET 
/rest/api/hungThreadDetail?tid={threadId} 
threadId表示线程id 
获取慢sql日志 
GET 
/rest/api/searchLog?startTime={startTime}&endTime={endTime}&proStart={min}
&proEnd={max} 
startTime表示日志开始时间，例如startTime=2021-07-26 10:30:20 
endTime表示日志结束时间，例如endTime=2021-07-26 11:30:20 
min表示sql执行耗时最小值，例如proStart=100 
max表示sql执行耗时最大值，例如proEnd=500 
系统日志 
GET 
/rest/log/searchRecent 
sql日志 
GET 
/rest/log/sqllog 
按照默认参数获取sql日志列表 
根据时间段和执行耗
时获取sql日志 
GET 
/rest/log/sqllog/searchLog?startTime=2021-07-14 14:02:31&endTime=2021-07-14 
15:40:54&proStart=1 
startTime为开始时间，endTime为结束时间，proStart为执行耗时(ms) 
获取jdbc健康状态 
GET 
/rest/api/health/jdbc?jdbcPoolName=xxx 
jdbcPoolName可为空，为空时返回所有数据源状态列表，返回属性与JMX接口
一致。 
获取http通道健康状
态 
GET 
/rest/api/health/connector 


## 第 38 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
29 
功能名称 
请求类型 
请求地址 
获取server健康状态 
GET 
/rest/api/health/server 
健康检查功能默认不开启，如需开启需要配置-Dmonitor.healthCheck.enable=true。 
 
3.1.3 请求参数及返回值 
上一章节中提供了各模块的接口REST地址。对于请求参数和返回值描述如下。 
 
接口请求参数： 
⚫ 
attrName：对应JMX 功能中MBEAN 的属性列表，支持多个以“,”分割。 
⚫ 
operatorName：对应JMX 功能中MBEAN 的操作列表，支持多个以“,”分割。如果操作中含有参数
用“:”分割名称和值，例如operatorName=count: system-http-listener。如果某个操作有多个参数，
则参数间用 “|”分割，例operatorName=point:x|y 
⚫ 
pathValue：对应JMX 功能中MBEAN 的ObjectName 中含有{}指定的数据，若ObjectName 值中
不含有{}可忽略此属性 
 
返回值格式： 
⚫ 
name：功能名称 
⚫ 
success: true 调用成功; false 调用失败 
⚫ 
message: 调用失败原因，当success=false 可用。 
⚫ 
errorInfo：调用失败堆栈，当success=false 可用。 
⚫ 
data：存放真实数据，结构为[<key（String 类型），value（Object 类型）>] ；key 为要查询的
属性或操作，value 为对应的数据。 
 
成功调用返回值示例： 
 
{ 
"name": "WEB_CONTAINER", 
"success": true, 
"errorInfo": null, 
"message": null, 
"data": [{ 
"ajpListener": [], 
"httpListener": [ 
            { 
"name": "system-http-listener", 


## 第 39 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
30 
"port": 9060, 
"status": null, 
"http2-enabled": null, 
"ssl-enabled": null, 
"default-virtual-host": "admin", 
"create-time": "2019-09-19 11:12:17" 
            }, 
            { 
"name": "tong-http-listener", 
"port": 8080, 
"status": null, 
"address": null, 
"http2-enabled": null, 
"ssl-enabled": null, 
"default-virtual-host": "server", 
"create-time": "2019-09-19 11:12:17" 
            }, 
            { 
"property": [], 
"name": "ejb-server-listener", 
"port": 5100, 
"status": null, 
"address": null, 
"http2-enabled": null, 
"ssl-enabled": null, 
"default-virtual-host": "admin", 
"create-time": "2019-09-19 11:12:19" 
            } 
        ], 
"virtualHost": [ 
            { 
"property": [], 
"name": "admin", 
"listeners": "system-http-listener,tong-https-listener", 
"alias": null, 
"status": null, 
"addValve": null, 
"accesslog-enabled": false, 


## 第 40 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
31 
"accesslog-dir": "logs/access", 
"sso-enabled": false, 
"remote-filter-enabled": false, 
"app-base": null, 
"auto-deploy": null, 
"deploy-on-startup": null, 
"deploy-ignore": null, 
"undeploy-old-version": null 
            }, 
            { 
"property": [], 
"name": "server", 
"listeners": "tong-http-listener,tong-https-listener,tong-ajp-listener", 
"alias": null, 
"status": null, 
"addValve": null, 
"accesslog-enabled": false, 
"accesslog-dir": "logs/access", 
"sso-enabled": false, 
"remote-filter-enabled": false, 
"app-base": "autodeploy", 
"auto-deploy": true, 
"deploy-on-startup": null, 
"deploy-ignore": null, 
"undeploy-old-version": null 
            } 
        ] 
}] 
} 
3.2 heimdall集群控制台REST接口 
3.2.1 REST接口列表 
REST所有接口后均需添加username和password两个参数，如果未添加这两个参数，则无权限访问REST
接口信息。 
例如：使用http://localhost:9060/heimdall/restapi/tongweb/list?username=rig&password=rig123.com访问集中
管理工具时，无需登录便可查看到REST接口信息。 
也可使用如下方式curl --user name:password http://localhost:9060/heimdall/restapi/tongweb/list进行访问。 


## 第 41 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
32 
说明： 
⚫ 
用户名、密码与TongWeb集中管理工具相同（rig/初始密码rig123.com）。调用REST时，密码无最长
使用期限，即90天后不会强制要求修改密码。 
⚫ 
curl命令执行时，若url中含有‘&’等特殊字符，url需要加引号。 
以下表格列出了heimdall集群控制台所有模块的REST接口的请求地址。 
3.2.2 返回值格式说明 
以下表格列出了返回值参数说明。 
3.2.3 接口地址调用示例 
3.2.3.1 查看所有tongweb节点 
请求地址 
/restapi/tongweb/list 
请求方式 
GET, POST 
请求参数 
无 
返回值 
⚫ 
id：节点id； 
⚫ 
name：节点名称； 
⚫ 
tongwebHome：节点位置； 
⚫ 
na：节点代理ip； 
⚫ 
port：节点管理控制台端口； 
⚫ 
cluster：节点所在集群； 
⚫ 
status：节点状态。 
功能名称 
类型 
请求地址 
查看所有tongweb节点 
GET, POST 
/restapi/tongweb/list 
启动tongweb节点 
GET, POST 
/restapi/tongweb/start 
停止tongweb节点 
GET, POST 
/restapi/tongweb/stop 
查看tongweb集群 
GET, POST 
/restapi/clusters/tree/target 
部署应用至集群 
GET, POST 
/restapi/clusters/tree/deploy 
解部署应用 
GET, POST 
/restapi/clusters/deployers/delete 
参数名称 
参数说明 
name 
功能名称。 
success 
true调用成功；false调用失败 
message 
调用失败原因，当success=false可用。 
errorInfo 
调用失败堆栈，当success=false可用。 
otherInfo 
存放真实数据。 


## 第 42 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
33 
示例说明 
/restapi/tongweb/list?username=rig&password=rig123.com 
{ 
  "name": null, 
  "success": true, 
  "errorInfo": null, 
  "message": null, 
  "otherInfo": [ 
    { 
      "id": "1035702074", 
      "name": "tongweb-1", 
      "tongwebHome": 
"D:\\workspace\\tong\\tw7\\tw-release\\target\\TW7-release-2024-06-20\\Agent\\nodes\\tong
web-1", 
      "na": "127.0.0.1", 
      "port": "9061", 
      "cluster": "t", 
      "status": "stopped", 
      "desc": null, 
      "install": false, 
      "restart": false, 
      "jmxport": 0 
    } 
  ] 
} 
 
3.2.3.2 启动tongweb节点 
请求地址 
/restapi/tongweb/start 
请求方式 
GET, POST 
请求参数 
tongwebId：节点id 
返回值 
success：true启动成功，false启动失败 
示例说明 
/restapi/tongweb/start?tongwebId=1035702074&username=rig&password=rig123.com 
 
[ 
  { 
    "name": "1035702074", 
    "success": true, 
    "errorInfo": null, 


## 第 43 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
34 
    "message": null, 
    "otherInfo": null 
  } 
] 
 
3.2.3.3 停止tongweb节点 
请求地址 
/restapi/tongweb/stop 
请求方式 
GET, POST 
请求参数 
tongwebId：节点id 
返回值 
success：true停止成功，false停止失败 
示例说明 
/restapi/tongweb/stop?tongwebId=1035702074&username=rig&password=rig123.com 
 
[ 
  { 
    "name": "1035702074", 
    "success": true, 
    "errorInfo": null, 
    "message": null, 
    "otherInfo": null 
  } 
] 
 
3.2.3.4 查看tongweb集群 
请求地址 
/restapi/clusters/tree/target?treeId=cluster 
请求方式 
GET, POST 
请求参数 
treeId：cluster 
返回值 
treeId：集群id 
示例说明 
/restapi/clusters/tree/target?treeId=cluster&username=rig&password=rig123.com 
 
[{ 
 
"checked": false, 
 
"chkDisabled": true, 
 
"diyshowName": "t", 
 
"ipAndName": "t", 
 
"isParent": false, 
 
"name": "t", 


## 第 44 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
35 
 
"parentId": "cluster", 
 
"path": "", 
 
"sessionCopyType": "", 
 
"status": "", 
 
"treeId": "t_1718853702218" 
}] 
 
3.2.3.5 部署应用至集群 
请求地址 
/restapi/clusters/tree/deploy 
请求方式 
GET, POST 
请求参数 
⚫ 
appName：应用名称 
⚫ 
appContextRoot：应用前缀 
⚫ 
deployOrder：部署顺序 
 
⚫ 
delegate：类加载顺序; false子优先, true父优先 
⚫ 
target：集群id 
⚫ 
appLocation：应用目录位置 
⚫ 
jspCompile：JSP预编译 
⚫ 
appType=war 
返回值 
⚫ 
success：true部署成功，false部署失败 
⚫ 
otherInfo：集群各节点部署信息 
示例说明 
/restapi/clusters/tree/deploy?appName=nonXaDsWeb&appContextRoot=%2FnonXaDsWeb
&deployOrder=100&deployTimeout=600&delegate=false&cacheMaxSize=10240&appDesc
ription=&targets=&sessionCopyType=TDG&redisModel=single&redisMainNode=1&redis
Db=0&redisPassword=NjHQrrVekUW241%2FKgenD7e1N8GyPDWQ%2Bo%2Bdq1ucqR
DRvI%2F4zm3OqqoRo5fNJ%2Br6Wwy6FeDgWA5t5ENG2fs%2F4SqikmOf7qhR9XxPBj
%2B7sPiCSBWb2p6nk%2Fad%2F8YoJaFe1Ge4IY8MTougIr%2FaWK33Dw%2BhvmGN3
XMQxdArFL69xVmo%3D&redisRetryTimes=5&redisConnectionTimeout=2000&redisTim
eout=2000&redisClientName=&connectionPoolMaxTotal=8&maxWaitMillis=1800&testWh
ileIdle=false&lifo=true&minEvictableIdleTimeMillis=1800000&timeBetweenEvictionRuns
Millis=-1&connectionPoolMinIdle=0&target=t_1718853702218&appsource=server&TICK
ET_NONCE=0DF18AA1264532F2B1234A6CDEC85BA1&vsnames=&appName=nonXaD
sWeb&appLocation=D%253A%255C%2FnonXaDsWeb%2F&jspCompile=false&requestPa
rametersLostValidation=false&sdDeploy=false&monitdir=false&appType=war 
 
{ 
  "name": null, 
  "success": true, 


## 第 45 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
36 
  "errorInfo": null, 
  "message": null, 
  "otherInfo": [ 
    { 
      "errorInfo": null, 
      "nodeID": "127.0.0.1", 
      "name": null, 
      "twID": "1035702074", 
      "clusterID": "t", 
      "path": 
"D:\\workspace\\tong\\tw7\\tw-release\\target\\TW7-release-2024-06-20\\Agent\\nodes\\tong
web-1", 
      "message": null, 
      "type": null, 
      "twStatus": null, 
      "target": { 
        "type": "cluster", 
        "targetId": "t_1718853702218", 
        "enable": "true" 
      }, 
      "subResult": null, 
      "error": false, 
      "success": true 
    } 
  ] 
} 
 
3.2.3.6 解部署应用 
请求地址 
/restapi/clusters/deployers/delete 
请求方式 
GET, POST 
请求参数 
appId：应用id 
返回值 
⚫ 
success：true解部署成功，false解部署失败 
⚫ 
otherInfo：集群各节点解部署信息 
示例说明 
/restapi/clusters/deployers/delete?appId=nonXaDsWeb&username=rig&password=rig123.co
m 
 
{ 


## 第 46 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
37 
  "name": null, 
  "success": true, 
  "errorInfo": null, 
  "message": null, 
  "otherInfo": [ 
    { 
      "errorInfo": null, 
      "nodeID": "1", 
      "name": "nonXaDsWeb", 
      "twID": null, 
      "clusterID": null, 
      "path": null, 
      "message": null, 
      "type": null, 
      "twStatus": null, 
      "target": null, 
      "subResult": [ 
        { 
          "errorInfo": null, 
          "nodeID": "127.0.0.1", 
          "name": null, 
          "twID": "1035702074", 
          "clusterID": "t", 
          "path": 
"D:\\workspace\\tong\\tw7\\tw-release\\target\\TW7-release-2024-06-20\\Agent\\nodes\\tong
web-1", 
          "message": null, 
          "type": null, 
          "twStatus": null, 
          "target": { 
            "type": "cluster", 
            "targetId": "t_1718853702218", 
            "enable": "true" 
          }, 
          "subResult": null, 
          "error": false, 
          "success": true 
        } 


## 第 47 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
38 
      ], 
      "error": false, 
      "success": true 
    } 
  ] 
} 
 


## 第 48 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
39 
第4章 SNMP 
4.1 OID列表 
4.1.1 操作系统信息 
Object Namejava.lang:type=OperatingSystem 
表 4.1-1：操作系统信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.1.1.1 
OctetString 
Arch 
amd64 
.1.3.6.1.4.1.55566.1.1.1.2 
Integer 
AvailableProcessors 
8 
.1.3.6.1.4.1.55566.1.1.1.3 
OctetString 
CommittedVirtualMemorySize 2457640960 
.1.3.6.1.4.1.55566.1.1.1.4 
OctetString 
FreePhysicalMemorySize 
5564010496 
.1.3.6.1.4.1.55566.1.1.1.5 
OctetString 
FreeSwapSpaceSize 
6200578048 
.1.3.6.1.4.1.55566.1.1.1.6 
OctetString 
Name 
Windows 10 
.1.3.6.1.4.1.55566.1.1.1.7 
OctetString 
ObjectName 
java.lang:type=OperatingSystem 
.1.3.6.1.4.1.55566.1.1.1.8 
OctetString 
ProcessCpuLoad 
0.001546481 
.1.3.6.1.4.1.55566.1.1.1.9 
OctetString 
ProcessCpuTime 
71125000000 
.1.3.6.1.4.1.55566.1.1.1.10 
OctetString 
SystemCpuLoad 
0.085423789 
.1.3.6.1.4.1.55566.1.1.1.11 
OctetString 
SystemLoadAverage 
-1 
.1.3.6.1.4.1.55566.1.1.1.12 
OctetString 
TotalPhysicalMemorySize 
16936042496 
.1.3.6.1.4.1.55566.1.1.1.13 
OctetString 
TotalSwapSpaceSize 
29820944384 
.1.3.6.1.4.1.55566.1.1.1.14 
OctetString 
Version 
10.0  
 
4.1.2 java运行时信息 
Object Namejava.lang:type=Runtime 
表 4.1-2：java 运行时信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.1.2.1 
OctetString 
BootClassPath 
D:\ja-work-space\tw-release\target\bin\.. 
/lib/endorsed\annotation-api.jar; 
D:\Java\jdk1.8.0_261\jre\lib\resources.jar; 
D:\Java\jdk1.8.0_261\jre\lib\rt.jar; 
D:\Java\jdk1.8.0_261\jre\lib\sunrsasign.jar; 
D:\Java\jdk1.8.0_261\jre\lib\jsse.jar; 


## 第 49 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
40 
OID 
Type 
Name 
Test Value 
D:\Java\jdk1.8.0_261\jre\lib\jce.jar; 
D:\Java\jdk1.8.0_261\jre\lib\charsets.jar; 
D:\Java\jdk1.8.0_261\jre\lib\jfr.jar; 
D:\Java\jdk1.8.0_261\jre\classes 
.1.3.6.1.4.1.55566.1.1.2.2 
OctetString 
BootClassPath
Supported 
TRUE 
.1.3.6.1.4.1.55566.1.1.2.3 
OctetString 
ClassPath 
D:\Java\jdk1.8.0_261\lib\tools.jar; 
D:\ja-work-space\tw-release\target\ 
TW_2020-11-13\bin\..\lib\bootstrap.jar; 
D:\ja-work-space\ tw-release\target\ 
TW_2020-11-13\bin\..\lib\sigar\sigar.jar; 
D:\ja-work-space\tw-release\target\ 
TW_2020-11-13\bin\..\lib\jdk-api.jar; 
D:\ja-work-space\tw-release\target\ 
TW_2020-11-13\bin\../lib/ejb-agent.jar 
.1.3.6.1.4.1.55566.1.1.2.4 
OctetString 
InputArgumen
ts 
#NAME? 
.1.3.6.1.4.1.55566.1.1.2.5 
OctetString 
LibraryPath 
D:\ja-work-space\tw-release\target\ 
TW_2020-11-13\bin\../native/windows/x64; 
D:\ja-work-space\tw-release\target\ 
TW_2020-11-13\bin\..\lib\sigar 
.1.3.6.1.4.1.55566.1.1.2.6 
OctetString 
ManagementS
pecVersion 
1.2 
.1.3.6.1.4.1.55566.1.1.2.7 
OctetString 
Name 
12944@DESKTOP-PHG17UD 
.1.3.6.1.4.1.55566.1.1.2.8 
OctetString 
ObjectName 
java.lang:type=Runtime 
.1.3.6.1.4.1.55566.1.1.2.9 
OctetString 
SpecName 
Java Virtual Machine Specification 
.1.3.6.1.4.1.55566.1.1.2.10 
OctetString 
SpecVendor 
Oracle Corporation 
.1.3.6.1.4.1.55566.1.1.2.11 
OctetString 
SpecVersion 
1.8 
.1.3.6.1.4.1.55566.1.1.2.12 
OctetString 
StartTime 
1.60627E+12 
.1.3.6.1.4.1.55566.1.1.2.13 
OctetString 
SystemPropert
ies 
UN SUPPORT 
.1.3.6.1.4.1.55566.1.1.2.14 
OctetString 
Uptime 
451388 
.1.3.6.1.4.1.55566.1.1.2.15 
OctetString 
VmName 
Java HotSpot(TM) 64-Bit Server VM 
.1.3.6.1.4.1.55566.1.1.2.16 
OctetString 
VmVendor 
Oracle Corporation 
.1.3.6.1.4.1.55566.1.1.2.17 
OctetString 
VmVersion 
25.261-b12 
 


## 第 50 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
41 
4.1.3 java类加载信息 
Object Name java.lang:type=ClassLoading 
表 4.1-3：java 类加载信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.1.3.1 
Integer 
LoadedClassCount 
14600 
.1.3.6.1.4.1.55566.1.1.3.2 
OctetString 
ObjectName 
java.lang:type=ClassLoading 
.1.3.6.1.4.1.55566.1.1.3.3 
OctetString 
TotalLoadedClassCount 
14600 
.1.3.6.1.4.1.55566.1.1.3.4 
OctetString 
UnloadedClassCount 
0 
.1.3.6.1.4.1.55566.1.1.3.5 
OctetString 
Verbose 
FALSE 
 
4.1.4 java编译信息 
Object Name java.lang:type=Compilation 
表 4.1-4：java 编译信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.1.4.1 
OctetString 
CompilationTimeMonitoringSu
pported 
TRUE 
.1.3.6.1.4.1.55566.1.1.4.2 
OctetString 
Name 
HotSpot 64-Bit Tiered Compilers 
.1.3.6.1.4.1.55566.1.1.4.3 
OctetString 
ObjectName 
java.lang:type=Compilation 
.1.3.6.1.4.1.55566.1.1.4.4 
OctetString 
TotalCompilationTime 
35812 
 
4.1.5 java内存信息 
Object Name java.lang:type=Memory 
表 4.1-5：java 内存信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.1.5.1 
OctetString 
HeapMemoryUsage 
UN SUPPORT 
.1.3.6.1.4.1.55566.1.1.5.2 
OctetString 
NonHeapMemoryUsage 
UN SUPPORT 
.1.3.6.1.4.1.55566.1.1.5.3 
OctetString 
ObjectName 
java.lang:type=Memory 
.1.3.6.1.4.1.55566.1.1.5.4 
Integer 
ObjectPendingFinalizationCount 
0 
.1.3.6.1.4.1.55566.1.1.5.5 
OctetString 
Verbose 
FALSE 
 


## 第 51 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
42 
4.1.6 java线程信息 
Object Name java.lang:type=Threading 
表 4.1-6：java 线程信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.1.6.1 
OctetString 
AllThreadIds 
187,186,185,184,183,182,181,180, 
179,178,177,176,174,173,171,170, 
152,151,118,117,116,115,114,113, 
112,110,109,107,106,105,100,99, 
98,96,95,94,93,92,91,90,89,88, 
87,86,85,44,43,21,20,19,18,16, 
15,5,4,3,2,1 
.1.3.6.1.4.1.55566.1.1.6.2 
OctetString 
CurrentThreadCpuTime 
625000000 
.1.3.6.1.4.1.55566.1.1.6.3 
OctetString 
CurrentThreadCpuTimeS
upported 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.4 
OctetString 
CurrentThreadUserTime 
46875000 
.1.3.6.1.4.1.55566.1.1.6.5 
Integer 
DaemonThreadCount 
50 
.1.3.6.1.4.1.55566.1.1.6.6 
OctetString 
ObjectMonitorUsageSupp
orted 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.7 
OctetString 
ObjectName 
java.lang:type=Threading 
.1.3.6.1.4.1.55566.1.1.6.8 
Integer 
PeakThreadCount 
61 
.1.3.6.1.4.1.55566.1.1.6.9 
OctetString 
SynchronizerUsageSuppo
rted 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.10 
OctetString 
ThreadAllocatedMemory
Enabled 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.11 
OctetString 
ThreadAllocatedMemory
Supported 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.12 
OctetString 
ThreadContentionMonitor
ingEnabled 
FALSE 
.1.3.6.1.4.1.55566.1.1.6.13 
OctetString 
ThreadContentionMonitor
ingSupported 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.14 
Integer 
ThreadCount 
58 
.1.3.6.1.4.1.55566.1.1.6.15 
OctetString 
ThreadCpuTimeEnabled 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.16 
OctetString 
ThreadCpuTimeSupporte
d 
TRUE 
.1.3.6.1.4.1.55566.1.1.6.17 
OctetString 
TotalStartedThreadCount 175 
 


## 第 52 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
43 
4.1.7 java垃圾回收信息 
Object Name java.lang:type=GarbageCollector,name=* 
表 4.1-7：java 垃圾回收信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.1.7.1.1 
OctetString 
CollectionCount 
12 
.1.3.6.1.4.1.55566.1.1.7.1.2 
OctetString 
CollectionTime 
267 
.1.3.6.1.4.1.55566.1.1.7.1.3 
OctetString 
LastGcInfo 
UN SUPPORT 
.1.3.6.1.4.1.55566.1.1.7.1.4 
OctetString 
MemoryPoolNames 
PS Eden Space 
.1.3.6.1.4.1.55566.1.1.7.1.5 
OctetString 
Name 
PS Scavenge 
.1.3.6.1.4.1.55566.1.1.7.1.6 
OctetString 
ObjectName 
java.lang:type=GarbageCollector 
.1.3.6.1.4.1.55566.1.1.7.1.7 
OctetString 
Valid 
TRUE 
.1.3.6.1.4.1.55566.1.1.7.2.1 
OctetString 
CollectionCount 
4 
.1.3.6.1.4.1.55566.1.1.7.2.2 
OctetString 
CollectionTime 
498 
.1.3.6.1.4.1.55566.1.1.7.2.3 
OctetString 
LastGcInfo 
UN SUPPORT 
.1.3.6.1.4.1.55566.1.1.7.2.4 
OctetString 
MemoryPoolNames 
PS Eden Space 
.1.3.6.1.4.1.55566.1.1.7.2.5 
OctetString 
Name 
PS MarkSweep 
.1.3.6.1.4.1.55566.1.1.7.2.6 
OctetString 
ObjectName 
java.lang:type=GarbageCollector 
.1.3.6.1.4.1.55566.1.1.7.2.7 
OctetString 
Valid 
TRUE 
 
4.1.8 JDBC连接池信息 
Object Name config:parent=/Tongweb/Server,name=JDBCConnectionPool* 
表 4.1-8：JDBC 连接池信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.2.1.1.1 
OctetString 
abandonWhenPercentageFull 0 
.1.3.6.1.4.1.55566.1.2.1.1.2 
OctetString 
algorithmType 
0 
.1.3.6.1.4.1.55566.1.2.1.1.3 
OctetString 
assocWithThread 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.4 
OctetString 
classPath 
C:/Downloads/mysql- 
connector-java-5.1.43.jar 
.1.3.6.1.4.1.55566.1.2.1.1.5 
OctetString 
clientInfo 
0 
.1.3.6.1.4.1.55566.1.2.1.1.6 
OctetString 
commitOnReturn 
TRUE 
.1.3.6.1.4.1.55566.1.2.1.1.7 
OctetString 
connectionProperties 
0 
.1.3.6.1.4.1.55566.1.2.1.1.8 
OctetString 
dataSourceCreator 
lite 
.1.3.6.1.4.1.55566.1.2.1.1.9 
OctetString 
defaultAutoCommit 
TRUE 


## 第 53 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
44 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.2.1.1.10 
OctetString 
defaultCatalog 
0 
.1.3.6.1.4.1.55566.1.2.1.1.11 
OctetString 
defaultReadOnly 
0 
.1.3.6.1.4.1.55566.1.2.1.1.12 
OctetString 
defaultTransactionIsolation 
0 
.1.3.6.1.4.1.55566.1.2.1.1.13 
OctetString 
failoverRequestIfBusy 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.14 
OctetString 
fairQueue 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.15 
OctetString 
ignoreExceptionOnPreLoad 
TRUE 
.1.3.6.1.4.1.55566.1.2.1.1.16 
OctetString 
initialSize 
10 
.1.3.6.1.4.1.55566.1.2.1.1.17 
OctetString 
isMulti 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.18 
OctetString 
isXa 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.19 
OctetString 
jdbcConnectionPoolRefs 
0 
.1.3.6.1.4.1.55566.1.2.1.1.20 
OctetString 
jdbcDriver 
com.mysql.jdbc.Driver 
.1.3.6.1.4.1.55566.1.2.1.1.21 
OctetString 
jdbcInterceptors 
StatusMonitor; 
QueryTimeoutIntercep 
tor(queryTimeout=0) 
.1.3.6.1.4.1.55566.1.2.1.1.22 
OctetString 
jdbcUrl 
jdbc:mysql://127.0.0.1:3006 
.1.3.6.1.4.1.55566.1.2.1.1.23 
OctetString 
jtaManaged 
TRUE 
.1.3.6.1.4.1.55566.1.2.1.1.24 
OctetString 
leakCheck 
TRUE 
.1.3.6.1.4.1.55566.1.2.1.1.25 
OctetString 
logAbandoned 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.26 
OctetString 
logValidationErrors 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.27 
OctetString 
maxActive 
10 
.1.3.6.1.4.1.55566.1.2.1.1.28 
OctetString 
maxAge 
0 
.1.3.6.1.4.1.55566.1.2.1.1.29 
OctetString 
maxIdle 
100 
.1.3.6.1.4.1.55566.1.2.1.1.30 
OctetString 
maxWaitTime 
30000 
.1.3.6.1.4.1.55566.1.2.1.1.31 
OctetString 
minEvictableIdleTime 
60000 
.1.3.6.1.4.1.55566.1.2.1.1.32 
OctetString 
minIdle 
10 
.1.3.6.1.4.1.55566.1.2.1.1.33 
OctetString 
modelerType 
com.tongweb.config.bean. 
JDBCConnectionPool 
.1.3.6.1.4.1.55566.1.2.1.1.34 
OctetString 
name 
Montclairey 
.1.3.6.1.4.1.55566.1.2.1.1.35 
OctetString 
password 
ZkwRPrJ2JktrXJAobnN3qg 
.1.3.6.1.4.1.55566.1.2.1.1.36 
OctetString 
propagateInterruptState 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.37 
OctetString 
removeAbandoned 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.38 
OctetString 
removeAbandonedTimeout 
2 
.1.3.6.1.4.1.55566.1.2.1.1.39 
OctetString 
rollbackOnReturn 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.40 
OctetString 
testFrequencySeconds 
0 
.1.3.6.1.4.1.55566.1.2.1.1.41 
OctetString 
testOnBorrow 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.42 
OctetString 
testOnConnect 
FALSE 


## 第 54 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
45 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.2.1.1.43 
OctetString 
testOnReturn 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.44 
OctetString 
testWhileIdle 
FALSE 
.1.3.6.1.4.1.55566.1.2.1.1.45 
OctetString 
timeBetweenEvictionRuns 
60000 
.1.3.6.1.4.1.55566.1.2.1.1.46 
OctetString 
userName 
root 
.1.3.6.1.4.1.55566.1.2.1.1.47 
OctetString 
validationInterval 
30000 
.1.3.6.1.4.1.55566.1.2.1.1.48 
OctetString 
validationQuery 
SELECT 1 
.1.3.6.1.4.1.55566.1.2.1.1.49 
OctetString 
validationQueryTimeout 
5 
 
4.1.9 Web容器信息 
Object Name config:name=WebContainer,parent=/Tongweb/Server 
表 4.1-9：Web 容器信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.2.2.1 
OctetString 
accessLog 
com.tongweb.config.bean.AccessLog 
@3c947bc5 
.1.3.6.1.4.1.55566.1.2.2.2 
OctetString 
ajpListener 
[] 
.1.3.6.1.4.1.55566.1.2.2.3 
OctetString 
hostnameVerifier 
NullHostnameVerifier 
.1.3.6.1.4.1.55566.1.2.2.4 
OctetString 
httpListener 
[com.tongweb.config.bean.HttpListener 
@60015ef5 
.1.3.6.1.4.1.55566.1.2.2.5 
Integer 
hungThreadThreshold 
0 
.1.3.6.1.4.1.55566.1.2.2.6 
OctetString 
jspDevelopment 
TRUE 
.1.3.6.1.4.1.55566.1.2.2.7 
OctetString 
jvmRoute 
0 
.1.3.6.1.4.1.55566.1.2.2.8 
OctetString 
modelerType 
com.tongweb.config.bean.WebContainer 
.1.3.6.1.4.1.55566.1.2.2.9 
OctetString 
parameterEncoding 
GBK 
.1.3.6.1.4.1.55566.1.2.2.10 
OctetString 
property 
[com.tongweb.config.bean.Property 
@3e96bacf 
.1.3.6.1.4.1.55566.1.2.2.11 
OctetString 
responseEncoding 
GBK 
.1.3.6.1.4.1.55566.1.2.2.12 
Integer 
sessionTimeout 
30 
.1.3.6.1.4.1.55566.1.2.2.13 
OctetString 
virtualHost 
[com.tongweb.config.bean.VirtualHost 
@55f616cf 
 
4.1.10 线程池信息 
Object Name TONGWEB:type=ThreadPool,name=* 


## 第 55 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
46 
表 4.1-10：线程池信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.1.*.1 
Integer 
acceptCount 
100 
.1.3.6.1.4.1.55566.1.3.1.*.2 
Integer 
acceptorThreadCount 
1 
.1.3.6.1.4.1.55566.1.3.1.*.3 
Integer 
acceptorThreadPriority 5 
.1.3.6.1.4.1.55566.1.3.1.*.4 
OctetString 
alpnSupported 
FALSE 
.1.3.6.1.4.1.55566.1.3.1.*.5 
OctetString 
bindOnInit 
TRUE 
.1.3.6.1.4.1.55566.1.3.1.*.6 
OctetString 
connectionCount 
1 
.1.3.6.1.4.1.55566.1.3.1.*.7 
Integer 
connectionLinger 
-1 
.1.3.6.1.4.1.55566.1.3.1.*.8 
Integer 
connectionTimeout 
60000 
.1.3.6.1.4.1.55566.1.3.1.*.9 
Integer 
currentThreadCount 
0 
.1.3.6.1.4.1.55566.1.3.1.*.10 
Integer 
currentThreadsBusy 
0 
.1.3.6.1.4.1.55566.1.3.1.*.11 
OctetString 
daemon 
TRUE 
.1.3.6.1.4.1.55566.1.3.1.*.12 
OctetString 
defaultSSLHostConfigN
ame 
_default_ 
.1.3.6.1.4.1.55566.1.3.1.*.13 
OctetString 
deferAccept 
FALSE 
.1.3.6.1.4.1.55566.1.3.1.*.14 
OctetString 
domain 
TONGWEB 
.1.3.6.1.4.1.55566.1.3.1.*.15 
OctetString 
executorTerminationTi
meoutMillis 
5000 
.1.3.6.1.4.1.55566.1.3.1.*.16 
Integer 
keepAliveCount 
0 
.1.3.6.1.4.1.55566.1.3.1.*.17 
Integer 
keepAliveTimeout 
60000 
.1.3.6.1.4.1.55566.1.3.1.*.18 
Integer 
localPort 
5100 
.1.3.6.1.4.1.55566.1.3.1.*.19 
Integer 
maxConnections 
10000 
.1.3.6.1.4.1.55566.1.3.1.*.20 
Integer 
maxKeepAliveRequests 100 
.1.3.6.1.4.1.55566.1.3.1.*.21 
Integer 
maxThreads 
200 
.1.3.6.1.4.1.55566.1.3.1.*.22 
Integer 
minSpareThreads 
10 
.1.3.6.1.4.1.55566.1.3.1.*.23 
OctetString 
modelerType 
com.tongweb.web.util.net.NioE
ndpoint 
.1.3.6.1.4.1.55566.1.3.1.*.24 
OctetString 
name 
http-nio-5100 
.1.3.6.1.4.1.55566.1.3.1.*.25 
OctetString 
paused 
FALSE 
.1.3.6.1.4.1.55566.1.3.1.*.26 
Integer 
pollerThreadCount 
1 
.1.3.6.1.4.1.55566.1.3.1.*.27 
Integer 
pollerThreadPriority 
5 
.1.3.6.1.4.1.55566.1.3.1.*.28 
Integer 
port 
5100 
.1.3.6.1.4.1.55566.1.3.1.*.29 
Integer 
portOffset 
0 
.1.3.6.1.4.1.55566.1.3.1.*.30 
Integer 
portWithOffset 
5100 
.1.3.6.1.4.1.55566.1.3.1.*.31 
OctetString 
running 
TRUE 
.1.3.6.1.4.1.55566.1.3.1.*.32 
OctetString 
sSLEnabled 
FALSE 


## 第 56 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
47 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.1.*.33 
OctetString 
selectorTimeout 
1000 
.1.3.6.1.4.1.55566.1.3.1.*.34 
Integer 
sniParseLimit 
65536 
.1.3.6.1.4.1.55566.1.3.1.*.35 
OctetString 
sslImplementation 
0 
.1.3.6.1.4.1.55566.1.3.1.*.36 
OctetString 
sslImplementationName 0 
.1.3.6.1.4.1.55566.1.3.1.*.37 
OctetString 
tcpNoDelay 
TRUE 
.1.3.6.1.4.1.55566.1.3.1.*.38 
Integer 
threadPriority 
5 
.1.3.6.1.4.1.55566.1.3.1.*.39 
OctetString 
useInheritedChannel 
FALSE 
.1.3.6.1.4.1.55566.1.3.1.*.40 
OctetString 
useSendfile 
TRUE 
 
4.1.11 TongWeb应用信息 
Object Name TONGWEB:j2eeType=WebModule,name=//*/*,* 
表 4.1-11：TongWeb 应用信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.2.*.1 
OctetString 
addWebinfClassesResources 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.2 
OctetString 
allowCasualMultipartParsing 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.3 
OctetString 
allowLinking 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.4 
OctetString 
allowMultipleLeadingForwardSl
ashInPath 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.5 
OctetString 
altDDName 
0 
.1.3.6.1.4.1.55566.1.3.2.*.6 
OctetString 
antiResourceLocking 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.7 
OctetString 
applicationEventListeners 
0 
.1.3.6.1.4.1.55566.1.3.2.*.8 
OctetString 
applicationLifecycleListeners 
0 
.1.3.6.1.4.1.55566.1.3.2.*.9 
Integer 
backgroundProcessorDelay 
-1 
.1.3.6.1.4.1.55566.1.3.2.*.10 
OctetString 
baseName 
ejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.11 
OctetString 
cachingAllowed 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.12 
OctetString 
catalinaBase 
D:\ja-work-space\tw-release\ 
target\TW_2020-11-13 
.1.3.6.1.4.1.55566.1.3.2.*.13 
OctetString 
catalinaHome 
D:\ja-work-space\tw-release\ 
target\TW_2020-11-13 
.1.3.6.1.4.1.55566.1.3.2.*.14 
OctetString 
charsetMapper 
com.tongweb.catalina.util. 
CharsetMapper@7636f097 
.1.3.6.1.4.1.55566.1.3.2.*.15 
OctetString 
charsetMapperClass 
com.tongweb.catalina.util. 
CharsetMapper 
.1.3.6.1.4.1.55566.1.3.2.*.16 
OctetString 
clearReferencesHttpClientKeep TRUE 


## 第 57 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
48 
OID 
Type 
Name 
Test Value 
AliveThread 
.1.3.6.1.4.1.55566.1.3.2.*.17 
OctetString 
clearReferencesObjectStreamCl
assCaches 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.18 
OctetString 
clearReferencesRmiTargets 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.19 
OctetString 
clearReferencesStopThreads 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.20 
OctetString 
clearReferencesStopTimerThrea
ds 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.21 
OctetString 
clearReferencesThreadLocals 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.22 
OctetString 
computedFailCtxIfServletStartF
ails 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.23 
OctetString 
configured 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.24 
OctetString 
containerSciFilter 
0 
.1.3.6.1.4.1.55566.1.3.2.*.25 
OctetString 
cookies 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.26 
OctetString 
copyXML 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.27 
OctetString 
createUploadTargets 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.28 
OctetString 
crossContext 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.29 
OctetString 
defaultContextPath 
0 
.1.3.6.1.4.1.55566.1.3.2.*.30 
OctetString 
defaultContextXml 
0 
.1.3.6.1.4.1.55566.1.3.2.*.31 
OctetString 
defaultWebXml 
0 
.1.3.6.1.4.1.55566.1.3.2.*.32 
OctetString 
delegate 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.33 
OctetString 
denyUncoveredHttpMethods 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.34 
OctetString 
dispatchersUseEncodedPaths 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.35 
OctetString 
displayName 
0 
.1.3.6.1.4.1.55566.1.3.2.*.36 
OctetString 
distributable 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.37 
OctetString 
docBase 
0 
.1.3.6.1.4.1.55566.1.3.2.*.38 
OctetString 
domain 
TONGWEB 
.1.3.6.1.4.1.55566.1.3.2.*.39 
OctetString 
domainInternal 
TONGWEB 
.1.3.6.1.4.1.55566.1.3.2.*.40 
Integer 
effectiveMajorVersion 
3 
.1.3.6.1.4.1.55566.1.3.2.*.41 
Integer 
effectiveMinorVersion 
0 
.1.3.6.1.4.1.55566.1.3.2.*.42 
OctetString 
encodedPath 
/ejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.43 
Integer 
errorCount 
0 
.1.3.6.1.4.1.55566.1.3.2.*.44 
OctetString 
failCtxIfServletStartFails 
0 
.1.3.6.1.4.1.55566.1.3.2.*.45 
OctetString 
fireRequestListenersOnForward
s 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.46 
OctetString 
ignoreAnnotations 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.47 
OctetString 
j2EEApplication 
none 


## 第 58 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
49 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.2.*.48 
OctetString 
j2EEServer 
none 
.1.3.6.1.4.1.55566.1.3.2.*.49 
OctetString 
javaVMs 
0 
.1.3.6.1.4.1.55566.1.3.2.*.50 
OctetString 
jndiExceptionOnFailedWrite 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.51 
OctetString 
logEffectiveWebXml 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.52 
OctetString 
logName 
com.tongweb.catalina.core. 
ContainerBase.[TONGWEB]. 
[server].[ejbserver] 
.1.3.6.1.4.1.55566.1.3.2.*.53 
OctetString 
loginConfig 
0 
.1.3.6.1.4.1.55566.1.3.2.*.54 
OctetString 
mBeanKeyProperties 
0 
.1.3.6.1.4.1.55566.1.3.2.*.55 
OctetString 
mapperContextRootRedirectEna
bled 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.56 
OctetString 
mapperDirectoryRedirectEnable
d 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.57 
OctetString 
maxTime 
0 
.1.3.6.1.4.1.55566.1.3.2.*.58 
OctetString 
minTime 
9.22337E+18 
.1.3.6.1.4.1.55566.1.3.2.*.59 
OctetString 
modelerType 
com.tongweb.tomee.catalina. 
remote.TomEERemoteWebapp 
.1.3.6.1.4.1.55566.1.3.2.*.60 
OctetString 
name 
ejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.61 
OctetString 
namingContextListener 
com.tongweb.catalina.core. 
NamingContextListener@4e1cfe9
2 
.1.3.6.1.4.1.55566.1.3.2.*.62 
OctetString 
namingContextName 
/TONGWEB/serverejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.63 
OctetString 
namingResources 
com.tongweb.catalina.deploy. 
NamingResourcesImpl@6a93ce5
e 
.1.3.6.1.4.1.55566.1.3.2.*.64 
OctetString 
objectKeyPropertiesNameOnly name=//server/ejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.65 
OctetString 
objectName 
TONGWEB:j2eeType=WebModu
le 
.1.3.6.1.4.1.55566.1.3.2.*.66 
OctetString 
objectNameKeyProperties 
j2eeType=WebModule 
.1.3.6.1.4.1.55566.1.3.2.*.67 
OctetString 
originalDocBase 
0 
.1.3.6.1.4.1.55566.1.3.2.*.68 
OctetString 
override 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.69 
OctetString 
path 
/ejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.70 
OctetString 
paused 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.71 
OctetString 
preemptiveAuthentication 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.72 
OctetString 
privileged 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.73 
OctetString 
processingTime 
0 


## 第 59 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
50 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.2.*.74 
OctetString 
publicId 
0 
.1.3.6.1.4.1.55566.1.3.2.*.75 
OctetString 
reloadable 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.76 
OctetString 
renewThreadsWhenStoppingCo
ntext 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.77 
OctetString 
replaceWelcomeFiles 
Get_Attribute_Error 
.1.3.6.1.4.1.55566.1.3.2.*.78 
OctetString 
requestCharacterEncoding 
0 
.1.3.6.1.4.1.55566.1.3.2.*.79 
Integer 
requestCount 
0 
.1.3.6.1.4.1.55566.1.3.2.*.80 
OctetString 
resourceOnlyServlets 
jsp 
.1.3.6.1.4.1.55566.1.3.2.*.81 
OctetString 
responseCharacterEncoding 
0 
.1.3.6.1.4.1.55566.1.3.2.*.82 
OctetString 
sendRedirectBody 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.83 
OctetString 
server 
0 
.1.3.6.1.4.1.55566.1.3.2.*.84 
OctetString 
servlet22 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.85 
OctetString 
sessionCookieDomain 
0 
.1.3.6.1.4.1.55566.1.3.2.*.86 
OctetString 
sessionCookieName 
0 
.1.3.6.1.4.1.55566.1.3.2.*.87 
OctetString 
sessionCookiePath 
0 
.1.3.6.1.4.1.55566.1.3.2.*.88 
OctetString 
sessionCookiePathUsesTrailing
Slash 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.89 
Integer 
sessionTimeout 
30 
.1.3.6.1.4.1.55566.1.3.2.*.90 
OctetString 
skipMemoryLeakChecksOnJvm
Shutdown 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.91 
OctetString 
startChildren 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.92 
Integer 
startStopThreads 
1 
.1.3.6.1.4.1.55566.1.3.2.*.93 
OctetString 
startTime 
1.60627E+12 
.1.3.6.1.4.1.55566.1.3.2.*.94 
OctetString 
startupTime 
0 
.1.3.6.1.4.1.55566.1.3.2.*.95 
OctetString 
stateName 
STARTED 
.1.3.6.1.4.1.55566.1.3.2.*.96 
OctetString 
swallowAbortedUploads 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.97 
OctetString 
swallowOutput 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.98 
OctetString 
throwOnFailure 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.99 
OctetString 
tldScanTime 
0 
.1.3.6.1.4.1.55566.1.3.2.*.100 
OctetString 
tldValidation 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.101 
OctetString 
unloadDelay 
2000 
.1.3.6.1.4.1.55566.1.3.2.*.102 
OctetString 
unpackWAR 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.103 
OctetString 
useHttpOnly 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.104 
OctetString 
useNaming 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.105 
OctetString 
useRelativeRedirects 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.106 
OctetString 
validateClientProvidedNewSessi TRUE 


## 第 60 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
51 
OID 
Type 
Name 
Test Value 
onId 
.1.3.6.1.4.1.55566.1.3.2.*.107 
OctetString 
webappVersion 
0 
.1.3.6.1.4.1.55566.1.3.2.*.108 
OctetString 
welcomeFiles 
0 
.1.3.6.1.4.1.55566.1.3.2.*.109 
OctetString 
workDir 
temp\work\server\ejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.110 
OctetString 
workPath 
D:\ja-work-space\tw-release\ 
target\TW_2020-11-13\temp\ 
work\server\ejbserver 
.1.3.6.1.4.1.55566.1.3.2.*.111 
OctetString 
wrapperClass 
com.tongweb.catalina.core. 
StandardWrapper 
.1.3.6.1.4.1.55566.1.3.2.*.112 
OctetString 
xmlBlockExternal 
TRUE 
.1.3.6.1.4.1.55566.1.3.2.*.113 
OctetString 
xmlNamespaceAware 
FALSE 
.1.3.6.1.4.1.55566.1.3.2.*.114 
OctetString 
xmlValidation 
FALSE 
 
4.1.12 TongWeb管理信息 
Object Name TONGWEB:type=Manager,host=*,context=/* 
表 4.1-12：TongWeb 管理信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.3.*.1 
Integer 
activeSessions 
0 
.1.3.6.1.4.1.55566.1.3.3.*.2 
OctetString 
className 
com.tongweb.catalina. 
session.StandardManager 
.1.3.6.1.4.1.55566.1.3.3.*.3 
Integer 
duplicates 
0 
.1.3.6.1.4.1.55566.1.3.3.*.4 
OctetString 
expiredSessions 
0 
.1.3.6.1.4.1.55566.1.3.3.*.5 
OctetString 
jvmRoute 
0 
.1.3.6.1.4.1.55566.1.3.3.*.6 
Integer 
maxActive 
0 
.1.3.6.1.4.1.55566.1.3.3.*.7 
Integer 
maxActiveSessions 
-1 
.1.3.6.1.4.1.55566.1.3.3.*.8 
OctetString 
modelerType 
com.tongweb.catalina. 
session.StandardManager 
.1.3.6.1.4.1.55566.1.3.3.*.9 
OctetString 
name 
StandardManager 
.1.3.6.1.4.1.55566.1.3.3.*.10 
OctetString 
pathname 
SESSIONS.ser 
.1.3.6.1.4.1.55566.1.3.3.*.11 
Integer 
processExpiresFrequency 6 
.1.3.6.1.4.1.55566.1.3.3.*.12 
OctetString 
processingTime 
0 
.1.3.6.1.4.1.55566.1.3.3.*.13 
Integer 
rejectedSessions 
0 
.1.3.6.1.4.1.55566.1.3.3.*.14 
OctetString 
secureRandomAlgorithm SHA1PRNG 
.1.3.6.1.4.1.55566.1.3.3.*.15 
OctetString 
secureRandomClass 
0 


## 第 61 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
52 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.3.*.16 
OctetString 
secureRandomProvider 
0 
.1.3.6.1.4.1.55566.1.3.3.*.17 
OctetString 
sessionAttributeNameFilt
er 
0 
.1.3.6.1.4.1.55566.1.3.3.*.18 
OctetString 
sessionAttributeValueClas
sNameFilter 
0 
.1.3.6.1.4.1.55566.1.3.3.*.19 
Integer 
sessionAverageAliveTime 0 
.1.3.6.1.4.1.55566.1.3.3.*.20 
OctetString 
sessionCounter 
0 
.1.3.6.1.4.1.55566.1.3.3.*.21 
Integer 
sessionCreateRate 
0 
.1.3.6.1.4.1.55566.1.3.3.*.22 
Integer 
sessionExpireRate 
0 
.1.3.6.1.4.1.55566.1.3.3.*.23 
Integer 
sessionMaxAliveTime 
0 
.1.3.6.1.4.1.55566.1.3.3.*.24 
OctetString 
stateName 
STARTED 
.1.3.6.1.4.1.55566.1.3.3.*.25 
OctetString 
warnOnSessionAttributeF
ilterFailure 
FALSE 
 
4.1.13 TongWeb服务信息 
Object Name TONGWEB:type=Server 
表 4.1-13：TongWeb 服务信息 
OID 
Type 
Name 
Test Value 
.1.3.6.1.4.1.55566.1.3.4.1 
OctetString 
address 
localhost 
.1.3.6.1.4.1.55566.1.3.4.2 
OctetString 
managedResource 
StandardServer[7090] 
.1.3.6.1.4.1.55566.1.3.4.3 
OctetString 
modelerType 
com.tongweb.catalina.core.StandardServe
r 
.1.3.6.1.4.1.55566.1.3.4.4 
Integer 
port 
7090 
.1.3.6.1.4.1.55566.1.3.4.5 
OctetString 
serverBuilt 
44147.70744 
.1.3.6.1.4.1.55566.1.3.4.6 
OctetString 
serverInfo 
TongWeb 
.1.3.6.1.4.1.55566.1.3.4.7 
OctetString 
serverNumber 
7.0.2.5 
.1.3.6.1.4.1.55566.1.3.4.8 
OctetString 
serviceNames 
TONGWEB:type=Service 
.1.3.6.1.4.1.55566.1.3.4.9 
OctetString 
shutdown 
TW7-SHUTDOWN 
.1.3.6.1.4.1.55566.1.3.4.10 
OctetString 
stateName 
STARTED 
 
 


## 第 62 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
53 
第5章 配置监控推送 
通过配置监控推送，TongWeb可以每天定时发送一次监控数据到用户指定的url中，并根据推送的返回
结果记录到单独的日志文件。具体配置步骤如下： 
打开${TongWeb_HOME}/conf/目录下的monitor-push.properties配置文件，填入配置项示例如下： 
 
具体字段说明: 
⚫ 
monitor.push.monitorEnable: 功能开关，false的时候将不启动定时器任务 
⚫ 
monitor.push.pushAddress: 用户配置监控中心的推送目标地址 
⚫ 
monitor.push.time.interval: 每天的推送时间 
⚫ 
monitor.push.system: 系统标识 
⚫ 
monitor.push.authcode: 授权码 
⚫ 
monitor.push.organ: 系统所属组织机构编号 
⚫ 
monitor.push.mac: 服务器mac地址 
⚫ 
monitor.push.ip: 服务器ip地址 
⚫ 
monitor.push.trace.log: 是否开启推送日志记录 
⚫ 
monitor.push.time.cron: 推送时间表达式 例如：monitor.push.time.cron=*/30 * * * * ? 
注：（当【每天的推送时间】配置时，monitor.push.trace.log和monitor.push.time.cron参数不生效  使
用此参数需要把monitor.push.time.interval参数注释掉） 


## 第 63 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
54 
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


## 第 64 页

东方通应用服务器软件TongWeb_V7.0二次开发接口 
7049_M9A01 
版权所有©东方通 
55 
 



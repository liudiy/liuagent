## 第 1 页

 
V7049A01 
1 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


## 第 2 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
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

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
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
2.8 查看安装信息，新增永久license绑定mac地址的说明。 
7049_M8A01 7.0.4.9_M8 
无 
7049_M7A01 7.0.4.9_M7 
无 
7049_M6A01 7.0.4.9_M6 
新增如下章节： 
2.8 查看安装信息 
修改如下章节： 
⚫ 
2.6 安装 License，将订阅模式修改为激活模式（active）。 
⚫ 
2.7 目录说明，补充二级目录说明。 
7049_M5A01 7.0.4.9_M5 
修改如下章节： 
2.6 安装 License，服务授权新增支持订阅模式。订阅模式既本地
文件授权，也支持授权平台授权。 
7049_M4A01 7.0.4.9_M4 
无 
7049_M3A01 7.0.4.9_M3 
无 
7049_M2A01 7.0.4.9_M2 
2.6 安装 License，使用 License Server 授权时，新增配置参数。 
7049_M1A01 7.0.4.9_M1 
附录A 开机自启动服务安装工具，新增集群模式下Agent服务的开
机自启说明。 
7049A01 
7.0.4.9 
修改如下章节： 
⚫ 
2.1 系统配置要求，新增支持JDK17。 
⚫ 
2.1 系统配置要求，国密认证JDK要求由“JDK8-JDK11”变更
为“JDK8及以上版本”，当在JDK17环境下，需要额外添加
启动参数。 
7048A01 
7.0.4.8 
修改如下章节： 
⚫ 
2.6 安装License，新增适配License Server，使用License Server
进行服务授权。 
⚫ 
3.1.3 安全停止，将原本的安全启动章节名称修改为“安全停
止”。 
⚫ 
3.1 系统配置要求，浏览器支持版本有IE8修改为“IE11”。 
⚫ 
3.1 安装要求，国密认证JDK环境要求由“JDK8小版本”修改
为“JDK8-JDK11”。 
7047A01 
7.0.4.7 
⚫ 
修改章节如下所示。 
◼ 
“3.8 目录说明”，将“apache-activemq”目录修改为
“tongweb-mq”。 
◼ 
“4.3.1 登录”更新“图4.3-3：首次登录修改密码设
置”。 
⚫ 
删除章节如下所示。 


## 第 4 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
iii 
手册版本 
适用于产品版本 
更新内容 
“1.6 集成第三方产品”，替换集成的activemq为OpenMq。 
7046A01 
7.0.4.6 
“3.5.2 Unix/Linux上停止服务器”停止命令增加超时时间设置 
7045A01 
7.0.4.5 
⚫ 
删除“5.6注意事项”中绝对路径的域，由于不受物理TongWeb
的管理，所以在创建时暂不支持端口自增加，只能手动修改。 
⚫ 
在“3.5.2Unix/Liunx上停止服务器”中添加快速停止TongWeb
参数quick 
⚫ 
将${TW_HOME}改为${TongWeb_HOME} 
⚫ 
将“ 2.3Windows 平台界面安装” 第9 条端口设置中的
jmx-connector修改为jmx-service 
⚫ 
更新“图3.3-5管理控制台首页”及服务器选择文件可选目录
说明 
⚫ 
更新“3.4.2 宕机重启模式用法”章节中的宕机重启参数说明 
7044A01 
7.0.4.4 
⚫ 
更新“图3.3-9端口设置界面”及“Linux平台命令行安装”中
shutdown-port默认为7090（原来为8005） 
⚫ 
“4.3.1登录”中添加更新初始密码的截图及提示 
⚫ 
更新“附录A 开机自启动服务安装工具”的使用方法 
⚫ 
更新“图4.3-3管理控制台首页”及说明 
⚫ 
删除原“3.2 软件安装包” 
7043A01 
7.0.4.3 
无 
7042A01 
7.0.4.2 
无 
7041A01 
7.0.4.1 
1. 统一使用TongWeb用户使用手册模板。 
2. 整合原《TongWeb7用户手册》第一章“TongWeb7应用服务器概
述”，第二章“安装指南”，第13章“TongWeb域”及附录4“开
机自启动服务安装工具说明”。 
3. 更新3.7专用机平台安装步骤 
 


## 第 5 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
iv 
前言 
本文档是TongWeb产品的用户使用手册之一，详细提供各版本的安装包，在不同平台上安装启动的步骤，
TongWeb域的创建及启停，开机自启动服务安装以及启动中的常见问题。 
 
适合的对象  
本手册主要适用于生产环境中的系统管理员，部分内容同样适用于应用开发人员和应用部署人员。  
本手册假定您已经具备如下技能：  
1. 基本系统管理任务； 
2. 安装软件； 
3. 使用Web浏览器； 
4. 启动数据库服务器； 
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
⚫ 008_TongWeb_V7.0二次开发接口：TongWeb的JMX，REST，SNMP接口说明。 
⚫ 009_TongWeb_V7.0应用开发手册：提供在TongWeb上开发应用的各类规范说明。 
⚫ 010_TongWeb_V7.0等级保护指南：提供等级保护功能开启后的使用说明。 
⚫ 100_TongWeb_V7.0集群管理指南-国防版：详细介绍集群的配置和管理。 
 
技术支持 
东方通产品将为您提供全方位的技术支持，您可以通过以下方式获得技术支持：  
网址：www.tongtech.com  
电话：400-650-7088 
邮箱：pqmo@tongtech.com 
 
您在取得技术支持时，请提供如下信息：  


## 第 6 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
v 
1.  您的姓名  
2.  您的公司信息  
3.  您的联系方式  
4.  操作系统及其版本  
5.  产品版本号  
6.  日志等错误的详细信息 
 


## 第 7 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
vi 
目 录 
第1章 TongWeb7应用服务器概述 ................................................................................................................... 1 
1.1 JavaEE规范 ............................................................................................................................................... 1 
1.2 规范支持 .................................................................................................................................................. 2 
1.3 体系结构 .................................................................................................................................................. 2 
1.4 TongWeb特性 ............................................................................................................................................ 4 
1.5 应用开发工具 .......................................................................................................................................... 4 
第2章 安装指南 ................................................................................................................................................. 6 
2.1 系统配置要求 .......................................................................................................................................... 6 
2.2 安装JDK环境 ........................................................................................................................................... 7 
2.3 Windows平台界面安装 ............................................................................................................................ 7 
2.4 Linux平台命令行安装 ............................................................................................................................ 12 
2.5 Linux平台静默安装 ................................................................................................................................ 17 
2.6 安装License ............................................................................................................................................ 18 
2.7 目录说明 ................................................................................................................................................ 19 
2.8 查看安装信息 ........................................................................................................................................ 21 
第3章 启动及停止 ........................................................................................................................................... 23 
3.1 启动服务器 ............................................................................................................................................ 23 
3.1.1 Windows上启动服务器 ................................................................................................................... 23 
3.1.2 Linux平台上启动服务器 ................................................................................................................. 23 
3.1.3 安全停止 ......................................................................................................................................... 23 
3.2 启动时记录TongWeb进程号 ................................................................................................................. 23 
3.3 管理控制台 ............................................................................................................................................ 24 
3.3.1 登录 ................................................................................................................................................. 24 
3.3.2 注销 ................................................................................................................................................. 27 
3.4 宕机重启模式 ........................................................................................................................................ 27 
3.4.1 宕机重启使用场景 ......................................................................................................................... 28 
3.4.2 宕机重启模式用法 ......................................................................................................................... 28 
3.5 停止服务器 ............................................................................................................................................ 29 
3.5.1 Windows上停止服务器 ................................................................................................................... 29 
3.5.2 Unix/Linux上停止服务器 ................................................................................................................ 29 
第4章 卸载TongWeb ....................................................................................................................................... 30 
4.1 Windows平台上卸载 .............................................................................................................................. 30 
4.2 Linux平台上卸载 .................................................................................................................................... 31 
第5章 TongWeb域 ........................................................................................................................................... 33 


## 第 8 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
vii 
5.1 概述 ........................................................................................................................................................ 33 
5.2 创建TongWeb域 ..................................................................................................................................... 33 
5.3 删除TongWeb域 ..................................................................................................................................... 34 
5.4 启动TongWeb域 ..................................................................................................................................... 34 
5.5 停止TongWeb域 ..................................................................................................................................... 34 
5.6 注意事项 ................................................................................................................................................ 34 
第6章 常见问题 ............................................................................................................................................... 35 
6.1 TongWeb启动失败 .................................................................................................................................. 35 
6.2 控制台无法访问 .................................................................................................................................... 36 
6.3 无法使用80端口 .................................................................................................................................... 38 
6.4 JVM内存无法调大 ................................................................................................................................. 38 
附录A 
开机自启动服务安装工具 ............................................................................................................... 39 
附录B 
术语及缩略语 ................................................................................................................................... 41 
 


## 第 9 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
1 
第1章 TongWeb7应用服务器概述 
应用服务器TongWeb V7.0全面支持JavaEE7及JavaEE8规范，作为基础架构软件，位于操作系统与应用
之间，帮助企业将业务应用集成在一个基础平台上，为应用高效、稳定、安全运行提供关键支撑，包括便
捷的开发、随需应变的灵活部署、丰富的运行时监视、高效的管理等。 
1.1 JavaEE规范 
应用服务器TongWeb v7支持JavaEE7和JavaEE8规范。新版规范提供了许多新的特性用来简化开发人员
的工作，提高开发效率。例如：用注解替代硬编码和xml配置文件，异步开发模型等等，使得开发人员可以
更加专注于业务功能的开发，不需要浪费太多时间在JavaEE程序的基础设施上。 
⚫ 
JavaEE7的主要增强 
◼ 
Servlet3.1 
Servlet3.1是JavaEE7中重点聚焦的功能之一，它使得开发web应用变得更加简单，增加了更
多便利的注解支持、提供可插拔设计、提供异步处理的支持等。 
◼ 
EJB3.2 
EJB3.2与JavaEE6提供的EJB3.1版本相比，支持本地异步会话Bean调用；有状态会话bean的生
命周期回调拦截方法，现在可以在一个事务环境中执行；可以完全禁用特定的有状态会话bean
的钝化；TimerService API已被扩展，现在可以在同一个EJB模块中查询所有活动计时器等等。 
◼ 
CDI1.1 
依赖注入是一个开发企业应用时越来越流行的技术，CDI将其扩展到了应用服务器内部的各容
器，如EJB容器、Web容器，该规范可以使普通JavaBean、SessionBean和JSF Backing Bean通
过DI的方式在应用中使用，并且可以关联到一个特定范围，例如request范围、session范围
等。 
◼ 
JPA2.1 
JPA(Java Persistence API)是JavaEE 5和Java SE共有的有关对象持久化的接口，即对象持
久化。JPA在JavaEE7里得到了进一步的增强，使得JPA技术变得更加有效和可靠，对应用提供
了更有效的性能提升。 
◼ 
JCA1.7 
TongWeb中的JCA架构实现了JCA1.7规范，JCA(Java Connector Architecture) 提供了一个应
用服务器和企业信息系统(EIS)连接的标准Java解决方案，以及把这些系统整合起来的方法。
JCA简化了异构系统的集成，用户只要构造一个基于JCA规范的连接器应用，并将该连接器应
用部署到J2EE服务器上，这样不用编写任何代码就可以实现EIS与J2EE应用服务器的集成。 
◼ 
JSF2.2 
JSF是JavaEE 5规范中提出的关于Web层的开发框架，与其他Web框架不同的是JSF以用户界面
为核心，它将控制粒度细化到页面的“组件”一级，即JSF将各类页面元素抽象成UI(User 
Interface即用户界面)组件，这些UI组件可以灵活的组装生成页面，并被方便的定制和重用。
JSF使得开发人员摆脱了细碎的HTML代码和JavaScript脚本调试，可以应用面向对象的思想开
发Web应用程序。 JSF2.2进一步增强了对HTML5开发的支持。 


## 第 10 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
2 
◼ 
Bean Validation1.1 
数据验证是贯穿企业应用各处的一个公共任务，从表示层到持久层，每一层都需要数据验证，
Bean Validation避免了每一层重复的验证代码，提供了统一的注解和验证框架。 
⚫ 
JavaEE8 的主要增强 
Servlet4.0 
Servlet4.0是JavaEE8中重点改进的功能之一，Servlet 4.0支持服务器推技术。这种推送技术使
得Servlet规范与HTTP/2协议保持一致，是最直观的HTTP/2强化功能，使服务器能预测客户端请求
的资源需求。然后，在完成请求处理之前，服务器可以将这些资源发送到客户端。 
 
1.2 规范支持 
表 1.2-1：TongWeb7支持的规范 
类型 
支持内容 
组件 
JSP2.3 
Servlet4.0 
WebSocket1.0 
JSF2.2 
JSTL1.2  
EJB3.2 
EL3.0 
JCA1.7 
Debugging Support for Other Languages 1.0 
Common Annotations for the Java Platform 1.2 
JPA2.1 
Bean Validation 1.1 
CDI 1.1 
JMS 1.1 
Dependency Injection for Java 1.0 
资源和服务 
JTA1.2 
JDBC 4.0  
协议 
HTTP1.1  
RMI 
安全 
JAAS1.0 
 
1.3 体系结构 
TongWeb体系结构图如下： 


## 第 11 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
3 
 
图 1.3-1：TongWeb体系结构图 
应用服务器TongWeb采用微内核架构，在Java SE之上，由JMX服务、类加载服务、配置服务和生命周期
服务构成应用服务器的最小内核。在此微内核基础上，围绕着Web、EJB两大核心容器，构建Java EE基础服
务层和扩展服务层。 
⚫ 
基础服务层 
基础服务层包括JNDI、JDBC、JTA、JMS、JCA、JPA、JavaMail等服务，用于处理Java EE核心基础
资源对象的创建和生命周期管理，并对上层容器和扩展服务提供基础服务接口。 
⚫ 
扩展服务层 
扩展服务层基于微内核和基础服务之上，采用松散耦合的模式接入应用服务器框架，为上层服务
和两大核心容器提供企业级扩展服务，并提供容器组件和上层服务的聚合能力。其中资源适配服
务作为连接应用服务器和外部资源的关键服务，为应用服务器和第三方企业资源系统的对接和通
信，提供了通用模型，从而极大地提高了应用服务器和其他外部系统的互操作能力。 
⚫ 
两大核心容器 
Web容器和EJB容器提供Web应用和企业级应用部署运行所需的底层核心组件，如Servlet、JSP、
SessionBean组件等。同时还负责接收处理来自各种客户端的请求，如浏览器、终端以及各种语言
写的客户端。核心容器通过内部的连接通道和协议处理器，可以处理各种协议的客户端请求，如
HTTP、HTTPS、SOAP、AJP协议等等。 
⚫ 
管理服务 
为了便于用户更好的管理应用服务器内部资源以及部署运行在应用服务器上的企业应用，TongWeb
还提供了覆盖所有核心容器和服务的管理服务，用户可以通过管理服务对应用服务器内所有服务、


## 第 12 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
4 
资源和应用进行管理，同时管理服务还提供UI界面和命令行工具来进一步简化用户的操作，提供
更加良好的易用性。 
 
1.4 TongWeb特性 
⚫ 
遵循Java EE规范 
TongWeb7支持JavaEE 7规范中的特性，CDI1.1、EJB3.2、Servlet3.1、JPA2.1、JSF2.2和Bean 
Validation1.1等以及JavaEE8中的servlet4.0。 
⚫ 
高可靠性、高伸缩性、灵活扩展的集群 
TongWeb的集群采用集中式的缓存集群解决方案，提供极高的可靠性，不存在任何单点问题，同时
拥有很高的伸缩性；缓存集群可以在运行时支持动态扩展，为整个集群提供灵活的扩展性。 
⚫ 
基于JMX的管理机制 
JMX技术是Java关于应用和资源管理的标准技术，它为开发标准化、集中式的、安全的远程管理应
用提供了方案。TongWeb采用JMX作为管理框架的基础，清晰简洁。  
⚫ 
提供多种管理工具 
TongWeb提供三种管理工具，分别是管理控制台和第三方JMX工具JConsole，还有命令行。管理控
制台和命令行提供应用组件和资源的管理等功能，JConsole是基于JMX的GUI工具，提供JVM、MBeans
等信息。 
⚫ 
提供调优辅助工具 
TongWeb提供日志服务、快照服务、监视服务、链路追踪服务和APM工具，便于用户解决功能或者
性能的问题。 
1.5 应用开发工具 
提供Web应用、EJB应用和企业应用的开发工具，并能够部署到TongWeb7应用服务器上。  
⚫ 
管理控制台 
通过管理控制台用户可以方便进行各类型应用的管理，以及各种资源与服务的使用和调优。  
⚫ 
Web容器 
提供Web应用的运行环境，如支持HTTP协议，支持SSL协议上的HTTP协议(HTTPS)等。 
⚫ 
生命周期事件订阅层 
该层接受Web容器发来的生命周期事件，注册到该层的监听器收到事件后控制上层服务和容器的生
命周期。Web容器核心和上层服务及容器通过该层进行解耦，同时生命周期层还支持定制和扩展，
这种松散耦合的架构使得应用服务器可以灵活扩展新的功能。 
⚫ 
EJB容器 
提供JPA和EJB应用的运行环境。  
⚫ 
数据源 
提供JDBC数据源，用于管理数据库连接。  
⚫ 
命名服务 


## 第 13 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
5 
提供本地和远程的名字服务。  
⚫ 
配置管理 
可以管理各个容器和服务的配置信息，并支持实时配置变更。 
⚫ 
安全服务 
提供基于Java EE标准的安全服务。  
⚫ 
交易服务 
支持JTA1.2规范, 保证数据和业务逻辑的正确性和完整性。  
⚫ 
日志服务 
提供日志服务，用户可以对不同的模块设置不同的日志获取粒度，以达到根据需要选择性的获取
不同粒度的日志信息或关闭日志信息。  
⚫ 
部署服务 
提供应用部署功能的核心服务，可以部署各种类型应用，包括web应用，ejb应用，企业应用等。  
⚫ 
监视服务 
提供监视服务，用户可以控制监视量的采集，并能够获取服务器提供的监控量的值。 


## 第 14 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
6 
第2章 安装指南 
2.1 系统配置要求 
安装TongWeb7应用服务器最低系统要求见以下内容： 
表 2.1-1：TongWeb系统配置要求 
系统组件 
系统要求 
操作系统 
⚫ 
Windows平台： 
◼ 
Microsoft Windows系列 
⚫ 
Linux平台： 
◼ 
RedHat系列 
◼ 
Suse Linux系列 
◼ 
深度操作系统 
◼ 
银河麒麟操作系统 
◼ 
中标麒麟操作系统 
◼ 
统信操作系统 
⚫ 
UNIX平台： 
◼ 
Sun Microsystems Solaris系列 
◼ 
IBM AIX系列 
⚫ 
Mac OS平台： 
Mac OS 
Java环境 
JDK7u40及以上版本 
注意： 
⚫ 
JDK11的环境，请使用TongWeb免安装版本。 
⚫ 
支持 Oracle JDK，但部分 Oracle JDK 版本商用收费，在生产使用时请注意
商业授权，或采用 Open JDK、Tong JDK。 
⚫ 
若需要创建HTTPS通道，且SSL协议使用“TLS1.3”，JDK要求JDK1.8.0_261
及以上版本。 
⚫ 
当创建HTTPS通道，需要启动国密认证时，JDK要求JDK8及以上版本。 
当在JDK17环境下时，需要额外添加如下启动参数。 
⚫ 
--add-opens=java.base/sun.security.rsa=ALL-UNNAMED 
⚫ 
--add-opens=java.base/sun.security.util=ALL-UNNAMED 
⚫ 
--add-opens=java.base/sun.security.jca=ALL-UNNAMED 
物理内存 
512MB及以上 
硬盘空间 
可用空间500MB及以上 
监视器 
图形界面安装需要256色，字符界面安装没有色彩要求 
浏览器 
Microsoft IE11或Firefox3.0及以上版本浏览器 
 


## 第 15 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
7 
2.2 安装JDK环境 
安装TongWeb前需要先安装JDK环境以及配置环境变量。 
1. 在Java官网上下载JDK安装文件。 
2. 安装成功后，配置 JDK环境变量，使之生效。 
3. 在命令行界面，输入“java -version”。提示Java 版本，说明安装成功，如下图所示。 
 
图 2.2-1：JDK安装界面 
2.3 Windows平台界面安装 
本章节以国防版TongWeb7在Windows平台上安装作为示例，其他版本步骤相同。 
1. 
运行TongWeb7产品提供的Install_TW7.0.x.x_GuoFang_windows.exe，出现下图所示安装界面。 
说明：7.0.x.x表示TongWeb7.0下的所有版本 
 


## 第 16 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
8 
图 2.3-1：TongWeb安装界面 
2. 
选择安装界面语言（中文简体/English），点击OK，进入“简介”界面。 
 
图 2.3-2：TongWeb安装简介 
3. 
点击“下一步”，进入“许可协议”界面。 
 
图 2.3-3：许可协议 
4. 
选择“本人接受许可协议条款”后，点击“下一步”，进入“选择Java VM”界面。 


## 第 17 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
9 
 
图 2.3-4：选择Java虚拟机 
5. 
选择Java虚拟机，进入“选择安装文件夹”界面。 
 
图 2.3-5：选择安装路径 
6. 
选择安装文件夹后，点击“下一步”，进入“选择捷径文件夹”界面。 


## 第 18 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
10 
 
图 2.3-6：选择快捷产品图标 
7. 
选择是否创建快捷图标，点击“下一步”，进入“预安装摘要”界面。 
 
图 2.3-7：预安装界面 
8. 
查看并审核预安装摘要后，点击“安装”，进入安装界面。 


## 第 19 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
11 
 
图 2.3-8：开始安装界面 
9. 
安装滚动条完成后，进入端口设置界面，可以修改http-listener、jmx-service、 shutdown-port
端口号。如下图所示，当前界面显示为默认端口。 
 
图 2.3-9：端口设置界面 
10. 设置端口后，点击“下一步”，进入安装完成界面。 


## 第 20 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
12 
 
图 2.3-10：安装完成界面 
11. 出现了成功安装的提示信息后，表示安装成功。点击“完成”退出安装程序。 
 
2.4 Linux平台命令行安装 
如果Linux平台提供图形界面安装，直接执行安装程序：sh Install_TW7.0.*.*_*_Linux.bin，安装过
程和Windows平台一致。 
如果没有开启图形界面功能，需要通过命令行安装。本章节以国防版TongWeb7在Linux平台上用命令行，
并选用英文安装作为示例，其他版本步骤相同。 
注：无论界面或命令行，如果想使用中文安装，都需要设置Linux平台编码LANG为zh_CN.UTF-8。 
1. 
以root用户运行sh Install_TW7.0.x.x_GuoFang_Linux.bin -i console，并选择安装语言。 
说明：7.0.x.x表示TongWeb7.0下的所有版本 
[root@ Machine04]# sh Install_TW7.0.x.x_GuoFang_Linux.bin -i console 
Preparing to install... 
Extracting the installation resources from the installer archive... 
Configuring the installer for this system's environment... 
 
Launching installer... 
 
Preparing CONSOLE Mode Installation... 
 


## 第 21 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
13 
================================================================ 
Choose Locale... 
---------------- 
 
  ->1- English 
    2- 中文简体 
 
CHOOSE LOCALE BY NUMBER: 1 
2. 
出现如下授权信息后，按回车键继续安装。 
======================================================== 
TongWeb7.0 GuoFang                       (created with InstallAnywhere) 
--------------------------------------------------------------------------- 
Preparing CONSOLE Mode Installation... 
 
======================================================== 
License Agreement 
----------------- 
 
Installation and Use of TongWeb7.0 GuoFang Requires Acceptance of theFollowing License 
Agreement: 
 
End User License Agreement (EULA) 
 
Copyright (c)2025 Beijing Tongtech co., Ltd. or its affiliates (hereinafterreferred to as "Tongtech"). 
All rights reserved. 
 
This End User License Agreement ("Agreement") applies to the software productand related 
documentation provided by Tongtech (“Software").Please read this Agreement carefully before 
installing or using the Software.By using the Software, you acknowledge that you accept all terms 
of thisAgreement.If you do not agree to the terms of this Agreement, you are not authorized toinstall 
or use the Software. 
Article 1-Definitions 
 
Unless the context indicates otherwise, the following terms have the meaningsset forth below: 
1. “ Software": refers to the software product provided by Tongtech, includingassociated 
documentation, data, and other materials. 
2,“User" or “You": refers to the individual or legal entity that obtains alicense to use the Software. 


## 第 22 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
14 
3.“License": refers to the limited, non-exclusive, non-transferable rightgranted by Tongtech to use 
the Software under this Agreement. 
4.“Device": refers to the computer or other terminal legally owned or 
 
PRESS <ENTER> TO CONTINUE: 
3. 
出现如下信息后，按回车键继续安装。 
3. Copy or transfer this software in whole or in part. 
 
When you transfer this software in part or in whole to any third part, your right to use the software 
shall terminate immediately without notice. 
 
The copyright and ownership of this software: 
The copyright of this software is owned by Tongtech co., LTD. The structures, tissues and codes are 
the most valuable commercial secrets of Tongtech co., LTD. This software and documents are 
protected by national copyright laws and international treaty provisions. You are not allowed to 
delete the copyright notice from this software. You must agree to prohibit any kind of illegal copy of 
this software and documents. 
 
Limited warranty: 
In the largest permitting area of the law, in no situation shall Tongtech co., LTD be liable for any 
special, unexpected, direct or indirect damages (including, without limitation, damages for loss of 
business profits, business interruption, loss of business information, or any other pecuniary loss) 
arising out of the use of or inability to use this product and the providing or inability to provide 
supporting services, even if Tongtech co., LTD has been advised of the possibility of such damages. 
 
PRESS <ENTER> TO CONTINUE: 
4. 
请选择是否接受许可条款，若接受请输入“Y”。 
Termination: 
Tongtech co., LTD may terminate the license at any time if you violate any term or condition of the 
license. When the license is terminated, you must destroy all copies of the software and all of its 
documents immediately, or return them to Tongtech co., LTD. 
 
Law: 
"COPYRIGHT LAW OF THE PEOPLE'S REPUBLIC OF CHINA", "Trademark Law of the 
People's Republic of China", "Patent Law of the People's Republic of China","Berne Conventionon 
the Protection of Literary and Artistic Works" 
 


## 第 23 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
15 
Now, you must have already carefully read and understand this license, and agree to obey all the 
terms and conditions strictly. 
 
DO YOU ACCEPT THE TERMS OF THIS LICENSE AGREEMENT? (Y/N): Y 
5. 
进入选择Java VM，默认为当前系统正在使用Java VM。 
=============================================================== 
Choose Java Virtual Machine 
--------------------------- 
Please Choose a Java VM for Use by the Installed Application 
->1- /usr/java/jdk1.8.0_144/bin/java   //当前系统正使用的JDK 
2- /usr/bin/java  
3- Choose a Java VM already installed on this system   //使用其它JDK 
ENTER THE NUMBER FOR THE JAVA VM, OR PRESS <ENTER> TO ACCEPT THE 
CURRENT SELECTION: 3  
ENTER THE ABSOLUTE PATH TO THE JAVA VM EXECUTABLE OF YOUR CHOICE: 
/home/tong/jdk/jdk1.7.0_67/bin/java 
PATH TO THE JAVA EXECUTABLE IS: 
/home/tong/jdk/jdk1.7.0_67/bin/java 
IS THIS CORRECT? (Y/N): Y 
6. 
按回车键进入安装路径设置。输入安装路径（注：目录不能带中文），若同意使用给出的默认安
装路径，请按回车键继续安装。 
=============================================================== 
Choose Install Folder 
--------------------- 
Where would you like to install? 
 
Default Install Folder: /root/TongWeb7.0 
 
ENTER AN ABSOLUTE PATH, OR PRESS <ENTER> TO ACCEPT THE DEFAULT: 
7. 
出现如下信息后，请输入链接选项，选择后，按回车键继续安装。 
================================================================ 
Choose Link Location 
-------------------- 
Where would you like to create links? 
 
  ->1- Default: /root 


## 第 24 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
16 
    2- In your home folder 
    3- Choose another location... 
    4- Don't create links 
 
ENTER THE NUMBER OF AN OPTION ABOVE, OR PRESS <ENTER> TO ACCEPT THE 
DEFAULT： 
8. 
确认预安装信息是否正确，若正确按回车键继续安装。 
=============================================================== 
Pre-Installation Summary 
------------------------ 
Please Review the Following Before Continuing: 
  
Product Name: 
    TongWeb7 GuoFang 
  
Install Folder: 
    /root/TongWeb7.0 
 
Link Folder: 
    /root 
 
Disk Space Information (for Installation Target):  
    Required:  107,191,640 bytes 
    Available: 230,416,384 bytes 
PRESS <ENTER> TO CONTINUE: 
9. 
安装完成后，进入端口修改界面，缺省值为默认端口。 
=============================================================== 
Installing... 
------------- 
[==================|==================|=====================] 
[------------------|------------------|------------------|----------------] 
=============================================================== 
Set Ports 
--------- 
tong-http-listener (DEFAULT: 8088): 8089 
system-http-listener (DEFAULT: 9060): 9061 
ejb-server-listener (DEFAULT:5100): 5100 


## 第 25 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
17 
jmx-service (DEFAULT:7200): 7201 
shutdown-port (DEFAULT:7090): 7090 
10. 输入端口后，按回车键结束安装。 
Installation Complete 
--------------------- 
 
Congratulations. TongWeb7 has been successfully installed to: 
 
   /root/TongWeb7.0 
 
PRESS <ENTER> TO EXIT THE INSTALLER: 
 
2.5 Linux平台静默安装 
如果想要在Linux平台上静默安装TongWeb （即安装时无提示也无需操作），需要制作一个
install.properties的属性配置文件，将该配置文件放到安装程序同级目录下。  
[root@machine01]# more install.properties 
INSTALL_UI=silent 
USER_INSTALL_DIR=/root/TongWeb7.0/ 
SILENT_JDK_HOME=/home/jdk/jdk1.8.0_144/ 
USER_INPUT_PORTS_RESULTS= "8081","9061","5101","7201","7090" 
⚫ 
INSTALL_UI：安装模式，此处介绍的是silent模式 
⚫ 
USER_INSTALL_DIR：TongWeb的安装路径（注：目录不要带中文） 
⚫ 
SILENT_JDK_HOME：设置JDK路径，该jdk路径优先。 
⚫ 
USER_INPUT_PORTS_RESULTS：TongWeb端口配置。 
格式为：USER_INPUT_PORTS_RESULTS=  
"tong-http-listener"," 
system-http-listener","ejb-server-listener","jmx-service","shutdown-port " 
运行以下命令即可完成安装：（以root用户运行，安装时无提示也无需操作） 
sh Install_TW7.0.*.*_GuoFang.bin -i silent -f install.properties 
执行完脚本以后，可以看到按照install.properties的设置，生成了一个新的TongWeb安装目录，比如
示例里的/root/TongWeb7.0/。 
 


## 第 26 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
18 
2.6 安装License 
您需要安装 License 后，才能启动 TongWeb，可选择“本地授权”或者“服务授权”。 
⚫ 
本地授权：通过提供的 license.dat 文件进行本地授权。 
⚫ 
服务授权：通过 License Server 服务，进行服务授权。 
操作步骤如下所示。 
⚫ 
方式一：本地授权 
购买TongWeb产品后，在TongWeb7品光盘中提供有license文件。将license.dat文件复制到安装完
成的TongWeb根目录下“${TongWeb_Home}”。 
登录管理控制台，在“首页”页面，即可查看License信息中“授权方式”为“本地授权”。 
 
 
⚫ 
方式二：服务授权 
通过 License Server 服务进行服务授权。当用户使用服务授权时，可选择“远程模式”或者“激
活模式”。 
◼ 远程模式：调用远程授权管理平台License Server，加载授权证书，校验授权证书内容。 
◼ 激活模式：既支持从本地读取license.dat文件，也支持从License Server平台加载授权证书进行
授权认证。 
激活模式的工作流程，如下所示。 
1. 
当本地不存在，则去远程校验，顺带下载到 “${TongWeb_HOME}/active”目录。 
2. 
当本地存在，则校验本地，定期尝试去做远程校验从而激活，没有激活最多存活365天。 
3. 
只要远程校验通过了，后面的周期校验都是走远程校验，而且顺带下载。 
4. 
当网络不通，则走“${TongWeb_HOME}/active”目录的本地文件。 
5. 
当网络不通，要重启，则走“${TongWeb_HOME}/active”目录的本地文件做校验重启，
此时走条件2。 
 
前置条件 
⚫ 
已搭建License Server服务。 
⚫ 
已申请硬件码并提供给东方通销售/售后。 
⚫ 
已将从东方通销售/售后人员获取的license.dat上传到License Server服务。 
⚫ 
已获取License Server服务的IP和端口。 
 


## 第 27 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
19 
操作步骤 
1. 
进入TongWeb安装目录“${TongWeb_Home}/bin”目录。 
2. 
打开“external.vmoptions”文件，并在“#server_options”下加入如下参数。 
➢ 
远程模式 
-Dserver.tongweb.license.type=remote 
-Dserver.tongweb.license.license-ips=IP:Port 
-Dserver.tongweb.license.publicKey=License Server 密钥 
说明： 
✓ 
remote：表示远程模式。 
✓ 
IP:Port：表示License Server服务的IP地址的端口号；默认端口为“8888”。 
✓ 
License Server 密钥：需要从 License Server 控制台获取。 
请将IP和Port替换为您的License Server服务的实际IP和端口。 
若有多个IP地址，则使用英文逗号进行分隔，如下所示。 
-Dserver.tongweb.license.license-ips=192.168.22.182:8888, 192.168.22.183:8888 
 
➢ 
方式二：激活模式 
-Dserver.tongweb.license.type=active 
-Dserver.tongweb.license.license-ips=IP:Port 
-Dserver.tongweb.license.publicKey=License Server 秘钥 
说明： 
✓ 
active：表示激活模式。 
✓ 
IP:Port 和 License Server 秘钥：配置说明请参见方式一：远程模式。 
3. 
配置完成后，保存并退出。 
登录管理控制台，在“首页”页面，即可查看License信息中“授权方式”为服务授权。 
 
2.7 目录说明 
TongWeb应用服务器安装后目录名称及说明。 
 
表 2.7-1：TongWeb目录结构 
一级目录 
二级目录 
说明 
Agent 
- 
代理服务器注册节点（仅企业版提供）。 


## 第 28 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
20 
一级目录 
二级目录 
说明 
bin 
代理服务器脚本。 
config 
代理服务器配置。 
logs 
代理服务器日志。 
nodes 
通过代理服务器创建的TongWeb节点。 
file 
代理服务器接收集中管理工具分发的文件。 
service 
代理服务器启动配置模版。 
temp 
临时文件目录。 
applications 
- 
系统应用所在目录。 
console 
服务器自带的控制台管理工具。 
genericra 
服务器自带的内部应用。 
heimdall 
服务器自带的集中管理工具。 
sysweb 
服务器自带的内部应用。 
autodeploy  
- 
服务器默认提供的自动部署监听目录。 
bin  
- 
服务器启动，停止等脚本文件所在目录。 
conf 
- 
服务器的配置文件所在目录。 
h3 
服务器HTTP3默认证书。 
schema 
服务器配置文件结构描述文件。 
security 
服务器默认安全域、内部密钥。 
deployment 
- 
已部署应用的应用程序目录 
domain_template 
- 
域服务器模板 
doc 
- 
用户手册目录 
lib  
- 
服务器运行所需的类文件所在目录，主要以Jar文件形
式存在。 
agent 
代理服务器运行所需jar文件。 
apm 
服务器应用性能监控工具依赖包。 
bc 
服务器自带的默认bcprov.jar。 
cdi-integration 
服务器CDI实现。 
classes 
服务器拓展公共类文件目录。 
client 
服务器EJB客户端依赖包。 
common 
服务器拓展jar包目录。 
endorsed 
服务器Java endorsed目录。 
flowcontrol 
服务器flowcontrol依赖包目录。 
hotswap-classes 
服务器类热加载目录。 
php 
服务器支持PHP依赖包目录。 
license_update 
- 
动态更新license目录。 
logs 
- 
服务器存放日志文件的目录，日志文件包括访问日志文
件和服务器日志文件等。 
audit-log 
控制台审计日志。 
command-audit-log 
命令行审计日志。 
heimdall-audit-log 
集中管理工具审计日志。 
startStopCommand-
TongWeb启停审计日志。 


## 第 29 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
21 
一级目录 
二级目录 
说明 
audit-log 
masterConfigBAK 
- 
tongweb作为集中管理工具，master节点的备份目录。 
注意： 
创建集群后，自动生成该目录。 
native 
- 
Apr native在不同平台所需要的库文件。 
persistence 
- 
存放各类监视量的持久化文件。 
注：启动监控后产生该目录。 
samples 
- 
应用服务器的示例目录，示例包括EJB、WEB等模块。 
service 
- 
自启动服务器目录。 
bin 
自启服务安装程序。 
conf 
自启服务安装程序配置文件。 
lib 
自启服务安装程序依赖包。 
linux 
自启服务linux模版。 
log 
自启服务安装程序日志。 
snapshot 
- 
存放服务器生成的快照文件 
注：创建快照后产生该目录 
temp 
- 
服务器产生的临时文件以及应用预编译文件所在的目
录。 
TongDataGrid 
- 
分布式缓存目录（仅企业版提供） 
bin 
分布式缓存启停脚本及相关配置文件。 
lib 
分布式缓存依赖jar包。 
tongweb-mq 
- 
tongweb-mq所在目录。 
tools 
- 
应用服务器所带的工具目录。 
appclient 
EJB客户端工具。 
eclipse-plugins 
服务器自带的eclipse插件。 
idea-plugins 
服务器自带的idea插件。 
lite-generator 
服务器轻量版生成工具。 
patch-7.0 
服务器补丁工具。 
pinpoint-plugins-* 
服务器自带的个版本pinpoint插件。 
TW-toolkit 
服务器Web应用迁移工具。 
tongWebList.yaml 
- 
集群模式下启动补丁工具后自动生成。记录当前有多少
tongweb实例存活。 
tongweb.pid 
- 
tongweb启动后的进程号记录文件 
Uninstall_TongWeb7.0 
- 
卸载TongWeb脚本目录 
 
2.8 查看安装信息 
为了帮助您进行系统维护、管理软件许可、进行故障排除等任务，TongWeb 提供了查看其安装信息的
功能。 


## 第 30 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
22 
前置条件 
已安装TongWeb。 
操作步骤 
1. 
进入 TongWeb 安装目录“${TongWeb_HOME}/bin”。 
2. 
运行“version.[bat|sh]”脚本，即可查看TongWeb 的版本信息、构建时间、安装时间以及 License 信
息等。 
 
说明： 
⚫ 
如上截图呈现的是临时license 的相关信息。 
⚫ 
若为永久license，在启动TongWeb 后，系统会自动将该license 与127.0.0.1 对应的mac 地址
进行绑定。License 信息将显示绑定的mac 地址信息（即bindmac 参数）。 
对于创建时间（create_time）小于90 天的永久license，用户可自由拷贝，且拷贝后的license
均能正常完成激活与绑定操作。 
记录安装时间说明 
⚫ 
记录安装时间优先级：Uninstall_TongWeb7.0\installvariables.properties 中记录时间 > tongweb.pid 创
建时间 > 根目录创建时间。 
⚫ 
在Linux 系统中，部分文件系统不支持记录文件的创建时间，读取的时间可能不准确。然而，一旦
TongWeb 启动，它将与系统时间进行同步，以此来保证时间记录的准确性。 


## 第 31 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
23 
第3章 启动及停止 
3.1 启动服务器 
3.1.1 Windows上启动服务器 
⚫ 
快捷方式启动   
TongWeb在安装过程中提供有多种快捷方式，通过选择快捷方式启动应用服务器。 
例如：开始->所有程序->TongWeb7->Start TongWeb7 
⚫ 
通过命令行启动 
在${TongWeb_HOME}/bin目录下运行startserver.bat可启动应用服务器。 
3.1.2 Linux平台上启动服务器 
⚫ 
在${TongWeb_HOME}/bin目录下运行startserver.sh可启动TongWeb。 
⚫ 
也可以在${TongWeb_HOME}/bin目录下运行startservernohup.sh，以后台运行的方式启动
TongWeb。 
查看日志：tail -f ${TongWeb_HOME}/logs/server.logs 
⚫ 
也可以在${TongWeb_HOME}/bin目录下运行nohup ./startserver.sh &，以后台运行的方式启动
TongWeb。 
查看日志：tail -f ${TongWeb_HOME}/bin/nohup.out 
3.1.3 安全停止 
安全停止功能可以防止通过停止脚本，非法停止应用服务器。 
开启该功能需要在${TongWeb_HOME}/bin/external.vmoptions脚本中修改： 
-Dstartup.secure=false改成-Dstartup.secure=true 
注意： 
如果脚本中没有-Dstartup.secure参数，需要添加该参数。 
此时，通过${TongWeb_HOME}/bin/stopserver来停止TongWeb应用服务器时，需要在调用停止脚本时输
入登录用户认证信息，用户名、密码同管理控制台用户名、密码一样。 
 
3.2 启动时记录TongWeb进程号 
为在HA场景下正确显示TongWeb进程状态，需要生成进程文件。可在启动脚本startserver.sh里把
tongweb_pid的值改成true即可（默认=false）。启动成功后，就会生成一个进程文件tongweb.pid，文件


## 第 32 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
24 
内容是TongWeb的进程号。 
tongweb_pid=true 
if [ $tongweb_pid = true ]; then 
    TONGWEB_PID=${TongWeb_Base}/tongweb.pid 
fi 
 
3.3 管理控制台 
TongWeb管理控制台是应用服务器提供的图形管理工具，它允许系统管理员以Web方式管理系统服务、
应用程序、监控系统信息等。 
3.3.1 登录 
在浏览器中输入http://<IP>:9060/console，其中<IP>表示TongWeb主机IP地址，9060为TongWeb管理
控制台默认监听端口。TongWeb安装在本机时，也可以通过http://localhost:9060/console登录管理控制
台。 
访问成功后出现以下登陆页面。默认系统管理员用户名及初始密码为：thanos/thanos123.com。系统
默认的用户名不可以修改或删除，但是可以在defaultRealm安全域的用户管理中添加用户及修改密码。 
 
图 3.3-1：管理控制台登录页面 
注意： 
⚫ 
默认情况下，用户连续认证失败 5 次后，账户将被锁定。 
⚫ 
默认情况下，当控制台会话持续超时达 30 分钟，账号将自动退出登录。 
 
用户首次登录集中管理控制台时会被提示要求修改初始密码，如下图所示。 


## 第 33 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
25 
 
图 3.3-2：首次登录管理控制台修改密码提示 
修改初始密码如下图所示，密码必须由大写字母、小写字母、数字、特殊字符4种组成，长度不得少于
10位。 
注意： 
⚫ 
新密码不能和初始密码一致。 
⚫ 
要求5次以内密码不能重复。 
 
图 3.3-3：首次登录修改密码设置 


## 第 34 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
26 
如果管理控制台已被某用户登录，使用该用户登陆时会出现如下提示信息: 
 
图 3.3-4：管理控制台登录冲突 
登录管理控制台后，TongWeb默认进入首页相关信息。此页用于显示TongWeb安装信息、JDK信息及
License信息，并提供TongWeb配置资源TongWeb.xml和external.vmoptions的下载,服务器选择文件可选目
录。左侧导航树上展示了管理控制台提供的所有功能，如下图所示。 
注意： 
设置服务器选择文件可选目录:首次登录不提供修改功能，用到需要选择文件的组件，页面会给出提示，
需要自己手动去单机控制台首页、设置服务器选择文件可选目录；目录的设置要求输入绝对路径， 
windows不允许设置为系统盘根目录、不允许为系统盘的Windows目录；linux不允许设置为"/"、
"/root"、"/etc"。 


## 第 35 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
27 
 
图 3.3-5：管理控制台首页 
 
3.3.2 注销 
TongWeb管理控制台中提供用户退出登录的功能，在管理控制台右上角用户名下，选择“退出登录”按
钮，便可退出当前用户的登录。  
 
3.4 宕机重启模式 
宕机重启模式：TongWeb运行中因为出错宕机（进程异常退出）时，可以自动重新启动。 
以宕机重启模式运行的TongWeb共有两个java进程：主进程（TongWeb重启监控进程）和子进程（TongWeb
应用服务器进程）。主进程只能监控同目录下启动的TongWeb子进程。 


## 第 36 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
28 
3.4.1 宕机重启使用场景 
只有服务器子进程发生异常宕机时，监控主进程才会重启TongWeb应用服务器。 
⚫ 
异常宕机 
1） Kill -9 子进程id：认为是TongWeb服务器异常宕机，重启应用服务器； 
2） Kill -2 子进程id：认为是TongWeb服务器异常宕机，重启应用服务器； 
3） Kill -15 子进程id：认为是TongWeb服务器异常宕机，重启应用服务器； 
4） 其它方式：可以通过监控主进程的监控日志或控制台日志，看到应用服务器子进程是如何退出
的。退出码为0的是正常退出，其他都属于异常退出。例如下图中，应用服务器子进程因为异
常退出（退出码137）而重启了。 
 
⚫ 
不属于异常宕机: 
1） 通过${TongWeb_HOME}/bin的stopserver.bat（stopserver.sh）正常停止服务。 
2） ctrl+c：停止重启监控主进程，这会导致同时停止监控主进程和应用服务器子进程。 
注意： 
通过操作系统查看进程命令可查看字符串 
com.tongweb.launcher.monitor.LauncherMonitor 
3） kill -3 子进程PID：输出子进程的jvm堆栈信息，输入到server.log日志中。TongWeb子进程
不会宕机。 
4） kill -3 主进程PID：输出主进程的jvm堆栈信息，服务器主进程不会宕机。 
3.4.2 宕机重启模式用法 
运行命令 
Windows： startserver.bat restart 
Linux：   startserver.sh restart 
宕机重启参数说明 
发生宕机时，重新启动有一个时间间隔，这个时间间隔可以在TW_HOME/bin 目录下的 
external.vmoptions文件中进行设置。 
-Dtongweb.restart.interval=1：设置宕机后重启的时间间隔，以秒为单位。如果不设置这个参数，
默认为1秒。 
内存溢出重启参数说明 
在Linux系统下会提供监测内存溢出以及HTTP通道线程挂起数功能。如扫描日志文件发现有内存溢出
时，就用jmap生成内存转储文件；发现线程挂起数超过配置值，则输出堆栈信息。文件存储路径为


## 第 37 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
29 
${TongWeb_HOME}/snapshot/restart，同时根据配置决定是否重启服务器。可在启动脚本中通过增加如下
参数配置： 
⚫ 
-Dmonitor.abnormal.restart=false: 设置服务器非正常状态时是否重启，如果不设置这个参数或
者参数值不为true，表示不重启，默认为false。 
⚫ 
-Dmonitor.interval=10: 设置监测时间间隔，以秒为单位。如果不设置这个参数，默认为10秒。 
⚫ 
-Dmonitor.hang.max=0: 设置允许的最大挂起线程数，如果不设置这个参数，默认为-1,表示不监
测线程挂起数。设置为0表示，只要发现有一个挂起则输出堆栈。 
⚫ 
-Dmonitor.hang.name=tong-http-listener: 设置监测某个HTTP通道名称下的线程挂起数，如果不
设置这个参数，默认为空，表示监测所有的HTTP通道线程挂起数。 
 
3.5 停止服务器 
3.5.1 Windows上停止服务器 
TongWeb提供几种方式停止服务器，分别是使用Ctrl+C强行停止服务器、通过停止脚本停止服务器。 
⚫ 
使用Ctrl+C停止 
在TongWeb的运行窗口直接按下Ctrl+C，即可终止TongWeb的运行。 
⚫ 
通过停止脚本停止 
在${TongWeb_HOME}/bin目录下运行stopserver.bat以停止TongWeb。 
在${TongWeb_HOME}/bin目录下运行forcestopserver.bat，强制停止TongWeb，当进程无法完全停
止时，通过该命令强行停止。 
3.5.2 Unix/Linux上停止服务器 
⚫ 
使用Ctrl+C停止： 
在TongWeb的运行窗口直接按下Ctrl+C，即可终止TongWeb的运行。 
⚫ 
通过停止脚本停止： 
◼ 
在${TongWeb_HOME}/bin目录下运行stopserver.sh以停止TongWeb。 
◼ 
在${TongWeb_HOME}/bin目录下运行stopserver.sh quick以快速停止TongWeb。 
◼ 
在${TongWeb_HOME}/bin目录下运行stopserver.sh quick 20，设置快速停止TongWeb的超时
时间，在设置的超时时间（20s）内快速停止TongWeb。 
◼ 
在${TongWeb_HOME}/bin目录下运行forcestopserver.sh，强制停止TongWeb，当进程无法完
全停止时，通过该命令强行停止。 


## 第 38 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
30 
第4章 卸载TongWeb 
4.1 Windows平台上卸载 
1. 通过选择快捷方式卸载TongWeb应用服务器。例如：开始->所有程序->TongWeb7-> Uninstall 
TongWeb7。执行卸载程序后，出现如下“卸载界面”。 
 
图 4.1-1：Windows卸载界面 
2. 确认卸载，卸载完成后，出现 “卸载完毕”界面。 
 
图 4.1-2：Windows卸载界面 


## 第 39 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
31 
3. 确认信息后，点击“完成”退出卸载程序。 
注意： 
如果文件在使用过程中被修改或者有新生成的文件夹，则卸载时会认为无法删除。 
 
4.2 Linux平台上卸载 
⚫ 
免安装版本：直接删除安装目录。 
⚫ 
安装程序版本：运行${TongWeb_HOME}/Uninstall_TongWeb7.0目录下的Uninstall_TongWeb7.0 
root@machine01 Uninstall_TongWeb7.0]# ./Uninstall_TongWeb7.0 
========================================================= 
TongWeb7.0 GuoFang                      (created with InstallAnywhere) 
---------------------------------------------------------------------------- 
Preparing CONSOLE Mode Uninstallation... 
========================================================= 
Uninstall TongWeb7.0 
-------------------- 
About to uninstall... 
 
TongWeb7.0 
 
This will remove features installed by InstallAnywhere. It will not remove files and folders created 
after the installation. 
 
PRESS <ENTER> TO CONTINUE: 
 
========================================================= 
Uninstalling... 
--------------- 
...* 
* 
************************* 
************************* 
************************* 
************************ 
========================================================= 
Uninstall Complete 


## 第 40 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
32 
------------------ 
Uninstall Complete 
 


## 第 41 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
33 
第5章 TongWeb域 
5.1 概述 
TongWeb域功能，其定义为逻辑服务器管理。通过安装介质首次安装的服务器为物理服务器。通过物理
服务器的域功能，可创建出多个逻辑服务器。这些逻辑服务器各自的配置信息、日志文件等私有属性，保
存在与其对应的各个域中。目前定义为一个域只管理一个逻辑服务器，逻辑服务器依赖的公有属性（如lib
文件、license文件、系统应用、Agent、tongweb-mq、TongDataGrid、samples等）都引自物理服务器（注：
域中不含这些物理文件）。基于域功能，只需要安装一份物理TongWeb，就可以创建多个TognWeb域服务器。 
域管理的逻辑服务器在功能上和物理服务器相比，裁剪掉了集中管理工具（heimdall），其它的功能
完全一致。 
5.2 创建TongWeb域 
物理TongWeb提供创建域的脚本，创建时需要指定一个名字，创建后在物理${TongWeb_HOME}/domains
目录下会生成一个以该名字命名的目录。该目录就是一个逻辑TongWeb服务器，这种域成为“相对域”。创
建时也可以指定一个绝对路径用以保存域文件，这种域称为“绝对域”。 
“相对域”在物理TongWeb路径变化后不用任何修改仍可使用，“绝对域”在物理TongWeb路径变化后，
需手动更新其相关脚本为新的物理TongWeb路径。 
以Linux 平台为例，创建名称为“tw_domain_1” 的相对域，在${TongWeb_HOME}/bin 目录下运
行./domain.sh create tw_domain_1。 
若要创建绝对路径为/opt/tw_domain_1的绝对域，则运行： 
./domain.sh create /opt/tw_domain_1。 
创建域过程中，可以给创建的域指定端口，以空格分隔开各项参数，参数顺序不固定，并且可选部分
端口设置或者不设置，不设置时仍是端口自增。格式如下： 
./domain.sh create /opt/tw_domain_1 managePort=9066 appPort=8888 ejbPort=5102 jmxPort=7210 
shutdownPort=7050 
说明： 
⚫ 
managePort为控制台管理端口 
⚫ 
appPort为应用访问端口 
⚫ 
ejbPort为远程ejb访问端口 
⚫ 
jmxPort为jmx端口 
⚫ 
shutdownPort为停止时调用的端口 
当前版本停止端口默认和jmx端口共用7200。 
当将7200端口的jmx协议由“rmi”改为“mp”协议，或者关闭JMX的7200端口，则JMX启用7090。 
◼ 
将“rmi”改为“mp”协议。 
<jmx-service port="7200" address="127.0.0.1" protocol="mp"/> 
◼ 
JMX关闭7200。 


## 第 42 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
34 
<jmx-service port="7200" address="127.0.0.1" enabled="false"> 
5.3 删除TongWeb域 
物理TongWeb 提供删除域的脚本，删除“ 相对域” 时候需要指定域的名字（即物理
${TongWeb_HOME}/domains下的文件夹名称）即可，删除“绝对域”则需要指定其绝对路径。 
以Linux 平台为例，删除名称为“tw_domain_1” 的相对域，在${TongWeb_HOME}/bin 目录下运
行./domain.sh delete tw_domain_1。 
若要删除绝对路径为/opt/tw_domain_1的绝对域，则运行： 
./domain.sh delete /opt/tw_domain_1。 
5.4 启动TongWeb域 
物理TongWeb提供启动域的脚本，启动“相对域”时候需要指定域的名字，启动“绝对域”则需要指定
其绝对路径。同时域本身的bin目录下也提供了其启动脚本，可直接使用，使用时不需要指定任何名字或路
径。 
以Linux平台为例，要启动名称为“tw_domain_1”的相对域，在${TongWeb_HOME}/bin目录下运
行./startdomain.sh tw_domain_1， 
若要启动绝对路径为/opt/tw_domain_1的绝对域，则运行： 
./startdomain.sh /opt/tw_domain_1。 
当然，也可以在逻辑TongWeb的bin目录下运行./startserver.sh启动该服务器。 
5.5 停止TongWeb域 
物理TongWeb提供停止域的脚本，停止“相对域”时候需要指定域的名字，停止“绝对域”则需要指定
其绝对路径，同时域本身的bin目录下也提供了停止动脚本，可直接使用，使用时不需要指定任何名字或路
径。 
以Linux平台为例，要停止名称为“tw_domain_1”的相对域，在${TongWeb_HOME}/bin目录下运
行./stopdomain.sh tw_domain_1。 
若要停止绝对路径为/opt/tw_domain_1的绝对域，则运行： 
./stopdomain.sh /opt/tw_domain_1。 
当然，也可以在逻辑TongWeb的bin目录下运行./stopserver.sh停止该服务器。 
5.6 注意事项 
由于新创建出来的域，运行TongWeb实例依赖物理TongWeb，所以域的位置必需和物理TongWeb必需处于
同一文件系统中。且对于绝对路径创建的域，若后期物理TongWeb路径发生了变化，必需手动修改域的启动
脚本，指向新的物理TongWeb。 
 
 


## 第 43 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
35 
第6章 常见问题 
本章节主要讲解如何处理启动异常的故障。 
6.1 TongWeb启动失败 
TongWeb无法启动或启动失败有以下几种情况，相应的故障现象及解决方法如下。（适用于TongWeb所
有版本） 
1. 故障现象： 
启动日志错误，具体的代码如下。 
JAVA_HOME was not setted. 
JAVA_HOME directory is wrong 
 
故障原因： 
没有安装JDK或没有设置正确的JAVA_HOME环境变量。 
解决方法： 
检查JAVA_HOME环境变量是否正确。 
 
2. 故障现象： 
启动日志错误，具体的代码如下。 
Error occurred during initialization of VM 
Could not reserve enough space for object heap 
 
故障原因： 
JVM内存设置过大没有足够可用内存。 
解决方法： 
JVM内存设置要合理。 
 
3. 故障现象： 
启动日志错误具体的代码如下。 
[INFO] [System.out] [License expired.] 或 
[INFO] [System.out] [License is not for this version of product.] 
 
故障原因： 
license过期或不合法。 
解决方法： 
重新获取合法的license。 
 
4. 故障现象： 
启动日志错误，具体的代码如下。 


## 第 44 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
36 
[2016-06-12 09:51:15] [SEVERE] [admin] [openRemote JMX Port error.] 
java.net.BindException: Address already in use: JVM_Bind 
      at java.net.TwoStacksPlainSocketImpl.socketBind(Native Method) 
 
故障原因： 
TongWeb相关端口被占用。 
解决方法： 
停止占用TongWeb端口的进程。 
 
5. 故障现象： 
在Unix/Linux平台下，以普通用户安装启动的TongWeb，但后来又以root用户启动过，再切回普通用户
时，TongWeb无法启动。 
故障原因： 
TongWeb或应用文件权限被更改。 
解决方法： 
通过chown命令更改TongWeb整个目录文件属主。 
 
6. 故障现象： 
TongWeb启动脚本报出了格式错误，造成启动失败。 
故障原因： 
由于启动批处理或shell脚本格式修改错误。 
解决方法： 
为防止startserver、external.vmoptions改错，可以使用图形界面进行修改。启动TongWeb，登录管
理控制台，进入启动参数配置页面，即可重新指定JVM参数、服务器参数和环境变量JAVA_HOME。 
 
7. 故障现象： 
在Linux平台下通过SSH登录，以./startserver.sh方式启动TongWeb，当SSH断开后TongWeb自动停止，
使启动失败。 
故障原因： 
通过SSH登录Linux系统，当SSH断开以后，控制进程收到SIGHUP信号退出，会导致该会话期内其他进程
退出，这样通过startserver.sh启动的TongWeb进程也会退出。 
解决方法： 
在Unix/Linux下用nohup命令启动，该命令可以在退出帐户/关闭终端之后继续运行相应的进程。使用
nohup ./startserver.sh &或./startservernohup.sh方式启动TongWeb。 
 
6.2 控制台无法访问 
启动TongWeb后控制台无法访问，解决此问题的具体步骤如下。 


## 第 45 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
37 
1. 先确认TongWeb是否已经启动成功，通过JDK的jps -v命令或ps -ef|grep java命令查看TongWeb的
进程是否存在，具体的运行代码如下。 
7044 ThorBootstrap -Xmx512m -XX:MaxPermSize=192m -XX:+UnlockDiagnosticVMOptions 
-XX:+LogVMOutput -Djava.security.auth.login.config= 
/home/TongWeb7.0/conf/security/login.config  
后面参数省略 
 
2. 查看TongWeb日志server.log中，是否已显示启动完成，只有启动成功才能访问控制台，日志中如
下内容表示启动完成。 
[INFO] [core] [TongWeb server startup complete in 72757 ms] 
 
3. 检查conf/tongweb.xml中的配置，确认控制台使用端口，并通过netstat命令确认端口已启动，具
体的运行代码如下。 
Windows 平台： netstat -ano | find "9060" 
Linux 平台：netstat -an | grep 9060 
tongweb.xml 中的配置： 
#TongWeb 控制台访问端口，若有ssl-enabled 为true 说明是https 协议。 
<http-listener name="system-http-listener" port="9060" ssl-enabled="true" 
 
4. 通过ping <TongWeb_IP>测试网络是否连通；通过telnet <TongWeb_IP> 9060测试端口是否连通。
常见故障原因如下： 
⚫ 
网络不通。 
⚫ 
网络通，但端口不通。通常是防火墙导致端口不通。需要确认网络连通，防火墙端口开启。 
5. 某些Windows平台下，需要把控制台站点加入IE的受信任站点才可以，如下图所示。 


## 第 46 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
38 
 
图 6.2-1：IE中添加受信任的站点 
6.3 无法使用80端口 
故障现象： 
在Unix/Linux平台下，用普通用户安装TongWeb、Apache或Nginx，并配置80端口，启动时报80端口没
有权限。 
故障原因： 
Unix/Linux平台限制，80端口只有root用户才能使用。 
解决方法： 
以root用户启动TongWeb、Apache或Nginx。 
6.4 JVM内存无法调大 
故障现象： 
剩余物理内存很大，应用需要使用更大的JVM内存，但JVM内存无法调大到4GB以上。如果在检查剩余物
理内存足够的情况下，发生这种问题，此时需要确认的信息有以下两点。 
1. 计算机的操作系统必须为64位，32位操作系统无法管理更多物理内存。 
2. 安装的JDK是否为64位。32位的JDK在Windows下仅能设到1.5GB左右，在不同的Unix/Linux系统下
仅能设为2~3GB。 
注意： 
以上方法适用于TongWeb所有版本以及所有Java类应用程序。 
 
 


## 第 47 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
39 
附录A 开机自启动服务安装工具 
通过运行该工具可以将TongWeb配成windows服务，在Linux下自动配成开机自启动。 
使用方法： 
进入通过安装程序安装好的TongWeb的bin目录下，执行下列命令： 
⚫ 
Windows：installservice.bat 
⚫ 
Linux:     sh installservice.sh  
Linux系统执行后，默认使用systemd管理tongweb，可以使用systemctl start|stop|restart等命令。
如果需要关闭开机自启，可执行以下命令： 
systemctl disable tongweb.service 
 
说明：专用机安装完成后，已实现开机自启。 
 
如果不能自启动： 
1. 
确认当前操作系统版本对于如上目录，是否是自启动。可以手动执行如上目录确认。 
2. 
确认要TongWeb能否正常启动，可以手动启动确认或者查看日志文件中的启动日志。 
 
关于windows服务： 
通过开机自启动服务安装工具，只是将TongWeb配成了windows服务，服务后续的启动、停止和删除都
需要通过命令行或者windows服务。 
TongWeb在windows平台提供以服务方式启动。支持64位和32位系统。 
在安装服务之前，首先需要运行${TongWeb_HOME}/service目录下的setEnv.bat。 
 
注意： 
如果需要支持已存在域的启动，需要设置-Dsingle=true（默认为-Dsingle=false）仅支持对该TongWeb
的自启动及停止。当配置-Dsingle=true时，可以看到准确的TongWeb服务启停状态。 
另外，当-Dsingle=false时，如果需要支持jdk9及以上环境，需要在setEnv.bat中配置： 
set TW_OPTS=%TW_OPTS% -Djdk9=true 
 
关于集群中的Agent服务： 
⚫ 
若启动过Agent服务，开机自启会自动启动Agent服务。 
若启动过Agent服务，且不需要开机自启动Agent服务，可手动删除
“${TongWeb_HOME}/conf/domains.list”中agent的记录。 
注意：Agent服务启动后，才会在“${TongWeb_HOME}/conf/domains.list”文件中记录。 
⚫ 
若没有启动过Agent服务，则不会开机自启动Agent服务。 
 
管理服务操作方法： 
1. 
在${TongWeb_HOME}/service/bin目录下运行TongwebService.exe -install，注册TongWeb服务。


## 第 48 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
40 
注册后用户可查看window服务是否已经增加了名为"Tong"的服务（服务名称可配置，默认为
"Tong"）。注：也可以通过安装工具完成。 
2. 
在${TongWeb_HOME}/service/bin目录下运行TongwebService -start，启动TongWeb服务。 
3. 
在${TongWeb_HOME}/service/bin目录下运行TongwebService -stop，停止TongWeb服务。 
4. 
在${TongWeb_HOME}/service/bin目录下运行TongwebService -uninstall，卸载TongWeb服务； 
 
${TongWeb_HOME}/service/conf/tw.xml中的参数说明如下所示： 
 
表 A.1-1：service参数说明 
Service子标签名称 
说明 
id 
服务的名称 
Name 
服务的显示名称，也就是通过Windows的服务管理查看到的服务名称。如果
配置成： 
<id>TongwebService</id> 
<name>Tongweb Service</name> 
那么在服务管理中将会如下图所示： 
 
查看服务属性如下图所示： 
 
description 
对服务的描述 
logpath 
日志路径。服务的安装启动日志路径配置如下： 
<logpath>${TongWeb_HOME}\log</logpath> 
可以修改为指定路径。 
timeout 
设置的服务器启动超时时间，超过时间时服务器还未启动成功，则服务器停
止启动。单位是毫秒。 
startargument 
启动TongWeb的各项参数 
stopargument 
停止TongWeb的各项参数 
 
作用范围说明：当-Dsingle=false时， 
⚫ 
如果不存在域，就启动/停止该TongWeb。 
⚫ 
如果存在域，会启动/启动域中所有TongWeb。


## 第 49 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
41 
附录B 术语及缩略语 
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
 


## 第 50 页

东方通应用服务器软件TongWeb_V7.0产品简介及安装指南 
7049_M9A01 
版权所有©东方通 
42 
 



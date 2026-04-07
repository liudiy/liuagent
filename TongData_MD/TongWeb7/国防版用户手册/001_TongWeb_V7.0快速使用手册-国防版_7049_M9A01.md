## 第 1 页

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


## 第 2 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
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

东方通应用服务器软件TongWeb_V7.0快速使用手册 
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
2.7 查看安装信息，新增永久license绑定mac地址的说明。 
7049_M8A01 7.0.4.9_M8 
无 
7049_M7A01 7.0.4.9_M7 
无 
7049_M6A01 7.0.4.9_M6 
新增如下章节： 
2.7 查看安装信息 
修改如下章节： 
2.6 目录结构说明，补充二级目录说明。 
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
修改如下章节： 
⚫ 
2.1 安装要求，新增支持JDK17。 
⚫ 
2.1 安装要求，国密认证JDK要求由“JDK8-JDK11”变更为
“JDK8及以上版本”，当在JDK17环境下，需要额外添加启动
参数。 
7048A01 
7.0.4.8 
修改如下章节： 
⚫ 
2.1 安装要求，浏览器支持版本由IE8修改为“IE11”。 
⚫ 
2.1 安装要求，国密认证JDK环境要求由“JDK8小版本”修改
为“JDK8-JDK11”。 
7047A01 
7.0.4.7 
新增如下章节： 
3.1 前置条件，创建数据源所需的前提条件。 
7046A01 
7.0.4.6 
⚫ 更新“图 3.1-4：创建连接池-4”、“图 3.3-1：访问应用” 
“2.5 启动和停止”停止命令增加超时时间设置 
7045A01 
7.0.4.5 
⚫ 
在“2.5启动和停止”中添加快速停止TongWeb参数quick 
⚫ 
将${TW_HOME}改为${TongWeb_HOME} 
⚫ 
更新“图 3.1-5：连接池测试连接” 
⚫ 
更新“图4.5-1：设置并发线程数” 
⚫ 
更新“图 4.6-1：修改HTTP通道” 
⚫ 
更新“图 4.8-1：JSP预编译” 
7044A01 
7.0.4.4 
⚫ 
更新“2.2安装步骤”中默认shut-down port为7090（原来为
8005） 
⚫ 
在“2.5启动和停止”中添加首次登录管理控制台需更新初始
密码的说明 


## 第 4 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
iii 
手册版本 
适用于产品版本 
更新内容 
⚫ 
更新“图3.1-1创建连接池-1” 
7043A01 
7.0.4.3 
无 
7042A01 
7.0.4.2 
无 
7041A01 
7.0.4.1 
统一使用TongWeb用户使用手册模板。 


## 第 5 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
iv 
前言 
本文档是TongWeb产品的用户使用手册之一，提供各版本客户快速安装，应用部署，及常用配置的说明。 
 
适合的对象 
本手册主要适用于生产环境中的系统管理员，部分内容同样适用于应用开发人员和应用部署人员。  
本手册假定您已经具备如下技能： 
1. 基本系统管理任务； 
2. 安装软件； 
3. 使用Web 浏览器； 
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
⚫ 008_TongWeb_V7.0二次开发接口：TongWeb的JMX、REST、SNMP接口说明。 
⚫ 009_TongWeb_V7.0应用开发手册：提供在TongWeb上开发应用的各类规范说明。 
⚫ 010_TongWeb_V7.0等级保护指南：提供等级保护功能开启后的使用说明。 
⚫ 100_TongWeb_V7.0集群管理指南-国防版：详细介绍集群的配置和管理。 
 
技术支持 
东方通产品将为您提供全方位的技术支持，您可以通过以下方式获得技术支持：  
网址：www.tongtech.com  
电话：400-650-7088 
邮箱：pqmo@tongtech.com 
 
您在取得技术支持时，请提供如下信息： 
1.  您的姓名  
2.  您的公司信息  
3.  您的联系方式  
4.  操作系统及其版本  


## 第 6 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
v 
5.  产品版本号  
6.  日志等错误的详细信息 


## 第 7 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
vi 
目 录 
第1章 产品介绍 ......................................................................................................................................................... 1 
1.1 概述 .................................................................................................................................................................. 1 
1.2 规范支持 .......................................................................................................................................................... 1 
第2章 安装 ................................................................................................................................................................. 2 
2.1 安装要求 .......................................................................................................................................................... 2 
2.2 获取安装包 ...................................................................................................................................................... 3 
2.3 前提条件 .......................................................................................................................................................... 3 
2.4 安装步骤 .......................................................................................................................................................... 3 
2.4.1 绿色版 ....................................................................................................................................................... 3 
2.4.2 安装程序版 ............................................................................................................................................... 4 
2.5 安装License ...................................................................................................................................................... 8 
2.6 目录结构说明 .................................................................................................................................................. 8 
2.7 查看安装信息 ................................................................................................................................................ 10 
2.8 启动和停止 ..................................................................................................................................................... 11 
第3章 应用部署 ....................................................................................................................................................... 13 
3.1 前置条件 ........................................................................................................................................................ 13 
3.2 创建数据源 .................................................................................................................................................... 13 
3.3 部署应用 ........................................................................................................................................................ 15 
3.4 测试并访问应用 ............................................................................................................................................ 17 
第4章 常用Web主要参数调整 ............................................................................................................................... 18 
4.1 设置JVM堆内存 ............................................................................................................................................ 18 
4.2 修改应用访问端口 ........................................................................................................................................ 18 
4.3 设置日志 ........................................................................................................................................................ 19 
4.4 设置访问日志 ................................................................................................................................................ 20 
4.5 设置并发线程数 ............................................................................................................................................ 20 
4.6 修改HTTP通道 .............................................................................................................................................. 21 
4.7 设置JDBC资源池性能参数 ........................................................................................................................... 21 
4.8 JSP预编译 ....................................................................................................................................................... 22 
附录A 
术语及缩略语 ........................................................................................................................................... 23 


## 第 8 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
1 
第1章 产品介绍 
1.1 概述 
应用服务器TongWeb v7支持JavaEE7和JavaEE8规范。它为企业应用提供了可靠、可伸缩、可管理和高
安全的基础平台。同时具有功能完善、支持开放标准和基于组件开发、多层架构、轻量等特点，为开发和
部署企业应用提供了必需的底层核心功能。用户通过TongWeb的管理控制台可方便的对应用进行管理，同时
能够监控系统组件和应用运行时的状态及调优。因此TongWeb适用于高度可用、可靠、可伸缩，稳定的业务
领域。 
1.2 规范支持 
表 1.2-1：支持的规范 
类型 
支持内容 
组件 
JSP2.3 
Servlet3.1/Severlet4.0 
WebSocket1.0 
JSF2.2 
JSTL1.2  
EJB3.2 
EL3.0 
JCA1.7 
Debugging Support forOther Languages 1.0 
Common Annotations for theJava Platform 1.2 
JPA2.1 
Bean Validation 1.1 
CDI 1.1 
Dependency Injection for Java 1.0 
资源和服务 
JTA1.2 
JDBC 4.0  
协议 
HTTP1.1  
RMI 
安全 
JAAS1.0 


## 第 9 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
2 
第2章 安装 
2.1 安装要求 
支持的平台 
表 2.1-1：TongWeb支持的平台 
Windows平台  
Microsoft Windows系列 
Linux平台  
RedHat系列 
Suse Linux系列 
深度操作系统 
银河麒麟操作系统 
中标麒麟操作系统 
统信操作系统 
Unix平台  
Sun Microsystems Solaris系列 
IBM AIX系列 
Mac OS平台 
Mac OS 
 
系统要求 
表 2.1-2：TongWeb系统要求 
系统组件 
系统要求 
Java环境 
JDK7u40及以上版本 
注意： 
⚫ 
JDK11的环境，请使用TongWeb免安装版本。 
⚫ 
支持 Oracle JDK，但部分 Oracle JDK 版本商用收费，在生产使
用时请注意商业授权，或采用 Open JDK、Tong JDK。 
⚫ 
若需要创建HTTPS通道，且SSL协议使用“TLS1.3”，JDK要求
JDK1.8.0_261及以上版本。 
⚫ 
当创建HTTPS通道，需要启动国密认证时，JDK要求JDK8及以
上版本。 
当在JDK17环境下时，需要额外添加如下启动参数。 
⚫ 
--add-opens=java.base/sun.security.rsa=ALL-UNNAMED 
⚫ 
--add-opens=java.base/sun.security.util=ALL-UNNAMED 
⚫ 
--add-opens=java.base/sun.security.jca=ALL-UNNAMED 
内存 
至少需要512MB的内存 
硬盘空间 
至少需要1024MB磁盘空间 
监视器 
图形界面安装需要256色，字符界面安装没有色彩要求 
浏览器 
Microsoft IE11或Firefox4.0及以上版本浏览器 
 


## 第 10 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
3 
2.2 获取安装包 
购买TongWeb 产品后，TongWeb 产品光盘中提供了绿色版或者安装程序版。 
产品版本 
安装包 
绿色版 
⚫ 
Windows: 
TongWeb7.0.x.x _XX_Windows.tar.gz 
⚫ 
Linux: 
TongWeb7.0.x.x_XX_Linux.tar.gz 
安装程序版 
⚫ 
Windows: 
Install_TW7.0.x.x_XX_Windows.exe 
⚫ 
Linux： 
Install_TW7.0.x.x_XX_Linux.bin 
 
2.3 前提条件  
TongWeb启动前，需设置使用的JDK路径，即设置本机环境变量JAVA_HOME值。 
2.4 安装步骤 
TongWeb提供绿色版或者安装程序版，本章节介绍如何安装绿色版和安装程序版。 
2.4.1 绿色版 
绿色版为免安装版，解压后即可使用。 
本章节以“在Linux平台上解压标准版TongWeb7”为例进行说明。 
前置条件 
已获取标准版TongWeb7安装包，例如：TongWeb7.0.x.x_Standard_Linux.tar.gz 
操作步骤 
1. 
以root用户登录Linux平台。 
2. 
将TongWeb安装包上传到Linux平台，例如“/home/test/”目录。 
3. 
执行如下命令，解压安装包。解压完成即完成TongWeb的安装。 
tar -zxvf TongWeb7.0.x.x_XX_Linux.tar.gz 
4. 
解压后，进入到安装目录，可查看安装相关目录结构，如下图所示。 


## 第 11 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
4 
 
2.4.2 安装程序版 
如果Linux平台提供图形界面安装，直接执行安装程序：sh Install_TW7.0.*.*_GuoFang_Linux.bin，
安装过程和Windows平台一致。 
如果没有开启图形界面功能，需要通过命令行安装。本章节以国防版TongWeb7在Linux平台上用命令行，
并选用英文安装作为示例，其他版本步骤相同。 
注：无论界面或命令行，如果想使用中文安装，都需要设置Linux平台编码LANG为zh_CN.UTF-8。 
1. 
以root用户运行sh Install_TW7.0.x.x_GuoFang_Linux.bin -i console，并选择安装语言。 
[root@ Machine04]# sh Install_TW7.0.x.x_GuoFang_Linux.bin -i console 
Preparing to install... 
Extracting the installation resources from the installer archive... 
Configuring the installer for this system's environment... 
 
Launching installer... 
 
Preparing CONSOLE Mode Installation... 
 
========================================================= 
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


## 第 12 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
5 
 
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
installing or using the Software.By using the Software, you acknowledge that you accept all terms of 
thisAgreement.If you do not agree to the terms of this Agreement, you are not authorized toinstall or 
use the Software. 
Article 1-Definitions 
 
Unless the context indicates otherwise, the following terms have the meaningsset forth below: 
1.“Software": refers to the software product provided by Tongtech, includingassociated 
documentation, data, and other materials. 
2,“User" or “You": refers to the individual or legal entity that obtains alicense to use the Software. 
3.“License": refers to the limited, non-exclusive, non-transferable rightgranted by Tongtech to use the 
Software under this Agreement. 
4.“Device": refers to the computer or other terminal legally owned or 
 
PRESS <ENTER> TO CONTINUE: 
3. 
出现如下信息后，按回车键继续安装。 
3. Copy or transfer this software in whole or in part. 
 
When you transfer this software in part or in whole to any third part, your right to 
use the software shall terminate immediately without notice. 
 
The copyright and ownership of this software: 
The copyright of this software is owned by Tongtech co., LTD. The structures, tissues 
and codes are the most valuable commercial secrets of Tongtech co., LTD. This software 
and documents are protected by national copyright laws and international treaty 
provisions. You are not allowed to delete the copyright notice from this software. 
You must agree to prohibit any kind of illegal copy of this software and documents. 
 
Limited warranty: 


## 第 13 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
6 
In the largest permitting area of the law, in no situation shall Tongtech co., LTD 
be liable for any special, unexpected, direct or indirect damages (including, without 
limitation, damages for loss of business profits, business interruption, loss of 
business information, or any other pecuniary loss) arising out of the use of or 
inability to use this product and the providing or inability to provide supporting 
services, even if Tongtech co., LTD has been advised of the possibility of such damages. 
 
PRESS <ENTER> TO CONTINUE: 
4. 
请选择是否接受许可条款，若接受请输入“Y”。 
Termination: 
Tongtech co., LTD may terminate the license at any time if you violate any term or 
condition of the license. When the license is terminated, you must destroy all copies 
of the software and all of its documents immediately, or return them to Tongtech co., 
LTD. 
 
Law: 
"COPYRIGHT LAW OF THE PEOPLE'S REPUBLIC OF CHINA", "Trademark Law of the People's 
Republic of China", "Patent Law of the People's Republic of China","Berne Conventionon 
the Protection of Literary and Artistic Works" 
 
Now, you must have already carefully read and understand this license, and agree to 
obey all the terms and conditions strictly. 
 
DO YOU ACCEPT THE TERMS OF THIS LICENSE AGREEMENT? (Y/N): Y 
5. 
进入选择Java VM，默认为当前系统正在使用Java VM。 
========================================================= 
Choose Java Virtual Machine 
--------------------------- 
Please Choose a Java VM for Use by the Installed Application 
->1- /usr/java/jdk1.8.0_144/bin/java   //当前系统正使用的JDK 
2- /usr/bin/java 
  3- Choose a Java VM already installed on this system//使用其它JDK 
ENTER THE NUMBER FOR THE JAVA VM, OR PRESS <ENTER> TO ACCEPT THE CURRENT SELECTION: 
3 
ENTER THE ABSOLUTE PATH TO THE JAVA VM EXECUTABLE OF YOUR CHOICE: 
/home/tong/jdk/jdk1.7.0_67/bin/java 
PATH TO THE JAVA EXECUTABLE IS: 
/home/tong/jdk/jdk1.7.0_67/bin/java 
IS THIS CORRECT? (Y/N): Y 
6. 
按回车键进入安装路径设置。输入安装路径（注：目录不能带中文），若同意使用给出的默认安装
路径，请按回车键继续安装。 


## 第 14 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
7 
========================================================= 
Choose Install Folder 
--------------------- 
 
Where would you like to install? 
 
Default Install Folder: /root/TongWeb7.0 
 
ENTER AN ABSOLUTE PATH, OR PRESS <ENTER> TO ACCEPT THE DEFAULT: 
7. 
出现如下信息后，请输入链接选项，选择后，按回车键继续安装。 
========================================================= 
Choose Link Location 
-------------------- 
 
Where would you like to create links? 
 
  ->1- Default: /root 
    2- In your home folder 
    3- Choose another location... 
    4- Don't create links 
 
ENTER THE NUMBER OF AN OPTION ABOVE, OR PRESS <ENTER> TO ACCEPT THEDEFAULT： 
8. 
确认预安装信息是否正确，若正确按回车键继续安装。 
========================================================= 
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
 


## 第 15 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
8 
PRESS <ENTER> TO CONTINUE: 
9. 
安装完成后，进入端口修改界面，缺省值为默认端口。 
====================================================== 
Installing... 
------------- 
[==================|==================|=================] 
[------------------|------------------|------------------|----------------] 
======================================================= 
Set Ports 
--------- 
tong-http-listener (DEFAULT: 8088): 8089 
system-http-listener (DEFAULT: 9060): 9061 
ejb-server-listener (DEFAULT:5100): 5100 
jmx-service (DEFAULT:7200): 7201 
shutdown-port (DEFAULT:7090): 7090 
10. 输入端口后，按回车键结束安装。 
Installation Complete 
--------------------- 
 
Congratulations. TongWeb7 has been successfully installed to: 
 
   /root/TongWeb7.0 
 
PRESS <ENTER> TO EXIT THE INSTALLER: 
2.5 安装License 
购买TongWeb产品后，在TongWeb产品光盘中提供有license文件。将license.dat文件复制到安装完成
的TongWeb根目录下。 
2.6 目录结构说明 
表 2.6-1：TongWeb目录结构 
一级目录 
二级目录 
说明 
Agent 
- 
代理服务器注册节点（仅企业版提供）。 
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


## 第 16 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
9 
一级目录 
二级目录 
说明 
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
audit-log 
TongWeb启停审计日志。 
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


## 第 17 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
10 
一级目录 
二级目录 
说明 
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
 
2.7 查看安装信息 
为了帮助您进行系统维护、管理软件许可、进行故障排除等任务，TongWeb 提供了查看其安装信息的
功能。 
前置条件 
已安装TongWeb。 
操作步骤 
进入 TongWeb 安装目录“${TongWeb_HOME}/bin”。 
运行“version.[bat|sh]”脚本，即可查看TongWeb 的版本信息、构建时间、安装时间以及 License 信息


## 第 18 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
11 
等。 
 
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
在Linux 系统中，部分文件系统不支持记录文件的创建时间，读取的时间可能不准确。然而，一
旦TongWeb 启动，它将与系统时间进行同步，以此来保证时间记录的准确性。 
2.8 启动和停止 
以在Linux下字符界面为例说明TongWeb的启动和停止过程： 
1. 启动TongWeb需要进入TongWeb的bin目录，执行如下命令： 
./startservernohup.sh 
注意：这是后台启动方式，如果直接运行startserver.sh，当Telnet断开后，会导致TongWeb进程
退出。 
2. 当日志中出现如下一行，没有异常信息，说明TongWeb启动成功。 
[2018-05-17 16:32:24] [INFO] [core] [TongWeb server startup complete in 7839 ms.] 
3. 在客户端打开浏览器，输入TongWeb管理控制台地址http://<TongWebIP>:9060/console，端口9060，


## 第 19 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
12 
前缀console，显示出TongWeb管理控制台首页面。 
输入用户名/密码登录，默认系统管理员及初始密码为：thanos/thanos123.com 
注意： 
⚫ 
首次登录管理控制台时必须更新初始密码，密码必须由大写字母、小写字母、数字、特殊字
符4种组成，长度不得少于10位。 
⚫ 
新密码不能和原始密码一致。 
4. 停止TongWeb，需进入TongWeb的bin目录，执行如下命令： 
./stopserver.sh 
 
快速停止TongWeb，执行如下命令： 
./stopserver.sh  quick 
设置快速停止TongWeb的超时时间，在设置的超时时间（20s）内快速停止TongWeb，执行如下命令： 
./stopserver.sh  quick  20 
强制停止TongWeb，执行如下命令。 
强停命令, 当进程无法完全停止时，通过该命令强行停止。 
./forcestopserver.sh 
 
 
 


## 第 20 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
13 
第3章 应用部署 
本章采用自带用例${TongWeb_HOME}/samples/jdbc/nonxa/nonXaDsWeb.war，介绍如何部署一个通过数
据源访问数据库信息的应用。 
3.1 前置条件 
根据下方选择，用户需要提前准备好对应数据库的连接信息，比如用户账号、IP地址、端口、相应版
本对应的JDBC的jar包，开通TongWeb所在机器和数据库服务器之间的端口，确保能够连接上。 
已在TongWeb管理控制台的首页设置服务器选择文件可选目录。 
3.2 创建数据源 
启动TongWeb，登录管理控制台，进行JDBC连接池配置。 
1. 进入“JDBC配置”界面，单击“创建连接池”按钮，如下图： 
 
图 3.2-1：创建连接池-1 
配置参数： 
⚫ 
名称：testdb 
⚫ 
资源类型：DataSource 
⚫ 
数据库类型：Oracle Type 4 Driver for Oracle 
⚫ 
数据库驱动名称：oracle.jdbc.driver.OracleDriver 
⚫ 
连接URL：jdbc:oracle:thin:@[host]:[1521]:[dbName] 


## 第 21 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
14 
⚫ 
数据库驱动类名：oracle.jdbc.driver.OracleDriver 
⚫ 
用户名／密码：数据库的用户密码 
⚫ 
驱动路径：数据库驱动所在路径 
2. 单击“下一步”，进入池设置，参数采用默认值，如下图: 
 
图 3.2-2：创建连接池-2 
3. 单击“下一步”，进入验证属性，参数采用默认值，如下图: 
 
图 3.2-3：创建连接池-3 
4. 单击“下一步”，进入高级属性，参数采用默认值，如下图: 
 
图 3.2-4：创建连接池-4 
5. 单击“完成”，testdb创建成功。单击“testdb”连接池后的测试连接，连接成功，如下图： 


## 第 22 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
15 
 
图 3.2-5：连接池测试连接 
3.3 部署应用 
TongWeb可以从本机和服务器，以目录或文件方式部署。但本机只能以文件方式部署，现介绍文件形式
部署。 
1. 登录TongWeb管理控制台，进入“应用管理”界面，单击“部署应用”，如下图： 
 
图 3.3-1：部署应用 
配置参数： 
⚫ 
文件位置：本机。 
⚫ 
部署文件：${TongWeb_HOME}\samples\jdbc\nonxa\nonXaDsWeb.war（注：应用所在路径）。 
2. 单击“开始部署”，进入基本属性配置界面。 


## 第 23 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
16 
 
图 3.3-2：部署应用-基本属性配置 
配置参数： 
⚫ 
应用名称：nonXaDsWeb 
⚫ 
应用前缀：/nonXaDsWeb 
⚫ 
防篡改：可根据实际需要选择开启。若选择开启，在“防篡改策略”下拉列表中可选择已创
建的防篡改策略。 
说明： 
在TongWeb管理控制台左侧导航栏中，单击防篡改策略，在防篡改策略页面，可创建防篡改策
略。 
⚫ 
其他参数：采用默认值 
3. 单击“下一步”，如下图： 
 
图 3.3-3：部署应用-虚拟主机配置 
4. 虚拟主机选择“server”，单击“下一步”，开始部署应用。 


## 第 24 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
17 
 
图 3.3-4：部署应用-部署完成 
5. 单击“完成”。如果显示部署成功，则整个部署过程完毕。同时注意观察TongWeb日志，查看部署
过程中是否出现异常信息。 
3.4 测试并访问应用 
1. 确认应用部署成功，日志中没有异常信息出现。 
2. TongWeb默认为应用分配的访问端口为8088，通过http://<IP>:8088/nonXaDsWeb/可以访问到应用。 
3. 或者单击应用后的“http访问”以访问应用。（注：TonWeb不自带https通道，如果想通过https访
问，需要在“管理控制台”－>“WEB容器配置”－>“HTTP通道管理”－>创建https通道）。 
 
图 3.4-1：访问应用 
 
 
 


## 第 25 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
18 
第4章 常用Web主要参数调整 
    本章简单介绍影响性能的主要参数，以200用户并发为基准，此参数调整基本可保证系统正常运行，但
并不能保证调整的参数为最优。 
4.1 设置JVM堆内存 
1. 修改${TongWeb_HOME}/bin目录下external.vmoptions配置文件，在配置文件开始，根据需要设置
JVM堆内存大小，主要是增大堆内存，用户还可根据自己需要增加JVM参数,建议设置如下： 
-Xms2048m 
-Xmx2048m 
2. 或者在控制台选择“启动参数配置”设置JVM堆内存大小、垃圾回收方法等，如图： 
 
图 4.1-1：设置JVM堆内存 
4.2 修改应用访问端口 
有两种方式可以修改应用访问端口。 
方式一： 
修改${TongWeb_HOME}/conf目录下的tongweb.xml文件，找到8088端口后改为需要的端口。修改配置文件后，
需重新启动TongWeb服务才能生效。 
方式二： 
1. 进入“管理控制台”->“WEB容器配置”－>“HTTP通道管理”，单击“tong-http-listener”，修改监
听端口字段处的8088端口。如图: 


## 第 26 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
19 
 
图 4.2-1：修改应用访问端口 
2. 同时还可以为应用配置多个访问端口，具体见《003_TongWeb服务配置指南》。 
3. 在Unix/Linux下如果要使用80端口，则需要以root用户启动、停止TongWeb服务器。 
4.3 设置日志 
TongWeb日志默认通过轮转方式生成，轮转日志时将新建一个名为server.log的空文件，并将旧文件重
命名为server.date_i，其中date是轮转文件的日期，i为序列号。 
进入“管理控制台”－>“日志服务”－>“系统日志配置”里进行配置。如下图： 
 
图 4.3-1：系统日志配置 
设置方式一：按大小轮转生成日志，如50M生成一个server.log。 
参数： 
⚫ 
日志数量：20个（系统日志超过该数量后，会自动删除较早的日志文件） 


## 第 27 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
20 
⚫ 
轮转大小：50MB 
设置方式二：按周期生成日志，按设置的时间生成一个server.log。 
参数： 
⚫ 
日志数量：20个（系统日志超过该数量后，会自动删除较早的日志文件） 
⚫ 
轮转周期：以小时为单位 
设置方式三：按天生成日志，按每天生成一个server.log。 
参数： 
⚫ 
日志数量：20个（系统日志超过该数量后，会自动删除较早的日志文件） 
4.4 设置访问日志 
访问日志主要记录应用访问的IP和URL，日志生成在${TongWeb_HOME}/logs目录下。进入“管理控制台”
－>“WEB容器配置”－>“虚拟主机管理”，选择应用使用的虚拟主机，如“server”和“admin”, 选择是
否开启“访问日志”。此选项默认为关闭，如果没有需要可以选择关闭此日志以节省资源。如下图： 
 
图 4.4-1：关闭访问日志 
4.5 设置并发线程数 
TongWeb默认的并发初始线程数只有1，实际使用时需根据并发数设置。进入“管理控制台”－> “WEB
容器配置”－>“HTTP通道处理”中，编辑应用所使用的通道，如“tong-http-listener”。 


## 第 28 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
21 
 
图 4.5-1：设置并发线程数 
⚫ 
最大线程数： 
200  
(注：暂时建议值) 
⚫ 
初始线程数： 
10   
(注：暂时建议值) 
⚫ 
等待队列：  100   (注：暂时建议值) 
4.6 修改HTTP通道 
进入“管理控制台”－>“WEB容器配置”－>“HTTP通道管理”，单击“tong-http-listener”修改参
数，如图： 
 
图 4.6-1：修改HTTP通道 
以下几个参数对大并发下设置才有效果，具体含义参见《003_TongWeb服务配置指南》，暂时使用默认
值。 
⚫ 
TCP_NODELAY 
⚫ 
请求超时时间 
⚫ 
最大长连接请求数 
⚫ 
处理器缓存数量 
4.7 设置JDBC资源池性能参数 
进入“管理控制台”－>“JDBC配置”，修改创建的testdb连接池，对连接池影响较大的参数是连接数，
如图： 


## 第 29 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
22 
 
图 4.7-1：设置JDBC资源池性能参数 
⚫ 
最大连接数： 
10  
(注：暂时建议值) 
⚫ 
初始连接数： 
10  
(注：暂时建议值) 
⚫ 
等待超时时间： 30000   (注：暂时建议值) 
4.8 JSP预编译 
部署Web应用时，有“JSP预编译”功能，如果勾选此选项可在部署应用时就将所有JSP编译为class,如
下图所示。 
 
图 4.8-1：JSP预编译


## 第 30 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
23 
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
 
 


## 第 31 页

东方通应用服务器软件TongWeb_V7.0快速使用手册 
7049_M9A01 
版权所有©东方通 
24 
 



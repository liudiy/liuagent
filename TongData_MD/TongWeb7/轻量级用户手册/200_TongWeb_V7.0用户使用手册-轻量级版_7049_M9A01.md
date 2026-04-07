## 第 1 页

东方通应用服务器软件TongWeb V7.0 用户使用手册-轻量级版 
V7049A01 
1 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


## 第 2 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
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

东方通应用服务器软件TongWeb_V7.0用户使用手册 
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
删除如下章节： 
5.7.3 多数据源配置，屏蔽多数据源功能。 
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
⚫ 
在“3.3tongweb.xml配置说明”中添加停止端口7090使用说明 
⚫ 
将${TW_HOME}改为${TongWeb_HOME} 
⚫ 
在“表6.2-4：连接池高级属性配置项“添加fair-queue公平锁配
置项 
⚫ 
更新“表6.2-4：连接池高级属性配置项“中max-age的默认值和
描述 
⚫ 
删除“表3.2-2：TongWeb参数说明“-Dtongweb.jconsole.cbport
参数 
⚫ 
删除“表3.2-1：jvm参数说明“-Djava.security.auth.login.config
参数 
⚫ 
删除“8.1JMX-service”章节中的外部使用jmx连接端口描述 
⚫ 
更新“表6.2-1：数据源连接池基本配置项“中user-name的说
明 
⚫ 
“5.2 容器配置”增加xmlBlockExternal、unloadDelay、
addWebinfClassesResources、sessionLog属性说明 
更新“1.1 概述”中的描述 
7044A01 
7.0.4.4 
⚫ 
“3.3tongweb.xml配置说明”中更新shutdown-port为7090 
⚫ 
更新“表3.2-2：TongWeb参数说明”中
-DshutdownSocketDisabled说明中的TCP监听默认端口为7090
（原来为8005） 
⚫ 
在“表3.2-2：TongWeb参数说明”中添加
-Dtongweb.restart.interval 
7043A01 
7.0.4.3 
无 
7042A01 
7.0.4.2 
无 


## 第 4 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
iii 
手册版本 
适用于产品版本 
更新内容 
7041A01 
7.0.4.1 
⚫ 统一使用TongWeb用户使用手册模板。 
⚫ 删除第二章“安装启动”的内容，提供“002_TongWeb安装启
动指南”。 
⚫ 删除原附录“命令行使用说明”，提供
“006_TongWebCommandstool使用指南”。 


## 第 5 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
iv 
前言 
本文档是轻量级版TongWeb产品的用户使用手册之一，提供轻量级版本客户详细的服务配置及应用管理
的说明。 
 
适合的对象  
本手册主要适用于生产环境中的系统管理员，部分内容同样适用于应用开发人员和应用部署人员。  
本手册假定您已经具备如下技能：  
1. 基本系统管理任务； 
2. 安装软件； 
3. 使用Web 浏览器； 
4. 启动数据库服务器； 
5. 在终端窗口中发布命令。 
 
用户使用手册集  
轻量级版TongWeb为您提供的用户使用手册集包含的文档有：  
⚫ 000_TongWeb_V7.0用户手册导读：各版本手册集的目录及手册版本说明。 
⚫ 002_TongWeb_V7.0产品简介及安装指南：提供各版本各平台上的安装启动的步骤。 
⚫ 004_TongWeb_V7.0应用管理指南：提供管理控制台对应用进行部署和管理操作的说明。 
⚫ 006_TongWeb_V7.0Commandstool使用指南：提供命令行commandstool的使用说明，基本参数及所有
命令示例。 
⚫ 200_TongWeb_V7.0轻量级版用户使用手册：提供轻量级版本客户详细的服务配置及应用管理的说明。 
 
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
5.  产品版本号  
6.  日志等错误的详细信息


## 第 6 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
v 
目 录 
第1章 产品简介 ......................................................................................................................................................... 1 
第2章 安装启动 ......................................................................................................................................................... 2 
第3章 配置文件 ......................................................................................................................................................... 2 
3.1 主要配置文件 .................................................................................................................................................. 2 
3.2 external.vmoptions参数说明 ............................................................................................................................. 2 
3.3 tongweb.xml配置说明 ...................................................................................................................................... 5 
3.4 tongweb-web.xml配置说明 .............................................................................................................................. 7 
第4章 应用管理 ........................................................................................................................................................ 11 
4.1 自动部署配置 ................................................................................................................................................. 11 
4.2 热部署 ............................................................................................................................................................. 11 
第5章 Web容器 ....................................................................................................................................................... 12 
5.1 容器说明 ........................................................................................................................................................ 12 
5.2 容器配置 ........................................................................................................................................................ 12 
5.3 访问日志 ........................................................................................................................................................ 13 
5.4 虚拟主机 ........................................................................................................................................................ 16 
5.5 通道 ................................................................................................................................................................ 18 
5.5.1 HTTP通道 ................................................................................................................................................ 18 
5.5.2 AJP通道 .................................................................................................................................................... 22 
5.6 虚拟目录 ........................................................................................................................................................ 23 
5.7 JDBC配置 ....................................................................................................................................................... 24 
5.7.1 JDBC数据源............................................................................................................................................. 24 
5.7.2 JDBC数据源配置 ..................................................................................................................................... 24 
第6章 安全服务 ....................................................................................................................................................... 27 
6.1 概述 ................................................................................................................................................................ 27 
6.2 安全域类型 .................................................................................................................................................... 27 
6.3 安全域配置 .................................................................................................................................................... 27 
6.3.1 文件安全域属性配置 ............................................................................................................................. 28 
6.3.2 JDBC安全域属性配置 ............................................................................................................................. 28 
6.3.3 LDAP安全域属性配置 ............................................................................................................................ 29 
6.3.4 JAAS安全域属性配置 ............................................................................................................................. 29 
6.3.5 Script安全域属性配置 ............................................................................................................................. 29 
6.3.6 服务扩展安全域属性配置 ..................................................................................................................... 29 
6.4 管理用户 ........................................................................................................................................................ 30 
第7章 监控协议 ....................................................................................................................................................... 31 


## 第 7 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
vi 
7.1 JMX-service ..................................................................................................................................................... 31 
7.2 SNMP代理服务 .............................................................................................................................................. 31 
7.2.1 SNMP代理服务配置 ............................................................................................................................... 31 
7.2.2 SNMP代理服务示例 ............................................................................................................................... 32 
第8章 日志服务 ....................................................................................................................................................... 34 
8.1 系统日志 ........................................................................................................................................................ 34 
8.2 日志级别 ........................................................................................................................................................ 34 
8.3 压缩日志 ........................................................................................................................................................ 35 
8.4 SQL日志保存路径 .......................................................................................................................................... 36 
附录A 
术语及缩略语 ........................................................................................................................................... 37 


## 第 8 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
1 
第1章 产品简介 
应用服务器TongWeb v7支持JavaEE7和JavaEE8规范。它为企业应用提供了可靠、可伸缩、可管理和高
安全的基础平台。同时具有功能完善、支持开放标准和基于组件开发、多层架构、轻量等特点，为开发和
部署企业应用提供了必需的底层核心功能。用户通过TongWeb轻量级的命令行工具可方便的对应用进行管理。
因此TongWeb轻量级适用于高度可用、可靠、可伸缩，稳定的业务领域。 
TongWeb7轻量级专注于对web应用的支持，具备启动速度快，占用系统资源少，应用开发和移植容易
的特点。版本主要是面向Web应用市场或容器云环境上对资源要求占用少启动快的场景，比如：政府、交通、
金融等行业的电子政务系统。 
轻量版不支持会话（session）的备份和复制、管理控制台、APM运维工具等企业级增量功能，一般通
过命令行方式进行功能配置和管理。 
 


## 第 9 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
2 
第2章 安装启动 
请参见《002_TongWeb产品简介及安装指南》 
 
第3章 配置文件 
3.1 主要配置文件 
在TongWeb轻量级中，主要配置文件有external.vmoptions、tongweb.xml、tongweb.properties、
default-web.xml，还有应用WEB-INF下带的tongweb-web.xml。 
表 3.1-1：主要配置文件说明 
配置文件 
说明 
external.vmoptions 
启动参数配置，包括JVM参数、服务器参数、环境变量JAVA_HOME等；存放
位置：${TongWeb_HOME}/bin目录下。 
tongweb.xml 
Web容器内配置的相关信息，如应用属性、通道、数据源、日志等都在该文件
里配置，存放位置：${TongWeb_HOME}/conf目录下。 
tongweb.properties 
服务器内部参数配置，包括类加载器的加载范围、注解的扫描范围等；存放位
置：${TongWeb_HOME}/conf目录下。 
default-web.xml 
主要是配默认的servlet值，如打开ssi, 增加共用filter，存放位置：
${TongWeb_HOME}/conf目录下。其配置内容形式和/WEB-INF/web.xml一致，
作用于所有的web应用，优先级低于web应用的/WEB-INF/web.xml。 
WEB-INF下的
tongweb-web.xml 
主要配置虚拟目录和访问应用的一些属性配置,存放web应用/WEB-INF/目录下 
3.2 external.vmoptions参数说明 
external.vmoptions文件存在与${TongWeb_HOME}/conf目录下。主要是对启动参数、jvm参数进行配置，
部分参数说明如下： 
表 3.2-1：jvm参数说明 
参数名称 
参数说明  
-Xmx2048m  
指定JVM堆的最大值，默认为物理内存的1/4或者1G，最小为2M  
-Xms2048m 
指定JVM堆的最小值，默认为物理内存的1/4或者1G，最小为2M  
-XX:CICompilerCount 
设置JVM中编译线程的数目 
-XX:MaxPermSize  
设置JVM堆中"永生代"的最大容量  
-XX:+UnlockDiagnosticVMOptions  
当这个参数打开时，可以使用其它的JVM诊断参数  
-XX:LogFile  
Java虚拟机的输出被记录到这个参数指定的文件中，如
${TongWeb_HOME}/logs/jvm.log 


## 第 10 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
3 
参数名称 
参数说明  
-Xloggc:gc.log 
指定垃圾收集日志文件。 
-Xdump:heap 
开启IBM JDK生成堆栈内存镜像。IBM JDK不支持jmap和jstack命令，添加此参数
后配合kill -3 pid系统命令以生成堆栈镜像。这个参数要配合export 
IBM_HEAPDUMPDIR和export IBM_JAVACOREDIR两个环境变量来指定镜像生成的位
置。 
-Djava.util.logging.manager= 
com.tongweb.log.TongwebLogManager 
指定日志管理类，必须是LogManager的子类. 此参数为必须参数。  
-Djava.endorsed.dirs  
在这个目录下的某种标准的实现将重载JDK内对该标准的实现，如果不设这个参
数，默认指向${TongWeb_HOME}/lib/endorsed。 
-Djava.net.preferIPv4Stack=true 
当需要TongWeb轻量级运行于AIX上时，需要在启动脚本中有这此选项配置。设置
为true时用于限制优先使用IP4地址。 
-Dibm.stream.nio=true 
当需要TongWeb轻量级运行于AIX上时，需要在启动脚本中有这此选项配置，它用
于处理 IO 和 NIO 转换器排序问题。如果此选项设置为 true，那么将使用 NIO 
转换器而不是 IO 转换器。缺省情况下，使用 IO 转换器。 
-Djava.security.egd 
随机数获取源，解决JVM在Linux上启动慢的问题。 
-Drequire-secret 
指定ajp协议的默认密码，该参数的优先级低于tongweb.xml。注：设置该参数后，
需要同步修改apache或其它支持ajp协议的负载均衡器的配置文件，以apache为
例，在其workers配置文件中添加'secret'密码属性，形如：
worker.tongweb1.secret=ajp协议密码。 
-Dxss_defense 
xss攻击防护开关，true表示开启，其它值或不存在该参数表示不开启。该功能会
检查请求中的所有参数名和参数值，若包含“尖括号”、“eval()”、“javascript”
等特殊字符则强制返回 403。 
-Dxss_apps 
xss攻击防护生效的应用名，多个应用名以逗号分隔。 
表 3.2-2：TongWeb参数说明 
参数名称 
参数说明 
-Dtongweb.java="%JAVA_HOME%"  
JDK安装的根目录。当用户需要更换TongWeb使用的jdk路径的时候，可以设置这
个参数。 
-Dtongweb.upload  
临时目录下存放所上传的应用目录。通常为${TongWeb_HOME}/temp/upload，当
用户需要更换其他路径作为上传应用目录的时候，可以对此参数进行设置。 
-Dtongweb.app  
已部署应用的目录 ，在脚本中必须设置为${TongWeb_HOME}/deployment。 
-Dtongweb.home  
TongWeb7的安装路径。 


## 第 11 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
4 
参数名称 
参数说明 
-Djava.io.tmpdir 
服务器产生的临时文件以及应用预编译文件所在的目录。 
-Duser.dir 
应用服务器TongWeb的启动脚本和停止脚本所在的目录。 
-Djava.awt.headless 
如果使用headless模式处理awt程序，设置为true; 否则以字符界面启动
TongWeb监控图形出不来。 
-Dcom.tongweb.commons.logging.Log= 
com.tongweb.commons.logging.impl.Jd
k14Logger 
指定TongWeb的日志服务实现类，当用户希望使用其他的日志服务实现类来代替
TongWeb的日志服务可以通过此参数进行设置。 
-Djava.security.policy 
服务器使用Java安全管理器对服务器资源的访问作进一步控制。JVM的安全机制
需要一个安全策略文件（.policy）来定义访问权限，这些权限定义了运行在一
个JVM实例中的类是否可以执行某项运行时操作。在启动服务器时可以用下面的 
-Djava.security.policy属性指定安全策略的全路径名。 
-Djava.security.manager 
如果需要-Djava.security.policy指定的安全策略文件生效，需要在java启动
参数中增加-Djava.security.manager。 
-Dtongweb.rmijmx.cbport  
内部使用的jmx连接端口。 
-Dopenejb.crosscontext=true 
对于跨上下文的访问，在TongWeb中需要在启动脚本中配置参数
-Dopenejb.crosscontext=true即可。 
-Dibm_heapdumpdir 
指定IBM JDK生成的堆内存镜像文件所在的文件夹。参数值必需和环境变量
export IBM_HEAPDUMPDIR值相同。 
-Dibm_javacoredir 
指定IBM JDK生成的栈内存镜像文件所在的文件夹。参数值必需和环境变量
export IBM_JAVACOREDIR值相同。 
-Dtongweb.X_Frame_Options 
配置Http和Ajp的X_Frame_Options响应头。可选配置参数如下：DENY，浏览器
拒绝当前页面加载任何Frame页面；SAMEORIGIN，frame页面的地址只能为同源
域名下的页面；ALLOW-FROM，允许frame加载的页面地址；指定为NONE或者不配
置该参数则在响应头中不存在该内容。 
-DSharedSessionEnabled 
应用共享Session开关,开启后各个应用使用共享的session，设置true或者
false，默认false表示关闭。 
-DSharedSessionContext 
创建Session时，是否使用http请求里基于Cookie附带的Session ID，默认false
表示关闭，关闭后创建Session会自动生成随机ID，开启后则复用Cookie里的ID。
该功能一般在跨应用或跨进程实现SSO时使用。 
-DcontentLength.limit 
设置POST请求中的content length限制，避免一直占住这个连接不断开，一般
针对POST请求的攻击，默认值为Integer的最大值，例如
-DcontentLength.limit=10000。 
-Dread.http.header.timeout 
读一个字节耗费的毫秒数(单位：毫秒/字节)，超过或等于这个速率算超时，默
认值为Long的最大值，例如:  
-Dread.http.header.timeout=500 
与-DcontentLength.limit参数配合使用。 
-Dread.http.header.timeout.limit 
请求头读取超时次数，超过次数将其列入黑名单，开始拒绝请求(连接)，默认
值为Integer的最大值，例如： 


## 第 12 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
5 
参数名称 
参数说明 
-Dread.http.header.timeout.limit=3 
与-Dread.http.header.timeout配合使用。 
-Dblacklist.expired=xxx 
对清理黑名单解锁时间进行设置，默认值为12（单位：小时），例如：
-Dblacklist.expired=1 
与-Dread.http.header.timeout.limit配合使用。 
-DCreateOne 
连接池中如果对每个连接都进行有效性验证是非常耗时的，影响用户体验。
-DCreateOne=true的作用是，在检查到第一个失效连接后，强制让连接池中所
有idle连接都失效,而不再去进行有效性检查，默认值为false。 
-DskipValidationXML 
默认为false,不开启。设置为true时则在应用部署时不会读取并解析应用中的
验证框架配置文件validation.xml。 
-DShutdownSocketDisabled 
以往的方式是在服务器启动后会开启一个TCP监听服务，默认端口为 7090,主要
用于接收停止脚本发送的停止命令，配置该参数可以选择是否开启该服务。该
参数的值为true或false，true表示禁用该服务，false表示保留该服务。若该
服务被禁用，则通过文件监控的方式来实现该功能。 
-DFullURLMode 
补充requestURI地址，boolean类型，true表示将应用配置的重定向地址补充到
requestURI中，false表示忽略，默认值为false。 
-DenableParallelDeploy 
为了满足用户部署应用多导致服务器启动慢的问题，设置为true为开启后服务
器启动时并行部署非系统应用，默认为false。 
-DcustomLogMoudle 
应用中存在如： 
Logger.getLogger（"org.postgresql.Driver"）获取到的Logger对象，如果业
务逻辑中对其进行删除等操作可能会导致与TongWeb的日志系统产生冲突。 
为了解决此类问题可以设置该参数，要求配置以逗号分隔的包名前缀，匹配相
应包名不被TongWeb自带的日志系统接管。 
如-DcustomLogMoudle=org.postgresql 
-Dtongweb.restart.interval 
宕机后重启的时间间隔，以秒为单位。如果不设置这个参数，默认为1秒。 
3.3 tongweb.xml配置说明 
TongWeb轻量级Web容器内的配置，都在${TongWeb_HOME}/conf/tongweb.xml文件里。这里对tongweb.xml
配置文件进行部分说明。注意：自己编辑时各标签要按以下顺序存放。配置文件如下： 
<?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
<tongweb> 
/*自动部署配置*/ 
 
    <auto-deploy enabled="true" jsp-compile="false" dir="${tongweb.root}/autodeploy" 
check-interval="3000"/> 
<hot-deploy enabled="false" watched-resource="WEB-INF/web.xml,MATA-INF/application.xml"/> 
/*部署的应用，会自动写入该标签内*/ 
<apps>    
</apps> 
/*shutdown-port停止端口，默认该属性不启用，默认值为7090*/ 


## 第 13 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
6 
<server shutdown-port="7090"> 
/*web容器配置*/ 
   <web-container jsp-development="true" parameter-encoding="GBK"  
response-encoding="GBK" hung-thread-threshold="0" hostnameVerifier="NullHostnameVerifier">  
/*访问日志配置*/ 
   <access-log pattern="%{yyyyMMddHHmmssSSS}t %U %m %a %D" suffix=".txt" log-extend="false" 
file-date-format="yy.MM.dd.HH"/> 
/*以下是虚拟主机配置*/ 
  <virtual-host name="admin" listeners="system-http-listener" accesslog-enabled="false" 
accesslog-dir="logs/access" sso-enabled="false" remote-filter-enabled="false"> 
     <sso/> 
     <remote-filter/> 
  </virtual-host> 
  <virtual-host name="server" listeners="tong-http-listener" accesslog-enabled="false" 
accesslog-dir="logs/access" sso-enabled="false" remote-filter-enabled="false" 
app-base="autodeploy" auto-deploy="true"> 
     <sso/> 
     <remote-filter/> 
  </virtual-host> 
/*通道配置，包括http-listener 和ajp-listener 通道*/ 
  <http-listener name="tong-http-listener" port="8088" io-mode="nio2" redirect-port="8443" 
uri-encoding="GBK" parse-body-methods="POST" default-virtual-host="server" 
create-time="2020-06-29 10:33:30"> 
  <ssl/> 
 
 
  <protocol not-allow-HTTP-methods="TRACE,OPTIONS,HEAD,CONNECT,DELETE" max-threads="200" 
min-spare-threads="10"/> 
     <http-options compression="off"/> 
     <advance/> 
     <property name="server" value="webserver"/> 
  </http-listener> 
</web-container> 
/*安全域配置*/ 
 <security-service> 
    <auth-realm name="defaultRealm" type="File"> 
        <property name="UsersFile" value="twusers.properties"/> 
        <property name="GroupsFile" value="twgroups.properties"/> 
    </auth-realm> 
 </security-service> 
/*添加数据源的位置，默认不带*/ 
  <jdbc-connection-pool name="testdb" jdbc-driver="oracle.jdbc.driver.OracleDriver" 
jdbc-url="jdbc:oracle:thin:@168.1.55.34:1521:xe" user-name="S7nzfWMRpY4rGeIteDQMyw==" 
password="S7nzfWMRpY4rGeIteDQMyw=="/> 
  <jmx-service port="7200" address="127.0.0.1" protocol="rmi"/> 
/*日志相关配置*/ 


## 第 14 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
7 
<log-service file="${tongweb.root}/logs/server.log" rotation-limit="50 MB" 
rotation-timelimit="0" rotation-file-count="20" rotation-by-day="false" 
log-format="[%d{yyyy-MM-dd HH:mm:ss}] [%p] [%c] [%m]%n" rotation="true" verbose="true"> 
      <module-log-levels web-container="INFO" jta="INFO" data-source="INFO" naming="INFO" 
deployment="INFO" core="INFO" security="INFO" rmi-service="INFO" systemout="INFO" 
other="INFO"/> 
      <async-logger-config asynclogger-waitstrategy="Sleep" 
asynclogger-ringbuffersize="1024"/> 
  </log-service> 
/*sql日志保存路径*/ 
    <log-save-path sql-log-path="logs" audit-log-path="logs/audit-log" 
persistence-log-path="persistence"/> 
/*压缩日志配置*/ 
    <compress-log-service compress-enabled="false,false" 
log-dir="${tongweb.root}/logs,${tongweb.root}/logs/access" compress-obj="1,2" 
rotation-time="1,1" execution-time="1,1"/> 
/*snmp服务配置*/ 
     <snmp-service enabled="false" port="161" address="0.0.0.0" version="3" 
transportType="udp" engineID="62:a0:c1:81:11:c3:17:33" securityName="public" 
authKey="nmsAuthKey" privKey="myDesPriviateKey"/> 
    </server> 
</tongweb> 
说明： 
1. 停止端口默认和jmx端口共用7200，如需单独使用停止端口，须将7200端口的jmx协议由“rmi”改
为“mp”协议 
<jmx-service port="7200" address="127.0.0.1" protocol="mp"/> 
2. 在添加数据时，用户密码需要通过password.bat脚本加密后放入tongweb.xml中 
3.4 tongweb-web.xml配置说明 
tongweb-web.xml配置文件说明如下： 
<?xml version="1.0" encoding="UTF-8"?> 
<tongweb-web-app> 
       <property /> 
       <context-root >webtest1</context-root> 
        ……………………………… 
</tongweb-web-app> 
 
表 3.4-1：tongweb-web.xml配置项 
元素/属性名 
说明 
property  
web应用其它可配的属性 
context-root 
Web应用访问前缀，该值可能被部署Web应用时的"应用前缀"属性覆盖。如
<context-root>webtest1</context-root> 


## 第 15 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
8 
security-role-mappin
g  
把角色映射到当前安全域中的用户或组。最多配置一个。如： 
<security-role-mapping> 
        <role-name>tongweb</role-name> 
        <principal-name>admin:twnt</principal-name> 
  </security-role-mapping> 
role-name  
被映射的角色名称，根据用户名或者用户所在组进行映射。 
角色名(唯一)，对应JavaEE标准部署描述符文件中的security-role元素 
principal-name  
拥有该角色的用户名，如果有group-name，用户名可以写0个或者多个，如果没有
group-name，用户名至少要有1个 
注意：在没有group-name时，只有principal-name设置的用户名可以通过安全认
证，需要配置多个用户名时，用冒号分隔。 
group-name  
拥有该角色的组名，如果有principal-name，组名可以写0个或者多个，如果没有
principal-name，组名至少要有1个。 
注意：当应用绑定的安全域的分配组和应用中的group-name设置的组相同，则应
用绑定的安全域中的所有用户都可以通过安全认证。需要配置多个组名时用冒号
分隔。 
resource-links 
 
用于指定对外部资源引用的声明，最多配置一个，包含0个或多个resource-link
元素；如： 
<resource-links> 
    <resource-link name="web_name" global="server_datasource" 
type="javax.sql.DataSource"/ 
    </resource-links> 
name 
被创建的资源连接的名称，相对于java:comp/env上下文。 
global 
在全局的jndi上下文中，连接的全局资源的名称。 
type 
资源类型，全类名。如：java.lang.Integer 
loader 
配置Web应用用来加载资源的类加载方式，最多配置一个： 
<loader delegate="false" search-external-first="true" 
external-classpath="/xx/lib/*.jar;/xx/res/static"/> 
delegate 
当为true时，加载类时采用的是双亲委托机制，即先从父类加载器加载类，依次
递归，如果父类加载器可以完成类加载任务，就成功返回；只有父类加载器无法
完成此加载任务时，才由加载web应用的类加载器从web应用中查找和加载类。为
false时，反之。默认false。 
search-external-firs
t 
当true时，首先从external-classpath配置的路径寻找资源。false时，从
classload加载。默认false。 
external-classpath 
该属性可以配置目录或者jar的路径。为目录时，首先在该目录下寻找class进行
加载；为jar时，将首先在该jar中寻找class进行加载，同时支持*.jar格式，即
首先在上级目录下的所有jar中寻找；目录或者jar不存在时自动跳过，多个路径
使用分号分隔。 
watched-resource 
监视web应用的静态资源，如果被监视的资源有更新，则重部署应用。 
可以包含一个或多个property元素。以下的name和value为property的属性，例如：


## 第 16 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
9 
<property name="web" value="WEB-INF/web.xml"> 
<watched-resource> 
    <property name="web" value=" WEB-INF/web.xml"/> 
    </watched-resource> 
name 
任意有意义的名称。 
Value 
要监视的资源的物理路径。 
Listeners 
该listener用于监听Context组件(即当前应用)的事件。通过这个listener，可以
实现在监听到Context的事件(例如应用启动前后，应用卸载等)发生时执行用户自
定义的逻辑。可以包含0个或多个listener元素。以下的name和class-name为
listener的属性，如： 
<listeners> 
    <listener name="demo_listener" 
class-name="com.tongweb.tw.WebAppEventListernerDemo"/> 
    </listeners> 
name 
名称任意有意义的名称 
class-name 
为一个实现了com.tongweb.web.thor.LifecycleListener接口的类。 
jar-scanner 
它用于扫描web应用程序的jar文件。如: 
<jar-scanner scan-all-directories="true" scan-all-files="false" 
scan-class-path="true"/> 
scan-all-directories 默认false。如果为true，到类加载路径下的所有目录去判断其是否是展开的jar
文件。 
scan-all-files 
默认false。如果是true，检查所有的在类加载路径下的文件是不是jar文件，而
不仅仅是.jar结尾的文件。 
scan-class-path 
默认false。如果为true，除了web应用，所有的其他的类加载路径都会被扫描，
以加载jar文件。 
manager 
设置session管理器的实现类名，session管理器是web容器用来创建、维持Web应
用的HTTP Session的组件，最多可以设置一个。如： 
<manager max-active-sessions="-1" max-inactive-interval="30" 
session-id-length="5"/> 
distributable 
当为true时，所有的session属性必须实现序列化。默认为false。 
max-active-sessions 
最大活跃session数，-1（默认）表示无限制。 
max-inactive-interva
l 
会话超时时间，默认为30分钟 
session-id-length 
session id的长度，默认为16。 
session  
应用中Session相关的属性设置，如： 
<session> 
   <cookie-properties> 
    <property name="cookieName" value="NEW_JSESSIONID" /> 
    </cookie-properties> 


## 第 17 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
10 
 </session> 
cookie-properties 
设置Session Cookie相关属性，包括Session Cookie的名字，如果不设置这个属
性，将使用默认值：JSESSIONID。 
以下为共享库依赖配置。 
元素/属性名 
说明 
sharedlib-config 
共享库配置的顶级元素，最多可以设置一个。例如： 
<sharedlib-config> 
 
 
<shared-lib-relation/> 
 
 
<app-exclude/> 
</sharedlib-config> 
shared-lib-relation 
关联共享库的Group，最多可以设置一个。例如： 
<shared-lib-relation> 
 
<shared-lib-ref name="springlibs1"/> 
 
<shared-lib-ref name="springlibs2"/> 
</shared-lib-relation> 
shared-lib-ref 
使用name指定已配置好的共享库名称，需要先在控制台配置。此标签可多个。如
果当前name指定的共享库不存在，则忽略此条配置。例如： 
<shared-lib-ref name="springlibs1"> 
 
<exclude-jar> 
 
 
<path>/home/userlib/service.jar</path> 
 
</exclude-jar> 
</shared-lib-ref> 
注：path为绝对路径，可以查看${TongWeb_HOME}/conf/assets.xml里面路径。 
exclude-jar 
配置当前关联的共享库中要排除的jar包。子标签path指定包的绝对位置。可为空。 
app-exclude 
配置排除当前应用自带的jar包，最多可以设置一个。即排除lib/xx.jar。子标签
path指定包的全名称。可为空。 
例如： 
<app-exclude> 
 
<path>aopalliance-1.0.jar</path> 
 
<path>commons-digester-2.1.jar</path> 
</app-exclude> 
 
 


## 第 18 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
11 
第4章 应用管理 
4.1 自动部署配置 
TongWeb轻量级支持文件和目录方式的自动部署。${TongWeb_HOME}/autodeploy是TongWeb的默认自动部
署目录，将应用拷贝到自动部署目录下即可部署应用，把应用从自动部署目录下删除即可解部署应用。 
自动部署配置在${TongWeb_HOME}/conf/tongweb.xml 的<autodeploy>节点中，各配置项说明如下： 
表 4.1-1：自动部署配置项 
配置项名称 
说明 
默认值 
enabled 
自动部署：是否开启自动部署功能 
true 
jsp-compile jsp预编译：是否开启jsp预编译功能，当开启时，会
在部署时对jsp进行编译，应用部署完成后，jsp不会
在请求访问时在进行编译。 
false 
dir 
自动部署目录：TongWeb应用服务器自动对该目录下的
目录和文件进行部署和解部署。 
${tongweb.root}/autodep
loy 
check-inter
val 
自动部署轮询时间间隔：TongWeb检查自动部署目录的
时间间隔，单位：毫秒。 
3000 
                        
4.2 热部署 
热部署同样是应用部署的一种方式，其主要的作用是在应用已经部署后，需要在线实时对应用进行修
改，结果立刻展现的一种方式。 
热部署的配置项在${TongWeb_HOME}/conf/tongweb.xml 的<hot-deploy>节点中，各配置项说明如下： 
表 4.2-1：热部署配置项 
配置项名称 
说明 
默认值 
enabled 
热部署：是否开启热部署功能 
false 
watched-resource 
监听资源：这里配置的静态资源会
被自动部署器监控用于更新和重
新加载应用 
WEB-INF/web.xml，
MATA-INF/application.xml 


## 第 19 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
12 
第5章 Web容器 
5.1 容器说明 
在Java EE平台上，Web应用运行在Web容器中。Web容器提供了Web应用运行时的环境，包括生命周期管
理、安全、请求转发等。同时Web容器为Web应用提供访问其他API的能力，如命名服务。 
   Web应用通过XML格式的部署描述文件来定义自身的行为。 
   一个容器可以同时运行多个 Web 应用，它们一般通过不同的 URI 来进行区分和访问，如：
http://host:port/contextroot/servletname   
说明： 
http(或https)://虚拟主机名或别名:虚拟主机关联的通道的监听端口/虚拟主机上部署应用的访问前
缀/应用中的Servlet名 
5.2 容器配置 
容器配置里的属性，是对所有Web应用的通用属性。 
容器配置的配置项在${TongWeb_HOME}/conf/tongweb.xml的<server>/<web-container>节点中，各配
置项说明如下： 
表 5.2-1：web容器配置项 
配置项名称 
说明 
默认值 
jvm-route 
在使用session亲和的负载均衡场景中需要设置的
TongWeb标识符。该标识符在集群中必须是唯一的。
会附加到生成的sessionID中 
无 
jsp-development 
JSP开发模式：是否启动JSP开发模式 
true 
parameter-encoding 
请求参数字符集：用于对URL请求进行解码的字符集 GBK 
response-encoding 
响应参数字符集：用户对URL 响应进行解码的字符
集 
GBK 
session-timeout 
Session超时时间，单位：秒 
30 
hung-thread-threshold 
超时线程的阈值： 0表示不开启超时线程检测，大
于0表示开启；单位：描述 
0 
hostnameVerifier 
主机名验证器：客户端应用程序访问应用服务器时，
即url.openConnection()，是否利用验证器验证，
分为“无”、“TW主机名验证器”和“自定义主机
名验证器”。 
1.无主机名验证器
hostnameVerifier="NullHostnameVerifier"； 
2.TW主机名验证器 
hostnameVerifier ="TWHostnameVerifier"； 
3.自定义的验证器类必须实现jdk的接口
HostnameVerifier，并且打成jar包，放入启动工程
的lib目录中，自定义主机名验证配置为：
hostnameVerifier="CustomerHostnameVerifier:c
NullHostnameVerifier 


## 第 20 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
13 
om.test.myHostVerifier", 其中 
“com.test.myHostVerifier”为自定义验证器的
类名。 
property属性 
说明 
默认值 
complete.message.timeout.se
conds 
http慢请求检测：服务器接收一个完整的http请求
时间，超过该值，则表示慢请求。当值大于0时，则
开启慢请求检测；值为0时，则不开启。 
0 
max.attack.times 
慢攻击容忍次数：服务器容忍客户端慢请求攻击的
次数，超过该配置，则将客户端IP加入黑名单，服
务器不在接收来自该IP的请求 
3 
blacklist.expired.hourinter
rupt.current.connect 
黑名单移除时间：慢攻击客户端IP地址在服务器黑
名单中的移除时间，单位：小时 
12 
interrupt.current.connect 
中断当前连接：服务器中断当前慢攻击请求的 http
连接 
true 
xmlBlockExternal 
禁止引入外部xml文件 
false 
unloadDelay 
应用退休超时时间 
2 
addWebinfClassesResources 
启用META-INF/resources 
false 
sessionLog 
session复制日志 
false 
hostHeaderGuard 
防host头攻击：启动或关闭放host头（主机名）攻
击 
false 
hostHeaderGuardWhiteList 
主机名白名单：开启“防host头攻击”后，配置允
许通过的主机名列表，以逗号分隔 
无 
 
5.3 访问日志 
    记录访问Web应用时http请求的相关信息，包括请求的方法，请求的协议，请求头中的信息，请求响应
的状态码等，不包括Web应用本身输出的日志信息。 
1. 访问日志配置是每个Web 应用的通用配置； 
2. 访问日志开关在虚拟主机中配置； 
3. 默认的访问日志名，如：access_log.server.20.06.29.17.txt； 
4. 访问日志配置项在${TongWeb_HOME}/conf/tongweb.xml 的
<server>/<web-container>/<access-log>节点中，各配置项说明如下： 
表 5.3-1：访问日志配置项 
配置项名称 
说明 
默认值 
pattern 
记录访问日志时使用的格式，分为传统模式和扩展模式。
默认为传统模式；具体格式见下表。 
%{yyyyMMddHHmmssSS
S}t %U %m %a %D 
prefix 
生成的访问日志前缀 
access_log. 
suffix 
生成的访问日志后缀 
.txt 
rotatable 
是否启用访问日志轮转；开启后，将按照轮转策略对访
问日志进行轮转，分为按天和按小时轮转；按天轮转时，
file-date-format="yy.MM.dd"； 
按小时轮转为file-date-format="yy.MM.dd.HH"> 
true，按小时轮转 


## 第 21 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
14 
log-extend 
是否使用扩展日志格式；如果开启，pattern=“cs-method 
cs-uri-query c-ip s-ip time” 
false 
file-date-f
ormat 
文件日期格式：轮转开启后的访问日志命名后缀；“yy”
表示年，“MM”表示月，“dd”表示天，“HH”表示小
时。如默认产生的访问日志文件格式为：
access_log.server.yy.MM.dd.HH.txt。 
yy.MM.dd.HH 
  property
属性 
说明 
默认值 
maxNum 
每个虚拟主机下的访问日志最大个数，超过配置的个数，
最早日志文件将被删除，配置为-1或0，不生效。 
-1 
maxDays 
每个虚拟主机下的访问日志存活天数，超过配置的最大
天数，最早日志文件将被删除，配置为-1或0，不生效。 
-1 
 
⚫ 传统模式格式 
表 5.3-2：访问日志传统模式格式 
传统格式  
访问日志格式说明  
%a 
远程主机的IP地址。 
%A 
本地IP地址 
%b  
发送字节数，包含HTTP请求头，如果为0时其值为 '-'  
%B  
发送字节数，不包含HTTP请求头 
%h  
远程主机名（当该通道的enable-lookups属性为false时，返回IP地址） 
%H  
请求协议 
%l  
已认证的远程逻辑用户名，一般返回 '-' 
%m  
请求方法（GET, POST, 等等） 
%p  
接受该请求的本地端口 
%q  
请求参数，（以'? '开头） 
%r  
请求的第一行（请求方法以及request URI） 
%s  
HTTP 响应状态码 
%S  
用户的session ID  
%t  
日期和时间，使用 Common Log 格式 
%u  
认证的远程用户,没有则返回 '-'  
%U  
请求的URL路径 
%v  
本地server名称 
%D  
处理请求所有时间，单位为毫秒 
%T  
处理请求所有时间，单位为秒（seconds） 


## 第 22 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
15 
%I  
当前请求线程名 
说明：支持写入请求/响应头，cookies，session，请求属性与时间戳格式的信息 
% {xxx}i    请求头信息，xxx为请求头属性。 
%{xxx}o  
响应头信息。 
% {xxx}c  
cookies信息。 
%{xxx}r  
xxx为ServletRequest的属性。 
%{xxx}s  
xxx为HttpSession的属性。 
%{xxx}t 
xxx是一个加强的SimpleDateFormat 模式，支持所有的SimpleDateFormat格式，并且支
持额外的属性。 
⚫ 扩展模式 
扩展模式的访问日志其实并不是对原来访问日志的扩展，而是以不同的pattern 对请求响应进行记录。
从属性来看，它只少了个"locale"属性，以及pattern 采用不同的值。 
这里的pattern 是由一些格式符号组成，有一些符号须要一些额外的前缀。一般的前缀有： "c"表示
客户端即远程。"s"表示服务器端即本地，"cs"表示客户端到服务器端。"sc"表示服务器端到客户端。
"x"表示"application specific"。 
表 5.3-3：访问日志扩展模式格式 
扩展格式  
访问日志格式说明  
bytes  
发送字节, 不包括HTTP headers, 如果为零显示为'-'  
c-dns  
远程主机名（或者IP地址，如果连接器的enableLookups为false）  
c-ip  
远程（客户端）IP地址  
cs-method  请求方法 （GET, POST等） 
cs-uri  
请求的URL  
cs-uri-que
ry  
请求参数 （如果存在，以"?"开头）  
cs-uri-ste
m  
请求的URL路径 
date  
yyyy-mm-dd format格式的GMT日期 
s-dns  
本地主机名 
s-ip  
本机ip地址 
sc-status  响应状态 
time  
该请求的时间 
time-taken  从开始到结束，服务器在该请求上所花的时间（以秒为单位） 
x-threadna
me  
当前请求线程名 


## 第 23 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
16 
说明： 
也支持从headers cookies，context，request或session属性和request参数中获取信息 
cs(XXX) 
请求头 
sc(XXX)  
响应头 
x-A(XXX)  
servlet上下文属性 
x-C(XXX)  
具有专用名的首个cookie值。例如，要记录一个叫做JSESSIONID，则指定该属性为
x-C(JSESSIONID)。 
x-O(XXX)  
将所有名称为XXX的响应头串接 
x-P(XXX)  
请求参数 
x-R(XXX)  
request属性 
x-S(XXX)  
session属性 
cs(XXX) 
请求头 
sc(XXX)  
响应头 
x-A(XXX)  
servlet上下文属性 
x-C(XXX)  
具有专用名的首个cookie值。例如，要记录一个叫做JSESSIONID，则指定该属性为
x-C(JSESSIONID) 
x-O(XXX)  
将所有名称为XXX的响应头串接  
可以用x-H(XXX)表示HttpRequestServlet的方法。 
x-H(authType)  
x-H(characterEncoding)  
x-H(contentLength)  
x-H(locale)  
x-H(protocol)  
x-H(remoteUser)  
x-H(requestedSessionId)  
x-H(requestedSessionIdFromCookie)  
x-H(requestedSessionIdValid)  
x-H(scheme)  
x-H(secure)  
5.4 虚拟主机 
虚拟机主机是TongWeb应用服务器管理的一组主机名。将单个物理主机分成多个“虚拟”的主机，即虚
拟主机间可共享一台物理主机的资源。每个虚拟主机通过“虚拟主机的唯一标识(id)”来区分。 


## 第 24 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
17 
TongWeb服务器上一个Web应用可以部署在多个虚拟主机上，虚拟主机提供“启用/停用”开关，默认为
启用。如果为“启用”，则虚拟主机接收请求并进行处理，如果为“停用”或虚拟主机不存在，则虚拟主
机不接收请求(返回状态码404)。 
虚拟主机与通道之间是多对多的关系，即一个虚拟主机可以与多个通道关联，一个通道可以与多个虚
拟主机关联。 
在使用虚拟主机时，首先应该确认操作系统的hosts表中，是否正确的配置了虚拟主机名与IP地址的映
射，例如：admin  10.10.4.10。如果未配置主机名与IP地址的映射，则需要手工添加。要注意hosts表中
配置的主机名必须与配置虚拟主机时填写的“主机名”一致。访问格式为：
http://virtualServer:port/contextRoot，虚拟主机virtualServer和通道port关联。所谓关联，就是指
创建虚拟主机virtualServer时指定了通道port为访问通道。 
示例： 
<virtual-host name="server" listeners="tong-http-listener,testhttps,testajp" 
status="true" accesslog-enabled="true" accesslog-dir="logs/access" sso-enabled="false" 
remote-filter-enabled="true" app-base="autodeploy" auto-deploy="true"> 
      <remote-filter allow-addr="192.168.33.197" allow-host="tongtech" 
filter-host-type="allow" filter-addr-type="allow"/> 
 </virtual-host> 
1. 
虚拟主机配置项在${TongWeb_HOME}/conf/tongweb.xml 的<server>/<web-container>/< 
virtual-host>节点中，各配置项说明如下： 
表 5.4-1：虚拟主机配置项 
配置项名称 
说明 
默认值 
name 
虚拟主机唯一名称 
server 
alias 
虚拟主机别名，可以定义多个别名，用逗号分隔 
 
status 
虚拟主机启动或停止的开关 
true 
listeners 
通道列表，与虚拟主机关联的通道，如存在多个通道，
以逗号分隔 
tong-http-li
stener 
accesslog-enabled 
虚拟主机的访问日志开关 
false 
accesslog-dir 
访问日志目录，如为相对目录，则相对 ${TongWeb_HOME} logs/access 
sso-enabled 
单点登录：单点登录功能是根据应用使用的安全域进行
匹配的，如关闭单点登录，则用户访问部署在同一虚拟
主机上的使用相同安全域的不同应用，需要分别认证。
如果开启单点登陆功能，用户只需认证一次就可以访问
部署在该虚拟主机上所有使用相同安全域的Web应用。 
false 
addValve 
自定义valve的类名，自定义的valve必须实现
com.tongweb.catalina.Valve接口，会添加到虚拟主机
的pipeline(valve链)里，访问应用时执行自定义的操
作。如果要为该valve属性设值，可以在类名后面用“,”
间隔进行追加，例如
com.tongweb.catalina.valves.RemoteIpValve, 
protocolHeader=X-Forwarded-Proto，则为
RemoteIpValve的对象属性“protocolHeader”设值为字
符串“X-Forwarded-Proto” 
 


## 第 25 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
18 
remote-filter-enabl
ed 
远程过滤：对允许访问的远程主机或ip进行过滤。 
false 
 
2. 
开启remote-filter-enabled=true 后，远程过滤功能的配置项在${TongWeb_HOME}/conf/tongweb.xml
的<server>/<web-container>/<virtual-host>/ <remote-filter>节点中，各配置项说明如下： 
表 5.4-2：远程过滤配置项 
配置项名称 
说明 
默认值 
filter-addr-type 
允许访问的ip地址,允许：“allow”；禁用："deny"” 
allow 
filter-host-type 
允许访问的虚拟主机，允许：“allow”；禁用："deny"” 
allow 
allow-host 
允许访问的虚拟主机名：可以是具体的正则表达式或具体的主机
名 
无 
allow-addr 
允许访问的IP地址：可以是正则表达式或具体的IP地址 
无 
deny-addr 
禁止访问的IP地址：可以是正则表达式或具体的IP地址 
无 
deny-host 
禁止访问的虚拟主机名：可以是具体的正则表达式或具体的主机
名 
无 
 
5.5 通道 
5.5.1 HTTP通道 
Web容器使用通道接收用户请求(每个通道提供自己的监听地址和监听端口)，TongWeb默认提供
tong-http-listener的HTTP监听器来监听用户请求，默认的端口号为8088，部署在轻量级上的Web应用访问
URL为：http://IP:8088/，加上web应用指定的上下文路径，访问Web应用。 
/*http通道示例*/ 
<http-listener name="tong-http-listener" port="8088" io-mode="nio2" 
redirect-port="8443" uri-encoding="GBK" parse-body-methods="POST" 
default-virtual-host="server" create-time="2019-10-29 10:54:11> 
                <ssl/> 
                <protocol not-allow-HTTP-methods="TRACE,OPTIONS,HEAD,CONNECT,DELETE" 
max-threads="200" min-spare-threads="10"/> 
                <http-options compression="off"/> 
                <advance/> 
                <property name="server" value="webserver"/> 
            </http-listener> 
/*https双向认证通道示例*/ 
<http-listener name="testhttps" port="8888" address="0.0.0.0" io-mode="nio" 
ssl-enabled="true" use-body-encoding-for-uri="false" max-post-size="2097152" 
parse-body-methods="GET,POST" default-virtual-host="server" > 
                <alias="server" keystore-file="conf/server.keystore" 
keystore-pass="vVm6OyRRxhs3QGlTnzcKGA==" keystore-type="JKS" client-auth="true" 
ssl-protocol="TLS" truststore-file="conf/server.keystore" 


## 第 26 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
19 
truststore-pass="vVm6OyRRxhs3QGlTnzcKGA==" truststore-type="JKS"/> 
                <protocol async-timeout="10000" backlog="100" 
connection-timeout="60000" keep-alive-timeout="60000" max-threads="200" 
min-spare-threads="10" processor-cache="200" tcp-no-delay="true" > 
                    <property name="threadPriority" value="5"/> 
                </protocol> 
                <http-options disable-upload-timeout="true" 
max-keep-alive-requests="100"/> 
                <advance oom-parachute="1048576"/> 
                <property name="enableRC4" value="false"/> 
            </http-listener> 
1. HTTP 通道的配置项在${TongWeb_HOME}/conf/tongweb.xml 的
<server>/<web-container>/<http-listener>节点中，各配置项说明如下： 
表 5.5-1：HTTP通道配置项 
配置项名称 
说明 
默认值 
name 
监听器的名称 
tong-http-
listener 
status 
通道的状态：当状态为started时，允许通道接收用户请求；
状态为stopped时，该通道不接收用户请求 
started 
address 
监听器监听地址：监听服务器上所有IP地址输入0.0.0.0，否
则输入服务器有效的IP地址或主机名 
0.0.0.0 
port 
监听器监听端口 
8088 
ssl-enabled 
表示是否使用SSL协议 
false 
io-mode 
通道使用的io模式：bio、nio、nio2 
nio2 
http2-enabled 
http2协议:在io模式为apr时，该选项只有在开启openssl选项
下才可选择 
false 
redirect-port 
重定向端口：客户端通过HTTP端口访问SSL的资源，则服务器
会将请求重定向到启用的SSL端口上，即设置的重定向端口。 
8443 
proxy-url 
代理服务器名和端口组成的URL为
http(s)://proxyName:proxyPort  
无 
use-body-encodin
g-for-uri 
如果contentType中指定了编码规范，则可以不使用
URIEncoding 
false 
max-parameter-co
unt 
被容器自动解析的参数/值对（GET&POST）的最大值。参数/值
对超出这个范围，超出的部分将被忽略，单位：个 
10000 
max-post-size 
Form表单使用Post方法时可提交的最大字节数。 
2097152
（2M） 
uri-encoding 
对请求URL进行编码的字符集。 
GBK 
parse-body-metho
ds 
以逗号分隔的HTTP方法列表，通过方法列表，等同于POST方法，
request 正文将被解析成请求参数。 
POST 
default-virtual-
host 
此通道对应的虚拟主机 
server 
property 
说明 
默认值 


## 第 27 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
20 
name 
http响应的server 头 
webserver 
enabledProtocols 
https采用的SSL协议版本 
无 
enableRC4 
是否开启用户加密算法 
false 
ciphers 
SSL&TLS Ciphers用户指定加密算法，用逗号分开功能优先与
RC4加密算法设置 
无 
 
2. 当ssl-enabled=true 时，需要对SSL 进行配置。在${TongWeb_HOME}/conf/tongweb.xml 的
<server>/<web-container>/<http-listener>/<ssl>节点中，各配置项说明如下： 
表 5.5-2：SSL配置项 
配置项名称 
说明 
默认值 
keystore-file 
秘钥库路径，支持绝对路径和相对路径；默认为当前根目录
的相对路径 
conf/server.
keystore 
keystore-pass 
秘钥库密码:自带的server.keystore证书密码；
${TongWeb_HOME}/bin目录下提供password工具来把明文转
换成加密后的密码 
changeit 
keystore-type 
秘钥库类型：自带的server.keystore证书类型 
JKS 
client-auth 
是否开启客户端认证 
false 
ssl-protocol 
设置使用的SSL协议，从JVM的文档中查看创建SSLContext对
象时，可以使用的算法的值 
TLS 
truststore-file 信任证书路径，支持绝对路径和相对路径；默认为当前根目
录的相对路径 
conf/server.
keystore 
truststore-pass 信任证书密码：自带的server.keystore证书密码 
changeit 
truststore-type 信任证书类型：自带的server.keystore证书类型 
JKS 
 
3. protocol 配置项在${TongWeb_HOME}/conf/tongweb.xml 的
<server>/<web-container>/<http-listener>/<protocol>节点中，各配置项说明如下： 
表 5.5-3：protocol配置项 
配置项名称 
说明 
默认值 
not-allow-HTTP-meth
ods 
要禁用的http请求的方法 
TRACE,OPTIONS, 
HEAD,CONNECT,DELETE 
async-timeout 
Servlet中的异步请求超时，单位：毫秒 
10000 
enable-lookups 
DNS反向查找；但设置为true时，可以调用
request.getRemoteHost去执行DNS lookups以
返回远程客户端的真实host name 
false 
max-header-count 
容器允许的最大请求头个数。当请求中包含头字
段个数大于该值时，请求会被拒绝，单位：个 
100 
use-ipv-hosts 
基于ip的虚拟主机 
false 
xpowered-by 
是否在reponse的http响应头里生成
X-Powered-By信息 
false 
backlog 
指定所有可以使用的处理请求的线程数都被使
100 


## 第 28 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
21 
用时，可以放到处理队列中的排队请求数，超过
这个数的请求将被拒绝。单位：个 
accept-thread-count 用于接受连接的线程数。当有大量短连接或使用
多CPU的机器时，都需要增大该值，一般情况下，
真正使用的不会超过2个。配置最大值不要超过
4。单位：个 
1 
connection-timeout 
Socket网络连接超时时间；单位：毫秒 
6000 
keep-alive-timeout 
长连接的超时时间；单位：毫秒 
6000 
max-threads 
通道可创建的最大线程数，当连接超过了最大连
接数，之后的连接不被处理；  
200 
min-spare-threads 
最小备用线程数，即初始化时创建的线程数 
10 
processor-cache 
该设置用于设置缓存对象的个数 
200 
max-connections 
在任何给定的时间服务器接受并处理的最大连
接数。当这个数字已经达到了，服务器将不会接
受任何连接，直到连接的数量降到低于此值。基
于acceptCount的设置，操作系统可能仍然接受
连接。 
10000 
property 
说明 
默认值 
threadPriority 
线程优先级基本，输入范围为1-5 
5 
 
4. http-options 配置项在${TongWeb_HOME}/conf/tongweb.xml 的
<server>/<web-container>/<http-listener>/<http-options>节点中，各配置项说明如下： 
表 5.5-4：http-options配置项 
配置项名称 
说明 
默认值 
compression 
压缩开关：开启后可以节省带宽；复制分别为（on:启用
压缩数据；off:禁用压缩数据；force:在所有情况下强制
压缩数据） 
off 
compressable-mime-t
ype 
用户http压缩的MIME类型 
text/html, 
text/xml, 
text/plain 
compression-min-siz
e 
启用传输压缩的内容最小值， 
单位：K 
2048 
disable-upload-time
out 
是否为数据上传指定更长的连接超时时间 
true 
max-http-header-siz
e 
http请求与请求头的最大值， 
单位为：字节 
8192 
max-keep-alive-requ
ests 
HTTP请求最大长连接个数。将此属性设置为1，将禁用
HTTP/1.0、以及HTTP/1.1的长连接。设置为-1，不禁用 
100 
 
5. advance 的配置项在${TongWeb_HOME}conf/tongweb.xml 的
<server>/<web-container>/<http-listener>/<advance>节点中，各配置项说明如下： 


## 第 29 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
22 
表 5.5-5：advance配置项 
配置项名称 
说明 
默认值 
disable-keep
-alive-perce
ntage 
为提高可扩展性，在长连接失效之前被使用的处理线程的百分比。小
于0的值将被设为0，大于100的值将被设为100 
75% 
selector-tim
eout 
选择轮询器selector的超时时间，这个值非常重要，因为连接清理工
作也是在同一个线程里，所以不要将此值设置的太高。单位：毫秒。 
1000 
usecomet 
是否允许使用Comet servle 
true 
use-sendfile 
使用此属性来启用或禁用sendfile的能力 
true 
oom-parachut
e 
java堆内存溢出时可以释放空间；单位：bytes 
1048576 
 
5.5.2 AJP通道 
和HTTP通道的工作方式一样，AJP通道同样能够接收请求，并返回处理结果。只不过它们使用AJP协议
代替HTTP。通常用于允许负载均衡器和TongWeb服务器直接进行通信。 
<ajp-listener name="testajp" address="0.0.0.0" port="5555" redirect-port="443" 
use-body-encoding-for-uri="false" > 
                <protocol async-timeout="10000" backlog="100" 
connection-timeout="60000" keep-alive-timeout="60000" max-threads="200" 
min-spare-threads="10" processor-cache="200" tcp-no-delay="true" self-tuned="false"> 
                    <property name="threadPriority" value="5"/> 
                </protocol> 
                <ajp-options require-secret="tw123" packet-size="8192"/> 
            </ajp-listener> 
AJP通道的配置项在${TongWeb_HOME}/conf/tongweb.xml的
<server>/<web-container>/<ajp-listener>节点中，各配置项基本与HTTP通道的一致，单独对以下标签中
属性说明如下： 
表 5.5-6：AJP通道配置项 
ajp-options 
配置项名称 
说明 
默认值 
require-secret 
负载均衡器发送的请求中包含了指定的secret keyword（加密关
键字），请求才会被应用服务器接收，否则返回403（访问拒绝）。
要使用此功能，需要在负载均衡器中配置与此相关的属性，且其
值与此处的require-secret的值相同。 
例如负载均衡器为apache，可以在其worker.proerpties文件中设
置“secret”属性（这个属性的值就是所谓的secret keyword），
设置其值与此处的配置相同即可。 
无 
packet-size 
ajp packet的最大值，byte类型。应该与mod_jk的
max_packet_size的值相同，默认8192。如果设的值小于8192，则
采用默认值。单位：bytes 
8192 


## 第 30 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
23 
 
5.6 虚拟目录 
TongWeb应用服务器中支持虚拟目录，应用中的JSP、html和静态资源可以在放在虚拟目录中（本地任
意目录），该功能仅限JSP、HTML和静态资源，JSP引用的class需要在应用的类路径下。 
JSP、HTML 和静态资源的加载优先级： 
⚫ 
war 中不存在，虚拟目录下存在，用的是虚拟目录下的； 
⚫ 
war 中存在，虚拟目录下不存在，用war 中的； 
⚫ 
war 包和虚拟目录下都存在并且同名的话，用的是虚拟目录下的文件； 
使用方式： 
⚫ 
在tongweb-web.xml 文件的根节点下加入如下内容： 
<property name="aliases" value="/aliasPath1=docBase1,/aliasPath2=docBase2"/> 
⚫ 
如果应用前缀为“/”，则配置如下： 
<property name="aliases" value="/ =D:\virtualdir"> 
⚫ 
说明：aliasPath1 指http 请求URL 中该资源的访问路径；docBase1 是资源所在的绝对目录。如
果有多个虚拟目录需要指定，将多个/aliasPathN=docBaseN 用逗号隔开即可。示例： 
<?xml version="1.0" encoding="UTF-8"?> 
<tongweb-web-app> 
   <property name="aliases" 
value="/images=D:\Work\vdir\images,/script=D:\Work\vdir\script,/pages=D:\Work\vdir\pages,/css=D
:\Work\vdir\css"/> 
</tongweb-web-app> 
比如某应用的静态图片的访问url为http://ip:port/appname/images/code.gif，那么其虚拟目录可以
配置为/images=D:\Work\vdir\images，其中/images是请求URL中该资源的访问路径，D:\Work\vdir\images
是存放该资源的绝对路径。同理/script下可以放置js资源，/pages下可以放置jsp资源，/css下可以放置
css文件。 
 


## 第 31 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
24 
5.7 JDBC配置 
5.7.1 JDBC数据源 
JDBC数据源的主要功能是为应用程序提供数据库连接。JDBC数据源基于数据库连接池技术，因此连接
复用便是JDBC数据源的基本功能。每个JDBC数据源使用一个连接池，维护一定数量的连接。连接池预先建
立多个数据库连接对象，然后将连接对象保存到连接池中，当客户请求到来时，从池中取出一个连接对象
为客户服务，当请求完成时，客户程序调用close()方法将连接对象放回池中。 
5.7.2 JDBC数据源配置 
TongWeb提供了jdbc数据源的的配置，为应用提供了连接数据库的方法。 
1. 将数据源驱动程序放到${TongWeb_HOME}/lib 目录下。 
2. 数据源配置项在${TongWeb_HOME}/conf/tongweb.xml 的<server>/<jdbc-connection-pool>节点中，
各配置项说明如下： 
<jdbc-connection-pool name="testdb" jdbc-driver="oracle.jdbc.driver.OracleDriver" 
jdbc-url="jdbc:oracle:thin:@168.1.55.34:1521:xe" 
user-name="S7nzfWMRpY4rGeIteDQMyw==" password="S7nzfWMRpY4rGeIteDQMyw=="/> 
 
表 5.7-1：数据源连接池基本配置项 
配置项名称 
说明 
默认值 
name 
JDBC的jndi唯一名称 
无 
is-multi 
是否是多数据源连接池 
false 
is-xa 
是否是XA数据源 
false 
dataSourceC
reator 
非XA数据源，dataSourceCreator=“lite”,XA数据源不需要配置 
lite 
jdbc-driver 
数据库驱动类名 
无 
jdbc-url 
连接数据库的url，如果有&要加转义字符，如
jdbc:mysql://168.1.13.108:3316/zhuhq?useUnicode=true&amp;cha
racterEncoding=UTF8 
无 
user-name 
连接数据库所需要的用户名,需通过${TongWeb_HOME}/bin目录下提供
password工具来把明文转换成加密后的用户名 
无 
password 
连接数据库用户名的密码，需通过${TongWeb_HOME}/bin目录下提供
password工具来把明文转换成加密后的密码 
无 
class-path 
数据库驱动包所在的路径；如果lib下已放入驱动包，则该项不需要配
置 
无 
connection-
properties 
连接属性：当用Driver建立新连接时被发送给JDBC 驱动的连接参数，
格式必须是propertyName=property，多个之间以分号分割 
无 
 


## 第 32 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
25 
表 5.7-2：连接池池配置项 
配置项名称 
说明 
默认值 
initial-siz
e 
初始连接数：首次创建池或应用服务器初始启动时，数据库连接池里
创建的连接数；单位：个 
10 
max-active 
最大连接数：连接池允许创建的最大连接数；单位：个 
10 
min-idle 
最小空闲连接数，单位：个 
10 
max-wait-ti
me 
当没有可用连接时, 连接池等待连接被归还的最大时间, 超时则抛出
异常；单位：毫秒 
30000 
 
表 5.7-3：连接池验证连接配置项 
配置项名称 
说明 
默认值 
validation-query 
用于测试连接数据库的SQL语句 
无 
test-on-borrow 
获取连接时验证 
false 
test-on-connect 
是否创建连接时验证 
false 
test-on-return 
是否返回连接时验证 
false 
test-while-idle 
是否对空闲连接进行校验；如果设置为true，那么会根据验证
间隔时间来进行验证 
false 
validation-query-t
imeout 
验证超时：测试连接活动的最长时间；单位：秒 
5 
validation-interva
l 
连接验证时间间隔；单位为毫秒 
30000 
 
表 5.7-4：连接池高级属性配置项 
配置项名称 
说明 
默认值 
default-auto-commit 自动提交：连接池创建连接的默认的auto-commit 状
态 
true 
Jta-managed 
是否使用jta事务的开关,取值为 
true 
commit-on-return 
连接返回时提交，不选则默认回滚 
false 
rollback-on-return 
默认回滚 
true 
assoc-with-thread 
线程连接关联 
false 
test-while-idle 
空闲回收：标记是否删除空闲时的连接 
false 
min-evictable-idle-
time 
空闲超时：当连接池中存在空闲的连接数大于连接池
的最小连接数时，服务器以用户配置的"检查连接的周
期"时间为周期对连接池中的空闲连接进行检查，主要
检查空闲连接是否超时。单位：毫秒 
60000 
time-between-evicti
on-runs 
检查连接的周期，单位：毫秒 
60000 
remove-abandoned 
泄露回收：如果发现泄露超时，则将连接丢弃 
false 
remove-abandoned-ti
meout 
泄露超时时间：在这段时间内跟踪连接池中的连接泄
漏，以WARNING级别将该堆栈信息输出到日志。以秒为
单位。默认值为0，表示已禁用连接泄漏跟踪；单位：
秒 
2 


## 第 33 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
26 
配置项名称 
说明 
默认值 
log-abandoned 
丢弃连接时的打印日志：如果设为true,在丢弃泄露连
接的时候打印日志 
false 
max-age 
连接最大寿命：保持连接的最大毫秒数。当一个连接
被归还时，如果自连接被创建到当前时间的时间差大
于该值，连接将被关闭而不是回到池中。允许范围是
30000-2147483647范围内的整数 
1800000 
jdbc-interceptors 
1.开启sql日志，配置如下：
jdbc-interceptors="StatusMonitor; 
ThorSlowQueryReport(threshold=1000)"； 
threshold=1000为sql执行过滤时间，单位为秒，默认
值1000； 
2.开启语句缓存，如下：StatementCache 
(prepared=true,callable=false,max=11)；
prepared=true是开启PreparedStatement语句缓存；
callable是开启CallableStatement语句缓存；max=11
表示语句最大缓存数 
3.开启语句跟踪，如下：StatementFinalizer 
4.配置语句超时，如下：
QueryTimeoutInterceptor(queryTimeout=0)，默认值
为0 
StatusMonito
r; 
QueryTimeout
Interceptor(
queryTimeout
=0) 
assoc-with-thread 
用户线程与数据库连接绑定（若希望数据库连接不上
释放连接则需要开启获取连接时验证），用户线程被
GC才释放连接。取值为true/false 
false 
leakCheck 
即时泄露回收：数据源连接回收功能，与数据源自身
的泄露回收功能相比，该功能在每次请求结束后都进
行回收，回收效率更高。一般情况下，没有主动关闭
连接的应用很大概率也没有主动关闭Statement，此时
需要配合数据源的语句跟踪功能一起使用,取值为
true/false 
false 
fair-queue 
公平锁配置。公平锁是指多个线程按照申请锁的顺序
去获得锁，线程会直接进入队列去排队，永远都是队
列的第一位才能得到锁。非公平锁是指在多个线程获
取锁时，会直接尝试获取，若获取不到，再去进入等
待队列，若能获取到，就直接获取到锁。 
true 
 


## 第 34 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
27 
第6章 安全服务 
6.1 概述 
安全服务用于对数据进行保护：在存储和传输数据时，防止对数据进行未经授权的访问。认证是一种
实体（用户、应用程序或组件）用来确定另一个实体是否是其声明的实体的方法，实体使用安全凭证对其
自身进行验证。授权是确定使用凭证的实体是否有权对所访问的资源进行操作的方法。 
6.2 安全域类型 
安全域是服务器定义和强制执行通用安全策略的范围，是存储用户和组信息及其关联的安全凭证的系统
信息库。服务器支持六种类型的安全域： 
• 
文件安全域：服务器将用户凭证存储在本地文件中。 
• 
LDAP 安全域：服务器从轻量目录访问协议(LDAP)服务器中获取用户凭证。支持的LDAP 服务器有
OpenLDAP 等。 
• 
JDBC 安全域：服务器从数据库中获取用户凭证。支持的数据库为数据源所支持的数据库。 
• 
Jaas 安全域：服务器从自定义的LoginModule 中获取用户凭证，支持用户使用自定义的LoginModule
灵活的进行安全域的验证。 
• 
脚本安全域：服务器按照JSR223 规范从脚本（如js 脚本）中获取用户凭证。 
• 
服务扩展安全域：认证过程由用户具体实现类完成，用户类必需实现TongWeb 服务器指定的接口
“LoginProvider”。 
6.3 安全域配置 
安全域的配置项在${TongWeb_HOME}/conf/tongweb.xml 的
<server>/<security-service>/<auth-realm>节点中，各配置项说明如下： 
<auth-realm name="testRealm" type="File" all-roles-model="strict" 
x509-username-retriever-class-name="com.tongweb.catalina.realm.X509SubjectDnRetriever" 
lock-enabled="true" failure-count="5" lock-out-time="300" cache-size="1000" 
cache-removal-warning-time="3600" use-context-class-loader="true"> 
    <property name="UsersFile" value="testRealm_users.properties"/> 
    <property name="GroupsFile" value="testRealm_groups.properties"/> 
 </auth-realm> 
表 6.3-1：安全域基本配置项 
配置项名称 
说明 
默认值 
name 
安全域的名称 
无 
type 
安全域类型：分为File、 SQL、LDAP、JAAS、Script
和SPI类型 
无 
all-roles-mode
l 
角色类型：分为strict、authOnly、
strictAuthOnly 
stick 
x509-username-
retriever-clas
X509证书解析器实现类：当使用X509客户端证书
时，指定的类名称将用于从证书中检索用户名。 
com.tongweb.catalina.re
alm. 


## 第 35 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
28 
s-name 
X509SubjectDnRetriever 
lock-enabled 
是否使用锁定机制；true为锁定，false为不锁
定 。当为true时，下面4个属性生效。 
true 
failure-count 
允许错误次数：单位：次 
5 
lock-out-time 
锁定超时。单位：秒 
300 
cache-size 
缓存大小。单位：个 
1000 
cache-removal-
warning-time 
最小缓存时间。单位：秒 
3600 
use-context-cl
ass-loader 
指定加载方式：当为true时，是应用类加载器；
false时，是服务器类加载器。如果选择应用类加
载则LoginModule等相关类可以放在web/lib下，
而选择服务器类加载，类将从TW7_HOME/lib下加
载 
true 
6.3.1 文件安全域属性配置 
表 6.3-2：文件安全域配置项 
property属性 
说明 
默认值 
UsersFile 
用户文件名 
安全域名称_users.properties 
GroupsFile 
组文件名 
安全域名称_groups.properties 
6.3.2 JDBC安全域属性配置 
表 6.3-3：JDBC安全域配置项 
property属性 
说明 
默认值 
dataSourceNa
me 
指定已存在的数据源；如果该参数指定
数据源后，下面的数据源连接属性不需
要在配置 
无 
jdbcURL 
连接数据库的url 
无 
jdbcDriver 
连接数据库的驱动 
无 
jdbcUser 
连接数据库的用户名称 
无 
jdbcPassword 
连接数据库的用户密码 
无 
userSelect 
sql语句，查询结果为满足条件的用户
和密码 
SELECT user_name, user_pass FROM 
users WHERE user_name=? 
groupSelect 
sql语句，查询结果为用户名和用户所
在组 
SELECT user_name, role_name FROM 
user_roles WHERE user_name =? 
digestAlgori
thm 
用户密码的加密方式，有SM3、MD5、
SHA-1、SHA-256、SHA-512、DIGEST 
MD5 
digestSaltLe
ngth 
加强字节长度：将密码和一些随机数字
混合加密，增加强度 
8 
digestIterat
ions 
迭代加密次数 
3 
passLength 
密码长度限制 
无 


## 第 36 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
29 
6.3.3 LDAP安全域属性配置 
表 6.3-4：文件安全域配置项 
property属性 
说明 
默认值 
connectionURL 
登录ldap服务器的主机名 
无 
connectionName 
访问LDAP目录的基准DN，例如ou=myou,o=myorg.com， 
其中ou为组织单元，o为组织。 
无 
connectionPassw
ord 
服务器密码：连接LDAP服务器的用户口令 
无 
userBase 
用户基本域名：用于查询用户对应目录的基本DN 
无 
userName 
用户名属性：通过该属性可以查询到用户名 
无 
userPassword 
密码属性：定义查询密码的属性 
无 
roleBase 
角色的基本域名：用于查询角色对应目录的基本DN 
无 
roleName 
角色名属性：通过该属性可以查询到角色名 
无 
roleSearchUser 
角色对应用户属性：通过该属性可以查询到用户 
无 
digestAlgorithm 
用户密码的加密方式，有SM3、MD5、SHA-1、SHA-256、SHA-512、
DIGEST 
MD5 
digestSaltLengt
h 
加强字节长度：将密码和一些随机数字混合加密，增加强度 
8 
digestIteration
s 
迭代加密次数 
3 
passLength 
密码长度限制 
无 
6.3.4 JAAS安全域属性配置 
表 6.3-5：JAAS安全域配置项 
property属性 
说明 
默认值 
loginModuleClassNa
mes 
必填项：安全域通过loginModule进行安全验证，需要实现
javax.security.auth.spi.LoginModule的接口 
无 
userClassNames 
用户自定义的用户权限封装类 
无 
roleClassNames 
用户自定义的角色权限封装类 
无 
6.3.5 Script安全域属性配置 
表 6.3-6：Script安全域配置项 
property属性 
说明 
默认值 
scriptURI 
脚本文件的路径，如loginscript_demo.js 
无 
engineName 
脚本文件的引擎 
js 
6.3.6 服务扩展安全域属性配置 
服务扩展安全域是指用户可以通过实现服务器提供的接口来提供用户凭证 ，该接口为LoginProvider。


## 第 37 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
30 
需要实现一个方法：List<String> authenticate(String user, String password) ，该方法的实现逻辑
大致为接收并处理用户输入的user和password两个参数，并返回List<String>类型的对象，其中包含了指
定用户的角色列表。用户的实现类需要安装JAVA SPI 机制在jar包内的META-INF/services文件夹下进行配
置。 
6.4 管理用户 
对于文件类型的安全域，支持在TongWeb中配置用户。配置路径为${TongWeb_HOME}/ conf/security
目录下，命名格式为：安全域名称_groups.properties、安全域名称_users.properties。 
⚫ 安全域名称_groups.propertis 中命名格式如下： 
用户名=组名 
⚫ 安全域名称_users.propertis 中命名格式如下： 
用户名=加密后的密码 


## 第 38 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
31 
第7章 监控协议 
7.1 JMX-service 
TongWeb的JMX支持两种协议，分别是rmi协议和mp协议。默认是rmi协议。 
1. 
JMX配置项在${TongWeb_HOME}/conf/tongweb.xml的<server>/<web-container>/<jmx-service>
节点中，各配置项说明如下： 
表 7.1-1：HTTP通道配置项 
配置项名称 
说明 
默认值 
port 
jmx监控端口 
7200 
address 
Jmx监听地址 
127.0.0.1 
protocol 
jmx支持的协议，分别为rmi、mp 
rmi 
2. 
如果需要服务器绑定IPv6类型的JMX地址，则需要在服务器启动脚本中指定实际的IPv6地址。需要
在${TongWeb_HOME}/bin/external.vmoptions中添加参数的方式来支持，配置如下： 
-Djava.rmi.server.hostname=[2001:da8:2004:1000:202:116:160:41] 
7.2 SNMP代理服务 
简单网络管理协议（SNMP）是专门设计用于在IP网络管理网络节点（服务器、工作站、路由器、交换
机及HUBS等）的一种标准协议，它是一种应用层协议。 
TongWeb支持SNMP协议。开启协议后，可以通过SNMP工具查看TongWeb的服务器状态信息。 
7.2.1 SNMP代理服务配置 
表 7.2-1：SNMP配置项 
配置项名称 
说明 
默认值 
enabled 
代理服务器启动开关:true为启动，false为未启动 
false 
port 
端口：SNMP代理服务器监控的端口 
161 
address 
ip地址：NMP代理服务器监控的ip的地址，默认为0.0.0.0，即
监听该服务器上所有ip地址  
0.0.0.0 
version 
SNMP协议版本：目前支持v2和v3版本。v3是v2的升级版，选择
v3版本需要填写下方的用户名，验证秘钥，隐私秘钥和引擎id；
v2版本不需要填写；值为3，代表v3版本；值为2，代表v2版本。 
3 
transportTyp
e 
传输类型：SNMP代理服务器与网络管理系统之间所使用的传输
协议，可选择udp和tcp协议 
udp 
engineID 
引擎id：标明当前 SNMP 代理唯一标识符，长度必须大于5位，
小于32位 
62a0c18111c3173
3 
securityName 
安全用户名：v3版本的usm用户名 
public 
authKey 
验证秘钥: 确保只有授权才能请求和使用的的秘钥，加密方式
仅支持MD5 
nmsAuthKey 
privKey 
隐私密码: 对消息进行加密和解密时使用的秘钥，加密方式仅
myDesPriviateKe


## 第 39 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
32 
支持DES，加密key不能少于16个字符 
y 
 OID值，TongWeb目前支持查询的监控类型如下： 
表 7.2-2：OID值及监控类型 
OID 
Object Name 
解释 
1.3.6.1.4.1.55566.1.1.1 java.lang:type=OperatingSystem 
java操作 
系统信息 
1.3.6.1.4.1.55566.1.1.2 java.lang:type=Runtime 
java运行时信息 
1.3.6.1.4.1.55566.1.1.3 java.lang:type=ClassLoading 
java类加载信息 
1.3.6.1.4.1.55566.1.1.4 java.lang:type=Compilation 
java编译信息 
1.3.6.1.4.1.55566.1.1.5 java.lang:type=Memory 
java内存信息 
1.3.6.1.4.1.55566.1.1.6 java.lang:type=Threading 
java线程信息 
1.3.6.1.4.1.55566.1.1.7 java.lang:type=GarbageCollector,name=* 
java垃圾 
回收信息 
1.3.6.1.4.1.55566.1.2.1 config:parent=/Tongweb/Server,name=JDBCConnection
Pool* 
Tongwebjdbc 
连接池信息 
1.3.6.1.4.1.55566.1.2.2 config:name=WebContainer,parent=/Tongweb/Server 
Tongwebweb 
容器信息 
1.3.6.1.4.1.55566.1.3.1 TONGWEB:type=ThreadPool,name=* 
Tongweb 
线程池信息 
1.3.6.1.4.1.55566.1.3.2 TONGWEB:j2eeType=WebModule,name=//*/*,* 
Tongweb 
应用信息 
1.3.6.1.4.1.55566.1.3.3 TONGWEB:type=Manager,host=*,context=/* 
Tongweb 
管理信息 
1.3.6.1.4.1.55566.1.3.4 TONGWEB:type=Server 
Tongweb 
服务信息 
 
部分特殊返回值释义如下： 
⚫ 
Error：通过Jconsole查询时，无法获取或报错的值。 
⚫ 
UNSUPPORT:：MBean属于CompositeData和TabularData这两类的返回值未做支持。 
⚫ 
NULL：当查询值没有返回内容时，例：JDBC数据源未做配置。 
7.2.2 SNMP代理服务示例 
1. 
下载SnmpWalk，下载地址：https://ezfive.com/snmpsoft-tools/； 
2. 
使用SnmpWalk 查看TongWeb 服务器信息： 
⚫ 
V1 格式：查看从OID 为“1.3.6.1.4.1.55566.1.1.1”开始的所有Object 监控值。 
SnmpWalk.exe -r:127.0.0.1 -os: 1.3.6.1.4.1.55566.1.3.4(OID值) 
返回结果如下：为TONGWEB:type=Server的所有属性值。 


## 第 40 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
33 
 
⚫ 
V2 格式： 
SnmpWalk.exe -r:127.0.0.1 -os:.1.3.6.1.4.1.55566.1.1.1  -v:2c 
SnmpWalk.exe -r:127.0.0.1 -os:.1.3.6.1.4.1.55566.1.1.1  -v:2c -c:public 
⚫ 
V3 格式： 
SnmpWalk.exe -r:127.0.0.1 -os:.1.3.6.1.4.1.55566.1.1.1 -sn:public -v:3 
-ap:MD5  
-aw:nmsAuthKey -pp:DES -pw:myDesPriviateKey -ei:62a0c18111c31733 
⚫ 
查看某个OID： 
SnmpWalk.exe -r:127.0.0.1 -os:.1.3.6.1.4.1.55566.1.1.1 
-op:1.3.6.1.4.1.55566.1.1.2 
（注：-os为起始OID，-op为终止OID位置） 
注意：snmpwalk 仅支持UDP 协议。 
3. 
TongWeb 提供了支持TCP 协议的简单调用示例代码snmpCli.rar，存放于
${TongWeb_HOME}/Samples/snmp 目录中。 
 
 


## 第 41 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
34 
第8章 日志服务 
TongWeb轻量级应用服务器中，常用的日志配置主要为以下几种：系统日志、访问 
日志、日志级别、压缩日志和sql日志保存路径。其中访问日志在5.3访问日志中已介绍，下面介绍其它几
种日志配置。 
8.1 系统日志 
系统日志主要记录TongWeb轻量级服务器运行过程中，各种系统日志信息。 
1. 系统日志轮转方式分为：不轮转、按大小轮转、按周期轮转、按天轮转，同时只能选择一种轮转方
式。 
2. 系统日志配置项在${TongWeb_HOME}/conf/tongweb.xml 的<server>/<log-service>节点中，各配置
项说明如下： 
表 8.1-1：系统日志配置项 
配置项名称 
说明 
默认值 
file 
系统日志路径 
${tongweb.root}
/ 
logs/server.log 
rotation-limit 
轮转文件大小：取值单位有MB、KB。 
50MB 
rotation-timelim
it 
周期轮转方式：分为按小时轮转和按天轮转，按
小时轮转；设置分别为rotation-timelimit=“11 
H”, otation-timelimit=“11 D”,表示11个小
时或11天 
无 
rotation-file-co
unt 
轮转文件个数：产生的系统日志超过轮转文件个
数时，会删除最早产生的日志文件 
20 
rotation-by-day 
按天轮转开关：取值为true或false 
false 
log-format 
系统日志产生的日志格式 
[%d{yyyy-MM-dd 
HH:mm:ss}] 
[%p] [%c] 
[%m] %n 
rotation 
日志轮转开关：取值为true或false；当值为true
时，轮转日志相关配置才有效 
true 
verbose 
控制台日志开关:取值为true或false；但值为
true时，可以通过控制台打印日志 
true 
asynclog-on 
是否开启异步日志 
true 
thread-num 
异步日志线程数  
1 
capacity 
异步日志队列缓存数 
2147483647 
 
8.2 日志级别 
TongWeb轻量级应用服务器中的日志级别：OFF、SERVER、WARNING、INFO、CONFIG、FINE、FINER、FINEST、
ALL。其中，log4j建议只使用四个级别，分别是 ERROR、WARN、INFO、DEBUG。 


## 第 42 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
35 
⚫ 
OFF: 关闭日志输出； 
⚫ 
SERVER: 输出验证错误信息-会对系统运行状态产生影响 
⚫ 
WARNING：输入警告信息-一些不严重的异常情况 
⚫ 
CONFIG：调试模式-输出便于调试程序运行的信息 
⚫ 
INFO：正常输出-正常输出提示信息    
系统日志配置项在${TongWeb_HOME}/conf/tongweb.xml 的
<server>/<log-service>/<module-log-levels>节点中，部分配置说明如下： 
表 8.2-1：日志级别配置项 
配置项名称 
说明 
默认值 
ejb-container 
Ejb容器内产生的日志信息 
INFO 
web-container 
Web容器内产生的日志信息 
INFO 
data-source 
数据源模块产生的日志信息 
INFO 
deployment 
部署模块产生的日志信息 
INFO 
core 
基础服务模块产生的日志信息 
INFO 
systemout 
通过system.out打印的日志信息 
INFO 
other 
其它日志信息 
INFO 
8.3 压缩日志 
 TongWeb轻量级应用服务器支持对系统日志、访问日志进行压缩配置。 
1. 开启压缩日志时，首先要对系统日志、访问日志进行轮转配置；只能对轮转的文件进行压缩。 
2. 生成压缩文件的时间点，每天定时执行压缩任务。如果当日设置的时间点已经过了，则次日开始
执行。TongwWeb 默认为每种类型的日志保留180 个压缩文件，超过后会删除较早生成的压缩包。 
3. 压缩日志配置项在${TW7_HOME}/conf/tongweb.xml 的<server>/<compress-log-service>节点中，
配置说明如下： 
表 8.3-1：压缩日志配置项 
配置项名称 
说明 
默认值 
compress-ena
bled 
压缩开关： 
取值为true或false。 
compress-enabled="true,true,true" 
第一个参数表示开启系统日志压缩，第二个参
数表示开启访问日志压缩，第三个参数表示开
启持久化日志。 
compress-enabled 
="false,false,false" 
log-dir 
压缩日志路径：log-dir里面第一个值是系统压
缩目录；第二个值是访问日志压缩目录 
log-dir= 
"${tongweb.root}/logs, 
${tongweb.root}/logs/acc
ess" 
compress-obj 
压缩对象：第一个值表示系统日志；第二个值
表示访问日志 
compress-obj="1,2,3" 
execution-ti
me 
压缩时间：每天定时执行压缩任务的时间点 
execution-time="1,1,1" 
 


## 第 43 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
36 
8.4 SQL日志保存路径 
轻量级服务器中，提供对SQL日志路径的配置。SQL日志路径配置项在
${TongWeb_HOME}/conf/tongweb.xml的<server>/<log-save-path>配置项说明如下： 
表 8.4-1：SQL日志路径配置项 
配置项名称 
说明 
默认值 
sql-log-path 
Sql日志配置路径 
logs 
persistence-log-path 
设置持久化日志的存放目录 
persistence 


## 第 44 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
37 
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


## 第 45 页

东方通应用服务器软件TongWeb_V7.0用户使用手册 
7049_M9A01 
版权所有©东方通 
38 
 



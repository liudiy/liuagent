## 第 1 页

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 V8.0 
常见问题手册 
文档版本：80 9XXA0 3 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
202 5年10月 


## 第 2 页

声明
版权
Copyright ©2025北京东方通科技股份有限公司或其关联公司（以下简称 “东方通”）。保留所有权利。
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
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
1


## 第 3 页

版本变更说明
本章节记录了 8.0.9.XX 版本的所有变更说明。
• A03
序号
问题类别
变更说明
1
其他类
新增如下章节：
如何通过 TongWeb JCA 连接消息服务器 IBM MQ？
• A02
序号
问题类别
变更说明
1
启动类
新增如下章节：
升级后启动失败，提示重新解压？
• A01
首次发版。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
2


## 第 4 页

前言
本文档是 TongWeb 产品的用户使用手册之一，详细介绍使用 TongWeb 过程中遇到的常见问题及解决方
案。
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
◦在终端窗口发布命令
◦使用 Web 浏览器
◦安装软件
• 术语和概念
本文档可能使用一些专业术语和概念。请确保您熟悉这些术语和概念，或者有能力查阅相关资料以便进
一步理解。
• 实践经验
为了最大程度地受益于本文档，建议您具备一定实践经验。这将帮助您更好地应用文档中的操作指南和
建议。
请注意，本文档不适用于没有相关专业背景和知识的用户。如果您对本文档的内容或所需背景有任何疑问，
请在使用之前咨询相关专业人士或寻求额外的支持。
用户手册集
TongWeb 为您提供如下用户使用手册。
用户手册
说明
000_TongWeb_V8.0产品对比手册
详细介绍了 TongWeb 的版本差异以及如何选择
TongWeb 的产品等。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
3


## 第 5 页

用户手册
说明
001_TongWeb_V8.0产品介绍手册
详细介绍了 TongWeb 的概述、体系结构、版本功能对比
等信息。
002_TongWeb_V8.0安装与使用指引
详细介绍了 TongWeb 各平台上的安装启动、版本切换等
说明。
003_TongWeb_V8.0控制台使用手册
详细介绍了 TongWeb 管理控制台对应用进行部署、管理
操作等说明。
004_TongWeb_V8.0命令行工具手册
详细介绍了 TongWeb 命令行工具的使用说明。
005_TongWeb_V8.0REST API手册
详细介绍了 TongWeb REST 接口的使用说明。
006_TongWeb_V8.0常见问题手册
详细介绍了使用 TongWeb 过程中遇到的常见问题及解决
方案。
007_TongWeb_V8.0安全加固手册
详细介绍了 TongWeb 常见的安全加固配置方法说明。
008_TongWeb_V8.0容器化部署手册
详细介绍了 TongWeb 在容器上的部署说明。
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
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
4


## 第 6 页

目录
声明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1
版本变更说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
前言. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  3
1. 技术指标类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
1.1. 支持 JDK 版本是什么？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
1.2. 支持的操作系统包含哪些？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
1.3. 支持的数据库包含哪些？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
2. 登录类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9
2.1. 验证码问题？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9
2.2. 启动 TongWeb 服务器后，在本机通过命令修改密码时报错？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9
2.3. 如何设置信任IP？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
2.3.1. 限制说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
2.3.2. 限制现象. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
2.3.3. 方式一：控制台设置信任IP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  11
2.3.4. 方式二：命令行设置信任IP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
2.3.5. 方式三：通过修改 console.xml 文件. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
2.4. 动态密码绑定不成功或登录验证不通过？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
2.5. 开启动态密码后，密钥丢失，怎么办？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
2.6. 密码丢失，如何找回密码？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  13
2.7. 同一用户登录控制台后，再使用REST/JMX/命令行等接口接入，浏览器上的会话被强制退出？. .  14
3. 启动类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
3.1. 确认 TongWeb 并未启动，系统提示已启动，如何处理？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
3.2. 如何指定启动 TongWeb 使用的 java 路径？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
3.3. Linux 下使用 IBM JDK 启动 TongWeb 失败？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
3.4. 某些平台启动过慢？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
3.5. 启动失败，报授权解密相关错误？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
3.6. 启动失败，授权提示信息不明确？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
3.7. 升级后启动失败，提示重新解压？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
3.8. 集中管理中，启动实例失败时，找不到日志？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  18
4. 集中管理类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
4.1. 集中管理所在节点故障，如何恢复？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
4.2. 如何查询受管实例的集中管理 IP？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
5. 应用类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
5.1. 支持部署的应用类型有哪些？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
5.2. 应用部署时间长或卡住？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
5.3. 开启异步请求报空指针？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
5


## 第 7 页

5.4. 自动部署不生效？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
5.5. 自动部署应用时，文件尚未完成上传，系统日志就提示不是一个有效的应用？. . . . . . . . . . . . . . . . .  22
5.6. 自动部署应用时，如果加载了 dll 本地库，应用无法卸载和升级？. . . . . . . . . . . . . . . . . . . . . . . . . . .  23
5.7. 自动部署目录下的应用文件被外部删除后，每次启动都报找不到应用？. . . . . . . . . . . . . . . . . . . . . . .  24
5.8. 删除自动部署目录下的应用有.unDeployed 文件？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
5.9. 更新 JSP 文件后，没有实时生效？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
5.10. Cookie 异常字符报错？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
5.11. URI 中有非法字符报错？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
5.12. JSP 编译报错？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
5.13. 应用部署缓存不足告警？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  28
5.14. WebService 异常报错？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  29
5.15. 与应用类冲突报错？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  30
5.16. 获取另一应用上下文为空？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  31
5.17. 编码设置问题？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  31
5.18. 应用慢线程检测问题？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  34
5.19. 如何更好的兼容 Web 应用？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  36
5.20. 什么情况下开启 “Web兼容模式” 或 “轻量模式”？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  37
5.21. 从 root 用户切换到普通用户后，再启动 TongWeb，报错 “The scratchDir you
specified:[xxxx] is unusable”？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  37
6. 数据源类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  39
6.1. 如何快速回收数据库连接？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  39
6.2. 如何获取数据库连接池关联的物理连接？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  39
7. EJB服务类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
7.1. 无状态会话Bean实例总数的监视为何会有跌落回升表现？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
7.2. 使用w3协议，首次访问ejb应用可以成功，过10秒后再次访问应用，会出现空白页并抛异常？. . .  41
8. 监视类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  42
8.1. 监视数据为 -1？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  42
8.2. 无法监控到应用数据源？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  42
9. 日志类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  43
9.1. 异常日志：All other methods are uncovered. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  43
10. 安全类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  44
10.1. 启动TongWeb后，修改并保存console.xml，文件的修改被还原？. . . . . . . . . . . . . . . . . . . . . . . . . .  44
11. 通知类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  45
11.1. 通知的详情表示什么含义？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  45
11.2. 通知的内容是什么？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  45
12. 其他类. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
12.1. 高并发压测只有5个工作线程？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
12.2. 服务器返回的密码全是固定的*号？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
6


## 第 8 页

12.3. SSL 加密套件在 IBM 平台和其它平台不一致？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
12.4. IP 匹配规则是什么？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
12.5. 如何通过 TongWeb JCA 连接消息服务器 IBM MQ？. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
7


## 第 9 页

1. 技术指标类
1.1. 支持 JDK 版本是什么？
JDK8-JDK24。
• 支持 Oracle JDK，但部分 Oracle JDK 版本商用收费，在生产使用时请注意商业授权，或采用 Open
JDK、Tong JDK。
• 启用国密认证，JDK 要求 JDK8-JDK11。
• 使用虚拟线程，JDK 要求 JDK21。
• 需要安装 JDK，不能仅安装 JRE。仅安装 JRE 会导致 TongWeb 部分功能不能使用。
• Linux 下若使用 IBM JDK，则需要手动放置如下 jar 包到 “${tongweb.home}/lib/compatible” 目录，否
则启动 TongWeb 失败。
◦JDK 8.0
bcprov-jdk15on-1.70.jar
◦JDK 8.0+
bcprov-jdk18on-1.78.1.jar
1.2. 支持的操作系统包含哪些？
• Windows：
Microsoft Windows 系列
• Linux：
RedHat 系列、Suse Linux 系列、麒麟、统信 UOS、中科方德、欧拉等。
• Mac OS：
Mac OS 系列
1.3. 支持的数据库包含哪些？
主流数据库：Oracle, MySQL5, MySQL8, Sybase 15, dameng, Kingbase, Kingbase8, Oscar, HSQL,
Sybase type 4 for Sybase 11.x, jtds sybase, postgreSQL, SQLServer, Derby Client, Derby Embedded,
IBM Type 4, gbase8t, gbase8s, sr, db2, highgo, uxdb, GaussDB 100, InspurK-DB, linkoopdb,
OceanBase, MogDB 等。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
8


## 第 10 页

2. 登录类
2.1. 验证码问题？
在一些平台上，验证码无法正常显示，有两种解决方法（择其一即可）。
• 方法一：修改服务器 tongweb.xml（打开 Headless 系统配置模式）

◦系统默认开启 “服务器主配置文件防篡改”，TongWeb 运行期间禁止对主配置文件 “tongweb.xml” 进行
修改。
◦若需要修改 “tongweb.xml”，请确保 TongWeb 服务器处于停止状态或 “服务器主配置文件防篡改”（可
进入 “安全管理” > “安全策略” > “文件防篡改” 模块修改）关闭。
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “tongweb.xml” 文件。
3. 将 “-Djava.awt.headless=true” 功能打开，如下所示。
<arg enabled="true">-Djava.awt.headless=true</arg>

该操作可兼容大部分平台，该参数由 JDK 提供，打开后可能对应用性能有所影响。
• 方法二：修改服务器 console.xml（禁用验证码功能）

◦系统默认开启 “服务器主配置文件防篡改”，TongWeb 运行期间禁止对主配置文件 “console.xml” 进行
修改。
◦若需要修改 “console.xml”，请确保 TongWeb 服务器处于停止状态或 “服务器主配置文件防篡改”（可
进入 “安全管理” > “安全策略” > “文件防篡改” 模块修改）关闭。
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “console.xml” 文件。
3. 将 “VerCodeEnabled” 参数设置为 “false”，可禁用验证码功能。
2.2. 启动 TongWeb 服务器后，在本机通过命令修改密码
时报错？
问题现象：
启动 TongWeb 服务器后，通过命令修改密码时报错，如下图所示。
原因分析：
连接主机的端口号不正确，不再是默认的“9060”。
解决方案：
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
9


## 第 11 页

在执行的命令中，添加 “--port”，指向实际的端口。
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “tongweb.xml” 文件，查看并获取控制台的端口，如 “8090”。
...
<connector SSLEnabled="true" address="0.0.0.0" clientAuth="false" keystoreFile="conf/server.keystore"
keystorePass="jo+fvRppEjYJWnAqSYOpfg==" maxSwallowSize="2097152" maxThreads="24"
minSpareThreads="5" name="admin" port="8090" scheme="https" secure="true"
sslEnabledProtocols="TLSv1.2" sslProtocol="TLSv1.2" systemManaged="true"
truststoreFile="conf/server.keystore" truststorePass="jo+fvRppEjYJWnAqSYOpfg=="/>
...
3. 执行命令时，添加 “--port” 指向实际端口 “8090”，如下所示。
sh commandstool.sh --model=password --action=update --username=thanos --password=thanos123.com
--acceptAgreement=true --port=8090 originalPassword=thanos123.com newPassword=Thanos12.com
confirmPassword=Thanos12.com
4. 命令执行完成后，即可查看到“修改密码更新成功”的提示信息。
2.3. 如何设置信任IP？
出于安全考虑，TongWeb 对于非信任 IP 禁止登录 TongWeb 管理控制台。用户将无法进行任何操作。
默认仅安装 TongWeb 的本机受信任。
当使用远程浏览器访问 TongWeb 控制台前，请在安装 TongWeb 的本机将远程浏览器所在主机的 IP 设置
为“信任 IP”。
信任 IP 可为具体的 IP、匹配 IP 的正则表达式或通配符 IP（如：168.1.2.*，168.1.4.5-168.1.4.99）。
设置为 “*” 表示信任所有机器（不建议）。
2.3.1. 限制说明
• 针对本机浏览器
安装 TongWeb 后，默认仅本机受信任，本机操作不受限制。
• 针对远程浏览器
在安装 TongWeb 的本机将远程访问 TongWeb 控制台的主机 IP 设置为 “信任 IP” 后，远程浏览器才有
权限执行相关操作。
2.3.2. 限制现象
当使用远程浏览器访问 TongWeb 控制台，并且没有设置信任 IP，可能会遇到 “该操作仅限于在服务器本机
或受信任的IP上执行” 等提示信息，如下图所示。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
10


## 第 12 页

2.3.3. 方式一：控制台设置信任IP
注意事项
需要浏览器所在 IP 是服务器本机或者已受信任。
控制台设置信任IP
1. 登录 TongWeb 管理控制台。
2. 在控制台左上角，单击 “集中管理”，进入集中管理页面。
3. 在左侧导航栏中，选择 “安全配置” > “控制台安全”，进入控制台安全页面。
4. 配置信任 IP。
指定信任的客户端 IP 地址，其值可为具体的 IP、匹配 IP 的正则表达式或通配符 IP（如：168.1.2.*
，168.1.4.5-168.1.4.99）。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
11


## 第 13 页

5. 配置完成后，单击“更新”，即可完成控制台安全的配置。
若界面弹出“控制台安全更新成功”，则说明控制台安全配置成功。
2.3.4. 方式二：命令行设置信任IP
启动TongWeb，并进入 “${tongweb.home}/bin” 目录，执行如下命令，设置信任IP。
如下以信任IP为“192.168.1.1”为例说明。
sh commandstool.sh --username=thanos --password=Thanos12.com --acceptAgreement=true
--model=consolesecurity --action=update trustedIP=192.168.1.1
若设置的是正则表达式，则需要先进行编码，编码方式如下所示。
1. 进入TongWeb管理控制台。
2. 切换到目标实例。
3. 选择“基础配置”>“加密工具”，进入加密工具页面。
4. 加密类型选择“特殊字符”。
5. 单击“加密”，即可得到加密结果。
2.3.5. 方式三：通过修改 console.xml 文件
注意：
• 系统默认开启 “服务器主配置文件防篡改”，TongWeb 运行期间禁止对主配置文件 “tongweb.xml” 或
“console.xml” 进行修改。
• 若需要修改 “console.xml”，请确保 TongWeb 服务器处于停止状态或 “服务器主配置文件防篡改”（“安
全管理” > “安全策略” > “文件防篡改”）关闭。
console.xml 文件路径 “${tongweb.base}/conf/”。
为 console 节点添加或者修改 “trustedIP” 属性，设置完成后，需要重启 TongWeb 服务器，方可生效。
“trustIP” 可以设置为 IP、匹配 IP 的正则表达式或者通配符 IP。
如下以将 trustIP 设置为 IP 地址为例进行说明。
<console trustedIP=”192.168.1.1”>
2.4. 动态密码绑定不成功或登录验证不通过？
请确保服务器时间和手机时间保持一致。
2.5. 开启动态密码后，密钥丢失，怎么办？
若动态密码丢失，您可以修改“${tongweb.base}/conf/console.xml” 里的 name="用户名" 节点的
“enableOtp” 值的方式关闭动态密码。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
12


## 第 14 页

注意事项
console.xml 为 TongWeb 主配置文件，具有防篡改限制。若需要修改并使其生效，请先停止 TongWeb 服
务器，然后再进行修改。
操作步骤
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “console.xml” 文件。
3. 将丢失密钥账户对应的 “enableOtp” 字段修改为 “false”，即可关闭动态密码。
修改位置，如下图所示。
4. 修改完成后，保存并退出。
5. 启动 TongWeb 服务器。
6. 登录 TongWeb 控制台时，可发现不输入动态密码，可成功登录到控制台。
2.6. 密码丢失，如何找回密码？
可通过修改 “${tongweb.base}/conf/console.xml” 里的 name="用户名" 节点的 password 值的方式重置为
初始密码。
注意事项
console.xml 为 TongWeb 主配置文件，具有防篡改限制。若需要修改并使其生效，请先停止 TongWeb 服
务器，然后再进行修改。
操作步骤
1. 进入 “${tongweb.base}/conf” 目录。
2. 打开 “console.xml” 文件。
3. 将丢失账户（如 “thanos” ）对应的 “password” 字段修改为如下字符串，即可重置为初始密
码“thanos123.com”。
44D3$2$0B8AA118786066B2A9DF05A44B342AE2FC147F2164B5A9F232259E50DE5D9F1C$SHA-256
修改位置，如下图所示。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
13


## 第 15 页

4. 将丢失账户（如 “thanos” ）对应的 “changeInitPwd” 字段修改为 “true”，要求该账户登录时，必须修
改初始密码。
修改位置，如下所示。
5. 修改完成后，保存并退出。
6. 启动 TongWeb 服务器。
7. 使用重置后的初始密码，即可成功登录 TongWeb 控制台。
2.7. 同一用户登录控制台后，再使用REST/JMX/命令行等
接口接入，浏览器上的会话被强制退出？
为了保证用户的登录安全，当使用某用户通过浏览器登录控制台后，若再使用相同的用户通过 REST\JMX\
命令行等接口接入，该用户在浏览器上的会话会被强制终止（即被踢出，需要重新登录）。
例如：使用 thanos 账户登录 TongWeb 控制台，再使用该用户进行 JMX 接口接入，如下图所示。
浏览器上的会话会被强制退出，如下图所示。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
14


## 第 16 页

东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
15


## 第 17 页

3. 启动类
3.1. 确认 TongWeb 并未启动，系统提示已启动，如何处
理？
问题现象：
确认 TongWeb 并未启动，但系统提示 TongWeb 已启动，如下所示。
[tongtech@backup bin]s ./startserver.shExecute the comand: serverThe server is starting.ommandsstart> has
beenexecuted.tongtech@backup bin]s
Ready to <start> TongWeb: /home/tongtech/TongWebx.x.x.x/domains/domainl
解决方案：
请尝试删除 “${tongweb.base}/data” 目录下的 “tongweb.pid”，然后重试。
3.2. 如何指定启动 TongWeb 使用的 java 路径？
指定启动TongWeb的java路径，按照优先级别可设置：
1. 打开 “${tongweb.base}/conf/tongweb.xml” 文件。
2. 在 <environments> 标签下，添加如下标签。
<env name="JAVA_HOME" value="指定java路径（注意是bin的父目录）"/>
3. 修改当前用户的环境变量 JAVA_HOME，指定的启动 TongWeb 的java路径（注意是bin的父目录）。
4. 当前环境变量 PATH 中的第一个 java 路径。
3.3. Linux 下使用 IBM JDK 启动 TongWeb 失败？
问题现象：
2024-07-16 17:01:17 >>> Ready to <start> TongWeb: domains/domain1
Exception in thread "main" java.lang.IllegalArgumentException: java.lang.NullPointerException
        at com.tongweb.BaseUtil.parseServerLic(Unknown Source)
        at com.tongweb.BaseUtil.getServerLic(Unknown Source)
        at com.tongweb.server.util.LicUtils.getServerLic(Unknown Source)
        at com.tongweb.main.TongWebMain.c(Unknown Source)
        at com.tongweb.main.TongWebMain.main(Unknown Source)
Caused by: java.lang.NullPointerException
        at java.io.StringReader.<init>(StringReader.java:61)
        at com.tongweb.BaseUtil.a(Unknown Source)
        ... 5 more
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
16


## 第 18 页

2024-07-16 17:01:18 >>> Command <start> has been executed.
解决方案：
1. 手动将如下 jar 包放置于 “${tongweb.home}/lib/compatible” 目录。
◦JDK 8.0
bcprov-jdk15on-1.70.jar
◦JDK 8.0+
bcprov-jdk18on-1.78.1.jar
2. 重新启动 TongWeb 服务器即可。
3.4. 某些平台启动过慢？
此问题源自Java语言的底层设计，解决办法：
1. 打开 tongweb.xml 文件。
2. 将 <arg enabled="true">-Djava.security.egd=file:/dev/./urandom</arg> 节点的 enabled 属性设置为
true 或 false 以观察效果。
3.5. 启动失败，报授权解密相关错误？
对于少数情况，如 AIX 平台或 IBM JDK 环境，启动会出现授权解析失败问题，此时可尝试在
${tongweb.home}/lib/compatible 下添加 bcprov-jdk15on-1.70.jar（Jdk 8.0） 或 bcprov-jdk18on-
1.78.1.jar（Jdk 8.0+） 依赖包，该包可自行从互联网或其它渠道获取。
3.6. 启动失败，授权提示信息不明确？
由于授权问题导致启动失败，其提示信息均为：Exception in thread "main" java.lang.RuntimeException: License
     
error! Run version.[sh | bat] for detail.
      
此设计是出于安全考虑的，可在一定程度上防止追踪破解授权代码。
如此的提示信息难以了解具体的启动失败原因，您可以根据提示执行 version  脚本以得到更加详细的信息。
3.7. 升级后启动失败，提示重新解压？
问题现象：
启动时报错 “The extracted version file may be incomplete and an atteempt is being made to re-unzip
it…”，如下图所示。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
17


## 第 19 页

原因分析：
操作系统字符集如果不支持中文，doc 下中文手册会导致 TongWeb 无法正常启动。
解决方案：
先手动解压升级包 “version*.zip” ，然后再启动 TongWeb。
3.8. 集中管理中，启动实例失败时，找不到日志？
在集中管理中，若启动实例失败，可优先在 server.log 中查找失败日志。
若在 server.log 中没有找到相关日志，再前往 “domain1/logs/subprocess” 目录中，查找最新时间的日
志。
日志名称格式：类型-名称-时间戳.log
例如：TDG-TTT-20231010*.log
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
18


## 第 20 页

4. 集中管理类
4.1. 集中管理所在节点故障，如何恢复？
若集中管理所在节点故障，可通过如下方式恢复对各节点的集中管理。
• 通过自动备份的 tongweb.xml 和 console.xml文件进行恢复。
tongweb.xml & console.xml备份路径：${tongweb.base}/data/conf/。
• 若配置文件丢失，可重新添加各节点。
4.2. 如何查询受管实例的集中管理 IP？
1. 打开受管实例的 “${tongweb.base}/conf/tongweb.xml” 文件。
2. 查看 <server> 标签的 “centralizedIp” 属性。
“centralizedIp” 属性记录了集中管理的 IP 地址。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
19


## 第 21 页

5. 应用类
5.1. 支持部署的应用类型有哪些？
TongWeb 支持五种 JavaEE 应用文件的类型，包括 Web 应用、EJB 应用、Connector 应用、EAR 应用、
其他。有关应用类型的详细说明，请参见《TongWeb_V8.0控制台使用手册》。
类型
扩展名
用途和构成
Web应用
.war
包含 Servlet 和 JSP 等 Web 组件，EJB 组件以及静态 HTML 页面、Jar 
文件、标记库等。
EJB应用
.jar
包含 EJB 实现以及 EJB 实现所需的类。
Connect应用
.rar
包含连接器（资源适配器）的实现类。
EAR应用
.ear
包含上述三种应用类型。
其它应用
.car
非标准格式的其他应用, 选择此类应用文件后，只能通过后台获取其应用
类型。
5.2. 应用部署时间长或卡住？
问题现象：
应用部署时间长或卡住不动，如下图。
原因分析：
可能是应用启动执行到某一初始化操作时间长引起的。
解决方案：
在应用部署过程中出现这种情况时，可以按照如下方式解决。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
20


## 第 22 页

1. 重新刷新 TongWeb 管理控制台。
2. 打开“监视管理”>"阻塞线程"页面，找到"TW-0.0.0.0-9060-*"的部署线程。
3. 查看原因，通常是数据源阻塞、线程阻塞等问题。
5.3. 开启异步请求报空指针？
部署应用选用线程池后，需要注意，访问应用响应时长超过通道中“异步请求的默认超时”时间后，会报请求
超时和空指针问题。
5.4. 自动部署不生效？
自动部署开关默认关闭。
若需要开启自动部署开关，请选择 “基础配置” > “全局配置” > “应用”，进入应用页面，打开“自动部署应
用”开关。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
21


## 第 23 页

打开自动部署开关后，只需要将应用包拷贝到 “${tongweb.base}/autodeploy” 目录，即可自动部署该应
用。
• 生成状态标签：开启该功能后，自动部署的应用将会生成对应的标签文件，成功：.deployed，失败
：.failed，卸载 *.unDeployed。
• 部署到 deployment：开启该功能后，自动部署的非文件夹类型应用将解压部署到
${tongweb.base}/deployment 目录，关闭该功能将在原地解压部署。
• 自动部署目录：指定自动部署的目录，默认为 “${tongweb.base}/autodeploy”。
5.5. 自动部署应用时，文件尚未完成上传，系统日志就提示
不是一个有效的应用？
问题现象：
当从本地上传应用包到服务器时，由于应用包过大，超过 1 分钟都没有完成上传，日志提示不是一个有效
的应用。
报错信息，如下所示：
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
22


## 第 24 页

错误码，如下所示：
Caused by: com.tongweb.server.util.ErrorCodeExceptionImpl: errorCode:018
errorCode:018 ：无法正常识别应用类型，请检查要部署的应用文件是否合法。
原因分析：
当应用包体积较大时，一旦开始上传，自动部署目录下会立即生成一个相应的目录，并且系统会尝试立即开
始部署流程。然而，由于此时文件尚未完全上传，系统日志中会记录一条错误信息，指出当前的应用不是一
个有效的应用包。
解决方案：
该报错信息并不会阻碍应用的部署进程；一旦文件全部上传完毕，应用便能顺利部署成功。
为了避免此类问题的发生，您可以参照如下步骤上传文件：
1. 首先，将应用包上传到服务器的某个指定目录。
2. 然后，使用 mv  命令，将应用包作为一个整体一次性移动到自动部署目录中，即可避免文件不全的问
题。
5.6. 自动部署应用时，如果加载了 dll 本地库，应用无法卸
载和升级？
问题1：自动部署导致应用无法完全卸载
1. 开启自动部署，重启 TongWeb；
2. 将 xx.war 文件放置于自动部署目录中，观察到生成了 xx.war.deployed 文件，表明应用已成功部署；
3. 手动从自动部署目录中删除 xx.war 文件；
4. 通过 TongWeb 打印的日志可以看到，应用卸载成功后，紧接着又去部署了 xx.war 应用。
问题2：应用升级出现重复应用
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
23


## 第 25 页

1. 开启自动部署，重启 TongWeb；
2. 把 xx.war 放入自动部署目录，确认应用已成功部署（生成了 xx.war.deployed）；
3. 准备一个更新版本的 xx.war 文件，将其替换自动部署目录中原有的同名文件以进行升级操作；
4. 登录 TongWeb 控制台，在 “应用” 列表中发现存在两个 xx.war 应用。
解决方案：
方式1：
1. 释放 dll 本地库；
2. 重启 TongWeb。
方式2：
为了避免此问题，您可以选择不升级或卸载应用，或者选择去控制台部署应用。
然而，在控制台部署应用后，如果您尝试点击卸载应用，虽然表面上看似卸载成功，但实际上手动去删除应
用，会提示 dll 被占用。要彻底删除应用，您必须先停止 TongWeb 服务。
5.7. 自动部署目录下的应用文件被外部删除后，每次启动都
报找不到应用？
屏蔽日志的方式：
1. 在控制台上删除该应用；
2. 修改 ${tongweb.base}/conf/tongweb.xml，将该应用对应的节点删除。
5.8. 删除自动部署目录下的应用有.unDeployed 文件？
这个文件是个标记，告诉用户出现这个表示卸载已成功结束，用户看到之后可自行选择删除这个文件，删除
不会有任何影响。
5.9. 更新 JSP 文件后，没有实时生效？
更新 JSP 文件后，若需要实时生效，请进入已部署应用的详细配置页面。在“JSP”页签下，开启“开启JSP开
发模式”开关。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
24


## 第 26 页

开启 JSP 开发模式后，当有 JSP 文件更新时，更新的文件会在 5 秒内重新加载以生效。

若开启了资源缓存，生效时间会在资源的缓存时长后。
5.10. Cookie 异常字符报错？
问题现象：
报“An invalid domain [.test.com] was specified for this cookie”错，如下所示。
2022-06-14 11:07:31 [WARN] - java.lang.IllegalArgumentException: An invalid domain [.test.com] was specified
for this cookie
2022-06-14 11:07:31 [WARN] -    at
com.tongweb.web.util.http.Rfc6265CookieProcessor.validateDomain(Rfc6265CookieProcessor.java:202)
2022-06-14 11:07:31 [WARN] -    at
com.tongweb.web.util.http.Rfc6265CookieProcessor.generateHeader(Rfc6265CookieProcessor.java:137)
2022-06-14 11:07:31 [WARN] -    at
com.tongweb.server.connector.Response.generateCookieString(Response.java:960)
解决方案：
在应用配置中，开启“使用老版 Cookie 处理器”。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
25


## 第 27 页

5.11. URI 中有非法字符报错？
问题现象：
报“Invalid character found in the request target”错，如下所示。
2022-06-14 10:16:24 [INFO] - Error parsing HTTP request header
 Note: further occurrences of HTTP request parsing errors will be logged at DEBUG level.
java.lang.IllegalArgumentException: Invalid character found in the request target [/dbpool/?aa=|ddd]]. The valid
characters are defined in RFC 7230 and RFC 3986
        at com.tongweb.coyote.http11.Http11InputBuffer.parseRequestLine(Http11InputBuffer.java:470)
        at com.tongweb.coyote.http11.Http11Processor.service(Http11Processor.java:212)
解决方案：
在目标 HTTP 通道中，开启“路径中允许使用的未编码字符”和“参数中允许使用的未编码字符”，并配置“" <
> [ \ ] ^ ` { | }”。
操作步骤，如下所示。
1. 登录管理控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “Web 容器” > “通道”，进入通道列表页面。
4. 单击目标通道的通道名，进入通道详细信息页面。
5. 单击 “HTTP 属性” 页签，打开 “路径中允许使用的未编码字符” 和 “参数中允许使用的未编码字符” 开
关。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
26


## 第 28 页

5.12. JSP 编译报错？
问题现象：
报“quoted with ["] which must be escaped when used within the value”错，如下所示。
2022-06-14 11:24:55 [WARN] - com.tongweb.jasper.JasperException: /index2.jsp (line: [11], column: [45])
Attribute value [String.valueOf("aa")] is quoted with ["] which must be escaped when used within the value
2022-06-14 11:24:55 [WARN] -    at
com.tongweb.jasper.compiler.DefaultErrorHandler.jspError(DefaultErrorHandler.java:26)
2022-06-14 11:24:55 [WARN] -    at
com.tongweb.jasper.compiler.ErrorDispatcher.dispatch(ErrorDispatcher.java:276)
解决方案：
在应用配置中，关闭“Strict Quote Escaping”。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
27


## 第 29 页

5.13. 应用部署缓存不足告警？
问题现象：
报“because there was insufficient free space available after evicting expired cache entries - consider
increasing the maximum size of the cache”错，如下所示。
2022-06-14 12:16:39 [WARN] - Unable to add the resource at [/WEB-
INF/classes/org/oasis_open/docs/wsrf/rp_2/jaxb.properties] to the cache for web application [cxf] because
there was insufficient free space available after evicting expired cache entries - consider increasing the
maximum size of the cache
2022-06-14 12:16:39 [WARN] - Unable to add the resource at [/WEB-
INF/classes/org/oasis_open/docs/wsrf/rp_2/jaxb.properties] to the cache for web application [cxf] because
there was insufficient free space available after evicting expired cache entries - consider increasing the
maximum size of the cache
解决方案：
应用部署增大 “最大缓存大小”，通常大于应用所有 jar 的大小，通过应用监控缓存使用情况。
查看资源缓存量是否够用，再调整“最大缓存大小”。
1. 选择 “应用管理” > “应用”，进入应用/列表页面。
2. 单击目标实例所在行的 “监视”，进入监视页面，查看资源缓存量是否够用。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
28


## 第 30 页

3. 进入应用配置页面，对缓存进行调整。
注意：
切记盲目调大，典型毛病“999999999”。
5.14. WebService 异常报错？
问题现象：
报错信息，如下所示。
Caused by: org.xml.sax.SAXParseException: 文件提前结束。
        at com.sun.org.apache.xerces.internal.parsers.DOMParser.parse(DOMParser.java:262)
        at com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderImpl.parse(DocumentBuilderImpl.java:339)
        at com.tongweb.ws.commons.schema.XmlSchemaCollection$2.run(XmlSchemaCollection.java:651)
        at com.tongweb.ws.commons.schema.XmlSchemaCollection$2.run(XmlSchemaCollection.java:649)
        at java.security.AccessController.doPrivileged(Native Method)
        at com.tongweb.ws.commons.schema.XmlSchemaCollection.parseDoPriv(XmlSchemaCollection.java:649)
        at com.tongweb.ws.commons.schema.XmlSchemaCollection.read(XmlSchemaCollection.java:618)
        ... 64 more
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
29


## 第 31 页

解决方案：
从异常“com.tongweb.ws.commons.schema”可以看出 TongWeb 的 WebService 参与了应用的 xml 处理。
可在部署应用时，勾选加载应用的 “Webservice” 或 “Web 兼容模式”，即可解决该问题。
注意：
1. 用户需要进入 “基础配置” > “全局配置” > “服务器” 页签，打开 “启用 Webservice” 开关。
2. 在应用的 “资源加载” 页面中 “加载应用实现” 里才会显示 “WebService”。
5.15. 与应用类冲突报错？
问题现象：
Caused by: java.lang.AbstractMethodError:
javax.ws.rs.core.UriBuilder.uri(Ljava/lang/String;)Ljavax/ws/rs/core/UriBuilder;
    at javax.ws.rs.core.UriBuilder.fromUri(UriBuilder.java:96)
    at com.sun.jersey.spi.container.servlet.ServletContainer.service(ServletContainer.java:669)
    at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
解决方案：
在开启”Web兼容模式“的情况下，依旧加载“tongweb-jee-api.jar”中的类，可以设置”强制从应用加载的
类“来解决。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
30


## 第 32 页

5.16. 获取另一应用上下文为空？
问题现象：
通过request.getServletContext().getContext("/app")获取另一应用上下文为空。
解决方案：
在应用配置的“安全”页签下，开启“允许跨应用访问”。
5.17. 编码设置问题？
在遇到中文问题时，通常需要通过设置编码格式来解决问题。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
31


## 第 33 页

下面介绍编码设置及优先级。
• web.xml中请求、响应编码的配置优先级最高
在JavaEE8规范中，web.xml 增加了 request、response编码配置，该配置优先级最高。
...
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns="http://xmlns.jcp.org/xml/ns/javaee"
    xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-
app_4_0.xsd"
    id="WebApp_ID" version="4.0">
    <display-name>charset</display-name>
    <default-context-path>/testde</default-context-path>
    <request-character-encoding>GBK</request-character-encoding>
    <response-character-encoding>GBK</response-character-encoding>
...
在以往的项目中，request、response 编码通常通过 filter 来设置，如下所示。
...
<filter-name>EncodingFilter</filter-name>
<filter-class>
    org.springframework.web.filter.CharacterEncodingFilter
</filter-class>
<init-param>
    <param-name>encoding</param-name>
    <param-value>UTF-8</param-value>
</init-param>
<init-param>
     <param-name>forceEncoding</param-name>
     <param-value>true</param-value>
</init-param>
...
• 控制台编码设置
在部署应用时通过配置"编码"来完成。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
32


## 第 34 页

参数说明，如下表所示。
参数
参数说明
应用请求编码
应用程序的默认 HTTP 请求编码，优先级低于 web.xml。
应用响应编码
应用程序的默认 HTTP 响应体编码，优先级低于 web.xml。
JSP 文件编码
指定 JSP 文件编码, 相当于javaEncoding。
静态文件编码
使用指定的编码解析应用的文件资源，如 *.html 等静态资源，可用于
解决文件编码和 JVM 默认编码不一致引起的乱码问题。相当
于fileEncoding。
• URL编码设置
为兼容 tomcat 编码，HTTP 通道中"其它"中的"URI 编码"相当于tomcat的URIEncoding；“URI 使用
Content-Type 解码"相当于tomcat的useBodyEncodingForURI。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
33


## 第 35 页

5.18. 应用慢线程检测问题？
在应用运行过程中，可能会有一些线程因等待锁、阻塞导致执行时间慢。这时可以开启 TongWeb 的"慢线
程检测"功能来排查问题。
当 http 线程超过"阻塞阈值"时，则日志输出相应线程堆栈。通过大量收集该日志样本，以判断线程慢的原
因。

仅收集一、两个该日志，不能说明线程慢在该处。
2023-02-14 15:29:53 [WARN] - Thread [TW-0.0.0.0-8088-1] (id=[61]) has been active for [20,131] milliseconds
(since [2/14/23 3:29 PM]) to serve the same request for [ http://192.168.55.159:8088/webtest01/TestServlet]
and may be stuck ( configured threshold for this StuckThreadDetectionValve is [20] seconds). There is/are [1]
thread(s) in total that are monitored by this Valve and may be stuck. java.lang.Throwable
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
34


## 第 36 页

at java.lang.Thread.sleep(Native Method)
at com.tong.TestServlet.doGet(TestServlet.java:41)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
at com.tongweb.server.core.ApplicationFilterChain.enterApp(ApplicationFilterChain.java:365)
"中断阈值"通常不建议开启，因为实际应用场景中线程有业务相关逻辑，中断线程可能造成业务的不完整。 
若能确保中断线程无问题，则可开启。相关日志如下所示。
2023-02-14 15:29:59 [WARN] - Thread [TW-0.0.0.0-8088-1] (id=[61]) has been interrupted because it was
active for [26,177] milliseconds (since [2/14/23 3:29 PM]) to serve the same request for [
http://192.168.55.159:8088/webtest01/TestServlet] and was probably stuck (configured interruption threshold
for this StuckThreadDetectionValve is [25] seconds). java.lang.Throwable
at java.lang.Thread.sleep(Native Method)
at com.tong.TestServlet.doGet(TestServlet.java:41)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:503)
at javax.servlet.http.HttpServlet.service(HttpServlet.java:590)
at com.tongweb.server.core.ApplicationFilterChain.enterApp(ApplicationFilterChain.java:365)
。。。。。。。
2023-02-14 15:30:01 [WARN] - Thread [TW-0.0.0.0-8088-1] (id=[61]) was previously reported to be stuck but
has completed. It was active for approximately [26,177] milliseconds.
"中断阈值"只中断TongWeb的http线程，若应用自建线程出现阻塞，可通过"监视管理">"阻塞线程"查看，该
功能为监控的JVM所有线程。"强停"功能同样谨慎使用。

当遇到线程阻塞类问题时，主要通过 TongWeb 提供的线程堆栈来分析问题，从应用侧来解决。对于"中断阈
值", "阻塞线程"的"强停"功能需谨慎使用。
若http通道的线程和队列占满，则报错，如下所示。
2023-02-24 13:58:57.963 [WARN] [TW-0.0.0.0-8088-ClientPoller] [com.tongweb.web.util.threads] - Executor
rejected socket [ com.tongweb.web.util.net.NioEndpoint$NioSocketWrapper@fa310e2:
com.tongweb.web.util.net2023-02-24 13:58:57.963 [WARN] [TW-0.0.0.0-8088-ClientPoller]
[com.tongweb.web.util.threads] - Executor rejected socket
[com.tongweb.web.util.net.NioEndpoint$NioSocketWrapper@fa310e2:com.tongweb.web.util.net.NioChannel@1
2bd59a6:java.nio.channels.SocketChannel[connected local=/127.0.0.1:8088 remote=/127.0.0.1:64068]] for
processing java.util.concurrent.RejectedExecutionException: Queue capacity is full
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
35


## 第 37 页

at com.tongweb.web.util.threads.ThreadPoolExecutor.execute(ThreadPoolExecutor.java:138)
at com.tongweb.web.util.threads.ThreadPoolExecutor.execute(ThreadPoolExecutor.java:109)
at com.tongweb.web.util.netat
com.tongweb.web.util.net.AbstractEndpoint.processSocket(AbstractEndpoint.java:938)
at com.tongweb.web.util.netat
com.tongweb.web.util.net.NioEndpoint$Poller.processKey(NioEndpoint.java:1366)
at com.tongweb.web.util.net.NioEndpoint$Poller.run(NioEndpoint.java:1338)
at java.lang.Thread.run(Thread.java:750)
5.19. 如何更好的兼容 Web 应用？
1. 开启“轻量模式”对整个TongWeb生效
此模式会关闭 EJB、JCA 等服务，并尝试从应用自身加载 JSF、JavaMail、WebService、Xml 等技术实
现。若应用是基于 Tomcat 或其它 Servlet 容器开发，则通常可以获得更好的兼容性。
2. 部署应用时开启“web兼容模式”
以 Web 兼容模式加载该应用。若该应用是基于 Tomcat 等 Web 容器开发，则可以尝试打开此开关以获
得更好的兼容性。
开启此模式后，EJB 等企业级技术实现将不再支持，同时尝试从应用自身加载
JSF、JavaMail、WebService、Xml 等企业级技术实现。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
36


## 第 38 页

5.20. 什么情况下开启 “Web兼容模式” 或 “轻量模式”？
• Web兼容模式
“Web 兼容模式” 仅对单个应用生效，是用户在部署应用时，对单个应用的配置，属于应用内存级别的隔
离，隔离效果有限。
当用户需要同时部署 EJB 和 Web 应用的情况下，单独对 Web 应用开启。
• 轻量模式
轻量模式是全局生效，隔离更彻底，等同于 TongWeb 轻量级版本的物理级隔离。
若用户只有 Web 应用而没有 EJB 应用，推荐使用“轻量模式”。
5.21. 从 root 用户切换到普通用户后，再启动 TongWeb
，报错 “The scratchDir you specified:[xxxx] is
unusable”？
问题描述：
从 root 用户切换到普通用户后，启动 TongWeb，系统报错 “The scratchDir you specified:[xxxx] is
unusable”？
1. TongWeb 安装目录的权限给到 777 。
2. 使用 root  用户启动 TongWeb，并部署一个 war 应用，然后访问应用。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
37


## 第 39 页

3. 关闭 TongWeb。
4. 切换到普通用户（如：test）启动 TongWeb。
5. 启动后，系统报错 “The scratchDir you specified:[xxxx] is unusable”。
部署的 war 应用，点击链接报错。
原因分析：
切换为普通用户后，root 用户生成的 temp 文件导致部署的应用异常。
解决方案：
使用普通用户启动 TongWeb 前，删除 “${tongweb.base}/temp” 文件夹。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
38


## 第 40 页

6. 数据源类
6.1. 如何快速回收数据库连接？
基于数据源连接池的设计，空闲连接的回收机制是依赖连接的时间戳来判定是否需要回收，即便只有一个连
接在循环使用连接池，也会顺次“激活”所有的连接，使得所有连接的时间戳始终是新的，因此不会被回收。
只有在没有任何请求的情况下，超过最大空闲时间才会被回收掉。
对于需要快速回收数据库连接的场景，用户可尝试开启 “使用 LIFO 队列” 功能，使用后进先出类型的队列
存储数据库连接。
“使用 LIFO 队列” 默认“开启”。
若没有开启，用户可参照如下操作步骤，开启 “使用 LIFO 队列” 功能。
1. 登录 TongWeb 管理控制台。
2. 切换到目标实例。
3. 在左侧菜单栏中，选择 “Web 容器” > “数据源”，进入数据源列表页面。
4. 打开已创建的数据源，单击 “连接池”，进入连接池页签。
5. 打开 “使用 LIFO 队列” 开关。
6. 开启完成后，单击 “更新”，即可完成 “使用 LIFO 队列” 的开启操作。
6.2. 如何获取数据库连接池关联的物理连接？
首先通过JNDI获取到连接池返回的逻辑连接，然后调用
com.tongweb.tongejb.resource.jdbc.managed.util.NativeJdbcExtractor 类（所在jar包位
于${tongweb.home}/version<版本号>/modules/ejb/tongweb-ejb.jar）的 extractNativeConnection 方法
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
39


## 第 41 页

，将前面获取到的逻辑连接作为参数传递给此方法，该方法返回的结果即为该逻辑连接关联的物理连接。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
40


## 第 42 页

7. EJB服务类
7.1. 无状态会话Bean实例总数的监视为何会有跌落回升表
现？
无状态会话Bean实例在使用完毕后会进入“重新初始化”状态，此时会从池中移除，因此看到实例总数跌落
，待初始化完毕后会重新回到池中，此时可以看到总数又回升。
7.2. 使用w3协议，首次访问ejb应用可以成功，过10秒后
再次访问应用，会出现空白页并抛异常？
解决方案：
• 方案一：
修改“EJB w3协议”>“连接配置”>“读超时时间”，把值改大一些。
把“读超时时间”调大，连接保持时间会更久一些。
• 方案二：
在“基础配置”>“启动参数”，添加-Dtongejb.client.keepalive=PING_PONG 。
添加启动参数，性能会稍微降低。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
41


## 第 43 页

8. 监视类
8.1. 监视数据为 -1？
监视数据为 -1，表示相应的监视功能未开启。
8.2. 无法监控到应用数据源？
• 使用监控应用数据源功能，需要进入“基础配置”>“全局配置”>“应用”，在应用页面，打开 “监视应用数
据源”开关。并且，在应用数据源初始化完成后，才能监控到。
• 请确保 JDBC 连接池类型为 HikariCP、Druid、DBCP、C3P0、BeeCP、BoneCP、Tomcat 或者 Hulk。
• DBCP、C3P0、BoneCP 目前暂不支持监控“线程等待数”，即该监控值始终为 “-1”。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
42


## 第 44 页

9. 日志类
9.1. 异常日志：All other methods are uncovered
在web.xml中指定deny-uncovered-http-methods元素，在<web-resource-collection>使用<http-
method>只配置了部分HTTP方法时，例如：
<deny-uncovered-http-methods/>
<security-constraint>
    <display-name>Example Security Constraint</display-name>
    <web-resource-collection>
        <web-resource-name>Protected Area</web-resource-name>
        <url-pattern>/successful.jsp</url-pattern>
        <http-method>DELETE</http-method>
        <http-method>GET</http-method>
        <http-method>POST</http-method>
        <http-method>PUT</http-method>
    </web-resource-collection>
    <auth-constraint>
        <role-name>admin</role-name>
    </auth-constraint>
</security-constraint>
如果在web.xml文件中指定了deny-uncovered-http-methods元素，那么容器将拒绝任何未涵盖的HTTP方
法，并返回403(SC_FORBIDDEN)状态码。 应用部署时会记录日志信息：
Adding security constraints with URL pattern [/successful.jsp] to deny access with the uncovered HTTP
methods that are not one of the following [DELETE POST GET PUT].
如果未在web.xml文件中指定deny-uncovered-http-methods元素，将不会增加配置的URL Pattern的安全
约束。 应用部署时会记录错误日志信息：
For security constraints with URL pattern [/successful.jsp] only the HTTP methods [DELETE POST GET PUT]
are covered. All other methods are uncovered.
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
43


## 第 45 页

10. 安全类
10.1. 启动TongWeb后，修改并保存console.xml，文件的
修改被还原？
TongWeb提供“服务器主配置文件防篡改”功能，该功能默认为开启状态。
开启后，禁止在 TongWeb 运行期间对主配置文件 tongweb.xml、console.xml 等进行修改。
若被意外篡改，则自动进行恢复。
若需要关闭该功能，可进入“安全管理”>“安全策略”>“文件防篡改”，进入文件防篡改页签，可关闭“服务器
主配置文件防篡改”。
为保证服务器主配置文件安全不被篡改，不建议关闭。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
44


## 第 46 页

11. 通知类
11.1. 通知的详情表示什么含义？
当有系统配置属性改变，服务器需要重新启动才能生效时，系统会给出一条通知，其“详情”一般表示具体的
发送变化的属性名，以及其变化前后的值。若变化的属性有多个，则会以分号分隔来表示。此外，属性发生
变化后，若再次编辑将其恢复为启动之初的值，则重启TongWeb通知会取消。
11.2. 通知的内容是什么？
• 通知的内容范围力求包含所有需要管理员介入的操作提醒，一般包含系统模块变更后的重启TongWeb提
醒信息和许可即将到期或已经过期的提醒信息。
• 可发布通知的模块包括但不局限于 “全局配置”、“无状态 EJB”、“有状态 EJB”、“单例 EJB”、“EJB 连
接”、“启动参数”、“系统日志” 以及授权到期的提醒。
• 控制台上显示的通知条目不会自动更新，需要手动刷新网页以更新。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
45


## 第 47 页

12. 其他类
12.1. 高并发压测只有5个工作线程？
可能和授权（license.dat）有关，试用和教学用的授权有最大并发处理线程为5的限制，请尝试检查并更换
授权以解决此问题。
12.2. 服务器返回的密码全是固定的*号？
此设计是出于安全考虑的，密码不能泄漏出去，即使加密了也不能。
12.3. SSL 加密套件在 IBM 平台和其它平台不一致？
IBM MQ 支持的 CipherSpec 及其对应的 CipherSuite： https://www.ibm.com/docs/zh/ibm-mq/9.1?
topic=java-tls-cipherspecs-ciphersuites-in-mq-classes
12.4. IP 匹配规则是什么？
信任的IP、拦截的IP、爬虫的IP均使用如下统一匹配规则：
1. 支持通配符*，比如10.10.45.*
2. 支持指定IP区间，比如10.10.45.1-10.10.45.250
3. 支持指定的IP，比如0.10.45.5
4. 支持同时指定多个规则，规则之间使用英文逗号分隔。比如10.10.45.*,10.10.45.1-10.10.45.250
5. 以上规则同时支持ipv4和ipv6
12.5. 如何通过 TongWeb JCA 连接消息服务器 IBM MQ？
以下是使用 TongWeb JCA 连接消息服务器 IBM MQ 的详细配置步骤：
1. 获取 IBM MQ 自带的 rar 适配器
◦文件名：wmq.jmsra.rar
◦默认路径：通常位于 “${IBMMQ_HOME}/java/lib” 目录
2. 部署 rar 适配器
a. 在 TongWeb 控制台的左侧菜单栏中，选择 “应用管理” > “应用”，进入应用列表页面。
b. 单击 “部署”，进入应用部署页面。
c. 上传 rar 适配器，并单击 “添加”，完成 rar 适配器的部署。
3. 创建连接池 testc
a. 在 TongWeb 控制台的左侧菜单栏中，选择 “EJB 容器” > “JCA 连接池”，进入 JCA 连接池页面。
b. 配置 JCA 连接池。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
46


## 第 48 页

▪连接池名称：testc
▪连接定义：javax.jms.QueueConnectionFactory
c. 配置其他属性。
d. 单击 “添加”，完成 JCA 连接池 testc 的创建。
4. 创建托管对象 testd
a. 在 TongWeb 控制台的左侧菜单栏中，选择 “EJB 容器” > “JCA 托管对象”，进入 JCA 托管对象页
面。
b. 配置 JCA 托管对象。
▪托管对象名称：testd
▪资源类型：javax.jms.Queue
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
47


## 第 49 页

c. 配置其他属性。
d. 配置完成后，单击 “添加”，完成 JCA 托管对象 testd 的创建。
5. 部署并访问 TongWeb 自带用例 jmsExample
注：自带用例 jmsExample.war 位于 “${tongweb.home}/version*/examples” 目录中。
a. 在 TongWeb 控制台的左侧菜单栏中，选择 “应用管理” > “应用”，进入应用列表页面。
b. 单击 “部署”，进入应用部署页面。
c. 上传 jmsExample.war 应用，并单击 “添加”，完成 jmsExample.war 应用的部署。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
48


## 第 50 页

说明：
通过上图中的两个链接，即可实现消息的收发测试。
东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
49


## 第 51 页

东方通应用服务器软件TongWeb_V8.0常见问题手册
809XXA03
版权所有©东方通
50



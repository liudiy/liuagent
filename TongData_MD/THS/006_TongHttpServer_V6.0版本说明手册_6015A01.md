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
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
1


## 第 3 页

前言
本文档是 TongHttpServer 产品手册之一，详细描述 TongHttpServer 各个版本变更内容。
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
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
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
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
3


## 第 5 页

目录
声明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1
前言. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
1. 版本信息说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  6
1.1. 版本信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  6
1.2. 注意事项. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  6
2. 版本变更说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  7
2.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  7
2.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  7
3. 版本配套说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
3.1. 产品文件清单. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
3.2. 获取文件方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9
4. 升级注意事项. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
4.1. 配置差异. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
4.1.1. 监控. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  10
4.1.2. 国密. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
4.1.3. sticky配置. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  12
5. 历史变更说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
5.1. V6.0.1.4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
5.1.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
5.1.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
5.1.3. 修复BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
5.1.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  16
5.2. V6.0.1.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
5.2.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  17
5.2.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  18
5.2.3. 修复 BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  18
5.2.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  18
5.3. V6.0.1.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  18
5.3.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  18
5.3.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
5.3.3. 修复BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
5.3.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
5.4. V6.0.1.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
5.4.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  19
5.4.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
5.4.3. 修复BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
4


## 第 6 页

5.4.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
5.5. V6.0.1.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
5.5.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  20
5.5.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
5.5.3. 修复BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
5.5.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
5.6. V6.0.0.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
5.6.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
5.6.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
5.6.3. 修复BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
5.6.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
5.7. V6.0.0.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
5.7.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
5.7.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
5.7.3. 修复BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
5.7.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
5.8. V6.0.0.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
5.8.1. 新增特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
5.8.2. 优化特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
5.8.3. 修复BUG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
5.8.4. 移除特性. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
5.9. V6.0.0.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  28
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
5


## 第 7 页

1. 版本信息说明
1.1. 版本信息
产品名称
东方通负载均衡软件 TongHttpServer
版本号
V6.0.1.5
发布日期
2025.10.10
发出人
东方通
1.2. 注意事项
无
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
6


## 第 8 页

2. 版本变更说明
2.1. 新增特性
相对于 V6.0.1.4 新增特性，如下表所示。
功能
更改说明
所属模块
新增审计日志保留
时长配置
• 达到参数设置天数，定时删除设置天数之前的所有操作日
志。
http:
  ...
  # clearlog
  clear_log_day: 1
ths-console
多语言支持
控制台支持英语、繁体。
ths-console
2.2. 优化特性
相对于 V6.0.1.4 优化特性，如下表所示。
功能
更改说明
所属模块
httpserverHA 高可
用
keepalived 版本升级 v2.2.8 → v2.3.4，修复CVE-2024-
41184。
httpserverHA
curl升级
libcurl 版本升级 v8.13.0 → v8.16.0，修复CVE-2025-5399漏
洞。
httpserver
PDMP-5903：修
复robots.txt请求漏
洞
修复管理台可以直接访问robots.txt，禁
用http://ip:8000/robots.txt请求
ths-console
版权协议更改
修改控制台登录页版权协议
ths-console
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
7


## 第 9 页

3. 版本配套说明
3.1. 产品文件清单
若已购买 TongHttpServer，可获取如下 TongHttpServer 安装包、版本文档、产品文档。
• THS安装包
安装包
说明
TongHttpServer_6.0.1.5_aarch64.tar.gz
THS arm平台安装包。
TongHttpServer_6.0.1.5_x86_64.tar.gz
THS x86_64平台安装包。
TongHttpServer_6.0.1.5_windows.zip
THS windows系统安装包。
TongHttpServer_6.0.1.5_alpine_aarch64.tar.gz
THS alpine aarch64安装包，用于制作测试镜像。
TongHttpServer_6.0.1.5_alpine_x86_64.tar.gz
THS alpine x86_64安装包，用于制作测试镜像。
TongHttpServer_Instance_Image_6.0.1.5_alpine_
x86_64.tar
THS x86_64 宿主机不使用集中管理控制台测试镜
像。
TongHttpServer_Instance_With_Agent_Image_6.
0.1.5_alpine_x86_64.tar
THS x86_64 宿主机使用集中管理控制台测试镜
像。
• 版本文档
版本文档
说明
006_TongHttpServer_V6.0版本说明书
记录当前版本相对于上一个版本的变更说明。
• 产品文档
产品文档
说明
000_TongHttpServer_V6.0产品白皮书
提供 TongHttpServer 单节点使用说明。
001_TongHttpServer_V6.0产品用户手册
提供 TongHttpServer 单节点使用说明。
002_TongHttpServer_V6.0监控配置手册
提供 TongHttpServer 监控配置手册。
003_TongHttpServer_V6.0常见配置指令手册
提供 TongHttpServer 常见配置指令说明。
004_TongHttpServer_V6.0国密证书解密手册
提供国密 SSL 双证书签发流程、加密证书解密说
明。
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
8


## 第 10 页

产品文档
说明
005_TongHttpServer_V6.0常见问题手册
提供使用 TongHttpServer 过程中遇到的常见问
题及解决方案。
3.2. 获取文件方式
仅可通过东方通技术支持获取相关配套文件。
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
9


## 第 11 页

4. 升级注意事项
THS V6.0.1.0 版本开始进行了如下调整，后续会一直沿用6.0.1.0设计，修改如下：
• 使用 golang 构建管理控制台
• 重新设计监控模块，丰富监控功能
• 支持 http3.0 升级 openssl1.1.0d 到 openssl3.0
• 重新设计sticky模块，所有负载均衡策略上均支持配置会话保持
重新设计后 httpserver.conf 存在配置差异。重构后导致从 V6.0.0.x 升级到 V6.0.1.x 版本会出现配置兼容
问题。
版本
涉及版本
V6.0.0.x
V6.0.0.0、V6.0.0.1、V6.0.0.2、V6.0.0.3
V6.0.1.x
V6.0.1.0 及后续版本
4.1. 配置差异
4.1.1. 监控
• 收集指标的共享内存
版本
配置
说明
V6.0.0.x
http {
    ……
    status_zone;
    ……
    server {
        …….
        location / {
            …….
            status_bypass on;
            …….
       }
   }
}
status_zone放在http段，按虚拟主机名进行
收集，不需要收集的location使
用status_bypass on指令。
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
10


## 第 12 页

版本
配置
说明
V6.0.1.x
http {
    server {
        …….
        status_zone sever_zone1;
        …….
        location / {
            …….
           status_zone
location_zone1;
           …….
        }
    }
}
stream {
    server {
        …….
        status_zone sever_zone1;
        …….
    }
}
在需要开启指标收集的地方设置
status_zone, 并定义名字，支持按location 
收集、按 http 虚拟主机收集， 四层按server
收集，其他监控指标可参考
《TongHttpServer_V6.0监控配置手册》
，V6.0.1.3 开始支持status_zone 配置在 http
段。
• 开启监控 RESTful 接口
版本
配置
说明
V6.0.0.x
http {
    server {
        …….
        location /xxx {
            …….
            api write=off;
            …….
        }
    }
}
api 参数后为 write=off。V6.0.1.3 开始
，httpserver 进程内部会将write=off替换成
/
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
11


## 第 13 页

版本
配置
说明
V6.0.1.x
http {
    server {
        …….
        location /xxx/ {
            …….
            api /;
            …….
        }
    }
}
api 参数为路径，可以灵活定义输出哪些监控
指标， api使用参考《TongHttpServer_V6.0
监控配置手册》
4.1.2. 国密
版本
配置
说明
V6.0.0.x
http {
    server {
        …….
        ssl_protocols GMTLSv1.1;
        ssl_certificate crt/SS.pem;
        ssl_certificate_key crt/SS.key.pem;
        ssl_certificate crt/SE.pem;
        ssl_certificate_key crt/SE.key.pem;
    }
}
国密开启使用GMTLSv1.1，然
后依次配置签名证书、签名秘
钥，加密证书、加密证书秘
钥。
V6.0.1.x
http {
    server {
        …….
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_gmtls on;
        ssl_certificate crt/SS.pem crt/SE.pem;
        ssl_certificate_key crt/SS.key.pem
crt/SE.key.pem;
    }
}
使用ssl_gmtls 开启国密，然
后配置国密签名证书、加密证
书、签名秘钥、加密秘钥
4.1.3. sticky配置
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
12


## 第 14 页

版本
配置
说明
V6.0.0.x
http {
    upstream backend{
        …….
        sticky;
    }
}
sticky为单独负载均衡算法，不能和
其它负载均衡算法共存。
V6.0.1.x
http {
    upstream backend {
        ip_hash/least_conn/randmon/hash;
        sticky cookie example
domain=$my_domain maxage=3600;
    }
    server {
        set $my_domain www.test.com;
    }
}
Sticky可以和轮询及其他负载均衡算
法结合使用，当首次cookie为空的时
候调用指定的负载均衡算法进行后端
节点分配，对于多个虚拟主机，可以
通过变量配置不同的cookie参数 。
类似upstream中的keepalive指令
，sticky必须配置在负载均衡算法以
后
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
13


## 第 15 页

5. 历史变更说明
5.1. V6.0.1.4
发布日期：2025-06-30
5.1.1. 新增特性
功能
更改说明
所属模块
新增 modsecurity 
模块
modsecurity waf 模块，用于检测和阻止 Web 攻击，正向代
理支持 IP 和域名黑白名单。
load_module modules/http_modsecurity_module.so;
...
http{
    ...
    modsecurity on;
    modsecurity_rules_file /opt/THS/conf/sql.rule;
}
httpserver
stream 模块新增
upstream 健康检
查
upstream 健康检查功能用于动态检测后端服务器的运行状态
，保证代理请求只转发给健康的后端，从而提高服务的可靠性
和可用性，支持 TCP/UDP/HTTP 检测方式。
stream {
    ...
    upstream ssl {
        health_check interval=10000 fall=3 rise=3 type=tcp;
        zone ssl 1m;
        server 10.10.22.131:9091;
    }
    ...
}
httpserver
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
14


## 第 16 页

功能
更改说明
所属模块
登录次数限制和用
户锁定时长配置
• 控制台登录密码错误次数上限配置。
• 控制台用户锁定时长配置。
http:
  ...
  # Sign-in settings
  login_set:
    # number of errors
    err_num: 5
    # lockout time
    lock_second: 60
ths-console
license 更新
控制台支持更新 license。
ths-console
自定义响应头
支持配置控制台响应头，用户可根据安全扫描结果对控制台包
头加固。
   response_header:
    - key: "X-Content-Type-Options"
      value: "nosniff"
    - key: "X-Fram-Options"
      value: "SAMEORIGIN"
    - key: "Strict-Transport-Security"
      value: "max-age=3153600;includeSubDomains"
    - key: "X-Xss-Protection"
      value: "1;mode=block"
    - key: "X-Download-Options"
      value: "noopen"
    - key: "Referrer-Policy"
      value: "no-referrer"
    - key: "X-Permitted-Cross-Domain-Policies"
      value: "none"
    - key: "Content-Security-Policy"
      value: "frame-ancestors 'self'"
    - key : "Cache-Control"
      value: "No-store"
    - key : "Pragma"
      value: "No-cache"
ths-console
动态密码
控制台新增动态密码验证。
ths-console
双向认证配置
支持 HTTP 模块双向认证证书配置。
ths-console
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
15


## 第 17 页

功能
更改说明
所属模块
modsecurity 配置
modsecurity 功能支持语法高亮及指定配置后缀为 .rule。
ths-console
stream 健康检查可
视化配置
stream 集群健康检查支持可视化配置
ths-console
5.1.2. 优化特性
功能
更改说明
所属模块
压缩可视化配置
HTTP 压缩功能同时支持 gzip 和 brotli 配置。
ths-console
漏洞升级
gcc/zlib/curl/openssl 漏洞升级。
httpserver
lua 模块
LuaJIT 升级。
httpserver
temp 缓存目录所
有者优化
修复“使用普通用户运行httpserver时且配置文件未配置user指
令，使用 root 账户执行 -t 配置检测命令
，client_body_temp、proxy_temp所属用户会被修改
为nobody”。
httpserver
5.1.3. 修复BUG
更改说明
所属模块
HTTP 主动健康检查长连接检测配置(check_keepalive_requests)导致检测不生效修
复
    upstream backend {
        server 127.0.0.1:8089;
        zone backend_zone 256k;
        #配置http长连接检测方式
        health_check interval=1000 fall=2 rise=2 type=http timeout=1000;
        check_http_send "GET /index.html
HTTP/1.1\r\nHost:127.0.0.1:8089\r\nConnection: Keep-Alive\r\n\r\n";
        check_keepalive_requests 100;
        check_http_expect_alive http_2xx http_3xx;
    }
httpserver
5.1.4. 移除特性
无
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
16


## 第 18 页

5.2. V6.0.1.3
发布日期：2024-11-30
5.2.1. 新增特性
相对于 V6.0.1.2 新增特性，如下表所示。
功能
更改说明
所属模块
新增monitor.conf
将普罗米修斯、restful监控指标放在monitor.conf中
，httpserver.conf引入，便于一键启用监控。
配置
V6.0.0.x 监控配置
兼容
• http段新增 status_zone 指令，将所有虚拟主机的指标收集
到all_server zone中，启用后对于未配置zone 的upstream
，自动创建该upstream的 name_zone 的统计zone，并收
集监控指标。
http {
     ......
     status_zone;
     ......
}
• api 指令传参为 “write=off” 时，运行时替换为6.0.1.x的
path格式 “/”
• 忽略6.0.0.x 配置文件中的 status_bypass 指令
httpserver
ssl_verify_client
force
ssl_verify_client 新增force选项，双向认证时客户端未提供证
书时，浏览器刷新可弹出证书选择框。
httpserver
sysguard模块
适配ngx_http_sysguard_module。
httpserver
Brotli 压缩
适配ngx_brotli_module。
httpserver
ajp
适配ngx_http_ajp_module。
httpserver
永久密码
用户密码有效期修改为0-60天，为0时，密码永不过期。
ths-console
站点资源
新增前端静态应用管理，设置资源目录权限为755，文件权限
为644。
ths-console
热加载按钮容错性
优化
热加载增加端口冲突检测，端口冲突后提示错误信息。
ths-console
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
17


## 第 19 页

功能
更改说明
所属模块
gzip、Brotli 压缩
可视化配置
支持可视化gzip、Brotli压缩配置到HTTP段中。
ths-console
httpserver监控优
化
监控RESTful接口 的启用关闭移到HTTP→主参数→扩展参数
右侧，DNS、虚拟主机、upstream、路由等 XX区域 调整为 
指标采集，并用按钮控制开启关闭。
ths-console
配置导入
新增Nginx配置、THS配置导入到当前系统，并对6.0.0.x
status_zone, api，sticky，status_bypass 指令调整成6.0.1.x
格式。
ths-console
配置版本
保存当前配置为历史版本，历史版本管理还原等
ths-console
windows支持
适配windows系统。
• ths-console
• httpserver
• httpserverHA
5.2.2. 优化特性
功能
更改说明
所属模块
敏感信息加密存储
审计日志加密存储。
ths-console
5.2.3. 修复 BUG
更改说明
所属模块
优化节点 license.dat 存储逻辑，节点偶现收到0字节license。
ths-agent
5.2.4. 移除特性
无
5.3. V6.0.1.2
发布日期：2024-09-09
5.3.1. 新增特性
相对于 V6.0.1.1 新增特性，如下表所示。
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
18


## 第 20 页

功能
更改说明
所属模块
单机控制台
新增golang单机控制台，支持HTTP 、stream、mail、动态模
块等可视化配置。
ths-console
ssl_ignore_ca_wea
k_sign
新增ssl_ignore_ca_weak_sign指令,默认off，忽略双向认证时
客户端证书签名算法较弱错误(68:CA signature digest
algorithm too weak)。
server {
    listen 443 ssl;
    ssl_ignore_ca_weak_sign on;
}
httpserver
otel模块
新增链路追踪otel模块。
httpserver
jwt认证
新增jwt认证模块。
httpserver
rtmp
新增rtmp流媒体模块。
httpserver
license-server
对接东方通license-server授权服务器4.5.1.3版本。
httpserver
日志切割脚本
新增crontab日志切割脚本THS/tools/scripts/logrotate.sh。
脚本
新增开机自启动脚
本
新增crontab日志切割脚本THS/tools/service。
脚本
5.3.2. 优化特性
无
5.3.3. 修复BUG
无
5.3.4. 移除特性
无
5.4. V6.0.1.1
发布日期：2024-03-21
5.4.1. 新增特性
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
19


## 第 21 页

无
5.4.2. 优化特性
无
5.4.3. 修复BUG
更改说明
所属模块
PDMP-4907：配置https正向代理请求报错状态码405，不支持CONNECT方法。
httpserver
NC-4282：由于ths-agent需要后于httpserver启动，提供统一启动脚
本sartNode.sh。
脚本
修复先启动 ths-agent，再启动 manager 时，HA 状态未上报，控制台HA状态为未
知。
ths-agent
PDMP-4864：openssl漏洞修复，CVE-2022-2068 CVE-2022-3996 CVE-2023-
0217 CVE-2023-4807 CVE-2022-3602 CVE-2023-0464 CVE-2022-3358 CVE-
2023-0286 CVE-2023-0216 CVE-2022-3786 CVE-2023-5678 CVE-2023-5363
CVE-2022-2097 CVE-2023-2975 CVE-2023-0215 CVE-2022-4203 CVE-2023-
0401 CVE-2022-4450 CVE-2023-0466 CVE-2023-1255 CVE-2023-2650 CVE-
2023-3817 CVE-2023-0465 CVE-2022-4304
httpserver
5.4.4. 移除特性
无
5.5. V6.0.1.0
发布日期：2023-12-07
5.5.1. 新增特性
相对于 V6.0.0.3 新增特性，如下表所示。
功能
更改说明
所属模块
新增ths-agent模
块
新增 ths-agent 模块，THSManager和THS通过ths-agent使
用grpc 协议通信，ths-agent位于THS/bin目录
，THSManager为服务端，ths-agent为客户端。
ths-agent
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
20


## 第 22 页

功能
更改说明
所属模块
Httpserver基本指
标
统计httpserver 配置版本、pid、ppid。
httpserver
License指标
输出当前THS 正在使用的lciense信息。
httpserver
连接指标
统计httpserver启动后接收的总连接数、空闲连接数、丢弃连
接数、活跃连接数。
httpserver
Zone指标
共享内存使用情况指标统计。
httpserver
Http server监控指
标
监控虚拟主机流量，并发、1xx、2xx、3xx、4xx，ssl握手等
指标。
httpserver
Http location监控
指标
监控location流量，并发、1xx、2xx、3xx、4xx，ssl握手等指
标。
httpserver
Http集群指标
监控upsream 中各server 的并发、流量1xx、2xx、3xx、4xx
，ssl握手、主动健康检查、被动监控检查等指标。
httpserver
HTTP 缓存指标
输出 HTTP 缓存命中情况指标。
httpserver
HTTP限速指标
输出HTTP limit_req 详情指标。
httpserver
HTTP 限连指标
输出HTTP limit_conn 详情指标。
httpserver
Stream 虚拟主机
指标
统计 stream 虚拟主机session 指标。
httpserver
Stream 集群指标
输出upsream 中各server 的状态、流量，被动监控检查等指
标。
httpserver
DNS 解析指标
输出DNS 解析情况统计指标。
httpserver
Stream 限连指标
输出Stream limit_conn 详情指标。
httpserver
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
21


## 第 23 页

功能
更改说明
所属模块
普罗米修斯接口
支持配置普罗米修斯接口，将监控数据导出到普罗米修斯。
http {
    ......
    include prometheus_all.conf;
    server {
        server_name localhost_ths_monitor;
        listen 49151;
        access_log off;
        #allow 127.0.0.1;
        #deny all;
        location /thsapi/ {
            api /status;
        }
        location =/prometheus {
            prometheus all;
        }
    }
}
httpserver
upstream resolver
upstream 中支持配置resolver指令。
upstream backend {
    resolver 114.114.114.114 ipv6=off;
}
httpserver
upstream server支
持动态域名解析
upstream 中支持配置resolver指令。
upstream backend {
    #resolver 也可以配置在http段
    resolver 114.114.114.114 ipv6=off;
    #需要配置zone
    zone backned 1m;
    server www.baidu.com:443 resolve;
}
httpserver
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
22


## 第 24 页

功能
更改说明
所属模块
TLSv1.3
ssl protocol。
server {
    ssl_protocols TLSv1.3;
}
httpserver
http3.0
支持http3.0。
http {
   server {
        listen 8443 quic reuseport;
        listen 8443 ssl;
        server_name localhost;
        access_log logs/access.log main;
        ssl_protocols TLSv1.3;
        ssl_certificate tools/crt_demo/server.crt;
        ssl_certificate_key tools/crt_demo/server.key;
        #ssl_session_cache    shared:SSL:1m;
        #ssl_session_timeout  5m;
        ssl_ciphers  HIGH:!aNULL:!MD5;
        #ssl_prefer_server_ciphers  on;
        location / {
            add_header Alt-Svc 'h3=":8443"; ma=86400';
            root html;
            index index.html;
        }
    }
}
httpserver
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
23


## 第 25 页

功能
更改说明
所属模块
对接license-
server4.4.5.0
对接东方通license-server4.4.5.0，优化心跳逻辑。
use_license_server on;
license_server https://192.168.22.26:8443;
license_server http://192.168.22.26:8888;
license_pubkey "xxxx";
license_interface enp5s0f1;
http {
}
httpserver
5.5.2. 优化特性
无
5.5.3. 修复BUG
无
5.5.4. 移除特性
更改说明
所属模块
去掉java开发的单机控制台
ths-console.jar
5.6. V6.0.0.3
发布日期：2023-10-11
5.6.1. 新增特性
相对于 V6.0.0.2 新增特性。
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
24


## 第 26 页

更改说明
所属模块
对接东方通license-server4.5.0.0，支持由license-server更新授权
use_license_server on;
license_server https://192.168.22.26:8443;
license_server http://192.168.22.26:8888;
license_pubkey "xxxx";
license_interface enp5s0f1;
http {
}
httpserver
5.6.2. 优化特性
无
5.6.3. 修复BUG
相对于 V6.0.0.1 修复BUG，如下表所示。
更改说明
所属模块
修复文件编辑页面中文注释保存后，文件最后出现
乱码
ths-console.jar
控制台依赖升级
ths-console.jar
控制台长时间运行报500错误
ths-console.jar
控制台验证码去掉下划线
ths-console.jar
PDMP-4692：修复license.dat中汉字大于20启动提
示license product error
httpserver
5.6.4. 移除特性
无
5.7. V6.0.0.2
发布日期：2023-03-29
5.7.1. 新增特性
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
25


## 第 27 页

相对于 V6.0.0.1 新增特性
无
5.7.2. 优化特性
相对于 V6.0.0.1 优化特性 无
5.7.3. 修复BUG
相对于 V6.0.0.1 修复BUG，如下表所示。
更改说明
所属模块
NC-2353：location添加处理方式代理到集群失败
ths-console.jar
额外参数输入框无法输入单引号，双引号
ths-console.jar
location匹配输入=号保存被过滤
ths-console.jar
PDMP-4370：鲲鹏aarch64环境，启动报错缺
少libcrypt.so.1
httpserver
404 页面显示TongHttpServer/版本号，不满足安
全要求，统一修改成webserver
httpserver
5.7.4. 移除特性
无
5.8. V6.0.0.1
发布日期：2022-12-27
5.8.1. 新增特性
相对于 V6.0.0.0 新增特性，如下表所示。
更改说明
所属模块
控制台三元分离
ths-console.jar
控制台新增国密证书生成，解密吉大，格尔签发的证书
ths-console.jar
控制台新增配置文件版本功能
ths-console.jar
新增licnese查看功能，执行start.sh -l /start.sh -L 查看
httpserver
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
26


## 第 28 页

更改说明
所属模块
license 每天检测3次，小于15天打印license过期警告，过期后主动退
出
httpserver
主动健康检查新增国密检查功能,health_check interval=3000 fall=31
rise=1 type=gmssl_hello;
httpserver
5.8.2. 优化特性
更改说明
所属模块
控制台UI升级，调整为新版UI
ths-console.jar
5.8.3. 修复BUG
相对于 V6.0.0.0 修复 BUG，如下表所示。
更改说明
所属模块
PDMP-3364：低版本火狐浏览器，界面显示不完全
ths-console.jar
PDMP-3698：控制台解析主配置文件报错
ths-console.jar
PDMP-2924：吉大国密数字信封解密
ths-console.jar
PDMP-3409：启动停止页面1000以下端口修改
为1024以下端口
ths-console.jar
PDMP-3337：控制台—http设置—虚拟主机—
编辑操作中：保存虚拟主机-主参数，会造成下
方location配置中集群名不复选参数，和选择列表丢
失
ths-console.jar
fastjson，springsecurity等安全问题，去掉fastjson
，升级springsecurity
ths-console.jar
httpserver配置php不能启动，报nginx_version找
不到
httpserver
开启统计后 location 中配置使用proxy_pass
http://ip:port方式会频繁输出
hander::shm_add_uastrean() failed错误
httpserver
5.8.4. 移除特性
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
27


## 第 29 页

无
5.9. V6.0.0.0
发布日期：2021-12-23
首次发版。
东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
28


## 第 30 页

东方通负载均衡软件 TongHttpServer V6.0 版本说明手册
6015A01
版权所有©东方通
29



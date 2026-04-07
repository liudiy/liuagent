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
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
1


## 第 3 页

前言
本文档是 TongHttpServer 产品手册之一，提供 TongHttpServer 监控使用说明。
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
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
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
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
3


## 第 5 页

目录
声明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  1
前言. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  2
1. 监控概述. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  7
2. 配置说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
2.1. api 指令说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  8
2.2. status_zone 指令说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  9
2.3. zone 指令说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  11
2.4. 接口安全. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  13
3. 详细说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
3.1. 开启 RESTful 接口. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
3.1.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  14
3.1.2. 验证过程. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  15
3.1.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  15
3.2. httpserver 基本指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
3.2.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
3.2.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
3.2.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
3.2.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  21
3.3. license 指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
3.3.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
3.3.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
3.3.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
3.3.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  22
3.4. 连接指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  23
3.4.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  23
3.4.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  23
3.4.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  23
3.4.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
3.5. 共享内存 zone 的 slab 分配器指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
3.5.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
3.5.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  24
3.5.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
3.5.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  25
3.6. HTTP 虚拟主机指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
3.6.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  26
3.6.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
4


## 第 6 页

3.6.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  27
3.6.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  28
3.7. HTTP 路由指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  28
3.7.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  28
3.7.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  30
3.7.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  30
3.7.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  31
3.8. HTTP 集群指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  31
3.8.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  31
3.8.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  32
3.8.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  33
3.8.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  33
3.9. HTTP 缓存指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  35
3.9.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  35
3.9.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  36
3.9.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  37
3.9.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  38
3.10. HTTP 限速指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  39
3.10.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  39
3.10.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  40
3.10.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
3.10.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
3.11. Stream 虚拟主机指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
3.11.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  41
3.11.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  42
3.11.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  43
3.11.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  43
3.12. Stream 集群指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  44
3.12.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  44
3.12.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
3.12.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
3.12.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  46
3.13. DNS 解析指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  48
3.13.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  48
3.13.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  49
3.13.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  49
3.13.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  50
3.14. 限连指标. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  50
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
5


## 第 7 页

3.14.1. 配置方式. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  51
3.14.2. 接口地址. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  52
3.14.3. 响应信息. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  52
3.14.4. 指标说明. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  52
4. 导出监控指标（prometheus 格式）. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  54
4.1. prometheus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  54
4.2. prometheus_templet. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  54
4.3. $prometheus_value 内置变量. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  55
4.4. 指标模板完整示例. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  56
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
6


## 第 8 页

1. 监控概述
TongHttpServer 提供 HTTP RESTful 接口，以 JSON 格式返回 httpserver 实例监控数据。同时，也支持和
普罗米修斯对接。
监控指标，如下所示。
• THS 基本指标；
• THS 客户端连接指标；
• 共享内存区域使用指标；
• SSL 握手指标；
• DNS 查询指标；
• 虚拟主机( server )请求、响应指标；
• 路由( location )请求、响应指标；
• 上游( upstream )请求、响应指标；
• HTTP 缓存指标；
• HTTP 限速指标( limit_req )；
• HTTP 限连指标( limit_conn )；
• HTTP 被动健康检查指标；
• HTTP 主动健康检查指标；
• Stream TCP/UDP 会话指标；
• Stream 主动健康检查指标；
• Stream 限连指标( limit_conn )。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
7


## 第 9 页

2. 配置说明
2.1. api 指令说明
用户可通过 “http://ip:port” 加 location 后缀访问监控指标。
TongHttpServer 默认配置中有以下示例，用户可通过 “http://ip:49151/thsapi/” 访问监控接口。
http {
    server {
        server_name localhost_ths_monitor;
        listen 49151;
        access_log off;
        #allow 127.0.0.1;
        #deny all;
        location /thsapi/ {
            api /status;
        }
    }
}
TongHttpServer 支持在 location 中使用 api  指令启用监控 HTTP RESTful 接口。
配置指令说明，如下所示。
分类
说明
指令
api
语法
api URI;
作用域
location
其中 URI 是必须参数，其工作原理类似于 alias 指令，但操作的是 API URI 树。
TongHttpServer 在 RESTful API 的 /status/  中提供所有指标。
完整指标配置，如下所示：
location /thsapi/ {
   api /status/;
}
以如下配置为例：
location /thsapi/ {
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
8


## 第 10 页

   api /status/http/server_zones/;
}
请求 URI /thsapi/  部分被 api  指令参数 “/status/http/server_zones/” 替换。
例如，当请求 “http://ip:49151/thsapi/server_zone” 时，“/thsapi/” 会被替换成
/status/http/server_zones/。
替换后，结果为 “http://ip:49151/status/http/server_zones/server_zone” 。
同时，也可以使用变量：
location ~^/thsapi/([^/]+)/(.*)$ {
    api /status/http/$1_zones/$2;
}
当使用 “/thsapi/location/location_zone/requests/” 访问监控地址，将按以下方式转换：
$1 = "location"
$2 = "location_zone/requests/"
替换后实际请求的监控地址为：/status/http/location_zone/location_zone/requests/。
2.2. status_zone 指令说明
HTTP 虚拟主机(server)、HTTP 路由(location)、HTTP DNS 解析(resolver)、stream 虚拟主
机(server)、stream DNS 解析(resolver) 需要使用 status_zone  配置指定 zone 收集指标。
指令说明
分类
说明
指令
status_zone
语法
status_zone zone;
作用域
http server、http location、http if in location、stream
server、resolver
• http server、location 监控 zone
配置示例，如下所示。
server {
    ...
    status_zone test_server_zone;
    ...
    location / {
        status_zone test_local_zone;
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
9


## 第 11 页

        root html;
        index index.html index.htm;
    }
}
• stream server 监控zone
配置示例，如下所示。
stream {
    upstream web {
        server 127.0.0.1:8000;
    }
    server {
        status_zone stream_zone;
        listen 12345;
        proxy_pass web;
    }
}
• resolver 监控 zone
resolver 支持配置在 http、http server、http location、http upstream、stream 及 stream server 
中。
配置示例，如下所示。
http {
    ...
    resolver 127.0.0.1:53 status_zone=resolver_zone;
    ...
    upstream backend {
        ...
        resolver 127.0.0.1:53 status_zone=upstream_resolver_zone;
        ...
    }
    server {
        ...
        resolver 127.0.0.1:53 status_zone=server_resolver_zone;
        ...
        location / {
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
10


## 第 12 页

            ...
            resolver 127.0.0.1:53 status_zone=location_resolver_zone;
            ...
        }
    }
}
stream {
    ...
    resolver 127.0.0.1:53 status_zone=stream_resolver_zone;
    ...
    server {
        ...
        resolver 127.0.0.1:53 status_zone=stream_server_resolver_zone;
        ...
    }
}
2.3. zone 指令说明
HTTP 集群配置(upstream)、Stream 集群(upstream) 、limit_conn_zone 并发连接、limit_req_zone 限制请
求速率，需要使用 zone  配置指定 zone 收集指标，获取集群健康状态等信息。
指令说明
分类
说明
指令
zone
语法
zone zone_name;
作用域
http upstream、stream upstream、http
• http upstream 监控 zone
配置示例，如下所示。
upstream health_check_ssl {
    health_check interval=30000 fall=3 rise=5 type=ssl_hello;
    server 10.10.22.131:9091;
    zone health_check_ssl 1m;
}
共享后端服务器状态（健康检查、连接数）。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
11


## 第 13 页

• stream upstream 监控 zone
配置示例，如下所示。
upstream ssl {
    health_check interval=10000 fall=3 rise=3 type=tcp;
    zone ssl 1m;
    server 10.10.22.131:9091;
}
共享后端服务器状态（健康检查、连接数）。
• http 限速监控 zone
配置示例，如下所示。
http{
    limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;
    ...
    server {
        ...
        location /limitrate {
            index limitrate.html;
            alias /opt/THS/html/;
            limit_req zone=one;
        }
    }
}
限请求速率的共享内存。
• http 限连监控 zone
配置示例，如下所示。
http{
    limit_conn_zone $binary_remote_addr zone=addr:10m;
    ...
    server {
        ...
        location /limitconn {
            index limitconn.html;
            alias /opt/THS/html/;
            limit_conn addr 1;
            limit_conn_status 500;
            limit_rate 50;
        }
    }
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
12


## 第 14 页

}
限并发连接的共享内存。
2.4. 接口安全
1. 基于 IP 控制：
location /thsapi/ {
    api /status/;
    allow 127.0.0.1;
    deny  all;
}
只允许 127.0.0.1 访问监控接口。
2. 基于 HTTP 基本认证：
location /thsapi/ {
    api /status/;
    auth_basic "test";
    auth_basic_user_file conf/htpasswd;
}
只允许 test 用户访问监控接口。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
13


## 第 15 页

3. 详细说明
3.1. 开启 RESTful 接口
TongHttpServer 默认开启了 RESTful 接口。
在 TongHttpServer 配置文件中，默认单独建立了一个虚拟主机，且配置了 location，开启了 RESTful 接
口。
注意： 用户不必为每个虚拟主机都开启 RESTful 接口。
3.1.1. 配置方式
1. 进入 THSManager 集中管控台的 “编辑配置” 界面或单机控制台的 “文件编辑” 中的 monitor.conf文件。
2. 在 HTTP 块中，输入如下内容。
配置说明，请参阅 API 指令说明。

分组节点在分组列表中找到 编辑配置 功能；
未分组节点在节点列表找到 编辑配置 功能；
单机控制台找到 monitor.conf  文件。
    server {
        server_name localhost_ths_monitor;
        listen 49151;
        access_log off;
        #allow 127.0.0.1;
        #deny all;
        location /thsapi/ {
            api /status;
        }
    }
配置示意图，如下所示。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
14


## 第 16 页

3. 单击 “保存” > “发布”，若提示成功，则表示配置完成。
3.1.2. 验证过程
使用 curl 命令或浏览器访问。
curl http://ip:49151/thsapi/
3.1.3. 响应信息
{
    "httpserver": {
        "version": "6.0.1.0",
        "address": "127.0.0.1",
        "generation": 1,
        "load_time": "2023-10-24T14:09:57.058Z",
        "pid": 75,
        "ppid": 74
    },
    "license_info": {
        "consumer_name": "test",
        "project_name": "test",
        "license_type": "trial",
        "create_date": "2022-12-20",
        "end_date": "2023-12-20",
        "product_name": "TongHttpServer",
        "version_number": "6.0",
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
15


## 第 17 页

        "license_id": ""
    },
    "connections": {
        "accepted": 4,
        "dropped": 0,
        "active": 3,
        "idle": 1
    },
    "slabs": {
        "cache_zone": {
            "pages": {
                "used": 2,
                "free": 506
            },
            "slots": {
                "64": {
                    "used": 1,
                    "free": 63,
                    "reqs": 1,
                    "fails": 0
                },
                "512": {
                    "used": 1,
                    "free": 7,
                    "reqs": 1,
                    "fails": 0
                }
            }
        },
        "limit_conn_zone": {
            "pages": {
                "used": 2,
                "free": 2542
            },
            "slots": {
                "64": {
                    "used": 1,
                    "free": 63,
                    "reqs": 74,
                    "fails": 0
                },
                "128": {
                    "used": 1,
                    "free": 31,
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
16


## 第 18 页

                    "reqs": 1,
                    "fails": 0
                }
            }
        },
        "limit_req_zone": {
            "pages": {
                "used": 2,
                "free": 2542
            },
            "slots": {
                "64": {
                    "used": 1,
                    "free": 63,
                    "reqs": 1,
                    "fails": 0
                },
                "128": {
                    "used": 2,
                    "free": 30,
                    "reqs": 3,
                    "fails": 0
                }
            }
        }
    },
    "http": {
        "server_zones": {
            "http_server_zone": {
                "ssl": {
                    "handshaked": 4174,
                    "reuses": 0,
                    "timedout": 0,
                    "failed": 0
                },
                "requests": {
                    "total": 4327,
                    "processing": 0,
                    "discarded": 8
                },
                "responses": {
                    "200": 4305,
                    "302": 12,
                    "404": 4
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
17


## 第 19 页

                },
                "data": {
                    "received": 442444,
                    "sent": 44442322
                }
            }
        },
        "location_zones": {
            "location_zone": {
                "requests": {
                    "total": 4258,
                    "discarded": 0
                },
                "responses": {
                    "200": 4257,
                    "304": 1
                },
                "data": {
                    "received": 5333300,
                    "sent": 333333544
                }
            }
        },
        "caches": {
            "cache_zone": {
                "size": 0,
                "cold": false,
                "hit": {
                    "responses": 0,
                    "bytes": 0
                },
                "stale": {
                    "responses": 0,
                    "bytes": 0
                },
                "updating": {
                    "responses": 0,
                    "bytes": 0
                },
                "revalidated": {
                    "responses": 0,
                    "bytes": 0
                },
                "miss": {
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
18


## 第 20 页

                    "responses": 0,
                    "bytes": 0,
                    "responses_written": 0,
                    "bytes_written": 0
                },
                "expired": {
                    "responses": 0,
                    "bytes": 0,
                    "responses_written": 0,
                    "bytes_written": 0
                },
                "bypass": {
                    "responses": 0,
                    "bytes": 0,
                    "responses_written": 0,
                    "bytes_written": 0
                }
            }
        },
        "limit_conns": {
            "limit_conn_zone": {
                "passed": 73,
                "skipped": 0,
                "rejected": 0,
                "exhausted": 0
            }
        },
        "limit_reqs": {
            "limit_req_zone": {
                "passed": 224213,
                "skipped": 0,
                "delayed": 63,
                "rejected": 23,
                "exhausted": 0
            }
        },
        "upstreams": {
            "upstream": {
                "peers": {
                    "192.168.16.4:80": {
                        "server": "backend.example.com",
                        "service": "_example._tcp",
                        "backup": false,
                        "weight": 5,
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
19


## 第 21 页

                        "state": "up",
                        "selected": {
                            "current": 2,
                            "total": 232
                        },
                        "max_conns": 5,
                        "responses": {
                            "200": 222,
                            "302": 12
                        },
                        "data": {
                            "sent": 33213421,
                            "received": 344343333
                        },
                        "health": {
                            "fails": 0,
                            "unavailable": 0,
                            "downtime": 0
                        },
                        "sid": "<server_id>"
                    }
                },
                "keepalive": 2
            }
        }
    },
    "resolvers": {
        "resolver_zone": {
            "queries": {
                "name": 243,
                "srv": 2,
                "addr": 0
            },
            "responses": {
                "success": 342,
                "timedout": 1,
                "format_error": 0,
                "server_failure": 1,
                "not_found": 1,
                "unimplemented": 0,
                "refused": 1,
                "other": 0
            }
        }
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
20


## 第 22 页

    }
}
3.2. httpserver 基本指标
3.2.1. 配置方式
请参阅 开启 RESTful 接口。
3.2.2. 接口地址
使用 curl 命令或浏览器访问，获取全部指标。
curl http://ip:49151/thsapi/httpserver
也可按如下接口获得各个指标。
curl http://ip:49151/thsapi/httpserver/version
curl http://ip:49151/thsapi/httpserver/address
curl http://ip:49151/thsapi/httpserver/generation
curl http://ip:49151/thsapi/httpserver/load_time
curl http://ip:49151/thsapi/httpserver/pid
curl http://ip:49151/thsapi/httpserver/ppid
3.2.3. 响应信息
{
    "version":"6.0.1.0",
    "address":"127.0.0.1",
    "generation":1,
    "load_time":"2023-10-24T14:09:57.058Z",
    "pid":75,
    "ppid":74
 }
3.2.4. 指标说明
参数
类型
参数说明
version
string
当前运行的 THS 服务版本。
address
string
接受 API 请求的服务地址。
generation
number
自启动以来重新加载配置的总次数。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
21


## 第 23 页

参数
类型
参数说明
load_time
string
最后一次重新加载配置的时间，格式为 ISO 8601，分辨率为
毫秒级。
pid
number
当前 worker 进程 ID。
ppid
number
当前 worker 进程的父进程 ID（master 进程 id）。
3.3. license 指标
3.3.1. 配置方式
请参阅 开启 RESTful 接口。
3.3.2. 接口地址
使用 curl 命令或浏览器访问，获取全部指标。
curl http://ip:49151/thsapi/license_info
也可按如下接口获得各个指标。
curl http://ip:49151/thsapi/license_info/consumer_name
curl http://ip:49151/thsapi/license_info/project_name
curl http://ip:49151/thsapi/license_info/license_type
curl http://ip:49151/thsapi/license_info/create_date
curl http://ip:49151/thsapi/license_info/end_date
curl http://ip:49151/thsapi/license_info/version_number
3.3.3. 响应信息
{
    "consumer_name":"test",
    "project_name":"test",
    "license_type":"trial",
    "create_date":"2022-12-20",
    "end_date":"2023-12-20",
    "product_name":"TongHttpServer",
    "version_number":"6.0",
    "license_id":""
 }
3.3.4. 指标说明
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
22


## 第 24 页

参数
类型
参数说明
consumer_name
string
客户名。
project_name
string
项目名。
license_type
string
license 类型。
create_date
string
license 创建时间。
end_date
string
license 有效截止时间。
product_name
string
产品名。
version_number
string
版本号。
license_id
string
license ID。
3.4. 连接指标
3.4.1. 配置方式
请参阅 开启 RESTful 接口。
3.4.2. 接口地址
使用 curl 命令或浏览器访问，获取全部指标。
curl http://ip:49151/thsapi/connections
也可按如下接口获得各个指标。
curl http://ip:49151/thsapi/connections/accepted
curl http://ip:49151/thsapi/connections/dropped
curl http://ip:49151/thsapi/connections/active
curl http://ip:49151/thsapi/connections/idle
3.4.3. 响应信息
{
"accepted":4,
"dropped":0,
"active":1,
"idle":0
}
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
23


## 第 25 页

3.4.4. 指标说明
参数
类型
参数说明
accepted
number
接受的客户端连接总数。
dropped
number
丢弃的客户端连接总数。
active
number
当前活跃的客户端连接数。
idle
number
当前空闲的客户端连接数。
3.5. 共享内存 zone 的 slab 分配器指标
共享内存的使用信息，如：limit_conn、limit_req、HTTP cache、ssl_session_cache、upstream
zone、licensememory 等。
1. limit_conn_zone 配置
limit_conn_zone $binary_remote_addr zone=limit_conn_zone:10m;
2. limit_req_zone 配置
limit_req_zone $binary_remote_addr zone=limit_req_zone:10m rate=1r/s;
3. cache_zone 配置
proxy_cache cache_zone;
4. SSL zone 配置
ssl_session_cache    shared:SSL:1m;
5. upstream zone 配置
upstream backend {
    ...
    zone backend_zone 1m;
    ...
}
3.5.1. 配置方式
请参阅 开启 RESTful 接口。
3.5.2. 接口地址
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
24


## 第 26 页

使用 curl 命令或浏览器访问，获取全部指标。
curl http://ip:49151/thsapi/slabs/<zone>
也可按如下接口获得各<zone>指标。
curl http://ip:49151/thsapi/slabs/<zone>
<zone> 为共享内存名
3.5.3. 响应信息
{
    "pages": {
        "used":2,
        "free":2542
    },
    "slots": {
        "64": {
        "used":1,
        "free":63,
        "reqs":1,
        "fails":0
        }
    }
}
3.5.4. 指标说明
参数
类型
参数说明
pages
object
内存业统计信息。
used
number
当前使用的内存页数。
free
number
当前空闲的内存页数。
slots
object
内存槽的统计信息。slots 对象包含请求内存槽大小的字段（
例如：8、16、32 等，直到页面大小的一半）。
used
number
指定大小的当前使用内存槽的数量。
free
number
指定大小的空闲内存槽的数量。
reqs
number
尝试分配指定大小的内存槽的总次数。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
25


## 第 27 页

参数
类型
参数说明
fails
number
分配指定大小的内存槽失败的次数。
3.6. HTTP 虚拟主机指标
3.6.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 “编辑配置” 或单机控制台的 “文件编辑” 界面。
3. 在 server 块中，输入如下内容。
配置说明，请参阅 status_zone 指令说明。
    server {
        ...
        status_zone server_zone;
        ...
    }
配置示意图，如下所示。
4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
26


## 第 28 页

3.6.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 server zone 指标。
curl http://ip:49151/thsapi/http/server_zones/
也可按如下接口获得各 <zone> 指标。
curl http://ip:49151/thsapi/http/server_zones/<zone>
<zone> ：为共享内存名。
3.6.3. 响应信息
{
    "ssl": {
        "handshaked":4174,
        "reuses":0,
        "timedout":0,
        "failed":0
        },
    "requests": {
        "total":4327,
        "processing":0,
        "discarded":8
        },
    "responses": {
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
27


## 第 29 页

        "200":4305,
        "302":12,
        "404":4
        },
    "data": {
        "received":7777333,
        "sent":673773673
        }
}
3.6.4. 指标说明
参数
类型
参数说明
ssl
object
ssl 统计信息（当 server 配置 ssl 监听端口时返回）。
handshaked
number
SSL 握手成功的总数。
reuses
number
SSL 握手期间会话复用的总数。
timedout
number
SSL 握手超时次数。
failed
number
SSL 握手失败的总数。
requests
object
请求统计信息。
total
number
客户端请求总数。
processing
number
正在处理的客户端请求数。
discarded
number
在未发送响应的情况下完成的客户端请求总数。
response
object
响应统计信息。
<code>
number
响应状态码 <code>(100-599) 非 0 响应数。
xxx
number
其他状态码（100-599 以外状态码）非 0 响应数。
data
object
流量统计。
received
number
从客户端接收到的总字节数。
sent
number
发送到客户端的总字节数。
3.7. HTTP 路由指标
3.7.1. 配置方式
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
28


## 第 30 页

1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 “编辑配置” 或单机控制台的 “文件编辑” 界面。
3. 在要监控的 location 块中，输入如下内容。
配置说明，请参阅 status_zone 指令说明。
    server {
        ...
        location / {
            status_zone test_location_zone;
        }
        ...
    }
配置示意图，如下所示。
4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
29


## 第 31 页

3.7.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 location zone 指标。
curl http://ip:49151/thsapi/http/location_zones/
也可按如下接口获得各<zone>指标。
curl http://ip:49151/thsapi/http/location_zones/<zone>
<zone> ：为共享内存名。
3.7.3. 响应信息
{
    "requests": {
        "total":4258,
        "discarded":0
        },
    "responses": {
        "200":4257,
        "304":1
        },
    "data": {
        "received":5333300,
        "sent":333333544
        }
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
30


## 第 32 页

    }
3.7.4. 指标说明
请参阅 虚拟主机指标说明。
3.8. HTTP 集群指标
在 upstream 上下文中指定的 zone <zone> 指令可对指定的 upstream zone 进行统计。
配置示例，如下所示。
upstream upstream {
    zone upstream 1m;
    server backend.test.com service=test.tcp resolve max_conns=5;
    keepalive 4;
}
API：/status/http/upstreams/<zone>
其中，<zone> 是用 zone 指令指定的任何 upstream zone 的名称。
3.8.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 “编辑配置” 或单机控制台的 “文件编辑” 界面。
3. 在要监控的 upstream 块中配置 zone 参数。
若需要获得主动健康检查的指标，也需要配置 zone 并配置 health_check  指令。
配置示例，如下所示。
    upstream upstream {
        zone backend 1m;
        server 127.0.0.1:8080;
        keepalive 4;
        health_check interval=3000 rise=2 fall=5 timeout=1000 type=tcp;
    }
配置示意图，如下所示。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
31


## 第 33 页

4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
3.8.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 upstream zone 指标。
curl http://ip:49151/thsapi/http/upstream/
也可按如下接口获得各 upstream 指标。
curl http://ip:49151/thsapi/http/upstream/<upstream_name>
<upstream_name> ：为 upstream 名字。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
32


## 第 34 页

3.8.3. 响应信息
{
    "peers": {
        "127.0.0.1:8080": {
            "server": "127.0.0.1:8080",
            "backup": false,
            "weight": 1,
            "state": "up",
            "selected": {
                "current": 0,
                "total": 0
            },
            "responses": {},
            "data": {
                "sent": 0,
                "received": 0
            },
            "health": {
                "fails": 0,
                "unavailable": 0,
                "downtime": 0
            },
            "health_check": {
                "rise_count": 8,
                "fall_count": 0,
                "check_type": "tcp"
            },
            "sid": "5958c386bf5e9109ac10d2a628645aea"
        }
    },
    "keepalive": 0,
    "zone_name": "backend"
}
3.8.4. 指标说明
peers：object，包含 upstream 监控指标作为子对象，其名称是对应地址。
每个子对象的成员，如下所示。
一级参数
二级参数
类型
参数说明
server
-
string
由 server 指令设置的地址。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
33


## 第 35 页

一级参数
二级参数
类型
参数说明
service
-
string
服务名称，在 server 指令中设置的
service。
backup
-
bool
当为备份服务时为 “true”。
weight
-
number
在 server 指令中 weight 指定的权重
值。
state
-
string
上游服务的当前状态 “up”、“down” 或
“unavailable”(unavailable 表示达到
了max_fails)。
selected
-
object
调度统计。
current
number
当前连接数。
total
number
总连接数。
max_conns
-
number
设置的最大连接数。
responses
-
object
响应统计。
<code>
number
状态码为 <code>(100-599) 的非零响应
数。
xxx
number
其他状态码（100-599 以外状态码）的
非零响应数。
data
-
object
流量指标。
received
number
从该上游服务接收的总字节数。
sent
number
发送到该上游服务的总字节数。
health
-
object
健康指标。
fails
number
访问上游服务失败次数。
unavailable
number
由于到达 max_fails 而使上游服务不可用
的次数。
downtime
number
上游服务不可用无法被选择的总时间（
毫秒级）。
downstart
string
最后一次不可用的时间，格式为 ISO
8601。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
34


## 第 36 页

一级参数
二级参数
类型
参数说明
health_check
-
object
健康指标。
rise_count
number
检测连续成功的次数，失败后该值清
零。
fall_count
number
检测连续失败的次数，成功后该值清
零。
check_type
string
检测方式。
sid
-
string
配置的上游服务器 ID。
其它参数说明，如下表所示。
参数名
类型
参数说明
keepalive
number
当前缓存的连接数。
zone_name
string
zone 名称。
3.9. HTTP 缓存指标
3.9.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 “编辑配置” 或单机控制台的 “文件编辑” 界面。
3. 使用 proxy_cache  配置使用的 zone ，并使用 proxy_cache_path  设置缓存。
proxy_cache  可配置在 HTTP  、server  、location  块中。
配置示例，如下所示。
http {
    proxy_cache_path levels=2:2 keys_zone=test_cach_zone:30m max_size=32m inactive=60m
use_temp_path=off;
    server {
        ...
        proxy_cache test_cache_zone;
        ...
    }
}
配置示意图，如下所示。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
35


## 第 37 页

4. 单击 “保存” > “发布”，若提示成功，则表示配置完成。
3.9.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 caches zone 指标。
curl http://ip:49151/thsapi/http/caches/
也可按如下接口获得各 <zone> 指标。
curl http://ip:49151/thsapi/http/caches/<zone>
<zone> ：为共享内存名。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
36


## 第 38 页

3.9.3. 响应信息
{
    "cache_zone": {
        "size": 0,
        "cold": false,
        "hit": {
            "responses": 0,
            "bytes": 0
        },
        "stale": {
            "responses": 0,
            "bytes": 0
        },
        "updating": {
            "responses": 0,
            "bytes": 0
        },
        "revalidated": {
            "responses": 0,
            "bytes": 0
        },
        "miss": {
            "responses": 0,
            "bytes": 0,
            "responses_written": 0,
            "bytes_written": 0
        },
        "expired": {
            "responses": 0,
            "bytes": 0,
            "responses_written": 0,
            "bytes_written": 0
        },
        "bypass": {
            "responses": 0,
            "bytes": 0,
            "responses_written": 0,
            "bytes_written": 0
        }
    }
}
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
37


## 第 39 页

3.9.4. 指标说明
一级参数
二级参数
类型
说明
size
-
number
当前缓存的大小。
max_size
-
number
已配置的缓存最大大小限制。
cold
-
bool
当缓存加载程序从磁盘加载数据时，为
“true”。
hit
-
object
有效缓存响应统计信息
（proxy_cache_valid）。
responses
number
从缓存中读取的响应总数。
bytes
number
从缓存中读取的总字节数。
stale
-
object
从缓存中获取过期响应的统计信息
（proxy_cache_use_stale）。
responses
number
从缓存中读取的响应总数。
bytes
number
从缓存中读取的总字节数。
updating
-
object
更新响应时从缓存中获取的过期响应的
统计信息（proxy_cache_use_stale
updating）。
responses
number
从缓存中读取的响应总数。
bytes
number
从缓存中读取的总字节数。
revalidated
-
object
从缓存中获取的过期和重新验证的响应
的统计信息（proxy_cache_revalidate
）。
responses
number
从缓存中读取的响应总数。
bytes
number
从缓存中读取的总字节数。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
38


## 第 40 页

一级参数
二级参数
类型
说明
miss
-
object
缓存中未找到响应的统计信息。
responses
number
对应响应的总数。
bytes
number
从代理服务器读取的总字节数。
responses_written
number
写入缓存的响应总数。
bytes_written
number
写入缓存的总字节数。
expired
-
object
未从缓存中取出的过期响应的统计信
息。
responses
number
对应响应的总数。
bytes
number
从代理服务器读取的总字节数。
responses_written
number
写入缓存的响应总数。
bytes_written
number
写入缓存的总字节数。
bypass
-
object
未在缓存中查找的响应统计信息
（proxy_cache_bypass）。
responses
number
对应响应的总数。
bytes
number
从代理服务器读取的总字节数。
responses_written
number
写入缓存的响应总数。
bytes_written
number
写入缓存的总字节数。
3.10. HTTP 限速指标
3.10.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 “编辑配置” 或单机控制台的 “文件编辑” 界面。
3. 使用 limit_req_zone  配置限速。
配置示例，如下所示。
http {
    limit_req_zone $binary_remote_addr zone=limit_req_zone:10m rate=1r/s;
}
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
39


## 第 41 页

配置示意图，如下所示。
4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
3.10.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 limit_reqs zone 指标。
curl http://ip:49151/thsapi/http/limit_reqs/
也可按如下接口获得各 <zone> 指标。
curl http://ip:49151/thsapi/http/limit_reqs/<zone>
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
40


## 第 42 页

<zone> ：为共享内存名。
3.10.3. 响应信息
{
    "passed": 43434,
    "skipped": 0,
    "delayed": 34,
    "rejected": 44,
    "exhausted": 0
}
3.10.4. 指标说明
参数
类型
说明
passed
number
通过的请求总数。
skipped
number
密钥长度为0或超过 65535 字节的请求总数。
delayed
number
延迟请求的总数。
rejected
number
被拒绝的请求总数。
exhausted
number
由于zone存储空间耗尽而被拒绝的请求总数。
3.11. Stream 虚拟主机指标
3.11.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 ”编辑配置“ 或单机控制台的 “文件编辑” 界面。
3. 使用 status_zone  指令，请参阅 status_zone 说明。
配置示例，如下所示。
stream {
    server {
    ...
    status_zone stream_server_zone;
    ...
配置示意图，如下所示。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
41


## 第 43 页

4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
3.11.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 resolver zone 指标。
curl http://ip:49151/thsapi/stream/server_zones
也可按如下接口获得各 <zone> 指标。
curl http://ip:49151/thsapi/stream/server_zones/<zone>
<zone> ：为共享内存名。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
42


## 第 44 页

3.11.3. 响应信息
{
  "ssl": {
    "handshaked": 234,
    "reuses": 0,
    "timedout": 0,
    "failed": 0
  },
  "connections": {
    "total": 245,
    "processing": 1,
    "discarded": 0
  },
  "sessions": {
    "success": 245,
    "invalid": 0,
    "forbidden": 0,
    "internal_error": 0,
    "bad_gateway": 0,
    "service_unavailable": 0
  },
  "data": {
    "received": 275523,
    "sent": 53223233
  }
}
3.11.4. 指标说明
一级参数
二级参数
类型
说明
ssl
-
object
ssl 统计信息（当 server 配置 ssl 监听端
口时返回）。
handshaked
number
SSL 握手成功的总数。
reuses
number
SSL 握手期间会话复用的总数。
timedout
number
SSL 握手超时次数。
failed
number
SSL 握手失败的总数。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
43


## 第 45 页

一级参数
二级参数
类型
说明
connections
-
object
连接统计信息。
total
number
客户端连接总数。
processing
number
当前正在处理的客户端连接数。
discarded
number
在未创建会话的情况下完成的客户端连
接总数。
sessions
-
object
会话统计信息。
success
number
code 为 200 完成的会话数，表示成功完
成。
invalid
number
code 为 400 完成的会话数，发生在客户
端数据无法解析时。例如：代理协议
头。
forbidden
number
当访问被禁止时。例如，当对某些客户
端地址的访问受到限制时，code 为 403 
完成的会话数。
internal_error
number
code 为 500 完成的会话数，内部服务器
错误。
bad_gateway
number
code 为 502 (例如，无法选择或到达上
游服务器)完成的会话数。
service_unavailabl
e
number
code为503完成的会话数，服务不可用。
例如，当访问受连接数限制时。
data
-
object
流量统计信息。
received
number
从客户端接收到的总字节数。
sent
number
发送到客户端的总字节数。
3.12. Stream 集群指标
3.12.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台 “编辑配置” 或单机控制台的 “文件编辑” 界面。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
44


## 第 46 页

3. 在 upstream 中使用 zone  配置。
配置示例，如下所示。
upstream backend {
    zone backend 1m;
    server 127.0.0.1:1234;
}
配置示意图，如下所示。
4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
45


## 第 47 页

3.12.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 resolver zone 指标。
curl http://ip:49151/thsapi/stream/
也可按如下接口获得各 upstream 指标。
curl http://ip:49151/thsapi/stream/upstreams/<upstream_name>
3.12.3. 响应信息
{
    "peers": {
        "127.0.0.1:8888": {
            "server": "backend.test.com",
            "service": "test.tcp",
            "backup": false,
            "weight": 5,
            "state": "up",
            "selected": {
                "current": 2,
                "total": 232
            },
            "max_conns": 5,
            "data": {
                "sent": 5434444,
                "received": 256466443
            },
            "health": {
                "fails": 0,
                "unavailable": 0,
                "downtime": 0
            },
            "health_check": {
                "rise_count": 5,
                "fall_count": 0,
                "check_type": "udp"
            }
        }
    }
}
3.12.4. 指标说明
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
46


## 第 48 页

peers：object，包含 upstream 监控指标作为子对象，其名称是对应地址。
每个子对象的成员，如下所示。
一级参数
二级参数
类型
说明
server
-
string
由 server 指令设置的地址。
service
-
string
服务名称，在 server 指令中设置的
service。
backup
-
bool
当为备份服务时为 “true”。
weight
-
number
在 server 指令中 weight 指定的权重
值。
state
-
string
上游服务的当前状态 “up”、“down” 或
“unavailable”(unavailable表示达到
了max_fails)。
selected
-
object
调度统计。
current
number
当前连接数。
total
number
总连接数。
max_conns
-
number
设置的最大连接数。
data
-
object
流量指标。
received
number
从该上游服务接收的总字节数。
sent
number
发送到该上游服务的总字节数。
health
-
object
健康指标。
fails
number
试图抵达上游服务失败次数。
unavailable
number
由于到达 max_fails 而使上游服务不可用
的次数。
downtime
number
上游服务不可用无法被选择的总时间（
毫秒级）。
downstart
string
最后一次不可用的时间，格式为 ISO
8601。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
47


## 第 49 页

一级参数
二级参数
类型
说明
health_check
-
object
主动健康检查指标。
rise_count
number
主动监测成功次数。
fall_count
number
主动监测失败次数。
check_type
string
检测方式 http/tcp/udp。
3.13. DNS 解析指标
3.13.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 “编辑配置” 或单机控制台的 “文件编辑” 界面。
3. 使用 resolver  配置 DNS 解析，请参阅resolver部分。
配置示例，如下所示。
resolver 127.0.0.53 status_zone=resolver_zone;
配置示意图，如下所示。
4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
48


## 第 50 页

3.13.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 resolver zone 指标。
curl http://ip:49151/thsapi/resolvers/
也可按如下接口获得各 <zone> 指标。
curl http://ip:49151/thsapi/resolvers/<zone>
<zone> ：为共享内存名。
3.13.3. 响应信息
{
    "queries": {
        "name":243,
        "srv":2,
        "addr":0
    },
    "responses": {
        "success":342,
        "timedout":1,
        "format_error":0,
        "server_failure":1,
        "not_found":1,
        "unimplemented":0,
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
49


## 第 51 页

        "refused":1,
        "other":0
    }
}
3.13.4. 指标说明
一级参数
二级参数
类型
说明
queries
-
object
查询次数统计。
name
number
将名称解析为地址的查询数量(A和AAAA
类型查询)。
srv
number
将服务解析为地址的查询数量(SRV类型
查询)。
addr
number
将地址解析为名称的查询数量(PTR类型
查询)。
responses
-
object
响应统计。
success
number
成功响应的次数。
timedout
number
查询超时的次数。
format_error
number
响应码为 1 的次数（格式错误）。
server_failure
number
响应码为 2 的次数（服务故障）。
not_found
number
响应码为 3 的次数（名称错误）。
unimplemented
number
响应码为 4 的次数（未实现）。
refused
number
响应码为 5 的次数（拒绝访问）。
other
number
响应码为其他非零值的查询数。
3.14. 限连指标
limit_conn 配置 zone 后，可收集对应的统计信息，配置如下所示。
limit_conn_zone $binary_remote_addr zone=limit_conn_zone:10m;
API：/status/http/limit_zones/<zone>, /status/stream/limit_zones/<zone>
分别对应 http 中配置 limit_conn 以及 stream 中配置有 limit_conn。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
50


## 第 52 页

3.14.1. 配置方式
1. 请参阅 开启 RESTful 接口。
2. 进入 THSManager 集中管控台的 “编辑配置” 界面，或单机控制台的 “文件编辑” 界面。
3. 使用 limit_conn_zone  配置限连。
配置示例，如下所示。
http {
    limit_conn_zone $binary_remote_addr zone=http_conn_zone:10m;
}
stream {
    limit_conn_zone $binary_remote_addr zone=stream_conn_zone:10m;
}
配置示意图，如下所示。
4. 单击 “保存” > “发布”，若提示成功，则说明配置完成。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
51


## 第 53 页

3.14.2. 接口地址
使用 curl 命令或浏览器访问，获取所有 limit_conn_zone zone 指标。
curl http://ip:49151/thsapi/http/limit_conns/
curl http://ip:49151/thsapi/stream/limit_conns/
也可按如下接口获得各 <zone> 指标。
curl http://ip:49151/thsapi/http/limit_conns/<zone>
curl http://ip:49151/thsapi/stream/limit_conns/<zone>
<zone> ：为共享内存名。
3.14.3. 响应信息
{
    "passed": 54,
    "skipped": 0,
    "rejected": 0,
    "exhausted": 0
}
3.14.4. 指标说明
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
52


## 第 54 页

参数
类型
说明
passed
number
通过的连接总数。
skipped
number
密钥长度为 0 或超过 255 字节的连接总数。
rejected
number
超过配置限制的连接总数。
exhausted
number
由于zone存储空间耗尽而拒绝的连接总数。
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
53


## 第 55 页

4. 导出监控指标（prometheus 格式）
TongHttpServer 支持灵活配置 prometheus 和 prometheus_templet 指令，并以 prometheus 格式导出监
控指标。
4.1. prometheus
分类
说明
指令
prometheus
语法
prometheus templet;
作用域
location
配置示例，如下所示。
location =/prometheus {
    prometheus templet;
}
其中，templet 需要通过 prometheus_templet 指令定义模板。
4.2. prometheus_templet
prometheus_templet 指令可定义由 THS 收集和导出已命名的指标模板；该模板与 prometheus 指令一起
使用。
分类
说明
指令
prometheus_templet
语法
prometheus_templet templet {…};
作用域
http
模板可以包含任意数量的指标定义，单个指标定义结构，如下所示。
<metric> <variable> path=<match> type=<type> help=<help>;
• metric
设置要以 prometheus 格式添加到响应中的度量标准的名称。可以包含一个可选的标签定义({…})，例
如:
http_requests_total{method="$1",code="$2"}
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
54


## 第 56 页

标签值可以使用 THS 内置变量；若 match 是一个正则表达式，标签值还可以使用正则捕获组。
• variable
设置要计算的变量的名称，并将其作为指标添加到响应中。
若没有这样的变量，或者结果值为空("")，则不添加指标。
• path=match
THS API 的 “/status” 之后与指标值相匹配的路径或正则表达式，例如：
'ths_http_server_zones_responses{zone="$1",code="$2"}' $prometheus_value
    path=~^/http/server_zones/([^/]+)/responses/([^/]+)$;
该示例模板导出 prometheus 格式指标，如下所示。
ths_http_server_zones_responses{zone="server_zone1",code="200"} 30
ths_http_server_zones_responses{zone="server_zone1",code="400"} 2
ths_http_server_zones_responses{zone="server_zone1",code="500"} 3
ths_http_server_zones_responses{zone="server_zone2",code="200"} 1
...
• type=<type>
prometheus 指标类型，如：counter、gauge。
• help=<help>
prometheus 指标提示信息。
4.3. $prometheus_value 内置变量
THS prometheus 模块有一个内置变量 $prometheus_value 。当 THS API 的 “/status” 部分中的路径与
prometheus_templet 指令定义指标的 match  选项进行匹配时，该变量会接收它的值。
$prometheus_value  的实际值可能为字符串，当不符合 prometheus 指标的格式时，可以使用 map  将字符串
转换为数值，例如：
map $prometheus_value $p8st_all_ups_state {
    "up"           1;
    "down"         2;
    "unavailable"  3;
    default        0;
}
prometheus_template main {
   'ths_stream_upstreams_peers_state{upstream="$1",peer="$2"}' $p8st_all_ups_state
      path=~^/stream/upstreams/([^/]+)/peers/([^/]+)/state$
      type=gauge
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
55


## 第 57 页

      'help=The current state of an upstream peer in "stream": 1 - up, 2 - down, or 3 - unavailable.';
}
4.4. 指标模板完整示例
在 THS 安装路径 “conf/prometheus_all.conf” 中包含了所有 THS prometheus 指标模板。
可参照如下配置：
http {
    include prometheus_all.conf;
    server {
        listen 8080;
        location =/prometheus {
            prometheus all;
        }
    }
}
东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
56


## 第 58 页

东方通负载均衡软件 TongHttpServer V6.0 监控配置手册
6015A01
版权所有©东方通
57



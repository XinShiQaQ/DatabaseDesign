# DatabaseDesign
This is for SCUT Database Course Design

这个repo暂时作为Django练手 随便玩随便整

考虑10月初找个时间开会确定下开发文档和细节 正式开始做

目前技术需求：

html/css

html和Django交互（表单的传递处理）

Mysql在Django的使用

搜索技术 -> 选用

oss在线储存服务（保存商品照片） -> 选用

Django服务服务器部署 -> 选用


文件构成：

./CourseDesign/templates 存放html文件

./CourseDesign/Ability 特定Ability功能（如Login）

./CourseDesign/CourseDesign 项目汇总设置


Table design:

UserAccount  储存用户账户密码

`CREATE TABLE Login_useraccount (userAccount varchar(15) NOT NULL PRIMARY KEY, userPassword varchar(15) NOT NULL);`

To Be Continue
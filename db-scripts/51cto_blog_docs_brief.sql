/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 80022
Source Host           : 127.0.0.1:3306
Source Database       : blog_documents

Target Server Type    : MYSQL
Target Server Version : 80022
File Encoding         : 65001

Date: 2021-09-06 10:12:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `51cto_blog_docs_brief`
-- ----------------------------
DROP TABLE IF EXISTS `51cto_blog_docs_brief`;
CREATE TABLE `51cto_blog_docs_brief` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blog_domain` varchar(255) DEFAULT NULL COMMENT '博客作者空间链接',
  `doc_title` varchar(100) DEFAULT NULL COMMENT '博客文章标题名称',
  `doc_brief` varchar(255) DEFAULT NULL COMMENT '博客文章摘要内容',
  `publish_date` varchar(50) DEFAULT NULL COMMENT '博文发布时间(字符串日期)',
  `context` text COMMENT '博客文档原文(text)',
  `html` text COMMENT '博客文档原文(html)',
  `old_data` text COMMENT '原始数据',
  `renew_data` text COMMENT '原始数据',
  `compare_data` text COMMENT '对比修改的差异的数据(具有操作的指向性)',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注信息',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `ext1` varchar(255) DEFAULT NULL COMMENT '扩展字段1',
  `ext2` varchar(255) DEFAULT NULL COMMENT '扩展字段2',
  `ext3` varchar(255) DEFAULT NULL COMMENT '文本扩展字段3',
  `status` tinyint DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1078 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='51CTO-博客文档列表内容';

-- ----------------------------
-- Records of 51cto_blog_docs_brief
-- ----------------------------

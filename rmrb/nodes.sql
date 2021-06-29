/*
 Navicat Premium Data Transfer

 Source Server         : datarequest
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : dataviz2021

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 16/06/2021 21:02:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for nodes
-- ----------------------------
DROP TABLE IF EXISTS `nodes`;
CREATE TABLE `nodes`  (
  `id` int(11) NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `image` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `intro` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of nodes
-- ----------------------------
INSERT INTO `nodes` VALUES (0, '张宪臣', 'zxc.jpg', '四人特工小组核心人员，和王郁是夫妻，他与张兰同组行动。两人在火车正面遭遇特务，最终携手反杀，逃过一劫。他在寻找破译密码母本的行动中，因寻找自己丢失多年的儿女而让敌人有了可乘之机。在受到敌人非人般的酷刑折磨后，他和卧底周乙联手布下险棋迷局并成功实施了乌特拉行动，最终他却牺牲了。');
INSERT INTO `nodes` VALUES (1, '周乙', 'zy.jpg', '表面上是伪满洲国哈尔滨特务科股长，实为潜伏在特务科的地下党特工人员，在张宪臣被捕后，他不得不冒着风险向二组传递信息，甚至险些暴露自己，但最后还是配合四人特工组完成了乌特拉行动并杀了叛徒。');
INSERT INTO `nodes` VALUES (2, '王郁', 'wy.jpg', '四人特工小组成员之一，入境后她和丈夫张宪臣有过约定，活着的那个人去寻找丢失的孩子。她和楚良组成的二组，却被特务科假扮的接头人给“软禁”了起来，后在楚良的掩护下顺利脱身。行动结束后，在周乙的帮助下和自己的孩子们团聚。');
INSERT INTO `nodes` VALUES (3, '王楚良', 'wcl.jpg', '四人特工小组成员之一，是一位高材生特工，和张兰是一对情侣。入境后和王郁一起成为二组成员，但他们这组却被特务科假扮的接头人给“软禁”了起来，后为了掩护共产党安插在特务科中的卧底周乙而服毒自尽了。');
INSERT INTO `nodes` VALUES (4, '张兰', 'zl.jpg', '四人特工小组成员之一，和王楚良是一对恩爱情侣，因为有着过目不忘的超强的记忆力而被选中参加行动。入境后和张宪臣一组行动，张宪臣被捕后，她在和周乙接上头后成功完成了乌特拉行动。');
INSERT INTO `nodes` VALUES (5, '高彬', 'gb.jpg', '伪满洲国哈尔滨特务科科长，此人心狠手辣且生性多疑，其阴鸷的目光中充满了杀气，让人不寒而栗，他在乌特拉行动小组执行任务的过程中设下重重障碍。');
INSERT INTO `nodes` VALUES (6, '鲁明', 'lm.jpg', '特务长官，重伤');
INSERT INTO `nodes` VALUES (7, '金志德', 'jzd.jpg', '伪满洲国哈尔滨特务科特务，做事比较粗心大意，受科长高彬的指派暗中死盯着周乙。最后，却反被周乙设计成了迷惑高彬的工具，最后被高彬下令枪毙。');
INSERT INTO `nodes` VALUES (8, '小孟', 'xm.jpg', '特务，科长心腹');
INSERT INTO `nodes` VALUES (9, '谢子荣', 'xzr.jpg', '地下党中的叛徒，在被特务科抓捕后，因怕死而背叛了组织，成了可耻的叛徒，向特务科泄露了乌特拉行动的相关信息并协助特务科追杀共产党特工，最后被周乙杀死。');
INSERT INTO `nodes` VALUES (10, '老冯', 'lf.jpg', '特务，被张宪臣用树枝打死');
INSERT INTO `nodes` VALUES (11, '张宪臣之子', 'zxczz.jpg', '乌特拉行动结束后与王郁相认');

SET FOREIGN_KEY_CHECKS = 1;

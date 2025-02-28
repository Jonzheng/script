/*
 Navicat Premium Data Transfer

 Source Server         : nikoni
 Source Server Type    : MySQL
 Source Server Version : 80036
 Source Host           : 129.204.165.23:3306
 Source Schema         : mhw

 Target Server Type    : MySQL
 Target Server Version : 80036
 File Encoding         : 65001

 Date: 27/02/2025 14:13:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for r_wp_craft
-- ----------------------------
DROP TABLE IF EXISTS `r_wp_craft`;
CREATE TABLE `r_wp_craft`  (
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '武器名称',
  `items` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '需要的材料',
  `unlock` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '' COMMENT '解锁条件',
  `buy` int NULL DEFAULT 1 COMMENT '购买金币',
  `zenny` int NULL DEFAULT 1 COMMENT '需要的金币',
  `create` tinyint(1) NULL DEFAULT 0 COMMENT '生产或强化',
  INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;

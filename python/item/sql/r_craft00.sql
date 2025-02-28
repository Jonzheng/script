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

 Date: 26/02/2025 11:50:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for r_craft
-- ----------------------------
DROP TABLE IF EXISTS `r_craft`;
CREATE TABLE `r_craft`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '调和结果',
  `quantity` int NULL DEFAULT NULL,
  `kv1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '原材料1',
  `kv2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '原材料2',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `unq`(`name`, `kv1`, `kv2`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 102 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;

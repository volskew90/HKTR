# HKTR ISO 20022 转换引擎 (HKTR Generator)

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

本项目是一个专门针对香港交易报告库 (HKTR) 报送要求的 ISO 20022 报文生成引擎。它能够将业务数据（CSV 格式）自动化转换为符合香港金融管理局 (HKMA) 规范的 `auth.030.001.04` (衍生品交易报告) XML 报文。

## 核心功能

- **自动化转换**：从 CSV/Excel 源数据到复杂嵌套 ISO 20022 XML 的一键转换。
- **合规性校验**：内置 XSD 架构校验（Schema Validation），确保生成的报文完全符合 HKMA 的技术规范。
- **强类型模型**：基于 `xsdata` 自动生成的数据模型，确保数据填充的精准度与代码的稳健性。
- **自定义映射**：支持通过 JSON 配置文件灵活定义业务字段与监管代码之间的映射关系。
- **高性能处理**：利用 `pandas` 和 `lxml` 高效处理大规模交易数据。

## 技术架构

- **语言**：Python 3.12+
- **包管理**：`uv` (高性能 Python 包管理器)
- **核心库**：
  - `xsdata`：用于 XML 到 Python 类对象的映射与序列化。
  - `pandas`：用于源数据读取与预处理。
  - `lxml`：用于高性能 XML 解析与 XSD 校验。

## 项目结构

```text
HKTR/
├── assets/                 # 资源文件
│   ├── auth_030_...xsd     # HKMA 官方 XSD 定义
│   ├── head_001_...xsd     # 业务报文头定义
│   └── mappings.json       # 业务字段映射配置
├── models/                 # 由 xsdata 生成的 ISO 20022 数据模型
├── converter.py            # 转换引擎核心逻辑
├── main.py                 # 项目入口脚本
├── input.csv               # 示例输入数据
├── pyproject.toml          # 项目依赖配置 (uv)
└── README.md               # 项目说明文档
```

## 安装指南

建议使用 `uv` 进行环境管理，以获得最佳性能。

1. **克隆仓库**：
   ```bash
   git clone https://github.com/volskew90/HKTR.git
   cd HKTR
   ```

2. **同步环境**：
   ```bash
   uv sync
   ```

## 使用说明

### 1. 准备数据
编辑 `input.csv`，确保包含项目所需的必要业务字段（如 `Trade_ID`, `Price` 等）。

### 2. 执行转换
运行主程序：
```bash
uv run python converter.py
```

### 3. 查看结果
程序将为每一行数据生成对应的 XML 文件，命名格式为 `HKTR_AUTH030_{TradeID}_{Timestamp}.xml`。生成的报文会自动经过 XSD 校验，校验结果将直接在终端显示。

## 校验机制

系统会自动加载 `assets/` 目录下的 `.xsd` 文件进行合规性检查。如果生成的数据不符合 HKMA 规范（例如字段长度、正则表达式不匹配或遗漏必填项），程序将详细列出错误的行号与具体原因。

## 映射配置

映射逻辑位于 `assets/mappings.json`。您可以根据实际业务代码调整此文件，例如将内部的机构代码映射为标准的 LEI 编码。

## 免责声明

本项目仅供学习与参考使用。在生产环境中报送监管数据前，请务必根据最新的 HKTR 技术文档进行全面的回归测试。

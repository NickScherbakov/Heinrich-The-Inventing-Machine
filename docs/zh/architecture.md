# 系统架构

🚧 **本文档正在翻译中**

完整的中文文档即将推出。目前，请参考[英文文档](../en/architecture.md)获取完整信息。

## 概述

Heinrich实现了模块化、可解释的TRIZ推理流程，将经典方法论与现代AI能力相结合。

## 系统组件

### 1. 核心流程 (heinrich/pipelines/)

实现TRIZ方法论的七个顺序模块

### 2. 知识库 (heinrich/knowledge/)

在结构化文件中组织的TRIZ知识

### 3. LLM集成 (heinrich/llm/)

多个LLM提供商的灵活集成层

### 4. 代理系统 (heinrich/agents/)

编排多步推理

### 5. 实用工具 (heinrich/utils/)

共享基础设施

## 了解更多

- **英文完整文档**: [Architecture (English)](../en/architecture.md)

---

如果您想帮助完成此翻译，请访问我们的[GitHub仓库](https://github.com/NickScherbakov/Heinrich-The-Inventing-Machine)。

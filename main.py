# OpenClaw 核心代码

## 说明

这是 OpenClaw 的核心框架代码。完整代码请参考各个技能目录：

- `skills/unified-workflow-engine/` - 工作流引擎
- `skills/mcp-adapter/` - MCP 协议实现
- `skills/unified-obsidian/` - Obsidian 集成
- `skills/unified-memory-system/` - 记忆系统

## 安装

```bash
pip install -r requirements.txt
```

## 使用

```python
from openclaw import WorkflowEngine

# 创建工作流
engine = WorkflowEngine()
result = engine.run('workflow.yaml')
```

## 文档

详见 [README.md](README.md)
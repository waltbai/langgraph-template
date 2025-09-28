# LangGraph Template

Template project for LangGraph-based agent development.

## Setup

Use uv to setup environment and install dependencies:

```shell
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
uv sync
```

## Usage

Use in command line:

```shell
uv run cli
```

Start server:

```shell
uv run server
```

Test cases:

```shell
uv run pytest
```

## Customize

### Modify project name

Folder names modification :

| Origin | Custom |
| --- | --- |
| `./src/example` | `./src/PROJECT_NAME` |
| `./packages/example-server` | `./packages/PROJECT_NAME-server` |
| `./packages/example-server/src/example_server` | `./packages/PROJECT_NAME-server/src/PROJECT_NAME_server` |

Project file (`./pyproject.toml`) modification:

| section | Origin | Custom |
| --- | --- | --- |
| `[project]` | `name=example` | `name="PROJECT_NAME"` |
| `[project]` | `dependencies=["example-server",...]` |  `dependencies=["PROJECT_NAME-server",...]` |
| `[project.scripts]` | `server = "example_server.app:main"` | `server = "PROJECT_NAME_server.app:main"` |
| `[project.scripts]` | `cli = "example.cli:main"` | `cli = "PROJECT.cli:main"` |
| `[tool.uv.sources]` | `example-server = { workspace = true }` | `PROJECT_NAME-server = { workspace = true }` |

### Modify agent

Some core definitions are in:

- `src/example/state.py`: Agent input/output/inner states.
- `src/example/context.py`: Agent context.
- `src/example/graph.py`: Agent workflow.
- `src/example/mcp/`: Agent tools via MCP protocol.

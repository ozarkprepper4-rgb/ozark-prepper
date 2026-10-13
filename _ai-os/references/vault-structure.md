# Vault Structure

## The 7-Layer Namespace Architecture

The AI OS vault is organized into 7 layers, each with its own namespace folder under `_ai-os/`:

```
_ai-os/
├── canon/                  # Principles and rules
│   ├── core-doctrine.md    # Identity, foundation, values
│   ├── agent-load-order.md # Who runs in what order
│   └── system-overview.md  # Master architecture diagram
├── tools/                  # Capabilities
│   └── README.md           # Tool registry
├── memory/                 # Knowledge storage
│   └── README.md           # Memory principles and protocol
├── projects/               # What is being built
│   └── INDEX.md            # Project index
├── workflows/              # How work gets done
│   └── README.md           # Workflow definitions
├── sessions/               # How I track tasks
│   └── README.md           # Session protocol
└── operators/              # People in the system
    └── INDEX.md            # Operator profile and state
```

## Layer Responsibilities

| Layer | Purpose | Key Files |
|-------|---------|-----------|
| canon | Core principles, agent hierarchy, architecture | core-doctrine.md, agent-load-order.md |
| tools | Capability catalog | tools/README.md |
| memory | Knowledge and facts | memory/README.md |
| projects | Task tracking | projects/INDEX.md |
| workflows | Repeatable processes | workflows/README.md |
| sessions | Session records | sessions/README.md |
| operators | People and state | operators/INDEX.md |

## Reading Order

To understand the system, read in this order:
1. canon/core-doctrine.md — what I am and why
2. canon/agent-load-order.md — who runs and in what order
3. tools/README.md — what I can do
4. memory/README.md — how I remember
5. projects/INDEX.md — what I am working on
6. workflows/README.md — how I get things done
7. sessions/README.md — how I track what happened
8. operators/INDEX.md — who Neil is and what he wants

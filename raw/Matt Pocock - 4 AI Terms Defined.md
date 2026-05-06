Source: Matt Pocock (@mattpocockuk)
Date: 2026-05-04 (implied by session date)
URL: https://twitter.com/mattpocockuk/status/... (mocked/implied)

4 of the most confusing terms in AI, defined:

Model: a blob of parameters, written during training. Does next-token prediction and nothing else. Stateless.

Harness: everything around the model that turns it into an agent: tools, system prompt, context window management, etc.

Environment: the world the agent acts on. Anything outside the harness that the agent perceives and acts on via tools.

Agent: a model, harnessed, in an environment.

---

Opus is a model.

Claude Code and Claude Web are different agents, because their harnesses differ - even though the models are the same.

The file system is an environment. MCP servers add tools to the environment.

---
title: Evgeni Chasnovski
type: entity
tags: [neovim, open-source, lua]
created: 2026-04-17
updated: 2026-04-17
sources: [vim-pack-guide.md]
---

# Evgeni Chasnovski

[[neovim|Neovim]] plugin author best known for **mini.nvim**, a collection of ~40 small, independent Lua modules each solving one editor problem (completion, statusline, file explorer, pick, snippets, etc.). Maintains a technical blog at [echasnovski.com](https://echasnovski.com).

## Notable work

- **mini.nvim** — modular plugin suite (`mini.basics`, `mini.completion`, `mini.cmdline`, `mini.snippets`, `mini.pick`, `MiniMisc`, many others). Known for composability, zero-dependency modules, and high test coverage.
- **mini.deps** — minimal Neovim plugin manager; conceptual predecessor to the built-in [[vim-pack]].
- **Colorschemes** — `miniwinter`, part of `mini.colors`.

## Influence on vim.pack

mini.deps informed several [[vim-pack]] design choices — the small API surface, lockfile-centered reproducibility, and the insistence on keeping the config file as the source of truth. The 2026-03-13 blog post [[vim-pack-guide|A Guide to vim.pack]] documents both vim.pack itself and migration from mini.deps.

## Style and philosophy

Advocates **moderate lazy loading** — warns that aggressive startup optimization usually costs more in config complexity than it saves in milliseconds. Favors mechanical transparency over declarative DSLs; the user should be able to read the config top-to-bottom and see exactly what happens.

## See also

- [[vim-pack]]
- [[vim-pack-guide]]
- [[neovim]]
- [[plugin-manager]]

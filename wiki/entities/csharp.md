---
title: C#
type: entity
tags: [csharp, dotnet, programming-languages, microsoft]
created: 2026-04-15
updated: 2026-04-15
sources: [csharp-14-whats-new.md]
---

# C#

C# is Microsoft's statically-typed, object-oriented programming language for the .NET platform. Release cadence is annual, with each version tied to a corresponding .NET release.

## Current version

**C# 14** — latest release, ships with **.NET 10**, supported in Visual Studio 2026 and the .NET 10 SDK. See [[csharp-14-whats-new]] for the full feature list.

## C# 14 headline additions

- [[extension-members]] — generalized extensions: properties, static members, operators
- [[field-keyword]] — `field` inside property accessors for auto-synthesized backing fields
- Null-conditional assignment (`customer?.Order = ...`)
- First-class implicit conversions for `Span<T>` / `ReadOnlySpan<T>`
- Lambda parameter modifiers (`ref`, `out`, `scoped`...) without explicit types
- `partial` constructors and events
- User-defined compound assignment operators
- `nameof` with unbound generics (`nameof(List<>)`)

## Versioning notes

Each C# version targets a specific .NET base class library. C# 14 requires .NET 10; older frameworks remain on earlier language versions. Configurable via `<LangVersion>` in the project file.

## See also

- [[csharp-14-whats-new]]
- [[extension-members]]
- [[field-keyword]]

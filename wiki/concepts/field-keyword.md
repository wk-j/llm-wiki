---
title: The `field` Keyword (C#)
type: concept
tags: [csharp, language-features, properties]
created: 2026-04-15
updated: 2026-04-15
sources: [csharp-14-whats-new.md]
---

# The `field` Keyword

Introduced in [[csharp|C#]] 14, `field` is a contextual keyword usable inside a property accessor body. It refers to a **compiler-synthesized backing field** for that property, eliminating the need to declare a `private` backing field by hand whenever you want custom accessor logic.

## The problem it solves

Before C# 14, any property that needed custom get/set logic (validation, lazy initialization, change notification) required explicitly declaring a backing field:

```csharp
private string _msg;
public string Message
{
    get => _msg;
    set => _msg = value ?? throw new ArgumentNullException(nameof(value));
}
```

The `_msg` field added naming noise, had to stay in sync with the property, and polluted the type's member list.

## With `field`

```csharp
public string Message
{
    get;
    set => field = value ?? throw new ArgumentNullException(nameof(value));
}
```

The compiler synthesizes the backing field. You can provide a custom body for **one or both** accessors — here the `get` is auto-implemented while `set` validates.

## Disambiguation

`field` is a contextual keyword, so a pre-existing identifier named `field` in scope could cause confusion or a breaking change. Two escape hatches:

- Use `@field` to force identifier interpretation
- Use `this.field` when referring to a member named `field`
- Or simply rename the clashing symbol

## Related

- Complements C# 9+ auto-property init and C# 11 required members
- Pairs naturally with nullability annotations and validation patterns

## See also

- [[csharp]]
- [[csharp-14-whats-new]]
- [[extension-members]]

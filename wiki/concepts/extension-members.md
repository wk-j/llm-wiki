---
title: Extension Members (C#)
type: concept
tags: [csharp, language-features, extensions]
created: 2026-04-15
updated: 2026-04-15
sources: [csharp-14-whats-new.md]
---

# Extension Members

Extension members, introduced in [[csharp|C#]] 14, generalize the decade-old *extension method* feature. A new `extension<T>(Receiver)` block can contain extension **methods**, **properties**, **static members**, and **operators** — all written in a static class but callable as though they belong to the extended type.

## Why this matters

Extension methods (C# 3.0) let you bolt instance-style methods onto types you didn't author, but the feature was limited to methods. There was no way to add a computed property, a static factory, or an operator to someone else's type without inheritance or wrapper types. C# 14 closes that gap.

## Syntax

Extension blocks live inside a `static class`. Two forms:

```csharp
public static class Enumerable
{
    // Instance-receiver block: members behave like instance members
    extension<TSource>(IEnumerable<TSource> source)
    {
        public bool IsEmpty => !source.Any();
        public IEnumerable<TSource> Where(Func<TSource, bool> predicate) { ... }
    }

    // Type-receiver block: members behave like static members of the receiver
    extension<TSource>(IEnumerable<TSource>)
    {
        public static IEnumerable<TSource> Combine(IEnumerable<TSource> a, IEnumerable<TSource> b) { ... }
        public static IEnumerable<TSource> Identity => Enumerable.Empty<TSource>();
        public static IEnumerable<TSource> operator +(IEnumerable<TSource> a, IEnumerable<TSource> b) => a.Concat(b);
    }
}
```

## Member kinds

| Kind | Instance-receiver | Type-receiver |
|---|---|---|
| Method | `sequence.Where(...)` | `IEnumerable<int>.Combine(a, b)` |
| Property | `sequence.IsEmpty` | `IEnumerable<int>.Identity` |
| Operator | — | `a + b` on `IEnumerable<T>` |

## Call sites

- Instance-receiver members look like instance calls: `sequence.IsEmpty`
- Type-receiver members look like static calls on the extended type: `IEnumerable<int>.Identity`
- User-defined extension operators bind like normal operators at the call site

## Relation to extension methods

Traditional `this`-parameter extension methods (C# 3.0) still work. The new syntax is additive and more expressive — the old form can be mechanically expressed in the new one, but the new form is required for properties, static members, and operators.

## See also

- [[csharp]]
- [[csharp-14-whats-new]]
- [[field-keyword]]

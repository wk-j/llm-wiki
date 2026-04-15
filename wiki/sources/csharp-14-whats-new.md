---
title: "What's new in C# 14"
type: source
tags: [csharp, dotnet, language-features, programming-languages]
created: 2026-04-15
updated: 2026-04-15
sources: [What's new in C 14.md]
---

# What's new in C# 14

Source: [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-14), authored by Bill Wagner. C# 14 ships with .NET 10 and is the latest C# release.

## Feature list

1. [[extension-members|Extension members]] — new `extension` block syntax
2. Null-conditional assignment (`?.` / `?[]` on the left-hand side)
3. `nameof` supports unbound generic types
4. More implicit conversions for `Span<T>` and `ReadOnlySpan<T>`
5. Modifiers on simple (untyped) lambda parameters
6. [[field-keyword|`field` backed properties]]
7. `partial` events and constructors
8. User-defined compound assignment operators
9. New preprocessor directives for file-based apps

## Feature details

### Extension members

New `extension<T>(Receiver)` block syntax extends beyond extension methods to:

- Extension **properties** (instance-style, e.g. `sequence.IsEmpty`)
- **Static** extension members — called as `IEnumerable<int>.Identity`, not on an instance
- User-defined **operators** as static extension methods (e.g. `operator +` on `IEnumerable<T>`)

Example:

```csharp
extension<TSource>(IEnumerable<TSource> source)
{
    public bool IsEmpty => !source.Any();
    public IEnumerable<TSource> Where(Func<TSource, bool> predicate) { ... }
}

extension<TSource>(IEnumerable<TSource>)  // receiver type only
{
    public static IEnumerable<TSource> Identity => Enumerable.Empty<TSource>();
    public static IEnumerable<TSource> operator +(IEnumerable<TSource> a, IEnumerable<TSource> b) => a.Concat(b);
}
```

See [[extension-members]].

### The `field` keyword

Contextual keyword inside property accessors that references a compiler-synthesized backing field — removes the boilerplate of writing `private T _x;` by hand.

```csharp
// Before
private string _msg;
public string Message
{
    get => _msg;
    set => _msg = value ?? throw new ArgumentNullException(nameof(value));
}

// C# 14
public string Message
{
    get;
    set => field = value ?? throw new ArgumentNullException(nameof(value));
}
```

Potential breaking change if a type already has an identifier named `field`; disambiguate with `@field` or `this.field`. See [[field-keyword]].

### Null-conditional assignment

`?.` and `?[]` now work on the left-hand side of `=` and compound assignments (`+=`, `-=`, etc.) — but not `++`/`--`.

```csharp
// Before
if (customer is not null) customer.Order = GetCurrentOrder();

// C# 14
customer?.Order = GetCurrentOrder();
```

The right-hand side is only evaluated when the left isn't null.

### `nameof` + unbound generics

`nameof(List<>)` now evaluates to `"List"`. Previously required a closed generic like `List<int>`.

### Implicit span conversions

First-class language support for `System.Span<T>` and `System.ReadOnlySpan<T>`: new implicit conversions between `Span<T>`, `ReadOnlySpan<T>`, and `T[]`. Span types can now be extension method receivers and compose with other conversions and generic type inference.

### Lambda parameter modifiers without types

Modifiers like `scoped`, `ref`, `in`, `out`, `ref readonly` no longer force you to spell out every parameter type:

```csharp
TryParse<int> parse = (text, out result) => Int32.TryParse(text, out result);
```

`params` still requires explicit types.

### Partial events and constructors

`partial` now applies to instance constructors and events alongside partial methods/properties. Rules:

- Exactly one defining declaration and one implementing declaration
- Only the implementing constructor can include `: this()` / `: base()`
- Only one partial declaration can include primary constructor syntax
- Implementing partial events must provide `add`/`remove` accessors; the defining declaration declares a field-like event

### User-defined compound assignment

Allows types to define their own `+=`, `-=`, etc. behavior directly (distinct from just overloading `+` and synthesizing `+=`).

### Preprocessor directives for file-based apps

New preprocessor directives specifically for file-based apps (single-file scripts / `dotnet run file.cs` scenarios).

## Release context

- Latest release; ships with [[csharp|C#]] on **.NET 10**
- Available in **Visual Studio 2026** and the **.NET 10 SDK**
- Breaking changes documented separately in the compiler breaking-changes article

## See also

- [[csharp]]
- [[extension-members]]
- [[field-keyword]]

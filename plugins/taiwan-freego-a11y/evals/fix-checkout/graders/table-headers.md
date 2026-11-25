---
type: regex
pattern: 'headers="product missing"'
match: not_contains
target: { source: file, path: checkout.html }
---

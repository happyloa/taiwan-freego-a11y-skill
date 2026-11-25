---
type: regex
pattern: 'onpaste\s*=\s*"event\.preventDefault\(\)"'
match: not_contains
target: { source: file, path: checkout.html }
---

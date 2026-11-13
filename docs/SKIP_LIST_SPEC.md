# Concurrent Skip List Specification 📑

## 1. Complexity
- Search: $O(\log N)$ average
- Insert/Delete: $O(\log N)$ average
- Concurrency: Fine-grained pointer CAS (Compare-And-Swap) operations.

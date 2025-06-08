# Why Return `l`?

You're searching for the **smallest value of `k`** such that Koko finishes within `h` hours.

## Binary Search Logic

- **If** `total_hours > h`:  
    This `mid` is too slow  
    → Need to try higher speeds  
    → `l = mid + 1`

- **If** `total_hours <= h`:  
    This `mid` works  
    → Try to find a smaller one  
    → `r = mid - 1`

You are shrinking the search range such that:

- All `k < l` are **invalid**
- All `k >= l` **could be valid**

When the loop ends (`l > r`), `l` is pointing at the **first valid speed** — the answer ✅

---

## Example Walkthrough

Let's walk through this with:

```python
piles = [3, 6, 7, 11]
h = 8
# Initial range: l = 1, r = 11
```

| l | r  | mid | total_hours      | Action   |
|---|----|-----|------------------|----------|
| 1 | 11 | 6   | 1+1+2+2 = 6 ≤ 8  | r = 5    |
| 1 | 5  | 3   | 1+2+3+4 = 10 > 8 | l = 4    |
| 4 | 5  | 4   | 1+2+2+3 = 8 ≤ 8  | r = 3    |

🔚 **Exit:** `l = 4`, `r = 3` → loop ends.

✅ **Return** `l = 4` — the minimum valid speed.

---

## 🧩 Key Insight

You **never store a separate answer variable**.

Instead, you're using the fact that `l` will land on the **smallest `k`** such that `total_hours(k) <= h`.

---

## ✅ Summary

| Concept                  | Explanation                                 |
|--------------------------|---------------------------------------------|
| Binary search type       | Closed interval: `while l <= r`             |
| Goal                     | Find smallest valid eating speed `k`         |
| When `total_hours > h`   | `mid` is too small → `l = mid + 1`          |
| When `total_hours <= h`  | `mid` might work → `r = mid - 1`            |
| Why return `l`?          | It's the smallest `k` that works            |
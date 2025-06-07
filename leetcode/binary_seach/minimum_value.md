# Explanation of Binary Search in Rotated Sorted Array

## Code Context

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
```

---

## Why `while left < right` and not `while left <= right`?

- The loop continues as long as there are at least two elements in the search window (`left < right`).
- When `left == right`, the search window has only one element, which must be the minimum, so the loop stops.
- Using `left <= right` might cause unnecessary extra iterations or require more careful pointer updates to avoid infinite loops.
- For this problem, stopping when one element remains is sufficient and cleaner.

---

## Why update `right = mid` instead of `right = mid - 1`?

- When `nums[mid] < nums[right]`:
  - The minimum could be at `mid` or to the left of `mid`.
  - So we **keep `mid` in the search** by setting `right = mid`.
- If we used `right = mid - 1`, we risk **excluding the minimum element** if it happens to be at `mid`.
- When `nums[mid] >= nums[right]`:
  - The minimum cannot be at `mid`.
  - So we safely exclude `mid` by setting `left = mid + 1`.

---

## Summary Table

| Condition                  | Pointer Update        | Reason                                  |
|----------------------------|----------------------|-----------------------------------------|
| `nums[mid] < nums[right]`  | `right = mid`        | Minimum **could be at `mid`**, keep it  |
| `nums[mid] >= nums[right]` | `left = mid + 1`     | Minimum **not at `mid`**, exclude it    |
| Loop condition             | `while left < right` | Stop when one element remains            |

---

## Why this approach works

- The rotated sorted array consists of two sorted parts joined at the pivot (minimum).
- By comparing `nums[mid]` and `nums[right]`, the algorithm determines which half contains the minimum.
- It narrows the search range without skipping the minimum element.
- The search ends when the minimum is isolated.
- Overall time complexity: **O(log n)**.

---

## Example Walkthrough

For `nums = [4, 5, 6, 7, 1, 2, 3]`:

- `left = 0`, `right = 6`
- `mid = 3` → `nums[mid] = 7`, `nums[right] = 3`
- `7 >= 3` → minimum is right half → `left = mid + 1 = 4`
- `left = 4`, `right = 6`
- `mid = 5` → `nums[mid] = 2`, `nums[right] = 3`
- `2 < 3` → minimum could be at mid → `right = mid = 5`
- `left = 4`, `right = 5`
- `mid = 4` → `nums[mid] = 1`, `nums[right] = 2`
- `1 < 2` → minimum could be at mid → `right = mid = 4`
- `left = 4`, `right = 4` → loop ends
- Return `nums[4] = 1` as minimum element.

---

If you want, I can provide examples of what goes wrong if you try other pointer updates or loop conditions.


# Sliding Window Patterns Comparison

### 🔹 1. Longest Substring Without Repeating Characters
**Goal:** Find the longest substring with **no repeating characters**.

- **Window Rule:** Shrink the window when a character repeats.
- **Key Check:** `if s[j] in window`
- **Data Structure:** Set or dictionary to track characters.
- **Pattern:** Dynamic window size, always valid.

🧠 **Memory Tip:**  
> “No repeats allowed — kick out duplicates immediately.”

---

### 🔹 2. Longest Repeating Character Replacement
**Goal:** Find the longest substring where you can **replace at most `k` characters** to make all characters the same.

- **Window Rule:** Shrink the window when `window size - maxFreq > k`
- **Key Check:** `if (j - i + 1) - maxFreq > k`
- **Data Structure:** Dictionary to count character frequencies.
- **Pattern:** Dynamic window size, may temporarily be invalid but fixed by shrinking.

🧠 **Memory Tip:**  
> “Allow up to `k` mistakes — fix them by shrinking the window.”

---

### 🔹 3. Permutation in String
**Goal:** Check if `s1`'s permutation exists in `s2`.

- **Window Rule:** Fixed window size = `len(s1)`
- **Key Check:** Compare frequency maps of `s1` and current window in `s2`
- **Data Structure:** Two dictionaries (or arrays) for frequency comparison.
- **Pattern:** Fixed-size window, slide one character at a time.

🧠 **Memory Tip:**  
> “Look for an exact match — same letters, same counts, fixed size.”

---

### 🧩 Summary Table

| Problem                             | Window Size     | Shrink When...                        | Data Structure     | Key Condition                        |
|-------------------------------------|------------------|----------------------------------------|---------------------|----------------------------------------|
| Longest Substring Without Repeat    | Dynamic          | Duplicate character found              | Set / Dict          | Char already in window                |
| Longest Repeating Char Replacement  | Dynamic          | Too many replacements needed           | Dict (char freq)    | `window size - maxFreq > k`           |
| Permutation in String               | Fixed (`len(s1)`) | Always slide after `len(s1)`           | Dict / Array        | `s1_count == s2_window_count`         |

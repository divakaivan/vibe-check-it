# vibe-check-it

How many times have you asked ChatGPT a question, received an answer, then asked “Are you sure?” - only for ChatGPT to give a different response? This package is designed for exactly those moments.

**vibe-check-it** is a lightweight Python utility that uses the coolest AI on the block - GPT-5 to verify the correctness of your vibe functions' outputs. Pass any function with inputs for it, and `vibe-check-it` will ask GPT-5, *"Are you sure this output is correct?"* - returning a boolean (`True` or `False`).

---

## Installation

```bash
pip install vibe-check-it
```

> **Note:** Requires an environment variable `OPENAI_API_KEY` with your OpenAI API key.

---

## Usage

```python
from vibesort import vibesort
from vibe_check_it import vibe_check_it

is_correct = vibe_check_it(vibesort, [2,3,4,1])

print(f"Output is correct? {is_correct}")
# True - vibesort's output was vibe-checked and it's correct
# False - seems GPT-5 wasn't sure the output is correct
```

---

## How it works

1. Calls your vibe function with the provided arguments.
2. Sends a prompt to GPT-5 with the function call, vibe result and arguments.
3. Asks GPT-5 to respond with a boolean (`True` or `False`) if the output is correct.
4. Parses and returns the AI's response.

---

## Requirements

* Python 3.10+
* Valid OpenAI API key set in environment variable `OPENAI_API_KEY`

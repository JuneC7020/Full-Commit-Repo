---
layout: post
title: "Python Code Highlighting & Blog Setup"
description: "Example post showing syntax highlighting, images, and easy posting workflow"
date: 2025-01-25
tags: [python, jekyll, blogging, setup]
categories: [python]
---

# Python Code Highlighting & Blog Setup

Welcome to your new Python blog! This post demonstrates the features we've set up for easy blogging.

## Code Examples

### Basic Python Function
```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

# Example usage
result = fibonacci(10)
print(f"First 10 Fibonacci numbers: {result}")
```

### List Comprehensions (Python Pro Tip!)
```python
# Traditional approach
squares = []
for x in range(10):
    squares.append(x**2)

# Pythonic approach with list comprehension
squares = [x**2 for x in range(10)]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]

print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")
```

### Dictionary Comprehensions
```python
# Create a dictionary mapping numbers to their squares
square_dict = {x: x**2 for x in range(1, 6)}

# Filter dictionary items
large_squares = {k: v for k, v in square_dict.items() if v > 10}

print(f"All squares: {square_dict}")
print(f"Large squares: {large_squares}")
```

## Inline Code Examples

Use `print()` for output, `len()` for length, and `range()` for sequences.

## Images

You can add images to your posts by placing them in `docs/assets/images/` and referencing them like this:

![Python Logo](https://www.python.org/static/img/python-logo.png)

## Easy Post Creation

To create a new post, simply run:

```bash
python create_post.py "Your Amazing Python Discovery"
```

This will:
- Create a new post file with today's date
- Use a template with proper front matter
- Generate a URL-friendly filename
- Include code highlighting setup

## Pro Tips for Blogging

> **💡 Pro Tip:** Always include code examples in your Python posts - they make concepts much clearer!

### Writing Tips:
1. **Start with a problem** - What Python challenge did you solve?
2. **Show the code** - Include working examples
3. **Explain the magic** - Why does this approach work?
4. **Share alternatives** - Show different ways to solve the same problem

## Categories and Tags

This post uses:
- **Categories**: `[python]` - for organizing posts
- **Tags**: `[python, jekyll, blogging, setup]` - for search and filtering

## Conclusion

Your blog is now set up with:
- ✅ Syntax highlighting for Python code
- ✅ Easy post creation script
- ✅ Image support
- ✅ Professional Jekyll theme
- ✅ SEO optimization

Happy blogging! 🐍✨

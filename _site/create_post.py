#!/usr/bin/env python3
"""
Easy post creation script for fullcommit blog
Usage: python create_post.py "My Post Title"
"""

import sys
import os
from datetime import datetime
import re

def slugify(title):
    """Convert title to URL-friendly slug"""
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def create_post(title):
    """Create a new blog post from template"""
    if not title:
        print("Usage: python create_post.py \"Your Post Title\"")
        return
    
    # Generate filename
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{today}-{slug}.md"
    filepath = os.path.join("docs", "_posts", filename)
    
    # Check if file already exists
    if os.path.exists(filepath):
        print(f"Post already exists: {filepath}")
        return
    
    # Read template
    template_path = os.path.join("docs", "_posts", "template.md")
    if not os.path.exists(template_path):
        print("Template not found. Creating basic template...")
        template_content = f"""---
layout: post
title: "{title}"
description: "Brief description of your post"
date: {today}
tags: [python, learning, tips]
categories: [python]
---

# {title}

Write your post content here...

## Code Examples

```python
def hello_world():
    print("Hello, fullcommit!")
    return "Python is awesome"

# Call the function
result = hello_world()
print(result)
```

## Images

![Alt text for your image](/fullcommit/assets/images/your-image.png)

## Conclusion

Wrap up your post here...
"""
    else:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        # Replace template placeholders
        template_content = template_content.replace("Your Post Title Here", title)
        template_content = template_content.replace("YYYY-MM-DD", today)
    
    # Write new post
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template_content)
    
    print(f"✅ Created new post: {filepath}")
    print(f"📝 Edit the file and add your content")
    print(f"🖼️  Add images to docs/assets/images/")
    print(f"🚀 Commit and push to publish")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        title = sys.argv[1]
        create_post(title)
    else:
        print("Usage: python create_post.py \"Your Post Title\"")
        print("\nExample:")
        print("python create_post.py \"Python List Comprehensions\"")

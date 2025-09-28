# fullcommit - Python Study Blog

A flexible blog for sharing Python studies, projects, and pro tips.

## 🚀 Quick Start

### Creating a New Post

```bash
python create_post.py "Your Post Title"
```

This creates a new post in `docs/_posts/` with:
- Proper front matter (date, tags, categories)
- Code highlighting setup
- Template structure

### Adding Images

1. Place images in `docs/assets/images/`
2. Reference them in posts: `![Alt text](/fullcommit/assets/images/filename.png)`

### Publishing

```bash
git add .
git commit -m "feat: new Python post about [topic]"
git push origin main
```

Your post will be live at: https://junec7020.github.io/fullcommit/

## 📁 Structure

```
docs/
├── _posts/           # Blog posts (Markdown)
├── assets/images/    # Images for posts
├── _config.yml       # Jekyll configuration
└── index.md          # Homepage

create_post.py        # Easy post creation script
```

## 🎨 Features

- **Syntax Highlighting**: Python code with line numbers
- **Responsive Design**: Works on all devices
- **SEO Optimized**: Meta tags and sitemap
- **Easy Publishing**: Simple git workflow
- **Image Support**: Drag and drop images

## 📝 Post Template

Each post includes:
- Front matter (title, description, date, tags)
- Code examples with syntax highlighting
- Image support
- Categories and tags for organization

## 🔧 Customization

Edit `docs/_config.yml` to:
- Change site title/description
- Add plugins
- Configure syntax highlighting
- Set up navigation

Happy blogging! 🐍✨

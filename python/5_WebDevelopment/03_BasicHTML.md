# 3. Basic HTML - Building Blocks of Web Pages

## Learning Objectives
By the end of this lesson, you will be able to:
- Use common HTML tags (headings, paragraphs, links, images, lists)
- Create well-structured HTML pages
- Add links between pages
- Understand semantic HTML

## What are HTML Tags?

HTML **tags** are like instructions that tell the browser how to display content. Each tag is wrapped in angle brackets `< >`.

### Common HTML Tags

#### Headings
Headings organize your content with different sizes. There are 6 levels (h1 to h6):

```html
<h1>This is the biggest heading</h1>
<h2>This is medium</h2>
<h3>This is smaller</h3>
```

**Use h1 for the main title of your page, h2 for sections, h3 for subsections, etc.**

#### Paragraphs
The `<p>` tag is used for regular text:

```html
<p>This is a paragraph of text that can be as long as you want.</p>
<p>This is another paragraph.</p>
```

#### Bold and Italic
Make text stand out with these tags:

```html
<b>This word is bold</b>
<i>This word is italic</i>
<strong>This is important (bold)</strong>
<em>This is emphasized (italic)</em>
```

#### Line Breaks
Create space between lines:

```html
<p>First line<br>Second line</p>
```

#### Horizontal Line
Add a divider:

```html
<hr>
```

#### Links
Create clickable links to other pages:

```html
<a href="https://www.google.com">Click here to go to Google</a>
<a href="about.html">Go to About page</a>
```

#### Images
Display pictures in your page:

```html
<img src="photo.jpg" alt="My Photo">
<img src="../images/picture.png" alt="A nice picture">
```

**Important:** The `alt` text describes the image if it doesn't load.

#### Lists
Create bullet points:

```html
<ul>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</ul>
```

Or numbered lists:

```html
<ol>
  <li>First step</li>
  <li>Second step</li>
  <li>Third step</li>
</ol>
```

## Complete Example Page

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Bio</title>
</head>
<body>
    <h1>Welcome to My Bio</h1>
    
    <h2>About Me</h2>
    <p>Hi! My name is <b>Sarah</b>. I am learning <i>web development</i>.</p>
    
    <h2>My Favorite Things</h2>
    <ul>
        <li>Programming</li>
        <li>Gaming</li>
        <li>Drawing</li>
    </ul>
    
    <h2>My Skills</h2>
    <ol>
        <li>Python programming</li>
        <li>HTML basics</li>
        <li>Problem solving</li>
    </ol>
    
    <h2>Connect With Me</h2>
    <p>Email me at: myemail@example.com</p>
    
    <hr>
    <p>© 2024 My Website</p>
</body>
</html>
```

## 🎯 Try It Yourself

Create a page about your **favorite hobby**:

1. Create a new file called `hobby.html`
2. Include:
   - An `<h1>` title like "My Favorite Hobby"
   - At least 3 paragraphs `<p>` describing it
   - Use `<b>` or `<strong>` for important words
   - Use `<i>` or `<em>` for emphasis
   - Create a list `<ul>` of 3-5 things you like about it
   - Add a link to a website about your hobby using `<a>`

3. Save and open in your browser
4. Make sure it looks good!

## Quick Reference Table

| Tag | Purpose | Example |
|-----|---------|---------|
| `<h1>...</h1>` | Big heading | `<h1>Main Title</h1>` |
| `<p>...</p>` | Paragraph | `<p>Text here</p>` |
| `<b>...</b>` | Bold text | `<b>Important</b>` |
| `<i>...</i>` | Italic text | `<i>Emphasis</i>` |
| `<a href="">...</a>` | Link | `<a href="page.html">Click me</a>` |
| `<img src="" alt="">` | Image | `<img src="pic.jpg" alt="Photo">` |
| `<ul><li>...</li></ul>` | Bullet list | `<ul><li>Item</li></ul>` |
| `<ol><li>...</li></ol>` | Numbered list | `<ol><li>Step</li></ol>` |
| `<hr>` | Line divider | `<hr>` |
| `<br>` | Line break | `Line1<br>Line2` |

## Example Reference
See [example_basicHTML.html](examples/example_basicHTML.html) for a working version with all these tags.

---

## Next Step
Ready to build something cool? Go to [Lesson 4: Project - Build Your About Me Page](04_Project_AboutMe.md)

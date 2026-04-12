# 5. Basic CSS - Make Your Pages Beautiful

## Learning Objectives
By the end of this lesson, you will be able to:
- Add colors and fonts to your web pages
- Use CSS to style HTML elements
- Understand selectors, properties, and values
- Create attractive, professional-looking pages

## What is CSS?

**CSS** (Cascading Style Sheets) is a language that makes web pages look good. While HTML creates the *structure*, CSS adds the *style*.

Think of it like this:
- **HTML** = Building frame and furniture (structure)
- **CSS** = Paint, decorations, and arrangement (style)

## How to Write CSS

There are 3 ways to add CSS to HTML:

### Method 1: Inline CSS (Inside HTML tags)

```html
<h1 style="color: blue; font-size: 40px;">Hello</h1>
<p style="color: red;">This is red text</p>
```

**Good for:** Quick testing. **Not recommended for:** Big projects.

### Method 2: Internal CSS (In the `<head>`)

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        h1 {
            color: blue;
            font-size: 40px;
        }
        p {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Hello</h1>
    <p>This is red text</p>
</body>
</html>
```

**Good for:** Simple pages. **Use:** When learning CSS.

### Method 3: External CSS (Separate .css file) ⭐ BEST!

**Create two files:**

`style.css`:
```css
h1 {
    color: blue;
    font-size: 40px;
}
p {
    color: red;
}
```

`index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello</h1>
    <p>This is red text</p>
</body>
</html>
```

**Good for:** Professional projects and big sites.

## CSS Basics: Selectors and Properties

### CSS Structure

```css
selector {
    property: value;
}
```

### Example:
```css
h1 {
    color: blue;        /* Property: value */
    font-size: 36px;    /* Another property */
}
```

## Common CSS Properties

### Text Colors
```css
h1 {
    color: blue;              /* Text color */
    background-color: yellow; /* Background color */
}
```

**Common colors:** red, blue, green, black, white, gray, orange, purple, pink, etc.

### Text Size
```css
h1 {
    font-size: 36px;          /* Large */
}
p {
    font-size: 14px;          /* Normal */
}
```

### Font Families
```css
p {
    font-family: Arial;        /* Simple, professional */
}

h1 {
    font-family: Georgia;      /* Fancy, serif */
}

body {
    font-family: "Comic Sans MS";  /* Fun, casual */
}
```

**Safe fonts:** Arial, Times New Roman, Georgia, Verdana, Comic Sans MS

### Bold and Italic
```css
strong {
    font-weight: bold;         /* Already bold, but explicit */
}
i {
    font-style: italic;
}
```

### Alignment
```css
h1 {
    text-align: center;        /* center, left, right */
}
```

### Spacing and Margins
```css
p {
    margin: 20px;              /* Space around element */
    padding: 10px;             /* Space inside element */
    line-height: 1.6;          /* Space between lines */
}
```

## Complete Example with CSS

```html
<!DOCTYPE html>
<html>
<head>
    <title>Styled Page</title>
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial;
            margin: 20px;
        }
        
        h1 {
            color: #0066cc;
            text-align: center;
            font-size: 36px;
        }
        
        h2 {
            color: #333333;
            border-bottom: 2px solid #0066cc;
            padding-bottom: 10px;
        }
        
        p {
            color: #555555;
            line-height: 1.8;
            font-size: 16px;
        }
        
        ul {
            color: #0066cc;
        }
    </style>
</head>
<body>
    <h1>Welcome!</h1>
    
    <h2>About This Page</h2>
    <p>This page has nice colors and formatting using CSS.</p>
    
    <h2>Features</h2>
    <ul>
        <li>Professional blue color</li>
        <li>Easy to read fonts</li>
        <li>Good spacing and layout</li>
    </ul>
    
    <p>Notice how much better this looks compared to plain HTML!</p>
</body>
</html>
```

## Color Codes

CSS supports 3 color formats:

```css
h1 {
    color: red;                /* Named color */
    color: #FF0000;            /* Hex code (red) */
    color: rgb(255, 0, 0);     /* RGB (red) */
}
```

**Hex Color Chart:**
- `#000000` = Black
- `#FFFFFF` = White
- `#FF0000` = Red
- `#00FF00` = Green
- `#0000FF` = Blue
- `#FFFF00` = Yellow
- `#FF00FF` = Magenta
- `#00FFFF` = Cyan

**Tip:** Use <https://www.w3schools.com/colors/colors_picker.asp>{:target="_blank"} to pick colors!

## 🎯 Try It Yourself

Style your About Me page:

1. Open your `aboutMe.html` file
2. Add a `<style>` section in the `<head>`
3. Add CSS rules for:
   - **body**: Set background color (light color like #f5f5f5) and font
   - **h1**: Make it big, centered, blue color
   - **h2**: Give it a bottom border, dark color
   - **p**: Set font size, text color
   - **ul**: Style the bullet points
   - **a**: Make links look nice (blue, underlined)

Example:
```html
<style>
    body {
        background-color: #f5f5f5;
        font-family: Arial;
    }
    h1 {
        color: #0066cc;
        text-align: center;
    }
    p {
        font-size: 16px;
        color: #333333;
    }
</style>
```

4. Save and refresh your browser
5. Watch your page transform! ✨

## Quick Reference

| Property | What it does | Example |
|----------|-----------|---------|
| `color` | Text color | `color: blue;` |
| `background-color` | Background | `background-color: yellow;` |
| `font-size` | Text size | `font-size: 20px;` |
| `font-family` | Font type | `font-family: Arial;` |
| `text-align` | Alignment | `text-align: center;` |
| `margin` | Space outside | `margin: 20px;` |
| `padding` | Space inside | `padding: 10px;` |
| `font-weight` | Bold/normal | `font-weight: bold;` |
| `font-style` | Italic/normal | `font-style: italic;` |
| `line-height` | Line spacing | `line-height: 1.8;` |

## Example Reference
See [example_styled_page.html](examples/example_styled_page.html) and [css/style.css](examples/css/style.css) for a working styled page.

---

## Next Step
Make your pages interactive! Go to [Lesson 6: Introduction to JavaScript](06_IntroJavaScript.md)

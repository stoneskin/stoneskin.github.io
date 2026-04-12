# 2. Build Your First Web Page

## Learning Objectives
By the end of this lesson, you will be able to:
- Create a simple HTML file
- Open it in a web browser
- Understand how web pages work
- Make your first changes to a web page

## What is a Web Page?

A **web page** is a document written in a special language called HTML (HyperText Markup Language). When you open a website in your browser, you're looking at web pages!

Every web page has:
- **Text** (words and paragraphs)
- **Headings** (titles and sections)
- **Links** (clickable to go to other pages)
- **Images** (pictures)
- **Styles** (colors, fonts)
- **Interactivity** (buttons that do things)

In this lesson, we'll create your very first one!

## Step 1: Create an HTML File

1. Open VSCode
2. Click **File** → **New Text File**
3. Click **Select a language** and choose **HTML**
4. Type the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Web Page</title>
</head>
<body>
    <h1>Welcome to My Website!</h1>
    <p>Hello! This is my first web page.</p>
    <p>I'm learning web development!</p>
</body>
</html>
```

## Step 2: Save Your File

1. Click **File** → **Save** (or press Ctrl+S)
2. Name it `myFirstPage.html`
3. Save it in your project folder
4. ✅ You now have an HTML file!

## Step 3: Open in a Browser

### Method 1: Using Live Server (EASIEST!)
1. Right-click on your file in VSCode
2. Click **"Open with Live Server"**
3. Your browser opens automatically and shows your page!

### Method 2: Manual Browser Opening
1. Open your file manager (Windows Explorer or Finder)
2. Find your `myFirstPage.html` file
3. Double-click it
4. It opens in your default web browser!

## Step 4: See Your Page in the Browser

You should see:
- A title that says **"Welcome to My Website!"** (big heading)
- Two lines of text below it

Congratulations! You've built your first web page! 🎉

## Understanding the Code

Each part of the HTML code has a purpose:

```html
<!DOCTYPE html>           <!-- Tells browser this is HTML5 -->
<html>                    <!-- Start of the page -->
<head>                    <!-- Hidden info about the page -->
    <title>...</title>    <!-- Shows in browser tab -->
</head>
<body>                    <!-- Everything visible on page -->
    <h1>...</h1>          <!-- Big heading -->
    <p>...</p>            <!-- Paragraph of text -->
</body>
</html>                   <!-- End of the page -->
```

## 🎯 Try It Yourself

Make changes to your HTML file:

1. Change the **title**: Replace `"My First Web Page"` with your name
2. Change the **h1**: Replace `"Welcome to My Website!"` with something cool like `"Welcome to [YOUR NAME]'s Website!"`
3. Change the **paragraphs**: Write something about yourself
4. **Save** the file (Ctrl+S)
5. **Refresh** your browser (press F5 or Ctrl+R)

Watch your changes appear instantly! That's the power of web development! ✨

## Vocabulary

| Term | Meaning |
|------|---------|
| **HTML** | Language for creating web pages |
| **Tag** | Instructions in angle brackets like `<p>` |
| **Element** | A tag and its content, like `<p>text</p>` |
| **Attribute** | Extra info about a tag |
| **Browser** | Program that shows web pages (Chrome, Firefox, Safari, Edge) |

## Example Reference
See [example_firstPage.html](examples/example_firstPage.html) for a working version of this lesson.

---

## Next Step
Now learn the building blocks! Go to [Lesson 3: Basic HTML](03_BasicHTML.md)

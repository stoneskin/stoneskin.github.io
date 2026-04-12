# 4. Project: Build Your About Me Web Page

## Learning Objectives
By the end of this project, you will:
- Apply HTML tags to create a real web page
- Organize information about yourself
- Practice using links, images, and lists
- Create your first web portfolio piece!

## Project Overview

You're going to build an **"About Me"** web page that tells visitors about yourself. This is a classic first project and looks great in your portfolio!

Your page will include:
- Your name (as a heading)
- A photo (if you want)
- Information about you
- Your interests/hobbies
- School/grade information
- Links to your favorite websites
- Contact information

## Step-by-Step Instructions

### Step 1: Create the HTML File

1. Open VSCode
2. Create a new file called `aboutMe.html`
3. Type the HTML structure:

```html
<!DOCTYPE html>
<html>
<head>
    <title>About Me</title>
</head>
<body>
    <!-- Your code goes here -->
</body>
</html>
```

### Step 2: Add Your Name and Photo

Inside the `<body>` section, add:

```html
<h1>About [Your Name]</h1>

<img src="yourphoto.jpg" alt="Photo of me">

<p>Hi! My name is <b>[Your Name]</b> and I'm in <b>grade [X]</b>.</p>
```

**Note:** Replace `yourphoto.jpg` with an actual photo file in your project folder.

### Step 3: Add "About Me" Section

```html
<h2>About Me</h2>
<p>
    I am a student who loves learning new things. 
    I'm interested in [TOPIC 1], [TOPIC 2], and [TOPIC 3].
    In my free time, I enjoy [ACTIVITY 1] and [ACTIVITY 2].
</p>
```

### Step 4: Add Your Interests Section

```html
<h2>My Interests</h2>
<ul>
    <li>Interest 1</li>
    <li>Interest 2</li>
    <li>Interest 3</li>
    <li>Interest 4</li>
    <li>Interest 5</li>
</ul>
```

### Step 5: Add a Skills Section

```html
<h2>My Skills</h2>
<ol>
    <li>Python Programming</li>
    <li>HTML and Web Design</li>
    <li>Problem Solving</li>
    <li>Teamwork</li>
</ol>
```

### Step 6: Add Your School Information

```html
<h2>School</h2>
<p>
    <b>School:</b> [Your School Name]<br>
    <b>Grade:</b> [Grade]<br>
    <b>Year Started:</b> [Year]
</p>
```

### Step 7: Add Favorite Links

```html
<h2>Links I Like</h2>
<ul>
    <li><a href="https://www.khanacademy.org/">Khan Academy</a> - Great for learning</li>
    <li><a href="https://code.org/">Code.org</a> - Programming tutorials</li>
    <li><a href="https://www.youtube.com/">YouTube</a> - Videos</li>
</ul>
```

### Step 8: Add Footer and Contact

```html
<hr>
<p><b>Contact Me:</b></p>
<p>Email: myemail@example.com</p>

<p><i>Last updated: April 2024</i></p>
```

## Complete Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>About Sarah</title>
</head>
<body>
    <h1>About Sarah</h1>
    
    <p>
        Hi! My name is <b>Sarah</b> and I'm in <b>grade 7</b>.
        I love learning about <i>technology</i> and <i>design</i>.
    </p>
    
    <h2>My Interests</h2>
    <ul>
        <li>Programming</li>
        <li>Gaming</li>
        <li>Drawing</li>
        <li>Reading</li>
        <li>Science</li>
    </ul>
    
    <h2>My Skills</h2>
    <ol>
        <li>Python programming</li>
        <li>HTML basics</li>
        <li>Problem solving</li>
        <li>Digital art</li>
    </ol>
    
    <h2>School</h2>
    <p>
        <b>School:</b> Lincoln Middle School<br>
        <b>Grade:</b> 7th<br>
        <b>Year Started:</b> 2023
    </p>
    
    <h2>Favorite Links</h2>
    <ul>
        <li><a href="https://www.khanacademy.org/">Khan Academy</a></li>
        <li><a href="https://code.org/">Code.org</a></li>
        <li><a href="https://www.python.org/">Python.org</a></li>
    </ul>
    
    <hr>
    <p><b>Contact Me</b></p>
    <p>Email: sarah@example.com</p>
    <p><i>Last updated: April 2024</i></p>
</body>
</html>
```

## 🎯 Your Assignment

1. Create your own `aboutMe.html` file
2. Include ALL the sections from the steps above
3. Fill in YOUR information (not placeholders!)
4. Save and open in your browser
5. Make sure everything looks correct
6. **Extra Credit:** 
   - Add more details and make it unique to YOU
   - Include a photo (if you have one)
   - Add more sections (quotes, achievements, etc.)

## Things to Check

Before you consider this done, make sure:

- ✅ Page title shows in browser tab
- ✅ Your name appears as the main heading
- ✅ All sections have headings
- ✅ Text is properly formatted with paragraphs
- ✅ Lists are properly formatted
- ✅ Links work when clicked
- ✅ No spelling mistakes
- ✅ Page looks clean and organized

## Example Reference
See [example_aboutMe.html](examples/example_aboutMe.html) for another version to compare with.

---

## Congratulations! 🎉

You've built your first real web page! This is a great portfolio piece. You can:
- Share it with family and friends
- Show it to teachers
- Add it to your GitHub account
- Use it as a practice piece for more complex designs

## Next Step
Ready to make your pages beautiful? Go to [Lesson 5: Basic CSS](05_BasicCSS.md)

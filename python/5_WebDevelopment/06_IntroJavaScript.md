# 6. Introduction to JavaScript - Make Your Pages Interactive

## Learning Objectives
By the end of this lesson, you will be able to:
- Add JavaScript to your HTML pages
- Create interactive buttons and events
- Use variables and simple functions
- Make your pages respond to user clicks

## What is JavaScript?

**JavaScript** is a programming language that runs in your web browser. It makes pages *interactive*.

- **HTML** = Structure (what's on the page)
- **CSS** = Style (how it looks)
- **JavaScript** = Behavior (what happens when you interact with it)

### Examples of JavaScript in Use:
- ✅ Button clicks that do something
- ✅ Pop-up messages
- ✅ Forms that check if you entered valid info
- ✅ Games (like Tic-Tac-Toe in a browser)
- ✅ Automatic slide shows
- ✅ Real-time calculations

## Adding JavaScript to HTML

Like CSS, there are 3 ways:

### Method 1: Inline (Inside HTML tags)

```html
<button onclick="alert('Hello!')">Click Me</button>
```

When you click the button, a pop-up appears with "Hello!"

### Method 2: Internal (In the `<script>` tag)

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>Interactive Page</h1>
    <button id="myButton">Click Me</button>
    
    <script>
        document.getElementById("myButton").onclick = function() {
            alert("You clicked the button!");
        };
    </script>
</body>
</html>
```

### Method 3: External (Separate .js file) ⭐ BEST for big projects

**Create:** `script.js`
```javascript
document.getElementById("myButton").onclick = function() {
    alert("You clicked the button!");
};
```

**In HTML:** `index.html`
```html
<script src="script.js"></script>
```

## Basic JavaScript Concepts

### Variables (Containers for Data)

```javascript
let name = "Sarah";
let age = 13;
let isStudent = true;

console.log(name);     // Shows in browser console
console.log(age);      // Shows: 13
```

### Functions (Reusable Code)

```javascript
function sayHello() {
    alert("Hello, friend!");
}

function greet(name) {
    alert("Hi, " + name + "!");
}

sayHello();        // Call it
greet("Sarah");    // Call with parameter
```

### Events (User Actions)

Common events:
- `click` - When user clicks
- `mouseover` - When mouse hovers over
- `change` - When input changes
- `submit` - When form is submitted

```html
<button onclick="doSomething()">Click Me</button>
<button onmouseover="sayHi()">Hover Over Me</button>
```

## Complete Interactive Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Page</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            padding: 20px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin: 10px;
            cursor: pointer;
        }
        #message {
            font-size: 24px;
            color: blue;
            margin: 20px;
        }
    </style>
</head>
<body>
    <h1>JavaScript Demo</h1>
    
    <button onclick="showMessage()">Click Button 1</button>
    <button onclick="showMessage2()">Click Button 2</button>
    <button onclick="clearMessage()">Clear</button>
    
    <div id="message"></div>
    
    <h2>Counter</h2>
    <p>Count: <span id="count">0</span></p>
    <button onclick="increment()">Count Up</button>
    <button onclick="decrement()">Count Down</button>
    <button onclick="resetCount()">Reset</button>
    
    <script>
        let count = 0;
        
        function showMessage() {
            document.getElementById("message").innerHTML = 
                "You clicked Button 1!";
        }
        
        function showMessage2() {
            document.getElementById("message").innerHTML = 
                "You clicked Button 2!";
        }
        
        function clearMessage() {
            document.getElementById("message").innerHTML = "";
        }
        
        function increment() {
            count = count + 1;
            document.getElementById("count").innerHTML = count;
        }
        
        function decrement() {
            count = count - 1;
            document.getElementById("count").innerHTML = count;
        }
        
        function resetCount() {
            count = 0;
            document.getElementById("count").innerHTML = count;
        }
    </script>
</body>
</html>
```

## Key JavaScript Concepts Explained

### DOM (Document Object Model)

The DOM is how JavaScript accesses HTML elements:

```javascript
// Get element by ID
let button = document.getElementById("myButton");

// Get element by class
let items = document.getElementsByClassName("item");

// Change HTML content
document.getElementById("message").innerHTML = "New text!";

// Change style
document.getElementById("box").style.color = "red";
document.getElementById("box").style.fontSize = "20px";
```

### Operators

```javascript
let a = 5;
let b = 3;

a + b;      // 8 (addition)
a - b;      // 2 (subtraction)
a * b;      // 15 (multiplication)
a / b;      // 1.67 (division)
a % b;      // 2 (remainder)

a = a + 1;  // Increase
a = a - 1;  // Decrease
```

### Conditions (If/Else)

```javascript
function checkAge(age) {
    if (age >= 13) {
        alert("You can join!");
    } else {
        alert("Too young, come back later!");
    }
}
```

### String Concatenation (Combining Text)

```javascript
let name = "Sarah";
let greeting = "Hello, " + name + "!";
alert(greeting);  // Shows: "Hello, Sarah!"

// Or using template literals (easier)
let greeting2 = `Hello, ${name}!`;
```

## 🎯 Try It Yourself

Create an interactive page:

1. Create a new file: `interactive.html`
2. Add HTML:
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Interactive Page</title>
    <style>
        body { font-family: Arial; padding: 20px; }
        button { padding: 10px 20px; margin: 10px; }
        #message { font-size: 20px; margin: 20px; }
    </style>
</head>
<body>
    <h1>Welcome!</h1>
    
    <button onclick="sayHello()">Say Hello</button>
    <button onclick="askName()">Ask for Name</button>
    <button onclick="changeColor()">Change Color</button>
    
    <div id="message"></div>
    
    <script>
        function sayHello() {
            document.getElementById("message").innerHTML = 
                "Hello! 👋";
        }
        
        function askName() {
            let name = prompt("What's your name?");
            document.getElementById("message").innerHTML = 
                "Nice to meet you, " + name + "!";
        }
        
        function changeColor() {
            document.body.style.backgroundColor = "lightblue";
        }
    </script>
</body>
</html>
```

3. Save and open in browser
4. Click the buttons and watch it respond!

## Common JavaScript Functions

```javascript
alert("This is a popup message");           // Pop-up alert
console.log("Debug message");                // Shows in browser console
prompt("Enter your name:");                  // Ask user for input
document.getElementById("id").innerHTML;     // Get/set HTML content
document.getElementById("id").style.color;   // Change CSS styles
```

## Debugging Tips

When something doesn't work:
1. Open browser **Developer Tools** (F12 or right-click → Inspect)
2. Go to **Console** tab
3. Look for red error messages
4. Use `console.log()` to print values

```javascript
let x = 5;
console.log("x =", x);  // Helps debug
```

## Example Reference
See [example_interactiveButtons.html](examples/example_interactiveButtons.html) for a working interactive example.

---

## Next Step
Apply everything to a real project! Go to [Lesson 7: Project - Build an Interactive Web Page](07_Project_WebPage.md)

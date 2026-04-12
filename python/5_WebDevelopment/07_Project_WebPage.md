# 7. Final Project: Build an Interactive Web Page

## Learning Objectives
By the end of this project, you will:
- Combine HTML, CSS, and JavaScript into ONE page
- Build a real, working web application
- Apply all your web development skills
- Create a portfolio-worthy project!

## Project Overview

Choose ONE of these projects and build it:

### Option 1: Interactive Quiz
A quiz page where:
- Users answer 5 multiple-choice questions
- JavaScript checks their answers
- Shows their score at the end
- Has nice styling and layout

### Option 2: To-Do List Application
A task manager where:
- Users can add new tasks
- Check off completed tasks
- Delete tasks
- Lists are interactive and styled beautifully

### Option 3: Interactive Portfolio
An enhanced version of your About Me page with:
- Section toggle buttons (click to show/hide)
- A contact form with validation
- Professional styling
- Smooth interactions

### Option 4: Simple Game
A browser game like:
- Number guessing game
- Rock-Paper-Scissors
- Memory card matching
- Simple dice roller with scoring

## Recommended: Build a Quiz

Here's a complete example you can follow:

### Step 1: Create the HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>Awesome Quiz</title>
    <link rel="stylesheet" href="quiz.css">
</head>
<body>
    <div class="container">
        <h1>🎓 My Awesome Quiz</h1>
        
        <div id="quizContainer">
            <div id="question"></div>
            
            <div id="options"></div>
            
            <button onclick="nextQuestion()">Next Question</button>
        </div>
        
        <div id="results" style="display: none;">
            <h2>Quiz Complete! 🎉</h2>
            <p>Your Score: <span id="score"></span> / 5</p>
            <button onclick="restartQuiz()">Take Quiz Again</button>
        </div>
    </div>
    
    <script src="quiz.js"></script>
</body>
</html>
```

### Step 2: Create the CSS File (quiz.css)

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.container {
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    padding: 40px;
    max-width: 500px;
    width: 100%;
}

h1 {
    text-align: center;
    color: #333;
    margin-bottom: 30px;
    font-size: 32px;
}

#question {
    font-size: 18px;
    color: #333;
    margin-bottom: 20px;
    font-weight: bold;
}

label {
    display: block;
    margin: 12px 0;
    padding: 12px;
    border: 2px solid #ddd;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s;
}

label:hover {
    background-color: #f0f0f0;
    border-color: #667eea;
}

input[type="radio"] {
    margin-right: 10px;
    cursor: pointer;
}

button {
    width: 100%;
    padding: 12px;
    margin-top: 20px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s;
}

button:hover {
    background: #764ba2;
}

#results {
    text-align: center;
}

#results h2 {
    color: #667eea;
    margin-bottom: 20px;
}

#results p {
    font-size: 24px;
    margin: 20px 0;
    color: #333;
}
```

### Step 3: Create the JavaScript File (quiz.js)

```javascript
// Quiz Questions and Answers
const questions = [
    {
        question: "What is the capital of France?",
        options: ["London", "Paris", "Berlin", "Madrid"],
        correct: 1  // Index of correct answer (0-3)
    },
    {
        question: "What color is the ocean?",
        options: ["Red", "Yellow", "Blue", "Green"],
        correct: 2
    },
    {
        question: "How many sides does a triangle have?",
        options: ["2", "3", "4", "5"],
        correct: 1
    },
    {
        question: "What is 5 + 3?",
        options: ["6", "7", "8", "9"],
        correct: 2
    },
    {
        question: "What programming language did we learn first?",
        options: ["JavaScript", "HTML", "CSS", "Python"],
        correct: 1
    }
];

let currentQuestion = 0;
let score = 0;
let selectedAnswer = null;

// Display a question
function displayQuestion() {
    const question = questions[currentQuestion];
    
    // Display question text
    document.getElementById("question").innerHTML = 
        `Question ${currentQuestion + 1} of ${questions.length}: ${question.question}`;
    
    // Display options
    let optionsHTML = "";
    for (let i = 0; i < question.options.length; i++) {
        optionsHTML += `
            <label>
                <input type="radio" name="answer" value="${i}">
                ${question.options[i]}
            </label>
        `;
    }
    document.getElementById("options").innerHTML = optionsHTML;
    
    selectedAnswer = null;
}

// Check answer and move to next
function nextQuestion() {
    // Get selected answer
    const radios = document.querySelectorAll('input[name="answer"]');
    for (let radio of radios) {
        if (radio.checked) {
            selectedAnswer = parseInt(radio.value);
            break;
        }
    }
    
    // Check if user selected an answer
    if (selectedAnswer === null) {
        alert("Please select an answer!");
        return;
    }
    
    // Check if correct
    if (selectedAnswer === questions[currentQuestion].correct) {
        score++;
    }
    
    // Move to next question or show results
    currentQuestion++;
    if (currentQuestion < questions.length) {
        displayQuestion();
    } else {
        showResults();
    }
}

// Show final results
function showResults() {
    document.getElementById("quizContainer").style.display = "none";
    document.getElementById("results").style.display = "block";
    document.getElementById("score").innerHTML = score;
}

// Restart quiz
function restartQuiz() {
    currentQuestion = 0;
    score = 0;
    selectedAnswer = null;
    document.getElementById("quizContainer").style.display = "block";
    document.getElementById("results").style.display = "none";
    displayQuestion();
}

// Start the quiz when page loads
displayQuestion();
```

### Step 4: Files to Create

Create 3 files in your project folder:
1. `quiz.html` - HTML file
2. `quiz.css` - CSS styling
3. `quiz.js` - JavaScript code

Then link them together in the HTML file.

## 🎯 Your Assignment

**Choose and complete ONE project:**

### If Building a Quiz:
1. Create the 3 files shown above
2. Customize it with YOUR questions:
   - Change the questions to something you like
   - Change the styling colors
   - Add more questions (5+ total)
3. Test it thoroughly
4. Make sure it looks professional

### If Building a To-Do List:
1. Create HTML with an input field and a list
2. Create CSS to make it look nice
3. Create JavaScript to:
   - Add tasks when user types and clicks Add
   - Delete tasks when user clicks X
   - Check off completed tasks
4. Style it beautifully with colors and spacing

### If Building an Interactive Portfolio:
1. Start with your About Me page
2. Add CSS for professional styling
3. Add JavaScript for:
   - Toggle buttons to show/hide sections
   - Form validation for contact info
   - Smooth scrolling effects
4. Make it look portfolio-ready

### If Building a Simple Game:
1. Create engaging gameplay
2. Add scoring system
3. Style it with colors and animations
4. Make it fun to play!

## Checklist Before Submitting

✅ **Functionality**
- [ ] All buttons work
- [ ] No JavaScript errors (check console with F12)
- [ ] All features work as intended
- [ ] Responsive (looks good on different screen sizes)

✅ **Design**
- [ ] Professional colors and fonts
- [ ] Good spacing and layout
- [ ] Clear and easy to use
- [ ] No spelling or grammar mistakes

✅ **Code Quality**
- [ ] Well-organized code
- [ ] Comments explaining hard parts
- [ ] Files properly linked (HTML → CSS, HTML → JS)
- [ ] No unnecessary code

✅ **Files**
- [ ] All 3 files created (HTML, CSS, JS)
- [ ] All links are correct
- [ ] Files saved in proper location

## Bonus Challenges (If You Finish Early)

- Add more questions/features to your project
- Implement a timer or difficulty levels
- Add animations using CSS
- Use Local Storage to save user progress
- Add more interactive elements
- Create multiple pages that link together

## Examples Reference
See the `examples/` folder for:
- `example_interactiveButtons.html` - Simple interactivity demo
- `example_styled_page.html` - CSS styling example

---

## Congratulations! 🎉

You've completed **Web Development Section 3!** You now know:

✅ HTML - Structure and content
✅ CSS - Styling and colors  
✅ JavaScript - Interactivity and functions

**You can now:**
- Build real websites
- Add styling and interactivity
- Show your projects to others
- Impress your friends and family
- Continue learning advanced web development

## What's Next?

Now that you know web basics, you can:
1. Learn advanced CSS (layouts, responsive design)
2. Learn more JavaScript (objects, arrays, APIs)
3. Learn frameworks like React or Vue
4. Build real projects and share them online
5. Get a job as a web developer!

Keep coding! 💻✨

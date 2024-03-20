# 0x01. AirBnB clone - Web static
- HTML, CSS, Front-end

## What is HTML?
- `HTML` stands for `HyperText Markup Language`. It is the standard markup language for creating web pages and web applications. HTML describes the structure of a web page semantically and is composed of a set of elements or tags that define the different parts of a document, such as headings, paragraphs, links, images, and more.

## How to create an HTML page?
- To create an HTML page, you need a basic text editor such as Notepad on Windows or TextEdit on macOS. Here's a simple example of an HTML page:

```
<!DOCTYPE html>
<html>
<head>
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is a paragraph.</p>
</body>
</html>
```

## What is a markup language?
- A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. It is used to define elements and their attributes within a document to provide structure and formatting.

## What is the DOM?
- The `Document Object Model` (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. The `DOM` represents the document as a tree of objects where each node represents a part of the document.

## What is an element/tag?
- An element or tag in `HTML` is a fundamental building block used to define different parts of a web page. Each element starts with an opening tag, contains content, and ends with a closing tag. For example, `<p>` is the opening tag for a paragraph element, and `</p>` is the closing tag.

## What is an attribute?
An attribute provides additional information about an `HTML` element and is placed within the opening tag of the element. Attributes typically consist of a name and a value and are used to modify the element's behavior or provide metadata. For example, the `href` attribute in an `<a>` tag specifies the URL of the link.

## How does the browser load a webpage?
- When a browser loads a webpage, it follows a series of steps:

- It resolves the domain name to an IP address using DNS.
- It sends a request to the server for the webpage.
- The server responds with the HTML content of the webpage.
- The browser parses the HTML, constructs the DOM tree, and renders the page.
- Additional resources like CSS stylesheets, JavaScript files, and images referenced in the HTML are also fetched and processed.

## What is CSS?
- `CSS` stands for `Cascading Style Sheets`. It is a style sheet language used to describe the presentation of a document written in `HTML`. `CSS` describes how elements should be rendered on screen, on paper, in speech, or on other media.

## How to add style to an element?
- You can add style to an `HTML` element using `CSS`. You can do this by specifying `CSS` rules either in an external stylesheet file or directly within the `HTML` document using the `<style>` tag or the style attribute of individual elements.

## What is a class?
- A class is a way to apply a specific set of styles to one or more `HTML` elements. Classes are defined in `CSS` and can be applied to elements using the class attribute. Multiple classes can be applied to a single element, allowing for the combination of different styles.

## What is a selector?
In `CSS`, a selector is a pattern used to select the elements that you want to style. Selectors can target elements based on their tag `name`, `class`, `ID`, `attributes`, or even their relationship with other elements in the document.

## How to compute CSS Specificity Value?
- `CSS` specificity is a set of rules that determine which `CSS` styles are applied to an element when there are conflicting styles. Specificity is calculated based on the combination of selectors used to target an element. The higher the specificity value, the more precedence the style has. Specificity is often represented by a four-part value (e.g., 0,0,0,0).

## What are Box properties in CSS?
- Box properties in `CSS` refer to properties that define the dimensions and spacing of an element's box model. These properties include `width`, `height`, `margin`, `padding`, `border`, and `box-sizing`. They are used to control how elements are sized, positioned, and spaced within a document.

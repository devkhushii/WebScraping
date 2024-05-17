import requests
from bs4 import BeautifulSoup

# Open the HTML file and read its content
with open("Sample.html","r") as f:
    html_doc=f.read()

# Parse the HTML content using BeautifulSoup
soup=BeautifulSoup(html_doc,"html.parser")
print(soup.prettify())  # Print the prettified version of the parsed HTML
print(soup.title.string, type(soup.title.string))        # Print the content of the <title> tag and its data type
print(soup.div)                # Print the content of the first <div> tag found in the HTML

print(soup.find_all("div"))     # Find and print all <div> tags in the HTML document

# Find all <a> tags, print their href attribute values, and text content
for link in soup.find_all("a"):    
    print(link.get("href"))
    print(link.get_text())

s=soup.find(id="link3")  # Find an element with id "link3" 
print(s.get("href"))      # and print its href attribute value

print(soup.select("div.italic"))     # Select and print all <div> tags with class "italic"
print(soup.select("span#italic"))     # Select and print all <span> tags with id "italic"
print(soup.span.get("class"))         # Print the value of the class attribute of the first <span> tag found

print(soup.find(class_="italic"))       # Find the first element with class "italic" and print it

# Print all children of the element with class "container"
for child in soup.find(class_="container").children:
    print(child)

# Print all parents of the element with class "box"
for parent in soup.find(class_="box").parents:
    print(parent)

# Modify the tag name, class attribute, and content of the element with class "container" and print it
cont=soup.find(class_="container")
cont.name="span"
cont["class"]="myclass"
cont.string="I am a string"
print(cont)


# Create a new <ul> tag, append <li> tags with text "Home" and "About" to it, and insert it at the beginning of <body>
ulTag=soup.new_tag("ul")
liTag=soup.new_tag("li")
liTag.string="Home"
ulTag.append(liTag)

liTag=soup.new_tag("li")
liTag.string="About"
ulTag.append(liTag)

soup.html.body.insert(0,ulTag)

# Write the modified HTML content to a file named "modified.html"
with open("modified.html","w") as f:
    f.write(str(soup))

# Check if the element with class "container" has an "id" attribute and print the result
cot=soup.find(class_="container")
print(cot.has_attr("id"))

# Define a function to find elements with a class attribute but without an id attribute
def has_class_but_not_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

# Find and print all elements matching the defined criteria
results=soup.find_all(has_class_but_not_id)
for result in results:
    print(result, "\n\n")


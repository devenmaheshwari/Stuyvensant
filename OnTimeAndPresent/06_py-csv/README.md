# K07 -- Show What You Know
## Umlauts - Deven Maheshwari, Alejandro Alonso, Yusuf Elsharawy Pd. 1
### A demonstration of profiency in foundational tools and concepts, though an explanation of K06.

File I/O --> We read in the CSV file using a basic Python module with the same name (csv). From this module we imported the DictReader class into our program
which allowed us to quickly convert the file's raw data into something usable. We then shifted the data line by line from the DictReader object into a standard Python dictionary.

Dictionary --> Dictionaries allowed us to easily store and access two-column, unordered data (an essential part of the exercise). We set up the dictionary by assigning key-value pairs as follows (example_dict["example key"] = value), and accessing them by key (example_dict["key"]), and using the .items() function in the dictionary class, converting into an iterable.

- Lists are useful to store many values in a particular order. You can easily access any element from the list, making it easy to pick a random one. And since lists can be modified and can change in size, it's often useful if you need to continually store more elements over time.

- GitHub-flavoured Markdown is an expanded version of regular Markdown. You can prepend a line with `# ` for a header, `## ` for a subheader, and so on. You can surround text with asterisks/underscores for _italics_, and doube asterisks/underscores for __bold__. Similarly, you can also surround text with backticks (`\`text\``) for a monospace font, and for a multiline code block you can use triple backticks, with a specified language for syntax highlighting:
````python
```python
def main():
	print("Hello World!")

if __name__ == '__main__':
	main()
```
````
You can learn more about GitHub-flavoured Markdown [here](https://guides.github.com/features/mastering-markdown/), or just search for yourself.

- For a weighted randomized selection, you can choose a random value between 0 and the total weight of all entries (using the random library in Python). Then you can go through each of the elements and decrement the random value by the element's weight. The first element to bring the value down to (or below) 0 is your randomly-chosen element.
	- For a higher speed, you can also use a binary search. If you create a list beforehand containing the cumulative weights (the sum of all weights up to and including that one), then choosing a random element can be done similarly to the above approach, except using a binary search instead. The correct element is the first one with a cumulative weight greater than or equal to your random value. Try implementing it yourself!
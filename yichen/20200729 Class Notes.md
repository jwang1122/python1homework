# 20200707ClassNotes.md

```
GUI server

To get to book app uncomment or add this line in app4.py:  from flask_cors import CORS
and this line: CORS(app)

Run the code
If it doesn't work, do: pip install flask_cors
Press enter
Run the code again
when you finish that, go to file and open a new window
In the new window, open the folder Reactjs
In the terminal type: cd book-app
Press enter
Then type: npm start
and press enter

In the GUI server you should see all of the books you have in MongoDB
If you go to MongoDB and change the data of one of your books then if you go back to the GUI server and refresh the page, the change you made in MongoDb will also be on the GUI server

For example, you first want to open your GUI server
Then you want to go to MongoDB and edit one of your books

Here is one of my books:

_id: "5d95c276e15847aabca442564f396085"
title: "Green Eggs and Ham"
author: "Dr. Seuss"
read: true
price: 4.99
rating: 1

If I change the rating from 1 to 5 like this:

_id: "5d95c276e15847aabca442564f396085"
title: "Green Eggs and Ham"
author: "Dr. Seuss"
read: true
price: 4.99
rating: 5

Then go back to my GUI server and refresh the page, this will appear:

_id: "5d95c276e15847aabca442564f396085"
title: "Green Eggs and Ham"
author: "Dr. Seuss"
read: true
price: 4.99
rating: 5

Instead of this:

_id: "5d95c276e15847aabca442564f396085"
title: "Green Eggs and Ham"
author: "Dr. Seuss"
read: true
price: 4.99
rating: 1


So the book with the rating 5 will appear
And the book with the rating 1 will not appear

On the GUI server, there is a button that says add new book
If you click that button you can enter a book title, a book author, and a book price

If you add a new book the book doesn't have to be real

For example, I added this book:

_id: "785c60fbd07f43a6ba151411dc1fb2f1"
title: "random"
author: "random "
read: false
price: "2000000"

This is not a real book

Whatever book you add in the GUI server it is also going to be in MongoDB

This added book: 

_id: "785c60fbd07f43a6ba151411dc1fb2f1"
title: "random"
author: "random "
read: false
price: "2000000"

Is on my GUI server and MongoDB




```
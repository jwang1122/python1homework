# 20200707ClassNotes.md
* First python code
```py
print ("Hello world")
CRUD
C: create
R: retrieve
U: update
D: delete
```
```
Install MonngoDB
click fill in connection fields indivisually
if you don't have pymongo, type pip install pymongo in terminal
if that doesn't work type: .\env\scripts\pip install pymongo in terminal

Use MongoDB
after you install MongoDB, click fill in connection fields indivisually
then click mydb then books


CRUD meaning
Create: POST
Retrieve: GET
Update: PUT
Delete: DELETE

Use CRUD
click edit and copy id
replace the id in delete file with the one you copied
run the file
the file will be deleted

```
```
Service request and service response
if you don't have flask type: pip install flask in terminal
run the code app1.py
press Ctrl and click on the link in the terminal
If it says NOT FOUND, then in the browser put forward slash and ping
Like this: /ping
Then it will print pong!
The ping you input in the browser is a service request
the pong output is a service response 
you can also change the size, color, and font of the service response

In app2.py the size, color, and font of pong is different

The size is bigger, the color is red and the font is bubble letters

in app3.py there are more service responses and requests
if you input forward slash and books
Like this: / books
then the service response will be the books you put in the code

in app4.py if you type in forward slash books
Like this: /books
then it will show all the books you have in MongoDB
In MongoDB if you change the data in one of your books by editing it, it will also change the data in the service response

To change the data in the service response you have to first run your code(app4.py)
in MongoDB one of my books is Green Eggs and Ham
if you click the edit button (which is next to the data and has a pen icon) you can change any of the data 
For example: i can changge the rating from 1 to 5 and if you refresh the page from this link (http://localhost:5000/ ) then the rating on the page will change from 1 to 5


_id:"5d95c276e15847aabca442564f396085"
title:"Green Eggs and Ham"
author: "Dr. Seuss"
read: true
price: 4.99
rating: 1


```
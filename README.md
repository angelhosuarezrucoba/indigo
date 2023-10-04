# Indigo Challenge


in order to run the code you need to have python installed 
you can run the code just executing this command

` python main.py `

if you want to run the test you should install the dependencies for testing
running this command 

` pip install -r requirements.txt ` 

then you can run the tests executing this command.

` pytest tests.py ` 

all these commands should be executed from the root folder

### Considerations

* There is no input validations, I'm short of time unfortunately
* I have declared all the types, so its very intuitive and simple
* All the requirements were accomplished. methods as add, less, greater and between have time complexity O(1), since im accesing to an specific value in the 
  array and it has O(1) constant time.
* Methods like build stats have time complexity O(n) since im iterating over all the array

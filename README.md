# **0x00. AirBnB clone - The console**
>In this repository, Sebastian Carvajal and I implemented the AirBnB clone - version1.

## Project's description: 
>This is the first step towards building a full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

>Steps:
* Create a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of the future instances.
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all the classes and storage engine.
* Create the command interpreter.

## Command Interpreter:
> The console allow us to create the data model, manage objects and store and persist objects to a file (JSON file). Some examples:
* Create a new object (ex: a new User or a new Place).
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…).
* Update attributes of an object.
* Destroy an object.

>The first piece is to manipulate the storage system. This storage engine will give us an abstraction between “Our objects” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later, we won’t have to pay attention (take care) of how our objects are stored. This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

>The console will be a tool to validate this storage engine.


### How to start it:
### How to use it:
### Examples:

## How can you report an error or solve a question?
> You can contact to authors sending a message through github accounts or an email to Jhojan Perlaza <4739@holbertonschool.com> or to Sebastian Carvajal <4574@holbertonschool.com>
# Very Basic Questions to Refresh Memory

### 1. What is a REST API?
- A REST API (representational state transfer) is a an application programming interface that conform to the REST style. REST is usually stateless. It will use HTTP methods like GET, POST, PUT, and DELETE. These APIs have a uniform interface allowing different software to connect.

### 2. What is the difference between a FE and BE in a web application?
- FE handles the client actions and sends requests to the server.
- BE handles those requests and returns the data that the client is looking for.

### 3. How would you design a simple todo list application?
- Based on the functional requirements, users should have CRUD functionality. Users should be able to check them off.
- FE - I would create a UI with react. BE - I would use NoSQL to store those todo list items.
- I would use REST API to connect between the FE and BE. Users would need to have some sort of
- Authentication to make sure we know who it is.

### 4. Walk me through the basics of how a web page loads and renders.
- First the user types in URL
- DNS Lookup resolves domain to IP address
- browser makes an HTTP request to the server.
- The BE server sends back a response containing the webpage data (HTML, CSS, and JS)
- The browser parses this Data and creates the DOM
- Renders the CSS
- Executes the JS
- Page can be interactive now.

### 5. What are key differences in Angular and React?
- During my migration, it was much less intuitive to work with Angular because I had to learn binding. Most of the legacy code was not modular so files were often hundreds of lines long.

### 6. Explain what an Object Relational Mapping (ORM) is?
- An ORM is a way to align programming code with database structures. For example in the Django ORM, there was a way to serialize the data coming from the MySQL database into a python object. This can be extended to any programming language or database, to where it can modify the data so that it can be used in a standard way.
- Allows developers to work with database records as if they were objects in their language.

### 7. Can you give me an example of a three tier web application?
- Presentation Tier : User Interface, Web browser or mobile app
- Application Tier : Business Logic, Processes user requests, Communication w DB
-  Data Tier : Stores and Manages Data

### 8. What does MVVM architecture mean to you?
![image](/system-design/interview-questions/assets/mvvm-pattern.png)
- View : Responsible for defining the structure, layout, and appearance of what the user sees on screen
- ViewModel : Notifies the view of any changes in state. Handles the UI changes to make appropriate changes to state.
- Model : Manages the data and business logic.

### 9. What strategies do you have for improving website performance or load times?
- Using hooks like useMemo or useRef to prevent re-renders when it is not necessary
- Limiting API calls to those that only matter
- Caching
- Using Content Distribution Networks (CDN) to transfer static assets for content.

### 10. How would you optimize a slow DB query?
- Add appropriate indexes
    - Helps Db jump to the correct place.
- Avoid N + 1 query problems
    - Happens when code makes too many queries.
    - Lets say you have 1 query to fetch N users. But for each user you run another query to get posts.
- Pagination
    - For large datasets you can just return a few of these items back.

### 11. What does code splitting mean?
- This is a web development technique where large JS is split into smaller more manageable chunks to only load when you need it.

### 12. CORS, what is it?
- This is a security rule in web browsers that controls which websites can talk to one another.

### 13. Difference between Django and Express [source](https://www.monocubed.com/blog/django-vs-express/#:~:text=Django%20is%20an%20advanced%20Python,complicating%20the%20characteristics%20of%20Node.)
- Django
    - Open source web framework that uses MVT
    - More complexity and comes with more things out of the box.
    - Less flexible
- Express

#### 14. Difference between TCP and UDP
Both are protocols that transfer information between applications.
- TCP - a more secure connection requiring a three way handshake. Reliable and packets are sent in order. Good for HTTPS requests and file transfers.
- UDP - Does not require a handshake and will just send data over. Not guarantee it will arrive in order. Good for time sensitive apps. Things like video streaming, gaming, voice.
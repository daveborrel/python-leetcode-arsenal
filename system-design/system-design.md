# System Design

## Functional vs Non Functional Requirements

### Functional

A checklist for a system and what it must be able to do. These requirements determine if the software is functioning properly or not.

### Non-Functional Requirements

Quality Attributes of the Software

## Estimation of Scale

Try to get a rough estimate of how much traffic, how many users, what kind of data will be used for a question like this.

## API

Discuss the different APIs that you might need to use
- Public API - businesses use this to make money.
- Internal API - the employees in the company need these endpoints to do their jobs.

## Data Design

Its important to understand how to craft different classes and how they are related to one another.

## Database

### SQL (Relational Databases)
- They have good data integrity and are [ACID](https://mariadb.com/resources/blog/acid-compliance-what-it-means-and-why-you-should-care/) Compliant.
- Security
- Vertical Scaling
- Table Based

ACID
- Atomicity - prevents half done operations, meaning entire transaction must be sucessful.
- Consistency - data must be valid or else it will roll back
- Isolation - ensures that each transaction happens once in its own time.
- Durability - must be able to persist

#### MySQL
- Open Source Relational Database Management System. 
- 

### NoSQL (Non Relational Databases)
- Have dynamic schema and can accomodate changing data needs
- Horizontal Scaling
- Document, Key Value, Graph, or Solumn Stores.

#### MongoDB
A document database that has a flexible schema approach. Stores data in BSON (Very similar to JSON) which allows for type.
- Has high availability, horizontal scaling.
- Cluster can have replicas

### Sharding
Splitting the values horizontally based on the range of values defined by the partition key.
For example, if you have key range from [0,100]
- You shards could look like A = [0,20] B = [20,40] and C = [40,60].

### NoSQL vs MySQL
MySQL has better join capabilities. 

- Join - can be thought of as connecting different spreadsheets on common information. If we have a spreadsheet of customers, orders, and products, we can combine them into a single super spreadsheet.   

NoSQL is better for high traffic websites and not needing complex reporting.

## Architecture

### Difference between Monolith and Microservices Architecture

Monolith - this is a self contained and independent application. It is a single unit and is responsible fro everything to satisfy a business need.
- Advantages
    - Simple to develop
    - easy monitoring
- Disadvantages
    - Maintenance becomes hard as the codebase grows
    - Entire application gets deployed
    - Harder to scale

Microserves - a collection of small, autonomous 
- Advantages
    - Loose coupling
    - Improves Fault Tolerance
- Disadvantages
    - Complex
    - Testing is more difficult
    - Better scaling because each service can be scaled independently

### Examples of High Level Architecture Diagrams

#### tinyURL

![image](/system-design/assets/tinyURL.png)

![image](/system-design/assets/bitly.JPG)

#### Notification System

![image](/system-design/assets/notificationm.png)

## Caching

To save the DB from overuse, we can use in-memory data stores.

Remember that There are different kinds of caching strategies.
- LRU (least recently used)
- LFU (least frequently used)

Redis - wider range of tasks.
memCached - simple and basic key value caching.

### Resources
[Functional vs Non-Functional Requirements: Understanding Core Principles](https://www.ironhack.com/gb/blog/functional-vs-non-functional-requirements-understanding-the-core-differences-and)
[Monolith vs Microservices](https://www.karanpratapsingh.com/courses/system-design/monoliths-microservices#microservices)
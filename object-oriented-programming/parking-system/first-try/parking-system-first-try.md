# Parking Lot

1. Generate Use Cases
2. Constaints Analysis
3. Basic Design
4. Identify Bottlenecks
5. Scalability

## Use Cases
- There can be multiple levels to the parking lot
- There can be different types
    - Small vehicles
    - Disability spots
- Entry and exit points

## Constraints

- The maximum number of cars in the parking lot
- The entry and exit limit the number of cars coming in and out of the lot

## Basic Design

- There should be 2 classes to start

- Parking Lot
- Fields
    - Number of spots
    - Level
- Methods
    - Get Spots
    - Park Vehicle

- Parking Spot
- Fields
    - Type
    - Vehicle in Spot

- Vehicle
    - Type

- I think this initial approach might be flawed because we don't know the types of parking lot spots that a parking lot might have.
- Maybe we need to create a parking spot class?

## Identify Bottlenecks

## Scalability

- How do we scale this?
    - More vehicles at one time?
- Maybe we need to see how much they have been parked for?
- Payments?

### Resources
[Solution](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/parking-lot.md)
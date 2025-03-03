# This is a creational design apttern that lets you ensure that a class only has one instance of it.

# What issue does this solve?
# (1) - Ensure that a class only has a single instance - good if there is some sort of control access for a single resource.
# (2) - Providing a global access point to that instance

# Solution
# (1) - Make the default constructor private
# (2) - Create a static creation method that acts as a constructor. This will call the private constructor and create an object in a field.
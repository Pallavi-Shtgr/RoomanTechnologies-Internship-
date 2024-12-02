-- Create a collection called Customers in a NoSQL database. Insert three customer documents into the Customers collection with the following details: Rahul Sharma, 35, Purchases: ["Laptop", "Phone"] Vikram Seth, 28, Purchases: ["Tablet", "Headphones"] Anjali Gowda, 40, Purchases: ["Camera", "Tripod"] 

 // Create the "Customers" collection (this is just a plain JavaScript object to mimic the collection)
const Customers = [];

// Insert three customer documents into the Customers collection
Customers.push(
  {
    name: "Rahul Sharma",
    age: 35,
    purchases: ["Laptop", "Phone"]
  },
  {
    name: "Vikram Seth",
    age: 28,
    purchases: ["Tablet", "Headphones"]
  },
  {
    name: "Anjali Gowda",
    age: 40,
    purchases: ["Camera", "Tripod"]
  }
);

// Output the Customers collection
console.log("Customers Collection:");
console.log(Customers);
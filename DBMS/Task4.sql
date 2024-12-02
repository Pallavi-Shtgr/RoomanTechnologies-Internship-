-- Query the collection to find all thr customers who is having laptop

// Create the "Customers" collection (this is a plain JavaScript array to mimic the collection)
const Customers = [
  { name: "Rahul Sharma", age: 35, purchases: ["Laptop", "Phone"] },
  { name: "Vikram Seth", age: 28, purchases: ["Tablet", "Headphones"] },
  { name: "Anjali Gowda", age: 40, purchases: ["Camera", "Tripod"] }
];

// Use filter() to find all customers whose purchases array includes 'Laptop'
const customersWhoPurchasedLaptop = Customers.filter(customer => 
  customer.purchases.includes("Laptop")
);

// Log the filtered customers
if (customersWhoPurchasedLaptop.length > 0) {
  console.log("Customers who purchased a Laptop:");
  console.log(customersWhoPurchasedLaptop);
} else {
  console.log("No customers found who purchased a Laptop.");
}
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  hobbies: ["reading", "coding"],
  address: {
    street: "123 Main St",
    city: "Bangkok"
  }
};

// Accessing properties
console.log(person.firstName);
console.log(person.lastName);
console.log(person.age);
console.log(person.hobbies[0],person.hobbies[1]);
console.log(person.address.street,person.address.city);
const fs = require('fs');

// Generate some text
const myText = "Pham Hong Dang!";

// Write the text to the shared file
fs.writeFileSync('data.txt', myText);
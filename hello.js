const fs = require('fs');

// Generate some text
const myText = "Pham Hong Dang! xm chao caho";

// Write the text to the shared file
fs.writeFileSync('data.txt', myText);
const { exec } = require("child_process");
const express = require("express");
const cors = require('cors')
const app = express();


// vvimp
const corsOpts = {
    origin: '*',
  
    methods: [
      'GET',
      'POST',
    ],
  
    allowedHeaders: [
      'Content-Type',
    ],
  };
  
  app.use(cors(corsOpts));

// Define the path to your Python script
const pythonScriptPath = "get_response.py";

// Create a function to execute the command and process the output
const executeScript = async (argument) => {
  try {
    const { stdout, stderr } = await new Promise((resolve, reject) => {
      exec(
        `python ${pythonScriptPath} ${argument}`,
        (error, stdout, stderr) => {
          if (error) {
            reject(error);
          } else {
            resolve({ stdout, stderr });
          }
        }
      );
    });

    // Process the output
    const output = stdout.trim();

    // Use the output outside the exec function
    console.log("This is the output:", output);

    return output;
  } catch (error) {
    console.error("Error executing Python script:", error);

    return "error has occured...";
  }
};

// Call the function t`o execute the script pass the argument
executeScript("hi");

app.set("view engine", "ejs");

app.use(express.json());

app.get("/", (req, res) => {
  res.render("base");
});

app.post("/request", async (req, res) => {
  console.log(req);

  // Access the message from the request body
  const message = req.body.message;

  // Process the message (example: convert to uppercase)
  const answer = await executeScript(message);

  // Create the response object
  const response = {
    answer: answer
  };

  // Send the response as JSON
  res.json(response);


});

app.listen(3000, () => {
  console.log("server is listening on port 3000");
});

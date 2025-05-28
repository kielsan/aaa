import express from "express";
import cors from "cors";
import fs from "fs";

const app = express();
const PORT = 3001;

// Middleware
app.use(cors());
app.use(express.json());

// API endpoint to get first signer and SOL senders
app.post("/api/data", async (req, res) => {
  const { tokenAddress } = req.body;

  // Read JSON file
  const data = JSON.parse(fs.readFileSync("data.json", "utf-8"));
  let a = data;
  a.content.push(req.body);
  // Write back to file
  fs.writeFileSync("data.json", JSON.stringify(a, null, 2));
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

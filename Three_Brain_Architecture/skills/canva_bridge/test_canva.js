import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "bash",
  args: [
    "-lc",
    'source "$HOME/.nvm/nvm.sh" && npx -y mcp-remote https://mcp.canva.com/mcp'
  ]
});

const client = new Client({
  name: "victoria-canva-bridge",
  version: "1.0.0"
});

try {
  await client.connect(transport);
  const result = await client.listTools();

  console.log("CANVA CONNECTED");
  console.log("TOOLS FOUND:", result.tools.length);

  for (const tool of result.tools) {
    console.log("-", tool.name);
  }
} finally {
  await client.close();
}

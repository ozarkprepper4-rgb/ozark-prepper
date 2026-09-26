import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

async function connect() {
  const transport = new StdioClientTransport({
    command: "bash",
    args: [
      "-lc",
      'source "$HOME/.nvm/nvm.sh" && npx -y mcp-remote https://mcp.canva.com/mcp'
    ]
  });

  const client = new Client({
    name: "victoria-ozark-prepper-canva",
    version: "1.0.0"
  });

  await client.connect(transport);
  return client;
}

async function main() {
  const args = process.argv.slice(2);
  const action = args[0];

  const client = await connect();

  try {
    if (action === "generate") {
      const designType = args[1];
      const description = args.slice(2).join(" ");

      if (!designType || !description) {
        throw new Error("Usage: generate <design_type> <description>");
      }

      const result = await client.callTool({
        name: "generate-design",
        arguments: {
          query: description,
          design_type: designType,
          user_intent: "Create Ozark Prepper content for Victoria and her team."
        }
      });

      console.log(JSON.stringify(result, null, 2));
      return;
    }

    if (action === "accept") {
      const jobId = args[1];
      const candidateId = args[2];

      if (!jobId || !candidateId) {
        throw new Error("Usage: accept <job_id> <candidate_id>");
      }

      const result = await client.callTool({
        name: "create-design-from-candidate",
        arguments: {
          job_id: jobId,
          candidate_id: candidateId,
          user_intent: "Save the selected Ozark Prepper Canva design for Victoria's team."
        }
      });

      console.log(JSON.stringify(result, null, 2));
      return;
    }

    if (action === "export") {
      const designId = args[1];
      const formatType = args[2] || "png";

      if (!designId) {
        throw new Error("Usage: export <design_id> <png|jpg|pdf|gif|pptx|mp4|csv>");
      }

      const result = await client.callTool({
        name: "export-design",
        arguments: {
          design_id: designId,
          format: {
            type: formatType,
            export_quality: formatType === "csv" ? undefined : "pro"
          },
          user_intent: "Export the selected Ozark Prepper design for Victoria's team."
        }
      });

      console.log(JSON.stringify(result, null, 2));
      return;
    }

    throw new Error("Actions: generate, accept, export");

  } finally {
    await client.close();
  }
}

main().catch(err => {
  console.error("CANVA ERROR:", err.message);
  process.exit(1);
});

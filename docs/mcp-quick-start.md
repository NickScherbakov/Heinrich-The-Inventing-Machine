# MCP Quick Start Guide

## For Developers New to MCP

This is a quick reference for getting started with GitHub MCP integration in the Heinrich project.

## What You Get

- AI can directly comment on GitHub issues and PRs
- AI can create and manage branches
- AI can search code and issues
- AI can update repository metadata
- No more copy-pasting AI responses!

## Fastest Way to Get Started (Hosted Setup)

### 1. Copy the Example Configuration
```bash
cp .mcp.json.example ~/.mcp.json
```

Or create `.mcp.json` in your project root with:
```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

### 2. Connect Your AI Assistant

When your AI assistant (like Claude Desktop or compatible tools) first connects:
- It will prompt for GitHub OAuth authorization
- Click the authorization link
- Approve the requested permissions
- Done!

### 3. Test It

Ask your AI: "Can you list the recent issues in the Heinrich repository?"

If it works, you're all set! 🎉

## For Local Development (Docker Setup)

### 1. Create GitHub Token

Go to: https://github.com/settings/tokens

Create token with scopes:
- `repo`
- `read:org`
- `user:email`
- `workflow`

### 2. Configure Environment

```bash
# Copy example file
cp .env.mcp.example .env.mcp

# Edit .env.mcp and add your token
# NEVER commit this file!
```

### 3. Start Docker Container

```bash
# Start
docker-compose -f docker-compose.mcp.yml up -d

# Check logs
docker-compose -f docker-compose.mcp.yml logs -f

# Stop
docker-compose -f docker-compose.mcp.yml down
```

### 4. Configure AI Assistant

Point to local server at `http://localhost:3000/mcp/`

## Need More Help?

📖 See the full guide: [docs/mcp-integration.md](mcp-integration.md)

## Troubleshooting Quick Fixes

**Can't connect?**
- Check your internet connection
- Verify OAuth authorization is complete
- For Docker: Check container is running with `docker ps`

**Authentication errors?**
- Regenerate your GitHub token
- Make sure token has required scopes
- Check token isn't expired

**Rate limiting?**
- Wait for rate limit reset (hourly)
- Use authenticated requests (higher limits)

## Example AI Commands to Try

Once connected, try these with your AI assistant:

1. "List open issues in this repository"
2. "Create a comment on issue #42 saying 'Working on this'"
3. "Search for files containing 'ProblemParser'"
4. "Show me the recent commits on the main branch"
5. "Create a branch called 'feature/test-mcp' from main"

## Security Reminders

- ⚠️ Never commit `.env.mcp` or `.mcp.json` files
- ⚠️ Use tokens with minimum required permissions
- ⚠️ Rotate tokens every 90 days
- ⚠️ Revoke tokens immediately if compromised

## Files Reference

- `.mcp.json.example` - Hosted MCP configuration template
- `.env.mcp.example` - Environment variables template for Docker
- `docker-compose.mcp.yml` - Docker setup for local deployment
- `.vscode/settings.mcp.json.example` - VS Code integration example
- `docs/mcp-integration.md` - Complete integration guide

---

**Ready to experience seamless AI collaboration with Heinrich!** 🚀

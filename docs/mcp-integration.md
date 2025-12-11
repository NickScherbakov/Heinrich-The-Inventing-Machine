# GitHub MCP Server Integration Guide

## Overview

This guide explains how to set up GitHub MCP (Model Context Protocol) Server integration for the Heinrich project. MCP enables seamless interaction between AI assistants (like GitHub Copilot) and GitHub repositories, allowing AI to directly perform actions without manual copying and pasting.

### What is MCP?

Model Context Protocol (MCP) is an open standard developed by Anthropic that provides AI assistants with standardized access to external tools and services. The GitHub MCP Server specifically enables AI to:

- Comment on issues and pull requests
- Create and manage branches
- Update repository metadata
- Manage collaborators
- Search code and issues
- And much more!

## Benefits for Heinrich

MCP integration aligns perfectly with Heinrich's mission of automation and improving creative processes. It creates a "bridge" between human intention and AI execution, enabling:

- **Faster workflow**: No manual copying of AI-generated content
- **Seamless collaboration**: AI can directly interact with GitHub
- **Enhanced productivity**: Reduced friction in development processes
- **Better integration**: AI becomes a true collaborator in the development process

## Setup Options

There are two main ways to set up GitHub MCP Server:

1. **Hosted MCP Server** (Recommended) - Easier setup, no local infrastructure needed
2. **Local Docker MCP Server** - More control, runs on your machine

---

## Option A: Hosted MCP Server (Recommended)

The hosted variant uses GitHub's official MCP endpoint and OAuth authentication.

### Prerequisites

- GitHub account with appropriate repository access
- AI assistant that supports MCP (e.g., Claude Desktop, GitHub Copilot compatible tools)
- Access to repository settings

### Step 1: Create MCP Configuration File

Create a `.mcp.json` file in your home directory or project root:

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "metadata": {
        "name": "GitHub MCP Server",
        "description": "Official GitHub MCP integration for Heinrich project"
      }
    }
  }
}
```

### Step 2: OAuth Authentication

1. When your AI assistant first connects to the MCP server, it will prompt for GitHub OAuth authorization
2. Click the authorization link provided
3. Authorize the application with required scopes:
   - `repo` (Full control of private repositories)
   - `read:org` (Read org and team membership)
   - `user:email` (Access user email addresses)
   - `workflow` (Update GitHub Action workflows)

### Step 3: Verify Connection

Test the connection by asking your AI assistant to perform a simple GitHub operation:

```
"Can you list the recent issues in this repository?"
```

If successful, the AI will retrieve and display the issues directly.

### Supported Operations (Hosted)

- Reading issues, PRs, and comments
- Creating comments on issues and PRs
- Creating and managing branches
- Searching code and repositories
- Reading file contents
- Updating issue labels
- Managing project metadata

### Limitations (Hosted)

- Requires active internet connection
- Subject to GitHub API rate limits
- Dependent on GitHub's hosted service availability

---

## Option B: Local Docker MCP Server

The local variant gives you more control and allows for customization.

### Prerequisites

- Docker and Docker Compose installed
- GitHub Personal Access Token (PAT)
- Port 3000 available (or configure alternative)

### Step 1: Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Heinrich MCP Server")
4. Select the following scopes:
   - `repo` (Full control of private repositories)
   - `read:org` (Read org and team membership)
   - `user:email` (Access user email addresses)
   - `workflow` (Update GitHub Action workflows)
   - `admin:repo_hook` (Full control of repository hooks) - optional
5. Click "Generate token" and **save the token securely**

### Step 2: Set Up Environment Variables

Create a `.env.mcp` file in your project root (this file is gitignored):

```bash
# GitHub Personal Access Token
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token_here

# Repository Configuration
GITHUB_OWNER=NickScherbakov
GITHUB_REPO=Heinrich-The-Inventing-Machine

# Server Configuration
MCP_PORT=3000
```

**Important**: Never commit this file to version control!

### Step 3: Create Docker Compose Configuration

Use the provided `docker-compose.mcp.yml` file (see Configuration Files section below).

### Step 4: Start the MCP Server

```bash
# Start the server
docker-compose -f docker-compose.mcp.yml up -d

# Check logs
docker-compose -f docker-compose.mcp.yml logs -f

# Stop the server
docker-compose -f docker-compose.mcp.yml down
```

### Step 5: Configure AI Assistant

Point your AI assistant to the local MCP server:

```json
{
  "mcpServers": {
    "github-local": {
      "url": "http://localhost:3000/mcp/",
      "metadata": {
        "name": "Local GitHub MCP Server",
        "description": "Self-hosted GitHub MCP for Heinrich"
      }
    }
  }
}
```

### Supported Operations (Local)

All operations from hosted variant, plus:
- Custom extensions and plugins
- Local caching for faster responses
- Custom rate limiting configuration
- Offline operation (with cached data)

---

## VS Code Integration

### Option 1: Add to Existing Settings

Add the following to `.vscode/settings.json`:

```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": true,
    "plaintext": true,
    "markdown": true
  },
  "github.copilot.mcp.enabled": true,
  "github.copilot.mcp.servers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

### Option 2: Use Example Configuration

Copy `.vscode/settings.mcp.json.example` to `.vscode/settings.json` and customize as needed.

---

## Security Considerations

### Token Security

- **Never commit tokens** to version control
- Use environment variables or secure vaults for tokens
- Rotate tokens regularly (every 90 days recommended)
- Use tokens with minimum required scopes
- Revoke tokens immediately if compromised

### Access Control

- Review which AI assistants have access to your MCP server
- Regularly audit OAuth authorizations in GitHub settings
- Use separate tokens for different environments (dev, staging, prod)
- Consider using fine-grained personal access tokens for better security

### Network Security

- For local deployment, restrict access to localhost only
- Use HTTPS for any remote connections
- Consider using VPN or SSH tunneling for remote access
- Implement rate limiting to prevent abuse

---

## Troubleshooting

### Connection Issues

**Problem**: AI assistant cannot connect to MCP server

**Solutions**:
- Verify the URL is correct (check for typos)
- Ensure OAuth authorization is complete
- Check network connectivity
- For local deployment, verify Docker container is running

### Authentication Errors

**Problem**: "Authentication failed" or "Invalid token"

**Solutions**:
- Regenerate GitHub Personal Access Token
- Verify token scopes include required permissions
- Check token expiration date
- Ensure token is correctly set in environment variables

### Rate Limiting

**Problem**: "Rate limit exceeded" errors

**Solutions**:
- Wait for rate limit reset (usually hourly)
- Use authenticated requests (higher limits)
- Implement caching in your workflow
- Consider upgrading to GitHub Enterprise for higher limits

### Docker Issues

**Problem**: Container won't start

**Solutions**:
```bash
# Check Docker is running
docker info

# View detailed logs
docker-compose -f docker-compose.mcp.yml logs --tail=100

# Rebuild container
docker-compose -f docker-compose.mcp.yml build --no-cache

# Check port availability
netstat -an | grep 3000
```

---

## Advanced Configuration

### Custom Port Configuration

Edit `docker-compose.mcp.yml`:

```yaml
ports:
  - "8080:3000"  # Map to different host port
```

### Multiple Repository Access

For accessing multiple repositories, configure multiple server instances:

```json
{
  "mcpServers": {
    "github-heinrich": {
      "url": "https://api.githubcopilot.com/mcp/",
      "metadata": {
        "repository": "NickScherbakov/Heinrich-The-Inventing-Machine"
      }
    },
    "github-other": {
      "url": "https://api.githubcopilot.com/mcp/",
      "metadata": {
        "repository": "owner/other-repo"
      }
    }
  }
}
```

### Logging Configuration

For local deployment, configure logging in Docker Compose:

```yaml
environment:
  - LOG_LEVEL=debug  # debug, info, warn, error
  - LOG_FORMAT=json  # json, text
```

---

## Example Workflows

### Commenting on Issues

```
AI Prompt: "Add a comment to issue #42 saying we're working on the MCP integration"
AI Action: Automatically posts comment via MCP
```

### Creating Branches

```
AI Prompt: "Create a new branch called 'feature/mcp-enhancements' from main"
AI Action: Creates branch directly in repository
```

### Searching Code

```
AI Prompt: "Find all Python files that import 'ProblemParser'"
AI Action: Searches repository and returns results
```

### Managing Labels

```
AI Prompt: "Add 'documentation' and 'enhancement' labels to issue #15"
AI Action: Updates issue labels directly
```

---

## References

The following resources provide additional information about GitHub MCP Server and the Model Context Protocol. While these links were valid at the time of writing, please check for the most current documentation:

- [GitHub Blog: A practical guide on how to use the GitHub MCP server](https://github.blog/ai-and-ml/generative-ai/a-practical-guide-on-how-to-use-the-github-mcp-server/)
- [Model Context Protocol servers repository](https://github.com/modelcontextprotocol/servers)
- [Setting Up the Official GitHub MCP Server by Debbie O'Brien](https://debbie.codes/blog/github-mcp-server/)
- [GitHub MCP Server Setup & Configuration Guide by Synlabs](https://www.synlabs.io/post/github-mcp-server-setup-configuration)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)

**Note**: For the most up-to-date information, always refer to the official GitHub and MCP documentation.

---

## Support

If you encounter issues with MCP integration:

1. Check the troubleshooting section above
2. Review the GitHub MCP Server documentation
3. Open an issue in the Heinrich repository with:
   - Your setup type (hosted/local)
   - Error messages
   - Steps to reproduce
   - Environment details (OS, Docker version, etc.)

---

## Contributing

Found a way to improve MCP integration? We welcome contributions!

1. Document your improvement in this guide
2. Test thoroughly with both setup variants
3. Submit a pull request with clear description
4. Update examples if adding new capabilities

---

**Remember**: MCP integration represents Heinrich's commitment to seamless human-AI collaboration in the inventive problem-solving process. Use it to enhance your workflow and contribute to the community!

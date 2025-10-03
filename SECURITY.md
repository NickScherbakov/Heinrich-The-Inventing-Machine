# Security Policy

## Supported Versions

Heinrich follows semantic versioning. We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | ✅ Full support    |
| 0.5.x   | ✅ Security fixes  |
| < 0.5   | ❌ End of life     |

## Security Considerations

### LLM Integration Risks

Heinrich integrates with various Large Language Model providers. Be aware of:

- **Data Privacy**: Problem descriptions sent to external LLM APIs
- **API Key Security**: Secure storage of provider credentials
- **Prompt Injection**: Potential manipulation of TRIZ reasoning through crafted inputs
- **Output Validation**: Generated solutions should be validated before implementation

### Knowledge Base Integrity

- All TRIZ knowledge sources are validated against authoritative references
- Scientific effects database includes proper attributions
- Case studies use only publicly available or properly licensed examples

### Ethical AI Boundaries

- Heinrich persona maintains clear boundaries about being an AI system
- No claims of simulating real persons (living or deceased)
- Educational focus with appropriate disclaimers about solution applicability

## Reporting Security Vulnerabilities

**Do NOT create public GitHub issues for security vulnerabilities.**

Instead, please send a detailed report to: **security@heinrich-triz.org**

### What to Include

1. **Vulnerability Description**: Clear description of the security issue
2. **Reproduction Steps**: Step-by-step instructions to reproduce the issue
3. **Impact Assessment**: Potential impact and affected components
4. **Proof of Concept**: If applicable, minimal code demonstrating the issue
5. **Suggested Fix**: If you have ideas for fixing the vulnerability

### Response Timeline

- **Initial Response**: Within 48 hours
- **Vulnerability Assessment**: Within 7 days
- **Fix Development**: Varies by complexity, typically 2-4 weeks
- **Public Disclosure**: After fix is released and users have time to update

## Security Best Practices

### For Users

1. **API Keys**: Store LLM provider API keys securely
   ```bash
   # Use environment variables, not hardcoded strings
   export OPENAI_API_KEY="your-secure-key"
   ```

2. **Input Validation**: Sanitize problem descriptions before processing
   ```python
   # Example input validation
   def validate_problem_input(text: str) -> bool:
       if len(text) > 10000:  # Reasonable length limit
           return False
       if contains_suspicious_patterns(text):
           return False
       return True
   ```

3. **Output Review**: Always review generated solutions before implementation
4. **Network Security**: Use HTTPS for all API communications
5. **Regular Updates**: Keep Heinrich updated to latest version

### For Developers

1. **Dependency Management**: Regularly update dependencies
   ```bash
   pip-audit  # Check for known vulnerabilities
   ```

2. **Code Scanning**: Use static analysis tools
   ```bash
   bandit -r heinrich/  # Security linting
   ```

3. **Secrets Management**: Never commit secrets to repository
4. **Input Sanitization**: Validate all external inputs
5. **Error Handling**: Don't expose internal details in error messages

## Secure Configuration

### Environment Variables

```bash
# Required
HEINRICH_API_MODE=production  # Never use 'debug' in production
HEINRICH_LOG_LEVEL=INFO       # Don't use DEBUG in production

# LLM Provider Keys (choose one or more)
OPENAI_API_KEY=your-key
ANTHROPIC_API_KEY=your-key

# Optional Security Settings
HEINRICH_MAX_INPUT_LENGTH=5000
HEINRICH_ENABLE_SAFETY_FILTERS=true
HEINRICH_OUTPUT_SANITIZATION=true
```

### Network Security

```yaml
# docker-compose.yml security configuration
version: '3.8'
services:
  heinrich:
    image: heinrich:latest
    environment:
      - HEINRICH_API_MODE=production
    networks:
      - heinrich-internal
    read_only: true
    user: "1000:1000"  # Non-root user
    
networks:
  heinrich-internal:
    internal: true
```

## Threat Model

### Assets We Protect

1. **User Problem Data**: Confidential problem descriptions and solutions
2. **API Credentials**: LLM provider authentication keys  
3. **TRIZ Knowledge Base**: Integrity of methodology implementation
4. **System Availability**: Reliable operation of Heinrich services

### Potential Threats

1. **Prompt Injection**: Malicious inputs attempting to manipulate reasoning
2. **Data Exfiltration**: Unauthorized access to problem/solution data
3. **Credential Theft**: Compromise of LLM provider API keys
4. **Service Disruption**: DoS attacks or resource exhaustion
5. **Supply Chain**: Compromised dependencies or base images

### Security Controls

1. **Input Validation**: Comprehensive sanitization of all inputs
2. **Authentication**: Secure API key management and rotation
3. **Authorization**: Principle of least privilege access
4. **Encryption**: TLS for data in transit, encryption for data at rest
5. **Monitoring**: Logging and alerting for suspicious activities
6. **Testing**: Regular security testing and vulnerability assessments

## Compliance

Heinrich is designed to support various compliance requirements:

- **GDPR**: Personal data handling and user consent mechanisms
- **SOC 2**: Security controls for service organizations
- **ISO 27001**: Information security management practices

## Security Contact

For non-urgent security questions: security@heinrich-triz.org
For urgent security issues: Use encrypted communication (PGP key available on request)

## Acknowledgments

We appreciate responsible disclosure and will acknowledge security researchers who help improve Heinrich's security (with their permission).

---

**Remember**: Security is a shared responsibility. Users, developers, and maintainers all play a role in keeping Heinrich secure and trustworthy.
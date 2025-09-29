# Migration Guide: Enhanced Release Workflow with DAK Processing

This guide provides step-by-step instructions for migrating from the standard release workflow to the enhanced version with complete DAK processing capabilities.

## Quick Migration Checklist

- [ ] Backup existing workflow files
- [ ] Add enhanced workflow to smart-html repository
- [ ] Update repository workflow files
- [ ] Add DAK configuration
- [ ] Test the enhanced workflow
- [ ] Update documentation and links

## Step 1: Backup Existing Files

Before making any changes, backup your current workflow configuration:

```bash
# Backup existing workflow (if it exists)
cp .github/workflows/release.yml .github/workflows/release-backup.yml

# Backup any existing release configuration
cp release-config.yaml release-config-backup.yaml 2>/dev/null || echo "No existing config"
```

## Step 2: Add Enhanced Workflow to smart-html

If you're maintaining the smart-html repository, add these files:

```bash
# Copy the enhanced workflow
cp release-enhanced.yml .github/workflows/

# Copy the DAK processor script  
cp dak_processor.py scripts/

# Copy the enhanced release configuration
cp release-config-dak.yaml scripts/

# Copy documentation
cp README-DAK-RELEASE.md .
```

## Step 3: Update Repository Workflows

For each repository that should use DAK processing:

### A. Create/Update `.github/workflows/release.yml`

```yaml
name: Release IG with DAK Processing

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:
      sitepreview_dir:
        description: 'Site preview directory name'
        required: false
        default: 'sitepreview'
      do_dak:
        description: 'Enable DAK processing'
        required: false
        type: boolean
        default: true

jobs:
  release:
    uses: costateixeira/smart-html/.github/workflows/release-enhanced.yml@main
    with:
      pubreq_package_id: "your.package.id"           # Replace with your package ID
      pubreq_version: ${{ github.event.release.tag_name || 'dev' }}
      pubreq_canonical: "http://your.domain/your-ig" # Replace with your canonical URL
      pubreq_path: "/your-ig"                        # Replace with your path
      sitepreview_dir: ${{ github.event.inputs.sitepreview_dir || 'sitepreview' }}
      do_dak: ${{ github.event.inputs.do_dak != 'false' }}
    secrets: inherit
```

### B. Add `release-config.yaml` to Repository Root

```yaml
# Basic DAK-enabled configuration
dak:
  enabled: true

# Standard IG configuration
source_dir: "."
webroot_repo: "https://github.com/costateixeira/smart-html"
registry_repo: "https://github.com/costateixeira/ig-registry"

# Repository-specific settings
publication:
  canonical: "http://your.domain/your-ig"
  package_id: "your.package.id"
  
deployment:
  sitepreview_dir: "sitepreview"
  exclude:
    - "ig-build-zips/"
    - "temp/"
```

## Step 4: Enable DAK Processing

Choose one of these methods to enable DAK processing:

### Option A: Add dak.json (Recommended for DAK repositories)

Create `dak.json` in repository root:

```json
{
  "resourceType": "DAK",
  "id": "your.ig.id",
  "name": "YourIGName", 
  "title": "Your Implementation Guide Title",
  "description": "Description of your implementation guide",
  "version": "1.0.0",
  "status": "draft",
  "publicationUrl": "http://your.domain/your-ig",
  "publisher": {
    "name": "Your Organization",
    "url": "http://your.organization"
  }
}
```

### Option B: Add smart-base Dependency (For SMART Guidelines)

Update `sushi-config.yaml`:

```yaml
# Existing configuration...

dependencies:
  smart.who.int.base: current  # Add this line
  
# Rest of your configuration...
```

## Step 5: Test the Enhanced Workflow

### A. Test with Workflow Dispatch

1. Go to your repository on GitHub
2. Click **Actions** tab
3. Select **Release IG with DAK Processing** workflow
4. Click **Run workflow**
5. Choose branch and verify settings
6. Click **Run workflow**

### B. Monitor the Build

Check these sections in the workflow logs:

- ✅ **Setup** - Environment and dependencies
- ✅ **Standard IG Build** - FHIR IG Publisher execution
- ✅ **DAK Post-Processing** - Schema and API generation
- ✅ **Artifact Copy** - Moving DAK files to deployment
- ✅ **Deployment** - Publishing to GitHub Pages

### C. Verify Generated Artifacts

After successful completion, check your GitHub Pages site:

```
https://yourusername.github.io/your-repo/sitepreview/
```

Look for these new files:
- `dak-api.html` - DAK API documentation hub
- `ValueSet-*.schema.json` - JSON schemas for ValueSets
- `ValueSet-*.jsonld` - JSON-LD vocabularies
- `StructureDefinition-*.schema.json` - Logical model schemas
- `qa.json` - Enhanced QA report

## Step 6: Update Documentation

### A. Update Repository README

Add a section about the enhanced features:

```markdown
## API Documentation

This implementation guide includes comprehensive API documentation:

- **DAK API Hub**: [dak-api.html](https://yourusername.github.io/your-repo/sitepreview/dak-api.html)
- **JSON Schemas**: Validation schemas for all ValueSets and Logical Models
- **JSON-LD Vocabularies**: Semantic web integration for ValueSets
- **OpenAPI Specifications**: Complete API documentation for all endpoints

## Release Process

This repository uses the enhanced release workflow with DAK processing. 
To create a release:

1. Create a new release on GitHub
2. The workflow automatically builds and deploys with DAK processing
3. Access the enhanced IG at the GitHub Pages URL
```

### B. Update Links and References

Update any existing documentation to reference the new artifact locations:

- Link to `dak-api.html` instead of basic artifact lists
- Reference JSON schema files for validation examples
- Include JSON-LD vocabularies in semantic web documentation

## Common Migration Issues

### Issue: DAK Processing Not Running

**Symptoms**: Workflow completes but no DAK artifacts generated

**Solutions**:
1. Check `do_dak` parameter is `true` in workflow
2. Verify either `dak.json` exists or smart-base dependency is present
3. Check workflow logs for "DAK processing not enabled" messages

### Issue: Script Download Failures

**Symptoms**: Errors downloading DAK scripts from smart-base

**Solutions**:
1. Verify smart-base repository is accessible
2. Check network connectivity in GitHub Actions
3. Verify script names exist in smart-base repository

### Issue: Missing Artifacts in Deployment

**Symptoms**: DAK processing runs but artifacts don't appear in final site

**Solutions**:
1. Check "Copy DAK artifacts to webroot" step in logs
2. Verify output directory exists and contains artifacts
3. Check file permissions and copy commands

### Issue: Performance/Timeout Problems

**Symptoms**: Workflow times out during DAK processing

**Solutions**:
1. Increase memory allocation for Java in workflow
2. Add timeout configuration to release-config.yaml
3. Consider excluding large files from processing

## Rollback Procedure

If you need to rollback to the standard workflow:

### A. Restore Standard Workflow

```bash
# Restore original workflow
cp .github/workflows/release-backup.yml .github/workflows/release.yml

# Or use standard workflow reference
```

Update workflow to use standard release:

```yaml
jobs:
  release:
    uses: costateixeira/smart-html/.github/workflows/release.yml@main  # Remove -enhanced
    with:
      # Remove do_dak parameter
      pubreq_package_id: "your.package.id"
      # ... other standard parameters
```

### B. Clean Up Configuration

```bash
# Remove DAK-specific configuration (optional)
rm dak.json  # If you added this
rm release-config.yaml  # If you only added it for DAK

# Or update release-config.yaml to disable DAK
```

```yaml
# Disable DAK in configuration
dak:
  enabled: false
```

## Testing Checklist

Before fully migrating, test these scenarios:

- [ ] **Standard Release**: Create a test release and verify basic IG generation
- [ ] **DAK Artifacts**: Verify all DAK artifacts are generated and accessible
- [ ] **API Documentation**: Check that dak-api.html loads and contains expected content
- [ ] **Schema Validation**: Test that generated JSON schemas are valid
- [ ] **Performance**: Ensure build time is acceptable for your repository size
- [ ] **Links and Navigation**: Verify all internal links work in the enhanced IG

## Support

If you encounter issues during migration:

1. **Check Logs**: Review complete GitHub Actions logs for specific errors
2. **Validate Configuration**: Use YAML validators for configuration files
3. **Test Locally**: Run individual DAK scripts locally to isolate issues
4. **Report Issues**: Open issues in smart-html or smart-base repositories
5. **Rollback**: Use rollback procedure if critical issues occur

## Next Steps

After successful migration:

1. **Monitor Performance**: Track build times and resource usage
2. **Update Team Documentation**: Train team on new features and artifacts
3. **Integrate API Documentation**: Link to DAK API hub from main documentation
4. **Customize Configuration**: Tune settings based on your repository's needs
5. **Contribute Improvements**: Share feedback and contribute enhancements

---

For additional help, see the complete [README-DAK-RELEASE.md](README-DAK-RELEASE.md) documentation.

# Publication Release Workflow

This workflow automates the creation of pull requests in the smart-html repository when smart-XXX repositories publish release branches.

## Overview

The publication release workflow enables automatic integration of published content from WHO SMART Guidelines repositories (smart-XXX pattern) into the main smart.who.int website hosted by the smart-html repository.

## How It Works

### Trigger Methods

The workflow can be triggered in three ways:

1. **Repository Dispatch** (Primary method)
   - Triggered by other workflows using the `repository_dispatch` event
   - Event type: `release-publication-request`

2. **Workflow Call** (Direct method)
   - Can be called directly from other workflows
   - Requires explicit input parameters

3. **Manual Dispatch** (GitHub UI method)
   - Can be triggered manually from the GitHub Actions UI
   - Allows users to manually initiate publication releases
   - Accessible from the "Actions" tab in the smart-html repository

### Workflow Process

1. **Validation**: Verifies the request meets security requirements
   - Repository must be in WorldHealthOrganization
   - Repository must follow smart-XXX pattern (excluding smart-html)
   - Branch must follow release-* pattern

2. **Content Download**: Downloads published content from the source repository
   - Source: `smart-XXX/gh-pages/branches/release-*`
   - Target: Local temporary directory

3. **PR Creation**: Creates a pull request in smart-html
   - Creates new branch: `release-{repo-code}-{release-version}`
   - Copies content to appropriate directory: `{repo-code}/`
   - Uses squash commits for compact artifacts

## Security Features

### Organization Verification
- Only accepts requests from WorldHealthOrganization repositories
- Rejects requests from external organizations

### Repository Pattern Validation
- Only processes smart-XXX repositories (excluding smart-html itself)
- Prevents unauthorized repository access

### Branch Pattern Validation
- Only processes release-* branches
- Prevents accidental triggers from development branches

### Safe Content Handling
- Python scripts are located in `.github/scripts/` (not deployed to GitHub Pages)
- Uses GitHub's secure token handling
- Follows GitHub variable injection safety protocols

## Usage Examples

### From smart-base ghbuild workflow

```yaml
- name: Trigger publication release
  if: success() && startsWith(github.ref_name, 'release-')
  run: |
    curl -X POST \
      -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
      -H "Accept: application/vnd.github.v3+json" \
      "https://api.github.com/repos/WorldHealthOrganization/smart-html/dispatches" \
      -d "{
        \"event_type\": \"release-publication-request\",
        \"client_payload\": {
          \"source_repository\": \"smart-trust\",
          \"release_branch\": \"release-v1.0.0\",
          \"source_owner\": \"WorldHealthOrganization\"
        }
      }"
```

### Direct workflow call

```yaml
jobs:
  trigger-release:
    uses: WorldHealthOrganization/smart-html/.github/workflows/publication-release.yml@main
    with:
      source_repository: "smart-trust"
      release_branch: "release-v1.0.0"
      source_owner: "WorldHealthOrganization"
```

### Manual dispatch from GitHub UI

To manually trigger the publication release workflow:

1. Navigate to the WorldHealthOrganization/smart-html repository
2. Go to the "Actions" tab
3. Select "Publication Release Workflow" from the workflow list
4. Click "Run workflow"
5. Fill in the required parameters:
   - **Source repository**: The smart-XXX repository name (e.g., "smart-trust")
   - **Release branch**: The release branch name (e.g., "release-v1.0.0") 
   - **Source owner**: Repository owner (defaults to "WorldHealthOrganization")
6. Click "Run workflow" to start the publication process

This method is useful for:
- Testing the publication workflow
- Manually triggering releases when automated triggers fail
- Re-running publication for existing release branches

## Expected Behavior

### Successful Execution
When the workflow executes successfully:

1. **Existing PR Handling**: If a PR already exists for the same release:
   - The existing PR is automatically closed with a comment
   - The existing branch is deleted
   - A new branch and PR are created with the latest content

2. **New PR Created**: A new pull request is created with:
   - Title: "Release: Add {repo-name} content from {release-branch}"
   - Branch: `{repo-code}-release-{release-version}` (e.g., `trust-release-v1.0.0`)
   - Content: Published files from the release branch

3. **Directory Structure**: Content is placed in the appropriate directory:
   ```
   smart-html/
   ├── trust/          # Content from smart-trust
   ├── base/           # Content from smart-base
   ├── immunizations/  # Content from smart-immunizations
   └── ...
   ```

4. **Approval to Publish**: The PR includes an "Approval to Publish" section and can be merged to publish content to smart.who.int

### Branch Naming Convention
- Format: `{repo-code}-release-{release-version}`
- Examples:
  - `trust-release-v1.0.0` (from smart-trust, release-v1.0.0)
  - `base-release-2024.1` (from smart-base, release-2024.1)
  - `immunizations-release-beta` (from smart-immunizations, release-beta)

### Error Handling
- Invalid repositories are rejected with clear error messages
- Missing content results in workflow failure with diagnostic information
- Network errors are logged and reported

## Directory Mapping

The workflow maps smart-XXX repositories to directories in smart-html:

| Source Repository | Target Directory | Published URL |
|------------------|------------------|---------------|
| smart-trust | trust/ | smart.who.int/trust |
| smart-base | base/ | smart.who.int/base |
| smart-immunizations | immunizations/ | smart.who.int/immunizations |
| smart-{code} | {code}/ | smart.who.int/{code} |

## Monitoring and Debugging

### Logs
The workflow provides detailed logs for:
- Validation steps and results
- Content download progress
- PR creation status
- Error conditions

### GitHub Actions
- View workflow runs in the Actions tab
- Check individual step outputs for debugging
- Review failed runs for error analysis

### PR Comments
Created PRs include comprehensive information:
- Source repository and branch details
- Content location and structure
- Review checklist
- Workflow metadata

## Maintenance

### Updating the Workflow
1. Test changes on a feature branch first
2. Validate with actual smart-XXX repositories
3. Update documentation as needed
4. Coordinate with smart-base workflow changes

### Security Updates
- Review and update Python dependencies regularly
- Monitor GitHub security advisories
- Update action versions as needed

## Troubleshooting

### Common Issues

**Permission Denied**
- Verify GITHUB_TOKEN has appropriate permissions
- Check repository access settings

**Content Not Found**
- Verify release branch exists in source repository
- Check gh-pages branch has the expected content structure
- Confirm deployment completed successfully

**PR Creation Failed**
- Check for branch name conflicts
- Verify base branch (main) exists and is accessible
- Review GitHub API rate limits

### Support
For issues with the publication release workflow:

1. Check the workflow run logs in GitHub Actions
2. Review the smart-base ghbuild workflow logs
3. Contact the repository maintainers
4. Create an issue in the smart-html repository
# Smart-Base GHBuild Workflow Changes

This document describes the necessary changes to the smart-base ghbuild workflow to support the new publication release automation.

## Required Changes

### 1. Add Release Branch Detection

The smart-base ghbuild workflow needs to detect when a release branch (following the `release-*` pattern) has been successfully deployed and trigger the publication release workflow in smart-html.

Add this step after the successful deployment steps:

```yaml
- name: Trigger publication release for release branches
  if: env.IS_DEFAULT_BRANCH == 'false' && startsWith(github.ref_name, 'release-')
  run: |
    echo "Release branch detected: ${{ github.ref_name }}"
    echo "Checking if deployment was successful..."
    
    # Only trigger if this is a WHO organization repository
    if [[ "${{ github.repository_owner }}" == "WorldHealthOrganization" ]]; then
      echo "Triggering publication release workflow in smart-html..."
      
      # Extract repository name
      REPO_NAME="${{ github.repository }}"
      REPO_NAME="${REPO_NAME#*/}"
      
      # Trigger the publication release workflow via repository_dispatch
      curl -X POST \
        -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
        -H "Accept: application/vnd.github.v3+json" \
        "https://api.github.com/repos/WorldHealthOrganization/smart-html/dispatches" \
        -d "{
          \"event_type\": \"release-publication-request\",
          \"client_payload\": {
            \"source_repository\": \"$REPO_NAME\",
            \"release_branch\": \"${{ github.ref_name }}\",
            \"source_owner\": \"${{ github.repository_owner }}\",
            \"workflow_run_id\": \"${{ github.run_id }}\",
            \"commit_sha\": \"${{ github.sha }}\"
          }
        }"
      
      echo "✅ Publication release request sent to smart-html repository"
    else
      echo "⚠️ Skipping publication release - not a WHO organization repository"
    fi
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 2. Add Conditional Logic

Update the existing deployment condition to account for the new behavior:

```yaml
- name: Deploy candidate
  uses: JamesIves/github-pages-deploy-action@v4.4.2
  if: env.IS_DEFAULT_BRANCH == 'false'
  with:
    branch: gh-pages
    folder: ./output
    commit-message: Deploy candidate branch
    target-folder: branches/${{ env.BRANCH_DIR }}
    single-commit: true
    clean: false 
```

This ensures that release branches are deployed to the `branches/release-*` folder structure that the publication release workflow expects.

### 3. Add Environment Variables

Ensure these environment variables are available in the workflow:

```yaml
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 4. Security Considerations

The workflow should only trigger the publication release for:

- Repositories in the WorldHealthOrganization
- Repositories following the smart-* naming pattern (excluding smart-html)
- Branches following the release-* pattern
- Successful deployments only

### 5. Required Permissions

Ensure the workflow has the necessary permissions:

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

## Integration Points

### Trigger Timing

The publication release should be triggered:

1. **After** the gh-pages deployment is successful
2. **Only** for release-* branches
3. **Only** for WHO organization repositories
4. **Only** for smart-* repositories (excluding smart-html)

### Data Flow

1. smart-XXX repository creates a release-* branch
2. smart-base ghbuild workflow deploys to gh-pages/branches/release-*
3. Upon successful deployment, triggers smart-html publication-release workflow
4. smart-html workflow downloads content from smart-XXX/gh-pages/branches/release-*
5. smart-html workflow creates a PR to include the content in the main smart.who.int site

### Error Handling

The workflow should handle these scenarios gracefully:

- Network failures when calling the smart-html repository
- Missing or invalid release content
- Existing PRs for the same release
- Permission issues

## Testing

To test the integration:

1. Create a release-* branch in a smart-XXX repository
2. Verify the ghbuild workflow deploys to gh-pages/branches/release-*
3. Verify the publication release workflow is triggered in smart-html
4. Verify a PR is created in smart-html with the appropriate content

## Monitoring

Add logging to track:

- When publication release requests are sent
- Success/failure of the API calls
- Branch and repository information for debugging

## Rollback Plan

If issues arise, the trigger can be disabled by:

1. Commenting out or removing the trigger step
2. The existing deployment functionality remains unchanged
3. Manual PR creation can be used as a fallback
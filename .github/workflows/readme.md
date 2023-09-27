# ReleaseBuild Workflow

This is a GitHub Actions workflow designed to be called from other repositories, To set up the environment, clone the smart-html repository, download necessary dependencies, and perform the publication process for a FHIR IG Release.

## Usage

To use this workflow in your repository, follow these steps:

1. Create a workflow file in your repository and call this workflow. For example, you can call this workflow from your repository's workflow file like this:

```
    jobs:
      call_build: 
        uses: WorldHealthOrganization/smart-html/.github/workflows/release.yml@main
```

   This will trigger the ReleaseBuild workflow from the smart-html repository.

2. Create a branch in your FHIR Implementation Guide (IG) repository called "release-candidate."

3. In the "release-candidate" branch, create a file named `publication-request.json`. This file may contain information or instructions related to the publication process.

4. When you want to initiate the publication process, trigger the workflow by following the defined 'workflow_call' event. The workflow will set up the environment, clone the smart-html repository, and generate a preview of the site to be published.

## Workflow Details

The ReleaseBuld workflow performs the following actions:

1. Sets up the environment using the `hl7fhir/ig-publisher-base:latest` Docker container.

2. Clones the published web site.

3. Downloads necessary dependencies, including the FHIR IG Publisher tool.

4. Performs the publication process for the FHIR IG Release.

5. Creates an updated website for preview.

6. Deploys the generated preview to the 'gh-pages' branch under the "website" folder.

## Contact

For questions or assistance with this workflow, please contact the repository maintainers.

Author: \[Your Name\]
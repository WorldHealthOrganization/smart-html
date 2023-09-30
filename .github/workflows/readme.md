# ReleaseBuild Workflow

This is a GitHub Actions workflow designed to prepare a new FHIR IG release publication 
It sets up the environment, clones the smart-html repository, downloading necessary dependencies, and builds the release, leaving a preview of the website in a folder in the IG repository.

## Usage

To use this workflow in your repository, follow these steps:

### Setup
1. To setup yyour repository for this auto release build, simply call this workflow from the IG repository. For example, adding this to a workflow in the repository:

```
    jobs:
      call_build: 
        uses: WorldHealthOrganization/smart-html/.github/workflows/release.yml@main
```

   This will trigger the workflow. 


### Trigger publication release

The workflow is triggered when the branch is called `release-candidate` and there's a publication-request.json`  file present. To preview a release, simply set this up when the IG is ready:

2. Create a branch in your FHIR Implementation Guide (IG) repository called "release-candidate."

3. In the "release-candidate" branch, create a file named `publication-request.json`. This file may contain information or instructions related to the publication process.



## Workflow Details

This workflow performs the following actions:

1. Sets up the environment using the `hl7fhir/ig-publisher-base:latest` Docker container.

2. Clones the published web site.

3. Downloads necessary dependencies, including the FHIR IG Publisher tool.

4. Performs the publication process for the FHIR IG Release.

5. Creates an updated website for preview.

6. Deploys the generated preview to the `gh-pages` branch under the `website` folder.


![IG Release Publication](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/WorldHealthOrganization/smart-html/main/docs/release-publication.plantuml)


## Contact

For questions or assistance with this workflow, please contact the repository maintainers.

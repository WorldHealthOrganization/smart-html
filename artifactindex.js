async function fetchJSON(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
}

// Custom function to resolve type
function resolveType(canonical, kind) {
    if (canonical.type === 'StructureDefinition') {
        if (kind === 'logical') {
            return 'Logical model';
        }
        if (kind === 'complex-type') {
            return 'Extension (complex)';
        }
        if (kind === 'simple-type') {
            return 'Extension (simple)';
        }
    }
    if (canonical.type === 'CodeSystem') {
        if (canonical.supplements) {
            return 'CodeSystem Supplement';
        }
        return 'CodeSystem';
    }
    // Add more custom logic as needed
    return canonical.type; // default return type if no custom logic applies
}

// Function to initialize DataTable
function initializeDataTable() {
    if (!$.fn.dataTable.isDataTable('#artifacts-table')) {
        $('#artifacts-table').DataTable({
            searching: true,
            destroy: true,
            columns: [
                {
                    data: null,
                    render: (data, type, row) => {
                        const folder = row.folder; // Assuming `folder` is a property in your canonical object
                        const displayTitle = row.title || row.id; // Use title if available, otherwise use id
                        return `<a href="${folder}/${row.type}-${row.id}.html">${displayTitle}</a>`;
                    }
                },
                {
                    data: 'type',
                    render: function(data, type, row) {
                        if (row.resolvedType) {
                            return row.resolvedType;
                        }
                        return data;
                    }
                },
                { data: 'name' },
                { data: 'version' },
            ],
        });
    }
}

// Fetch and load the artifact information
async function loadArtifacts() {
    try {
        const igs = await fetchJSON('igs.json');
        const artifacts = [];
        for (const folder of igs) {
            const canonicalsURL = `${folder}/canonicals.json`;
            const canonicals = await fetchJSON(canonicalsURL);

            for (const canonical of canonicals) {
                canonical.folder = folder; // Add folder to canonical object for later use in rendering the link

                if (canonical.type === 'StructureDefinition' || canonical.type === 'CodeSystem') {
                    const response = await fetch(`${folder}/${canonical.type}-${canonical.id}.json`);
                    const json = await response.json();
                    const kind = json.kind;
                    canonical.resolvedType = resolveType(canonical, kind);
                    canonical.title = json.title || canonical.id; // Add title to canonical, defaulting to id if not available
                } else {
                    canonical.title = canonical.id; // Default title to id if not a StructureDefinition or CodeSystem
                }

                artifacts.push(canonical);
            }
        }
        const artifactsTable = $('#artifacts-table').DataTable();
        artifactsTable.clear().rows.add(artifacts).draw();
    } catch (error) {
        console.error('Error fetching artifact information:', error);
    }
}

// Fetch and load the package information
async function loadPackageInfo() {
    try {
        const igs = await fetchJSON('igs.json');
        const packageInfoContainer = document.getElementById('packageInfo');

        for (const folder of igs) {
            const packageListURL = `${folder}/package-list.json`;
            const packageList = await fetchJSON(packageListURL);

            const title = packageList.title;
            const description = packageList.introduction;

            const ciBuildEntry = packageList.list.find(entry => entry.status === 'ci-build');
            const YYY = ciBuildEntry.path.substring(ciBuildEntry.path.lastIndexOf('/') + 1);

            const packageDiv = document.createElement('div');
            packageDiv.classList.add('col');
            packageDiv.innerHTML = `
                <div class="card full-width">
                    <div class="card-body">
                        <h2 class="card-title">${title}</h2>
                        <p class="card-text">${description}</p>
                    </div>
                    <div class="card-footer d-flex justify-content-end">
                        <a href="./${folder}/index.html" class="btn btn-primary me-3 discrete-button">Implementation Guide</a>
                        <a href="https://github.com/openmrs/${YYY}" class="btn btn-primary me-3 discrete-button">GitHub</a>
                        <a href="./${folder}/history.html" class="btn btn-primary discrete-button">Publication History</a>
                    </div>
                </div>
            `;
            packageInfoContainer.appendChild(packageDiv);
        }
    } catch (error) {
        console.error('Error fetching package information:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.nav-tab');
    const tabContent = document.querySelectorAll('.tab-content > div');

    function changeTab(e) {
        e.preventDefault();
        tabs.forEach(tab => {
            tab.classList.remove('active');
        });
        e.target.classList.add('active');

        const targetContent = e.target.getAttribute('data-target');

        tabContent.forEach(content => {
            if (content.id === targetContent) {
                content.classList.remove('d-none');
            } else {
                content.classList.add('d-none');
            }
        });
    }

    tabs.forEach(tab => {
        tab.addEventListener('click', changeTab);
    });

    initializeDataTable(); // Ensure DataTable is initialized only once

    loadPackageInfo();
    loadArtifacts();
});

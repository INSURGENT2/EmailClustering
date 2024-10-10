function toggleTable(cluster) {
    // Hide all tables first
    const tables = document.querySelectorAll('.email-table-container');
    tables.forEach(table => {
        table.style.display = 'none';
    });

    // Show the clicked cluster's table
    const selectedTable = document.getElementById(`table-cluster-${cluster}`);
    if (selectedTable) {
        selectedTable.style.display = 'block';
    } else {
        console.error(`Table for cluster ${cluster} not found.`);
    }
}

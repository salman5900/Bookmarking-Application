const toggleBtn = document.getElementById('toggleBtn');
const fileList = document.getElementById('fileList');

// Toggle visibility when toggle button is clicked
toggleBtn.addEventListener('click', function (e) {
    e.stopPropagation(); // OK here
    fileList.style.display = (fileList.style.display === 'block') ? 'none' : 'block';
});

// Allow navigation inside fileList
fileList.addEventListener('click', function (e) {
    // Do NOT stop propagation or prevent default
    // Let anchor tags behave normally
    fileList.style.display = 'none'; // Optional: auto-hide when a file is selected
});

// Click outside closes it
document.addEventListener('click', function (e) {
    if (!fileList.contains(e.target) && e.target !== toggleBtn) {
        fileList.style.display = 'none';
    }
});

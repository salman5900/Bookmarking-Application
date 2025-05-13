const toggleBtn = document.getElementById('toggleBtn');
const fileList = document.getElementById('fileList');

// Toggle visibility only on button click
toggleBtn.addEventListener('click', function (e) {
    e.stopPropagation(); // Only stop bubbling to avoid auto-close
    if (fileList.style.display === 'block') {
        fileList.style.display = 'none';
    } else {
        fileList.style.display = 'block';
    }
});

// Clicking on a link should work normally
fileList.addEventListener('click', function (e) {
    // Don't do anything — let the link work
    fileList.style.display = 'none'; // Optional: hide after selection
});

// Close dropdown if clicked outside
document.addEventListener('click', function (e) {
    if (!fileList.contains(e.target) && e.target !== toggleBtn) {
        fileList.style.display = 'none';
    }
});

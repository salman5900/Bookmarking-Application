const toggleBtn = document.getElementById('toggleBtn');
const fileList = document.getElementById('fileList');

// Toggle the list when the button is clicked
toggleBtn.addEventListener('click', function (e) {
    e.stopPropagation(); // Prevent click from bubbling up
    fileList.style.display = (fileList.style.display === 'block') ? 'none' : 'block';
});

// Close the list when clicking anywhere outside
document.addEventListener('click', function (e) {
    if (!fileList.contains(e.target) && e.target !== toggleBtn) {
        fileList.style.display = 'none';
    }
});

// Event listener for hamburger button
document.getElementById('hamburger-btn').addEventListener('click', function() {
  document.getElementById('sidebar').classList.toggle('show-sidebar');
});

// Event listener for exit button
document.getElementById('exit-btn').addEventListener('click', function() {
  document.getElementById('sidebar').classList.remove('show-sidebar');
});

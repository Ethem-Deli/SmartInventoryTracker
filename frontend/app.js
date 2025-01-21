async function loadInventory() {
    const response = await fetch('/api/inventory'); // Replace with your backend route
    const data = await response.json();
    console.log(data);
}

document.addEventListener("DOMContentLoaded", loadInventory);

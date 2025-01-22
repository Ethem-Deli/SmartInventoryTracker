document.addEventListener("DOMContentLoaded", () => {
    async function loadInventory() {
        const response = await fetch('/api/inventory');
        const data = await response.json();
        const container = document.getElementById('inventory-items');
        container.innerHTML = ''; // Clear previous items
        data.forEach(item => {
            const div = document.createElement('div');
            div.classList.add('inventory-item');
            div.innerHTML = `
                <span>${item.product_name}</span>
                <span>Qty: ${item.quantity}</span>
                <span>Price: $${item.price}</span>
            `;
            container.appendChild(div);
        });
    }

    document.getElementById('inventory-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const productName = document.getElementById('product-name').value;
        const quantity = document.getElementById('quantity').value;
        const price = document.getElementById('price').value;
        const batchName = document.getElementById('batch-name').value;

        const response = await fetch('/api/inventory', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_name: productName, quantity, price, batch_name: batchName })
        });

        if (response.ok) {
            alert("Item added successfully!");
            loadInventory();
            document.getElementById('inventory-form').reset();
        } else {
            alert("Failed to add item!");
        }
    });

    loadInventory();
});

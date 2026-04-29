let currentTable = 'knowledge';
let isEditing = false;

const sectionTitles = {
    'knowledge': 'Knowledge Library',
    'business': 'Business Hub',
    'brand_voice': 'Brand Voice'
};

async function checkPassword() {
    const passwordInput = document.getElementById('password-input');
    const password = passwordInput.value.trim();
    
    const response = await fetch('/api/auth', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password })
    });

    if (response.ok) {
        document.getElementById('auth-overlay').style.display = 'none';
        document.getElementById('main-content').style.display = 'flex';
        loadItems();
    } else {
        document.getElementById('auth-error').style.display = 'block';
    }
}

async function loadItems() {
    const response = await fetch(`/api/${currentTable}`);
    const items = await response.json();
    const grid = document.getElementById('items-grid');
    grid.innerHTML = '';

    document.getElementById('current-section-title').innerText = sectionTitles[currentTable];

    items.forEach(item => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <h3>${item.title}</h3>
            <p>${item.content}</p>
            <div class="card-footer">
                <span class="card-date"><i class="ph ph-calendar-blank"></i> ${new Date(item.created_at).toLocaleDateString('vi-VN')}</span>
                <div class="actions">
                    <button class="btn-small" title="Sửa" onclick="editItem(${item.id}, '${item.title.replace(/'/g, "\\'")}', '${item.content.replace(/'/g, "\\'").replace(/\n/g, '\\n')}')">
                        <i class="ph ph-pencil-simple"></i>
                    </button>
                    <button class="btn-small btn-delete" title="Xóa" onclick="deleteItem(${item.id})">
                        <i class="ph ph-trash"></i>
                    </button>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

function switchTab(table, btn) {
    currentTable = table;
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    loadItems();
}

function openModal() {
    isEditing = false;
    document.getElementById('modal-title').innerText = 'Thêm Nội Dung Mới';
    document.getElementById('edit-id').value = '';
    document.getElementById('item-title').value = '';
    document.getElementById('item-content').value = '';
    document.getElementById('modal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('modal').style.display = 'none';
}

function editItem(id, title, content) {
    isEditing = true;
    document.getElementById('modal-title').innerText = 'Chỉnh Sửa Nội Dung';
    document.getElementById('edit-id').value = id;
    document.getElementById('item-title').value = title;
    document.getElementById('item-content').value = content;
    document.getElementById('modal').style.display = 'flex';
}

async function saveItem() {
    const id = document.getElementById('edit-id').value;
    const title = document.getElementById('item-title').value;
    const content = document.getElementById('item-content').value;

    const method = isEditing ? 'PUT' : 'POST';
    const url = isEditing ? `/api/${currentTable}/${id}` : `/api/${currentTable}`;

    const response = await fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, content })
    });

    if (response.ok) {
        closeModal();
        loadItems();
    }
}

async function deleteItem(id) {
    if (confirm('Bạn có chắc chắn muốn xóa mục này?')) {
        const response = await fetch(`/api/${currentTable}/${id}`, {
            method: 'DELETE'
        });
        if (response.ok) {
            loadItems();
        }
    }
}

// Enter key for password
document.getElementById('password-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') checkPassword();
});

let currentTable = 'dashboard';
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
        document.getElementById('main-app').style.display = 'grid'; // App uses grid layout
        // Default to dashboard
        document.querySelector('[data-nav="dashboard"]').click();
        initBrainAnimation();
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
        card.className = 'item-card';
        card.innerHTML = `
            <h3>${item.title}</h3>
            <p>${item.content}</p>
            <div class="item-footer">
                <span class="item-date"><i class="ph ph-calendar-blank"></i> ${new Date(item.created_at).toLocaleDateString('vi-VN')}</span>
                <div class="item-actions">
                    <button class="action-btn" title="Sửa" onclick="editItem(${item.id}, '${item.title.replace(/'/g, "\\'")}', '${item.content.replace(/'/g, "\\'").replace(/\n/g, '\\n')}')">
                        <i class="ph ph-pencil-simple"></i>
                    </button>
                    <button class="action-btn delete" title="Xóa" onclick="deleteItem(${item.id})">
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
    
    // Update active state on nav links
    document.querySelectorAll('.nav-link[data-nav]').forEach(b => b.classList.remove('active'));
    if (btn) {
        btn.classList.add('active');
    } else {
        const activeNav = document.querySelector(`[data-nav="${table}"]`);
        if(activeNav) activeNav.classList.add('active');
    }

    const dashboardView = document.getElementById('dashboard-view');
    const itemsContainer = document.getElementById('items-container');

    if (table === 'dashboard') {
        dashboardView.style.display = 'block';
        itemsContainer.style.display = 'none';
    } else {
        dashboardView.style.display = 'none';
        itemsContainer.style.display = 'block';
        loadItems();
    }
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

function initBrainAnimation() {
    const stage = document.getElementById('brain-stage');
    if (stage && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
        stage.addEventListener('mousemove', (e) => {
            const rect = stage.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const rx = ((y / rect.height) - 0.5) * -10;
            const ry = ((x / rect.width) - 0.5) * 12;
            stage.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
        });

        stage.addEventListener('mouseleave', () => {
            stage.style.transform = 'rotateX(0deg) rotateY(0deg)';
        });
    }
}

// Enter key for password
document.getElementById('password-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') checkPassword();
});

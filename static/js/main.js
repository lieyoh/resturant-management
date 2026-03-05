// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
  // Initialize page switcher to first page
  showPage('home');
});

// Page switcher
function showPage(page) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  const el = document.getElementById('page-' + page);
  if (el) el.classList.add('active');
}

// Tier filter for menu page
function filterTier(tier) {
  const sections = document.querySelectorAll('.menu-section');
  sections.forEach(sec => {
    sec.style.display = (tier === 'all' || sec.id.includes(tier)) ? 'grid' : 'none';
  });

  // Highlight tabs
  const tabClasses = ['tab-active-green', 'tab-active-yellow', 'tab-active-red', 'tab-active-white'];
  document.querySelectorAll('#filterTabs button').forEach(btn => btn.classList.remove(...tabClasses));

  const tabMap = {
    normal: 'tab-normal',
    high: 'tab-high',
    hard: 'tab-hard',
    all: 'tab-all'
  };

  const tabId = tabMap[tier] || 'tab-all';
  const tabEl = document.getElementById(tabId);
  if (tabEl) {
    const colorClass = tier === 'normal' ? 'tab-active-green' :
                       tier === 'high'   ? 'tab-active-yellow' :
                       tier === 'hard'   ? 'tab-active-red' : 
                                           'tab-active-white';
    tabEl.classList.add(colorClass);
  }
}
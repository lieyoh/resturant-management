document.querySelectorAll('input[name="table_id"]').forEach(radio => {
    radio.addEventListener('change', (e) => {
      
      document.getElementById('selected_table_input').value = e.target.value;
      
      const btn = document.getElementById('submit_btn');
      btn.disabled = false;
      btn.classList.remove('bg-gray-800', 'text-gray-500');
      btn.classList.add('bg-yellow-500', 'text-black', 'hover:bg-yellow-400');
      btn.innerText = "Confirm Table " + e.target.value + " & Continue";
    });
  });
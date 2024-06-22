document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.update-task').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskId = this.closest('li').getAttribute('data-id');
            fetch(`/update/${taskId}`, {
                method: 'POST',
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    this.nextElementSibling.classList.toggle('completed');
                }
            });
        });
    });

    document.querySelectorAll('.delete-task').forEach(button => {
        button.addEventListener('click', function() {
            const taskId = this.closest('li').getAttribute('data-id');
            fetch(`/delete/${taskId}`, {
                method: 'POST',
            }).then(response => response.json()).then(data => {
                if (data.success) {
                    this.closest('li').remove();
                }
            });
        });
    });
});

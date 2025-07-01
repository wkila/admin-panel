document.addEventListener('DOMContentLoaded', function() {
    // Пример: слушаем отправку формы
    document.querySelectorAll('.forms_display').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            let formData = new FormData(form);
            formData.append('action', form.id);  // например, action = id формы

            fetch("{% url 'api_products' %}", {
                method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                console.log('Ответ сервера:', data);
                // Здесь можно обновить страницу, показать результат и т.д.
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
        });
    });
});

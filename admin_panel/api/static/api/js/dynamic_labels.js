const select = document.getElementById('product-select');
const container = document.querySelectorAll(".forms_display")

container.forEach(element => {
    element.style.display = 'none'
})

select.addEventListener('change', function() {
    const selectedValue = this.value;
    container.forEach(element => {
        element.style.display = 'none'
    })
    container.forEach(element => {
        if (element.id === selectedValue) {
            element.style.display = 'block'
        }
    })

});
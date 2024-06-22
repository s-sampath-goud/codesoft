document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('search');
    searchInput.addEventListener('input', () => {
        const query = searchInput.value;
        fetch(`/search?query=${query}`)
            .then(response => response.json())
            .then(data => {
                const contactList = document.getElementById('contact-list');
                contactList.innerHTML = '';
                data.forEach(contact => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <span>${contact.name} - ${contact.phone}</span>
                        <a href="/update/${data.indexOf(contact)}">Edit</a>
                        <form action="/delete/${data.indexOf(contact)}" method="post" style="display:inline;">
                            <button type="submit">Delete</button>
                        </form>
                    `;
                    contactList.appendChild(li);
                });
            });
    });
});

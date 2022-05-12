function deleteItem(element) {
    
    if(window.confirm("Wollen Sie dieses Item wirklich löschen?"))
    {
        element.parentElement.submit(this);
    }
}
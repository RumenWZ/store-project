const myBtn = document.getElementsByClassName('delete-cart-product')

for(let i=0; i<myBtn.length ; i++){
    myBtn[i].addEventListener('click', () => {
        const productId = myBtn[i].dataset.product
        console.log(productId)

        giveProductId(productId)
    })
}


function giveProductId(productId) {
    const url = '/cart/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({"productId": productId}),
    })
    .then((response) => {
            return response.json()
        })
    .then((data) => {
            console.log('data:', data)
        })
}
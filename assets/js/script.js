let toggle_btn = document.querySelector("#profile .details .right a.edit");
let close_btn = document.querySelector("#show_hide .close img");
let toggle_editor = document.querySelector("#show_hide");

const toggle_class = () => {
    toggle_editor.classList.toggle("hide");
};

if (toggle_btn) {
    console.log(toggle_btn);
    toggle_btn.addEventListener("click", (e) => {
        e.preventDefault();
        toggle_class();
    });
}
if (close_btn) {
    close_btn.addEventListener("click", (e) => {
        toggle_class();
    });
}

$(document).on("submit", "form.checkout", (e) => {
    e.preventDefault();
    var $this = $("form.checkout");
    let form_data = document.querySelector("form.checkout");

    var url = form_data.getAttribute("action");
    var method = form_data.getAttribute("method");

    $.ajax({
        type: method,
        url: url,
        dataType: "json",
        data: new FormData(form_data),
        processData: false,
        contentType: false,
        cache: false,

        success: (data) => {
            console.log(data);
            Swal.fire({
                title: "Confirm Order",
                text: "Confirm order and pay now",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, pay now!",
            }).then((result) => {
                if (result.isConfirmed) {
                    Swal.fire(
                        "Confirmed!",
                        "Your order has been  confirmed",
                        "success"
                    ).then((result) => {
                        if (result.isConfirmed) {
                            window.location.assign(data.redirect);
                        }
                    });
                }
            });
        },
        error: (error) => {
            console.log(error);
        },
    });
});

// toggle users cart functionality for admin dashboard

let cart = document.querySelector("#manage-users > #cart-hide-show");
let cart_close_btn = document.querySelector(
    "#manage-users > #cart-hide-show .close-btn img"
);
let cart_show_btn = document.querySelectorAll(
    "#manage-users > .content > ul.left li .actions img.cart"
);

cart_show_btn.forEach((btn) => {
    btn.addEventListener("click", (e) => {
        let cart_id = btn.getAttribute("data-cart-id");
        let ul = cart.querySelector("#cart-attach");
        let user_name = cart.querySelector('h1 > a')
        user_name.textContent = ''
        let html = ''
        $(ul).html(html);

        $.ajax({
            type: "get",
            url: `/admin/cart/${cart_id}/`,
            success: function (data) {
                user_name.innerText = data.customer.name

                if (data.items.length == 0) {
                    console.log("not found");
                    let h1 = document.createElement("h1");
                    h1.innerText = "Cart is empty";
                    h1.classList.add('empty-cart')
                    $(ul).html(h1);
                } else {
                    data.items.forEach((item) => {
                        html += `
                    <li>
                        <div class="left">
                            <a href="/products/${item.product.id}/">
                                <img loading='lazy' src="${item.product.image}" alt="">
                            </a>
                        </div>
                        <div class="right">
                            <h4>${item.product.name}</h4>
                            <h4>₹${item.product.price}</h4>
                        </div>  
                    </li>
                        `;
                        $(ul).html(html);
                    });
                }
            },
            error: function (error) {
                console.log(error);
            },
        });

        html = "";
        cart.classList.remove("toggle");

        var rect = btn.getBoundingClientRect(),
            // scrollLeft =
            //     window.pageXOffset || document.documentElement.scrollLeft,
            scrollTop =
                window.pageYOffset || document.documentElement.scrollTop;
        cart.style.top = scrollTop + 100 + "px";

        // to close the cart tab
        cart_close_btn.addEventListener("click", (e) => {
            cart.classList.add("toggle");
        });
    });
});


// toggle cart from user profile page (admin only)

let cart_toggle_btn = document.querySelector('#view-user-profile > .top .right > img')
let cart_2 = document.querySelector('#view-user-profile > #cart-hide-show')
let cart_hide_btn = cart_2.querySelector('.close-btn img ')

cart_toggle_btn.addEventListener('click', (e) => {
    cart_2.classList.remove('toggle')
})
cart_hide_btn.addEventListener('click', (e) =>{
    cart_2.classList.add('toggle')
})
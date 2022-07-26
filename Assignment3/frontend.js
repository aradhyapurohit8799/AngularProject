const body = document.querySelector("body")
const totalsales = document.querySelector('#value1');
const uniquecust = document.querySelector('#value2');
const avgamnt = document.querySelector('#value3');
const table = document.querySelector('.value4');
const dailysales = document.querySelector('.Tab-head');
const loginForm = document.querySelector('form');
const redirect = document.querySelector('.form-wrap');


loginForm.addEventListener('submit', e => {

    e.preventDefault();

    const username = loginForm.username.value.trim();
    const password = loginForm.password.value.trim();
    loginForm.reset();

    authenticate(username, password).then(Response => {
        window.localStorage.setItem('mytoken', Response.access_token);

    })

    if (window.localStorage.getItem('mytoken') !== "undefined") {
        const login = document.getElementById("container-login");
        login.classList.add("d-none");

        const indexHeader = document.getElementById("header");
        indexHeader.classList.remove("d-none");

        const indexContent = document.getElementById("main");
        indexContent.classList.remove("d-none");

        getDailySales(window.localStorage.getItem('mytoken'))
            .then(Response => {
                console.log(Response.Items);
                dailysales.innerHTML = "<th>userid &nbsp &nbsp</th> <th>product id &nbsp &nbsp</th> <th>Sales Amount &nbsp &nbsp</th> <th>Sales Date &nbsp &nbsp</th> "

                for (let i = 0; i < Response.Items.length; i++) {
                    console.log(Response.Items[i]);
                    table.innerHTML += `
                    <tr class="P1">
                        <td>${Response.Items[i].userid}</td>
                        <td>${Response.Items[i].product_id}</td>
                        <td>${Response.Items[i].sales_amount}</td>
                        <td> ${Response.Items[i].sales_date}</td>
                    </tr>
                    `
                }




            })
            .catch(err => console.log(err));

        getTotalSales(window.localStorage.getItem('mytoken'))
            .then(Response => {
                console.log(Response["Total Sales"]);
                if (Response["Total Sales"] !== 0)
                    totalsales.innerHTML = `&dollar; ${Response["Total Sales"]}`
            })
            .catch(err => console.log(err))

        getUniqueCust(window.localStorage.getItem('mytoken'))
            .then(Response => {
                console.log(Response["unique cutomers"]);
                if (Response["unique cutomers"] !== 0)
                    uniquecust.innerHTML = `${Response["unique cutomers"]}`
            })
            .catch(err => console.log(err))

        getAverageSales(window.localStorage.getItem('mytoken'))
            .then(Response => {
                console.log(Response["Average Sales"]);
                if (Response["Average Sales"] !== (0 / 0))
                    avgamnt.innerHTML = `&dollar; ${Response["Average Sales"]}`;

            })
            .catch(err => console.log(err))

    }
    else {
        redirect.innerHTML = `
        <h1> Invalid Credentials ! </h1>
        <p> Please refresh the page and try again </p>
        `;
    }
});
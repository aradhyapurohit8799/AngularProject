// post: register user
const registration = async () => { //async

    const base = 'http://127.0.0.1:5000/register';

    const response = await fetch(base, //await
        {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ id: 123, firstname: "Aradhya", lastname: "Purohit", username: "AP8799", password: "asdf" })
        });
    const data = await response.json(); //await

    // return data;
    return data;
};
registration()
    .then(response => response.message)
    .then(json => console.log(json))
    .catch(err => console.log("Error has encountered", err))


// post: authenticate user

const authenticate = async (username, password) => { //async

    const base = 'http://127.0.0.1:5000/auth';
    username = username;
    password = password;

    const response = await fetch(base, { //await
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username, password: password })
    });
    const data = await response.json(); //await

    return data;

};


//GET Daily Sales Data

const getDailySales = async (token) => {

    const base = 'http://127.0.0.1:5000/total sales/3';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};


// GET Total Sales Data

const getTotalSales = async (token) => {

    const base = 'http://127.0.0.1:5000/Total Sales Value';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};


// GET Unique Customer Data

const getUniqueCust = async (token) => {

    const base = 'http://127.0.0.1:5000/Unique';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};


// GET Average Sales Data

const getAverageSales = async (token) => {

    const base = 'http://127.0.0.1:5000/AVG';

    const response = await fetch(base, {
        method: 'GET',
        headers: {
            "Authorization": `JWT ${token}`
        }
    });

    const data = await response.json();

    return data;

};



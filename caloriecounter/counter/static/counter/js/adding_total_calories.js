 //Had the help of copilot with this code to write a javascript function to get the total amount of calories from the backend and display it on the page when the button is clicked.
 //The JavaScript code here is an IIFE, which means we are wrapping the code in a private function, which will run as soon as it is defined. This prevents JS naming conflicts.
 (() => {
    // Get the button by its ID
    const btn = document.getElementById('show-total-btn');
    // if button is not found, exit the function
    if (!btn) return;

    // We add an event listener to the button to wait for the user to click it.
    btn.addEventListener('click', function() {
        // The listener function fetches data from the URL stored in the button's data-url attribute. If no URL is found, it logs an error message.
        const url = btn.dataset.url;
        if (!url) {
            console.error('No URL found for total_calories');
            return;
        }
        //fetch() returns a Promise, which is why we use .then() and .catch(). It gets the data from the backend using the fetch API, which is a way to get HTTP requests in JavaScript. We go to /counter/total_calories/ to go to the view and it will return the total calories in JSON format.
        fetch(url)
            //This processes the response from the fetch call, checking if it was successful and parsing it as JSON.
            .then(response => {
                if (!response.ok) throw new Error('Network response was not ok');
                return response.json();
            })
            //Once we check that the response is ok, we take the data and update the inner HTML of the element with the ID total-result to display the total calories.
            .then(data => {
                const target = document.getElementById('total-result');
                if (target) target.innerHTML = `<p>Total Calories: ${data.total}</p>`;
            })
            //This handles errors that may occur during the fetch operation, logging them to the console for debugging.
            .catch(err => {
                console.error('Error fetching total calories:', err);
            });
    });
})();

document.addEventListener("DOMContentLoaded", function () {
    // Get references to the filter elements
    var venueTypeFilter = document.getElementById("venue-type");
    var locationFilter = document.getElementById("location");
    var numPeopleFilter = document.getElementById("num-people");

    // Get references to the hotel list and hotels
    var hotelList = document.querySelector(".hotel-list");
    var hotels = hotelList.getElementsByClassName("hotel");

    // Attach event listeners to the filters
    venueTypeFilter.addEventListener("change", updateFilters);
    locationFilter.addEventListener("change", updateFilters);
    numPeopleFilter.addEventListener("input", updateFilters);

    // Function to update the filters and hide/show hotels accordingly
    function updateFilters() {
        var selectedVenueType = venueTypeFilter.value;
        var selectedLocation = locationFilter.value;
        var selectedNumPeople = numPeopleFilter.value;

        // Loop through all hotels and check if they match the filters
        for (var i = 0; i < hotels.length; i++) {
            var hotel = hotels[i];
            var venueType = hotel.querySelector("h2").textContent.toLowerCase();
            var location = hotel.querySelector("p:nth-child(2)").textContent.toLowerCase();
            var numPeople = parseInt(hotel.querySelector("p:nth-child(3)").textContent.split(":")[1]);

            // Check if the hotel matches the selected filters
            var venueTypeMatch = selectedVenueType === "all" || venueType.includes(selectedVenueType.toLowerCase());
            var locationMatch = selectedLocation === "all" || location.includes(selectedLocation.toLowerCase());
            var numPeopleMatch = isNaN(selectedNumPeople) || numPeople >= selectedNumPeople;

            // Show/hide the hotel based on filter matches
            if (venueTypeMatch && locationMatch && numPeopleMatch) {
                hotel.style.display = "flex";
            } else {
                hotel.style.display = "none";
            }
        }
    }
});

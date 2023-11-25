function submitForm() {
    var targetWeight = document.getElementById("target_weight").value;
    
    var excludeWeights = document.querySelectorAll('input[name="excludeWeights"]:not(:checked)');
    var apiUrl = window.location + "/" + encodeURIComponent(targetWeight);
    if (excludeWeights.length > 0) {
      var excludeWeightsArray = Array.from(excludeWeights).map(function (checkbox) {
        return 'exclude_number=' + encodeURIComponent(checkbox.value);
      });
  
      apiUrl += '?' + excludeWeightsArray.join('&');
    }
    console.log("API URL: ", apiUrl);
  
    // Submit to API
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
  
        var resultContainer = document.getElementById("resultContainer");
  
        // Clear previous results
        resultContainer.innerHTML = '';
  
        // Iterate over properties of the JSON object and display the result
        var plates = data['plate_calculation']['plates']
        for (var number in plates) {
          if (plates.hasOwnProperty(number)) {
            var count = plates[number];
  
            // Create a new paragraph element for each number and count
            var paragraph = document.createElement("p");
            paragraph.textContent = number + " lbs x " + count;
  
            // Append the paragraph to the result container
            resultContainer.appendChild(paragraph);
          }
        }
      })
      .catch(error => {
        console.error('Error:', error);
        // Optionally handle errors (no thanks)
      });
  }
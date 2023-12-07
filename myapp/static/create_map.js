let map, infoWindow, instructionLabel, currentMarker;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 38.033554, lng: 78.507980 },
    zoom: 10,
    restriction: {
      latLngBounds: {
        north: 38.039644,
        south: 38.02767194537799,
        west: -78.52015995187004,
        east: -78.49957854027083,
      },
    },
  });

 
  instructionLabel = new google.maps.InfoWindow({
    content: "Click on the map to mark the location",
  });

  
  google.maps.event.addListenerOnce(map, "idle", function () {
    instructionLabel.setPosition(map.getCenter());
    instructionLabel.open(map);
  });

  
  google.maps.event.addListener(map, "click", function (event) {
    placeMarker(event.latLng);
  });
}

function placeMarker(location) {
  
  if (currentMarker) {
    currentMarker.setMap(null);
  }

 
  const marker = new google.maps.Marker({
    position: location,
    map: map,
    icon: {
      path: google.maps.SymbolPath.CIRCLE,
      scale: 10, 
      fillOpacity: 1,
      strokeWeight: 2,
      fillColor: "#5384ED",
      strokeColor: "#ffffff",
    },
  });

  infoWindow = new google.maps.InfoWindow({
    content:
      "You marked the location at " +
      location.lat().toFixed(6) +
      ", " +
      location.lng().toFixed(6),
  });

  infoWindow.open(map, marker);


  instructionLabel.close();


  currentMarker = marker;
  document.getElementById("latitudeInput").value = location.lat();
  document.getElementById("longitudeInput").value = location.lng();
}

window.onload = getLocation;

function getLocation() {
  infoWindow = new google.maps.InfoWindow();

  if (navigator.geolocation) {
    target = new google.maps.LatLng(38.027500, -78.515320);

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };

        var marker = new google.maps.Marker({
          position: pos,
          map: map,
          icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 30,
            fillOpacity: 1,
            strokeWeight: 2,
            fillColor: "#5384ED",
            strokeColor: "#ffffff",
          },
        });

        instructionLabel.close();

        currentMarker = marker;
      },
      () => {
        handleLocationError(true, infoWindow, map.getCenter());
      }
    );
  } else {

    handleLocationError(false, infoWindow, map.getCenter());
  }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}

initMap();

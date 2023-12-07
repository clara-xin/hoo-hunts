let map, infoWindow;


async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 38.033554, lng: 78.507980 },
    zoom: 10,
    restriction: { latLngBounds: { north: 38.039644, south: 38.02767194537799, west: -78.52015995187004, east: -78.49957854027083 } }
  });

}


window.onload = getLocation;

// function getLocation() {
// infoWindow = new google.maps.InfoWindow();

// const locationButton = document.createElement("button");
//   locationButton.style.backgroundColor = "#448FDA";
//   locationButton.style.borderRadius = "3px";
//   locationButton.style.color = "rgb(25,25,25)";
//   locationButton.style.fontFamily = "Roboto,Arial,sans-serif";
//   locationButton.style.fontSize = "16px";
//   locationButton.style.lineHeight = "38px";
//   locationButton.style.margin = "8px 0 22px";
//   locationButton.style.padding = "0 5px";
//   locationButton.style.textAlign = "center";


//   locationButton.textContent = "Check Current Location";
//   locationButton.classList.add("custom-map-control-button");
//   map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
//   locationButton.addEventListener("click", () => {

//   // Try HTML5 geolocation.
//   if (navigator.geolocation) {
//     target = new google.maps.LatLng(38.027500, -78.515320);

//     // const targetCircle = new google.maps.Circle({
//     //   map,
//     //   center: target,
//     //   radius: 30,
//     // });

//     navigator.geolocation.getCurrentPosition(
//       (position) => {
//         const pos = {
//           lat: position.coords.latitude,
//           lng: position.coords.longitude,
//         };

//           var marker = new google.maps.Marker({
//             position: pos,
//             map: map,
//             icon: {
//               path: google.maps.SymbolPath.CIRCLE,
//               scale: 30,
//               fillOpacity: 1,
//               strokeWeight: 2,
//               fillColor: '#5384ED',
//               strokeColor: '#ffffff',
//             },
//           });

//         // const marker = google.maps.geometry.poly.containsLocation(pos, targetCircle)
//         // ? new google.maps.Marker({
//         //   position: pos,
//         //   map: map,
//         //   icon: {
//         //     path: google.maps.SymbolPath.CIRCLE,
//         //     scale: 10,
//         //     fillOpacity: 1,
//         //     strokeWeight: 2,
//         //     fillColor: '#5384ED',
//         //     strokeColor: '#ffffff',
//         //   },
//         // })
//         // : "You have not found the spot.";

//         // if (targetCircle.containsLocation(pos, targetCircle)) {
//         //   var marker = new google.maps.Marker({
//         //     position: pos,
//         //     map: map,
//         //     icon: {
//         //       path: google.maps.SymbolPath.CIRCLE,
//         //       scale: 10,
//         //       fillOpacity: 1,
//         //       strokeWeight: 2,
//         //       fillColor: '#5384ED',
//         //       strokeColor: '#ffffff',
//         //     },
//         //   });
//         // } else {
//         //   var marker = new google.maps.Marker({
//         //     position: pos,
//         //     map: map,
//         //     icon: {
//         //       path: google.maps.SymbolPath.CIRCLE,
//         //       scale: 30,
//         //       fillOpacity: 1,
//         //       strokeWeight: 2,
//         //       fillColor: '#5384ED',
//         //       strokeColor: '#ffffff',
//         //     },
//         //   });
//         // }
//       },
//       () => {
//         handleLocationError(true, infoWindow, map.getCenter());
//       },
//     );

//   } else {
//     // Browser doesn't support Geolocation
//     handleLocationError(false, infoWindow, map.getCenter());
//   }
//   });
// }

// function handleLocationError(browserHasGeolocation, infoWindow, pos) {
//   infoWindow.setPosition(pos);
//   infoWindow.setContent(
//     browserHasGeolocation
//       ? "Error: The Geolocation service failed."
//       : "Error: Your browser doesn't support geolocation.",
//   );
//   infoWindow.open(map);
// }

initMap();
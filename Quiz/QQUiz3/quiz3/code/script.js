window.onload = () => {
     let places = staticLoadPlaces();
     renderPlaces(places);//for lication lat: <your-latitude>,lng: <your-longitude>,
};
// run function renderplace  ⬆


function staticLoadPlaces() {
    return [
        {
            name: 'MyModel',
            location: {
                lat: <your-latitude>,
                lng: <your-longitude>,
            }
        },
    ];
}

function renderPlaces(places) {
    let scene = document.querySelector('a-scene');//find a-scene in html

    places.forEach((place) => {
        let latitude = place.location.lat;//copy location
        let longitude = place.location.lng;

        let model = document.createElement('a-entity');//make new entity
        model.setAttribute('gps-entity-place', `latitude: ${latitude}; longitude: ${longitude};`);//make gps
        model.setAttribute('gltf-model', './assets/MyModel/scene.gltf');//add 3d mode in view
        model.setAttribute('rotation', '0 90 0');//rorate
        model.setAttribute('animation-mixer', '');//play animation
        model.setAttribute('scale', '1 1 1');//zoom to 0.5 but i change to 1

        model.addEventListener('loaded', () => {
            window.dispatchEvent(new CustomEvent('gps-entity-place-loaded'))//load to Listener
        });

        scene.appendChild(model);
    });
}
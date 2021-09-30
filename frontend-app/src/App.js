import React, { useState } from 'react';
import SockJsClient from 'react-stomp';
import GoogleMapReact from 'google-map-react';
import Marker from './marker.js';

const SOCKET_URL = 'http://localhost:8080/data';
const App = () => {
 const defaultProps = {
    center: {
      lat: 59.99835602,
      lng: 18.01502627
    },
    zoom: 5
  };
  const [lat, setLatitutude] = useState(58)
  const [lon, setLongitude] = useState(17)
  const [secondLat, setSecondLatitude] = useState(57)
  const [secondLon, setSecondLongitude] = useState(11)

  let onConnected = () => {
    console.log("Connected!!")
  }

  let onMessageReceived = (msg) => {
    if(msg.key === "ABC") {
      let value = JSON.parse(msg.value)
      setLatitutude(value.lat);
      setLongitude(value.lon)
    } else if(msg.key === "XYZ") {
      let value = JSON.parse(msg.value)
      setSecondLatitude(value.lat);
      setSecondLongitude(value.lon)
    }
  }

  return (
    <div>
      <SockJsClient
        url={SOCKET_URL}
        topics={['/topic']}
        onConnect={onConnected}
        onMessage={msg => onMessageReceived(msg)}
        debug={false}
      />
 <div style={{ height: '100vh', width: '100%' }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: process.env.REACT_APP_GOOGLE_MAPS_API_KEY }}
        defaultCenter={defaultProps.center}
        defaultZoom={defaultProps.zoom}
      >
      <Marker
            lat={lat}
            lng={lon}
            name="ABC"
          />
      <Marker
            lat={secondLat}
            lng={secondLon}
            name="XYZ"
          />
      </GoogleMapReact>
    </div>
    </div>
  );
}

export default App;

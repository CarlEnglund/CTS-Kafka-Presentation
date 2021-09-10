import React from 'react';
import './marker.css';

const Marker = (props: any) => {
    const { name} = props;
    return (
      <div className="marker">
          <p className="planeText">{name}</p>
      </div>
    );
  };

  export default Marker;
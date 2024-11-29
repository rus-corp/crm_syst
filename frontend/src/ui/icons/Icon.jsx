import React from 'react';


export default function Icon({ isActive, IconComponent}) {
  return(
    <IconComponent style={{fill: isActive ? '#3F8CFF' : '#7D8592'}} />
  );
}
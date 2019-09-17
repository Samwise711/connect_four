import React from 'react';
import './Cell.css';

const Cell = ({ value, columnIndex, play }) => {
 let color = 'white';
 if (value === 1) {
   color = 'black';
 } else if (value === 2) {
   color = 'red';
 }

 return (
   <td>
     <div className="cell" onClick={() => {play(columnIndex)}}>
       <div className={color}></div>
     </div>
   </td>
 );
};

export default Cell;

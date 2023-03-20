import React, {useState} from "react";
import './Gallery1.css'
import Img3 from '../Images/kitchen6.jpeg'
import Img2 from '../Images/dinning6.jpeg'
import Img1 from '../Images/bd6.jpeg'
import Img5 from '../Images/br6.jpeg'
import Img4 from '../Images/laundry6.jpeg'
import Img6 from '../Images/gym6.jpeg'



const Gallery6 = () => {

    let data = [
        {
            id: 1,
            imgsrc: Img1,
        },
        {
            id: 2,
            imgsrc: Img2,
        },
        {
            id: 3,
            imgsrc: Img3,
        },
        {
            id: 4,
            imgsrc: Img4,
        },
        {
            id: 5,
            imgsrc: Img5,
        },
        {
            id: 6,
            imgsrc: Img6,
        }

    ]
    const[model, setModel] = useState(false)
    const[tempimgsrc, setTempimgsrc] = useState('');
    const getImg = (imgsrc) =>{
        setTempimgsrc(imgsrc);
        setModel(true);
    }
   return(
   <>
    
   <div className= {model? "model open" : "model"}>
    <img src={tempimgsrc}  alt=""/>
   </div>
   <div className="gallery">
     {data.map((item, index) => {
        return (
           <div className="pics" key={index} onClick={() => getImg(item.imgsrc)}>
            <img src={item.imgsrc} alt="" style={{width: '100%'}}/>
           </div>
        )
     })}
   </div>
     
   </>
   )
}

export default Gallery6


import React, { useState } from 'react'
import Modal from 'react-modal'
import { AiOutlineClose} from 'react-icons/ai';
export default function Insp_H({number, name, data}) {
    const [isOpen, setIsOpen] = useState(false);
    const customStyles = {
        overlay: {
           backgroundColor: 'rgba(0, 0, 0, 0.6)'
        },
        content: {
           top: '50%',
           left: '50%',
           right: 'auto',
           bottom: 'auto',
           marginRight: '-50%',
           transform: 'translate(-50%, -50%)',
           backgroundColor: 'rgba(218, 226, 234, 0.95)'
        }
  
     }
    return (
        <>
        <div className="h-full w-3/12">
             <div className='flex items-center justify-center  h-full' role="button" onClick={() => setIsOpen(true)}>
                <div className="flex bg-white flex-col w-64 items-center rounded-2xl mx-6 mt-10">
                    <span className=" mb-8 mt-3 font-semibold">{number}</span>
                    <span className="mb-8">{name}</span>
                    
                    <span className="mb-3">{data}</span> 
                </div>
             </div>
             <Modal ariaHideApp={false} isOpen={isOpen} onRequestClose={() => setIsOpen(true)} style={customStyles}>
                <div className='bg-modal'>
                    <button className="mr-4 text-2xl" onClick={() => setIsOpen(false)}><AiOutlineClose /></button>
                    <div className='flex  items-center justify-center'>
                        <h2>Relatório</h2>
                        <h3>{name}</h3>
                        <p>{data}</p>
                    </div>
                </div>

             </Modal>
          </div>

        </>
       
    );
}



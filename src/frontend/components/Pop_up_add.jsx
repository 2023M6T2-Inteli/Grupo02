import React, { useState, useEffect } from 'react'
import Modal from 'react-modal'
import { AiOutlineClose, AiOutlineMinus, AiFillDelete } from 'react-icons/ai';
import { Plus } from "react-bootstrap-icons";
import Canvas from './Canvas'


const Pop_up_add = () => {
   const [isOpen, setIsOpen] = useState(false)
   const [selectedImage, setSelectedImage] = useState(null);
   const [imageUrl, setImageUrl] = useState(null);
   const [fileInputDisplay, setFileInputDisplay] = useState(null);
   useEffect(() => {
      if (selectedImage) {
         console.log(selectedImage)
         setFileInputDisplay('none')
         setImageUrl(URL.createObjectURL(selectedImage));
      }
   }, [selectedImage]);
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
         <div>
            <div role="button" onClick={() => setIsOpen(true)}><Plus /></div>
            <Modal ariaHideApp={false} isOpen={isOpen} onRequestClose={() => setIsOpen(true)} style={customStyles}>
               <div className='bg-modal'>
                  <div className="flex justify-between ">
                     <h1 className="ml-4 font-medium text-blue-600 text-3xl font-sans">Crie sua rota</h1>
                     <button className="mr-4 text-2xl" onClick={() => setIsOpen(false)}><AiOutlineClose /></button>
                  </div>
                  <div className="flex justify-between items-center mr-4 ml-4 h-full">
                     <div className='flex flex-col w-9/12 H-90 '>
                        <div className="flex justify-between items-center mb-10">
                           <div>
                              {/* <label for="small-input" className="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Nome da Rota</label> */}
                              <input placeholder='Nome da Rota' type="text" id="small-input" className="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                           </div>
                           <div>
                              {/* <label for="small-input" className="block mb-2 text-sm font-medium text-gray-900 dark:text-black">Descrição da para a rota</label> */}
                              <input placeholder='Descrição da rota' type="text" id="small-input" className="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 sm:text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
                           </div>
                        </div>
                        <div className="flex flex-col justify-center w-full h-full" style={{ display: fileInputDisplay }}>
                           <p className="mb-2">Envie, abaixo, a rota do robô para o espaço confinado.</p>
                           <label for="dropzone-file" className="flex flex-col items-center justify-center w-full h-full border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600" >
                              <div className="flex h-full flex-col items-center justify-center pt-5 pb-6">
                                 <svg aria-hidden="true" className="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
                                 <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Clique para fazer o upload da imagem</span> ou arraste e solte-a aqui</p>
                                 <p className="text-xs text-gray-500 dark:text-gray-400">SVG, PNG ou JPG (MAX. 800x400px)</p>
                              </div>
                           </label>
                           <input
                              accept="image/"
                              type="file"
                              id="dropzone-file"
                              // className="hidden"
                              style={{ display: 'none' }}
                              onChange={e => setSelectedImage(e.target.files[0])}
                           />
                        </div>
                        {/* <div style={{ width: '25px', height: '25px' }}> */}
                        {imageUrl && selectedImage && (<Canvas backgroundImageSrc={imageUrl} alt={selectedImage.name} />)
                        }
                        {/* </div> */}
                        <div className='pb-10'></div>
                        <button
                           className='W-max-21 bg-azul rounded-2x1 h-9 text-white'
                           onClick={() => { setSelectedImage(null); setFileInputDisplay(null) }}>
                           Mudar
                        </button>
                     </div>
                     <div className="w-3/12 flex flex-col items-center">
                        <div className="bg-azul cursor-pointer mb-8 flex flex-col rounded-2xl text-white items-center gap-y-1.5 p-8 H-max-15 W-max-20">
                           <div className='circulo'></div>
                           <span>Inserir nó</span>
                        </div>
                        <div className="bg-azul cursor-pointer mb-8 flex flex-col rounded-2xl text-white items-center gap-y-1.5 p-8 H-max-15 W-max-20">
                           <div className="text-4xl"><AiOutlineMinus /></div>
                           <span>Inserir aresta</span>
                        </div>
                        <div className="cursor-pointer bg-azul mb-8 flex flex-col rounded-2xl text-white items-center gap-y-1.5 p-8 H-max-15 W-max-20">
                           <div><AiFillDelete /></div>
                           <span>Deletar</span>
                        </div>
                        <button onClick={() => setIsOpen(false)} className='W-max-20 bg-azul rounded-2xl h-9 text-white'>save</button>
                     </div>
                  </div>
               </div>

            </Modal>
         </div>
      </>
   )
}
export default Pop_up_add
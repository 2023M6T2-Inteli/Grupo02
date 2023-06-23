import Pop_up_edit from "./Pop_up_edit";
import {AiFillDelete } from 'react-icons/ai';
import React, { useState } from 'react'

export default function Registration({ name, description, image_address, id }) {
    const [isDelete, setIsDelete] = useState("")
    try{
        if (isDelete != "") {
            var data = {
                "name": name
              };
            fetch('http://localhost:8000/graph/delete', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(data)
              })
                .then(function (response) {
                  if (response.ok) {
                    console.log('Post deleted successfully');
                  } else {
                    console.log('Error deleting post');
                  }
                })
                .catch(function (error) {
                  console.log('Error:', error);
                });
        }
    } catch (error) {
        
    }

    return (
        <div className="flex pl-2 py-4 pr-6 bg-componentes w-5/6 h-12 rounded-lg my-4 flex justify-between">
            <span style={{ cursor: 'pointer' }} className="text-primary">
                {name}
            </span>
            <div className="flex gap-x-4">
                <Pop_up_edit name={name} description={description} image={image_address} id={id} />           
                <button className="redhover" onClick={() => setIsDelete(name)}><AiFillDelete /></button>     
            </div>

        </div>
    );
}

import React, { useState, useEffect } from 'react';
import Modal from 'react-modal';
import { AiOutlineClose, AiOutlineMinus, AiFillDelete } from 'react-icons/ai';
import { Plus } from 'react-bootstrap-icons';

function SendSupabase() {
  // Your Supabase URL and Key
  const supabaseUrl = 'https://exwsjbueckvbqbvtahzr.supabase.co';
  const supabaseKey = 'YOUR_SUPABASE_KEY';

  // Function to send the image to Supabase
  const sendImageToSupabase = async (file) => {
    const formData = new FormData();
    formData.append('image', file);

    const response = await fetch(`${supabaseUrl}/upload`, {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      const imageUrl = data.url; // URL of the uploaded image
      // Do something with the image URL (e.g., store it in state)
      console.log('Image URL:', imageUrl);
    } else {
      console.error('Failed to upload image to Supabase');
    }
  };

  // Rest of your component code...

  return (
    // Your component JSX...
  );
}

export default SendSupabase;

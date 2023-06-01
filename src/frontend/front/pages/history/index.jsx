import Header from '../../components/Header'
import Insp_H from '@/components/Insp_H';
import Searchh from '@/components/Search';
<<<<<<< HEAD
import { useEffect, useState } from 'react';

export default function History() {
  const [cards, all_cards] = useState([]);
  const get_all_cards = async (url) =>{
      const res = await fetch(url);
      const data = await res.json();
      console.log(data)
      all_cards(data.results);
  };
  useEffect(() =>{
          /*let url = "http://127.0.0.1:5000"
          get_all_cards(url+"/routine")*/
          let url = 'https://randomuser.me/api/'
          get_all_cards(url)
      },[]);
  return (
    <div className='w-full h-full bg-cinza'>
      <Header />
      <div className="w-screen h-fit my-12 flex items-center justify-center">
        <div className='w-11/12 pb-90 rounded-md h-5/6 bg-azul flex flex-col items-center justify-center'>
          <span className='mt-12 text-white mb-10 text-3xl font-bold'>Histórico de Inspeções</span>
          <div className=' mb-10'>
            <Searchh />
          </div>
          <div className="insp_h">
            {cards.length > 0 && cards.map(card =>
                <Insp_H number={card.email} name={card.phone} data={card.cell} /> 
              )}
=======

export default function History() {
  return (
    <div className='w-full h-full bg-cinza'>
      <Header />
      <div class="w-screen h-fit my-12 flex items-center justify-center">
        <div className='w-11/12 pb-90 rounded-md h-5/6 bg-azul flex flex-col items-center justify-center'>
          <span class='mt-12 text-white mb-10 text-3xl font-bold'>Histórico de Inspeções</span>
          <div class=' mb-10'>
            <Searchh />
          </div>
          <div class="insp_h">
           
            <Insp_H
              name="Camara a vaco Norte"
              number="Projetp 02"
              data="22/23/2002"
            />

            <Insp_H
              name="Camara a vaco Norte"
              number="Projetp 03"
              data="22/23/2002"
            />

            <Insp_H
              name="Camara a vaco Norte"
              number="Projetp 04"
              data="22/23/2002"
            />

            <Insp_H
              name="Camara a vaco Norte"
              number="Projetp 03"
              data="22/23/2002"
            />

            <Insp_H
              name="Camara a vaco Norte"
              number="Projetp 04"
              data="22/23/2002"
            />

>>>>>>> parent of 96cb9c4 (...)
            </div>
        </div>
      </div>
    </div>
  );
<<<<<<< HEAD
}
=======
}
>>>>>>> parent of 96cb9c4 (...)

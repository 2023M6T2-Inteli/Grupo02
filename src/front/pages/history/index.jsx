import Header from '../../components/Header'
import Insp_H from '@/components/Insp_H';
import SearchBar from '@/components/Search';
import { useEffect, useState } from 'react';

export default function History() {
  const [cards, all_cards] = useState([]);
  useEffect(() => {
    let url = "http://127.0.0.1:8000/register/id/1"
    // let url = 'https://jsonplaceholder.typicode.com/todos/'
    get_all_cards(url)
  }, []);
  const get_registers = async (url) => {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    all_cards(data);
  }
  const get_all_cards = async (url) => {
    const res = await fetch(url);
    const data = await res.json();
    console.log(data)
    all_cards(data);
  };
  return (
    <div className='w-full h-full bg-cinza'>
      <Header />
      <div className="w-screen h-fit my-12 flex items-center justify-center">
        <div className='w-11/12 pb-90 rounded-md h-5/6 bg-azul flex flex-col items-center justify-center'>
          <span className='mt-12 text-white mb-10 text-3xl font-bold'>Histórico de Inspeções</span>
          <div className=' mb-10'>
            <SearchBar />
          </div>
          <div className="insp_h">
            {cards.length > 0 && cards.map(card =>
              <Insp_H number={card.date} name={card.name} data={card.description} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
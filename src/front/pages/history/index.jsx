import Header from '../../components/Header'
import Insp_H from '@/components/Insp_H';
import SearchBar from '@/components/Search';
import { useEffect, useState } from 'react';

export default function History() {
  const [registers, set_register] = useState([]);
  useEffect(() => {
    let url = "http://127.0.0.1:8000/register/get_all"

    get_registers(url)
  }, []);
  const get_registers = async (url) => {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    set_register(data);
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
            {registers.length > 0 && registers.map(register =>
              <Insp_H number={register.date} name={register.name} data={register.description} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
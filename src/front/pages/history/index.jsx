import Header from '../../components/Header'
import Insp_H from '@/components/Insp_H';
// import SearchBar from '@/components/Search';
import { Search } from "react-bootstrap-icons";
import { useEffect, useState } from 'react';

export default function History() {
  const [registers, set_register] = useState([]);
  const [filteredList, setFilteredList] = useState(registers);

  const filterBySearch = (event) => {
    const query = event.target.value;

    var updatedList = [...registers];
    updatedList = updatedList.filter((item) => {
      item = item.name
      return item.toLowerCase().indexOf(query.toLowerCase()) !== -1;
    });
    setFilteredList(updatedList);
  }

  useEffect(() => {
    let url = "http://127.0.0.1:8000/register/get_all"

    get_registers(url)
  }, []);
  const get_registers = async (url) => {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    set_register(data);
    setFilteredList(data);

  };
  return (
    <div className='w-full h-full bg-cinza'>
      <Header />
      <div className="w-screen h-fit my-12 flex items-center justify-center">
        <div className='w-11/12 pb-90 rounded-md h-5/6 bg-azul flex flex-col items-center justify-center'>
          <span className='mt-12 text-white mb-10 text-3xl font-bold'>Histórico de Inspeções</span>
          <div className=' mb-10'>
            {/* <input className="text-sm font-inter w-5/6 pl-4" placeholder="Pesquise por ID do espaço confinado" onChange={filterBySearch} /> */}
            {/* <SearchBar filter={filterBySearch} /> */}
            <div className="bg-gray-50  py-2 pl-1 rounded-full flex justify-between text-primary">
              <input className="text-sm font-inter w-5/6 pl-4" placeholder="Busca por nome do registro" onChange={filterBySearch} />
              <button className="w-8">
                <Search />
              </button>
            </div>

          </div>
          <div className="insp_h">
            {filteredList.length > 0 && filteredList.map(register =>
              <Insp_H number={register.date} name={register.name} data={register.description} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
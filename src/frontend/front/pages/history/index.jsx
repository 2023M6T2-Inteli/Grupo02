import Header from '../../components/Header'
import Insp_H from '@/components/Insp_H';
import Searchh from '@/components/Search';

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



            </div>
        </div>
      </div>
    </div>
  );
}

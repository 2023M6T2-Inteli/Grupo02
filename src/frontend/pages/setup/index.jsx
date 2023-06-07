import { useState, useEffect } from "react"
import Registration from "@/components/Registration";
import NewRoute from "@/components/NewRoute";
import SearchBar from "@/components/Search";
import Header from "@/components/Header";

const route_id = [
  { id: "K2WW0PJN3" },
  { id: "1KA88J102G" },
  { id: "0M9KL2S15" },
  { id: "B6Z11L9M3" },
  { id: "L099D2FA1M" }
];

const imageMapping = {
  K2WW0PJN3: "https://www.previnsa.com.br/wp-content/uploads/2017/06/93495-trabalho-em-espaco-confinado-o-que-eu-preciso-saber.jpg",
  "1KA88J102G": "https://c-safety.com.br/wp-content/uploads/2020/12/aluguel-de-equipamentos-para-espacos-confinados-no-rj.png",
  "0M9KL2S15": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgmbPh7UlRXoUYF2T9nHCVn3BxsJgKfBakwA&usqp=CAU",
  B6Z11L9M3: "https://www.nederman.com/-/media/nederman-br/cases-images/espacos-confinados---nederman.png?h=420&la=pt-BR&w=710&rev=d7332e169eb248d58f5c46459c230c75&crop=1&hash=106621108E6BADF5340554EBEAD17C3C",
  L099D2FA1M: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYhrKBwDjtUEPUqgfOoQtopg1sjXO73P2Gyg&usqp=CAU"
};

// import axios from "axios"

export default function Inspection() {
  const [graphs, setGraphs] = useState([])
  const [selectedRoute, setSelectedRoute] = useState('');

  useEffect(() => {

    let url = "http://localhost:8000/graph/get_all"

    getGraphs(url)
  }, []);

  const getGraphs = async (url) => {
    // const config = {
    //   headers: {
    //     "Access-Control-Allow-Origin": "*",
    //     "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS"
    //   }
    // }
    // const response = await axios(url).catch((err) => console.log("Error: ", err))
    const response = await fetch(url);
    //get the data from the response
    const data = await response.json();
    //set the state of the graphs

    console.log(data)

    setGraphs(data)
  }

  const handleRouteClick = (routeId) => {
    setSelectedRoute(routeId);
  };

  return (
    <div className="bg">
      <Header />
      <div className="flex ml-16 mr-16 mb-16">
        <div className="mt-16 pt-10 pl-10 pb-8 w-2/5 bg-azul rounded-lg">
          <div className="font-inter text-white">
            <p>Selecione o espaço confinado que deseja inspecionar.</p>
          </div>
          <div className="mt-4">
            <SearchBar />
          </div>
          <div className="mt-6 mb-6">
            <NewRoute />
          </div>
          {graphs.map(json => (
            <div
              key={json.id}
              className="mt-4 text-primary content-center"
              onClick={() => handleRouteClick(json.id)}
            >
              <Registration id={json.name} />
            </div>
          ))}
        </div>

        <div className="grid w-3/5">
          <div className="ml-16 mt-16 mb-80 bg-azul rounded-lg h-full">
            <div className="font-inter text-white pt-10 pl-10">
              {!selectedRoute && (<p>Selecione um espaço confinado para visualizar uma prévia de sua rota.</p>)}
              {selectedRoute && (<img src={imageMapping[selectedRoute]} />
              )}
            </div>
          </div>
          <div className="ml-16 mt-24 bg-azul rounded-lg">
            <div className="font-inter text-white pt-10 pl-10">
              <p>Iniciar inspeção</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

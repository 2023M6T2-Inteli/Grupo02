import { useState, useEffect } from 'react';
import axios from "axios"
import Registration from "@/components/Registration";
import NewRoute from "@/components/NewRoute";
import SearchBar from "@/components/Search";
import Header from "@/components/Header";
<<<<<<< HEAD
const imageMapping = {
  K2WW0PJN3: "https://www.previnsa.com.br/wp-content/uploads/2017/06/93495-trabalho-em-espaco-confinado-o-que-eu-preciso-saber.jpg",
  "1KA88J102G": "https://c-safety.com.br/wp-content/uploads/2020/12/aluguel-de-equipamentos-para-espacos-confinados-no-rj.png",
  "0M9KL2S15": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgmbPh7UlRXoUYF2T9nHCVn3BxsJgKfBakwA&usqp=CAU",
  B6Z11L9M3: "https://www.nederman.com/-/media/nederman-br/cases-images/espacos-confinados---nederman.png?h=420&la=pt-BR&w=710&rev=d7332e169eb248d58f5c46459c230c75&crop=1&hash=106621108E6BADF5340554EBEAD17C3C",
  L099D2FA1M: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYhrKBwDjtUEPUqgfOoQtopg1sjXO73P2Gyg&usqp=CAU"
};
export default function Inspection(){
    console.log("renderizou")
    const [graphs, setGraphs] = useState([])
    const [selectedRoute, setSelectedRoute] = useState('');
    useEffect(() => {
        let url = "http://localhost:8000/graph/get_all"
        getGraphs(url)
    },[])
    const getGraphs = async (url) => {
        const response = await axios(url).catch((err) => console.log("Error: ", err))
        //get the data from the response
        const data = response.data
        //set the state of the graphs
        console.log(data)
        setGraphs(data)
    }
  const handleRouteClick = (routeId) => {
    setSelectedRoute(routeId);
=======


export default function Inspection() {
  const [graphs, setGraphs] = useState([])
  const [selectedGraph, setSelectedGraph] = useState('');

  useEffect(() => {

    let url = "http://localhost:8000/graph/get_all"

    getAllGraphs(url)
  }, []);

  const getAllGraphs = async (url) => {

    const all_graphs = await fetch(url);

    const data = await all_graphs.json();

    console.log(data)

    setGraphs(data)
  }

  const handleRouteClick = (imageAddress, name) => {
    setSelectedGraph({
      'image': imageAddress,
      'name': name
    });
>>>>>>> 8bafb163b2a34169447e2f4aeac95d0a6d8cf17f
  };
  return (
    <div className="bg bg-cinza w-screen h-screen">
      <Header />
      <div className="flex ml-16 mr-16 mb-16">
<<<<<<< HEAD
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
                <Registration id={json.id} name={json.name} description={json.description} image={json.image_address} />
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
              <div className="font-inter text-white pt-10 pl-10 flex justify-between">
                <p>Iniciar inspeção</p>
                <a href="/running">---</a>
              </div>
            </div>
=======
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
          {graphs.map(graph => (
            <div
              key={graph.id}
              className="mt-4 text-primary content-center"
              onClick={() => handleRouteClick(graph.image_address, graph.name)}
            >
              <Registration name={graph.name} description={graph.description} image_address={graph.image_address} nodes={graph.nodes} />
            </div>
          ))}
        </div>
        <div className="grid w-3/5" >
          <div className="ml-16 mt-16 bg-azul rounded-lg h-full pl-10 pt-2 pr-10">
            <h3 className="text-white text-center">{selectedGraph.name}</h3>
            {selectedGraph && (<img className="border-2" src={selectedGraph.image} />)}
            {!selectedGraph && (<div className="font-inter text-white pt-10 pl-10">Selecione um espaço confinado para visualizar uma prévia de sua rota.</div>)}
          </div>

          <div className="ml-16 mt-24 bg-azul rounded-lg h-1/2">
            <a href="/running">
              <div className="font-inter text-white flex justify-between">
                <p className="">Iniciar inspeção</p>
              </div>
            </a>
>>>>>>> 8bafb163b2a34169447e2f4aeac95d0a6d8cf17f
          </div>
      </div>
    </div>
  );
}
<<<<<<< HEAD
import { useState, useEffect } from 'react';
import axios from "axios"
=======
import { useState, useEffect } from "react"
>>>>>>> Dev
import Registration from "@/components/Registration";
import NewRoute from "@/components/NewRoute";
import SearchBar from "@/components/Search";
import Header from "@/components/Header";


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

  const handleRouteClick = (imageAddress) => {
    setSelectedGraph(imageAddress);
  };

  return (
    <div className="bg bg-cinza w-screen h-screen">
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
          {graphs.map(graph => (
            <div
              key={graph.id}
              className="mt-4 text-primary content-center"
              onClick={() => handleRouteClick(graph.image_address)}
            >
              <Registration name={graph.name} description={graph.description} image_address={graph.image_address} nodes={graph.nodes} />
            </div>
          ))}
          <div className="mt-4">
            <SearchBar />
          </div>
          <div className="mt-6 mb-6">
            <NewRoute />
          </div>

          < div className="grid w-3/5" >
            <div className="ml-16 mt-16 mb-80 bg-azul rounded-lg h-full">
              {!selectedGraph && (<div className="font-inter text-white pt-10 pl-10">Selecione um espaço confinado para visualizar uma prévia de sua rota.</div>)}
              {selectedGraph && (<img className="pt-10" src={selectedGraph} />)}
              <div className="ml-16 mt-24 bg-azul rounded-lg">
                <div className="font-inter text-white pt-10 pl-10 flex justify-between">
                  <p>Iniciar inspeção</p>
                  <a href="/running">---</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div >
  );
}
